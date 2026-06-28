---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-11_attacking-rdp-from-inside-how-we-abused-named-pipes-for-smart-card-hijacking-una.md
original_filename: 2022-01-11_attacking-rdp-from-inside-how-we-abused-named-pipes-for-smart-card-hijacking-una.md
title: 'Attacking RDP from Inside: How we abused named pipes for smart-card hijacking,
  unauthorized file system access to client machines and more'
category: documents
detected_topics:
- access-control
- command-injection
- mfa
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- mfa
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 53bd1a187feb8161c585dac10025f116c9645bdda740cd18a30bbb613ce3e128
text_sha256: 5a2947c31662d5116c59f923b4a94a0412695170ee9ad601fc191192afa8ee11
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking RDP from Inside: How we abused named pipes for smart-card hijacking, unauthorized file system access to client machines and more

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-11_attacking-rdp-from-inside-how-we-abused-named-pipes-for-smart-card-hijacking-una.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `53bd1a187feb8161c585dac10025f116c9645bdda740cd18a30bbb613ce3e128`
- Text SHA256: `5a2947c31662d5116c59f923b4a94a0412695170ee9ad601fc191192afa8ee11`


## Content

---
title: "Attacking RDP from Inside: How we abused named pipes for smart-card hijacking, unauthorized file system access to client machines and more"
page_title: "Attacking RDP from Inside: How we abused named pipes for smart-card hijacking, unauthorized file sys"
url: "https://www.cyberark.com/resources/threat-research-blog/attacking-rdp-from-inside"
final_url: "https://www.cyberark.com/resources/threat-research-blog/attacking-rdp-from-inside"
authors: ["Gabriel Sztejnworcel (@sztejnworcel)"]
programs: ["Microsoft"]
bugs: ["RCE"]
publication_date: "2022-01-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3015
---

# Attacking RDP from Inside: How we abused named pipes for smart-card hijacking, unauthorized file system access to client machines and more

January 11, 2022 Gabriel Sztejnworcel

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fattacking-rdp-from-inside)
  * [Twitter](https://twitter.com/share?text=Attacking%20RDP%20from%20Inside%3A%20How%20we%20abused%20named%20pipes%20for%20smart-card%20hijacking%2C%20unauthorized%20file%20sys...&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fattacking-rdp-from-inside&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#2b14585e49414e485f166844455f4e455f0e191b4d5944460e191b46520e191b635e490e191a0d4a465b1049444f521668434e48400e191b445e5f0e191b5c434a5f0e191c580e191b434a5b5b4e4542454c0e191b4a5f0e191b6852494e596a59400e191a0e1b6a0e1b6a6a5f5f4a484042454c0e191b796f7b0e191b4d5944460e191b624558424f4e0e186a0e191b63445c0e191b5c4e0e191b4a495e584e4f0e191b454a464e4f0e191b5b425b4e580e191b4d44590e191b58464a595f06484a594f0e191b4342414a484042454c0e19680e191b5e454a5e5f43445942514e4f0e191b4d42474e0e191b5852585f4e460e191b4a48484e58580e191b5f440e191b4847424e455f0e191b464a484342454e580e191b4a454f0e191b4644594e0e1b6a62450e191b5f4342580e191b4947444c0e191b5b44585f0e191b5c4e0e191b4a594e0e191b4c4442454c0e191b5f440e191b4f4258485e58580e191b5f434e0e191b4f4e5f4a4247580e191b444d0e191b4a0e191b5d5e47454e594a494247425f520e191b42450e191b7c42454f445c580e191b794e46445f4e0e191b6f4e58405f445b0e191b784e595d42484e580e19680e191b5c434248430e191b5c4e0e191b594e484e455f47520e191b5e4548445d4e594e4f050e191b7c4e0e191b594e5b44595f4e4f0e191b5f434e0e191b5d5e47454e594a494247425f520e191b5f440e191b664248594458444d5f0e191b42450e191b4a0505050e1b6a0e1b6a435f5f5b580e186a0e196d0e196d5c5c5c054852494e594a5940054844460e196d594e58445e59484e580e196d5f43594e4a5f06594e584e4a594843064947444c0e196d4a5f5f4a484042454c06594f5b064d59444606424558424f4e)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fattacking-rdp-from-inside&title=Attacking%20RDP%20from%20Inside%3A%20How%20we%20abused%20named%20pipes%20for%20smart-card%20hijacking%2C%20unauthorized%20file%20system%20access%20to%20client%20machines%20and%20more&summary=In%20this%20blog%20post%20we%20are%20going%20to%20discuss%20the%20details%20of%20a%20vulnerability%20in%20Windows%20Remote%20Desktop%20Services%2C%20which%20we%20recently%20uncovered.%20We%20reported%20the%20vulnerability%20to%20Microsoft%20in%20a...)

![](https://www.cyberark.com/wp-content/uploads/2022/01/tsk-hero.jpeg)

In this blog post we are going to discuss the details of a vulnerability in Windows Remote Desktop Services, which we recently uncovered. We reported the vulnerability to Microsoft in a coordinated disclosure process. Microsoft has released a fix in the latest security update and the vulnerability is now identified as [CVE-2022-21893](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21893).

### TL;DR

This vulnerability enables any standard unprivileged user connected to a remote machine via remote desktop to gain file system access to the **client machines** of other connected users, to view and modify clipboard data of other connected users, and to impersonate the identity of other users logged on to the machine using smart cards. This could lead to data privacy issues, lateral movement and privilege escalation.

The latest versions of Windows (client and server editions) are affected by this vulnerability, and it goes back at least to Windows Server 2012 R2, so we can say that the majority of Windows versions in use today are affected.

Let’s dive in.

### Start with Some Background: RDP Virtual Channels

The Remote Desktop Protocol (RDP) splits a single connection into multiple logical connections called virtual channels for handling different types of data. Some channels are responsible for the core functionality of RDP, such as graphical and input data, while other channels handle protocol extensions, such as clipboard, drive and printer redirection. There is also an [API](https://docs.microsoft.com/en-us/windows/win32/api/wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex) for working with virtual channels which allows writing an application that communicates with RDP clients over custom virtual channels. This [blog post](https://www.cyberark.com/resources/threat-research-blog/explain-like-i-m-5-remote-desktop-protocol-rdp) contains a great introduction to the RDP protocol.

While some channels are handled by the Remote Desktop Services (RDS) service, which is implemented as a DLL hosted in svchost.exe, others are handled by other processes. For example, the clipboard redirection channel (CLIPRDR) is handled by the rdpclip.exe process which executes separately for each connected user, running under its privileges. The virtual channel data is passed between these processes and the RDS service over Windows named pipes.

### Short Introduction to Windows Named Pipes

Named pipes are one of the most common ways for interprocess communication in Windows and work in a client/server model. The named pipe server is created using the [CreateNamedPipe](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-createnamedpipea) function, and clients connect to it using the [CreateFile](https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea) function. Both sides specify the name of the pipe, which is in the following format: \\\\.\pipe\name (for the server or for a client that connects to a local named pipe) or \\\hostname\pipe\name (for a client that connects to a remote named pipe). Once the connection is established, the client and the server use the [WriteFile](https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-writefile) and [ReadFile](https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile) functions to exchange data.

One of the key concepts for understanding this vulnerability and the named pipes attack surface in general is pipe server instances. It is common to have one server process that handles multiple clients. This is achieved by creating multiple pipe server instances, meaning that the server process will call CreateNamedPipe multiple times with the same pipe name. Each time it will get a new server instance. When a client connects to a named pipe server, it connects to one instance. If there are multiple instances available, the client will connect to the one that was created first (FIFO ordering).

Since each call to CreateNamedPipe is independent, it’s also possible for different processes, possibly malicious, to create pipe server instances of the same name. Combining this with the FIFO behavior, we can start to see how this can lead to several issues. So how can we prevent other processes from creating server instances for our named pipes? Well, a named pipe is a securable object; it has a security descriptor that contains access control lists. One of the parameters of CreateNamedPipe is a security attributes object that contains the security descriptor. So whenever using named pipes, it’s important to think about the permissions – who is allowed to access this pipe and how – and pass the security attributes object accordingly. It’s also important to verify that no other process has created a pipe server instance with the same name before we did, unless it’s a valid use case. In that case, the security descriptor would be set. This can be achieved by specifying FILE_FLAG_FIRST_PIPE_INSTANCE in the call to CreateNamedPipe. You can find more information about named pipes and their attack surface in this detailed [blog post](https://csandker.io/2021/01/10/Offensive-Windows-IPC-1-NamedPipes.html).

### Start Putting it Together: Virtual Channel Named Pipes

As we mentioned, processes that handle virtual channels use named pipes for passing the virtual channel data to and from the RDS service. The name of this pipe is “TSVCPIPE-” followed by a GUID.

![Virtual channel communication between rdpclip.exe, RDS and the RDP client](https://www.cyberark.com/wp-content/uploads/2022/01/proc-rds-client-comm.png)

_Figure 1: Virtual channel communication between rdpclip.exe, RDS and the RDP client_

The GUID is generated once by the service and used for all sessions. Restart the service, and you will get a new GUID. While the service is running all sessions will always have pipe instances with the same GUID. So once connected via RDP, we can just list the open pipes on the machine, which is something that every user can do, and see the pipe with its full name.

![](https://www.cyberark.com/wp-content/uploads/2022/01/pipelist-wide.png)

_Figure 2: Output of Sysinternals’[pipelist](https://docs.microsoft.com/en-us/sysinternals/downloads/pipelist) utility showing the TSVCPIPE pipe_

### The Vulnerability

A process can create pipe server instances with the name of an existing pipe server if the security descriptor of the first instance allows it. It turns out that the TSVCPIPE security descriptor **allows any user to create pipe server instances** of the same name. Moreover, the data is sent over the pipes in clear text and without any integrity checks.

### The Basic Attack

The vulnerability makes the following attack scenario possible:

  1. An attacker connects to a remote machine via RDP
  2. The attacker lists the open named pipes and finds the full name of the TSVCPIPE pipe
  3. The attacker creates a pipe server instance with the same name and waits for a new connection
  4. Once a new connection arrives, RDS creates its own pipe server instance for the session and a pipe client that will attempt to connect to it
  5. Because of the FIFO, the pipe client will connect to the attacker pipe server instance instead of the one created by the RDS service
  6. The attacker connects as a client to the real RDS pipe server instance
  7. The attacker holds both ends of the connection; they can act as man-in-the-middle, passing the data back and forth, viewing and (optionally) modifying it

![MiTM process intercepting the TSVCPIPE communication](https://www.cyberark.com/wp-content/uploads/2022/01/tsvcpipe-mitm.png)

_Figure 3: MiTM process intercepting the TSVCPIPE communication_

We have implemented a tool that performs these steps to create a man-in-the-middle that prints the data passing through the pipes. As you can see in the following demonstration video, among other things we are able to see clipboard data. This can be images, files or text that might contain personal data or sensitive data such as passwords, which is often the case in RDP sessions.

![](https://fast.wistia.com/embed/medias/jajlp7p1ab/swatch)

_Video 1: Clipboard Interception_

### Taking it a Step Further: Access Other Users’ Redirected Drives

The initial tool just prints out raw data. This is great for demonstrating the issue but going over the raw data without knowing what we are looking for is tedious and impractical. We would like to have something that does more than that. As we said in the beginning, there are several channels that use these pipes, each with its own protocol. We have decided to target the device redirection channel (RDPDR). Our goal is to access the victim’s redirected drives and folders in a convenient way.

### The RDPDR Channel

The RDPDR channel is used for redirecting devices such as drives and smart cards from the client machine to the remote session. On the remote machine, the channel is handled by a filesystem driver that communicates with RDS over the TSVCPIPE pipe. Here’s a brief introduction to the protocol.

![](https://www.cyberark.com/wp-content/uploads/2022/01/rdpdr-wide-1.png)

_Figure 4: RDPDR initialization sequence from the protocol[specification](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpefs/34d9de58-b2b5-40b6-b970-f82d4603bdb5)_

The server starts the protocol sequence with a Server Announce Request. The client then responds with a Client Announce Reply and a Client Name Request, passing the client computer name. The client and server then exchange capabilities. Afterward, the client sends a Client Device List Announce Request, passing a list of all devices they want to redirect. The server responds with a Server Device Announce Response for each one of the devices. Once the connection is established, the client and server start exchanging data by sending Device I/O Requests. At each point, the server can send a new Server Announce Request, which will re-initiate the protocol sequence.

### Attacking the RDPDR Pipe

To recall, the victim’s pipe client running in the RDPDR filesystem driver is connected to the pipe server in our MiTM process, while we have a pipe client connected to the victim’s pipe server in the RDS service. We could just send our own crafted I/O requests from our pipe client to the victim’s pipe server, which will be forwarded to the client machine over the RDP connection. This seems possible but will require implementing almost the entire protocol. We chose to do something else: As the attacker is also connected via RDP, they have their own pipe instances. If we could make our (the attacker) pipe instances go through our MiTM tool, we could just connect the pipe client running in the filesystem driver for the attacker session to the pipe server running in RDS for the victim session. This way, the attacker should be able to see the victim’s drives (in file explorer, for example) as if they were connected to their client machine.

![Change Handles](https://www.cyberark.com/wp-content/uploads/2022/01/tsvcpipe-change-handles.png)

_Figure 5: Change Handles_

Since the attacker connects to the machine and only then runs the MiTM process, their pipes are not connected to it. So how can we get the attacker pipes to connect to the MiTM process? That’s easy. We could, for example, start a new session for the attacker, but we chose to use the session reconnection feature of Remote Desktop. If a user disconnects from a session, the session is maintained for a certain period, and if the same user connects to the machine again, it will reconnect to the same session. While the session is in disconnected state, the processes continue to run. So, we only need to close the RDP client and connect with the same user again to reconnect to the same session. Upon reconnection, the pipes will be recreated but this time the MiTM process will catch them, allowing us to change the pipe handles (the objects that point to the actual pipe objects in the Windows kernel. As part of the connection, the filesystem driver of the attacker session will start the RDPDR protocol initialization sequence, sending a Server Announce Request. We will forward this request to the victim, which will make it re-initialize the protocol – but this time with the attacker session. We have successfully implemented this technique. Here’s a video demonstrating the attack:

![](https://fast.wistia.com/embed/medias/5cs5oi1j0u/swatch)

_Video 2: Drive Redirection_

### The Grand Finale: Hijacking Smart Cards

Smart card redirection also uses the RDPDR channel; it is just another device. This means that if a user connects using a smart card (or just redirects their smart card to use it from within the session), the attacker could also take over the user’s smart card and use it as if it were connected to their machine. When the victim enters their smart card PIN number, an IO control request is sent to the smart card over the channel with the PIN number in clear text, so the attacker can see it. The attacker can now connect to**any resource, on the same machine or on other machines** , using the victim’s smart card and PIN number, effectively impersonating the victim’s security context. In case the victim logs in with a privileged account, this leads to **privilege escalation**. The following video demonstrates the smart card attack:

![](https://fast.wistia.com/embed/medias/k731548uyx/swatch)

_Video 3: Smart Card Redirection_

### Summary

This vulnerability shows an example of an unconventional attack vector targeting RDP. Instead of tapping into the input side of the server/client as one usually does, we abused the RDP server internal mechanism as an entry point.

We chose to focus on drive and smart card redirection. We believe that we could also apply the same technique to other types of devices, protocols and channels, such as printers, audio, USB devices and authentication redirection (Remote Credential Guard).

As mentioned above, we reported the issue to Microsoft and they have released a patch to fix the issue. We strongly recommend applying this patch (almost all Windows versions are affected). **Also, developers of applications that use custom virtual channels should check whether they are vulnerable and conduct their own security assessment.**

For more information on Microsoft’s patch, please visit <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21893>.

### Disclosure Timeline

08/19/2021 – Vulnerability reported to Microsoft with the initial POC  
08/25/2021 – Microsoft acknowledged the reported behavior  
09/01/2021 – Microsoft shared their severity assessment. The vulnerability is rated “Important”  
09/12/2021 – Updated Microsoft regarding the RDPDR scenario and sent a new POC  
12/29/2021 – Microsoft assigned CVE-2022-21893  
01/11/2022 – Microsoft released a patch fixing the issue

We would like to share our appreciation to Microsoft Security Response Center for their cooperation.

**Editor’s note**(April 12, 2022)**:**

_Today, Microsoft[published a new CVE](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24533) – CVE-2022-24533 – and patch related to the vulnerability that we addressed in this blog post. We are engaging in additional testing and evaluation of this mitigation, and will publish our findings in an upcoming post. Stay tuned! _

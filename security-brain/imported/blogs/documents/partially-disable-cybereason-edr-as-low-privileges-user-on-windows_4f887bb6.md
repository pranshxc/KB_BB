---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-28_partially-disable-cybereason-edr-as-low-privileges-user-on-windows.md
original_filename: 2022-10-28_partially-disable-cybereason-edr-as-low-privileges-user-on-windows.md
title: Partially disable Cybereason EDR as low privileges user on Windows
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 4f887bb6a603b2c033be8c27fc3b0a91a3bfb846914cf8544bf34994b8851d1a
text_sha256: bef1bc56f0cd9b64f646a33405a26920100c7a52cd4d67aea395773802a6f1d5
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Partially disable Cybereason EDR as low privileges user on Windows

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-28_partially-disable-cybereason-edr-as-low-privileges-user-on-windows.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `4f887bb6a603b2c033be8c27fc3b0a91a3bfb846914cf8544bf34994b8851d1a`
- Text SHA256: `bef1bc56f0cd9b64f646a33405a26920100c7a52cd4d67aea395773802a6f1d5`


## Content

---
title: "Partially disable Cybereason EDR as low privileges user on Windows"
url: "https://medium.com/@mehdi.alouache/partially-disable-cybereason-edr-as-low-privileges-user-on-windows-1405fd53e90e"
authors: ["Mehdi Alouache"]
programs: ["Cybereason"]
bugs: ["EDR bypass", "Local Privilege Escalation"]
publication_date: "2022-10-28"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 3833
scraped_via: "browseros"
---

# Partially disable Cybereason EDR as low privileges user on Windows

Partially disable Cybereason EDR as low privileges user on Windows
Mehdi Alouache
Follow
4 min read
·
Oct 28, 2022

7

Update on December 6th, 2022 : Cybereason investigated and wanted to exercise their right to answer. They noticed anti-tampering was not enabled on my test tenant, so they activated it. Since then, it is not possible to kill any probes except NNX.exe, which doesn’t seem related to detection capabilities, but only needed for less important features.

EDR — Endpoint Detection & Response — has been a trending topic in cybersecurity since the last decade. Among the biggest players of this industry sits Cybereason, top performer of the MITRE ATT&CK evaluation of 2022, making it a good candidate for your security posture.

However, from an attacker point of view, how can you get rid of some of its detection capabilities ? Let’s see…

This article is not meant to bash on Cybereason. However, they do not offer any kind of public bug bounty program, so I felt free to write a short article here about what seems to be a flaw in the repair mechanism of the solution.

Please note I don’t have the full details of the roles of each loader and probe, as those details belong to Cybereason. Some parts of the presentation may be inaccurate.

Cybereason, and all EDR solutions in an extent, are designed to be unalterable. As attackers, we all have faced a pentest where we were able to remotely disable a classical antimalware (such as Defender) with a PsExec invocation as NT AUTHORITY\SYSTEM. However this kind of method will not be useful agaisnt Cybereason, because nothing can uninstall or (permanently) disable Cybereason except Cybereason itself.

That being said, can we politely ask Cybereason to disable itself ?

Cyberason probes

Depending on the actives modules running, a number of different processes can be spawned by Cybereason, acting as probes to detect and prevent some threats.

Press enter or click to view image in full size

In red, what I believe to be the initial loader. The CrAmTray.exe process is run is each user context, probably the GUI part of Cybereason.

In blue, some of the probes responsible for detection and or prevention. These are our target.

Killing some probes

As mentioned before :

nothing can uninstall or (permanently) disable Cybereason except Cybereason itself

Like many other Windows programs, Cybereason offers a GUI to repair itself or uninstall itself. The uninstallation requires a token to guarantee only an EDR administrator can remove it. But anyone can run the repair part.

Get Mehdi Alouache’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s run it.

Press enter or click to view image in full size

In Windows application manager, select “Modify” on Cybereason

“Do you want to authorize this application to modify settings on your device ?”

Agree on running Cybereason.exe /modify

Run a Repair.

It will run until it waits for a while at “stopPylumLoader”. PylumLoader seems to be the loader for every other service.

Kill Task

As soon as the stopPylumLoader phase ends, kill all Cybereason Sensor processes manually.

Press enter or click to view image in full size

Agent repaired failed, displaying this error. But let’s now give a look to the probes…

Press enter or click to view image in full size

Some of them failed to restart after PylumLoader got killed improperly. The lime green bar displays a process still running, while the dark greens indicates the process was stopped. No other instance of those processes could be found, which means probes actually got stopped and couldn’t restart.

Ony the CrsSvc.exe service was able to stay alive during the manipulation.

Final words

The number of probes running depend of the modules activated. When all of them were running, this manipulation only disabled around 50% of them. I am not certain to be able to determine what they do, like for instance “NNX.exe”. Some are easier to guess, such as Execution Prevention Service.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-06_rediscovering-epic-games-0-days-forever-unpatched.md
original_filename: 2022-07-06_rediscovering-epic-games-0-days-forever-unpatched.md
title: Rediscovering Epic Games 0-Days (Forever Unpatched?)
category: documents
detected_topics:
- sso
- access-control
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- sso
- access-control
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 79601082a6cc48e21ea8126649f31c0317b896c20df0acb00a8b230c98e0bca1
text_sha256: eeccc96649abab51abb118bb6b4d5aea747d0b4d26ba347efd22d10e4f8a724b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Rediscovering Epic Games 0-Days (Forever Unpatched?)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-06_rediscovering-epic-games-0-days-forever-unpatched.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `79601082a6cc48e21ea8126649f31c0317b896c20df0acb00a8b230c98e0bca1`
- Text SHA256: `eeccc96649abab51abb118bb6b4d5aea747d0b4d26ba347efd22d10e4f8a724b`


## Content

---
title: "Rediscovering Epic Games 0-Days (Forever Unpatched?)"
page_title: "Rediscovering Epic Games 0-Days (Forever Unpatched?) | Advanced Offensive Cybersecurity Training"
url: "https://www.signal-labs.com/blog/rediscovering-epic-games-0-days"
final_url: "https://signal-labs.com/rediscovering-epic-games-0-days/"
authors: ["Christopher Vella (@Kharosx0)"]
programs: ["Epic Games"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-07-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2486
---

Skip to content

[ ![Primary Logo | Signal Labs | Advanced Offensive Cybersecurity Training | Self-Paced Trainings | Live Trainings | Virtual Trainings | Custom Private Trainings for Business](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwMCAyMTIiIHdpZHRoPSIxMDAwIiBoZWlnaHQ9IjIxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=) ](https://signal-labs.com)

  * [Trainings](https://signal-labs.com/self-paced-trainings/)
  * [Who We Are](https://signal-labs.com/about/)
  * [Blog](https://signal-labs.com/blog/)
  * [For Business](https://signal-labs.com/business/)
  * [Lesson Samples](https://www.youtube.com/@Signal-Labs)

  * [Trainings](https://signal-labs.com/self-paced-trainings/)
  * [Who We Are](https://signal-labs.com/about/)
  * [Blog](https://signal-labs.com/blog/)
  * [For Business](https://signal-labs.com/business/)
  * [Lesson Samples](https://www.youtube.com/@Signal-Labs)

[ Student Portal ](/student-login/)

[ Enroll Today ](/self-paced-trainings/)

# Rediscovering Epic Games 0-Days (Forever Unpatched?)

## July 6, 2022

## By: Christopher Vella

![Rediscovering Epic Games 0-Days \(Forever Unpatched?\) | Signal Labs | Advanced Offensive Cybersecurity Training | Self-Paced Trainings | Live Trainings | Virtual Trainings | Custom Private Trainings for Business](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTgwMCA2MzUiIHdpZHRoPSIxODAwIiBoZWlnaHQ9IjYzNSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

## How It Started

So one day I was browsing ZDI (usually its the same sort of targets, lots of Foxit bugs, Adobe, Ivanti, etc) and noticed a couple entries by [@izobashi](https://twitter.com/izobashi) ([ZDI-22-537](https://www.zerodayinitiative.com/advisories/ZDI-22-537/), [ZDI-22-538](https://www.zerodayinitiative.com/advisories/ZDI-22-537/)) for Epic Games Launcher, there were two things that stood out:

  1. It wasn’t patched at time of advisory release (which means no patch in 120 days since reporting it, maybe unpatched forever?)
  2. It was file overwrite and file deletion bugs which can be leveraged for LPE, and affected the installer (these bugs are common and very familiar to me)

Now as a gamer (albeit not one with Epic’s launcher installed) I’ve had the displeasure of noting multiple vulnerabilities in gaming related software (alongside a strong dislike for anti-cheats in my kernel or acting as a hypervisor, though I understand why they do), I figured I’d check now if I can find these same bugs in the latest version of Epic’s launcher.

Although we don’t have a PoC or really any detailed information from the ZDI listings, the bugs are familiar enough that we can jump right in with our trusty [ProcMon ](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)and see what we find.

## Finding the bugs

After installing Epic’s launcher I immediately find the installer in C:\Windows\Installer (shh! its a secret directory), I know this is Epic’s MSI due to the signature matching Epic as expected:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTE3NCA0NzQiIHdpZHRoPSIxMTc0IiBoZWlnaHQ9IjQ3NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

The reason bugs in installers are common can be noted to a few factors:

  1. They typically auto-elevate to SYSTEM (even if you’re just a lowly non-administrative user)
  2. They can be executed in install / remove / repair modes that perform various operations, including file operations (copy, rename, delete) and can run arbitrary bundled scripts
  3. People don’t spend security $$$ on hardening their installers? (I don’t know, but it sure seems like it)

Before we go any further, lets configure our ProcMon, but first — why ProcMon?:

  1. Tells us what processes are doing (to an extent) 
  1. What files they’re accessing
  2. What permissions they’re operating at
  3. What files / registry entries they’re reading / writing / deleting
  2. Is filterable 
  1. Write rules to only show / capture what you’re interested in

Now to configure ProcMon, what are we looking for exactly?:

  1. File creation/opening events that satisfy the following: 
  1. Operating on folders or files we can control 
  1. Why? So we can redirect them via symlinks of course 
  1. If it overwrites a file in C:\windows\system32, how would our lowly non-admin user control it?
  2. If it overwrites a file in C:\users\lowly_user\Desktop that we can control, its a different story!
  3. (Or any other location we have write or similar access to)
  2. ?? (There are more potentially interesting events, like paths or files that don’t exist that we may create, etc… but for this exercise we don’t care)

Now you may think if we exclude the following folders, that’d be good enough to meet our requirements above:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTkzNyA5OTUiIHdpZHRoPSIxOTM3IiBoZWlnaHQ9Ijk5NSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

The point of the above is:

  * Capture `CreateFile` and `Load Image` operations
  * Ensure username contains `NT` (e.g. NT SYSTEM)
  * Exclude folders we can’t modify / control: 
  * C:\ProgramData\Microsoft
  * C:\Program Files*
  * C:\Windows\

Can you think what the problem with the above excluded directories is?

..

…

….

Well actually there are multiple (for example, C:\windows\temp is typically user-writable! Meaning we actually can have some control over the contents of this directory, yet in the above filters we exclude it, although this isn’t an issue for this particular example).

The actual issue is excluding all of `C:\Program Files`, because Epic actually applies a permissive DACL on `c:\Program Files (x86)\Epic Games\Launcher` and its subfolders! (Not a great thing to do in general…)

This can be verified with icacls:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNzc1IDEzMCIgd2lkdGg9Ijc3NSIgaGVpZ2h0PSIxMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)

(Tip: Enumerate ACLs on everything -> install software -> enumerate again -> diff!)

Ok so lets ensure the path `C:\Program Files (x86)\Epic Games\Launcher` is included in our procmon filter and start capturing (In this case I’m going to remove the exclude for `C:\Program Files` and specifically include the launcher path above — once we have the trace we can play with the filters to see other interesting events too, like searching for operations that begin with `Set` to see renames, deletions, etc).

Lets right click the .msi file and press `Repair`, wait for it to complete and see if anything interesting happens.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTU3NiA5MTUiIHdpZHRoPSIxNTc2IiBoZWlnaHQ9IjkxNSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

Well that’s a lot.

To be honest its not surprising, the .msi in repair mode is there to, well, “repair” its files (which is typically achieved by replacing them with a pre-packaged good version).

Since the ACLs on this folder are weak, what would happen if we were to redirect one of these files elsewhere?

To test this, I’m going to show the two 0-days, first is the file overwrite.

Lets start by grabbing the [symbolic testing tools from GPZ](https://github.com/googleprojectzero/symboliclink-testing-tools) and compile them.

Now lets turn a folder (in this case, `C:\Program Files (x86)\Epic Games\Launcher\Engine\Binaries\Win32` into a symlink pointing to `\RPC Control`:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAyNCA4MyIgd2lkdGg9IjEwMjQiIGhlaWdodD0iODMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)

(If you can’t delete Win32, try stopping Epic’s running processes first)

Ok now lets try the repair operation again and see what happens.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgODg5IDMxMSIgd2lkdGg9Ijg4OSIgaGVpZ2h0PSIzMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)

Ok so its looking for a DLL in our Win32 folder, however Win32 now points to `\RPC Control` and there doesn’t exist any `\RPC Control\msvcp140_2.dll` for the target to obtain a handle to.

Lets try creating this, and redirecting it to `C:\Windows\System32\License.rtf` as an example, now lets first note the size of our `License.rtf` file:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAyNCAyNTAiIHdpZHRoPSIxMDI0IiBoZWlnaHQ9IjI1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

Ok so yours is likely **not** 7 bytes like mine, but note that mine only allows modification by Administrators or higher, users just have RX.

Now lets create the link to it:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAyNCA2NSIgd2lkdGg9IjEwMjQiIGhlaWdodD0iNjUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)

Now press `Retry` on the msi error, and you’ll notice it continues and pops up another error (for a different DLL!)

However, note that License.rtf has been overwritten!

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNzgzIDE4NiIgd2lkdGg9Ijc4MyIgaGVpZ2h0PSIxODYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)

This is the first 0-day, arbitrary file overwrite!

To ensure this sticks, we can now delete Win32, recreate it as a regular folder (`mkdir Win32`) and press Retry, this should cause the installer to continue without any more errors and leave the file overwritten.

However, we can turn this into an arbitrary deletion vulnerability by causing the target to now delete License.rtf!

We can do this by simply pressing `Cancel` instead of retry! The target MSI will rollback its operations, and this will cause it to delete the overwritten file entirely!

With these two bugs (file overwrite + file deletion) we can actually leverage them for LPE, there’s other posts on achieving this (e.g. <https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks>)

Whos taking bets how long these bugs will remain as 0-days in Epic’s launcher?

![Brand Icon Seperator | Signal Labs | Advanced Offensive Cybersecurity Training | Self-Paced Trainings | Live Trainings | Virtual Trainings | Custom Private Trainings for Business](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwMCAyNDciIHdpZHRoPSIyMDAwIiBoZWlnaHQ9IjI0NyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

## Empowering Cyber Defense with Advanced Offensive Security Capabilities

Signal Labs provides self-paced and live training solutions, empowering our learners to acquire the latest cutting-edge skills in this rapidly evolving field. Improve your vulnerability research campaigns and adversary simulation capabilities with the latest in offensive research and techniques.

[ Enroll Today ](/self-paced-trainings/)

[__Prev Back](https://signal-labs.com/announcing-self-paced-trainings/)

[Next __Next](https://signal-labs.com/fuzzing-wechats-wxam-parser/)

## Related Posts

### Welcome to Hack-ademia

[ View All Articles ](/blog/)

[ ![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgODY5IDUzMyIgd2lkdGg9Ijg2OSIgaGVpZ2h0PSI1MzMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+) ](https://signal-labs.com/parsing-msdn-for-documented-technique-dev/)

####  [ Parsing MSDN for (Documented) Technique Development ](https://signal-labs.com/parsing-msdn-for-documented-technique-dev/)

[ Read More ![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNjQgNjQiIHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=) ](https://signal-labs.com/parsing-msdn-for-documented-technique-dev/)

[ ![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgOTkwIDY3OCIgd2lkdGg9Ijk5MCIgaGVpZ2h0PSI2NzgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+) ](https://signal-labs.com/hypervisor-0days-custom-os-sample/)

####  [ Sample Approach to Hypervisor 0-Days w/ Custom OS Development ](https://signal-labs.com/hypervisor-0days-custom-os-sample/)

[ Read More ![](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNjQgNjQiIHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=) ](https://signal-labs.com/hypervisor-0days-custom-os-sample/)

[ View All Articles ](/blog/)

![Brand Icon Seperator | Signal Labs | Advanced Offensive Cybersecurity Training | Self-Paced Trainings | Live Trainings | Virtual Trainings | Custom Private Trainings for Business](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjAwMCAyNDciIHdpZHRoPSIyMDAwIiBoZWlnaHQ9IjI0NyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)

## Elevate Your Cyber Expertise

**Elevate Offensive Capabilities for Cyber Defense:** Drive growth in cyber defense with real-world critical skills in offensive security research and techniques.

[ Enroll Today ](/self-paced-trainings/)

[ Contact Us ](/contact/)

[ Contact Us ](/contact/)

© Signal Labs

[Privacy Policy](/privacy-policy/) \+ [Terms](/terms-and-conditions/)

[Self-Paced Trainings](/self-paced-trainings/)

[For Business](/business/)

[Student Login](/student-login/)

[ X ](https://x.com/signal_labs)

[ LinkedIn ](https://www.linkedin.com/company/cybersec-signal-labs/about/)

[ GitHub ](https://github.com/Signal-Labs)

[ ![Wordmark Logo | Signal Labs | Advanced Offensive Cybersecurity Training | Self-Paced Trainings | Live Trainings | Virtual Trainings | Custom Private Trainings for Business](data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTAwMCAyMDQiIHdpZHRoPSIxMDAwIiBoZWlnaHQ9IjIwNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=) ](https://signal-labs.com)

  * [Trainings](https://signal-labs.com/self-paced-trainings/)
  * [Who We Are](https://signal-labs.com/about/)
  * [Blog](https://signal-labs.com/blog/)
  * [For Business](https://signal-labs.com/business/)
  * [Student Login](/student-login/)
  * [Contact Us](https://signal-labs.com/contact/)

  * [Trainings](https://signal-labs.com/self-paced-trainings/)
  * [Who We Are](https://signal-labs.com/about/)
  * [Blog](https://signal-labs.com/blog/)
  * [For Business](https://signal-labs.com/business/)
  * [Student Login](/student-login/)
  * [Contact Us](https://signal-labs.com/contact/)

## Stay Connected

### We'll let you know when our next live training is scheduled.

First Name 

Last Name 

Email 

Subscribe

## Stay Connected

### We'll let you know when our next live training is scheduled.

First Name 

Last Name 

Email 

Subscribe

## Stay Connected

### We'll let you know when our next live training is scheduled.

First Name 

Last Name 

Email 

Subscribe

## Stay Connected

### We'll let you know when our next live training is scheduled.

First Name 

Last Name 

Email 

Subscribe

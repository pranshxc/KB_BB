---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-19_filesapp-symbolic-link-following.md
original_filename: 2022-03-19_filesapp-symbolic-link-following.md
title: Files.app Symbolic Link Following
category: documents
detected_topics:
- command-injection
- automation-abuse
- clickjacking
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- clickjacking
- mobile-security
language: en
raw_sha256: fe1a07648054ca86d92c432283beef178d7e7d1b23a52bff379d28f6a5336299
text_sha256: 170b7a105507bedfd94b7b7b26773e3d01803663fe4235a14bae9605c6e99bdd
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Files.app Symbolic Link Following

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-19_filesapp-symbolic-link-following.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, clickjacking, mobile-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `fe1a07648054ca86d92c432283beef178d7e7d1b23a52bff379d28f6a5336299`
- Text SHA256: `170b7a105507bedfd94b7b7b26773e3d01803663fe4235a14bae9605c6e99bdd`


## Content

---
title: "Files.app Symbolic Link Following"
url: "https://breakpoint.sh/posts/files.app-symbolic-link-following"
final_url: "https://breakpoint.sh/posts/files.app-symbolic-link-following"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Apple"]
bugs: ["iOS"]
publication_date: "2022-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2801
---

# [Breakpoint](/)

  * [RESEARCH](/research)
  * [ABOUT](/about)
  * [CONTACT](/cdn-cgi/l/email-protection#99ffebf6f4b4eaf0edfcd9fbebfcf8f2e9f6f0f7edf5edfdb7faf6f4)

# Files.app Symbolic Link Following

Ron Masas

4 minute read

19 March, 2022

![](/files.app-symbolic-link-following/cover.jpg)

Content

1. Airdrop2. Attack Setup3. The Bug4. The Attack5. Practical Attack

* * *

Timeline

Report sent to Apple

22 September, 2021

Apple validated the report

25 September, 2021

Apple requested my assessment of whether iOS 15.4 addresses the bug I reported.

8 February, 2022

iOS 15.4 fixes the bug, no CVE was assigned 🤷‍♂️

14 March, 2022

I requested addional information from Apple.

15 March, 2022

Apple decided not to issue a CVE, and said the report did not qualify for the Apple Security Bounty.

24 March, 2022

In this post, I'm going to go over how a simple symbolic link could have been used to extract the entire _/private/var/mobile/Containers/_ folder. This folder contains, among other things, iOS applications data, usually in the form of an unencrypted database. FYI, this is true for many "End-to-end" encrypted messeaging apps like WhatsApp, Telegram, and Facebook Messenger.

Additionally, it contains the _"./Shared/AppGroup/[UUID]/File Provider Storage"_ folder, which is where the _"Files"_ app stores your local files also known as _"On My iPhone"_. And finally, the _"Mobile Documents"_ folder which is the device local copy of iCloud Drive, applications backups, etc.

The research for this bug was bitter sweet, while writing up my report iOS 15 was released, limiting the impact of the bug to _"File Provider Storage"_ and _"Mobile Documents"_ folders. This issue was addressed in the [security content of iOS 15.4](https://support.apple.com/en-us/HT213182#:~:text=Ron%20Masas%20of%20BreakPoint.sh)

> iOS 15.4 fixes the first iOS bug I've found!  
> Blog post and proof of concept video below:<https://t.co/hD0jHmtk2O>[#infosec](https://twitter.com/hashtag/infosec?src=hash&ref_src=twsrc%5Etfw) [#BugBounty](https://twitter.com/hashtag/BugBounty?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/bqGgKUoXzt](https://t.co/bqGgKUoXzt)
> 
> — Ron Masas (@RonMasas) [March 19, 2022](https://twitter.com/RonMasas/status/1505300044173430784?ref_src=twsrc%5Etfw)

## Airdrop

Airdrop was first introduced in Mac OS X Lion and iOS 7. AirDrop can be used to share and receive photos, documents, links, and more with other Apple devices that are nearby.

## The Bug

The Files Application on iOS does not sufficiently account for when a given file is a symbolic link that resolves to a target outside of the intended control sphere. This allows an attacker to cause the app to operate on unauthorized files.

For one, entire sensitive folders like _/private/var/mobile/Containers/_ could have been extracted using Airdrop by simply sharing a symlink.

One attack scenario is physical extraction from an unlocked device. Let's say you asked your target for his phone to "call your mom". Once you have the unlocked phone at hand, you download a symlink that points to the information you want to steal and share it with your device using Airdrop.

If you like to reproduce my findings on an iOS device running iOS 14.8.1 and below, do the following:

  1. Create a symbolic link to _/private/var/mobile/Containers/_ (Other directories may also work, this folder was the highest impact directory I was able to find)

  
  
  mkdir /tmp/foo
  ln -s /private/var/mobile/Containers/ /tmp/foo/share_containers
  zip --symlinks -r foo.zip /tmp/foo
  

  2. Get _foo.zip_ to your iOS device - I did it using Airdrop
  3. Extract _foo.zip_ by tapping on the _foo.zip_ file, and navigate to the _foo_ folder.
  4. Open the _share_containers_ file and click on the share icon at the top right corner.
  5. Share the file using Airdrop.

Sharing may take some time depending on the amount of data you have on your phone. For best results, keep both devices "awake" while the folder is sent.

As I said in the beginning, I wasn't quick enough to report this bug, it was patched on iOS 15. I think the CVE for it was _CVE-2021-30855_. However, I found that relative symbolic links still work when targeting the _"File Provider Storage"_ and _"Mobile Documents"_ folders. I also found I could store and share symbolic links using iCloud Drive, which makes the attack much more reliable.

## Attack Setup

First, we need to create our symlink. In this example, we are going to target the iCloud Drive, so traversing back 2 directories should land us at the iCloud root directory AKA _"Mobile Documents"_.
  
  
  ln -s ../../ contarct.pdf
  

In your iCloud Drive, create a new folder and copy _"contarct.pdf"_ into it. Right click on the folder and choose Share > Share Folder

![](/files.app-symbolic-link-following/share-folder.jpg)

In the Share Folder dialog, set "Who can access" to "Anyone with a link" and click on the share button.

![](/files.app-symbolic-link-following/share-settings.jpg)

Right click on the folder again, and choose Share > Copy Link.

![](/files.app-symbolic-link-following/copy-link.jpg)

You should now have a shareable link to a folder with the symlink we just created.

# The Attack

All that left for us to do now is share the link with our target, and ask him to send us the _contarct.pdf_ file. If he does, we will gain access to his iCloud Drive files.

![](/files.app-symbolic-link-following/attack.jpg)

When the user sends the _contarct.pdf_ he is actually sharing _../../_ which is the _"Mobile Documents"_ folder. Since the user is trying to share a folder, it will be zipped before it sent, in this example via WhatsApp.

The attacker can now download and extract the file to get a full copy of the user iCloud Drive and application backups.

![](/files.app-symbolic-link-following/files.jpg)

# Practical Attack

Since I'm using a test phone, my iCloud Drive is pretty empty. When testing on my own account, I had to wait a few minutes for my phone to generate the zip and a few more just to send it.

A more practical attack would be targeting specific folders within the _"File Provider Storage"_ and _"Mobile Documents"_ folders. Something like the Chrome downloads folder for example.

# Conclusion

Symlinks are extremely powerful when hunting for bugs. In my [previous post](/posts/bypassing-the-macos-gatekeeper) I've used one to bypass the macOS Gatekeeper. Please don't forget to update iOS and iPadOS to 15.4 and macOS Monterey to 12.3.

Timeline

Report sent to Apple

22 September, 2021

Apple validated the report

25 September, 2021

Apple requested my assessment of whether iOS 15.4 addresses the bug I reported.

8 February, 2022

iOS 15.4 fixes the bug, no CVE was assigned 🤷‍♂️

14 March, 2022

I requested addional information from Apple.

15 March, 2022

Apple decided not to issue a CVE, and said the report did not qualify for the Apple Security Bounty.

24 March, 2022

### Open Source

  * [VooDoo](https://github.com/breakpointHQ/VOODOO)
  * [Snoop](https://github.com/breakpointHQ/snoop)
  * [Chrome Bandit](https://github.com/breakpointHQ/chrome-bandit)
  * [TCC ClickJacking](https://github.com/breakpointHQ/TCC-ClickJacking)

### Company

  * [About](/about)
  * [Github](https://github.com/breakpointHQ)
  * [Research](/research)

### Imprint

BreakPoint Technologies LTD  
Israel, HaPninim 1  
6803001 Tel Aviv-Jaffa

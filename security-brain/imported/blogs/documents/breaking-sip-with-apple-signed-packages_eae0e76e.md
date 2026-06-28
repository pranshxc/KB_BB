---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-04_breaking-sip-with-apple-signed-packages.md
original_filename: 2024-03-04_breaking-sip-with-apple-signed-packages.md
title: Breaking SIP With Apple-signed Packages
category: documents
detected_topics:
- command-injection
- supply-chain
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- supply-chain
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: eae0e76e2e2e7edda27cdb7e0df4588ea4fabf587f229cd3f88329caf69e600e
text_sha256: e09451a58f1899cda21b82f13505d0e1e17535271b05b68b38d3c8f7013331a0
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking SIP With Apple-signed Packages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-04_breaking-sip-with-apple-signed-packages.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `eae0e76e2e2e7edda27cdb7e0df4588ea4fabf587f229cd3f88329caf69e600e`
- Text SHA256: `e09451a58f1899cda21b82f13505d0e1e17535271b05b68b38d3c8f7013331a0`


## Content

---
title: "Breaking SIP With Apple-signed Packages"
page_title: "Breaking SIP with Apple-signed Packages | L3Harris® Fast. Forward."
url: "https://www.l3harris.com/newsroom/editorial/2024/03/breaking-sip-apple-signed-packages"
final_url: "https://www.l3harris.com/newsroom/editorial/2024/03/breaking-sip-apple-signed-packages"
authors: ["Michael Cowell"]
programs: ["Apple (macOS)"]
bugs: ["SIP bypass"]
publication_date: "2024-03-04"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 395
---

Editorial

##  Breaking SIP with Apple-signed Packages

Trenchant, of L3Harris Technologies, performs vulnerability research against a wide variety of interesting and challenging targets.

SA

Space & Airborne Systems

Mar 4, 2024 | 5+ Minute Read

SHARE

  * [ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on facebook in New Window")
  * [ Linkedin ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on linkedin in New Window")
  * [ X ](https://x.com/intent/post?text=Breaking+SIP+with+Apple-signed+Packages&url=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on x in New Window")

  * [ Cyber ](/search?size=n_10_n&filters%5B0%5D%5Bfield%5D=domains&filters%5B0%5D%5Bvalues%5D%5B0%5D=Cyber&filters%5B0%5D%5Btype%5D=any)
  * [ Space & Mission Systems ](/search?size=n_10_n&filters%5B0%5D%5Bfield%5D=business_segments&filters%5B0%5D%5Bvalues%5D%5B0%5D=Space%20%26%20Mission%20Systems&filters%5B0%5D%5Btype%5D=any)
  * [ Software, Cyber and Robotic Solutions ](/search?size=n_10_n&filters%5B0%5D%5Bfield%5D=topical_areas&filters%5B0%5D%5Bvalues%5D%5B0%5D=Software%2C%20Cyber%20and%20Robotic%20Solutions&filters%5B0%5D%5Btype%5D=any)
  * [ Intelligence ](/search?q=tags%3A%22Intelligence%22)

SHARE

  * [ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on facebook in New Window")
  * [ Linkedin ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on linkedin in New Window")
  * [ X ](https://x.com/intent/post?text=Breaking+SIP+with+Apple-signed+Packages&url=https%3A%2F%2Fwww.l3harris.com%2Fnewsroom%2Feditorial%2F2024%2F03%2Fbreaking-sip-apple-signed-packages "Share page on x in New Window")

By Michael Cowell

 _Note: This article is one in a technical series by Trenchant of L3Harris Technologies._

The original topic of my first blog post, posted approximately a year ago, was to discuss how command injection vulnerabilities are present in PackageKit on macOS. While writing the article, I found some Apple-signed packages which had command injection vulnerabilities which could be used to bypass SIP.

The vulnerability, assigned CVE-2023-38609, was finally fixed in [Ventura 13.5](https://support.apple.com/en-us/HT213843).

**Background**

Way back in March 2020, Patrick Wardle posted [a blog post](https://objective-see.org/blog/blog_0x56.html) identifying vulnerabilities in Zoom, which he combined with lax application entitlements to achieve camera and microphone access via execution in Zoom.

At the time, it was possible to modify installation scripts, which were stored in a world-writable location (later reported by NCC Group as CVE-2020-9817) to achieve root when a user installed a package.

I used this paradigm with Microsoft Teams to overwrite ffmpeg with a re-exported dylib in the same way as Wardle did with Zoom, achieving microphone and camera access within the Teams process. Unfortunately, Microsoft realised this was an issue somewhere around May 2020 and removed the library validation issue, and around the same time CVE-2020-9817 was fixed in Catalina 10.15.5.

While playing around with packages, I stumbled upon the fact that environment variables were inherited in installation scripts, and through experimentation it became clear that only the PATH variable appeared to have been constructed in PackageKit - meaning that the following line in one of Team’s scripts would prove problematic:

/usr/bin/sudo -u $USER /usr/bin/open “$TEAMS_APPLICATION”

Luckily for users, it seemed most application updaters did not use package files, so opportunities to elevate permissions in this way are likely still limited. One notable exception was Zoom which had a similar injection issue to the one shown in Teams above. It would launch Installer as a regular user, allowing a malicious (unprivileged) process to detect an update and launch an Installer instance with a malicious variable.

It was a pretty interesting quirk, although scenarios in which it could have been useful are fairly slim. I instead chose to apply the lack of environment variable to Apple-signed packages.

**Targeting SIP**

Packages are installed by either installd (using package_script_service) or system_installd, where the latter is used if:

  1. It's an Apple-signed package
  2. The certificate is still valid
  3. The installation target is a live volume (as otherwise SIP isn't applicable)

When updating the OS, packages might need to access locations inaccessible with SIP enabled. To do this, system_installd has an additional entitlement:

<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "https://www.apple.com/DTDs/PropertyList-1.0.dtd">  
<plist version="1.0">  
<dict>  
<key>com.apple.private.apfs.create-synthetic-symlink-folder</key>  
<true/>  
<key>com.apple.private.launchservices.cansetapplicationstrusted</key>  
<true/>  
<key>com.apple.private.package_script_service.allow</key>  
<true/>  
<key>com.apple.private.responsibility.set-arbitrary</key>  
<true/>  
<key>com.apple.private.responsibility.set-hosted-properties</key>  
<true/>  
<key>com.apple.private.security.storage-exempt.heritable</key>  
<true/>  
<key>com.apple.private.security.syspolicy.package-installation</key>  
<true/>  
<key>com.apple.private.security.syspolicy.package-verification</key>  
<true/>  
<key>com.apple.private.storage.fusion.allow-pin-fastpromote</key>  
<true/>  
<key>com.apple.private.tcc.manager.access.delete</key>  
<array>  
<string>kTCCServiceAll</string>  
</array>  
**< key>com.apple.rootless.install.heritable</key>**  
** <true/>**  
</dict>  
</plist>

This allows system_installd and any process it creates to write to SIP-protected locations. The separation of package_script_service and system_installd makes sense. To circumvent this separation would require a stolen certificate or validation flaw.

Fairly quickly I was able to identify multiple packages that had command injection vulnerabilities in installation scripts, which allowed me to inherit the entitlement.

The first with this command injection was SafeView up to 9.4.0, which used $USER in a very similar way to Microsoft Teams:

launchctl asuser "$(id -u ${USER})" sudo -u ${USER} launchctl load /Library/LaunchAgents/com.apple.SafeView.app.NexusAgent.plist

I reported this to Apple who released a patch in SafeView 9.5.0. The patch instead relied on stat to build $USER, and then blacklisted the old package in GateKeeper. I responded that the patch was insufficient as earlier versions of the package could presumably still be used and, regardless, I had already found other options.

Ultimately, the best one I found was Remote Desktop Admin 3.7.2, which is a relatively small package (~15MB) and also trusted $USER in AlertAll.sh:

#!/bin/sh  
target=$2  
pkg=$0

ALERTALL="./Tools/AlertAll.app/Contents/MacOS/AlertAll"  
if [ "$USER" = "" ]; then  
USER="root"  
fi

if [ -e "/usr/bin/sudo" ]; then  
/usr/bin/sudo -u $USER $ALERTALL $target  
else  
$ALERTALL $target  
fi

EXITCODE=$?

exit $EXITCODE

In the end, I manually found four packages which had similar issues

**Installed Software**| **Package Name**| **Version**  
---|---|---  
**SafeView**| **SafeView**|  9.4.0  
**Remote Desktop Admin**| **RemoteDesktopAdmin**|  3.5.3  
**Remote Desktop Admin**| **RemoteDesktopAdmin**|  3.7.2  
**iPhoto Update**| **iPhotoUpdate**|  9.2.3  
  
  

A lot of packages would’ve been better than RemoteDesktopAdmin on account of the size, but due to the system partition becoming read-only in macOS 11 these packages will no longer install. While iPhotoUpdate is mentioned here, it is less serious than others as the command injection is gated behind a check for COMMAND_LINE_INSTALL being zero, meaning that you cannot exploit it in the background.

After reporting all four, I decided to try and automate things.

* * *

The XAR format

At their core, .pkg files are just XAR archives with specific files expected by PackageKit. A package with scripts will look something like the following:

admin@admins-MBP Downloads % xar -t -f iDVD7.1.2Update.pkg  
Bom  
PackageInfo  
Payload  
Scripts

One benefit to the XAR file format is that it stores a (compressed) table of contents at the start of the file, just after the header.

![Image of the XAR file format's stored table of contents at the file start](/sites/default/files/2024-03/breaking-sip1_0.png)

As a lot of Apple-signed packages are large packages such as OS installers I was able to use this to my advantage. By dumping a list of packages from Apple’s SUCatalogs, I could then check if a package contained scripts by reading the header, and then reading the number of bytes of compressed TOC. Then, by only downloading packages with a “Scripts” entry, I was able to reduce the search space considerably.

After quickly implementing a “partial” XAR script in python, I tried to take it a step further and download just the Scripts file. Unfortunately, Apple’s servers rejected the Range header, and a partial download was impractical for large files as the Scripts entry is usually at the end of the archive.

Regardless, I was able to filter out packages without scripts. Package scripts are often re-used extensively between software packages, so by further de-duplicating individual scripts I ended up with a minimal set of potentially vulnerable items to investigate.

Sadly, this was all for nothing as I didn’t find anything smaller (and thus better) than RemoteDesktopAdmin. Some packages existed that allowed for a SIP-exempt change of permissions, but doing anything interesting with this would require a separate TCC bypass. (For example, you could use it to own the location clients list, but would still need a separate bypass, or use something overt like Finder to modify the entries.)

**Exploitation**

One downside to this finding is that running installer requires root permissions. I decided to pair the bug with CVE-2022-46689, aka MacDirtyCow, to escalate from user to SIP-exempt prompt. I used this fairly simple approach:

  1. Use MacDirtyCow to overwrite the /etc/pam.d/sudo file, making sure to pad appropriately to maintain validity.
  2. Call installer with a malicious environment variable.
  3. Restore the original pam file.

The necessary code for replicating this is available here ([**CVE-2023-38609**](https://github.com/mc-17/CVE-2023-38609)) and will work up to Ventura 13.0.1. If you’re running it with root via some other means, it will work up to 13.4.1.

I’ve also included the partial XAR implementation here ([**XAR**](https://github.com/mc-17/xar)).

**The Fix**

Apple's first fix was blacklisting SafeView 9.4.0 from GateKeeper, preventing new installations.

When I raised the issue of the other packages, they addressed it by adding a blacklist in PackageKit matching the specific scripts, landing in 13.5 - matching scripts would be run without SIP exemption.

In Sonoma 14.1, they appear to have gone a step further and introduced “mutations”. These are matched on the script name, position (pre/post install) and package identifier. “Mutations” also allow for a find/replace to be performed prior to execution or for the script to be run as-is but without SIP entitlements.

<dict>  
<key>ScriptTypes</key>  
<array>  
<string>preinstall</string>  
<string>preflight</string>  
<string>postinstall</string>  
<string>postflight</string>  
</array>  
<key>RelativePathTransformation</key>  
<true/>  
<key>RelativePath</key>  
<string>%@_actions/LurkAndLaunch.pl</string>  
<key>DropSIP</key>  
<true/>  
<key>ComponentPackageIdentifiersRegex</key>  
<array>  
<string>^.*$</string>  
</array>  
</dict>

The newer approach is easier to maintain, and allows for more fine-grained control over bad scripts. For some scripts, the entry is functionally identical to the original blacklist due to widespread usage. The find/replace functionality (defined in InstallScriptMutations.plist) also allows for Apple to patch scripts that still might need SIP-exemption, but have other vulnerabilities.

The file with this definition (/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/InstallScriptActions.plist) would also be useful to easily uncover currently live SIP bypass packages from Release Candidates.

The current fix seems fairly good, however all Apple packages still run with SIP exemption unless explicitly blacklisted, which still leaves some room for errors. It doesn’t seem unreasonable to sign packages that require SIP-exemption with a separate certificate. A separate certificate requirement would be a more robust solution versus hoping that engineers don’t slip up.

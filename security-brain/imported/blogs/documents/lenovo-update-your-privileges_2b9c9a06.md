---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-19_lenovo-update-your-privileges.md
original_filename: 2023-07-19_lenovo-update-your-privileges.md
title: Lenovo Update Your Privileges
category: documents
detected_topics:
- access-control
- automation-abuse
- sso
- command-injection
- race-condition
- api-security
tags:
- imported
- documents
- access-control
- automation-abuse
- sso
- command-injection
- race-condition
- api-security
language: en
raw_sha256: 2b9c9a0642c99f8952ac6580775d91417698a4156e0dbd438b149bf38f7bcb41
text_sha256: de56cea8154cf66aee05f2a39330fa7bcf3158749d8b1434e60bc1a24ca5128f
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Lenovo Update Your Privileges

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-19_lenovo-update-your-privileges.md
- Source Type: markdown
- Detected Topics: access-control, automation-abuse, sso, command-injection, race-condition, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `2b9c9a0642c99f8952ac6580775d91417698a4156e0dbd438b149bf38f7bcb41`
- Text SHA256: `de56cea8154cf66aee05f2a39330fa7bcf3158749d8b1434e60bc1a24ca5128f`


## Content

---
title: "Lenovo Update Your Privileges"
page_title: "Lenovo Update Your Privileges – Compass Security Blog"
url: "https://blog.compass-security.com/2023/07/lenovo-update-your-privileges/"
final_url: "https://blog.compass-security.com/2023/07/lenovo-update-your-privileges/"
authors: ["Raphael Rosenast"]
programs: ["Lenovo"]
bugs: ["Local Privilege Escalation", "DLL Hijacking", "Windows"]
publication_date: "2023-07-19"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 919
---

A journey into the discovery of two privilege escalation vulnerabilities in the Lenovo update functionality.

The information in this blog post is related to the the following vulnerabilities detected by Compass Security:

  * [CVE-2022-4568 in Lenovo System Update](https://support.lenovo.com/us/en/product_security/ps500553-lenovo-system-update-elevation-of-privileges-vulnerability) prior to 5.08.01
  * [CVE-2022-4569 in ThinkPad Hybrid USB-C with USB-A Dock Firmware Update Tool](https://support.lenovo.com/us/en/product_security/LEN-103544) prior to V1.0.35_v2

The presented vulnerabilities were disclosed immediately after discovery and Lenovo has remediated both vulnerabilities as of the writing of this blog post.

## A Wild CMD Window Appears

Have you ever been working and suddenly an unexpected CMD window shows up, grabs your keyboard focus and disappears again?

It was this unpleasant experience that started the journey. An unexpected and quickly disappearing CMD window always leaves a bland aftertaste – especially working in IT Security. This is why we decided to push off work for a few minutes and started a quick investigation into the origins of the window.

As one of our [Forensic Readiness](https://blog.compass-security.com/2017/06/forensic-readiness/) practices, we audit [Process Creation](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-process-creation) including the [Command Line](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing) resulting in an Event Log entry for every started process.

The investigation into the Security Event Log revealed the following interesting [Event ID 4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688) at the relevant time, showing the executed process: 

**Executable Path**|  User Name  
---|---  
C:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15\Drivers\Win10\x64\dpinst.exe dpinst.exe| lenovo_tmp_jrhlXESX  
  
We may therefore assume the observed CMD Window is related to an automatic Lenovo update installed for the [ThinkPad Hybrid USB-C Dock](https://www.lenovo.com/ch/de/p/accessories-and-software/docking/docking_usb-docks-\(universal-cable-docks\)/40af0135ch).

Furthermore, the elevated CMD Window runs an executable in the path `C:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15` under a user `lenovo_tmp_jrhlXESX` ?

Let’s look at the user first.

### The `lenovo_tmp` User

A user account is created during a Lenovo System Update as a way for restricted users to install updates with elevated permissions. `UACSdk.exe` creates the user with the prefix `lenovo_tmp_` and a partially randomized username consisting of four lowercase and four uppercase characters. The account is created as a regular user at first via [NetUserAdd ](https://learn.microsoft.com/en-us/windows/win32/api/lmaccess/nf-lmaccess-netuseradd)and later on added into the Administrators group.

Vulnerabilities were found in the user creation in the past and the [according blog article by IOActive](https://ioactive.com/privilege-escalation-vulnerabilities/) describes the behavior of the Lenovo Update well.

**Can we obtain the credentials to the user?**

The password of the user is generated before user creation. Mainly the deprecated function [CryptGenRandom ](https://learn.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-cryptgenrandom)is used for generating 76 random bytes.

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-21-1024x439.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-21.png)_Random generator involved in the password generation_

After this, the randomly generated bytes are split, shifted, and mangled together and then converted to UTF-8 Unicode. In the end, a total of 19 characters are selected for the password and a null terminator is included.

**The short analysis of the password generation did not result in a viable option to obtain the password.**

However, it remains to say that the password generation method also involves behavior, which was not fully understood. For example, the creation of a hash of the random bytes and the immediate destruction of the result (potentially checking for errors?).

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-12.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-12.png)Hashing and immediate destruction

Usually, the user is deleted after the installation of the updates is finished. There is also a cleanup routine to delete all users with names containing `lenovo_tmp` potentially dealing with the issue of [not always fully deleted](https://www.reddit.com/r/PowerShell/comments/mq3bjp/scripting_help/) users.

Interestingly, some companies may have introduced a monitoring exceptions for account creation with names, such as `lenovo_tmp`, which may come in handy when running an attack.

> This has definitely been a contentious issue for anyone who monitors account creation in their environment for some time.  
>  
> The options are  
>  
> ensure deletion of the account after the updates occur  
>  
> don’t monitor lenovo_tmp_* accounts  
>  
> don’t use the update software
> 
> — Jim Schwar (@jimiDFIR) [July 27, 2020](https://twitter.com/jimiDFIR/status/1287756082165747712?ref_src=twsrc%5Etfw)

Furthermore, the path from where the executable is started is unusual as well.

### The Path

The `C:\DRIVERS` path of the executable caught our eye because on a usual Windows installation, the user has permissions to append subdirectories to the drive root and naturally has modify permissions on these directories.

A quick check off the file permissions or more precisely discretionary access control lists (DACLs) with [icacls ](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)shows that all authenticated users have modify permissions on the directory in question as well:
  
  
  PS> icacls C:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15
  ...
  NT AUTHORITY\Authenticated Users:(I)(M)
  NT AUTHORITY\Authenticated Users:(I)(OI)(CI)(IO)(M)

Therefore, it should be possible to replace the Lenovo executable `dpinst.exe `with another executable and trigger an update to reach code execution under the elevated `lenovo_tmp `user.

Well, yes but no: There is a digital signature check of the executable involved (which on a side note may have been prone to a [bait and switch attack](https://github.com/googleprojectzero/symboliclink-testing-tools/blob/main/BaitAndSwitch/BaitAndSwitch_ReadMe.txt)), but an easier exploitation is possible:

The Event Logs show, that in the same modifiable directory, there is a batch file `DriverInstallerScript.bat `run under the same elevated permissions during the update.

**Executable Path**|  User Name  
---|---  
c:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15\DriverInstallerScript.bat /silent| lenovo_tmp_jrhlXESX  
  
This batch script tries to determine the current OS Version and ultimately runs the before observed `dpinst.exe`. As there is no file signature, it should be possible to simply modify the batch script and run the update to execute commands.

## Exploiting CVE-2022-4569

Naturally, the ThinkPad Hybrid Dock is required for this exploitation. However, if it is present, a few lines of code allow to exploit CVE-2022-4569: The following example shows how to insert a new administrator through the batch file and start of the Lenovo Update Service as well as run the command for an update:
  
  
  PS> echo "net user /add InsertedUser S3kur.Password.Here.123" >> "C:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15\DriverInstallerScript.bat"
  
  PS> echo "net localgroup Administrators InsertedUser /add" >> "C:\DRIVERS\ThinkPad_Hybrid_USB-C_With_USB-A_Dock_MFG_Driver_V1.0.0.15\DriverInstallerScript.bat"
  
  PS C:\Program Files (x86)\Lenovo\System Update> .\ConfigService.exe start
  PS C:\Program Files (x86)\Lenovo\System Update> .\TvsuCommandLauncher.exe 5

As behavior like adding a new user is usually monitored, the triggered alert nicely displays the chain of events:

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-15-1024x303.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-15.png)Result of the privilege escalation as observed by [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-endpoint?view=o365-worldwide)

It is up to the reader to think of a stealthier strategy for exploitation or a username with monitoring exclusions.

## More DACL Issues

During the analysis of the executables involved in the Lenovo Update, several executables were quickly glanced over. One notable executable is named `Tvsukernel.exe`, which is typically run under the administrative `lenovo_tmp` user by the “System Update” Service.

`Tvsukernel.Startup.Main` shows the following cleanup routine:

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-16-1024x561.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-16.png)Cleanup routine of Tvsukernel.exe

The `[Directory.Delete](https://learn.microsoft.com/en-us/dotnet/api/system.io.directory.delete?view=net-7.0#system-io-directory-delete\(system-string-system-boolean\))` call shows the directory `C:\TvsuSession` is recursively deleted. This means all files and subdirectories within the directory are deleted as well:

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-17.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-17.png)Recursive directory deletion

Similarly to above, this directory can be created and modified by any authenticated user as well. But how can we exploit this recursive folder deletion?

##  From File Deletion to Elevated Code Execution

In 2021, Abdelhamid Naceri has demonstrated a technique, on how deletion of user writable folder contents by an elevated account may lead to code execution under the elevated accounts privileges. [An excellent description of the technique is found on the blog of Zero Day Initiative](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks).

Although having been used in a multitude of exploits recently, this technique is still not common knowledge. Therefore, we will go over the building blocks.

First, how would we get code execution from an arbitrary file deletion?

### The Windows Installer Service

The [Windows Installer](https://en.wikipedia.org/wiki/Windows_Installer) Service is responsible for performing installations of applications. During every installation, the service creates records of all changes performed. These records allow a rollback in case of an error during installation and therefore allow reverting to a previous system state cleanly. The records are stored in a folder named `C:\Config.Msi`.

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-29-1024x578.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-29.png)

Control of these records (by overwriting them) results in the control of the filesystem state after an installation rollback is performed. Therefore, if attackers can delete the `C:\Config.Msi` directory during an installation with elevated privileges, they can then write their own records to be executed when triggering an installation rollback. A typical attack record would drop a file such as an executable or DLL to disk, which is then executed under a privileged account at some point.

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-32-1024x611.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-32.png)

Now, how does this help us?

With the found vulnerability we can delete the directory `C:\TvsuSession` with administrative privileges but how can it replace `C:\Config.Msi`?

### Bending Directory Content Deletion

Ideally, we would now want to create a symbolic link from `C:\TvsuSession` to `C:\Config.Msi` in order to bend the deletion of files from the Lenovo directory to the other. However, unprivileged Windows users can’t create symbolic links.

This is where a technique pioneered by [James Forshaw](https://tyranidslair.blogspot.com/) comes in: NTFS Junctions in combination with Object Manager symbolic links as described in the [following blog article by Almond Offensive Security](https://offsec.almond.consulting/intro-to-file-operation-abuse-on-Windows.html).

#### NTFS Junctions

NTFS junctions are a filesystem feature like Unix mount points for directories. It allows unprivileged users to create a link from one directory to another directory only. However, upon deletion of the junction pointing at directory, the original directory is not deleted. As we want to link the files within the directory, such a Junction will only go halfway.

#### Windows Object Manager

The [Windows Object Manager](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/windows-kernel-mode-object-manager) manages objects such as files, devices and registry keys. It can be accessed for example using [WinObj by Mark Russinovich](https://learn.microsoft.com/en-us/sysinternals/downloads/winobj). The part interesting to us is, that unprivileged users can create symbolic links in Object Manager directories such as `\RPC Control`. Such a symbolic link can point to any path on the filesystem including files.

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-24.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-24.png)_Symbolic link in the_` \RPC Control` _directory of the Object Manager_

When chaining NTFS junctions together with Object Manager symbolic links, unprivileged users can create sort of a pseudo symbolic link. We could use such a pseudo symbolic link from `C:\TvsuSession` to `C:\Config.Msi` to forward a deletion of the content.

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-26-1024x263.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-26.png)

An example tool to create these pseudo symbolic links is provided in the [symbolic link-testing-tools Developed by James Forshaw](https://github.com/googleprojectzero/symboliclink-testing-tools):
  
  
  PS> .\CreateSymlink.exe C:\TvsuSession\file.txt C:\Config.Msi\file.txt
  Opened Link \RPC Control\file.txt -> \??\C:\Config.Msi\file.txt: 00000098
  Press ENTER to exit and delete the symlink

#### Opportunistic Lock

As we are now able to delete the records of the Windows Installer, we may in theory be able to conduct an attack but we would have trouble getting the timing of the deletion right. This is where the [opportunistic lock](https://learn.microsoft.com/en-us/windows/win32/fileio/opportunistic-locks\)) (oplock) comes in. This lock can be placed on a file and whenever another process tries to accesses the locked file, a callback routine is triggered to inform us about the access. Furthermore, the file access of the other process is delayed until the callback returns. Therefore, the oplock can for example be used to coordinate actions and gain time in race condition scenarios.

### Tying Techniques Together

With this, the building blocks for the exploitation of the vulnerability in `Tvsukernel.exe` are set. The exact technique exploiting the Lenovo System Update DACL issue is described in more detail on the [blog of the Zero Day Initiative](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks) under _From Folder Contents Delete to SYSTEM EoP_.

These are the exact steps performed:

  1. Start an installation using the Windows Installer Service, which is set up to fail at a later stage.
  2. Create the following folder structure:` C:\TvsuSession\folder1`.
  3. Create a file within: `C:\TvsuSession\folder1\file1.txt`.
  4. Set an oplock on the file `C:\TvsuSession\folder1\file1.txt`.
  5. Run Lenovo System Update and wait for `Tvsukernel.exe` to start the deletion of `file1.txt`. This will trigger the oplock.
  6. In the oplock callback: 
  * Move `file1.txt` elsewhere, so that `C:\TvsuSession\folder1` is empty and could be deleted (directly deleting `file1.txt` would require the release the oplock).
  * Recreate `C:\TvsuSession\folder1` as a junction to the `\RPC Control `folder of the object namespace.
  * Create a symbolic link at `\RPC Control\trick.txt` pointing to `C:\Config.Msi::$INDEX_ALLOCATION` (deletion of the `$INDEX_ALLOCATION` directory stream is similar to the deletion of the directory).
  7. When the callback completes, the oplock is released and the vulnerable process continues execution. The deletion of `file1.txt` becomes a deletion of `C:\Config.Msi.`
  8. Create `C:\Config.Msi` with your own instructions.
  9. Fail the installation started previously and wait for the installer to apply the rollback from your own instructions.
  10. Profit.

The creation of an Object Manager symbolic link in general is a highly suspicious endeavor especially when linked to `C:\Config.Msi::$INDEX_ALLOCATION` and such actions may therefore be detected:

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-25-1024x505.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-25.png)The Object Manager symbolic link was detected by Microsoft Defender for Endpoint

We have not further investigated into an exploitation variant for the Lenovo System Update vulnerability without the Object Manager symbolic link and are therefore unaware of a stealthier variant.

## Exploiting CVE-2022-4569

You may ask: Do we have to perform all these steps manually?  
Answer is: No.

The [Zero Day Initiative has provided another GitHub repository](https://github.com/thezdi/PoC/tree/master/FilesystemEoPs) with a framework where such an attack is readily implemented. The specific implementation places the file `C:\Program Files\Common Files\microsoft shared\ink\HID.DLL` on disk. The placed DLL hijacks the execution of the On-Screen Keyboard and allows to get a SYSTEM command prompt upon start of the Keyboard.

Using the provided implementation, the following steps allow the exploitation of CVE-2022-4568:

Prerequisites: The directory `C:\Config.Msi` must not exist. If it does exist, the same vulnerability may be used to delete the directory before starting the process.

  1. Set up for the privilege escalation upon deletion of the `Config.Msi` folder.  
`.\FolderOrFileDeleteToSystem.exe`
  2. Set up the pseudo-symlink (NTFS Junction and Object Manager symlink):  
`.\FolderContentsDeleteToFolderDelete.exe /target C:\Config.Msi /initial C:\TvsuSession`
  3. Run Lenovo System Update:  
`.\ConfigService.exe start && .\TvsuCommandLauncher.exe 8`
  4. Open the On-Screen Keyboard

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/LenovoPrivEsc2-1024x579.gif)](https://blog.compass-security.com/wp-content/uploads/2023/06/LenovoPrivEsc2.gif)Example exploitation of CVE-2022-4569

Keep in mind, the On-Screen Keyboard DLL Hijack is well known and certainly monitored for. Such actions should usually be detected:

[![](https://blog.compass-security.com/wp-content/uploads/2023/06/image-23-1024x225.png)](https://blog.compass-security.com/wp-content/uploads/2023/06/image-23.png)_On-Screen Keyboard DLL Hijack as detected by Microsoft Defender for Endpoint_

For a more stealthy privilege escalation, another technique should be used.

## Key Takeaway

Whenever a privileged process performs operations on a user modifiable part of the filesystem, there is a potential for privilege escalation. Even if the operations performed are as small as a file deletion, the consequences may be significant.

## Links

CVE-2022-4568

  * [Lenovo](https://support.lenovo.com/us/en/product_security/ps500553-lenovo-system-update-elevation-of-privileges-vulnerability)
  * [Advisory](https://www.compass-security.com/fileadmin/Research/Advisories/2022_21_CSNC-2022-015_Lenovo_System_Update_Privilege_Escalation.txt)

CVE-2022-4569

  * [Lenovo](https://support.lenovo.com/us/en/product_security/LEN-103544)
  * [Advisory](https://www.compass-security.com/fileadmin/Research/Advisories/2022_21_CSNC-2022-016_ThinkPad_Hybrid_USB-C_With_USB-A_Dock_Privilege_Escalation.txt)

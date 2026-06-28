---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-17_abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks.md
original_filename: 2022-03-17_abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks.md
title: Abusing Arbitrary File Deletes To Escalate Privilege And Other Great Tricks
category: documents
detected_topics:
- sso
- idor
- access-control
- command-injection
- rate-limit
- race-condition
tags:
- imported
- documents
- sso
- idor
- access-control
- command-injection
- rate-limit
- race-condition
language: en
raw_sha256: 120959e970ed09248c25266747baf62dba5c2926498be7524cba99ae777cfc74
text_sha256: c8472c5c3462a1c009751de8cc4de90841552189bd5155e8f76642f91cafc76e
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Arbitrary File Deletes To Escalate Privilege And Other Great Tricks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-17_abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks.md
- Source Type: markdown
- Detected Topics: sso, idor, access-control, command-injection, rate-limit, race-condition
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `120959e970ed09248c25266747baf62dba5c2926498be7524cba99ae777cfc74`
- Text SHA256: `c8472c5c3462a1c009751de8cc4de90841552189bd5155e8f76642f91cafc76e`


## Content

---
title: "Abusing Arbitrary File Deletes To Escalate Privilege And Other Great Tricks"
page_title: "Zero Day Initiative — Abusing Arbitrary File Deletes to Escalate Privilege and Other Great Tricks"
url: "https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks"
final_url: "https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks"
authors: ["Abdelhamid Naceri", "Simon Zuckerbraun"]
programs: ["Microsoft (Windows)"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2806
---

# Blog

#  Abusing Arbitrary File Deletes to Escalate Privilege and Other Great Tricks 

__ March 17, 2022

__ Simon Zuckerbraun

**UPDATED Sept. 3, 2024:** This blog has been updated. The original version, published on March 17, 2022, can be found at this [archive ](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks-archive).

What do you do when you’ve found an arbitrary file delete as `NT AUTHORITY\SYSTEM`? Probably just sigh and call it a DoS. Well, no more. In this article, we’ll show you some great techniques for getting much more out of your arbitrary file deletes, arbitrary folder deletes, and other seemingly low-impact filesystem-based exploit primitives.

**The Trouble with Arbitrary File Deletes**

When considering how to leverage an arbitrary file delete on Windows, two great obstacles present themselves:

  1. Most critical Windows OS files are locked down with DACLs that prevent modification even by `SYSTEM`. Instead, most OS files are owned by `TrustedInstaller`, and only that account has permission to modify them. (Exercise for the reader: Find the critical Windows OS files that can still be deleted or overwritten by `SYSTEM`!)
  2. Even if you find a file that you can delete as `SYSTEM`, it needs to be something that causes a “fail-open” (degradation of security) if deleted.

A third problem that can arise is that some critical system files are inaccessible at all times due to sharing violations.

Experience shows that finding a file to delete that meets all the above criteria is very hard. When looking in the usual places, which would be within `C:\Windows`, `C:\Program Files` or `C:\ProgramData`, we’re not aware of anything that fits the bill. There is some [prior work](https://offsec.almond.consulting/intro-to-file-operation-abuse-on-Windows.html) that involves exploiting antivirus and other products, but this is dependent on vulnerable behavior in those products.

**The Solution is Found Elsewhere: Windows Installer**

In March of 2021, we received a [vulnerability report](https://www.zerodayinitiative.com/advisories/ZDI-21-965/) from researcher Abdelhamid Naceri ([halov](https://twitter.com/KLINIX5)). The vulnerability he reported was an arbitrary file delete in the User Profile service, running as `SYSTEM`. Remarkably, his submission also included a technique to parlay this file delete into an escalation of privilege (EoP), resulting in a command prompt running as `SYSTEM`. The EoP works by deleting a file, but not in any of the locations you would usually think of.

To understand the route to privilege escalation, we need to explain a bit about the operation of the Windows Installer service. The following explanation is simplified somewhat.

The Windows Installer service is responsible for performing installations of applications. An application author supplies an `.msi` file, which is a database defining the changes that must be made to install the application: folders to be created, files to be copied, registry keys to be modified, custom actions to be executed, and so forth.

To ensure that system integrity is maintained when an installation cannot be completed, and to make it possible to revert an installation cleanly, the Windows Installer service enforces transactionality. Each time it makes a change to the system, Windows Installer makes a record of the change, and each time it overwrites an existing file on the system with a newer version from the package being installed, it retains a copy of the older version. In case the install needs to be rolled back, these records allow the Windows Installer service to restore the system to its original state. In the simplest scenario, the location for these records is a folder named `C:\Config.Msi`.

During an installation, the Windows Installer service creates a folder named `C:\Config.Msi` and populates it with rollback information. Whenever the install process makes a change to the system, Windows Installer records the change in a file of type `.rbs` (rollback script) within `C:\Config.Msi`. Additionally, whenever the install overwrites an older version of some file with a newer version, Windows Installer will place a copy of the original file within `C:\Config.Msi`. This type of a file will be given the `.rbf` (rollback file) extension. In case an incomplete install needs to be rolled back, the service will read the `.rbs` and `.rbf` files and use them to revert the system to the state that existed before the install.

The service enforces transactionality during uninstalls as well. For example, to remove a previously installed file, the service moves the file from its installed location to `C:\Config.Msi`, giving the file a new, randomized name and the extension `.rbf`. Each time it makes a change to the system during the uninstall, the service records the change in an `.rbs` file, also located within `C:\Config.Msi`. If the uninstall runs into an error and needs to be rolled back, the `.rbs` file is consulted to determine what changes have already been made so that each can be reverted. If an installed file has been removed, as described above, a record in the `.rbs` indicates the relevant `.rbf` and the original path to which the file must be restored. Barring exceptional circumstances (more on this later), at the conclusion of any install or uninstall, _whether it was successful or rolled back_ , Windows Installer deletes `C:\Config.Msi` and all its contents.

This mechanism must be protected against tampering. If a malicious user were able to alter the `.rbs` and/or `.rbf` files before they are read, arbitrary changes to the state of the system could occur during rollback. Therefore, Windows Installer sets a strong DACL on `C:\Config.Msi`. Furthermore, to distinguish between a legitimate `C:\Config.Msi` and a fraudulent folder named `C:\Config.Msi` that may have been created by an attacker, Windows Installer uses a registry key located in the secure hierarchy rooted at `HKLM`. The full key name is `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\Folders`. Whenever creating a secure `C:\Config.Msi`, the service also creates a corresponding value within the above key, having the name `C:\Config.Msi`. The presence of this value indicates that `C:\Config.Msi` is a legitimate, strong-DACL folder that was created by the installer service and hence can be trusted. When deleting `C:\Config.Msi`, the installer service deletes the corresponding registry value. Should an attacker create their own folder at the location `C:\Config.Msi`, Windows Installer will not trust that folder, because the corresponding registry value will be absent.

Here is where an opening arises, though: What if an attacker has an arbitrary folder delete vulnerability? They could use it to delete a legitimate `C:\Config.Msi`, then recreate `C:\Config.Msi` with a weak DACL. The installer service will proceed to trust the new folder, even though the attacker has full control over its contents. Even though, before proceeding, Windows Installer checks the registry value described above, the check will succeed because the registry value remains in place. With full control over `C:\Config.Msi`, the attacker can place arbitrary `.rbs` and `.rbf` files there. In this way, the attacker can abuse the installer service to make arbitrary system changes during the rollback of an install or uninstall.

Note that the only required exploit primitive here is the ability to delete an empty folder. Moving or renaming the folder works equally well.

**From Arbitrary Folder Delete/Move/Rename to SYSTEM EoP**

In the original (March 2022) version of this blog, we detailed and released source code for Abdelhamid Naceri’s installer-based privilege escalation technique. A couple of drawbacks remained, however:

• The technique involved deleting and recreating `C:\Config.Msi` at a specific moment during an install. As a result, the timing considerations were somewhat tricky, and the exploit was less than fully reliable.

• A more serious consequence was that the exploit was inapplicable in cases where the attacker does not have the freedom to trigger the arbitrary folder delete in the middle of an install. A common scenario is when the arbitrary file delete occurs only upon system restart.

We are in luck, however, because in June of 2023, Abdelhamid Naceri submitted another case to ZDI that included an improved privilege escalation technique. Subsequently, I refined the technique even further, and together with the current version of this article, we are releasing details and [source code](https://github.com/thezdi/PoC/tree/main/FilesystemEoPs). The exploit now offers a very high degree of reliability and all race conditions have been eliminated. It has been tested on Windows 11 Enterprise 23H2 22631.4037 x64 (August 2024 patch level).

The essential new trick behind the improved technique is as follows: As noted above, when the installer service is performing an uninstall and wants to uninstall a file, it does not simply delete the file. That would make the uninstall difficult to roll back if an error occurs before the uninstall runs to completion. Instead, it moves the file to `C:\Config.Msi`, giving it a randomized name and the extension `.rbf`. In case of rollback, the installer service moves the file back to its original location and name. Note how this makes it easy for the installer service to preserve the file’s security descriptor. Therein lies a weakness, though: Since the file maintains the same DACL throughout, an attacker can obtain a handle to the `.rbf` file and keep the handle open, preventing its deletion at the end of the uninstall. The installer service won’t be able to delete `C:\Config.Msi`, either, because it is not an empty folder. Instead, the installer service will terminate without deleting `C:\Config.Msi`. Nor will it remove the registry value described above, since, from the installer service’s perspective, `C:\Config.Msi` is still a trusted folder with a strong DACL. Now, with the installer having run to completion, the attacker is free to trigger an arbitrary folder delete vulnerability to delete `C:\Config.Msi` at whatever time is most convenient, and subsequently re-create `C:\Config.Msi` with a weak DACL giving the attacker full control. The Windows Installer service will continue to trust `C:\Config.Msi` due to the presence of the registry value.

This trick allows splitting the exploit into two stages, with the arbitrary folder delete taking place in between the two stages:

• Stage 1: The exploit runs a successful install following by a successful uninstall, except that the exploit prevents deletion of `C:\Config.Msi` as detailed above.

• Between the stages, the attacker triggers the arbitrary folder deletion (or move or rename) to remove `C:\Config.Msi`. 

• Stage 2: The exploit recreates `C:\Config.Msi` with a weak DACL and launches an install that rolls back. Thanks to the attacker’s control over `C:\Config.Msi`, the attacker can force the rollback mechanism to consume fraudulent data within `C:\Config.Msi` and make arbitrary changes to the system. 

Note that the source code for this new exploit includes a new `.msi` file, different from the `.msi` file included with the earlier exploit source. This new `.msi` file is a bit more complex, having various special characteristics. Rather than enumerate them, which I believe would only be confusing to the reader, I will mention them in the course of the following chronological explanation of the EoP, each in its proper sequence.

The full mechanism of the new privilege escalation technique is as follows:

  1. **Stage 1 begins here.** Perform an install of the `.msi`. The `.msi` installs a single file, named `dummy.txt`, to a location determined by the variable `TARGETDIR`. The contents of `dummy.txt` are not relevant. The `.msi` has the “UAC Compliant” flag set, so that the installer service will permit a standard (non-admin) user to run the .msi. So that the install can succeed, we set `TARGETDIR` to a path that can be written by the attacker.
  2. Acquire a handle to the installed file `dummy.txt` within `TARGETDIR`.
  3. Initiate an uninstall. The following steps execute in parallel with the uninstall, until noted.
  4. Poll the handle to `dummy.txt`, calling `GetFinalPathNameByHandle`. Eventually, the uninstaller will move `dummy.txt` to `C:\Config.Msi` and change its filename to a randomized name with an `.rbf` extension. When the change in filename is detected, store the file’s new name in a variable, and close the file handle.
  5. The `.msi` contains a custom action named `SyncOnRbfWritten`, to be executed at sequence point 6503 during an uninstall (see tables `InstallExecuteSequence`, `CustomAction` and `Property` of the `.msi`). This sequence point occurs after the installer has finished preparing the `.rbf`. The custom action signals a named Windows event `FolderOrFileDeleteToSystem_RbfFullyWritten`, then waits on a second named Windows event `FolderOrFileDeleteToSystem_ReadyForAttemptedDelete`. This allows the PoC to perform the next step at exactly the right time during the uninstall.
  6. Wait until `FolderOrFileDeleteToSystem_RbfFullyWritten` is signaled (see previous step). Then, open a handle to the `.rbf`, but without the `FILE_SHARE_DELETE` file sharing flag. This will prevent the installer from deleting the `.rbf` (and, consequently, `C:\Config.Msi`) at the end of the uninstall.
  7. Signal `FolderOrFileDeleteToSystem_ReadyForAttemptedDelete`, allowing the uninstall to proceed. Wait for the uninstall to complete.
  8. Delete the `.rbf` file, so that `C:\Config.Msi` will be left as an empty folder. This concludes Stage 1.
  9. At this point, the attacker should trigger their arbitrary folder delete/move/rename vulnerability to remove `C:\Config.Msi`. Even if this requires a system restart, it poses no problem. Stage 2 may commence any time after the removal of `C:\Config.Msi`. The steps below detail Stage 2.
  10. **Stage 2 begins here.** Create `C:\Config.Msi` with a weak DACL and obtain a handle.
  11. Initiate an install of the `.msi`, setting `TARGETDIR` to a location writeable by the attacker, and also setting the `ERROROUT` variable. The following steps execute in parallel with the install, until noted.
  12. Begin a loop, calling `ReadDirectoryChangesW` to receive notifications of activity within `C:\Config.Msi`. Loop until the `.rbs` file created by the install is detected. Store the name of the `.rbs` file in a variable. (Detail: A bit of extra synchronization is performed to ensure that the install does not begin before we begin monitoring directory changes.)
  13. The `.msi` contains a custom action named `SyncBeforeRollback`, to be executed at sequence point 6501 during an install if the `ERROROUT` variable is set (see tables `InstallExecuteSequence`, `CustomAction` and `Property` of the `.msi`). This sequence point occurs after the installer has finished writing the `.rbs`. The custom action signals a named Windows event `FolderOrFileDeleteToSystem_RbsFullyWritten`, then waits on a second named Windows event `FolderOrFileDeleteToSystem_ReadyForRollback`. This allows the PoC to perform the next several steps at exactly the right time during the install.
  14. Wait for the event `FolderOrFileDeleteToSystem_RbsFullyWritten` (see previous step). Then, use the handle to `C:\Config.Msi` from step 10 above to reapply the weak DACL. (This is needed because the installer service has reapplied the correct, strong DACL in the interim. That would prevent us from tampering with the contents of `C:\Config.Msi` in the steps below, and, supposedly, should also prevent us from reapplying the weak DACL to `C:\Config.Msi` itself. Nevertheless, we can reapply the weak DACL to `C:\Config.Msi` because we the handle we have open from step 10 has `WRITE_DAC` access, and DACLs are checked only at the time a handle is opened, not at the time a handle is used.)
  15. Overwrite the `.rbs` file with a fraudulent version, and drop a fraudulent `.rbf` sibling to it within `C:\Config.Msi`. Together, the fraudulent `.rbs` and `.rbf` indicate that to roll back the install, the `.rbf` file (containing attacker-controlled data, which is a DLL) must be moved and renamed as specified in the `.rbs`.
  16. Signal the event `FolderOrFileDeleteToSystem_ReadyForRollback` so that the installer will proceed.
  17. The `.msi` contains a custom action (type 19) named `ErrorOut`, to be executed at sequence point 6502 if the `ERROROUT` variable is set. We have set that variable, so the install will encounter an error and begin rollback.
  18. The installer service consumes the fraudulent `.rbs` and `.rbf`, dropping the DLL.

**From Arbitrary File Delete to SYSTEM EoP**

The technique described above assumes a primitive that deletes an arbitrary empty folder. Often, though, one has a file delete primitive as opposed to a folder delete primitive. That was the case with Abdelhamid Naceri’s User Profile bug. To achieve `SYSTEM` EoP in this case, his exploit used one additional trick, which we will now explain.

In NTFS, the metadata (index data) associated with a folder is stored in an alternate data stream on that folder. If the folder is named `C:\MyFolder`, then the index data is found in a stream referred to as `C:\MyFolder::$INDEX_ALLOCATION`. Some implementation details can be found [here](http://inform.pucp.edu.pe/~inf232/Ntfs/ntfs_doc_v0.5/attributes/index_allocation.html). For our purposes, though, what we need to know is this: deleting the `::$INDEX_ALLOCATION` stream of a folder effectively deletes the folder from the filesystem, and a stream name, such as `C:\MyFolder::$INDEX_ALLOCATION`, can be passed to APIs that expect the name of a file, including `DeleteFileW`.

So, if you are able to get a process running as `SYSTEM` or admin to pass an arbitrary string to `DeleteFileW`, then you can use it not only as a file delete primitive but also as a folder delete primitive. From there, you can get a `SYSTEM` EoP using the exploit technique discussed above. In our case, the string you want to pass is `C:\Config.Msi::$INDEX_ALLOCATION`.

Be advised that success depends on the particular code present in the vulnerable process. If the vulnerable process simply calls `DeleteFileA`/`DeleteFileW`, you should be fine. In other cases, though, the privileged process performs other associated actions, such as checking the attributes of the specified file. This is why you cannot test this scenario from the command prompt by running `del C:\Config.Msi::$INDEX_ALLOCATION`.

**From Folder Contents Delete to SYSTEM EoP**

Leveling up once more, let us suppose that the vulnerable `SYSTEM` process does not allow us to specify an arbitrary folder or file to be deleted, but we can get it to delete the contents of an arbitrary folder, or alternatively, to recursively delete files from an attacker-writable folder. Can this also be used for EoP? Researcher Abdelhamid Naceri demonstrated this as well, in a subsequent submission in July 2021. In this submission he detailed a [vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-049) in the `SilentCleanup` scheduled task, running as `SYSTEM`. This task iterates over the contents of a temp folder and deletes each file it finds there. His technique was as follows:

  1. Create a subfolder, `temp\folder1`.
  2. Create a file, `temp\folder1\file1.txt`.
  3. Set an oplock on `temp\folder1\file1.txt`.
  4. Wait for the vulnerable process to enumerate the contents of `temp\folder1` and try to delete the file `file1.txt` it finds there. This will trigger the oplock.
  5. When the oplock triggers, perform the following in the callback:  
a. Move `file1.txt` elsewhere, so that `temp\folder1` is empty and can be deleted. We move `file1.txt` as opposed to just deleting it because deleting it would require us to first release the oplock. This way, we maintain the oplock so that the vulnerable process continues to wait, while we perform the next step.  
b. Recreate `temp\folder1` as a junction to the ‘\RPC Control`folder of the object namespace. c. Create a symlink at`\RPC Control\file1.txt`pointing to`C:\Config.Msi::$INDEX_ALLOCATION`.
  6. When the callback completes, the oplock is released and the vulnerable process continues execution. The delete of `file1.txt` becomes a delete of `C:\Config.Msi`.

Readers may recognize the symlink technique involving `\RPC Control` from James Forshaw’s [symboliclink-testing-tools](https://github.com/googleprojectzero/symboliclink-testing-tools). Note, though, that it’s not sufficient to set up the junction from `temp\folder1` to `\RPC Control` and then let the arbitrary file delete vulnerability do its thing. That’s because `\RPC Control` is not an enumerable file system location, so the vulnerable process would not be able to find `\RPC Control\file1.txt` via enumeration. Instead, we must start off by creating `temp\folder1\file1.txt` as a bona fide file, allowing the vulnerable process to find it through enumeration. Only afterward, just as the vulnerable process attempts to open the file for deletion, we turn `temp\folder1` into a junction pointing into the object namespace.

For working exploit code, see project `FolderContentsDeleteToFolderDelete`. Note that the built-in malware detection in Windows may flag this process and shut it down. I recommend adding a “Process” exclusion for `FolderContentsDeleteToFolderDelete.exe`.

You can chain these two exploits together. To begin, run `FolderOrFileDeleteToSystem` and wait for it to prompt you to trigger privileged deletion of `Config.Msi`. Then, run `FolderContentsDeleteToFolderDelete /target C:\Config.Msi`. It will prompt you to trigger privileged deletion of the contents of `C:\test1`. If necessary for your exploit primitive, you can customize this location using the `/initial` command-line switch. For testing purposes, you can simulate the privileged folder contents deletion primitive by running `del /q C:\test1\*` from an elevated command prompt. `FolderContentsDeleteToFolderDelete` will turn this into a delete of `C:\Config.Msi`, and this will enable `FolderOrFileDeleteToSystem` to drop the `HID.DLL`. Finally, open the On-Screen Keyboard and hit Ctrl-Alt-Delete for your `SYSTEM` shell.

**From Arbitrary Folder Create to Permanent DoS**

Before closing, we’d like to share one more technique we learned from this same researcher. Suppose you have an exploit primitive for creating an arbitrary folder as `SYSTEM` or admin. Unless the folder is created with a weak DACL, it doesn’t sound like this would be something that could have any security impact at all. Surprisingly, though, it does: it can be used for a powerful denial of service. The trick is to create a folder such as this one:

`C:\Windows\System32\cng.sys`

Normally there is no file or folder by that name. If an attacker name squats on that filesystem location with an extraneous file or even an empty folder, the Windows boot process is disrupted. The exact mechanism is a bit of a mystery. It would appear that Windows attempts to load the `cng.sys` kernel module from the improper location and fails, and there is no retry logic that allows it to continue and locate the proper driver. The result is a complete inability to boot the system. Other drivers can be used as well for the same effect.

Depending on the vulnerability at hand, this DoS exploit could even be a remote DoS, as nothing is required besides the ability to drop a single folder or file.

**Conclusion**

The techniques we’ve presented here show how some rather weak exploit primitives can be used for great effect. We have learned that:

• An arbitrary folder delete/move/rename (even of an empty folder), as `SYSTEM` or admin, can be used to escalate to SYSTEM.  
• An arbitrary file delete, as `SYSTEM` or admin, can usually be used to escalate to `SYSTEM`.  
• A delete of contents of an arbitrary folder, as `SYSTEM` or admin, can be used to escalate to `SYSTEM`.  
• A recursive delete, as `SYSTEM` or admin, of contents of a fixed but attacker-writable folder (such as a temp folder), can be used to escalate to `SYSTEM`.  
• An arbitrary folder create, as `SYSTEM` or admin, can be used for a permanent system denial-of-service.  
• An arbitrary file delete or overwrite, as `SYSTEM` or admin, even if there is no control of contents, can be used for a permanent system denial-of-service.

We would like to thank researcher Abdelhamid Naceri for his great work in developing these exploit techniques, as well as for the vulnerabilities he has been reporting to our program. We look forward to seeing more from him in the future. Until then, follow the team on [Twitter](https://www.twitter.com/thezdi), [Mastodon](https://infosec.exchange/@thezdi), [LinkedIn](https://www.linkedin.com/company/zerodayinitiative), or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Windows](/blog/tag/Windows)
  * [LPE](/blog/tag/LPE)
  * [Research](/blog/tag/Research)
  * [Exploit](/blog/tag/Exploit)

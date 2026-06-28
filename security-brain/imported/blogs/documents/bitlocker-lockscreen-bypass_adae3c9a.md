---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-15_bitlocker-lockscreen-bypass.md
original_filename: 2021-01-15_bitlocker-lockscreen-bypass.md
title: BitLocker Lockscreen bypass
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: adae3c9a0bd2ed5ac0e3752c61f8e58186002d27d213cd542175dedec0f0940f
text_sha256: 82028a8b5d5f05b35b3d7b5da33e7b4a17cf7802e3bb9a8891b71b87f8beb0e1
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# BitLocker Lockscreen bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-15_bitlocker-lockscreen-bypass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `adae3c9a0bd2ed5ac0e3752c61f8e58186002d27d213cd542175dedec0f0940f`
- Text SHA256: `82028a8b5d5f05b35b3d7b5da33e7b4a17cf7802e3bb9a8891b71b87f8beb0e1`


## Content

---
title: "BitLocker Lockscreen bypass"
page_title: "BitLocker Lockscreen bypass | secret club"
url: "https://secret.club/2021/01/15/bitlocker-bypass.html"
final_url: "https://secret.club/2021/01/15/bitlocker-bypass.html"
authors: ["Jonas L (@jonasLyk)"]
programs: ["Microsoft"]
bugs: ["Lock screen bypass", "Local Privilege Escalation", "Windows"]
publication_date: "2021-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3994
---

# BitLocker Lockscreen bypass

![main authors image](/assets/author_img/jonas-l.jpg) [Jonas L](/author/jonas-l)

Jan 15, 2021 

* * *

BitLocker is a modern data protection feature that is deeply integrated in the Windows kernel. It is used by many corporations as a means of protecting company secrets in case of theft. Microsoft recommends that you have a Trusted Platform Module which can do some of the heavy cryptographic lifting for you.

#  Bypassing BitLocker in 6 easy steps

Given a Windows 10 system without known passwords and a BitLocker-protected hard drive, an administrator account could be adding by doing the following:

  * At the sign-in screen, select “I have forgotten my password.”
  * Bypass the lock and enable autoplay of removable drives.
  * Insert a USB stick with my .exe and a junction folder.
  * Run executable.
  * Remove the thumb drive and put it back in again, go to the main screen.
  * From there launch narrator, that will execute a DLL payload planted earlier.

Now a user account is added called hax with password “hax” with membership in Administrators. To update the list with accounts to log into, click _I forgot my password_ and then return to the main screen.

##  Bypassing the lock screen

First, we select the “I have forgotten my password/PIN” option. This option launches an additional session, with an account that gets created/deleted as needed; the user profile service calls it a default-account. It will have the first available name of defaultuser1, defaultuser100000, defaultuser100001, etc.

To escape the lock, we have to use the Narrator because if we manage to launch something, we cannot see it, but using the Narrator, we will be able to navigate it. However, how do we launch something?

![](/assets/bitlockerbypass/1.png)

If we smash shift 5 times in quick succession, a link to open the Settings app appears, and the link actually works. We cannot see the launched Settings app. Giving the launched app focus is slightly tricky; you have to click the link and then click a place where the launched app would be visible with the correct timing. The easiest way to learn to do it is, keep clicking the link roughly 2 times a second. The sticky keys windows will disappear. Keep clicking! You will now see a focus box is drawn in the middle of the screen. That was the Settings app, and you have to stop clicking when it gets focus.

Now we can navigate the Settings app using CapsLock + Left Arrow, press that until we reach Home. Now, when Home has focus, hold down Caps Lock and press Enter. Using CapsLock + Right Arrow navigate to Devices and CapsLock + Enter when it is in focus.

![](/assets/bitlockerbypass/2.png)

Now navigate to AutoPlay, CapsLock + Enter and choose “Open Folder to view files (File Explorer).” Now insert the prepared USB drive, wait some seconds, the Narrator will announce the drive has been opened, and the window is focused. Now select the file **Exploit.exe** and execute it with CapsLock + Enter. That is arbitrary code execution, ladies and gentlemen, without using any passwords. However, we are limited by running as the default profile.

I have made a video with my phone, as I cannot take screenshots.

##  Elevation of privilege

When a USB stick is mounted, BitLocker will create a directory named ClientRecoveryPasswordRotation in System Volume Information and set permissions to:
  
  
  NT AUTHORITY\Authenticated Users:(F)
  NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
  

To redirect the create operation, a symbolic link in the NT namespace is needed as that allows us to control the filename, and the existence of the link does not abort the operation as it is still creating the directory.

Therefore, take a USB drive and make `\System Volume Information` a mount point targeting `\RPC Control`. Then make a symbolic link in `\RPC Control\ClientRecoveryPasswordRotation` targetting `\??\C:\windows\system32\Narrator.exe.local`. If the USB stick is reinserted then the folder `C:\windows\system32\Narrator.exe.local` will be created with permissions that allows us to create a subdirectory:
  
  
  amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.18362.657_none_e6c5b579130e3898
  

Inside this subdirectory, we drop a payload DLL named _comctl32.dll_. Next time the Narrator is triggered, it will load the DLL. By the way, I chose the Narrator as that is triggerable from the login screen as a system service and is not auto-loaded, so if anything goes wrong, we can still boot.

##  Combining them

The `ClientRecoveryPasswordRotation` exploit to work requires a symbolic link in `\RPC Control`. The executable on the USB drive creates the link using two calls to `DefineDosDevice`, making the link permanent so they can survive a logout/in if needed.

Then a loop is started in which the executable will:

  * Try to create the subdirectory.
  * Plant the payload `comctl32.dll` inside it.

It is easy to see when the loop is running because the Narrator will move its focus box and say “access denied” every second. We can now use the link created in `RPC Control`. Unplug the USB stick and reinsert it. The writeable directory will be created in `System32`; on the next loop iteration, the payload will get planted, and exploit.exe will exit. To test if the exploit has been successful, close the Narrator and try to start it again.

If the narrator does not work, it is because the DLL is planted, and Narrator executes it, but it fails to add an account because it is launched as `defaultuser1`. When the payload is planted, you will need to click back to the login screen and start Narrator; 3 beeps should play, and a message box saying the DLL has been loaded as `SYSTEM` should show. Great! The account has been created, but it is not in the list. Press “I forgot my password” and click back to update the list.

A new account named hax should appear, with password hax.

#  Making a malicious USB

I used these steps to arm the USB device
  
  
  C:\Users\jonas>format D: /fs:ntfs /q
  Insert new disk for drive D:
  Press ENTER when ready...
  -----
  File System: NTFS.
  Quick Formatting 30.0 GB
  Volume label (32 characters, ENTER for none)?
  Creating file system structures.
  Format complete.
  30.0 GB total disk space.
  30.0 GB are available.
  

Now, we need to elevate to admin to delete `System Volume Information`.
  
  
  C:\Users\jonas>d:
  D:\>takeown /F "System Volume Information"
  

This results in
  
  
  SUCCESS: The file (or folder): "D:\System Volume Information" now owned by user "DESKTOP-LTJEFST\jonas".
  

We can then
  
  
  D:\>icacls "System Volume Information" /grant Everyone:(F)
  Processed file: System Volume Information
  Successfully processed 1 files; Failed processing 0 files
  D:\>rmdir /s /q "System Volume Information"
  

We will use James Forshaw’s tool (attached) to create the mount point.
  
  
  D:\>createmountpoint "System Volume Information" "\RPC Control"
  

Then copy the attached exploit.exe to it.
  
  
  D:\>copy c:\Users\jonas\source\repos\exploitKit\x64\Release\exploit.exe .
  1 file(s) copied.
  

#  Patch

I disclosed this vulnerability and it was assigned CVE-2020-1398. Its patch can be found [here](https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2020-1398)

Tagged[ windows](/tags#windows) [PREVIOUSEscaping VirtualBox 6.1: Part 1 ](/2021/01/14/vbox-escape.html) [NEXTProcess on a diet: anti-debug using job objects ](/2021/01/20/diet-process.html)

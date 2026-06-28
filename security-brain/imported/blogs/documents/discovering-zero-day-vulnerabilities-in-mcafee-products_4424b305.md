---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-09_discovering-zero-day-vulnerabilities-in-mcafee-products.md
original_filename: 2021-07-09_discovering-zero-day-vulnerabilities-in-mcafee-products.md
title: Discovering Zero-Day Vulnerabilities in McAfee Products
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 4424b305c4b0488e9bbef262b32206e1c6ee6481c2dbbc881659ef6888d1077f
text_sha256: 8e7f0975a6f102d407307092ac0cd691eed742d04f27b09e359e9386f7994315
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Discovering Zero-Day Vulnerabilities in McAfee Products

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-09_discovering-zero-day-vulnerabilities-in-mcafee-products.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `4424b305c4b0488e9bbef262b32206e1c6ee6481c2dbbc881659ef6888d1077f`
- Text SHA256: `8e7f0975a6f102d407307092ac0cd691eed742d04f27b09e359e9386f7994315`


## Content

---
title: "Discovering Zero-Day Vulnerabilities in McAfee Products"
url: "https://mrd0x.com/discovering-mcafee-products-zero-day-vulnerabilities/"
final_url: "https://mrd0x.com/discovering-mcafee-products-zero-day-vulnerabilities/"
authors: ["mr.d0x (@mrd0x)"]
programs: ["McAfee"]
bugs: ["Local Privilege Escalation"]
publication_date: "2021-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3521
---

Discovery and exploitation of two Zero-Day vulnerabilities affecting Mcafee Agent < 5.7.4 and McAfee Drive Encryption < 7.2.9.5

# Introduction

At the beginning of 2021 I had some free time so I tried to find vulnerabilities in McAfee products. After a week of testing various techniques **I managed to discover two Zero-Day vulnerabilities**. Below I explain how I discovered and exploited them.

# Dumping SiteList.xml With User Privileges (CVE-2021-31836)

This vulnerability affects **McAfee Agent < 5.7.4** and requires normal user privileges.

Sitelist.xml is an important target when attacking machines with McAfee products. It contains UNC paths, usernames, server names, and encrypted passwords (which can be decrypted). In my [previous article](https://mrd0x.com/abusing-mcafee-vulnerabilities-misconfigurations/), I listed a few ways to find sitelist.xml. This vulnerability creates another way to get ahold of sitelist.xml.

## Discovering The Vulnerability

While looking around the McAfee Agent folder I found an interesting executable that comes with the agent. Maconfig.exe is a tool that can be used to dump sitelist.xml, the only problem is it requires administrator privileges.

If you try to run it from an account with low privileges you’ll get ‘Access is Denied’.

[ ![Access-Denied](/static/3bd249be94b16c6d6264607bca05f6d6/691c3/access_denied.png) ](/static/3bd249be94b16c6d6264607bca05f6d6/691c3/access_denied.png)

Fortunately, I noticed a problem with the permissions set on the parent folder which contains the executable maconfig.exe. A user with low privileges can copy and paste the parent folder to a different location and with that in mind, I copied the parent folder to my desktop and tried executing maconfig.exe and it ran!

[ ![Maconfig](/static/8d1242d7e386b6cf3ca6f313d2ec5f6b/0b5b1/maconfig_help.png) ](/static/8d1242d7e386b6cf3ca6f313d2ec5f6b/0b5b1/maconfig_help.png)

## Exploitation

Exploiting the vulnerability is extremely easy:

  1. Copy the folder “C:\Program Files\McAfee\Agent” to a location you have write access to (e.g. Desktop)
  2. Run the following command: **maconfig.exe -getsiteinfo [destination]**
  3. Use [this tool](https://github.com/funoverip/mcafee-sitelist-pwd-decryption) to decrypt the passwords in sitelist.xml

## Demo

![Maconfig-Demo](/4c9d22e1c9e1e8b37ad2451e77379afc/maconfig_demo.gif)

## Acknowledgment

[ ![Ack](/static/ba6b5d98f3ff961467f6615aefd2d919/6b9fd/ack.png) ](/static/ba6b5d98f3ff961467f6615aefd2d919/6b9fd/ack.png)

# DLL Hijacking For Privilege Escalation & Persistence

This vulnerability affects **McAfee Drive Encryption < 7.2.9.5** and requires local administrator privileges as a prerequisite.

I was able to execute any DLL upon the screen locking or unlocking. I was surprised at first because most (if not all) security vendors prevent any external DLLs from being injected into their processes. After a few hours of testing and analysis I eventually understood why this works.

## Discovery

Finding this vulnerability required some digging in the registry. Most McAfee registry keys cannot be edited due to tamper prevention/HIPS. Fortuantely, some keys are not protected by tamper prevention/HIPS and can be modified. Some of the unprotected registry keys contain paths to a McAfee DLL. Upon changing the path to a custom DLL, nothing happens, because McAfee prevents external DLLs from being injected… that is except for one key.
  
  
  Computer\HKEY_LOCAL_MACHINE\SOFTWARE\McAfee EndPoint Encryption\AppExtensions\MfeCryptoAdapter

This registry key contains ‘DllPath’ and the value can be modified by anyone with local administrator privileges. Upon setting this to a custom DLL, it will run everytime the screen is locked or unlocked.

[ ![Registry](/static/c90619b00dde91ab54d033e7b4da08de/29d31/registry.jpg) ](/static/c90619b00dde91ab54d033e7b4da08de/8a8a2/registry.jpg)

It turns out the reason this works is because the DLL isn’t injected into a McAfee process, rather it’s injected into the Logon User Interface (LogonUI.exe). And since LogonUI.exe runs with NT AUTHORITY/SYSTEM privileges, our DLL inherits those permissions.

## Exploitation

To exploit this vulnerability follow the steps below:

  1. Create your malicious dll (let’s call it evil.dll)
  2. Run the following command to modify the registry: **reg add “HKLM\SOFTWARE\McAfee EndPoint Encryption\AppExtensions\ MfeCryptoAdapter” /t reg_sz /v dllpath /d C:\path\to\malicious\dll\evil.dll**

## Demo

I created a simple DLL that launches Notepad.exe and modified the registry key to point to my DLL. You can lock the screen with cmd prompt using **rundll32.exe user32.dll,LockWorkStation**.

[ ![Notepad](/static/e723d1f952aaeb4dc51f3d525d7cbebb/29d31/notepad2.jpg) ](/static/e723d1f952aaeb4dc51f3d525d7cbebb/e0f57/notepad2.jpg)

We see below that notepad is launched with SYSTEM privileges.

[ ![Permissions](/static/5a8cb0a3018600b2889cd316914d5074/ebfc4/permission.jpg) ](/static/5a8cb0a3018600b2889cd316914d5074/ebfc4/permission.jpg)

## No CVE issued

Unfortunately after reporting this vulnerability to McAfee they replied with the following:

_We are not planning to put another CVE for the DLL Hijacking issue as fixing the registry keys will automatically get this resolved._

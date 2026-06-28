---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-20_slack-announcement-only-channel-post-restriction-bypass.md
original_filename: 2019-03-20_slack-announcement-only-channel-post-restriction-bypass.md
title: Slack announcement-only channel post restriction bypass
category: blogs
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- blogs
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 3298ceae610fcc2a99dfb9949bfe342bd0d3bf6d7d96f76dc75267817fa7a7e5
text_sha256: c6d07251789570d3e5c3b3eb1c44643148be0c1727870bacfecaae6dba7651bc
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Slack announcement-only channel post restriction bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-20_slack-announcement-only-channel-post-restriction-bypass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3298ceae610fcc2a99dfb9949bfe342bd0d3bf6d7d96f76dc75267817fa7a7e5`
- Text SHA256: `c6d07251789570d3e5c3b3eb1c44643148be0c1727870bacfecaae6dba7651bc`


## Content

---
title: "Slack announcement-only channel post restriction bypass"
url: "https://www.rodneybeede.com/security/slack-announcement-only-channel-post-restriction-bypass.html"
final_url: "https://www.rodneybeede.com/security/slack-announcement-only-channel-post-restriction-bypass.html"
authors: ["Rodney Beede"]
programs: ["Slack"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2019-03-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5349
---

# Slack announcement-only channel post restriction bypass

Last Modified: Wed, 20 Mar 2019 15:28:59 +0000 ; Created: Wed, 20 Mar 2019 12:00:00 +0000 

Slack is a messaging platform with channels for communication. One feature includes an announcement-only channel for communication to users. Only authorized users may post content to these channels as per: [Create an announcement-only channel, get.slack.help, Feb 21, 2019](https://get.slack.help/hc/en-us/articles/360004635551-Create-an-announcement-only-channel#enterprise-grid-plan-1).  The official Slack documentation states:  By limiting who can post, announcement-only channels are a great way to broadcast information to everyone in Slack. This type of channel becomes read-only to anyone without permission to post. Instead of the message field, members will see a message like this:  Your Workspace Owners have limited who can post to #announcements-global  However, I found a way for unauthorized users to bypass this restriction via the use of commonly added third party applications. One example is via the Simple Poll app. 

  1. Go to a channel that has restricted posting, such as #general, using a user who is not allowed to post new messages or thread replies
  2. Select a message posted in the channel by one of the authorized users
  3. Click on the ... menu for that message
  4. More message actions...
  5. Turn question into poll via Simple Poll add-on
  6. Post the poll with whatever text you want
  7. Notice (screenshot attached) that the poll appears for all users even though "Your Workspace Owners have limited who can post to #general

![](/images/Slack_vuln-496095.png)

### Analysis

This was just one example app. Many other apps could be used as well to do the same. The issue lies in that Slack at its core does not prevent apps from making this unauthorized post to an announcement-only channel and bypassing this security control.  Slack should not trust third party apps to restrict who can post to an announcement-only channel. Doing so at present will require uninstalling many third party apps used by customers to prevent this vulnerability. 

## Impact

In this case #general was locked down because everyone was in it and kept posting @here comments that annoyed people. An attacker, however, could post a phishing message with a malicious link to a channel such as #general which all employees would see in their Slack.  A Workspace Owners/org admin must monitor the channel and delete unauthorized posts to mitigate.  An attacker can also quickly delete the Poll post to minimize the chance of a legit admin seeing the post and determining who was phished. 

## Vendor Response

The vendor states that these security bugs must be addressed in the third party apps themselves. 

## Timeline

| Feb. 14, 2019 | Reported via Slack.com instructions to <https://hackerone.com/reports/496095>  
---|---  
Feb. 18, 2019 | Vendor replies they will not fix.  
Feb. 18, 2019 | Request to make report public  
Mar. 20, 2019 | 30 day mark and public disclosure  
  
![](/images/hackerone.com_reports_496095.png)

  * [GitHub Repositories](https://www.rodneybeede.com/curriculum%20vitae/GitHub-Repos.html)
  * [Cybersecurity Career Advice](https://www.rodneybeede.com/curriculum%20vitae/Cybersecurity_Career_Advice.html)
  * [Linux Guest will not Autoresize Display in VMWare Workstation Pro 25H2](https://www.rodneybeede.com/computer%20problems/Linux_Guest_will_not_Autoresize_Display_in_VMWare_Workstation_Pro_25H2.html)
  * [Network Adapter Disappears or No Media After Windows Resumes From Sleep](https://www.rodneybeede.com/computer%20problems/Network_Adapter_Disappears_or_No_Media_After_Windows_Resumes_From_Sleep.html)
  * [NanoPi R76S as a Router Benchmarks](https://www.rodneybeede.com/tech%20tricks/NanoPi_R76S_as_a_Router_Benchmarks.html)

* * *

  * [Computer Problems](/categories/Computer Problems.html)
  * [Curriculum Vitae](/categories/Curriculum Vitae.html)
  * [Free Stuff](/categories/Free Stuff.html)
  * [Games](/categories/Games.html)
  * [Misc](/categories/Misc.html)
  * [Programming](/categories/Programming.html)
  * [Security](/categories/Security.html)
  * [Tech Tricks](/categories/Tech Tricks.html)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-31_broken-access-control-leads-to-change-of-admin-details.md
original_filename: 2021-08-31_broken-access-control-leads-to-change-of-admin-details.md
title: Broken Access Control Leads To Change Of Admin Details
category: documents
detected_topics:
- access-control
- password-reset
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- password-reset
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 630a45f38ff459bcc56d880985e8909c91d86c7f617fd2d54d4e3576062b9c24
text_sha256: e40d36e622e68249799a94efa7025531124c7793954e33f5cf6e9ecc4345aab6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access Control Leads To Change Of Admin Details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-31_broken-access-control-leads-to-change-of-admin-details.md
- Source Type: markdown
- Detected Topics: access-control, password-reset, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `630a45f38ff459bcc56d880985e8909c91d86c7f617fd2d54d4e3576062b9c24`
- Text SHA256: `e40d36e622e68249799a94efa7025531124c7793954e33f5cf6e9ecc4345aab6`


## Content

---
title: "Broken Access Control Leads To Change Of Admin Details"
page_title: "BROKEN ACCESS CONTROL LEADS TO CHANGE OF ADMIN DETAILS | by V3D | Medium"
url: "https://v3d.medium.com/broken-access-control-leads-to-change-of-admin-details-a783e31729c4"
authors: ["V3D (@v3d_bug)"]
bugs: ["Privilege escalation", "Client-side enforcement of server-side security"]
publication_date: "2021-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3367
scraped_via: "browseros"
---

# Broken Access Control Leads To Change Of Admin Details

BROKEN ACCESS CONTROL LEADS TO CHANGE OF ADMIN DETAILS
V3D
Follow
3 min read
·
Aug 31, 2021

1K

2

Hi Fellow Hunters, hope you are doing well and taking care of your health in this pandemic situation, my name is V3D (Ved Parkash). I want to write a quick write-up on my recent finding which is a BROKEN ACCESS CONTROL LEADS TO CHANGE OF ADMIN DETAILS.

Without any Further ado.. Let’s Start.

Using Google Dorks, i started searching for private programs.

Here are some dorks for searching Private Bug Bounty Programs.

“powered by bugcrowd” -site:bugcrowd.com

“powered by hackerone” “submit vulnerability report”

Then i came across a program REDACTED.COM which i immediately started looking for bugs.

As usual I started with subdomain discovery and i got nearly 30 subdomains and after probing with httpx i got 20 alive subdomains. I started checking for functionalities that each subdomain has, there are only 2–3 subdomains with some functionality. I started checking bugs in Password Reset Functionality, Email Verification Functionality and checking for flaws in input sanitization. I am unable to find any bugs in these functionalities.

I recently read a write-up by @sunilyedla.

You can check it out here -> https://sunilyedla.medium.com/simple-sweet-bypassing-email-update-restriction-to-change-emails-of-team-members-6ce5770e7929

In this write-up, sunilyedla bhai came across a target in which users can invite other users in various different roles. I thought to check that functionality in my target since it also contains the same functionality where an admin can invite a user

I created two accounts an admin account and a user account to test the functionality. There is a section where a user can view the details of his account and the admin who invited him.

Get V3D’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

A user can

→ Invite other user

An admin can

→ Invite other user

→ Remove any user

Here user can edit his details but he can only view admin details and cannot edit them.

Press enter or click to view image in full size
Overview of User Account

Here i thought Let’s check if there is a flaw in Update Functionality. So i tried to update user details and to my surprise i can see the admin details are also being passed in the request. You know what to do know, Yeah you are right i changed the details of admin and to my surprise there is no back-end check and i successfully able to edit the details of admin.

To confirm the Vulnerability I opened the admin account in another browser to see whether the details are updated or not.

And they were successfully changed, i can edit the first name, last name and mobile number of admin. I quickly reported the issue and the team triaged it immediately but the severity is set to P4 by the team, I explained about the severity clearly to team and they bump it to P2.

Press enter or click to view image in full size

Tip: Never Forget To Check Functionality, there is a huge scope for finding bugs in Functionalities

Special Thanks to my dear brother’s: Aditya Shende, Sunil Yedla, Harsh Bothra, Manas Harsh, Aditya Sharma, Shubham Bhamare, 0xdln, The XSS Rat

Hope you learned something new. If you liked the write-up give it a clap and follow on twitter V3D

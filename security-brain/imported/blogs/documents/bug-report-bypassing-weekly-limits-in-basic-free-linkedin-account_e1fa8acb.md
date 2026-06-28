---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-16_bug-report-bypassing-weekly-limits-in-basic-free-linkedin-account.md
original_filename: 2022-02-16_bug-report-bypassing-weekly-limits-in-basic-free-linkedin-account.md
title: Bug Report; Bypassing Weekly Limits In Basic (Free) LinkedIn Account
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: e1fa8acb7cebc8e09254d9b9a687d6b23a735bd9bae9750fb0ea9b6920cb0d21
text_sha256: b2bedac508fdf5fbe7d0ef4733795b7b89c42d8fe03c84a35bb88ba729ffb756
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Report; Bypassing Weekly Limits In Basic (Free) LinkedIn Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-16_bug-report-bypassing-weekly-limits-in-basic-free-linkedin-account.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `e1fa8acb7cebc8e09254d9b9a687d6b23a735bd9bae9750fb0ea9b6920cb0d21`
- Text SHA256: `b2bedac508fdf5fbe7d0ef4733795b7b89c42d8fe03c84a35bb88ba729ffb756`


## Content

---
title: "Bug Report; Bypassing Weekly Limits In Basic (Free) LinkedIn Account"
url: "https://ashok314.medium.com/bug-report-bypassing-weekly-limits-in-basic-free-linkedin-account-f5265ac0418a"
authors: ["Ashok Acharya"]
programs: ["LinkedIn"]
bugs: ["Logic flaw"]
publication_date: "2022-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2902
scraped_via: "browseros"
---

# Bug Report; Bypassing Weekly Limits In Basic (Free) LinkedIn Account

Bug Report; Bypassing Weekly Limits In Basic (Free) LinkedIn Account
Ashok Acharya
Follow
4 min read
·
Feb 16, 2022

Publishing my first Security Vulnerability report for LinkedIn.Below is the report that I have submitted to LinkedIn Information Security Team.

— -Begin Report — -

Reported Issues
1. Reporting a flaw in LinkedIn connections, Bypassing Weekly limits in Basic (free) Account
Brief

LinkedIn user(with Free Basic Plan) was able to connect to unlimited users even after exceeding the “Weekly Limit”. There is a limit in how many people you can connect to in a week. After reaching the limit popup saying “you have reached your weekly limit” displays. If you go to responsive mode (normally in a browser by right mouse button and click “inspect”). After refreshing the page it goes to responsive mode. In this version, you can send “connection” requests to people even after you reached the limit.
The impact was, basic users, can bypass the weekly limit. Since this was a known issue, fixed by the LinkedIn team.

Reproduction Steps: Use a web browser and open LinkedIn in responsive mode (for web lite version). Stepwise as shown in following images
Browser used: Brave Browser, Chrome
OS: win 10,win 11
Linkedin : Web application
Severity: Medium

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Timeline

— — End of Issue 1 — -

2. The issue regarding the ability to connect to 3rd degree + connections
Brief

In this issue, the user was able to connect to the 3+ (Third plus) degree connections. These are different levels of connections in LinkedIn. 3+ are the people which are out of your network. Normally the name is displayed as a placeholder “LinkedIn Member”. These are higher than 3rd-degree connections. In a basic free plan, a user is not allowed to connect to them, Not even see their name or profile detail(can only see their position and company). With this info(position and company name), you can find out their name and profile by doing the same reproduction steps as issue 1 but with no connection to issue 1 at all. User can see their name and their profile, activity, etc which is not possible normally. This issue exposes the information(Name, profile details, activities)of the users to the outside networks and you are able to connect to them.
This issue was reported and and was not previously known, later verifierd and acknowlwdged by LinkedIn Security team and currently tested and fixed.

Reproduction Steps: Use a web browser and open LinkedIn in responsive mode (for web lite version). Stepwise as shown in following images
Browser used: Brave Browser, Chrome
OS: win 10,win 11
Linkedin : Web application
Impact: Medium
Information Security (User data, activity and privecy(via conncetion/message)): Medium

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Timeline
Press enter or click to view image in full size

— -End of Issue 2 — —

Get Ashok Acharya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

— End of Report — -

P.S.: I am new to both blogging and bug bounty. I may update the content(not the actual report, but the motivation, Drafts and report timeline, HackerOne’s Bounty programs, any related queries hereafter, etc. ) of this blog.

#linkedin #bug_bounty

Original: https://pi.hashnode.dev/linkedin-bug-report

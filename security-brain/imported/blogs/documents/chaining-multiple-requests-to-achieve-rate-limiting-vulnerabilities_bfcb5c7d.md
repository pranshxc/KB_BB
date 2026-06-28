---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-29_chaining-multiple-requests-to-achieve-rate-limiting-vulnerabilities.md
original_filename: 2020-11-29_chaining-multiple-requests-to-achieve-rate-limiting-vulnerabilities.md
title: Chaining Multiple Requests to Achieve Rate Limiting Vulnerabilities
category: documents
detected_topics:
- rate-limit
- sso
- command-injection
tags:
- imported
- documents
- rate-limit
- sso
- command-injection
language: en
raw_sha256: bfcb5c7d37dc36ab37952f0dc76ac2485f0cf404f1c4e40a1f5e8ee45447e626
text_sha256: 2ec2257f348c09aa7d1a6d9784710ed892fe9fd07724e9db57b5ccfa7d7ea81d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Multiple Requests to Achieve Rate Limiting Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-29_chaining-multiple-requests-to-achieve-rate-limiting-vulnerabilities.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `bfcb5c7d37dc36ab37952f0dc76ac2485f0cf404f1c4e40a1f5e8ee45447e626`
- Text SHA256: `2ec2257f348c09aa7d1a6d9784710ed892fe9fd07724e9db57b5ccfa7d7ea81d`


## Content

---
title: "Chaining Multiple Requests to Achieve Rate Limiting Vulnerabilities"
url: "https://ahmdhalabi.medium.com/chaining-multiple-requests-to-achieve-rate-limiting-vulnerabilities-96c1e8365c06"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["Rate limiting bypass"]
bounty: "1,000"
publication_date: "2020-11-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4102
scraped_via: "browseros"
---

# Chaining Multiple Requests to Achieve Rate Limiting Vulnerabilities

Chaining Multiple Requests to Achieve Rate Limiting Vulnerabilities
Ahmad Halabi
Follow
4 min read
·
Nov 30, 2020

523

3

Hello,

I want to share with you a new methodology about finding rate limit vulnerabilities and even bypassing rate limit protections.

For those who don’t know me, my name is Ahmad Halabi and I am a part time bug bounty hunter.

Overview ::

A lot of programs and companies implement Rate Limiting protections on sensitive endpoints that requires authentication and important functionalities like Login and creating posts as an example. Protections can vary a lot, and since there are multiple types and ways how protections are implemented, there are also methods to bypass some of these protections.

Today I am going to talk about a vulnerability that I found in a public program on hackerone that focuses on Rate Limiting protection as one of its top security priorities.

Chaining Multiple Requests to achieve Rate Limiting vulnerability which was Sending Unlimited Collaboration Invites

The program generally contains Algorithm section in the page where you can add collaborator to work with you on your project.
When you add a collaborator, a notification is sent to his email telling him to join you as a collaborator.
You can invite a user just once, unless you removed him from collaborator and re-invited him.

Through the above feature, I found a bug by chaining three requests add_collaborator , normal request and remove_collaborator I was able to create a thing in burp called Macro that lead me send notifications to a target user unlimited times by performing the below steps:

Perform add collaborator request.
Send normal request to www.target.com.
Perform remove collaborator request.

And repeating the above three steps in an automated way will result in bombing victim’s mailing system with collaboration invites.

Steps To Reproduce ::

To prove the existence of the bug in the basic way, all you need is to add a collaborator, remove it, and then add it again and remove it. You will receive two notifications to that user mail inbox.

If you want to do it in advanced way, you can create a script that automate the add, remove collaborator process and repeats itself every time. Or you can use burp as well. I used burp Macro feature.

Keep burp proxy running and Perform add collaborator and remove collaborator and navigate to your account.
Collaboration Settings
In burp, navigate to Project Options -> Under Session Handling Rules click Add -> In Rule Actions click Add then choose Run a Macro.
Under Select Macro click Add -> Burp requests history will open, now choose the three requests in order: Add collaborator — Request to profile account — Remove collaborator. Click Ok and then click Test macro and see that a notification is sent to the target email inbox.
Press enter or click to view image in full size
Launching Macro Attack
You can try Test macro many times and every time you try it, a notification will be sent to the mail inbox.
Press enter or click to view image in full size
Notifications sent to victim inbox

Automating this attack will lead to huge mass mailing victim inbox.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Impact ::

Abuse sending collaboration invites to any user, large scaled attack will blow up users mailing system with huge number of invites.

Why this Vulnerability Arises ::

Simply because the program didn’t expect chaining three requests to achieve rate limiting on collaboration invites.

Remediation ::

Applying rate limit protection for the Add Collaborator and Remove Collaborator requests.

Lesson Learned from this bug ::

If you depend on multiple requests to perform your certain action, don’t just rely on them as a protection, you should also implement sort of rate limiting protection because multiple requests can be chained to exploit rate limiting.

Report Timeline ::

19 Sep, 2020 : Initial Report.

2 Nov, 2020 : Report Triaged.

24 Nov, 2020: Bounty Awarded ($1,000).

24 Nov, 2020: Report Resolved.

For those who didn’t read my article yet about how I started bug bounty hunting, how I ranked 1st at U.S. Dept Of Defense (2019) and how I reached top 100 hackers on hackerone, You can find it below.

My Bug Bounty Journey & Ranking 1st in U.S. DoD & Achieving top 100 hackers in 1 year
I am sharing some of my methodology, recourses, tips and advices to become a better bug bounty hunter.

ahmdhalabi.medium.com

The article also contains all needed resources to start and a lot of valuable tips.

Good luck :)

Ahmad Halabi
Security Researcher

ahmadhalabi.net

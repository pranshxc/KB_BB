---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-22_reflected-xss-leads-to-3000-bug-bounty-rewards-from-microsoft-forms.md
original_filename: 2023-01-22_reflected-xss-leads-to-3000-bug-bounty-rewards-from-microsoft-forms.md
title: Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 4b36143680459ca51b1c517a42e4b12fb79f0d02d22c225f5e3e77669aaa7296
text_sha256: f631555288be80ccb5db510aeb954649b103f77bcde9695ce09caac62c9721fa
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-22_reflected-xss-leads-to-3000-bug-bounty-rewards-from-microsoft-forms.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `4b36143680459ca51b1c517a42e4b12fb79f0d02d22c225f5e3e77669aaa7296`
- Text SHA256: `f631555288be80ccb5db510aeb954649b103f77bcde9695ce09caac62c9721fa`


## Content

---
title: "Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms"
url: "https://infosecwriteups.com/reflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261"
authors: ["Supakiad S. (@Supakiad_Mee)"]
programs: ["Microsoft"]
bugs: ["Reflected XSS"]
bounty: "3,000"
publication_date: "2023-01-22"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1638
scraped_via: "browseros"
---

# Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms

Top highlight

Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms
Supakiad S. (m3ez)
Follow
3 min read
·
Jan 22, 2023

348

5

Microsoft Forms Vulnerability: Reflected Cross-site Scripting (XSS)

Table of Contents
Introduction
Background
Details of the Vulnerability
Proof of Concept
Disclosure Timelines
Introduction

In this blog post, I will discuss the details of a reflected cross-site scripting (XSS) vulnerability in Microsoft Forms.

Press enter or click to view image in full size

Additionally, in my last blog post, I disclosed a vulnerability report on Microsoft Power Apps and dove into the processes of reporting. You can refer to my previous post on: Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022) for more detailed information on the process of reporting and claiming rewards through MSRC platform.

Background

Microsoft Forms is a popular web-based tool for creating surveys, quizzes, and other forms. It allows users to create forms and surveys, share them with others, and collect responses in a centralized location. However, we discovered that it is possible to inject malicious JavaScript code into the forms, which can be executed by unsuspecting users.

I followed the MSRC’s guidelines for reporting vulnerabilities and submitted my findings. For more information, please refer to:

Example Report Submissions to the MSRC
Microsoft Bounty Programs | MSRC
FAQs — Report an issue and submission guidelines (microsoft.com)
Details of the Vulnerability:

The vulnerability lies in the way Microsoft Forms processes user input. Specifically, it fails to properly validate user input, allowing an attacker to inject malicious JavaScript code into the id parameter. An attacker can generate a malicious link with injected XSS Payload, they can take advantage of this vulnerability to take over authenticated accounts or perform state-changing actions with authenticated users’ sessions in the application, or even use a vulnerable domain to make a phishing page and etc.

Vulnerable product: Microsoft Forms

Vulnerable URL: https://forms.office.com/pages/responsepage.aspx

Get Supakiad S. (m3ez)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Vulnerable Parameter: id

Reflected XSS (Cross-Site Scripting) is a type of web vulnerability that allows an attacker to inject malicious code into a website, which is then executed by the victim’s browser. This happens when the website includes untrusted user input in its pages without proper validation or encoding. The attacker crafts a special link or form that, when clicked or submitted by the victim, causes the victim’s browser to execute the malicious code. The victim’s browser is tricked into thinking the code is part of the website, allowing the attacker to steal sensitive information or perform other malicious actions

Exploitation:

To exploit this vulnerability, an attacker would need to craft a specially-crafted link that contains the malicious JavaScript code. The attacker would then need to trick the user into clicking on the link, which would cause the code to be executed. This could be done through social engineering tactics, such as phishing emails or instant messaging.

Proof of Concept:

Here is an example of a proof of concept that demonstrates the vulnerability:

1. Navigated to URL:

https://forms.office.com/Pages/ResponsePage.aspx

2. Injected XSS payload into id parameter value and added to a vulnerable URL from step 1.

The payload was used:

d1bvs%3c%2fscript%3e%3cscript%3ealert(`XSS`)%3c%2fscript%3ec579g

Example injected Link:

https://forms.office.com/pages/responsepage.aspx?id=d1bvs%3c%2fscript%3e%3cscript%3ealert(`XSS`)%3c%2fscript%3ec579g

3. Open the URL in step 2.

4. When users open the XSS inject link, the XSS payload will be triggered and executed as shown below.

Press enter or click to view image in full size
https://youtu.be/pjbaZYEYQV8
Disclosure Timelines
Sep 27, 2022 — Vulnerability Discovered and Reported through MSRC portal.
Sep 29, 2022 — MSRC team confirmed. MSRC ticket was moved to Review/Repro.
Oct 4, 2022 — Bounty awarded and MSRC case status was changed from Review / Repro to Develop
Oct 21, 2022 — MSRC status was changed to Pre-Release and Complete.
Jan 22, 2023 — Public release of the security advisory.

I appreciate your feedback and would love to hear your thoughts on my blog. If you have any comments or suggestions, please feel free to reach out to me on LinkedIn or Twitter.

LinkedIn: Supakiad S.

Twitter: (@Supakiad_Mee)

Thank you for your support!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-20_hacking-apple-security-report-system.md
original_filename: 2021-11-20_hacking-apple-security-report-system.md
title: Hacking Apple Security Report System
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 1538777ab2da8d1a2cbd6394bb8fe8190926299d6c88ac841820663be8d0a914
text_sha256: f316c82f1993346d2c0e1c1dafd3d17964326661edaa3d64f1249a899c9fe195
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Apple Security Report System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-20_hacking-apple-security-report-system.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `1538777ab2da8d1a2cbd6394bb8fe8190926299d6c88ac841820663be8d0a914`
- Text SHA256: `f316c82f1993346d2c0e1c1dafd3d17964326661edaa3d64f1249a899c9fe195`


## Content

---
title: "Hacking Apple Security Report System"
url: "https://hackrzvijay.medium.com/hacking-apple-security-report-system-db84850002fb"
authors: ["HackrzVijay (@hackrzvijay)"]
programs: ["Apple"]
bugs: ["Logic flaw", "Social engineering"]
publication_date: "2021-11-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3154
scraped_via: "browseros"
---

# Hacking Apple Security Report System

Hacking Apple Security Report System
hackrzvijay
Follow
4 min read
·
Nov 20, 2021

14

Hacking apple security report system

Hello!
This article is about i found a bug in apple security report system while i reported several reports to apple product security.
Apple security has 9 digit number system for example like 123654987 to provide followup to their reports but this system can be hacked to update the reports as well as to gain information from the reports.
I have tested only on my reports by using my 2 test emails.
ADDING COMMENTS TO VICTIM REPORTS OR UPDATING THE VICTIM REPORTS
For test i have submitted the reply to credit my actual report with other email using the victim report id.
In the below image you can see the attacker email xxxkar4@gmail.com is replying to the victim report id XXXXXX552 to credit the information like below.
Press enter or click to view image in full size
After one day i got the reply to the attackers email XXXkar4@gmail.com mentions that the credit is updated in the records and the reply is sent to the attackers email not the victim email you can see below image.
Press enter or click to view image in full size
GETTING INFORMATION OF SECURITY REPORTS
Next for testing i have tried to retrieve the information like title of my report using the attackers email XXXXkar4@gmail.com with the victim report id XXXXXX885
Press enter or click to view image in full size
After 3 days i got the reply about the title of the report to the attackers email XXXXkar4@gmail.com
Press enter or click to view image in full size
Get hackrzvijay’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On FEB 6 2021 i reported this bug to the apple security team
And next day i got the response that they are investigating the issue.
On may 14 2021 After some delay like 3 months i got the below response from apple “They said that they are planning to address this issue in future security update”
Press enter or click to view image in full size
On jun 18 2021 i got reply from apple security they said that “They will address the issue with long term solution” view the below image.
Press enter or click to view image in full size
Next i have asked for updates for months.
On september 17 2021 i got the response from apple security saying that “They are unable locate the report with XXXXXX315” They asked email and also asked to very the report id which i submitted with.
Press enter or click to view image in full size
On October 12 2021 i got reply from apple security To the original report i.e XXXXXX315 saying that “This is not treated as security issue”.
Press enter or click to view image in full size

on October 12th 2021 i have made a writeup and sent them for approval for blog post.

Press enter or click to view image in full size

On October 15th 2021 they reply about the bug fix and asked for hall of fame credit.

Press enter or click to view image in full size

I asked about the bounty and on November 5th 2021 they replied that this bug is not eligible under apple security bounty because it rely on social engineering.

Press enter or click to view image in full size
IMPACT:
The security reports are in number format so attacker will reply to the reports and also can get information from the reports.

Follow me on twitter

Thanks!

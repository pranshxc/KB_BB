---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-23_the-neglected-bug-that-can-infect-all-facebook-users-who-pay-for-leads-ads.md
original_filename: 2019-04-23_the-neglected-bug-that-can-infect-all-facebook-users-who-pay-for-leads-ads.md
title: The neglected bug that can infect All Facebook users who pay for leads ads.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 80a4b932cf15da90b8e67d17ebe07dd955fb723e931fb253d9af928c16d75e17
text_sha256: 5651fc857ba694791406ed19b61c48b9106d95f9895850cef40b3ecae2e0e119
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# The neglected bug that can infect All Facebook users who pay for leads ads.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-23_the-neglected-bug-that-can-infect-all-facebook-users-who-pay-for-leads-ads.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `80a4b932cf15da90b8e67d17ebe07dd955fb723e931fb253d9af928c16d75e17`
- Text SHA256: `5651fc857ba694791406ed19b61c48b9106d95f9895850cef40b3ecae2e0e119`


## Content

---
title: "The neglected bug that can infect All Facebook users who pay for leads ads."
url: "https://medium.com/@heshamwatany/the-neglected-bug-that-can-infect-all-facebook-users-who-pay-for-leads-ads-8c374cd64d76"
authors: ["Hesham Watany"]
programs: ["Meta / Facebook"]
bugs: ["CSV injection"]
publication_date: "2019-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5294
scraped_via: "browseros"
---

# The neglected bug that can infect All Facebook users who pay for leads ads.

The neglected bug that can infect All Facebook users who pay for leads ads.
Hesham Watany
Follow
3 min read
·
Apr 23, 2019

2

Press enter or click to view image in full size
Photo by Con Karampelas on Unsplash

If you are paying for lead generation form in Facebook beware, your computer could be infected, your leads could be hacked.

When you make an ad that asks the Facebook user to put his contact information to call him later, you regularly check the new leads by downloading the excel/CSV file.

This file can be easily infected by any user by just entering any spreadsheet formula in the form which can execute any command in your sheet and also in your computer.

The funny part is if any user enters any formula that open cmd (windows command line) or any other program the file that you downloaded from facebook is considered infected and may contain a virus.
Example of opening calculator using spreadsheet formula
(=cmd|’ /C calc’!A0 ).

By this ability any user can run commands in your computers, can download files to your computers and run it.

Get Hesham Watany’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can avoid it by upgrading your antivirus and your operating system regularly, or just don’t download the leads that you paid for.

Example of lead generation form that we use every day
Video Proof of concept:
Facebook Lead Form Ads Formula CSV Injection by Hesham Watany
Technical stuff….

This bug considered as a security bug in the OWASP top 10 critical risks.

CSV Injection - OWASP
When a spreadsheet program such as Microsoft Excel or LibreOffice Calc is used to open a CSV, any cells starting with…

www.owasp.org

I have tried to report it to the security team, but they didn’t find it a security problem from their side.

…..and they replied

Then I tried to explain more how dangerous it is

…. they still see that this is not a security problem.

The Facebook security team is always working on making the platform safer for all of us.

Maybe they are wrong, maybe I am, but this security bug could really harm users computers.

However till they fix it, make sure that your computer and your leads are safe.

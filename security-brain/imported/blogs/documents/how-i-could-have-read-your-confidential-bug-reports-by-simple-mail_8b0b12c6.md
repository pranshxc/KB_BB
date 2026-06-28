---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-could-have-read-your-confidential-bug-reports-by-simple-mail.md
original_filename: 2022-01-25_how-i-could-have-read-your-confidential-bug-reports-by-simple-mail.md
title: How I could have read your confidential bug reports by simple mail?
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: 8b0b12c67717757487c8400fc680c1f799be1d0a2454442a384935977e64d96e
text_sha256: 5078e62a9a974a6402ee4cedf2b87912c59dcd7b8d034ee567f000d9b6e815f1
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have read your confidential bug reports by simple mail?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-could-have-read-your-confidential-bug-reports-by-simple-mail.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `8b0b12c67717757487c8400fc680c1f799be1d0a2454442a384935977e64d96e`
- Text SHA256: `5078e62a9a974a6402ee4cedf2b87912c59dcd7b8d034ee567f000d9b6e815f1`


## Content

---
title: "How I could have read your confidential bug reports by simple mail?"
url: "https://infosecwriteups.com/how-i-could-have-read-your-confidential-bug-reports-by-simple-mail-cfd2e4f8e25c"
authors: ["Sudhakar Muthumani (@Sudhakarmuthu04)"]
programs: ["Microsoft"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2022-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2980
scraped_via: "browseros"
---

# How I could have read your confidential bug reports by simple mail?

Press enter or click to view image in full size
Source: Internet
How I could have read your confidential bug reports by simple mail?
Sudhakar Muthumani
Follow
3 min read
·
Jan 25, 2022

62

Hey Everyone, Hope you’re doing safe and sound.

I have recently found a bug in the Microsoft research portal which could have let me read the bug report updates of fellow security researchers who report to Microsoft, this was a simple yet interesting thing I found while I was randomly exploring it.

What was the bug?

It was an information disclosure bug, Which discloses information of the report updates by having the vulnerability report ID.

Press enter or click to view image in full size
How to get the vulnerability report ID?

The vulnerability report ID is VULN-<Some number>. This is the unique identifier for every report. Microsoft validates the bug report by this ID. For every bug report, they give an ID which is a number like 010001 followed by 010002, which is easily guessable.

How to reproduce the bug?
Report a bug from User A.
Send a mail from User B’s mail ID to Microsoft’s vulnerability report mail ID, saying some info with the subject line of VULN-<the report number>
Now, User B is added to the ticketing portal of Microsoft.

Now, User B can receive updates of User A’s Bug report without his knowledge.

How the bug could have affected Microsoft?

Get Sudhakar Muthumani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If the attacker sends an automated mail by changing the report number to Microsoft’s mail ID then he could have listened to the bug report updates. If any sensitive information is sent via mail, then the attacker can use it for any malicious purposes.

Source: Internet

This bug was assigned as Important by Microsoft and fixed it. This was not awarded bounty because it was out of scope as per the Microsoft terms.

Thanks for reading, good day! :-)

Timeline:

Bug reported on 01/07/2021

Bug assigned on 21/07/2021

Sent to the development team on 16/09/2021

Bug fixed on 21/10/2021

Note: This blog was approved by Microsoft

Follow me on:

Instagram: https://www.instagram.com/sudhakar_._m/

Facebook: https://www.facebook.com/sudhakarmuthumani00

Twitter: https://twitter.com/Sudhakarmuthu04

Linkedin: https://www.linkedin.com/in/sudhakarmuthumani/

🔈🔈Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.

IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live

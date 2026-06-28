---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-24_break-the-logic-insecure-parameters-300.md
original_filename: 2022-08-24_break-the-logic-insecure-parameters-300.md
title: 'Break the Logic: Insecure Parameters (€300)'
category: documents
detected_topics:
- api-security
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- api-security
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: 7a7a0a43b70ec93fcd917ead0f7edaee6c1b13b4b2cdd840d3a1345926c0e21f
text_sha256: 15df1f5f9d4a98cd14d76d23537bb30628388e70800334dccf6224dc1539f202
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Break the Logic: Insecure Parameters (€300)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-24_break-the-logic-insecure-parameters-300.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `7a7a0a43b70ec93fcd917ead0f7edaee6c1b13b4b2cdd840d3a1345926c0e21f`
- Text SHA256: `15df1f5f9d4a98cd14d76d23537bb30628388e70800334dccf6224dc1539f202`


## Content

---
title: "Break the Logic: Insecure Parameters (€300)"
url: "https://canmustdie.medium.com/break-the-logic-insecure-parameters-300-e655cc4fcc42"
authors: ["can1337 (@canmustdie)"]
bugs: ["Parameter manipulation", "Logic flaw", "Mass assignment"]
bounty: "300"
publication_date: "2022-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2268
scraped_via: "browseros"
---

# Break the Logic: Insecure Parameters (€300)

Top highlight

Break the Logic: Insecure Parameters (€300)
can1337
Follow
4 min read
·
Aug 24, 2022

422

4

Hello everyone. Today, I’m going to talk about two minor vulnerabilities based on insecure parameters that I discovered in the same program. This will be a short story and I will call it as “redacted.com” cause the company runs a private program. So, let’s get started.

I. Bypassing mail verification using insecure parameters

redacted.com has 2 mail features, primary mail and extra mail. A user with primary mail can add extra mail. However, to make the extra mail the primary mail, the app needs to send a verification code to the extra mail.
So, the extra mail cannot be converted to the primary mail without confirmation.

First, let’s analyze how this process takes place under normal conditions.

1- I entered a mail in the extra mail section and observed that verification is required for the mail.

(As you can see in the picture, it sends a confirmation mail and our two options next to the field are “resend” or “delete” the mail.)

2- I ran Burp Suite and went back to the page. I entered an email again and got the request.

3- Two insecure parameters as “activated” and “for student verification” would return false, I changed both to true and submit the request.

4- I went back to redacted.com and I saw a tick button next to the email field. I clicked the tick button and refreshed the page.

Finally, the extra mail has moved to the primary mail section, the old primary mail has become an extra mail.

II. Bypassing study verification using hidden insecure parameter

At redacted.com, users can add custom “study” information. However, for this the study information must be verified and approved by the management first.
I mean, there is a verification process when users add their custom study information. Verification is done directly by redacted.com management.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But, a hidden insecure parameter can make users’ custom study information look like they’ve already been approved, and eventually actually get approved.

Let’s analyze it.

1- As I said, in the “I study” field, we can add our own special study information. For example, let’s type “admin” and send the request.

2- I ran Burp Suite and I sent the request again by typing “admin”.

3- The request was as above. I didn’t see anything of interest so I submitted the request and reviewed the response. In response, I saw a parameter “isVisible:” was set to false.

4- I resubmitted the request and added the parameter “isVisible:true” to the end of the request.

I refreshed the page and saw that the information I added appeared directly on my profile.

In this way, attackers would be able to add any information they wanted, bypassing the verification.

The bugs has been fixed and company was rewarded me with €300 for these two minor bugs.

That’s all for now. Thanks for reading. See you in another write up!

You can follow me on twitter: https://twitter.com/canmustdie

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

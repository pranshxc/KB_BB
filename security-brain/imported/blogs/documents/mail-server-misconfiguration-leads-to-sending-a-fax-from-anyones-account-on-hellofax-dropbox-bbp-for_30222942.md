---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-25_mail-server-misconfiguration-leads-to-sending-a-fax-from-anyones-account-on-hell_2.md
original_filename: 2022-07-25_mail-server-misconfiguration-leads-to-sending-a-fax-from-anyones-account-on-hell_2.md
title: Mail Server Misconfiguration leads to sending a fax from anyone’s account on
  HelloFax (Dropbox BBP) for a bounty of $4,913
category: documents
detected_topics:
- access-control
- idor
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 30222942952d0f234761b348e13e32946b7807a37f88690adfd2038f06fb593b
text_sha256: c484cb74c06435206a0d84ed2d07a047f271ffb3ee92da4af72da43a1b8f579b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Mail Server Misconfiguration leads to sending a fax from anyone’s account on HelloFax (Dropbox BBP) for a bounty of $4,913

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-25_mail-server-misconfiguration-leads-to-sending-a-fax-from-anyones-account-on-hell_2.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `30222942952d0f234761b348e13e32946b7807a37f88690adfd2038f06fb593b`
- Text SHA256: `c484cb74c06435206a0d84ed2d07a047f271ffb3ee92da4af72da43a1b8f579b`


## Content

---
title: "Mail Server Misconfiguration leads to sending a fax from anyone’s account on HelloFax (Dropbox BBP) for a bounty of $4,913"
url: "https://infosecwriteups.com/mail-server-misconfiguration-leads-to-sending-a-fax-from-anyones-account-on-hellofax-dropbox-bbp-aab3d97ab4e7"
authors: ["Sayaan Alam (@ehsayaan)"]
programs: ["Dropbox"]
bugs: ["Email spoofing"]
bounty: "4,913"
publication_date: "2022-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2404
scraped_via: "browseros"
---

# Mail Server Misconfiguration leads to sending a fax from anyone’s account on HelloFax (Dropbox BBP) for a bounty of $4,913

Mail Server Misconfiguration leads to sending a fax from anyone’s account on HelloFax (Dropbox BBP) for a bounty of $4,913
Sayaan Alam
Follow
4 min read
·
Jul 25, 2022

142

1

Hi Everyone!,

Hope you all are doing well :)

This article is about my recent finding of a mail server misconfiguration among multiple targets that allowed me to perform unauthorized actions on vulnerable web applications, This vulnerability is common among multiple targets and different types of web applications. Dropbox fixed the issue and awarded me a bug bounty of $4,913.

Description

I was working on the HelloFax application at Dropbox BBP and looking for auth issues but the application is well sanitized against authorization issues such as IDOR and Access Control so I thought to look for more interesting functionalities, I found a functionality that allows users to send a fax using their email without logging into their HelloFax account

Press enter or click to view image in full size

So , when a paid user sends an email to FAXNUMBER@hellofax.com, the application sends the content of the email as a fax to FAXNUMBER from the user’s HelloFax account, For eg. If I send an email 13456789000@hellofax.com, then the application sends a fax to +13456789000 from my HelloFax account

Exploitation

Here the first thing that came to my mind was to send a fake email to FAXNUMBER@hellofax.com by putting the victim’s email into FROM field, I quickly went to http://anonymailer.net/ and sent a fake email to +12345678900@hellofax.com, Surprisingly it worked well and I received this mail from HelloFax

Press enter or click to view image in full size

This email says that our fax has been sent successfully and the mail server at Hellofax did not verify the authenticity of the fake email sent by me and it sent the email from the victim’s account

Get Sayaan Alam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here is how the vulnerability works:-

Target allows us to perform an action by sending an email to email@target.com
An attacker sends a fake email to email@target.com by putting the victim’s email in FROM field
The target server receives the email and does not verify its authenticity and considers it as a legit email sent from a user
Application processes the email and performs action from the victim’s account and leads to authorization bypass

I reported the bug immediately to Dropbox BBP on Hackerone and it got triaged the next day but the team downgraded the severity to High stating the following reason

Team Comment on Hackerone

Though they paid me a bounty of $4913 on High category as per their policy

Press enter or click to view image in full size

Other Exploitation Scenarios

I found the same vulnerability on a bug reporting portal that allowed me to create bug tickets from the victim’s account by sending an email to bugs@redacted.com
This bug could be found on applications that are using their own support panels and we can create tickets there on behalf of the internal team or any other user
Any other kind of application that performs actions or creates tickets/bugs by sending email to them

The root cause of this vulnerability is that the target server does not verify SPF records, Email clients configured to use SPF and DMARC will automatically reject emails that fail validation and this should be applied to applications to prevent this vulnerability

Timeline

16-Dec-2021 — Reported bug to Dropbox BBP on Hackerone

17-Dec-2021 — Bug Triaged by Hackerone Triage Team

31-Dec-2021 — $4913 Bounty awarded by Dropbox Team

17-March-2022 — Dropbox Team fixed the issue

02-May-2022 — Report closed as resolved

Thanks for reading this, If you have any queries, feel free to reach me on Twitter at @ehsayaan or ehsayaan@gmail.com

Special thanks to Sam Curry for proofreading this writeup

Until next time!

Sayaan Alam

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE! https://weekly.infosecwriteups.com/

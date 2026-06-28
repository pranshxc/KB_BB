---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-24_tokopedia-account-takeover-bug-worth-8-million-idr.md
original_filename: 2018-12-24_tokopedia-account-takeover-bug-worth-8-million-idr.md
title: Tokopedia Account Takeover Bug Worth 8 Million IDR
category: documents
detected_topics:
- otp
- command-injection
- password-reset
tags:
- imported
- documents
- otp
- command-injection
- password-reset
language: en
raw_sha256: 7ab4c4b41d8fc52adbf33a430ce781112d2e710d99f883ee577bd9a0132fb221
text_sha256: e0f229707281842dca88f5f96e8a0b56c8c04c150c42d8a8bdeb7bc20c3f0716
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Tokopedia Account Takeover Bug Worth 8 Million IDR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-24_tokopedia-account-takeover-bug-worth-8-million-idr.md
- Source Type: markdown
- Detected Topics: otp, command-injection, password-reset
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `7ab4c4b41d8fc52adbf33a430ce781112d2e710d99f883ee577bd9a0132fb221`
- Text SHA256: `e0f229707281842dca88f5f96e8a0b56c8c04c150c42d8a8bdeb7bc20c3f0716`


## Content

---
title: "Tokopedia Account Takeover Bug Worth 8 Million IDR"
url: "https://medium.com/@ironfisto/tokopedia-account-takeover-bug-worth-8-million-idr-5474cb5b5cc9"
authors: ["Mukul Lohar (@ironfisto)"]
programs: ["Tokopedia"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2018-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5506
scraped_via: "browseros"
---

# Tokopedia Account Takeover Bug Worth 8 Million IDR

Tokopedia Account Takeover Bug Worth 8 Million IDR
Mukul Lohar
Follow
2 min read
·
Dec 24, 2018

174

3

Press enter or click to view image in full size

Hi Infosec community,

In October month i was just searching for bug bounty programs through google dorks & I landed on this link .

tokopedia/Bug-Bounty
Tokopedia Bug Bounty Policy. Contribute to tokopedia/Bug-Bounty development by creating an account on GitHub.

github.com

I went through terms and conditions. I started hunting for bugs & within an hour i found account takeover bug.

Steps To Reproduce:

Victim email of tokopedia account: ezgcmmfgc@champmails.com
1. Go to the https://accounts.tokopedia.com/reset-password
2. Now type the victim account email id & click on continue button. After that select verification method email.
3. Now copy the full URL from address bar. Which look like https://accounts.tokopedia.com/otp/c/page?otp_type=132& email=ezgcmmfgc%40champmails.com&ld=https://account s.tokopedia.com/resetpassword?e=***REDACTED-SUSPECT-TOKEN***4. Now in above URL. See there is password reset URL. Which start after “ld” parameter.
https://accounts.tokopedia.com/resetpassword?e=***REDACTED-SUSPECT-TOKEN***6. Now in password reset URL we have to just add “&otpcode=000000” at the end of password reset URL.
For ex.
https://accounts.tokopedia.com/resetpassword?e=ZXpnY21tZmdjQGNoYW1wbWFpbHMuY29t &otpcode=000000
7. Now go to the above URL. And just enter the password of whatever you choice. Victim Tokopedia account is successfully takeover.

Video POC:

Timeline:

Get Mukul Lohar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

14-Oct-2018: Reported

15-Oct-2018: Received Response

“Hi,

Thank you for waiting. Your report has been verified, and it’s a valid security bug with Critical Severity. We are still fixing this bug, please be patient.”

17-Oct-2018: Fixed

17-Oct-2018: 8 Million IDR Rewarded

Press enter or click to view image in full size
Bounty mail

6-Dec-2018: Received Bounty.

Twitter : https://twitter.com/ironfisto

Few more account takeover writeups coming . Thank for reading. Bye

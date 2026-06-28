---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-05_got-bounty-with-account-takeover-ato-unicode-case-mapping-collision-.md
original_filename: 2020-03-05_got-bounty-with-account-takeover-ato-unicode-case-mapping-collision-.md
title: Got *Bounty* with Account takeover (ATO ) Unicode-Case Mapping Collision !
category: documents
detected_topics:
- password-reset
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- command-injection
- otp
language: en
raw_sha256: 36b2d2778a7b3e00eb67ca2a51a157c62114b071a1b085467cd2f2bbd5fd26f9
text_sha256: 4315a7d17e20984acdb2edb1402064059168f07232e258fa4ab02fd89ebfbb1c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Got *Bounty* with Account takeover (ATO ) Unicode-Case Mapping Collision !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-05_got-bounty-with-account-takeover-ato-unicode-case-mapping-collision-.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `36b2d2778a7b3e00eb67ca2a51a157c62114b071a1b085467cd2f2bbd5fd26f9`
- Text SHA256: `4315a7d17e20984acdb2edb1402064059168f07232e258fa4ab02fd89ebfbb1c`


## Content

---
title: "Got *Bounty* with Account takeover (ATO ) Unicode-Case Mapping Collision !"
url: "https://medium.com/cyberverse/got-bounty-with-account-takeover-ato-unicode-case-mapping-collision-d23a7785e1be"
authors: ["Shaurya Sharma (@ShauryaSharma05)"]
bugs: ["Account takeover"]
publication_date: "2020-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4733
scraped_via: "browseros"
---

# Got *Bounty* with Account takeover (ATO ) Unicode-Case Mapping Collision !

Got *Bounty* with Account takeover (ATO ) Unicode-Case Mapping Collision !
Shaurya Sharma
Follow
2 min read
·
Mar 5, 2020

359

3

Hey hunters ! Recently I discovered a Unicode-Case Mapping Collision vulnerability on a private program.

Unicode exceptionally complex. Few people know all the tricks: from invisible characters and control characters to surrogate pairs and combined emojis (when adding two characters you get a third).

As the vulnerability is still not patched yet so I’m denoting the website with “xyz.in” in this blog

I have just registered my own domain to exploit a security flaw in xyz.in forgot password process to gain access to an account that belongs to a privileged user.

Get Shaurya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

THAT SHIT COST ME $20 😂
In this case, I used the Turkish character ‘ı’ (‘i’ without a dot), which is translated into Latin ‘i’, so that the postal address Test@xyz. ın after processing turns into Test@xyz.in
Successfully created a domain xyz. ın (Without the dot)
Created Free email from Google G-Suite trial pack and named it “Admin@xyz. ın”
Created an account on “xyz.in” with the malicious email address as “admin@xyz.ın”
Logged out from that account >> logged in “admin@xyz.ın” and clicked on Forget Password.
Intercepted the request>> And the input reflecting in UPPER CASE
The DB found replaced the malicious user with the correct one and triggered a password reset token on the malicious email address.
Successfully changed the password of the admin user, and got the bounty!!
Such collisions can be found on all Unicode planes: here is the complete list .

#HappyHunting #BugBounty #2020 #CyberVerse

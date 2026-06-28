---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-22_api-token-hijacking-through-clickjacking.md
original_filename: 2020-06-22_api-token-hijacking-through-clickjacking.md
title: API Token Hijacking Through Clickjacking
category: documents
detected_topics:
- command-injection
- mfa
- otp
- clickjacking
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- otp
- clickjacking
- api-security
language: en
raw_sha256: 23b3bd1c43368b13020228065839a441f69eb3097ed0fbda84997bcaa06becc2
text_sha256: 8528d095b89f5745a2ad0b596b6c1a2eefeb736ca8dec94b52aa17a70c1df6c8
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# API Token Hijacking Through Clickjacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-22_api-token-hijacking-through-clickjacking.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `23b3bd1c43368b13020228065839a441f69eb3097ed0fbda84997bcaa06becc2`
- Text SHA256: `8528d095b89f5745a2ad0b596b6c1a2eefeb736ca8dec94b52aa17a70c1df6c8`


## Content

---
title: "API Token Hijacking Through Clickjacking"
url: "https://medium.com/bugbountywriteup/api-token-hijacking-through-clickjacking-2e36c02e6c48"
authors: ["DarkLotus (@darklotuskdb)"]
bugs: ["Clickjacking"]
publication_date: "2020-06-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4477
scraped_via: "browseros"
---

# API Token Hijacking Through Clickjacking

API Token Hijacking Through Clickjacking
DarkLotus
Follow
3 min read
·
Jun 23, 2020

262

3

Press enter or click to view image in full size

Hey Fellas! I hope you all are doing good and safe. Thank you so much for showing your interest in my previous blogs.

Get DarkLotus’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As the title says, I will show you one of my “lit” findings which come under P2 on Bugcrowd. You can also use it for account takeover, by changing victim’s email with attackers email, disabling 2FA and so on.

Press enter or click to view image in full size
Let’s Begin!

Screenshot 1: This is the clickjacking HTML code (DM on twitter if you want this code). Here you have to insert your burp collaborator URL or any other server that you control to get the token.

Press enter or click to view image in full size

Screenshot 2: As you can see above, in the background we have the vulnerable site running and on top of it, our malicious Clickjacking code and just behind the “myCODE” there is a “copy” button which we are going to hijack.

Press enter or click to view image in full size

Screenshot 3: Now I have made “opacity” to zero, so that the victim can see the vulnerable website, here the victim has to do the following:
1. Click on “myCODE”. (which will copy the Token to clipboard automatically)
2. Paste it in the Verification Box and click on submit.

Press enter or click to view image in full size

Screenshot 4: And we are done! Now just see your burp collaborator logs and you will get the victims token.

Press enter or click to view image in full size

Screenshot 5: Now we have successfully hijacked the victim’s Token through clickjacking.

Press enter or click to view image in full size

Follow me on twitter for amazing bug bounty tips.

Thank You

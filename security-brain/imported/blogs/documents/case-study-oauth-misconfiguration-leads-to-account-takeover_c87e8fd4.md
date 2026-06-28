---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-21_case-study-oauth-misconfiguration-leads-to-account-takeover.md
original_filename: 2019-09-21_case-study-oauth-misconfiguration-leads-to-account-takeover.md
title: '[Case Study] OAuth Misconfiguration leads to Account Takeover'
category: documents
detected_topics:
- oauth
- command-injection
tags:
- imported
- documents
- oauth
- command-injection
language: en
raw_sha256: c87e8fd4bc4f0d57c6576b7e1f30c60f118cce769b9fbb6cab881598de1c60e0
text_sha256: c8ad1cdee3c43ca4549172406c2dfa578b1a7d30d5583ce752e97a4c08752d3d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# [Case Study] OAuth Misconfiguration leads to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-21_case-study-oauth-misconfiguration-leads-to-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c87e8fd4bc4f0d57c6576b7e1f30c60f118cce769b9fbb6cab881598de1c60e0`
- Text SHA256: `c8ad1cdee3c43ca4549172406c2dfa578b1a7d30d5583ce752e97a4c08752d3d`


## Content

---
title: "[Case Study] OAuth Misconfiguration leads to Account Takeover"
url: "https://medium.com/@0xgaurang/case-study-oauth-misconfiguration-leads-to-account-takeover-d3621fe8308b"
authors: ["Gaurang Bhatnagar (@0xgaurang)"]
bugs: ["OAuth", "Account takeover"]
publication_date: "2019-09-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5014
scraped_via: "browseros"
---

# [Case Study] OAuth Misconfiguration leads to Account Takeover

[Case Study] OAuth Misconfiguration leads to Account Takeover
Gaurang Bhatnagar
Follow
3 min read
·
Sep 21, 2019

212

2

Most of the security vulnerabilities arises within the integration part due to the incorrect implementation of third party services. Integrating third party OAuth providers are often left misconfigured by developers which may lead to a bigger security impact such as account takeover.

While working on a bug bounty program, I found that the target website had a OAuth Misconfiguration which allowed me to gain access to any user’s account.

It is always recommended that you use two test accounts to test the OAuth misconfiguration flaw. Someone would definitely not like it if you accidentally land up into other users account.

Here I have used two test accounts as part of creating proof of concept. Naming them: Attacker and gaurang (Victim)

The website used Google and Facebook Oauth to sign in. As a victim, I signed up and logged into the application via Google sign in. The following image shows how my profile page looked.

Press enter or click to view image in full size

Notice the linked accounts section. Here you can see my Google account is linked with my profile. I have not linked my Facebook account.

To test the Oauth functionality, i created another account by the name of Attacker. I used another mail id to register into the application. Here’s how the attacker profile looked.

Press enter or click to view image in full size

In the Linked Accounts section you can also link your facebook account by signing into the facebook app. When you click on the Connect button, following request is generated:

Press enter or click to view image in full size

As you can see in the request, while linking up your Facebook account, the application sends ownerBid of the user who is requesting.

Get Gaurang Bhatnagar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, what if i replace this ownerBid with someone else’s ownerBid?

As an Attacker i replaced the OwnerBid parameter with the Victim’s ownerBid (gaurang).

As expected, i found that attacker’s facebook profile was linked to Victim’s profile account.

Press enter or click to view image in full size

Now, Attacker can sign in using facebook and will get access to Victim’s account.

Impact:

The impact was high because the profiles were public and if you see the source code of a public profile you can get the OwnerBid (which was used to takeover the account). The OwnerBid and user_bid were same.

Press enter or click to view image in full size

Moreover, there were many celebrities who had their account on this website. And the above screenshot contains the OwnerBid/user_bid of a known celebrity. So it was possible for an attacker to get access to any user’s profile.

Takeaways:

Make sure to properly test the third party integrated services. There are fair chances that they may not be properly configured and may become a source of $$$$ for you :).

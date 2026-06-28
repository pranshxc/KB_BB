---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-02_bugbountyidorhow-i-was-able-to-exfiltrate-any-users-credit-coupons.md
original_filename: 2021-08-02_bugbountyidorhow-i-was-able-to-exfiltrate-any-users-credit-coupons.md
title: ~/BugBounty/IDOR/”How I was able to exfiltrate any user’s credit coupons”
category: documents
detected_topics:
- idor
- access-control
- rate-limit
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- idor
- access-control
- rate-limit
- command-injection
- password-reset
- otp
language: en
raw_sha256: 20ead2f34d1adcd72e7af67439e5df19c0e360947a1b1e0fc8801988433a1ae2
text_sha256: ebb0350eff66feb447d07b75fc621e740cfb019f8f39d0b7a3600d869f16b6ab
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# ~/BugBounty/IDOR/”How I was able to exfiltrate any user’s credit coupons”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-02_bugbountyidorhow-i-was-able-to-exfiltrate-any-users-credit-coupons.md
- Source Type: markdown
- Detected Topics: idor, access-control, rate-limit, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `20ead2f34d1adcd72e7af67439e5df19c0e360947a1b1e0fc8801988433a1ae2`
- Text SHA256: `ebb0350eff66feb447d07b75fc621e740cfb019f8f39d0b7a3600d869f16b6ab`


## Content

---
title: "~/BugBounty/IDOR/”How I was able to exfiltrate any user’s credit coupons”"
page_title: "~/IDOR/# How I was able to exfiltrate any user’s Shopify credit coupons | by Jai Sharma | Medium"
url: "https://ja1sharma.medium.com/bugbounty-idor-how-i-was-able-to-exfiltrate-any-users-credit-coupons-49631d9f3bc8"
authors: ["Jai Sharma (@ja1sharma)"]
bugs: ["IDOR"]
publication_date: "2021-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3449
scraped_via: "browseros"
---

# ~/BugBounty/IDOR/”How I was able to exfiltrate any user’s credit coupons”

~/IDOR/# How I was able to exfiltrate any user’s Shopify credit coupons
Jai Sharma
Follow
3 min read
·
Aug 1, 2021

289

Hi guys, I will explain how a simple HTTP Method Verb Tampering led to credit coupon stealing IDOR via this article.

#whoami: JAI SHARMA | Part Time Open Source Security Researcher

To begin with, I will walk you through with the target subdomains.

#target: BugCrowd Private Program

#In-scope: a.redacted.com, b.redacted.com

Subdomain: a.redacted.com, allows authenticated users to create discount Coupons for their individual business stores.

After spending 2–3 hours on the same domain, I decided to move onto the next in-scope subdomain: b.redacted.com. I was doing a basic website crawling without prior user authentication.

Next, I tried to log in to the application with valid user credentials. While crawling the target, I found an interesting preflight API call:

OPTIONS /api/v1/client_info?email=user@web.com&external_id=00000111&customer_token=7ddf32e17a6ac5ce04a8ecbf782ca509&merch_id=60037

Noticed anything? Yes, the user email id was sent via the OPTIONS method, resulting in a plain 204 response. Basically, it was triggered to ensure if the oncoming requests are safe or not.

Press enter or click to view image in full size

The next thing I tried, to tamper with the OPTIONS verb, I changed it to GET, I got some strange response, which includes everything user: user@web.com has created in a.redacted.com — Credit Coupons, Credit History, Expired Coupons, etc.

Press enter or click to view image in full size

At this point, I wanted to see, if by just manipulating the email id, if I can fetch data(from a.redacted.com) of other users.

I was able to pull that off. However, this requires an attacker to know the victim’s email and external_id. This seems doable. However, it was still incomplete.

I observed that the external_id value is an incremental value, which is unique for each unique user.

Get Jai Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found the same API call to be missing any rate limit. Well Okay! What else?

Surprisingly, the same external_id is shared once a password reset request was initiated.

Now all I have to do is, create another test account obtain the victim’s email id and external ID (easy enumeration/exposed via password reset functionality). Using the same vulnerable request with tampered OPTIONS to GET Method.

And I can fetch the Coupons created in a.redacted.com by the victim, not only the currently active credit coupons, but also, expired coupons, current balance, and other transaction details.

Press enter or click to view image in full size

Initially, it was triaged as a P3, later changed to P2 after seeing the potential impact.

Timelines:

Submitted on: 02 Jun 2021

VRT: Broken Access Control (BAC) > Insecure Direct Object References (IDOR)

Priority: P2

Triaged on: 07 Jun 2021

Rewarded on: 21 Jun 2021

PO Feedback:

If you make till here, thank you so much for giving it a read, do share your thoughts on this.

Connect with me on Twitter: https://twitter.com/ja1sharma

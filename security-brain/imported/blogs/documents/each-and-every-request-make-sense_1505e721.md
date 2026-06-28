---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-05_each-and-every-request-make-sense.md
original_filename: 2021-01-05_each-and-every-request-make-sense.md
title: Each and every request make sense…
category: documents
detected_topics:
- access-control
- jwt
- command-injection
- otp
tags:
- imported
- documents
- access-control
- jwt
- command-injection
- otp
language: en
raw_sha256: 1505e721ab36a7396d59755717d84a7dc1a344c48deb7b2c2e76cba247d6796d
text_sha256: 6e6adaebbbc04cadb5f4fb38aac8a8c6bf721f63f4215b90a2fecd904ec5e530
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Each and every request make sense…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-05_each-and-every-request-make-sense.md
- Source Type: markdown
- Detected Topics: access-control, jwt, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `1505e721ab36a7396d59755717d84a7dc1a344c48deb7b2c2e76cba247d6796d`
- Text SHA256: `6e6adaebbbc04cadb5f4fb38aac8a8c6bf721f63f4215b90a2fecd904ec5e530`


## Content

---
title: "Each and every request make sense…"
url: "https://akshartank.medium.com/each-and-every-request-make-sense-4572b3205382"
authors: ["Akshar Tank"]
bugs: ["Privilege escalation", "Exposed JWT generation endpoint", "JWT"]
publication_date: "2021-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4028
scraped_via: "browseros"
---

# Each and every request make sense…

Each and every request make sense…
Akshar Tank
Follow
3 min read
·
Jan 5, 2021

15

Hello Everyone,

I hope your 2020 wasn’t that bad and you still gave your efforts to be productive.

In this short write-up, I would talk about how I was able to access every admin account in the same organization as well as cross-organization. It was done on a company that is very well-known in the developer’s community. However, I won’t mention its name as it is a private program.

So this is a digital signature website where anyone can send a document to sign to the other person. The application manages well its access control by differentiating proper roles and no inter-role leakages(Privilege escalation). It used traditional cookies for normal users and JWT sent in an “X-admin-token” header to identify admin, which according to me is the better way to manage roles if implemented correctly. However, there was one thing noticeable that, an admin can be a normal user too. This sprouted a series of doubt in me of how can this be happening.

Get Akshar Tank’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thus, after attaching burp to the browser, I read each and every request of how an admin user is getting the JWT even though he was using cookies. But to my surprise, a single request(as below) is serving a JWT to the admin without checking his cookies, just by supplying an ID that is public to the organization.

Press enter or click to view image in full size
User to Admin request

So any user can just execute a URL in his session and would get the JWT. Now the user can exchange this token to obtain “X-admin-token”.

Press enter or click to view image in full size

To check whether admin APIs are accessible or not I checked this token and as expected the token didn’t work with most APIs, as access control policies were attached to it.

Adding more to my work, I started searching some APIs where I can use this token and after some time I found many from reading company’s documentation, one of them was leaking billing details of the organization.

Press enter or click to view image in full size
Billing detials

Impact

Privilege escalation in the organization.
Privilege escalation across organizations where accountID must be known, which can be known if a person from a different company has sent you a document to sign.

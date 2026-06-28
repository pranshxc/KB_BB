---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-29_how-i-turned-self-xss-to-stored-via-csrf_2.md
original_filename: 2019-11-29_how-i-turned-self-xss-to-stored-via-csrf_2.md
title: How I turned Self XSS to Stored via CSRF
category: documents
detected_topics:
- xss
- command-injection
- csrf
tags:
- imported
- documents
- xss
- command-injection
- csrf
language: en
raw_sha256: 7084d6bbe6609d677de1529f0ef9dd5047262c6638f14f2ad9e8fbfc8f7f9930
text_sha256: c986750cda1e249f74e0d4e3713f006d7c0a1296ae25ff56b1e5207a2ad0df5b
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I turned Self XSS to Stored via CSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-29_how-i-turned-self-xss-to-stored-via-csrf_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7084d6bbe6609d677de1529f0ef9dd5047262c6638f14f2ad9e8fbfc8f7f9930`
- Text SHA256: `c986750cda1e249f74e0d4e3713f006d7c0a1296ae25ff56b1e5207a2ad0df5b`


## Content

---
title: "How I turned Self XSS to Stored via CSRF"
url: "https://medium.com/@abhishake100/how-i-turned-self-xss-to-stored-via-csrf-d12eaaf59f2e"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["Self-XSS", "CSRF"]
bounty: "550"
publication_date: "2019-11-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4911
scraped_via: "browseros"
---

# How I turned Self XSS to Stored via CSRF

How I turned Self XSS to Stored via CSRF
Abhishek
Follow
3 min read
·
Nov 29, 2019

123

1

Press enter or click to view image in full size

Curated list of Bug Bounty programs — https://bugbountydirectory.com

Since the company told me to keep the name private, lets call it private.com

So private.com allows users to create groups and then invite other users to share anything in that group. So i tried to find XSS in the group name and i found it quickly, like pretty quickly. My payload was <script>alert(1)</script> in the group name and i got a pop-up.

Press enter or click to view image in full size

So i tried to see if other users get impacted as well. I quickly created an account and invited the user to my group. The XSS didn’t execute, it was all encoded. I tried to bypass it but didn’t have any luck. So this was just a Self XSS.😑

So i started looking around for something else and i noticed that group names were encoded everywhere except for the dialog box that appeared after creating a group.

We’ve added zxc

Press enter or click to view image in full size

Turns out the self XSS i found was of the dialog box and not the group name itself and so i thought what if somehow i managed to create a group on behalf of the user and then the dialog box will appear executing the XSS.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i started burpsuite and i looked at the request and voila.

Press enter or click to view image in full size

There was no CSRF protection against the request so i quickly generated a working PoC and tried it and boom XSS got executed and i was like.

This was a great find for me as it impacted other users. Technically i don’t think its a stored XSS as it will execute only once after the user visits the link.

Press enter or click to view image in full size
Bounty

They fixed it quickly within 2 days by completely removing the dialog box and adding CSRF protection.

I hope you learned something from this and if you liked it then please share.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.

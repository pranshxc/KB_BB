---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-04_how-i-got-hall-of-fame-in-microsoft.md
original_filename: 2020-07-04_how-i-got-hall-of-fame-in-microsoft.md
title: How I got hall of fame in Microsoft
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 3e3ff7f757c5e24ca23728620e427abf2519cc0fc06c101e87aa3f21d59dcc1e
text_sha256: acdcdbc3d6cb0674e124ae11d1918e4a793d88fafdfa4557782276d7122e1df4
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I got hall of fame in Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-04_how-i-got-hall-of-fame-in-microsoft.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `3e3ff7f757c5e24ca23728620e427abf2519cc0fc06c101e87aa3f21d59dcc1e`
- Text SHA256: `acdcdbc3d6cb0674e124ae11d1918e4a793d88fafdfa4557782276d7122e1df4`


## Content

---
title: "How I got hall of fame in Microsoft"
url: "https://medium.com/@noneofyou/how-i-got-hall-of-fame-in-microsoft-9b507dec3860"
authors: ["Akash basnet (@noneofyou007)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2020-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4443
scraped_via: "browseros"
---

# How I got hall of fame in Microsoft

How I got hall of fame in Microsoft
Akash basnet
Follow
2 min read
·
Jul 4, 2020

113

1

by admin · July 4, 2020

Hello, This is Akash Basnet a.k.a (Noneofyou). Today I am going to share my recent finding in Microsoft.

As everyone, I always had a wish to be in hall in fame in Microsoft. So, one day I was hunting in Microsoft searching for XSS as it is easy to find. But in my case, I had no luck. So, I started enumerating subdomains of Microsoft but still no luck.

I was hopeless and thought of why not check the acquisition sites acquired by Microsoft. I started searching for Microsoft acquired company from crunch base site and found mover.io.

Mover.io is a company acquired by a Microsoft which is a tool to migrate data from various cloud storage providers to Office 365 quickly, securely, and with little hassle. It supports all major providers like Dropbox, Google, Amazon , etc.

Get Akash basnet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I scanned all the subdomain with the help of sublist3r & found a interesting domain name internal-status.mover.io. There was option to create a event & the parameter of title & detailed description are vulnerable to Html injection & Reflected XSS. I put the payload and boom XSS got executed.

Press enter or click to view image in full size

I imediately reported to the Microsoft team got reply.

Press enter or click to view image in full size
Press enter or click to view image in full size

And, finally after few weeks got listed in hall of fame in Microsoft !!

Press enter or click to view image in full size

You can visit the link to verify the Hall Of Fame: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services?SilentAuth=1&rtc=1

Moral: If you didn’t find bug in main site go for acquisition sites .

https://www.youtube.com/watch?v=e1kbN5ToqfY

Link to the video POC. Also, don’t forget to like, and subscribe the channel. Thanks ❤

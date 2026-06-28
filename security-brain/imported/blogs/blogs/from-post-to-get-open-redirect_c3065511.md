---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-31_from-post-to-get-open-redirect.md
original_filename: 2019-12-31_from-post-to-get-open-redirect.md
title: From POST to GET Open redirect
category: blogs
detected_topics:
- xss
- command-injection
tags:
- imported
- blogs
- xss
- command-injection
language: en
raw_sha256: c306551102b917c18e8a352cf0e2ea3941fb1dc1602ef1f2b92328e2c619554f
text_sha256: 549d855ec528421b22290cf19994206becf1c0f28ab7e3dd4d073aa44847afdf
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# From POST to GET Open redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-31_from-post-to-get-open-redirect.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c306551102b917c18e8a352cf0e2ea3941fb1dc1602ef1f2b92328e2c619554f`
- Text SHA256: `549d855ec528421b22290cf19994206becf1c0f28ab7e3dd4d073aa44847afdf`


## Content

---
title: "From POST to GET Open redirect"
url: "https://medium.com/sourav-sahana/from-post-to-get-open-redirect-e91f4f4206a"
authors: ["Sourav Sahana (@kernel_rider)"]
bugs: ["Open redirect"]
bounty: "450"
publication_date: "2019-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4852
scraped_via: "browseros"
---

# From POST to GET Open redirect

From POST to GET Open redirect
Sourav Sahana
Follow
2 min read
·
Jan 1, 2020

250

2

Hey ! I’m Sourav Sahana from India. This is the write-up for my first bug bounty so I am really sorry if I have made something wrong. This was an unique bug for me because I’ve rewarded three times for this bug. Hope you will enjoy this blog.

Summery

After so many duplicates and not applicable I found a program on Bugcrowd. As usual, like other beginner hunter I’m also looking for open redirect, subdomain takeover, server side injection, xss but I was failed and got demotivated and leave the program. next day again I started to take a last try. This time I was testing cookie invalidation issue. Again failed..

Discovery

There is no cookie invalidation issue. But I got this endpoint in search bar :https://manage.statuspage.io/login?redirect=%2fpages/ . I immediately change redirect parameter and BAAM.. It redirects to evil.com. But the problem is it only redirect if I’’m already signed in.If not signed in application was asking to login and then I was redirecting to evil.com. I thought it’s a valid issue and reported it. After two days my report was changed from P4 to P5 because it is post based. I was like:

I have to dig further. then I discover this endpoint: https://manage.statuspage.io/logout?redirect=https%3A%2F%2Fevil.com/ and also told them that if user already signed in then he will simply redirect to evil.com. Next day he changed the report from P5 to P4. And It’s a valid bug. I got my first valid bug and bounty. My first bounty $100 and it’s huge for me.

Wait! wait! wait! not finished yet. After one month hey replay me that this issue has been fixed. But I told then that I can still redirect using this url: https://manage.statuspage.io/logout?redirect=https%3A%2F%2Fbugcrowd.com/ . Then replayed me:- “Thank you for your reply. https://manage.statuspage.io/logout would be considered a different endpoint, so I would encourage you to submit that as a separate report so we can track it separately.”. again I submitted a report and this time I got $50. After one month they flag my report as Resolved. But this time also my luck was with me.. The bug was not fixed but they marked this as resolved and gave me 2 weeks if I can still reproduce this bug. I replayed yes! I can. No replay from his side.

I was waiting for the correct time. After 2 weeks again I reported this bug. And this time it was P3, I don’t know why. Whatever ! I got $300. Total bounty earned : $450

Get Sourav Sahana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thank you and happy hunting

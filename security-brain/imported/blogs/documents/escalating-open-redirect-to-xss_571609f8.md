---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_escalating-open-redirect-to-xss.md
original_filename: 2022-08-13_escalating-open-redirect-to-xss.md
title: Escalating Open Redirect to XSS
category: documents
detected_topics:
- oauth
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- oauth
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 571609f8bd81cedff184d9d0d10a539fe9affdcb2638b01b444885c653a15b7d
text_sha256: b9cc21ef8393e722e91c87ac20221c359102a8ea47ed54c6e6fdceac48dfae6b
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Open Redirect to XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_escalating-open-redirect-to-xss.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `571609f8bd81cedff184d9d0d10a539fe9affdcb2638b01b444885c653a15b7d`
- Text SHA256: `b9cc21ef8393e722e91c87ac20221c359102a8ea47ed54c6e6fdceac48dfae6b`


## Content

---
title: "Escalating Open Redirect to XSS"
url: "https://sagarsajeev.medium.com/escalating-open-redirect-to-xss-d2b9355e5f05"
authors: ["Sagar Sajeev (@Sagar__Sajeev)"]
bugs: ["Open redirect", "XSS"]
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2319
scraped_via: "browseros"
---

# Escalating Open Redirect to XSS

Escalating Open Redirect to XSS
Sagar Sajeev
Follow
2 min read
·
Aug 13, 2022

298

2

Hello everyone. Myself Sagar Sajeev.

In this writeup, I’ll discuss a how I was able to find a Open Redirect on a target website and escalate it to a XSS, thereby increasing the severity.

Press enter or click to view image in full size
Image Credit — StackHawk

Let the target domain be:-

Get Sagar Sajeev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“https://www.radacted.com/resources?search=hacker”

Note that the search term ‘hacker’ was being reflected in the page.
Tried for XSS here in all possible ways. But couldn’t find one. So I thought of looking for Open Redirects.
Looking for Open Redirects
PayloadsAllTheThings helped me a lot here.
I found that the following payload triggered XSS.

https://redacted.com/resources?next=sub.redacted.com&next=javascript:confirm(document.cookie)

So when a victim clicks on this link, he will be redirected to sub.redacted.com and within a second or 2, the XSS payload will be triggered.

Note:-

In all the above mentioned instances, the victim is signed into his account.
The ‘next’ parameter was added manually to the URL. You can also try manually adding others like ‘ ?continue= ’ , ‘ ?redirect_uri= ’ ,’ ?return=’ , ‘ ?go= ’ , ‘?continue_to=’ etc..
sub.redacted.com in the next parameter can be any whitelisted SLD. Thus adding any subdomain of the target to it does the job.
Using AND operator forces both the conditions to be true. Thus ‘javascipt:confirm(document.cookie)’ was also executed by the client side.

Tip : Also try URL-encoding (or even double URL-encode) the operators like &. This may help in bypassing certain front-end restrictions.

Timeline

Submitted : 04–08–2022

Accepted : 05–08–2022

I do occasionally share some tips about Bug Bounties and related stuff over at my Twitter and LinkedIn handle. So do follow me there. If you’ve got any queries, feel free to message me. I will be more than happy to help.

LinkedIn : https://www.linkedin.com/in/sagar-sajeev-663491208/

Twitter : https://twitter.com/Sagar__Sajeev

Thanks for going through my writeup and I hope it was useful to you. I’ve made 6 other writeups on my Medium handle. Please do check those out as well.

Happy Hunting!

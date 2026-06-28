---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-24_bug-bounty-in-lockdown-sqli-and-business-logic.md
original_filename: 2020-06-24_bug-bounty-in-lockdown-sqli-and-business-logic.md
title: Bug Bounty in Lockdown (SQLi and Business Logic)
category: documents
detected_topics:
- sqli
- business-logic
- xss
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- sqli
- business-logic
- xss
- command-injection
- mfa
- api-security
language: en
raw_sha256: 51af802c34bfeb7029bcdd3587304106d6851914754f870cc461ab990f153d3c
text_sha256: 721cc012208636b0ea437798e73e7ed0aee9f0ccf75e9639b8f81a6b6d00e3bd
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty in Lockdown (SQLi and Business Logic)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-24_bug-bounty-in-lockdown-sqli-and-business-logic.md
- Source Type: markdown
- Detected Topics: sqli, business-logic, xss, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `51af802c34bfeb7029bcdd3587304106d6851914754f870cc461ab990f153d3c`
- Text SHA256: `721cc012208636b0ea437798e73e7ed0aee9f0ccf75e9639b8f81a6b6d00e3bd`


## Content

---
title: "Bug Bounty in Lockdown (SQLi and Business Logic)"
url: "https://medium.com/@abhishake100/bug-bounty-in-lockdown-sqli-and-business-logic-98ab8cb5f661"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["SQL injection", "Logic flaw"]
publication_date: "2020-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4472
scraped_via: "browseros"
---

# Bug Bounty in Lockdown (SQLi and Business Logic)

Bug Bounty in Lockdown (SQLi and Business Logic)
Abhishek
Follow
3 min read
·
Jun 24, 2020

177

2

Press enter or click to view image in full size

Curated list of Bug bounty programs — https://bugbountydirectory.com

I hope you all are doing well in this lockdown. I kinda have a hard time concentrating on bug bounty for now cause of staying home all the time. Usually i go play football once a week but since the lockdown cant go out no more. I still managed to find few bugs during this time. Found a few XSS and 2fa bypass. But for now ill share just the 2 bugs that i found.

So the first bug i found was SQLi which was quite an easy find. The company has a public VDP but since i reported many bugs to them they asked me to look at a completely different website that they own.

Press enter or click to view image in full size

And of course i have taken permission from them before publishing the blog. With the help of wappalyzer found out that the website runs on PHP and so i used a simple google dork site:redacted.com inurl:id= and just found 1 url.

Press enter or click to view image in full size

I added ' at the end of id=1 and it gave me a MySQL error.

Press enter or click to view image in full size

This itself tells us that there is SQL injection. I injected sleep command and it worked which confirmed the vulnerability.

Press enter or click to view image in full size

This is enough for POC, reported it and the team fixed it pretty quickly.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the second bug was a business logic issue. The website is about creating projects or a presentation and sharing them with others. Users can create a free account but can only create 1 project. Creating multiple projects requires you to upgrade your account.

Press enter or click to view image in full size

When clicked on New Project it would redirect me to the payment page. So i thought of bypassing it, tried using Turbo Intruder to send the request of creating project multiple times but it gave me errors so i thought of trying it on the app version from Playstore. When browsing the app i discovered that you can create multiple projects in it without any restrictions and i was like.

There was an add button in the app which let me create as much projects as i want.

And the changes reflected on the website as well.

Press enter or click to view image in full size

And just like that i bypassed it. The app was really old and haven’t been updated for years.

Press enter or click to view image in full size

Always look at the app of the website if it has. Sometimes developers forget about the app and functionalities are never updated. The team were also kind enough to give bounty instead of coupons.

Press enter or click to view image in full size

Hope you learned something from this.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.

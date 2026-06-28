---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-28_hyperlink-injection-easy-money-sometimes.md
original_filename: 2020-01-28_hyperlink-injection-easy-money-sometimes.md
title: Hyperlink Injection - Easy Money (sometimes)
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 9c4ba3fc500a2997f881e97031d9643ee585ac90e50c364c083845adeb8837b7
text_sha256: b696443dcc7eecb1542a79ea0d6a79c7046ac177066da14035960e842e302e78
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hyperlink Injection - Easy Money (sometimes)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-28_hyperlink-injection-easy-money-sometimes.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `9c4ba3fc500a2997f881e97031d9643ee585ac90e50c364c083845adeb8837b7`
- Text SHA256: `b696443dcc7eecb1542a79ea0d6a79c7046ac177066da14035960e842e302e78`


## Content

---
title: "Hyperlink Injection - Easy Money (sometimes)"
url: "https://medium.com/@abhishake100/hyperlink-injection-easy-money-sometimes-cc1104655300"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["Hyperlink injection"]
bounty: "450"
publication_date: "2020-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4804
scraped_via: "browseros"
---

# Hyperlink Injection - Easy Money (sometimes)

Hyperlink Injection - Easy Money (sometimes)
Abhishek
Follow
3 min read
·
Jan 28, 2020

183

1

Press enter or click to view image in full size

Curated list of Bug bounty programs — https://bugbountydirectory.com

What is Hyperlink Injection, its basically spoofing or injecting a link when sending an email invitation.

Its a P5 according to bugcrowd, but some companies might consider it as a serious issue so report if you find it, might get paid.

Press enter or click to view image in full size

How do you find it, pretty simple. Lets consider the Missive app, its an email/chat app for a group of people or a team. You create an organization and then add people in it and they can join in via email-invitation which looks like this.

Press enter or click to view image in full size

Here, the organization name(Whatnow), my first name(John) and last name (Cena) are reflected, from here you can try to change any 3 names to a link and see if its shown in the email. For eg. I tried to change the organization name and it didn’t look like a link. They add a space after the dot in the URL.

Press enter or click to view image in full size

The only place left was to change my name to a link, so i changed my name to www.evil.com saved it and then sent the invite again which looked something like this.

Press enter or click to view image in full size

There you have it, Hyperlink Injection. I know it looks pretty obvious that there is a malicious link in the email, so to make it less suspicious i changed my name to John [Also special discount for new users go to www.evil.com for 50% off]

Press enter or click to view image in full size

I think that looks pretty neat.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Same goes to UsabilityHub, a platform for online surveys and tests. They also had a feature to invite a member in their team and after changing the name to a URL the email invitation looked like this.

Press enter or click to view image in full size

Although its a paid feature the security team hooked me up to a paid account for it to try.

Now some companies pay might vary on what they think about the severity of the bug. In the case of Missive, they considered it as a low severity.

Press enter or click to view image in full size

Some don’t consider it.

Press enter or click to view image in full size

Some pay good.

Press enter or click to view image in full size

And some pretty GOOD.

Press enter or click to view image in full size

Thanks to Missive and UsabilityHub for allowing me to disclose the issue. Both platforms fixed the issue pretty quickly. Hope you guys know what Hyperlink Injection is now.

Follow me on twitter — https://twitter.com/abhishekY495

Thank you.

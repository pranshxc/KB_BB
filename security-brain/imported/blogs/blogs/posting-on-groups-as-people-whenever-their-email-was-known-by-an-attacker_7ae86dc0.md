---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-29_posting-on-groups-as-people-whenever-their-email-was-known-by-an-attacker.md
original_filename: 2017-06-29_posting-on-groups-as-people-whenever-their-email-was-known-by-an-attacker.md
title: Posting on groups as people whenever their email was known by an attacker
category: blogs
detected_topics:
- access-control
- command-injection
tags:
- imported
- blogs
- access-control
- command-injection
language: en
raw_sha256: 7ae86dc07c4de3b9d1d33f739178c5880ebab9454f42317d5a6733040345b123
text_sha256: 434d1f88bbf7cc68d8e039b95a82945b709717f19734cb844e9a604a28897403
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Posting on groups as people whenever their email was known by an attacker

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-29_posting-on-groups-as-people-whenever-their-email-was-known-by-an-attacker.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7ae86dc07c4de3b9d1d33f739178c5880ebab9454f42317d5a6733040345b123`
- Text SHA256: `434d1f88bbf7cc68d8e039b95a82945b709717f19734cb844e9a604a28897403`


## Content

---
title: "Posting on groups as people whenever their email was known by an attacker"
url: "https://medium.com/@zahidali_93675/posting-on-groups-as-people-whenever-their-email-was-known-by-an-attacker-9dc8d7baf970"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "7,500"
publication_date: "2017-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6168
scraped_via: "browseros"
---

# Posting on groups as people whenever their email was known by an attacker

Posting on groups as people whenever their email was known by an attacker.
Zahid Ali
Follow
2 min read
·
Jun 29, 2017

170

1

Summary :

‘’Facebook groups are one of the most popular features where people discuss anything under the sun. There have been instances where such discussions have landed people in jail. That being the case, what if I could post something on behalf of you in a Facebook group? Well, the after effect depends on what I post on your behalf, Doesn’t it? Apparently there existed a vulnerability which could let you spoof anyone and post anything to a Facebook group.’’

Hey Everyone! I hope you all doing well, Today i want to share an issue i found in Facebook groups. I was looking for some other ways to post in Facebook groups which landed me to this link; https://www.facebook.com/help/206871819351594

According to the link we need to set a slug for our group and then group members/admins (only) can use email to post in group;

User emails “Hello test post” to group_slug@groups.facebook.com
- Facebook checks sender email is a group member or not
- If member, the email content get posted in group

So after understanding the feature i quicky set up a SMTP (used smtp2go), and a perl script called “sendemail” to send emails using our smtp server.

Command — perl sendemail.pl -f victim@email.com -t group_slug@groups.facebook.com -u Hello -m Whatsup -s smtp_host -xu smtp_username -xp smtp_password

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Where -f = From Sender

-t = Target Email
-u = Subject
-m = message
-s = SMTP host with port
-xu = SMTP username
-xp = SMTP password

Response — Email sent successfully

I quickly refreshed group and found out that it was posted successfuly in the group :d

The only catch here was that you should be knowing the email address to spoof a member of a group. But there was a way around for this as well.

Proof of concept video

Thanks to Facebook for quick fix and for generous bounty amount.

Initial Report Sent — Wed, Jun 14, 2017 at 6:45 AM
Escalation by Facebook — Sat, Jun 17, 2017 at 5:00 AM
Fixed by Facebook — Same Day
Bounty Awarded by Facebook — Thu, Jun 29, 2017 at 12:59 AM - (7500usd)

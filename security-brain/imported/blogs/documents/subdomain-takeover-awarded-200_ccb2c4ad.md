---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-07_subdomain-takeover-awarded-200_2.md
original_filename: 2019-05-07_subdomain-takeover-awarded-200_2.md
title: Subdomain takeover [Awarded $200]
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: ccb2c4ad971550bdb6399a7de450d277700d81192a5bca6c0442dc34e8a00485
text_sha256: 8950fce99ab6d57adc02490ca35c1efd4f0925032f24047fc26b33f5d1c68261
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain takeover [Awarded $200]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-07_subdomain-takeover-awarded-200_2.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `ccb2c4ad971550bdb6399a7de450d277700d81192a5bca6c0442dc34e8a00485`
- Text SHA256: `8950fce99ab6d57adc02490ca35c1efd4f0925032f24047fc26b33f5d1c68261`


## Content

---
title: "Subdomain takeover [Awarded $200]"
url: "https://medium.com/@friendly_/subdomain-takeover-awarded-200-8296f4abe1b0"
authors: ["Friendly (@SkeletorKeys)"]
programs: ["ownCloud"]
bugs: ["Subdomain takeover"]
bounty: "200"
publication_date: "2019-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5269
scraped_via: "browseros"
---

# Subdomain takeover [Awarded $200]

Subdomain takeover [Awarded $200]
Friendly
Follow
3 min read
·
May 7, 2019

125

2

The story is simple, the reward was “alright”. Let’s start. ^_^

Press enter or click to view image in full size

I came across a website known as ownCloud. Their bug bounty program is located here — https://owncloud.com/owncloud-bug-bounty-program/ and their H1 program is located here https://hackerone.com/owncloud

Their bounty program looked nice and juicy and I wanted some dough ( 🤑 )

So I ran https://github.com/aboul3la/Sublist3r [pretty sure everyone is aware of this] and I came cross a domain that was displayed as

Press enter or click to view image in full size

So I did a quick search on their CNAME and it points to owncloud.fider.io but somehow wasn’t reflecting back on their feedback.owncloud.com domain. CNAME check tool I used — https://toolbox.googleapps.com/apps/dig/

I then registered on https://getfider.com/ a demo account and saw that they had a custom page to set whichever domain you wanted.

Press enter or click to view image in full size

I then pointed the feedback.owncloud.com domain to my testing domain on https://getfider.com/ and saw that my inputs reflected over to http://feedback.owncloud.com/

Press enter or click to view image in full size

I also noticed that they had an advanced page in the settings page which allows you to use CSS. I cooked up an IP grabber and a cookies grabber code via CSS to show the escalation of this.

Press enter or click to view image in full size

I swiftly reported it and in 2 hours, the issue was fixed via email. I was then told to send the report on HackerOne and I got my bounty.

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I thought I would have gotten $5k for their subdomain takeover, but turns out it was $200 since .ownCloud was out of scope. However, I’d deem this as a very high security risk and the payout should have been more, but what can you do — the company has “more rights” to your inputs than you yourself.

Grateful- but not satisfy.

Timeline:

4/20/2019 issue was reported. — 2 hours later the issue was fixed.

Via email talks 3 weeks 5/6/2019.

Paid out on 5/7/2019–$200.

Worth it? Not sure.

Thanks for reading.

If you have questions regarding this, then feel free to shoot me a DM on Twitter https://twitter.com/Skeletorkeys or, join our Discord Server https://discord.gg/B6rZDTB to talk to any of the hundreds of people for help, or just looking to talk to other Hax0rs.

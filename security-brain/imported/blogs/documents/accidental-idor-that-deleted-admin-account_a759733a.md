---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-25_accidental-idor-that-deleted-admin-account.md
original_filename: 2020-01-25_accidental-idor-that-deleted-admin-account.md
title: Accidental IDOR that Deleted Admin Account.
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
language: en
raw_sha256: a759733a6224ae6f8323b2126cea0effba2f67a6c439c082021f331430ae6bbb
text_sha256: aa5be8b61a768db49bdfb908bcc2b9b589128f784e88c813a8db7ed6e9b54e10
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Accidental IDOR that Deleted Admin Account.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-25_accidental-idor-that-deleted-admin-account.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a759733a6224ae6f8323b2126cea0effba2f67a6c439c082021f331430ae6bbb`
- Text SHA256: `aa5be8b61a768db49bdfb908bcc2b9b589128f784e88c813a8db7ed6e9b54e10`


## Content

---
title: "Accidental IDOR that Deleted Admin Account."
url: "https://medium.com/bugbountywriteup/accidental-idor-that-deleted-admin-account-d51264292b66"
authors: ["Sayaan Alam (@ehsayaan)"]
bugs: ["IDOR"]
bounty: "325"
publication_date: "2020-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4812
scraped_via: "browseros"
---

# Accidental IDOR that Deleted Admin Account.

Accidental IDOR that Deleted Admin Account.
Sayaan Alam
Follow
2 min read
·
Jan 25, 2020

1.5K

Hey Everyone, Last week I got invited to a private program through one of my friend Ananda Dhakal.

About the Bug
IDOR was in OWASP Top Ten — 2013 and it’s a vulnerability, which allows you to access unauthorized data due to exposed reference. Let’s move to practical scenario.

So I was testing out that program and at starting I found a normal rate limiting worth $25 😅😅 , Yeah It’s too low, I was also not happy with it.
So I started playing with requests on my burp repeater, after testing some time I didn’t get anything so I stopped and shut my mac down.
After Few Minutes I got a discord notification from admin worth $300...Guess what was that???

Press enter or click to view image in full size

I was surprised and remembered that I was playing with requests, I think I had deleted it.
So I instantly went through my whole burp history and searched for delete request, Hopefully, I got It.

Press enter or click to view image in full size

There was a feature On that website to add and delete team members on my account, So when I was with requests I had sent a delete request with user_id = 1, that’s why the admin account got deleted. After this, I was confirmed that I can delete anyone’s account.
I reported the bug and sent the pic. Within an hour I got my reward of $300 + 25$ For Limiting Bug. It was the fastest ever resolution in BB Carrier.

Get Sayaan Alam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you have questions and anything about the post you want to ask me, please contact me via twitter. I’ll have my DM open.

Guys Please Don’t Hesitate To Clap 50 Times😊
Until Next Time!

If you like my blog posts and my work, please consider checking out my “Buy me a coffee” page
https://www.buymeacoffee.com/jgUFSPu

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

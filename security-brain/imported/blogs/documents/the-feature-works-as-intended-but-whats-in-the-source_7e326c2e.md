---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-08_the-feature-works-as-intended-but-whats-in-the-source.md
original_filename: 2020-08-08_the-feature-works-as-intended-but-whats-in-the-source.md
title: The feature works as intended, but what’s in the source?
category: documents
detected_topics:
- xss
- mobile-security
- idor
- command-injection
- graphql
- information-disclosure
tags:
- imported
- documents
- xss
- mobile-security
- idor
- command-injection
- graphql
- information-disclosure
language: en
raw_sha256: 7e326c2edf8c48246ed4174d7f209aefdf799471ea8698f8b450bded63a1a1d4
text_sha256: 0cab89830375d5b0ccadf040f5b9b944d0d78f215b1920f367e03619dc39273f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The feature works as intended, but what’s in the source?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-08_the-feature-works-as-intended-but-whats-in-the-source.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, idor, command-injection, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `7e326c2edf8c48246ed4174d7f209aefdf799471ea8698f8b450bded63a1a1d4`
- Text SHA256: `0cab89830375d5b0ccadf040f5b9b944d0d78f215b1920f367e03619dc39273f`


## Content

---
title: "The feature works as intended, but what’s in the source?"
url: "https://medium.com/@zseano/the-feature-works-as-intended-but-whats-in-the-source-d29f9401bcf6"
authors: ["Zseano (@zseano)"]
bugs: ["Information disclosure"]
publication_date: "2020-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4343
scraped_via: "browseros"
---

# The feature works as intended, but what’s in the source?

The feature works as intended, but what’s in the source?
Sean (zseano)
Follow
3 min read
·
Aug 8, 2020

279

This is another bug that was right in front of everyone because if you didn’t purposely look for it you’d never realise personal information was being ‘secretly’ leaked.

How does this feature work..?

When testing on [redacted] I noticed this piece of text:

Checking this box allows us to share your address with the list creator to help them manage their thank you list. You can change your preference at any time.

It only mentions that your address will be shared and nothing else. This is where I begin writing notes, such as “Feature [xyz] — Address is shared, reflected on [redacted].com/example. Only visible to list creator, no-one else.”. This way I know my goals and I can begin to understand how the developers think when implementing features such as this. As my testing continues i’ll begin adding onto my notes to determine if any features are connected or if they share data etc. The more you understand how a site is “put together”, the more you’ll be able to tear it down!

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tested the feature and it appeared to be working as intended. I purchased a gift from the list and I appeared in the “Thank you” list and the list creator could see my address (as stated). I tried testing for multiple issues such as stored XSS, IDOR, purchasing with sandbox CC etc but I had no success. Everything simply worked as intended.

What’s in the source?

Still authenticated as the list creator I decided to browse the source when viewing my thank you list (via view-source). I was curious, was it only my address that was shared? I decided to search for the email I used to purchase an item, so I pressed CTRL + F and began searching for “@googlemail.com”..

… and there it was, my email sitting secretly in the HTML DOM. Curiosity paid off. That simple. Any user who bought a gift from my list would not only share their address, but also share me their private email address. The problem was, they had no idea. They were not informed that their email would be shared, nor was the list creator informed that they would get access to it.

Repo steps provided:

Press enter or click to view image in full size
Takeaways

Just because a feature says it will only share certain information, verify this! Do as much detective work as possible to determine if any more information can be revealed. Developers work with lots of data and as technology grows they have to be sure which data to reflect, but because they handle lots of data, developers can make mistakes and leak more data than intended. GraphQL is notorious for this and I consider it leakyql

(side tip: don’t forget mobile apps AND mobile version of the web app! most companies have separate teams for mobile related stuff. most mobile stuff comes *after* the desktop app, so usually it’s just chucked together without security in mind. They just create a simple UI and begin pulling data.)

~ zseano

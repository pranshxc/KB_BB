---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-06_stored-xss-via-alternate-text-at-zendesk-support.md
original_filename: 2019-01-06_stored-xss-via-alternate-text-at-zendesk-support.md
title: Stored XSS Via Alternate Text At Zendesk Support
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: ad694b145611b8834f0d99c0ce78089927b53de71a5314d9e47cd22b4f8852dc
text_sha256: 7e419ca21f21202a1ef6d3bb80b1fa1123e9bb70a6a66e58d6091ef882f5b251
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS Via Alternate Text At Zendesk Support

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-06_stored-xss-via-alternate-text-at-zendesk-support.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ad694b145611b8834f0d99c0ce78089927b53de71a5314d9e47cd22b4f8852dc`
- Text SHA256: `7e419ca21f21202a1ef6d3bb80b1fa1123e9bb70a6a66e58d6091ef882f5b251`


## Content

---
title: "Stored XSS Via Alternate Text At Zendesk Support"
url: "https://medium.com/@hariharan21/stored-xss-via-alternate-text-at-zendesk-support-8bfee68413e4"
authors: ["Hariharan.s (@DJHARIZ1)"]
programs: ["Zendesk"]
bugs: ["Stored XSS"]
publication_date: "2019-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5485
scraped_via: "browseros"
---

# Stored XSS Via Alternate Text At Zendesk Support

Stored XSS Via Alternate Text At Zendesk Support
Hariharan S
Follow
3 min read
·
Jan 6, 2019

290

1

Hi Guys,

Finding bugs nowadays is like finding a needle in an haystack, But i was lucky enough to get that needle.

Well…The story begins just like every bug hunter’s daily routine..

Just a normal day in search for any bug that i could get my hands on.

But no luck..Now they usual thought came in “Time to jump to the next program” and i jumped and landed straight on a program called ZENDESK ..

Now i had to find what does this website do🤔🤔…It took me about 20 minutes to understand that it was actually a Support desk providing site for other websites..

Ok Now to Initialise the hunt..

Tempmail..Account Create..Bla Bla, And Logged on to my account.

Hmmm….What next!!

Of course time to test for xss

Basically all i did was just inserting payloads on all the input fields i could get my hands on.

This is when i came across a rich text editor but it did not have any much function just like normal text editors.

Get Hariharan S’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In it i found a URL input field and what’s funny about this field is that it does not actually detect if the given input is a URL. So i put my favorite XSS payload “Love Img XSS Payload” in the url input field and click ok.

But Nothing….

But…Apart from the url input field there was a ALTERNATIVE TEXT for the url. So i tested my luck on that…gave a random url and dropped the XSS payload on the ALTERNATIVE TEXT and clicked on ok.

I Click on the Link and BOOM!!

Got XSSed….

Report Timeline :

Jul 23rd- Report Submitted
Jul 24th- Report Triagged
Aug 23rd- Bounty Time$$$
Sep 12th- Resolved and Got listed on thier HOF

And That's How a Alternative Text Executed a XSS…As it Goes.

So Adios Amigos…That's all 4 now..This is Hariharan Signing Off..

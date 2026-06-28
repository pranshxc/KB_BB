---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-16_how-i-found-credential-enriched-redis-dump.md
original_filename: 2019-04-16_how-i-found-credential-enriched-redis-dump.md
title: How i found credential enriched redis dump
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 2b4b4b52e6738072737f524cb2377e51c24996f8ddee270e5544dc47b56aaee0
text_sha256: 4d0dbaf89393043de73d7d41bcff5fb660b046cf822b8b0bb296f950d8cae4aa
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How i found credential enriched redis dump

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-16_how-i-found-credential-enriched-redis-dump.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2b4b4b52e6738072737f524cb2377e51c24996f8ddee270e5544dc47b56aaee0`
- Text SHA256: `4d0dbaf89393043de73d7d41bcff5fb660b046cf822b8b0bb296f950d8cae4aa`


## Content

---
title: "How i found credential enriched redis dump"
url: "https://medium.com/@D0rkerDevil/how-i-found-credential-enriched-redis-dump-2b9e808024c4"
authors: ["Ashish Kunwar (@D0rkerDevil)"]
bugs: ["File disclosure", "Information disclosure"]
publication_date: "2019-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5307
scraped_via: "browseros"
---

# How i found credential enriched redis dump

How i found credential enriched redis dump
Ashish Kunwar
Follow
2 min read
·
Apr 16, 2019

249

2

Hello, Everyone

So, i was testing a program , and during my recon i came across tons of subdomains unfortunately there were wildcard.

Anyways, my eye got attention on a subdomain“redacted-redacted.redacted.com” and it was a static page just to download their mobile apps , as it was a beta version so i thought why not do some directory search,so i ran dirsearch on default list

python3 dirsearch.py -e <extensions list> -u http://redacted-redacted.redacted.com

and a file dump.rdb catch-ed my attention , it was 3mb in size

Now a question arise what is Dump.rdb?

To those who don’t know

rdb file is a binary representation of the in-memory store. This binary file is sufficient to completely restore Redis’ state. The rdb file format is optimized for fast read and writes. Where possible LZF compression is used to reduce the file size

so as we see it had LZF compression so it was hard to read , so i downloaded couple of things

rdbtools
python-lzf

sudo pip install rdbtools python-lzf

and now once they are installed , we run command in order to make it readable , and in order to read we have to convert it to json

rdb — comand json dump.rdb -f output.json

Get Ashish Kunwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

or you can also save the output in directly in a .txt file

sudo rdb — command json dump.rdb > out.txt

this will save all the json output in .txt

(somewhat direct output save makes the file readable in compare to original output rdbtools does)

and now you can open it in your fav. editor or use this service or whatever suits you.

http://jsonviewer.stack.hu

Now when i opened it, i found smtp login creds, usernames, passwords,addresses, etc.

Press enter or click to view image in full size

Unfortunately i cannot tell you the company name or any other detail, just this writeup gives idea what to do if you find anything like this.

So i reported to the company and they replied

“it is 3 years old but thank you for letting us know, Bla Bla Bla…”

unfortunately no Bounty yet.

“But its always great to learn something and experience from it.”

My DM is open for any questions.

Thank you for Reading

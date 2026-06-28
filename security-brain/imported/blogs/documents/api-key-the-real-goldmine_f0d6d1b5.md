---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-19_api-key-the-real-goldmine.md
original_filename: 2018-08-19_api-key-the-real-goldmine.md
title: 'API key: The real goldmine'
category: documents
detected_topics:
- api-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- api-security
- command-injection
- information-disclosure
language: en
raw_sha256: f0d6d1b5c1011ec108a032e684f45ce99aa3c4a5e211ffcebb363d9c01260c4e
text_sha256: c83b3ae775ce92f87ce82260451d8ae94bde40ee8e75a8782a16d003a436a9af
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# API key: The real goldmine

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-19_api-key-the-real-goldmine.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `f0d6d1b5c1011ec108a032e684f45ce99aa3c4a5e211ffcebb363d9c01260c4e`
- Text SHA256: `c83b3ae775ce92f87ce82260451d8ae94bde40ee8e75a8782a16d003a436a9af`


## Content

---
title: "API key: The real goldmine"
url: "https://medium.com/@YumiSec/api-key-the-real-goldmine-84490a56b7c4"
authors: ["Yumi"]
bugs: ["Information disclosure"]
publication_date: "2018-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5743
scraped_via: "browseros"
---

# API key: The real goldmine

Top highlight

API key: The real goldmine
Yumi
Follow
2 min read
·
Aug 19, 2018

144

2

Hey everyone and welcome to my new write-up !

Today I would like to share an interesting way to exploit an API leakage. On a side note, this bug was found on a private program, so all the informations about the company/detailled exploitation will be redacted.

During one of my bug hunting session, I found an interesting line in the HTML source code.

<input type=”hidden” id=”redacted” value=’https://thirdpartysite.com/89fs9re98jy4819rj91tu18i8918'>

As you can see, the company seems to use a third party website. We can also see a weird string after the domain name. My first reflex was to enter the URL of this third party website into my browser but it returned some GPS informations, so nothing interesting.

My second reflex was to check the documentation of this third party website. With the help of the documentation, I got two important infos. The first one is that this website is used for location/mapping purpose (this explain the GPS locations returned by the API). The second one is the fact that the random string after the domain name seems to be a secret key. Nice news but we need a working proof of concept to be a valid issue.

I’ve checked all the documentation during 1 or 2 hours without finding any interesting way to exploit this key. I was going to give-up but I’ve seen something interesting. When you have a standart plan on the website. You have 1000 free calls on the API per day and after that you will pay $0.001 for each new call and to make a call, you need the secret key.

So an attacker just need to make 1000 calls in a day and after that the company will pay additionaly. I tested it on my own installation and this worked perfectly fine. This kind of issue can lead to serious business damages for a company.

Get Yumi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I reported it to the program and they quickly triaged the report and rewarded me.

Timeline:

2018/05/18: Submitted

2018/05/18: Closed as informative

2018/05/18: Reopened

2018/05/22: Triaged and rewarded

2018/08/16: Resolved

I hope you enjoyed this reading !

Thanks to aku_da_cherry for his help on this write-up.

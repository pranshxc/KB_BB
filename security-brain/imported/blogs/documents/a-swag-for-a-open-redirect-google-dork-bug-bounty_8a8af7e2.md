---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-02_a-swag-for-a-open-redirect-google-dork-bug-bounty.md
original_filename: 2022-07-02_a-swag-for-a-open-redirect-google-dork-bug-bounty.md
title: A swag for a Open Redirect — Google Dork — Bug Bounty
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 8a8af7e28097ea3c3edf2a38f9a4f6fd92854dde1b6b126e75e13cb5f2836c50
text_sha256: 40c67614666a0f090a96660610e553c91b214ec7a20e911b32bb387c4f9ed0c0
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# A swag for a Open Redirect — Google Dork — Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-02_a-swag-for-a-open-redirect-google-dork-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `8a8af7e28097ea3c3edf2a38f9a4f6fd92854dde1b6b126e75e13cb5f2836c50`
- Text SHA256: `40c67614666a0f090a96660610e553c91b214ec7a20e911b32bb387c4f9ed0c0`


## Content

---
title: "A swag for a Open Redirect — Google Dork — Bug Bounty"
url: "https://infosecwriteups.com/a-swag-for-a-open-redirect-google-dork-bug-bounty-2143b943f34e"
authors: ["Proviesec (@proviesec)"]
bugs: ["Open redirect"]
publication_date: "2022-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2491
scraped_via: "browseros"
---

# A swag for a Open Redirect — Google Dork — Bug Bounty

Member-only story

A swag for a Open Redirect — Google Dork — Bug Bounty
Proviesec
Follow
4 min read
·
Jul 3, 2022

114

2

Press enter or click to view image in full size

Hello Folks 👋,I have found a good open redirect with my param scanner. I will tell you here how I found it and what kind of swag I got. I am also currently modifying my scanner, PSFuzz, so that it can also scan OpenRedirects and will then improve it over time. https://github.com/Proviesec/PSFuzz

And here is my story:

I was invited to a new private BugBounty programme and thought, well, I’ll look for the easy stuff first. Since I use Burp, I record my history with all redirects and links, which makes searching for bugs easier. After investigating a few simple security holes, I actually wanted to try to find some XSS stuff. I also like to use Google Dorks, for example I used

site:*redacted.com inurl:target 

and had a result, so I looked to see if it was suitable for an open redirect.

Steps To Reproduce:
Behind the google result was the login page of the website. And I always love to test these. And this time I noticed that the parameter target contained a whole URL, which was very tempting to test.
The url looks like this: https://my.redacted.com/forgetUsername?target=https:%2F%2Fwww.redacted.com
Therefore, you could already see that the link no longer jumps to the “my” subdomain but to the “www” subdomain.

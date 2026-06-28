---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-11-20_google-bug-bounty-nice-catch-on-google-cloud-platform-live.md
original_filename: 2014-11-20_google-bug-bounty-nice-catch-on-google-cloud-platform-live.md
title: 'Google Bug Bounty: Nice Catch on Google Cloud Platform Live'
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 78930f4ac8b7b13695ea786e6dcb01b6c8afe221ff90983804b9b4aa99ff7c52
text_sha256: 8f14cc18ce04b8ffd37264dc42c15fcf2877748eafea03948fd4e490c9f737ca
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Google Bug Bounty: Nice Catch on Google Cloud Platform Live

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-11-20_google-bug-bounty-nice-catch-on-google-cloud-platform-live.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `78930f4ac8b7b13695ea786e6dcb01b6c8afe221ff90983804b9b4aa99ff7c52`
- Text SHA256: `8f14cc18ce04b8ffd37264dc42c15fcf2877748eafea03948fd4e490c9f737ca`


## Content

---
title: "Google Bug Bounty: Nice Catch on Google Cloud Platform Live"
page_title: "Google Bug Bounty: Nice Catch on Google Cloud … | RCE Security"
url: "https://www.rcesecurity.com/2014/11/google-bug-bounty-nice-catch-on-google-cloud-platform-live"
final_url: "https://www.rcesecurity.com/2014/11/google-bug-bounty-nice-catch-on-google-cloud-platform-live/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Google"]
bugs: ["Reflected XSS"]
publication_date: "2014-11-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6357
---

# Google Bug Bounty: Nice Catch on Google Cloud Platform Live

Nov 20, 2014 · By [Julien Ahrens](/about/)

It’s been a while since I’ve published my last article, this is mainly because I’m currently working on a nice project overseas in Asia and enjoying this relaxed life here a little bit. Therefore I also keep this blog post a little short, because it’s just for the record.

In early September, I stumbled - more or less accidentally - over multiple Non-Persistent Cross-Site Scripting vulnerabilities on [Google’s Cloud Platform Live](https://www.gcp-live.com) while I was indeed searching for a cloud solution (funnily enough), but since the proxy is always running… ;-)

![](/2014/11/google-bug-bounty-nice-catch-on-google-cloud-platform-live/images/google-gcp-xss-0-1024x435-1.b0bc1c3345dc56efa85fa5742a4965888e9fb566e0894788431e65790502b148.png)

I’ve sent the bug report to Google and quickly received an answer from Jose of the Google Security Team with the - among bug hunters - beloved “Nice catch!” answer. Thanks to Jose at this point for his commitment and the really transparent disclosure process. This is a good example how vulnerability coordination should be handled!

I’ve received the bug bounty payment in the meanwhile and got listed in [Google’s Hall of Fame](https://www.google.com/about/appsecurity/hall-of-fame/reward/) \- please notice my awesome GIMP skills too ;-)

![google-gcp-xss-1](/2014/11/google-bug-bounty-nice-catch-on-google-cloud-platform-live/images/google-gcp-xss-1.4402f934b10a7bd62233d29866b010b3d303c16c7606250a303e9b75e22c55a5.png)

Now, I’m having some delicious Asian seafood paid by Google :-)…

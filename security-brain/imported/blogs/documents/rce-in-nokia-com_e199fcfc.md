---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-27_rce-in-nokiacom.md
original_filename: 2018-12-27_rce-in-nokiacom.md
title: RCE in nokia.com
category: documents
detected_topics:
- idor
- command-injection
- csrf
tags:
- imported
- documents
- idor
- command-injection
- csrf
language: en
raw_sha256: e199fcfc4cede9806b6538266a2c1302e29a4371088854721ce8a6a10a14f178
text_sha256: dd12515388aa157809486741e13b16fb22f95b3c066c1139a71cd96f69a6b85c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# RCE in nokia.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-27_rce-in-nokiacom.md
- Source Type: markdown
- Detected Topics: idor, command-injection, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e199fcfc4cede9806b6538266a2c1302e29a4371088854721ce8a6a10a14f178`
- Text SHA256: `dd12515388aa157809486741e13b16fb22f95b3c066c1139a71cd96f69a6b85c`


## Content

---
title: "RCE in nokia.com"
url: "https://medium.com/@sampanna/rce-in-nokia-com-59b308e4e882"
authors: ["Sampanna Chimoriya"]
programs: ["Nokia"]
bugs: ["RCE"]
publication_date: "2018-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5504
scraped_via: "browseros"
---

# RCE in nokia.com

RCE in nokia.com
Sampanna Chimoriya
Follow
2 min read
·
Dec 27, 2018

62

As I explained in my previous post I like to find and read various bug bounty so I love 
Pentester Land
. So, I was just browsing through bug bounty writeup and found a report on nokia. I didn’t know Nokia also had bug bounty so I decided give it a try. I like to use https://yandex.com to search for subdomains before using https://google.com or https://duckduckgo.com because I think yandex provides more exotic subdomains than google or duckduckgo for a bug bounty hunter.

So, I decided to use yandex to search for subdomain using site operator. After some scrolling I discovered http://emop.ext.net.nokia.com . It had a login prompt and looked really old so I thought maybe there are some vulnerabilites here. I like to use nikto to discover vulnerabilites for such websites. So I always use https://suip.biz/?act=nikto to scan for vulnerabilites using nikto. I absolutely love https://suip.biz because there are various tools like nikto, whatweb, sqlmap which can be used online thanks to https://suip.biz. I decided to use nikto and whatweb on nokia subdomain and found that it was a Drupal site. I immediately decided to check the version of Drupal and turns out it was vulnerable to various vulnerabilites like Drupalgeddon. So, I decided to send report to
security-alert@nokia.com and I received a message in two weeks to ask for my name to be featured in hall of fame . So, I decided to visit Nokia white hat page and it turned out it updates it’s page based on month. So, I will probably be featured in hall of fame after the end of this month.

Get Sampanna Chimoriya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The things I would like for you take away from this post are described below.

Always, always read bug bounty writeups and completely stalk a researcher you love in every social media you can find on him/her to find every tips and knowledge s/he would provide.
Use suip.biz because it provides great tools and as it’s completely free so more people should find and use it.
Use Yandex before Google or DuckDuckGo because in my opinion it provides subdomains which can be more vulnerable and useful for bug bounty hunter.
If you read more bug bounty then just like I automatically decided to check this subdomains you will understand which subdomain might be more vulnerable and which should be tested more than other subdomains. You will automatically decide to check for CSRF or IDOR after browsing a page because it would give you a feeling that it might be vulnerable to it and you would be more right about it than wrong.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-03_dev-xss-protection-bypass-made-my-quickest-bounty-ever.md
original_filename: 2017-12-03_dev-xss-protection-bypass-made-my-quickest-bounty-ever.md
title: DEV XSS Protection bypass made my quickest bounty ever!!
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 42208654a5246885cb0bbf3b91a28e866dc547f5f90c6d29cf1ab26d733fb5ca
text_sha256: 2c876adde311f792eddacbe4cd54e8eb8e0ece8e747a16a31a2c67e33c2ce67c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# DEV XSS Protection bypass made my quickest bounty ever!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-03_dev-xss-protection-bypass-made-my-quickest-bounty-ever.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `42208654a5246885cb0bbf3b91a28e866dc547f5f90c6d29cf1ab26d733fb5ca`
- Text SHA256: `2c876adde311f792eddacbe4cd54e8eb8e0ece8e747a16a31a2c67e33c2ce67c`


## Content

---
title: "DEV XSS Protection bypass made my quickest bounty ever!!"
url: "https://medium.com/@Skylinearafat/xss-protection-bypass-made-my-quickest-bounty-ever-f4fd970c9116"
authors: ["Yeasir Arafat"]
bugs: ["XSS"]
bounty: "150"
publication_date: "2017-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6037
scraped_via: "browseros"
---

# DEV XSS Protection bypass made my quickest bounty ever!!

DEV XSS Protection bypass made my quickest bounty ever!!
Yeasir Arafat
Follow
2 min read
·
Dec 3, 2017

133

3

Hi All,This is Yeasir Arafat here.I would love to share my last XSS which made my fastest bounty ever.I believe sharing is caring :D

So, this time I was able to bypass protection also able to manage some bounty with quick time.I have got some cool swag and little bounty to them before reporting this XSS to them :) .I had found HTML injection on their public discussion.At that time I was able to inject malicious script with HTML.

example of malicious script :

<a href=\”https://attacker/phish.php\"><img src=\”https://attacker/content.jpg\"></a><script>

After reporting this issue to them they filtering any malicious script with normal XSS payload.At that time me and my friend Shawar Khan tried to convert it to XSS but no luck :( .

After getting some cool swag they announced their bounty program.I thought why not some bounty also?

Get Yeasir Arafat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As bcz limited scope in DEV I start looking for XSS.I dropped some common payload like img src/svg onload bla bla bla but their firewall blocking me all the time.I put some advanced payload and see the response is different from other payloads.Like below picture,

Press enter or click to view image in full size
i-frame vulnerable

This was interesting,I thought may be i-frame payloads can trigger XSS here.Bit moment later I put advanced i-frame payload and got the stored one that can bypassed their filtering protection.Payload:

<iframe src=”data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E”></iframe>

Why this payload??

As I stated before that, after reporting HTML injections they filtering any malicious script but I noticed that their comment box is vulnerable to i-frame injections.Then I start looking for advanced i-frame XSS payload in Google found some and works that i-frame payload :) .

I quickly report it to them and got their fast response with 150$ bounty in less than 30 minutes.Which was my fastest bounty ever.

PoC video

Thanks

Yeasir Arafat

Web Application Security Researcher

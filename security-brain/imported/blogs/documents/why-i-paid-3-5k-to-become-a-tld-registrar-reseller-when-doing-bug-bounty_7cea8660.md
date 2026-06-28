---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-05_why-i-paid-35k-to-become-a-tld-registrar-reseller-when-doing-bug-bounty.md
original_filename: 2020-07-05_why-i-paid-35k-to-become-a-tld-registrar-reseller-when-doing-bug-bounty.md
title: Why I paid 3.5K to become a TLD registrar reseller when doing bug bounty
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 7cea8660b1d5e4efbc4ed5914232b3024f75abe983c908b2b280b31576d5ac01
text_sha256: 6b8a098221195d5f855a745f2051e75e9281a03e232322f9db8f8e7c0a85dc76
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Why I paid 3.5K to become a TLD registrar reseller when doing bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-05_why-i-paid-35k-to-become-a-tld-registrar-reseller-when-doing-bug-bounty.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `7cea8660b1d5e4efbc4ed5914232b3024f75abe983c908b2b280b31576d5ac01`
- Text SHA256: `6b8a098221195d5f855a745f2051e75e9281a03e232322f9db8f8e7c0a85dc76`


## Content

---
title: "Why I paid 3.5K to become a TLD registrar reseller when doing bug bounty"
url: "https://medium.com/@hgreal/why-i-paid-3-5k-to-become-a-tld-registrar-reseller-when-doing-bug-bounty-d9d407911dce"
authors: ["hg_real (@hgreal1)"]
bugs: ["XXE"]
bounty: "7,500"
publication_date: "2020-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4439
scraped_via: "browseros"
---

# Why I paid 3.5K to become a TLD registrar reseller when doing bug bounty

Why I paid 3.5K to become a TLD registrar reseller when doing bug bounty
hg_real
Follow
3 min read
·
Jul 6, 2020

330

2

I was looking for a new bug bounty target and found an interesting TLD registrar target, after doing some recon there was no decent scope until I saw that there was some reseller platform, i looked at the prerequisites to become a TLD registrar reseller and my mood went down. You needed the following requirements:

Have a web hosting company website
Have a support center so your customers can call you
Paying an initial 3.5 K upfront

After some chatting with a 2 other bug bounty hunters on slack we had a great idea! We were joking to set up a web hosting company and to pay for this and split the costs…

After some discussing we gave up on this idea

Press enter or click to view image in full size

This idea kept in my mind for a few months and I decided to give it a go

I did set up a website https://hgrealhosting.com and bought myself some webhosting company template and I was ready to go

Signed up and paid the initial 3.5K and got a mail that i would receive my password in my physical mailbox within 2 weeks.
2 weeks I patiently waited and then the mailman arrived with a letter containing my password 😎, ready for some bug hunting!

After doing recon on this reseller dashboard they were very secure
But I’m not giving up, doing some more research and went reading the EPP docs

an example can be found here https://docs.dnsbelgium.be/gtld/epp/

Get hg_real’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It is basicly an XML based protocol so I sent some XXE payloads and it wasn’t vulnerable.

When i was giving up on this target I went looking on every page again on this reseller dashboard and then I spotted some /etc/passwd output.

Why was this here, how the heck did I trigger this, apparently there is something called Second-order IDOR. when you make an IDOR request you don’t see the results, but you see the results on another page or a few requests later. actually when doing this XXE attack my results where seen on my reseller dashboard

I wrote a python script to sent XXE payloads to scan their server and web scraping the contents of these files on the reseller dashboard after every XXE request I finally I got some server passwords and much more.

I told this at my bug bounty comrades and gave them access to my account.
We got a few other bugs

All of a sudden my account got blocked and I got a call from their CISO

My reaction

“Well.. that’s some very strong social engineering you did to get access to our reseller dashboard. We never expected an ethical hacker would pay 3.5K just for new endpoints. Really appreciate this! we will sent this money back of course and thanks for the reports. The developers said it was out of scope but I told them it was in-scope”

Everthing went better than expected and we got 7.5K for our submissions and a refund.

My thoughts about paying money for extra untested endpoints

Just do it, but if you don’t find bugs and don’t get a refund you’re screwed 😆

Thanks for reading and happy hunting !

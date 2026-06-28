---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-06_self-xss-leads-to-blind-xss-and-reflected-xss.md
original_filename: 2018-08-06_self-xss-leads-to-blind-xss-and-reflected-xss.md
title: Self XSS leads to blind XSS and reflected XSS.
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
raw_sha256: b877b548828b2d8e92d1b9409fc6fe7b58017f73e7047b4880a38caa38f63970
text_sha256: be1fb26885002579f7d253e7685d37b8659f8c1dfd42bed03a9ca413cc560bcf
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Self XSS leads to blind XSS and reflected XSS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-06_self-xss-leads-to-blind-xss-and-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `b877b548828b2d8e92d1b9409fc6fe7b58017f73e7047b4880a38caa38f63970`
- Text SHA256: `be1fb26885002579f7d253e7685d37b8659f8c1dfd42bed03a9ca413cc560bcf`


## Content

---
title: "Self XSS leads to blind XSS and reflected XSS."
url: "https://medium.com/@friendly_/self-xss-leads-to-blind-xss-and-reflected-xss-950b1dc24647"
authors: ["Friendly (@SkeletorKeys)"]
bugs: ["Blind XSS", "Reflected XSS"]
bounty: "700"
publication_date: "2018-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5771
scraped_via: "browseros"
---

# Self XSS leads to blind XSS and reflected XSS.

Self XSS leads to blind XSS and reflected XSS.
Friendly
Follow
3 min read
·
Aug 7, 2018

174

3

In regards to this tweet: https://twitter.com/Skeletorkeys/status/1026497897871884289

Important Note:

This website does not want me to disclose their website name,until they have setup their Bounty Program, which I will disclose in the future if they allow me to — or they will likely do it themselves from my interpretation on what they said. However in this post, I will explain to my best knowledge on how KNOXSS plays a role here, how I got a blind XSS through a self XSS and a reflected XSS.

If you message me on Twitter for help, then I will try my best to assist you! But regarding this website will be a straight NO. My reason is simple for that: I do not want to break their privacy nor lose my contact with them, or any other future bounties this website has to offer me.

I don’t expect this to work for everyone, or some of you since each websites WAF security is different than-one-and-another — and how it works.

Now to the fun part:

To XSS yourself on this website was the most trickiest part and difficult part. When I tried to input the following tags : ", ', ><, / and \ — I saw that they were being filtered in their live support chat and wasn’t being rendered in at all. After spending 20 - 30 mins, I tried some HTML entities and I saw my outputs being rendered in regular tags, so I decided to cook up an image tag XSS.

That being said, I used the following HTML entities: &quot;&gt;&lt;img src=x onerror=alert(1);&gt; and my output became "><img src=x onerror=alert(1);> which then gave me this:

OUR MAGICAL CONFIRMATION “1” :D

Then their live support team member messaged me saying: “Hey did you send a popup box with a message saying “1”, and I responded with “Yes I did.” That moment I knew I had a blind XSS which reflects back into their Admin Panel.

So I quickly cooked up another payload to grab their cookies — the big boys cookies. That moment I knew I had access to their Administrators and Devs account. I swiftly contacted them and their Administrators again and I was asked me if I could login as them and give a proof of concept — which I did.

Logged in and changed their names to my name for a bit more proof of concept. They were shocked.

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

They asked me for my PayPal to send me a lil something, something. ;)

I was awarded $500 for this with the reason “Security Guy.” Ha.

However, I didn’t stop there. Next part is using KNOXSS and Sublist3r —

I used Sublist3r which helped me locate and able to find all their subdomains. I found one of their subdomain http://search.websitename.com which wasn’t listed on their website at all and it wasn’t secured at all. Just had a search box, a bunch of outdated information.

First I tried "><svg/onload=alert(1)> and I got no alert. Which was a bummer. I tried every single possible payload I could think of and got no result. So I went to KNOXSS and posted my POST DATA and saw something interesting which was %3E%3CScrip%3E being rendered in the URL as ></Script>. So I did a quick Google and found a payload that was similar to something I was using, and that payload was:

1%3C!%27/*%22/*\%27/*\%22/* — %3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm1%20//%3E#

I input that in my URL with my POST DATA and got my little confirmation 1. I quickly contacted their Administrators and Devs and explained how dangerous this can be and how bad it could be. They agreed with me and quickly took down that subdomain.

I was then rewarded $200 for a reflected XSS and with a little reason: “Try to reflect this back.” They have a great sense of humor. Ha.

Total bounty for the day: $700 USD

If you have any questions or comments, feel free to message me on Twitter, or tweeting me @Skeletorkeys

Thank you for reading and I hope this is informative enough and I do apologize for not sharing that domain with you all. Again, this isn’t my choice it’s the websites choice and I respect that and I hope you guys do as well.

I probably used some terms wrong too. Heh.

Anyways, thanks for reading.

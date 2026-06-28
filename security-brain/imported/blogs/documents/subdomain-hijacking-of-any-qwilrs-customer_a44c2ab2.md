---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-01_subdomain-hijacking-of-any-qwilrs-customer.md
original_filename: 2023-01-01_subdomain-hijacking-of-any-qwilrs-customer.md
title: Subdomain Hijacking Of Any Qwilr’s Customer
category: documents
detected_topics:
- idor
- oauth
- sso
- xss
- command-injection
- otp
tags:
- imported
- documents
- idor
- oauth
- sso
- xss
- command-injection
- otp
language: en
raw_sha256: a44c2ab2e9662162cb37ed2250ef8b4e66a91e155f2eda13ba2aa6b8fe25bbea
text_sha256: 354fafbde6a61105283cb80e69b96f70e2637fa354247ee523d124838d3c2218
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Hijacking Of Any Qwilr’s Customer

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-01_subdomain-hijacking-of-any-qwilrs-customer.md
- Source Type: markdown
- Detected Topics: idor, oauth, sso, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `a44c2ab2e9662162cb37ed2250ef8b4e66a91e155f2eda13ba2aa6b8fe25bbea`
- Text SHA256: `354fafbde6a61105283cb80e69b96f70e2637fa354247ee523d124838d3c2218`


## Content

---
title: "Subdomain Hijacking Of Any Qwilr’s Customer"
page_title: "Subdomain Hijacking Of Any Qwilr’s Customer - 0xPrial"
url: "https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/"
final_url: "https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/"
authors: ["Prial Islam Khan (@prial261)"]
bugs: ["Subdomain takeover"]
publication_date: "2023-01-01"
added_date: "2023-01-02"
source: "pentester.land/writeups.json"
original_index: 1717
---

Skip to content

[ ![](https://0xprial.com/wp-content/uploads/2022/01/prial-islam65.png) ](https://0xprial.com)

  * [Home](https://0xprial.com/)
  * [About Me](https://0xprial.com/#aboutme)
  * [Skills](https://0xprial.com/#skils)
  * [Services](https://0xprial.com/#services)
  * [Acknowledgements](https://0xprial.com/#acknowledgements)
  * [Write-Ups](https://0xprial.com/#writeUps)

__ Menu

  * [Home](https://0xprial.com/)
  * [About Me](https://0xprial.com/#aboutme)
  * [Skills](https://0xprial.com/#skils)
  * [Services](https://0xprial.com/#services)
  * [Acknowledgements](https://0xprial.com/#acknowledgements)
  * [Write-Ups](https://0xprial.com/#writeUps)

[ Contact Me ](https://0xprial.com/contact)

![](https://0xprial.com/wp-content/uploads/2023/01/Subdomain-Hijacking-OF-Any-Qwilrs-customer-1024x597.png)

# Subdomain Hijacking Of Any Qwilr’s Customer

First Happy new year to **fellow Hackers** ,

I was planning to write on my blog regularly for the last few months, but I could not do that due to my lack of time and laziness. So here’s a new year gift for you guys ?

Back in October 2022, I was testing a really old private program on HackerOne and they were running a bug bounty program when I started my journey on this platform. So I thought let’s take a look at this target.

Their scope was ***.target.com** and you know what to do next! After doing Subdomain Enumeration I always check all subdomains based on the below points –

  * Print all DNS records. I mostly use – `for sub in $(cat subdomains.txt);do dig $sub +noquestion +noauthority +noadditional +nostats | grep -wE "CNAME|A"`
  * Print live subdomain titles and status codes. I mostly use – `cat subdomains.txt |httpx -status-code -content-length -title -tech-detect -follow-redirects`

Nothing special caught my attention. But few of the subdomains were pointing to **< subdomain>.target.info** and this time I passively enumerated subdomains for this **.info** TLD from [**project sonar FDNS**](https://opendata.rapid7.com/sonar.fdns_v2/)datasets as this **.info** TLD is not listed in the target’s scope and I don’t want to create any unwanted incident. Also, I was only interested to take a look at this **.info** TLD as the program scope was a wildcard and I know most of the wildcard programs accept **DNS Hijacking** issues for any of their assets. Then I noticed two of the subdomains are pointing to the **CNAME** record **custom-domains.qwilr.com**

![CNAME-Record](https://0xprial.com/wp-content/uploads/2023/01/CNAME-Record.png)

This caught my attention as visiting these domains was responding like the below screenshot – 

![Qwilr error](https://0xprial.com/wp-content/uploads/2023/01/qwilr-error.png)

This error looks suspicious. So I quickly googled available docs on Qwilr’s custom domain setup and I found [**this page**](https://help.qwilr.com/article/63-custom-domain) where they mentioned only enterprise plan users can set up a custom domain. I registered a trial account and tried to use the custom-domain feature from **https://app.qwilr.com/#/settings/** and it always gives a popup like the below –

![Custom domain requirements](https://0xprial.com/wp-content/uploads/2023/01/Custom-domain-requirments.png)

So no way to check if our target’s subdomains were actually claimed or not. While I was quitting on this I noticed they have the option at [**https://app.qwilr.com/#/settings/subdomain**](https://app.qwilr.com/#/settings/subdomain) to get a subdomain of your choice like **< your_subdomain>.qwilr.com** and serve your pages on that subdomain. 

As you can get a subdomain of **qwilr.com** and the custom domain setup required **CNAME** record is **custom-domains.qwilr.com** which is also a subdomain of that domain, so what will happen if I can claim this `custom-domains` prefix from my trial account? Most of the time if vendors offer such subdomains as services they blacklist or reserve a few keywords like admin, support, app, login, etc for their usage or security purposes. But in the case of Qwilr’s they didn’t take any such steps that allowed me to use the `custom-domains` prefix from my trial account.

![Available to claim](https://0xprial.com/wp-content/uploads/2023/01/Available-to-claim.png)

We all know **CNAME records** can be used to alias one name to another and our target subdomain’s CNAME is **custom-domains.qwilr.com** which is claimed by me and I can serve contents on it. So technically my Qwilr pages should be accessible from all domains which are pointing to the CNAME unless there is any additional configuration in place in the backend.

So I created a PoC page from [**https://app.qwilr.com/#/pages**](https://app.qwilr.com/#/pages) and copied the shareable URL what looks like [**https://custom-domains.qwilr.com/0xPrial-3tI11SSQiC5z**](https://custom-domains.qwilr.com/0xPrial-3tI11SSQiC5z). The next thing I did was replaced the subdomain with **< subdomain>.target.info** and visited the URL and boom – ![Takeover PoC](https://0xprial.com/wp-content/uploads/2023/01/Takeover-PoC.png)

Again I replaced the subdomain with the other subdomain **partnerships.target.info** and it’s also reflecting my PoC.

![Takeover PoC 2](https://0xprial.com/wp-content/uploads/2023/01/Takeover-PoC-2.png)

So I again used the [**project sonar FDNS**](https://opendata.rapid7.com/sonar.fdns_v2/)datasets to look for all DNS records that are pointed to **CNAME** **custom-domains.qwilr.com**

![FDNS Records](https://0xprial.com/wp-content/uploads/2023/01/FDNS-Records.png)

300+ subdomains using that record and I confirmed all of them are vulnerable and I can access my PoC from all of those subdomains. A few of the PoC are listed below –

![PoC burnrate.io](https://0xprial.com/wp-content/uploads/2023/01/PoC-burnrate.io_.png)**PoC burnrate.io** ![Yale University PoC](https://0xprial.com/wp-content/uploads/2023/01/PoC-yale.edu_.png)**Yale University PoC** ![Stanford University PoC](https://0xprial.com/wp-content/uploads/2023/01/PoC-Standford.edu_.png)**Stanford University PoC** ![PoC TravelBank](https://0xprial.com/wp-content/uploads/2023/01/PoC-TravelBank.png)**PoC TravelBank** ![PoC DEPT®](https://0xprial.com/wp-content/uploads/2023/01/PoC-DEPT.png)**PoC DEPT®**

I created two submissions on HackerOne and they **Triaged** both reports and forwarded the issue to the Qwilr support team immediately. I also forwarded this to a few other bug bounty programs and one of them confirmed they have an active working service. So this proves I can hijack and serve my PoC content on both claimed and non-claimed subdomains.

![burnrate CEO reply](https://0xprial.com/wp-content/uploads/2023/01/burnrate-CEO-reply.png)

Another program replied with additional info that confirms my theory –

![Rewarded](https://0xprial.com/wp-content/uploads/2023/01/Rewarded.png)

### **Timeline**

  * Discovered the vulnerability – **25 October, 2022**
  * Created HackerOne Submissions – **25 October, 2022**
  * HackerOne Triaged both reports – **26 October, 2022**
  * Created other Bug Bounty Submissions – **27 October, 2022**
  * The vulnerability was Fixed By Vendor – **Nov 01, 2022**
  * Both HackerOne report was rewarded – **Nov 09, 2022**
  * Got a few rewards & cool swags from other programs.

### **Remarks**

  * Never test OOS assets actively. If you want to do it ask for proper permission and try to reduce the noise.
  * Never test a 3rd party vendor unless they have a responsible disclosure policy.
  * Always read 3rd party vendor docs and look into all options of their services.
  * Think out of the box.

**./logout**

Post Views: 25,954

  * [ January 1, 2023  ](https://0xprial.com/2023/01/01/)
  * 2:58 am 
  * [ One Comment  ](https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/#comments)

[ Back To Blog ](https://0xprial.com/0xprialw/blog/)

[ Back To Home ](https://0xprial.com)

##  One Response 

  1. ![](https://secure.gravatar.com/avatar/50aff0a90c84088fc95b863f1fb1ec9936a880091b32bd899d0bffb41452b5d5?s=42&d=mm&r=g) **itissoul** says:

[January 1, 2023 at 10:05 AM](https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/#comment-338)

The so valuable and help full for me. Thank you so much for share

Reply

## Leave a Reply [Cancel reply](/subdomain-hijacking-of-any-qwilrs-customer/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

**Captcha** *

![](data:image/png;base64,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)Type the text displayed above:

## RECENT TWEETS 

[Tweets by 0xPrial](https://twitter.com/0xPrial?ref_src=twsrc%5Etfw)

## RECENT POSTS 

[ ![The Art Of Zendesk Hijacking](https://0xprial.com/wp-content/uploads/2023/11/The-Art-Of-Zendesk-Hijacking-768x448.png) ](https://0xprial.com/the-art-of-zendesk-hijacking/)

Bug Bounty

###  [ The Art Of Zendesk Hijacking ](https://0xprial.com/the-art-of-zendesk-hijacking/)

[ ![](https://0xprial.com/wp-content/uploads/2021/05/IDOR-Leads-To-Leak-Any-Uber-Restaurants-Analytics-1-768x448.png) ](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/)

Bug Bounty

###  [ IDOR Leads To Leak Any Uber Eats Restaurant Analytics ](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/)

[ ![](https://0xprial.com/wp-content/uploads/2021/02/HOW-TO-GET-STARTED-IN-BUG-BOUNTY-768x402.png) ](https://0xprial.com/how-to-get-into-bug-bounties-part-01/)

Bug Bounty

###  [ How to Get Into Bug Bounties – Part 01 ](https://0xprial.com/how-to-get-into-bug-bounties-part-01/)

[ ![](https://0xprial.com/wp-content/uploads/2020/03/XSS-WAF-Character-limitation-bypass-like-a-boss-768x448.png) ](https://0xprial.com/xss-waf-character-limitation-bypass-like-a-boss/)

Bug Bounty

###  [ XSS WAF & Character limitation bypass like a boss ](https://0xprial.com/xss-waf-character-limitation-bypass-like-a-boss/)

[ ![](https://0xprial.com/wp-content/uploads/2019/01/Unicode-vs-WAF-—-XSS-WAF-Bypass-768x448.png) ](https://0xprial.com/unicode-vs-waf-xss-waf-bypass/)

Bug Bounty

###  [ Unicode vs WAF — XSS WAF Bypass ](https://0xprial.com/unicode-vs-waf-xss-waf-bypass/)

[ ![](https://0xprial.com/wp-content/uploads/2018/11/XSS-bypass-using-META-tag-in-realestate.postnl.nl_-768x448.png) ](https://0xprial.com/xss-bypass-using-meta-tag-in-realestate-postnl-nl/)

Bug Bounty

###  [ XSS bypass using META tag in realestate.postnl.nl ](https://0xprial.com/xss-bypass-using-meta-tag-in-realestate-postnl-nl/)

[ ![](https://0xprial.com/wp-content/uploads/2022/01/prial-islam65.png) ](https://0xprial.com/home)

Sometimes, Hacking Is Just Someone Spending More Time On Something Than Anyone Else Might Reasonably Expect 

[ Facebook ](https://www.facebook.com/0xPrial/) [ Icon-x-twitter __](https://twitter.com/0xprial) [ Linkedin ](https://www.linkedin.com/in/0xprial/) [ Youtube ](https://www.youtube.com/0xprial) [ Github ](https://github.com/0xPrial/)

# Useful Link 

  * [ Contact ](https://0xprial.com/contact)
  * [ Privacy Policy ](https://0xprial.com/privacy-policy)
  * [ Terms & Condition ](https://0xprial.com/terms-condition)
  * [ Site Map ](https://0xprial.com/site-map)

# Newsletter

Name

Email

SUBSCRIBE

__

© All Rights Reserved By [Prial Islam](https://www.linkedin.com/in/0xprial/)

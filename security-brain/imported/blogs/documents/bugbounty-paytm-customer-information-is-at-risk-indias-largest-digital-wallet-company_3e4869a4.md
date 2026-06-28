---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-03_bugbounty-paytm-customer-information-is-at-risk-indias-largest-digital-wallet-co.md
original_filename: 2018-08-03_bugbounty-paytm-customer-information-is-at-risk-indias-largest-digital-wallet-co.md
title: '#BugBounty — @Paytm Customer Information is at risk — India’s largest digital
  wallet company'
category: documents
detected_topics:
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: 3e4869a439e432708f5a5b89918249e7d5324f3da93b461064bcab394462c1c9
text_sha256: f56e6bee002fd9c18e0cf6e9edb23287c8155fac194a20beed359c86c9f236fe
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — @Paytm Customer Information is at risk — India’s largest digital wallet company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-03_bugbounty-paytm-customer-information-is-at-risk-indias-largest-digital-wallet-co.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `3e4869a439e432708f5a5b89918249e7d5324f3da93b461064bcab394462c1c9`
- Text SHA256: `f56e6bee002fd9c18e0cf6e9edb23287c8155fac194a20beed359c86c9f236fe`


## Content

---
title: "#BugBounty — @Paytm Customer Information is at risk — India’s largest digital wallet company"
page_title: "#BugBounty — @Paytm Customer Information is at risk — India’s largest digital wallet company | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-paytm-customer-information-is-at-risk-indias-largest-digital-wallet-company-6f7116d4b2d5"
authors: ["Avinash Jain (@logicbomb_1)"]
programs: ["Paytm"]
bugs: ["IDOR"]
publication_date: "2018-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5777
scraped_via: "browseros"
---

# #BugBounty — @Paytm Customer Information is at risk — India’s largest digital wallet company

#BugBounty — @Paytm Customer Information is at risk — India’s largest digital wallet company
Avinash Jain (@logicbomb)
Follow
3 min read
·
Aug 3, 2018

486

4

Hi Guys,

Recently, I have found a serious vulnerability in Paytm (India’s largest digital wallet company ). Through which I was able to access every other user’s information containing their bill details, name , address etc. When I first reported to Paytm Security team , they did accept it but didn’t fix it saying “It is according to their functionality and third party issue”.

Then I tested out the same thing in other e-wallet companies like Mobikwik, Freecharge but fortunately they are not doing but they shouldn’t do, this vulnerability and such user information disclosure was not there. I again reported it to Paytm Team and this time they were quick to accept it.

Press enter or click to view image in full size
Issue re-reported to Paytm
Press enter or click to view image in full size
Paytm Team Response

Let’s see the technical details —

While doing online payment for electricity bill, I happened to reach this section —

Press enter or click to view image in full size
Online Electricity Payment — Paytm

After filing the required details that is my account number and associated mobile number , I was simply presented with my bill information-

Press enter or click to view image in full size
Bill Details

Let’s check the HTTP request triggered —

Press enter or click to view image in full size
HTTP Request for getting bill information

As it can be seen , mobile number(recharge_number_2) and account number (recharge_number) is getting passed in order to validate the correct combination of both and presenting user with his bill details.But this is not what I thought it should be . I proceeded to change the account number i.e recharge_number parameter keeping any random mobile number and I was able to fetch complete bill details of some other user associated with that account number —

Press enter or click to view image in full size
Other user bill details disclosure

I was expecting Paytm must be having a strong application firewall and they should have placed some throttling over repeated requests but again there was nothing like this . I run intruder (bruteforcing) over consumer number and within couple of hours , I was having thousands of User’s bill information containing their name, address , bill amount , dob etc.

Press enter or click to view image in full size
User Information disclosure
Press enter or click to view image in full size
User Information disclosure

And this is how I was able to access information of other users in Paytm.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )

Report details-

27-Nov-2017 — Bug reported to the concerned company.

5-Jan-2018 — Bug was marked fixed.

5-Jan-2018 — Tested and confirmed the fix.

5-Jan-2018 — Rewarded by company.

21-June-2018 — Bug re-opened.

25-July-2018 — Rewarded by company.

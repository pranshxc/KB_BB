---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-29_business-logic-vulnerabilities.md
original_filename: 2022-07-29_business-logic-vulnerabilities.md
title: Business logic vulnerabilities
category: documents
detected_topics:
- business-logic
- command-injection
- api-security
tags:
- imported
- documents
- business-logic
- command-injection
- api-security
language: en
raw_sha256: dbd12cfd75ac9097594b3a04511d0f25a19a520d5bcb5b0df97384094b78b29c
text_sha256: c96509d7994d3d349d59c145fd575e38ab5c784c798faee893edcea6e7f0a817
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Business logic vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-29_business-logic-vulnerabilities.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `dbd12cfd75ac9097594b3a04511d0f25a19a520d5bcb5b0df97384094b78b29c`
- Text SHA256: `c96509d7994d3d349d59c145fd575e38ab5c784c798faee893edcea6e7f0a817`


## Content

---
title: "Business logic vulnerabilities"
page_title: "Business Logic Vulnerabilities == $$$ | by Sagar Sajeev | Medium"
url: "https://sagarsajeev.medium.com/business-logic-vulnerabilities-b4db2af08aaf"
authors: ["Sagar Sajeev (@Sagar__Sajeev)"]
bugs: ["Logic flaw", "Payment tampering"]
bounty: "400"
publication_date: "2022-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2382
scraped_via: "browseros"
---

# Business logic vulnerabilities

Top highlight

Sagar Sajeev
Follow
3 min read
·
Jul 29, 2022

659

7

How’s it going everyone! My name is Sagar Sajeev. I had found an interesting Business Logic Flaw and wanted to share it with you guys.

According to OWASP , Business Logic Vulnerabilities are ways of using the legitimate processing flow of an application in a way that results in a negative consequence to the organization.

How did I find it?
This Particular target E-Commerce website offers 15% instant discount for purchases which span a total of $400 or above (T&C’s apply).
I added some products to the cart so as to reach the $400 threshold cart value.
The 15% discount coupon was added automatically.
At the last checkout page, they’ll show you all the items that have been added. Well, they had an option to remove any item from the cart.
I removed a bunch of items and bought down the cart value to around $120.
To my surprise, the coupon was still valid and I was offered 15% instant discount even though the cart value was less than $400.
I made the purchase for $120 and as per the invoice the discount was indeed applied.
Reported this vuln to the Security department of the E-Commerce site and it was rated as a high severity bug.

(P.S — I did ask them whether I could make a writeup on this. They said it was fine, but they specifically asked me not to mention their Website name anywhere. That’s why I didn’t include any target name in this writeup.)

I was awarded $400 as bounty and an additional $200 coupon which can be redeemed for any purchases made only in this particular E-Commerce website.
The Sec team was super helpful. They responded, resolved and rewarded the bounty, all within 24hrs.
Press enter or click to view image in full size

Tip — Most of the time Logic vulns will be unique in its own way. So perhaps the best approach would be trying out stuff which can break the application logic. If some application function seems obvious to you, try thinking what/how it can be exploited by a malicious user.

Timeline

Submitted : 28–07–2022

Get Sagar Sajeev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Accepted : 28–07–2022

Resolved : 29–07–2022

Bounty Awarded : 29–07–2022

I hope y’all would have learned something new today. I’ve made two other writeups. Please do check them out as well.

I do share tips about Bug Bounties and related stuff every now and then over at my Twitter and LinkedIn handle. So do follow me there.

LinkedIn : https://www.linkedin.com/in/sagar-sajeev-663491208/
Twitter : https://twitter.com/Sagar__Sajeev

If you’ve got any queries, feel free to message me. I will be more than happy to help.

Happy Hacking!

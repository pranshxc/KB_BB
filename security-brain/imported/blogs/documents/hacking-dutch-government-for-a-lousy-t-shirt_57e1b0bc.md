---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_hacking-dutch-government-for-a-lousy-t-shirt.md
original_filename: 2021-09-02_hacking-dutch-government-for-a-lousy-t-shirt.md
title: Hacking Dutch Government For a lousy T-shirt
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: 57e1b0bc29501fe933f588e744f7411ce7a472942cc772c3ea72eaed616566d5
text_sha256: 144f6355a7126ee0af28dc5dedf1ad5c2d18b56fce96fed7348883612b73e21e
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Dutch Government For a lousy T-shirt

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_hacking-dutch-government-for-a-lousy-t-shirt.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `57e1b0bc29501fe933f588e744f7411ce7a472942cc772c3ea72eaed616566d5`
- Text SHA256: `144f6355a7126ee0af28dc5dedf1ad5c2d18b56fce96fed7348883612b73e21e`


## Content

---
title: "Hacking Dutch Government For a lousy T-shirt"
url: "https://medium.com/pentesternepal/hacking-dutch-government-for-a-lousy-t-shirt-8e1fd1b56deb"
authors: ["Veshraj Ghimire (@GhimireVeshraj)"]
programs: ["Dutch Government"]
bugs: ["IDOR", "Information disclosure"]
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3360
scraped_via: "browseros"
---

# Hacking Dutch Government For a lousy T-shirt

Hacking Dutch Government For a lousy T-shirt
Veshraj Ghimire
Follow
3 min read
·
Sep 2, 2021

458

5

Good day, everyone! Greetings, As this is my first post on Pentester Nepal, I’d want to thank you for taking the time to read it. Allow me to begin by providing a brief introduction of myself. I’m Veshraj Ghimire, an infoSec enthusiast who is passionate about offensive security (mostly web application). Recently I was rewarded with cool swag by dutch government for finding vulnerability on their assets. So, in this article, I’ll answer some of the questions that people have asked me about it.

Press enter or click to view image in full size
The lousy tshirt is so cool actually😛
What was the issue and how did you found it?

One day, while i was scrolling twitter as usual. I got to know about National Cyber Security Centre rewarding with cool swags, which got my attention. Then i planned to look after it to get my first swag. I gathered some domains from GitHub then started with subdomain enumeration. As soon as I had a list of subdomains, I wanted to check out some. It took me a while to discover that a subdomain of bkwi.nl was using Gitlab. I thought to look after previously found misconfigurations on gitlab. After spending some time to look after possible vulnerabilities on Gitlab, i got GitLab User Information Disclosure Via Open API. https://gitlab.bkwi.nl/api/v4/users/31 was disclosing informations of user 31 similarly, upon brute-forcing last digits, i got information of many other users being disclosed.

Press enter or click to view image in full size
GitLab User Information Disclosure Via Open API

So, the bug was this simple, due to the Gitlab misconfiguration, it was possible to disclose the information about users.

How Long did it took for you to receive the swag?

1. Reported : Fri, Jun 25, 10:45 PM

2. Got replied with “we will process your report in accordance with our Responsible Disclosure Policy” : Fri, Jun 25, 10:59 PM

3. Got replied with “We have confirmed your report and have informed the responsible organization. When they inform us that the issue is fixed, we will let you know. If they have questions we will also contact you.” : Jun 28, 2021, 5:16 PM

4. It was fixed and Got replied with:

Get Veshraj Ghimire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“Dear Veshraj,

The vulnerability you reported has been fixed.

As a token of our appreciation we would like to offer you a T-shirt. If you
would like a T-shirt please provide us with your preferred T-shirt size
(S/M/L/XL) and on what address you would like to receive the T-shirt.
Please, be compliant with the international address standard [0] when you
write down your address.” : Jul 6, 2021, 5:35 PM

5. Finally, received the cool swag : August 21, 2021.

Can I report my findings and get swags?

Yes, you can go through this Blog and know more about reporting the vulnerabilities on National Cyber Security Centre. Once the issue will get accepted and fixed, you will be rewarded with cool T-shirt.

What are in scope Domains?

The scope fot this program is actually huge. Every sites managed by dutch government are in scope. So, you can choose any of them and start looking for security vulnerabilities. You can also find some of the in scope domains here.

What if i found multiple vulnerabilities?

I also tried reaching out team and asked what if one finds multiple vulnerabilities on their assets and their answer was:

many vulns= many swags hehe

That’s all there is to it; Thank you for sticking with me until the end. If you have any questions concerning this post, please feel free to ask. If you’d like to communicate with me, you can find me on Twitter. That concludes the story of how i got my first swag. Stay Safe✌️✌️

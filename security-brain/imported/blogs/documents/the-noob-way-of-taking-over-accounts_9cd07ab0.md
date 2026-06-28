---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-29_the-noob-way-of-taking-over-accounts.md
original_filename: 2020-07-29_the-noob-way-of-taking-over-accounts.md
title: The Noob Way Of Taking Over Accounts
category: documents
detected_topics:
- access-control
- idor
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 9cd07ab0fbb311581a6705fd4188ee4c2bb8b336ae1cf76c8dd8403fea9f61d9
text_sha256: 55c43b38168894f1c37b31d2058bd042bfc565fe4ff55b6ee4210886a7e29a1b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The Noob Way Of Taking Over Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-29_the-noob-way-of-taking-over-accounts.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9cd07ab0fbb311581a6705fd4188ee4c2bb8b336ae1cf76c8dd8403fea9f61d9`
- Text SHA256: `55c43b38168894f1c37b31d2058bd042bfc565fe4ff55b6ee4210886a7e29a1b`


## Content

---
title: "The Noob Way Of Taking Over Accounts"
page_title: "THE NOOB WAY OF TAKING OVER ACCOUNTS | by Mudassir Sharief | Medium"
url: "https://medium.com/@mudassirsharief58/the-noob-way-of-taking-over-accounts-81aee783c064"
authors: ["Mudassir Sharief"]
bugs: ["Broken authorization", "Account takeover", "Homograph attack"]
bounty: "955"
publication_date: "2020-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4372
scraped_via: "browseros"
---

# The Noob Way Of Taking Over Accounts

THE NOOB WAY OF TAKING OVER ACCOUNTS
Mudassir Sharief
Follow
4 min read
·
Jul 29, 2020

167

2

Hello Readers! Welcome to my another blog post, today I am going to share a very interesting finding which is Account takeover, well there are multiple ways of doing so, it basically depends on functionalities available in the application. So this post will be limited to my approach and finally will share some handy tips. Before I start i would like to give a huge shout out to 
Dimitrios Bougioukas
 and his excellent course eWPTX, highly recommended this course gives you the best knowledge for WebAppSec out there and its because of this course and its basics i was able to perform this attack successfully.

Lets Start …….

A brief information about the target,the target allows user’s to register their companies. once you setup the company you become the admin of the company at target.com and you will have the privilege to add your colleagues and set their privileges. Please note that Only you can set their privileges. Moving on, target.com also allows its users to have internal communications, share resources and so on.

Firstly, I registered a company with my email, I named the company as “Tommy” and i became the Admin for this company at target.com. Cool.

Press enter or click to view image in full size
Press enter or click to view image in full size

Now, the target.com will not allow any other user who is trying to register with the same Company named as “Tommy”. If any one tries to register it will throw this message “The company Tommy is already setup and contact the Admin”

Press enter or click to view image in full size
Interesting RIGHT?

Target.com has implemented some Validations, and it just took 10 mins to bypass it.

I used a technique called “Visual Spoofing|Homoglyph ” which is “In typography, a Homoglyph is one or two or more characters, or glyphs, with shapes that either appear identical or cannot be differentiated by quick visual inspection.”

An additional classification is:

HOMOGRAPH — > a word that looks the same as another word

Get Mudassir Sharief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

HOMOGLIPH — > a look-alike character used to create homographs

I went back on the Registration page and Re- registered the same company with different email, I just replaced “Tommy” with “Tömmy” and guess what I became the Admin for the company “Tommy”

Press enter or click to view image in full size

It was a Complete Vertical Privilege Escalation…

Now I can delete the real Admin from its own Company, can download all the information which was shared among the colleagues basically completely take over the Organization.

The severity for this finding was rated as → 9.1/10

And finally was awarded with 955$ bounty :D

TIPS:

If the validations are implemented on client side it can be bypassed in multiple ways, if you try this technique and it doesn't work fine for you, try permutations and combinations like perform the visual spoofing on client side and capture the packet with burp and change back to its real form and so on.
I always use a Firefox plugin called “Containers” for testing IDOR’s and privilege Escalations. Try out this amazing extension.
Don’t give up, Consistency is very important. Be active, learn new ways and try to be creative.
And again THE BUGS are out THERE, HUNT THEM ALL ;)

Thank You for reading I hope this write-up proves beneficial for you all :)

Get in touch on LinkedIn: https://www.linkedin.com/in/mudassir-sharief-568717152/

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-05_shopify-multipass-misconfiguration.md
original_filename: 2021-06-05_shopify-multipass-misconfiguration.md
title: Shopify Multipass Misconfiguration
category: documents
detected_topics:
- command-injection
- password-reset
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- business-logic
- api-security
language: en
raw_sha256: c857575ef4a20a6c1dabcc101a3ac7897db9819c21e761a63f2a01e2f0111f97
text_sha256: 5007499016b543ab87ef5e8b2f287efa60f9e54170b1a65e4355d1f9631b1a07
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Shopify Multipass Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-05_shopify-multipass-misconfiguration.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, business-logic, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `c857575ef4a20a6c1dabcc101a3ac7897db9819c21e761a63f2a01e2f0111f97`
- Text SHA256: `5007499016b543ab87ef5e8b2f287efa60f9e54170b1a65e4355d1f9631b1a07`


## Content

---
title: "Shopify Multipass Misconfiguration"
url: "https://batee5a.medium.com/shopify-multipass-misconfiguration-2bc85e92ad1d"
authors: ["Ahmed A. Sherif"]
bugs: ["Broken authentication", "Logic flaw"]
publication_date: "2021-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3596
scraped_via: "browseros"
---

# Shopify Multipass Misconfiguration

Shopify Multipass Misconfiguration
Ahmed A. Sherif (Batee5a)
Follow
3 min read
·
Jun 5, 2021

116

Press enter or click to view image in full size

Hello,

I decided to write this article as I noticed it is not mentioned anywhere else in the bug-bounty tips and went un-noticed for a large amount of time as I found this in 2021 on targets that started their bug bounty programs in 2014 (Large time for such vulnerability to go un-noticed) and it could land you a Medium->Critical report depending on the policies of the program.

Summary:

Shopify offers a functionality called Multipass Login, It basically redirects the users from the main website to the shopify store of that website and logs them in with the same email address they used to sign-up for in the original website. If no account with that email address exists yet, one is created. So, where is the problem?

The issue arises when the main website does not force email verification of the user before redirecting him to the shopify store.

Breaking the Logic:

Imagine the following situation, a website that has a separate shopify store on a different subdomain. The victim goes directly to the shop to order some items and checks-out using his e-mail. Since shopify stores save this separately from the main website, a new record with the user’s information, credit card, email, etc… is created on the shopify store (even if he chose to check-out as a guest) and the user didn’t even visit the main website.
Now the attacker can go to the main website, create an account with the user’s email, doesn’t need verification to be logged in, and gets redirected to the shopify store. Remember the shopify feature? it now turned into a vulnerability as the attacker is logged in to the shopify store with the same email as the user so he has access to his previous orders, PII, CC Info, etc..

Get Ahmed A. Sherif (Batee5a)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to Reproduce:

First of all, you need to make sure that the shopify store of the website is on a different sub-domain from the original website (or atleast the checkout page)
You also need to validate that the website does not require email verification for registering new emails and can log you in instantly after registering.
After validating the previous two steps, it is straightforward. You make a purchase as a guest using the victim email, then from an incognito session register a new account on the main website using the same email and get redirected to the shopify store belonging to that website. You should see all the data of the purchase.

FAQ:

Q. How did I find this vulnerability?
A. By reading the shopify multipass documentation, the description of the vulnerability is present in the last couple of lines. I recommend you read the documentations of third party applications that websites use as they may be of great help in understanding the application logic and spotting out misconfigurations.

https://shopify.dev/docs/admin-api/rest/reference/plus/multipass

You should make sure that registering new accounts at your main website requires validation of the email address which is used. Otherwise, someone could sign up to your main site using somebody else’s email address, thus getting access to his customer account in your Shopify store.

Q. If I find this vulnerability, will It be considered a Critical one?
A. Not necessarily as it depends on the program it self. I have reported this vulnerability 4 times so far, 2 got accepted as Critical, whilst 1 was accepted as High and one was accepted as Medium. It needs extensive pre-requisites as the victim needs to have made atleast one purchase as a guest and you need to know his email so thats why some programs may lower its severity.

Q. Can I easily find this vulnerability?
A. No, it is not abundant but it does exist and not a lot of people know about it but I have found it on OLD, LARGE, PUBLIC bug bounty programs, the ones you think you wouldn’t find anything in them and you just ignore them so I would say you have a pretty good chance at finding this in other private ones.

That’s it for this article, If you have any questions don’t hesitate to contact me through
https://twitter.com/Ahmed_ASherif

See you in a new one!

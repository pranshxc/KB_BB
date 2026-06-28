---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-07_what-if-you-could-deposit-money-into-your-betting-account-for-free-oh-wait-where.md
original_filename: 2021-04-07_what-if-you-could-deposit-money-into-your-betting-account-for-free-oh-wait-where.md
title: What if you could deposit money into your Betting account for free? Oh wait
  where has this 25k came from…
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 513e0729e52e45502756ad9f59a28db3c038da9cbb01584429f7de11ac714319
text_sha256: f05cf18a8a1055849a38b18338174fa9c22adb37f90580783b6fd8f318f96355
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# What if you could deposit money into your Betting account for free? Oh wait where has this 25k came from…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-07_what-if-you-could-deposit-money-into-your-betting-account-for-free-oh-wait-where.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `513e0729e52e45502756ad9f59a28db3c038da9cbb01584429f7de11ac714319`
- Text SHA256: `f05cf18a8a1055849a38b18338174fa9c22adb37f90580783b6fd8f318f96355`


## Content

---
title: "What if you could deposit money into your Betting account for free? Oh wait where has this 25k came from…"
url: "https://mikey96.medium.com/what-if-you-could-deposit-money-into-your-betting-account-for-free-24f6690aff46"
authors: ["Mikey (@mikey96_bh)"]
bugs: ["Logic flaw"]
bounty: "10,000"
publication_date: "2021-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3754
scraped_via: "browseros"
---

# What if you could deposit money into your Betting account for free? Oh wait where has this 25k came from…

What if you could deposit money into your Betting account for free?
Mikey
Follow
6 min read
·
Apr 6, 2021

377

1

I have always been interested in payment systems since I had to implement my very first PayPal IPN around about 4 years ago. IPN’s are generally how the payments are communicated and processed between the payment company and vendor site. The general flow of an IPN is as follows:

Press enter or click to view image in full size
General overview of the IPN process.

I was fascinated at how the data was transferred between PayPal and the vendor, then finally how this was processed as a valid transaction. A friend (@SecureFocus on Twitter) and I had originally found a vulnerability in a small number of online games, where the IPN they all used did not register the unique PayPal transaction ID in their database. This meant if you could capture the request PayPal was sending to the server, you could relay it an infinite number of times and get the in-game rewards over and over again. Although this was a very basic attack and only involved changing the “statusUrl” parameter to a server we controlled, it was really the start of a nice journey that led to some critical bounties for me from two of the biggest online gambling companies in the UK.

The most important concept in this research was the relay attack, I set out to identify other payment systems where I could manipulate the statusUrl address to a server that I owned. I found out that it is pretty common for default configurations of payment systems to use a HTML form with a GET/POST request to submit the data to the payment provider, in order to generate the transaction in the first place. All you simply had to do is capture the request in burp suite and edit the statusUrl parameter, which would generate a valid transaction with your server as a status URL and from there you can capture the valid transaction request from the payment provider that would usually be processed by the targeted site.

Press enter or click to view image in full size
Showing how to manipulate the status URL so you can receive the response from payment provider in this one Skrill.

The next step in this was picking a payment system that had a weakness in their protocol for the way they verified legitimate transactions. I settled on then UK based payment provider — Skrill. The weakness here was immediately obvious and I almost could not believe my eyes from what I was seeing in the API documentation, I will talk more about this later. At the time the whole validation process relied upon six different factors which were combined to make a MD5 signature. These factors are merchant_id, transaction_id, secret_word, mb_amount, mb_currency, status_code and a secret word.

Press enter or click to view image in full size
Parameters all involved in generating the MD5 signature that make up a valid transaction.

The image below shows how these parameters are combined to make the signature. Essentially in simplified terms it looks like this: MD5(merchant_id + transaction_id + MD5(secret_word).toUppercase() + mb_amount + mb_currency + status).

Press enter or click to view image in full size
How Skrill generates the MD5 signature.

This is firstly done by Skrill and is sent alongside other payment data for it to be validated by the target server. The information that is sent to the target, that I intercepted looked a lot like this:

Press enter or click to view image in full size
Data sent from Skrill for their clients to verify the transaction as legitimate.

Now you have an idea of all the information that it is possible to intercept if the statusUrl parameter is changed. You can confirm this is correct by then relaying it back to your target and the transaction should process just fine. If you are vigilant you may have noticed that all of the parameters used to make the MD5 signature are sent back in the response so they target can generate a signature to match what has been received. Matching these signatures is what ultimately confirms the transaction as legitimate. The real vulnerability lies within the secret word itself mainly due to the limitations of this being no more than 10 characters, all lowercase, 0–9 and no symbols allowed. This makes bruteforcing it a great possibility.

Press enter or click to view image in full size
The terrible limitations to a secret word that controls the full validation process…

A quick note… below is an example of how targets will generally process the information that Skrill or you an attacker sends to them. The MD5 signatures have to match in order for anything to be done with the data and therefor the transaction.

Code to show the general implementation of validating transactions via Skrill from request data.

Bruteforcing is exactly what I set out to do, I decided to write my own tool in Java that would hash the exact same way as mentioned above. I would then supply the static parameters from a valid transaction I had relayed myself. In essence the tool would iterate through a massive 50GB wordlist, hashing each word in the following format MD5(merchant_id + transaction_id + MD5([WORD-HERE]).toUppercase() + mb_amount + mb_currency + status) until it found a valid match for the MD5 signature I had intercepted. I think you can all imagine my face when I decided to try this brute-forcing on two of the UK’s biggest gambling chains and I had successfully cracked both passwords in less than 24 hours.

Get Mikey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next stage of this was to try and turn this into a valid attack scenario by creating my own “valid transactions” from thin air. This I thought would be more complex but in fact all I had to do is fill in the form for the 25,000GBP I would like to deposit and intercept the request. In this request I had all the parameters I needed to generate a valid MD5 signature: transaction_id, merchant_id, mb_amount, mb_currency and status. All that was left to do was to generate a valid MD5 signature. This was done in the same manner as above using the newly cracked secret word.

Press enter or click to view image in full size
How I generated the “fake” MD5 signature.

Finally once I had my generated a MD5 signature to match the data of the transaction I had just started, all that was left to do is send the POST request to the IPN processor on the target. I crafted my cURL request so it looked something like this: curl https://target.com/moneybookers.aspx — data “[TRANSACTION DATA HERE]” with the data looking like the image below:

Press enter or click to view image in full size
Format of the transaction data I sent to the targets, with the parameters replaced with genuine parameters for the transactions I had started on the platforms.

I then sent the cURL request and low and behold I checked my betting account and there it was 25,000GBP in my balance!

I immediately reached out to the Application Security teams of both companies after validating the vulnerability. I advised them on the best remediation steps which were: generate the transaction internally so an attacker cannot manipulate the statusUrl parameter, validate that the requests come from the Skrill servers before processing them and finally use better PASSWORDS!

The AppSec teams were very thankful that I reported this in the manner I did, I was actually told there was no way this could be detected as a fraudulent transaction. I was rewarded ~10,000$ total across the two companies and personally thanked by the head of security. I will not disclose the company names, but I way say they acted promptly and fixed the issues almost immediately.

I wish I could share more screenshots but that would totally give away the platforms this worked on and I do not want to do that! If anyone wants anymore details then please reach out to me, I am happy to discuss this with anyone. Thanks for reading!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-09_bypassing-payments-in-apple-for-free-trails-for-lifetime.md
original_filename: 2024-01-09_bypassing-payments-in-apple-for-free-trails-for-lifetime.md
title: Bypassing Payments In Apple For Free Trails For Lifetime
category: documents
detected_topics:
- otp
- automation-abuse
- command-injection
- rate-limit
- api-security
- mobile-security
tags:
- imported
- documents
- otp
- automation-abuse
- command-injection
- rate-limit
- api-security
- mobile-security
language: en
raw_sha256: f735dfe837d01bcfb5244d993ed4ea025a6a0ec92961f5af6d5ca800f790d3b4
text_sha256: 020446e03e9846f94c32069c64f5eb5f050d1d0dbca4d1bf9c363449cb705f52
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing Payments In Apple For Free Trails For Lifetime

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-09_bypassing-payments-in-apple-for-free-trails-for-lifetime.md
- Source Type: markdown
- Detected Topics: otp, automation-abuse, command-injection, rate-limit, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: True
- Raw SHA256: `f735dfe837d01bcfb5244d993ed4ea025a6a0ec92961f5af6d5ca800f790d3b4`
- Text SHA256: `020446e03e9846f94c32069c64f5eb5f050d1d0dbca4d1bf9c363449cb705f52`


## Content

---
title: "Bypassing Payments In Apple For Free Trails For Lifetime"
page_title: "BYPASSING PAYMENTS IN APPLE FOR FREE TRAILS FOR LIFETIME | by Sam | InfoSec Write-ups"
url: "https://medium.com/@sam0-0/bypassing-payments-in-apple-for-free-trails-for-lifetime-8e3019dfe57b"
authors: ["Sam (@__Sam0_0)"]
programs: ["Apple"]
bugs: ["Payment bypass"]
publication_date: "2024-01-09"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 567
scraped_via: "browseros"
---

# Bypassing Payments In Apple For Free Trails For Lifetime

BYPASSING PAYMENTS IN APPLE FOR FREE TRAILS FOR LIFETIME
Sam
Follow
5 min read
·
Jan 9, 2024

130

3

Hi, hope you guys are doing well,

So ,Lets start without wasting any time , Apple music provides free trials for every new user, But it requires to add a credit card to it and then allows a user to get free trial, Now what if we can bypass the payment verification and get unlimited trials for lifetime ?

It took me a week,but i did exactly the same ! It also results in mass account creation of apple ids without verifying or adding your phone number , we can create apple account in bulks within seconds, Which could be benifitial for spammer or few organizations!

There are total 3 requests are responsible for creating an apple account : 1-https://buy.music.apple.com:443/WebObjects/MZFinance.woa/wa/***REDACTED-SUSPECT-TOKEN***2-https://buy.music.apple.com:443/WebObjects/MZFinance.woa/wa/***REDACTED-SUSPECT-TOKEN***3-https://buy.music.apple.com:443/WebObjects/MZFinance.woa/wa/createAccountSrv

Explanation of attack flow : [creating apple id for free trial]

(Step-1): In the First request the conformation code is generated and in response for an given email, But the cookies are playing main role in this whole process, after 2 days of work, i finally understood the whole flow of account creation and identified cookies which are responsible for the oprations, So for the first cookie we need an cookie named wosid-lite , Without it we cannot genrate an verification code for an email, so after digging up more, i found one more endpoint : https://buy.music.apple.com:443/account/restricted/create/options ,Which gives us new value of wosid-lite for each request, Now as we have wosid-lite we can generate as many verification codes as we want and in response of first request we get an clientoken which we are using in next steps.

(Step-2): Now in Second request , we are verifying the code and email, but this request works only if ns-mzf-inst is present in cookies, Then after digging more in apple i found one more endpoint : https://buy.music.apple.com:443/WebObjects/MZFinance.woa/wa/validateAccountFieldsSrv , Which gives us new value of ns-mzf-inst for each new request , Now as we have clientoken, wosid-lite from First step and ns-mzf-inst, we can verify our email with verification code , and in response we will get pageuuid , which we are using in next steps.

(Step-3): In Third request, we are verifying address and other details of users , for that, we will need pageuuid, clientoken and cookies from above steps, Then there are two options for us , Add credit card or go with None,As we need free trails we have to go with card,So now to bypass apple payments system, we will need an dummy card for that i took “401658”, Then used an credit card generator from bin, and generated 200 dummy credit cards,Now, we have to fill all the address, and put state and city as new york, and we are ready to make this request to fool the apple payments by dummy cards, and put all the data in request and send it and in response we can see status:0 or xml data to verify that the account is created. (I automated all the input fields with random but valid data in automation ), After carefully adding everything we are good to create an account, But apple is protected by an ip rate limit , which is very very easy to bypass, just by rotating proxies for automation,(I am successfully able to bypass this too by using an proxy ip) and get apple accounts in mass/bulk/
Now as we added out dummy credit card successfully, we just now have to enroll any trial in any apple product just by adding cvv of fake dummy credit cards.

Steps to reproduce :
Steps are briefly explained in the explanation section, please refer to that and, because it will be very messy to write down here, if still you guys needs steps then i can provide them, connect me on my twitter
1- Run the python script and wait for output.
2- in output we will get an email ,password , cvv, now just login with that email and password , and activate any trial and add cvv, and you will get free trial with fake/dummy credit card.
We, can run the script as many time as we want , and get free one month trials on every run !

python script is here if you need it : https://github.com/SAM0-0/APPLE-PAYMENT-BYPASS/blob/main/exploit.py

POC : https://youtu.be/3WJ8F5GLzBc

Get Sam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The response from apple is that they investigated this for six months , and told me that they fixed the issue, and i also verified the issue as well, But when it came to bounty they told me that this report is not eligible for bounty, they only awards bounty for the bugs present in the list which is on their website ! Their response : “This is because the reported issue and your proof-of-concept do not demonstrate the categories listed on https://security.apple.com/bounty/categories,” they denied and refused to award a bounty !

Press enter or click to view image in full size

I even investigated it further, even after no bounty and maybe i think i found a bypass as well, but not gonna report it to apple anytime !

This issue also allowed us to create bulk account without adding phone number to an apple id which is mandatory for creating an apple id if you are not adding your credit cards, and also allowed to bypass credit card verification by adding dummy cards, and random but logical shipping addresses with it, And create free trails and accounts for unlimited time, so when trail expires we can get new account in few seconds,In some countries Apple also offers 6 months trails too, But its only useful for android and web users, to use apple services for free for the rest of the life, For apple users they can use family sharing option to get trails without removing their own apple account from their device, Users should not pay for the thing which can be available for free !😏

Time-line :

9 oct 2022 — Reported the bug

15 Mar 2023 — Fixed the bug

24 Mar 2023 — Denied for any bounty !

9 Jan 2024 — Disclosure

Follow me here for more write ups and any questions ! :)

https://twitter.com/__Sam0_0

Thanks.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-20_how-i-registered-multiple-accounts-in-privateinternetaccess-vpn-service-for-free.md
original_filename: 2019-02-20_how-i-registered-multiple-accounts-in-privateinternetaccess-vpn-service-for-free.md
title: How I Registered Multiple Accounts in PrivateInternetAccess VPN Service for
  FREE
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- mobile-security
language: en
raw_sha256: 45fd195f5b8d1607e818a849ec55d8bf12e7766282fa15532e0d4b1dee36212b
text_sha256: ef5366a11513d19195389535589cd245a307d369d5af4aa71ad2faedfbb85be4
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I Registered Multiple Accounts in PrivateInternetAccess VPN Service for FREE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-20_how-i-registered-multiple-accounts-in-privateinternetaccess-vpn-service-for-free.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `45fd195f5b8d1607e818a849ec55d8bf12e7766282fa15532e0d4b1dee36212b`
- Text SHA256: `ef5366a11513d19195389535589cd245a307d369d5af4aa71ad2faedfbb85be4`


## Content

---
title: "How I Registered Multiple Accounts in PrivateInternetAccess VPN Service for FREE"
url: "https://medium.com/@spade.com/how-i-registered-multiple-accounts-in-privateinternetaccess-vpn-service-for-free-a2068642f418"
authors: ["Spade"]
programs: ["PrivateInternetAccess VPN"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2019-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5398
scraped_via: "browseros"
---

# How I Registered Multiple Accounts in PrivateInternetAccess VPN Service for FREE

How I Registered Multiple Accounts in PrivateInternetAccess VPN Service for FREE
Ace Candelario
Follow
3 min read
·
Feb 20, 2019

114

1

Summary

PIA ( Private Internet Access ) is a personal virtual private network service. It supports multiple VPN technologies PPTP, L2Tp/ IPsec, SOCKS5 and OpenVPN. PIA’s service is not free but I found a way to register multiple accounts without crushing your bank savings — — you read it right, you can have it for FREE!

Here’s how

Tuesday morning someone whispered to my ear telling me to find a vulnerability in PIA service. It’s like the Hacker’s Spirit summoned into my body so I take a look in their Android Application. I geared myself with my hacking weapons and opened Genymotion and Burp Suite right away to tamper some vulnerable endpoints on their Android Application which is available in Google Playstore. After 2 minutes of battling in their application, I found nothing and got bored, but the hacking spirit is still pushing me to try again. I have to sacrifice my last penny in my savings — 362.00 PHP or USD 6.95 and get a registered account to PIA’s VPN service. While monitoring all the tampered data in Burp Suite, I noticed this endpoint.

POST /api/client/signup HTTP/1.1
User-Agent: privateinternetaccess.com Android Client/1.7.3.1(451)
Content-Type: application/json; charset=utf-8
Content-Length: 365
Host: www.privateinternetaccess.com
Connection: close
Accept-Encoding: gzip, deflate
{“store”:”google_play”,”client_version”:”v1.7.3.1(451)”,”receipt”:{“order_id”:”GPA.XXXX-XXXX-XXXX-XXXXX”,”token”:”<some token>”,”product_id”:”monthly_pia_2"},”email”:”<here goes the email>”,”marketing”:{}}

This request is responsible for creating accounts and the HTTP response should be your username and also your password. I sent it to Burp Repeater for further experimentation. I tried to change the email to my other dummy email and what I noticed is the password became null.

and I was like

I have guts that there’s something here. If you notice the order_id is a random number. what I did is I tried to increment the last digit number and guess what’s the response? — ***insert drum rolls!

me reaction :)

I successfully register for free and I received an invoice to my dummy email from PIA for purchasing a monthly subscription. I tried another dummy email and it registered again for free with another invoice from PIA. The subscription is just for one month. Submitted the issue to PIA security team and they reply fast within the day. Two days later, they issue a $1000 bounty for this finding with a great fix implementation.

mind blown :D

Just found this wonderful bug within 10 minutes and my USD 6.95 turns to USD 1000 within two days. Amazing isn’t? What I learned is sometimes, you need to spent your last money and expect that it will be transformed into precious gems — — worthy bug.

Get Ace Candelario’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to Reproduce

Download and Install the PrivateInternetAccess from Google Play
Register and buy Subscription then tamper the request using Burp Suite
You should encounter the vulnerable request I mentioned above
To make another account just change the email parameter and decrease the order_id or increment it. As long as it’s not existing on PIA’s database.
TIMELINE

02–12 -2019: Report Submitted

02–12 -2019: Security Team acknowledged my report

02–13 -2019: Replied to their response if they have a further question

02–14 -2019: $1000 bounty rewarded and fixed the issue.

02–16 -2019: Reward received via PayPal

02–19 -2019: Request for disclosure via blog

02–19 -2019: Confirm disclosure

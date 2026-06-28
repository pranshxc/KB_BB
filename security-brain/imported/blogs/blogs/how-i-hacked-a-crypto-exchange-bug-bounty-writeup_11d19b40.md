---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-07_how-i-hacked-a-crypto-exchange-bug-bounty-writeup.md
original_filename: 2018-08-07_how-i-hacked-a-crypto-exchange-bug-bounty-writeup.md
title: How I hacked a Crypto Exchange (Bug Bounty Writeup)
category: blogs
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- mfa
- otp
tags:
- imported
- blogs
- idor
- access-control
- command-injection
- password-reset
- mfa
- otp
language: en
raw_sha256: 11d19b40c8aed980677fe0de1fba27d2c66ed47075ec506e73300cf2d9ea6701
text_sha256: b7a588d9465633cc0c629c3109ae02f9f351dd2a0b55649a43b268297aa335ff
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked a Crypto Exchange (Bug Bounty Writeup)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-07_how-i-hacked-a-crypto-exchange-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, mfa, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `11d19b40c8aed980677fe0de1fba27d2c66ed47075ec506e73300cf2d9ea6701`
- Text SHA256: `b7a588d9465633cc0c629c3109ae02f9f351dd2a0b55649a43b268297aa335ff`


## Content

---
title: "How I hacked a Crypto Exchange (Bug Bounty Writeup)"
page_title: "How I hacked a Crypto Exchange (Bug Bounty Writeup) — Steemit"
url: "https://steemit.com/cryptocurrency/@mabdullah22/how-i-hacked-a-crypto-exchange-bug-bounty-writeup"
final_url: "https://steemit.com/cryptocurrency/@mabdullah22/how-i-hacked-a-crypto-exchange-bug-bounty-writeup"
authors: ["Muhammad Abdullah"]
bugs: ["IDOR"]
publication_date: "2018-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5765
---

# How I hacked a Crypto Exchange (Bug Bounty Writeup)

**[mabdullah22 (25)](/@mabdullah22)**in [#cryptocurrency](/created/cryptocurrency) • 8 years ago (edited)

Hi  
This is my first write-up on Steem and also a Info-Sec writeup after a long time. The story starts when My 6th semester ended and I got some time to hunt. In summer break you have HELL of a time. So I was looking to hunt some website, tied of Duplicates on Hackerone. I came across a Crypto Exchange while surfing google.I won’t be taking the Exchange name here let's say it as xyz.exchange.

So I signed up for the exchange and started testing it. The exchange was highly vulnerable, I was surprised to see that an exchange having volume in thousand of BTC is vulnerable to these type of Vulnerabilities.

The bug which helped me to hack the whole exchange was IDOR.

# Description:

Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability, attackers can bypass authorization and access resources in the system directly, for example, database records or files.  
Insecure Direct Object References allow attackers to bypass authorization and access resources directly by modifying the value of a parameter used to directly point to an object. Such resources can be database entries belonging to other users, files in the system, and more. This is caused by the fact that the application takes user-supplied input and uses it to retrieve an object without performing sufficient authorization checks.

Reference: <https://www.owasp.org/index.php/Top_10_2010-A4-Insecure_Direct_Object_References>

# Testing + Exploitation :

IDOR!! I love IDORs , especially when they are in Password Reset functionality.

This attack basically consists of two vulnerabilities.

IDOR in Password Reset + 2fa bypass

## IDOR in Password Reset Functionality:

When I Requested a password reset link I got something like below

<http://xyz.exchange/#/reset_password/cet6YhGBFVD89jnuOiVMwfdr4mcsaeEwk2OimSc0LtVg>

I thought that the exchange is using some kind of token implementation here. But I was wrong when I intercepted my Request in Burp. It was a simple POST request being made at /api/reset_password

[![reset request.PNG](https://steemitimages.com/p/3jpR3paJ37V8JxyWvtbhvcm5k3roJwHBR4WTALx7XaoRovtrc72Z4Hqz4Dsr6dwAk3JJ9pt3TzkftKDVz9bhHyHrZXQd2Fx3MeNyJCorNDzUfeBfqiN8X2DTgvVkRk5UBoEri?mode=fit&format=match&width=640)](https://steemitimages.com/p/3jpR3paJ37V8JxyWvtbhvcm5k3roJwHBR4WTALx7XaoRovtrc72Z4Hqz4Dsr6dwAk3JJ9pt3TzkftKDVz9bhHyHrZXQd2Fx3MeNyJCorNDzUfeBfqiN8X2DTgvVkRk5UBoEri?mode=fit&format=match&width=640 "This image will open in a new tab")

This request had an id parameter. Every user is assigned an id in the system. The id was incrementing id. From a Hacker perspective, I first thing that came into my mind was what happens if I change this id. And to my surprise, it was vulnerable to IDOR.  
I made two accounts and tested it and it WORKED!!!

I was like…

[![Minionshappyyay.gif](https://steemitimages.com/p/3jpR3paJ37V8JxyWvtbhvcm5k3roJwHBR4WTALx7XaoRovtz2Q5hogzxZS5ZisjyWhwUse5KqmsLjbqpAYXTucfkWBUw31a3mSubNEc8NR7iNPYdG5vvHpsKJyNf3zRiGv9z5?mode=fit&format=match)](https://steemitimages.com/p/3jpR3paJ37V8JxyWvtbhvcm5k3roJwHBR4WTALx7XaoRovtz2Q5hogzxZS5ZisjyWhwUse5KqmsLjbqpAYXTucfkWBUw31a3mSubNEc8NR7iNPYdG5vvHpsKJyNf3zRiGv9z5?mode=fit&format=match "This image will open in a new tab")

Now comes the second part. Taking over the full account is not possible without correct 2fa token as its required upon login.

For confirming the 2fa token the following request was being made.

[![2fa request.PNG](https://steemitimages.com/p/99pyU5Ga1kwqSXWA2evTexn6YzPHotJF8R85JZsErvtTWYpQm6GMMabZiA1A3FTood4PNkpnZ7TEu5zTrRRAymtxhRU96wqgFyxjRkSd6eJvgvujp6CEpLHkiYXPWuGbFU?mode=fit&format=match&width=640)](https://steemitimages.com/p/99pyU5Ga1kwqSXWA2evTexn6YzPHotJF8R85JZsErvtTWYpQm6GMMabZiA1A3FTood4PNkpnZ7TEu5zTrRRAymtxhRU96wqgFyxjRkSd6eJvgvujp6CEpLHkiYXPWuGbFU?mode=fit&format=match&width=640 "This image will open in a new tab")

Code as the 2fa token. I set the burp to show its response. The response was as follows.

[![2fa response.PNG](https://steemitimages.com/p/cyxkEVqiiLy2ofdgrJNxeZC3WCHPBwR7MjUDzY4kBNr81LuwfR8WtmAUi7VcBZebD7WnaZdK7wMHBvxByskvgJyhKMTiQgwqtJcc7LtVjU6XdPsRc6h2k13BxZsSnw9i6UE?mode=fit&format=match&width=640)](https://steemitimages.com/p/cyxkEVqiiLy2ofdgrJNxeZC3WCHPBwR7MjUDzY4kBNr81LuwfR8WtmAUi7VcBZebD7WnaZdK7wMHBvxByskvgJyhKMTiQgwqtJcc7LtVjU6XdPsRc6h2k13BxZsSnw9i6UE?mode=fit&format=match&width=640 "This image will open in a new tab")

So the trick was to just set the response to true as you will get access to the account even token as “123456”.

Later I found the Admin’s Email and his corresponding account Id via using IDOR in their Ticket System. But I didn’t exploited it as COO didn’t give me the permission.

# Take Aways:

~ Burp is your Ultimate Friend Always keep it on and Look at every Request being Made.  
~ Never Forget to Play With Request Responses.

# Time-line:

Getting this bug to Authorities was another story Which I will share some other time.

June. 16, 2018 → Initial Report Sent  
NO RESPONSE  
June. 30, 2018 → Mail for Update  
NO RESPONSE  
July. 6, 2018 → Reported Via Telegram group of Exchange  
July. 6, 2018 → Triaged  
July. 7, 2018 → Fixed  
July. 7, 2018 → Bounty awarded

[ #exchange ](/trending/exchange)[ #security ](/trending/security)[ #infosec ](/trending/infosec)[ #bugbounty ](/trending/bugbounty)

8 years ago in [#cryptocurrency](/created/cryptocurrency) by **[mabdullah22 (25)](/@mabdullah22)**

$0.09

  * Past Payouts $0.09
  * \- Author $0.07
  * \- Curators $0.02

11 votes

  * [\+ moneyguruu](/@moneyguruu)
  * [\+ payelmia](/@payelmia)
  * [\+ scimyworld](/@scimyworld)
  * [\+ steemek](/@steemek)
  * [\+ kellancoin](/@kellancoin)
  * [\+ ambika138](/@ambika138)
  * [\+ akhileshbhai](/@akhileshbhai)
  * [\+ sujon123](/@sujon123)
  * [\+ gaboski](/@gaboski)
  * [\+ dion66](/@dion66)
  * [\+ kate-nakamoto](/@kate-nakamoto)

Reply [2](/cryptocurrency/@mabdullah22/how-i-hacked-a-crypto-exchange-bug-bounty-writeup "2 Responses")

  *  *  *  *

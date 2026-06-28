---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-20_oauth-misconfiguration-found-in-small-time-window-of-attack.md
original_filename: 2021-03-20_oauth-misconfiguration-found-in-small-time-window-of-attack.md
title: OAuth Misconfiguration found in small time-window of attack
category: documents
detected_topics:
- oauth
- command-injection
tags:
- imported
- documents
- oauth
- command-injection
language: en
raw_sha256: 0f35027d0ae8447df507ced8f0afd12e777ed3705ba19df8aa9683b35973fd2a
text_sha256: 593349416ff741885f78fca618b57bb0ffed824b8ea84a6d970e050ddb0120dd
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# OAuth Misconfiguration found in small time-window of attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-20_oauth-misconfiguration-found-in-small-time-window-of-attack.md
- Source Type: markdown
- Detected Topics: oauth, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `0f35027d0ae8447df507ced8f0afd12e777ed3705ba19df8aa9683b35973fd2a`
- Text SHA256: `593349416ff741885f78fca618b57bb0ffed824b8ea84a6d970e050ddb0120dd`


## Content

---
title: "OAuth Misconfiguration found in small time-window of attack"
url: "https://muhammad-aamir.medium.com/oauth-misconfiguration-found-in-small-time-window-of-attack-b585afcb94c6"
authors: ["Muhammad Aamir (@Muhammad__Aamir)"]
bugs: ["OAuth"]
bounty: "300"
publication_date: "2021-03-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3801
scraped_via: "browseros"
---

# OAuth Misconfiguration found in small time-window of attack

OAuth Misconfiguration found in small time-window of attack
Muhammad Aamir
Follow
3 min read
·
Mar 20, 2021

241

1

Hi Everyone,

I am Muhammad Aamir, a cybersecurity professional from Pakistan. Here I share with you an OAuth misconfiguration vulnerability found in small time-window of attack. The program is on Bugcrowd and I was rewarded with $300 for this find. I reported it in the last month of 2020 and got acceptance & bounty in the same month.

The program has a domain in scope which offers login either via email (domain’s own account management after Sign up process) or Facebook credentials. I decided to login via my Facebook account and got in easily as expected. For successful login, the application server follows OAuth flow of authentication where the Facebook server would return an access code for login if the credentials are right. The access request to application server takes the following form:

https://redacted.com/login?id=xxx&code=x-xxxxxx-xxxxxxxxx-xxxxxxxxxxxxxx

If I would logout from the application but not from the Facebook account, it is normal that I could again login to the application just by a single click because I’m already logged in with Facebook on the same browser. However, if I logout from the application as well as from the Facebook account, the application would again ask for Facebook credentials to allow me the account’s access. In fact, it would again follow OAuth flow of authentication where the Facebook server would return a new access code for login if the credentials are right again.

What I did initially was that I logged out from the application as well as from the Facebook account. Then on the application’s interface, I clicked on “Login with Facebook” and got into my account even though I was not currently logged in on Facebook. I got a little suspicion at that time so I logged out from the application again and quickly changed my Facebook account’s password to ensure that my previous password should not be able to give me the Facebook account’s access if it still resides somewhere in the application’s or browser’s memory. Once again on the application’s interface, I clicked on “Login with Facebook” and got into my account this time as well. Hmmm … Finally, I took the HTTP request which contained the access code and applied that on a fresh browser. Bingo! I got into my account yet again.

Get Muhammad Aamir’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It pushed me to report the behavior as it was pointing out to a vulnerability. I had later some discussions with the program while they were boiling down the existence of this issue. Finally, they mentioned that they were in fact allowing it in a way that within a time-window of 5 minutes after receiving a valid code, their server doesn’t go back to Facebook if the access is requested again. For a particular login id, they use the same access code that had been received earlier.

It means that if I had once got a valid access code, then within the small time-window, the server continued using the same code even if I made fresh requests of login to the application via Facebook. It didn’t go back to Facebook for a new access code irrespective of the actions taken on the Facebook account such as logging out from Facebook or even changing the password of Facebook account. Therefore, within the small time-window of 5 minutes, the access of account was possible with expired credentials of Facebook (knowing the access code) that had been recently used to get the code.

The program was not ready to change this behavior initially. But later on, they realized the impact of this vulnerability as it could be used for replay attacks to get unauthorized access of account by hackers in the small time-window of attack. Since the window of attack was short (5 minutes only) and some conditions also existed for a successful replay attack, the program kept it in low severity (P4 in Bugcrowd) but rewarded me with $300 which is a bit higher than their reward range of P4 findings.

Press enter or click to view image in full size
Request prone to the replay attack

I hope you’ve enjoyed reading it :) Thank you.

Stay Safe Everyone!

Twitter: @Muhammad__Aamir

LinkedIn: https://www.linkedin.com/in/muhammad-aamir-457932150

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-12_csrf-with-idor-a-deadly-combo.md
original_filename: 2021-01-12_csrf-with-idor-a-deadly-combo.md
title: CSRF with IDOR - A Deadly Combo
category: documents
detected_topics:
- idor
- csrf
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- idor
- csrf
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 94d1d14d030b530e2654501cc9db106806983445cfea8b559f66cadb8f95a31e
text_sha256: 093d797782ac4744d39e057d361c7a255ae1310ad14d74de6bc3556aaef627f9
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF with IDOR - A Deadly Combo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-12_csrf-with-idor-a-deadly-combo.md
- Source Type: markdown
- Detected Topics: idor, csrf, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `94d1d14d030b530e2654501cc9db106806983445cfea8b559f66cadb8f95a31e`
- Text SHA256: `093d797782ac4744d39e057d361c7a255ae1310ad14d74de6bc3556aaef627f9`


## Content

---
title: "CSRF with IDOR - A Deadly Combo"
url: "https://shahjerry33.medium.com/csrf-with-idor-a-deadly-combo-203e93967702"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["CSRF", "IDOR"]
publication_date: "2021-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4005
scraped_via: "browseros"
---

# CSRF with IDOR - A Deadly Combo

CSRF with IDOR - A Deadly Combo
Jerry Shah (Jerry)
Follow
4 min read
·
Jan 12, 2021

630

2

Press enter or click to view image in full size

Summary :

I was invited on a private program on HackerOne and there were so many domains in scope so I thought of testing some of them. In one of the domain I found this vulnerability which is Cross Site Request Forgery, when combined with Insecure Direct Object Reference was able to delete anyone’s account.

I was searching for different vulnerabilities on that domain and I saw that there are two different types of account you can register yourself with :

Open Source Account
Trial Account

In trial account you get the trial of 29 days and you also have the option to cancel it, so I thought of trying Insecure Direct Object Reference attack first but it didn't work so moving on with CSRF it was successful but with the help of IDOR.

When I registered myself using trial account there was an option of “Cancel Enterprise”, now when you click this option the account will be deleted automatically. In the request I found there were 2 parameters googleAnalyticsId=<Value>&mktToken=<Value>, but when I captured the request of the another account in the private browser there were only parameters with no value passed for eg. (googleAnalyticsId=&mktToken=), so I thought it might be vulnerable to CSRF attack but the GET request was having the username of the account GET /userName1/account/cancelTrial/?&googleAnalyticsId=&mktToken= so I thought of crafting a CSRF request by changing the username GET /userName2/account/cancelTrial/?&googleAnalyticsId=&mktToken= but still something was left so I quickly checked the referrer header which was Referrer: https://example.com/userName1/account/account so I changed the referrer header to Referer: https://example.com/userName2/account/account in my CSRF attack and the attack was successful.

What is CSRF ?

Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.

What is IDOR ?

Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly.

How I found this vulnerability ?

I went to https://example.com from two different browsers (normal & private)
Then I created trial accounts on both the browsers
I verified the links and went to my dashboard
I then visited https://example.com/<userName2>/account/ account link from the second account (second browser), and here I found an option of Cancel Enterprise (trial) account
Press enter or click to view image in full size
Account1
Press enter or click to view image in full size
Account2
Press enter or click to view image in full size
Account Deletion

5. Then I clicked on the button and captured the request using burp suite

Press enter or click to view image in full size
cancelTrial/Deletion Request

Here you can see I have removed the value of googleAnalyticsId=&mktToken= parameters.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. Then I changed the username to username in first browser and in the GET request URL and Referrer header and crafted the CSRF PoC

Press enter or click to view image in full size
Changing Values

7. Then I generated a CSRF poc and saved it as .html

Press enter or click to view image in full size
CSRF PoC
Press enter or click to view image in full size
PoC - (Proof-Of-Concept)

8. I ran it and reloaded the page in the first browser account and the account got deleted

Press enter or click to view image in full size
Running PoC
Press enter or click to view image in full size
Account Deleted

Here the email ID of the target account was sovovem334@yektara.com (Temp Mail)

Press enter or click to view image in full size
Email Of Target Account

For the better understanding of the vulnerability I compared the request of both the accounts (account1 & account2) which were open on two different browsers (Firefox & Firefox Private). I compared the request using “Comparer” module of BurpSuite.

Press enter or click to view image in full size
Comparer

NOTE : Here pentesterworld is the attacker’s account and defendingera is the victim’s account.

Mitigation :

A proper CSRF token should be added in a request and should be validated on client as well as server side.

Press enter or click to view image in full size

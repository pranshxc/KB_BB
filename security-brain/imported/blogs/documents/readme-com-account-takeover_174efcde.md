---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-05_readmecom-account-takeover.md
original_filename: 2019-09-05_readmecom-account-takeover.md
title: Readme.com Account Takeover
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 174efcde993be16cdf313bf45b828341ebd1dbd58cbf5d342c349b61746fcb32
text_sha256: 6ec328c7e00f023cf9c4ec503696cd6516ae488e87ee1fd2a4d959ae16a4106e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Readme.com Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-05_readmecom-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `174efcde993be16cdf313bf45b828341ebd1dbd58cbf5d342c349b61746fcb32`
- Text SHA256: `6ec328c7e00f023cf9c4ec503696cd6516ae488e87ee1fd2a4d959ae16a4106e`


## Content

---
title: "Readme.com Account Takeover"
url: "https://medium.com/@0xankush/readme-com-account-takeover-bugbounty-fulldisclosure-a36ddbe915be"
authors: ["Ankush Goel (@0xankush)"]
programs: ["Readme.com"]
bugs: ["Password reset"]
publication_date: "2019-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5049
scraped_via: "browseros"
---

# Readme.com Account Takeover

Ankush Goel
 highlighted

Readme.com Account Takeover #BugBounty #FullDisclosure #Fixed
Ankush Goel
Follow
3 min read
·
Sep 5, 2019

442

4

Hi Everyone,

In this blog post, i will talk about how i was able to compromise user accounts using HTTP parameter pollution vulnerability in the password reset page of a popular company. Below is a description about the vulnerability.

HTTP Parameter Pollution, as implied by the name, pollutes the HTTP parameters of a web application in order to perform or achieve a specific malicious task/attack different from the intended behavior of the web application.

Alert: Full Disclosure: I will be disclosing the details of the company as the company didn’t follow the responsible disclosure guidelines. I didn’t receive any response from the company regarding this vulnerability even after reporting them via multiple channels such as twitter, Facebook, LinkedIn, and Email. They also have a public Bug Bounty Program.

So the company is ReadMe. They just received $9 Million in funding recently. Read Here. ReadMe helps companies create and manage their documentation(including API documentation) all in one place. Big companies such as Coinbase, Microsoft, IBM, Mozilla, Trello etc are their clients. See full list here.

So here goes the details…..

After finding out about there bug bounty program from my friend, i started doing recon the website. After just creating account on the website dash.readme.io i started browsing it just like a normal user would do to understand the flow of the website.

Next, i tried to understand their password reset mechanism. They would just send a unique link to my email address for password reset such as this https://dash.readme.io/reset/l2s6ugXXXXXXXXXXXXXVAzLDMeVWXXX. Its a unique and tied to the particular email address. I tried resetting other accounts password but the token was tied to the email who requested the password.

Below are the details of the post request for the password reset. This will send a unique link to the email.

Press enter or click to view image in full size
burp request — password reset

Here is the request that was modified to get reset link. By just adding another email parameter to the request with the attacker email address, you can get the password email for the victim. Both email addresses with receive the password reset link and the link is only valid for 20 mins.

Press enter or click to view image in full size
Modified Request

Basically, the logic in the website creates a reset link for the first email address but send the link to both email addresses mentioned in the request. Now you can reset the account password for the victim email address.

BOOM!!!. ACCOUNT TAKEOVER

Get Ankush Goel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps:

Go to https://dash.readme.io/forgot/
Start Burp Proxy and start intercepting requests
Enter the email address of the victim on the website and click submit
intercept request on burp and add another email parameter with the attacker’s email address and forward the request
Now you will receive the email from readme regarding account password reset.

IMPACT: High!! at least for the customers :)

Readme customers page provides a good list of targets. You can collect a list of email addresses for a target company and send that through burp intruder. If any of those emails have readme account, you will receive the account password reset link for that account. Reset the password and access the account. Now you can modify the documentation and insert malicious links or misdirect users. The possibilites are endless.

#Disclosure Timeline!!!!

07.30.2019: Notified the company about the bug with all the details via email. No Response.

08.02.2019: Contacted with their support via chat. No response.

08.04.2019: Contacted via twitter, LinkedIn and Facebook. No response.

09.05.2019: Still no response from the company…..

Full Disclosure

10.04.2019: Received response from the company acknowledging the bug. The company fixed the bug. Waiting on the bounty …. :)

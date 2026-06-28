---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-24_http-parameter-pollution-its-contaminated.md
original_filename: 2020-07-24_http-parameter-pollution-its-contaminated.md
title: HTTP Parameter Pollution - It’s Contaminated
category: documents
detected_topics:
- command-injection
- mfa
- otp
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- otp
- api-security
language: en
raw_sha256: d412aafdfc151c276947248410e79a84dca803d9fb5e1c2ec192eda3ecf00997
text_sha256: f03432e30112c36b8a1dbbe0d729bceddba9ba6b075ea6a67069c1f2da3cfbb4
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP Parameter Pollution - It’s Contaminated

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-24_http-parameter-pollution-its-contaminated.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `d412aafdfc151c276947248410e79a84dca803d9fb5e1c2ec192eda3ecf00997`
- Text SHA256: `f03432e30112c36b8a1dbbe0d729bceddba9ba6b075ea6a67069c1f2da3cfbb4`


## Content

---
title: "HTTP Parameter Pollution - It’s Contaminated"
url: "https://medium.com/@shahjerry33/http-parameter-pollution-its-contaminated-85edc0805654"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["HTTP parameter pollution"]
publication_date: "2020-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4390
scraped_via: "browseros"
---

# HTTP Parameter Pollution - It’s Contaminated

HTTP Parameter Pollution - It’s Contaminated
Jerry Shah (Jerry)
Follow
3 min read
·
Jul 24, 2020

403

3

Press enter or click to view image in full size

Summary :

HTTP Parameter Pollution (HPP) means to pollute the HTTP parameters of a web application for achieving a specific malicious task. It refers to manipulating how a website treats parameters it receives during HTTP requests. It changes a website’s behaviour from its intended one. HTTP
parameter pollution is a simple kind of attack but it is an effective one.

When you pollute any parameter the code runs only on the server-side which is invisible to use, but we can see the results on our screen. The process in between is a black box.

For example, there is a URL https://www.anybank.com/send which has three parameters :

from :
to :
amount :

URL : https://www.anybank.com/send/?from=accountA&to=accountB&amount=10000

Now this is a normal URL which will proceed a transaction of 10000 from accountA to accountB but what if we add another same parameter “from :”

So the URL will be like https://www.anybank.com/send/?from=accountA&to=accountB&amount=10000&from=accountC

When this URL will be proceed a transaction of 10000 it will be deducted from accountC rather than accountA. This is how you manipulate the parameters in HTTP Parameter Pollution attack. Although the scope of this vulnerability is not limited only to GET request you can also perform this attack on a POST based request. You can try this vulnerability on many places like password change, 2FA, comments, profile photo upload, on a parameter where API key is passed, OTP etc.

When you manipulate any parameter, it’s manipulation depends on how each web technology is parsing their parameters. You can identify web technologies using “Wappalyzer”. Below is the screenshot of some technologies and their parameter parsing.

Press enter or click to view image in full size
Technologies and their parameter parsing

I would like to share one of my finding of HPP where I was able to take over an account using this vulnerability.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I find this vulnerability ?

I went to a login page of that program, it asked for an OTP for login
Send OTP

2. I typed an email and clicked on “Send One Time Password”

3. I intercepted the request using burp suite and added another email by using same parameter (I created two emails for testing purpose)

Press enter or click to view image in full size
Burp Request

4. I received an OTP of shrey……@gmail.com to my another account radhika…..@gmail.com

OTP

5. I copied the OTP and went to shrey….@gmail.com on that program’s login screen, I entered this OTP and I was in the account.

Press enter or click to view image in full size
Account Take Over

So what happened here is the back-end application took the value of first “email” parameter to generate an OTP and used the value of second “email” parameter to supply the value, which means an OTP of shrey….@gmail.com was sent to radhika….@gmail.com.

NOTE : Here in an image on 4th step where I received an OTP to radhika….@gmail.com I was confused because the message said Hi Radhika, so I thought that the parameter is not polluted and the OTP was for radhika….@gmail.com but when I tried the OTP on shrey….@gmail.com it worked.

Mitigation :

A proper input validation should be performed in order to prevent this kind of attacks.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-10_how-i-was-able-to-bypass-philips-authentication.md
original_filename: 2022-09-10_how-i-was-able-to-bypass-philips-authentication.md
title: How I was able to Bypass Philips Authentication
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: b84bc6b5f12f6383fb8c0a60f02921f0dbe270cefecec5f69e025ec1dd30fe78
text_sha256: a5aaa0d24f9474f06d304851bfba74b66c4ec20d77ce2ef776a8bafdcd5515b9
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: true
---

# How I was able to Bypass Philips Authentication

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-10_how-i-was-able-to-bypass-philips-authentication.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: True
- Raw SHA256: `b84bc6b5f12f6383fb8c0a60f02921f0dbe270cefecec5f69e025ec1dd30fe78`
- Text SHA256: `a5aaa0d24f9474f06d304851bfba74b66c4ec20d77ce2ef776a8bafdcd5515b9`


## Content

---
title: "How I was able to Bypass Philips Authentication"
page_title: "How I was able to Bypass Famous Company Authentication | by ParagBagul | Medium"
url: "https://medium.com/@Parag_Bagul/how-i-was-able-to-bypass-philips-authentication-c3bd3e1df9ff"
authors: ["ParagBagul"]
programs: ["Philips"]
bugs: ["Outdated component with a known vulnerability", "Authentication bypass"]
publication_date: "2022-09-10"
added_date: "2022-09-19"
source: "pentester.land/writeups.json"
original_index: 2183
scraped_via: "browseros"
---

# How I was able to Bypass Philips Authentication

How I was able to Bypass Famous Company Authentication
ParagBagul
Follow
3 min read
·
Sep 10, 2022

31

1

This article is based on a new finding in which I discovered the nacos authentication bypass vulnerability on Philips website which leads to full nacos dashboard access.

during my information gathering phase, I found the subdomain https://idpuat.philips.com.cn/nacos

after that open URL. there was a panel of nacos service.

Press enter or click to view image in full size
nacos login panel

I decided let’s try default credentials but fail 😞 I started researching about nacos service. this is that kind of phase before hacking anything you need to learn about it. and you need research for that

#what is nacos?

nacos is an easy-to-use platform designed for dynamic service discovery and configuration and service management? It helps you to build cloud-native applications and microservices platforms easily.

I started looking for vulnerabilities of nacos. the search result was very interesting

Press enter or click to view image in full size
nacos exploit search

in search, I found that nacos version 1.4.1 has an authentication bypass. At that time I didn’t have any idea. which version of nacos using.after that, I started to research on cve-2021–29441

#what is cve-2021–29441?

This vulnerability allows an attacker to access the user list interface and add a new user. Nacos uses the AuthFilter servlet filter to enforce authentication. This filter has a backdoor that enables Nacos servers to bypass this filter and therefore skip authentication checks.

#Impact:critical

#Actual Exploitation:

for exploitation, I started a burp suite and intercept the below URL

https://idpuat.philips.com.cn/nacos/v1/auth/users/?pageNo=1&pageSize=9

Press enter or click to view image in full size
intercepted request

after intercepting the request I quickly sent that request to the burp suite repeater. in response, the website leaked the username and password that exist on the website.

Press enter or click to view image in full size
username and password leak

you can also do the same thing with curl.

Get ParagBagul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

curl XGET ‘http://vulnerablewebsite.com/nacos/v1/auth/users/?pageNo=1&pageSize=9 — path-as-is’

boom listed nacos users. this vulnerability also allows attackers to create a new user. after that, I created the user with below command below command.

Press enter or click to view image in full size
user created

you can also create a user with curl use the below command:-

curl -XPOST ‘http://vulnerablewebsite.com/nacos/v1/auth/users/?username=test&password=***REDACTED*** — path-as-is’

instead of username test you can add any username you want to add. same for password also.

curl -XPOST ‘http://vulnerablewebsite.com/nacos/v1/auth/users/?username=test&password=***REDACTED*** — path-as-is’

boom user created that I was thinking about can we log in with this user?

the answer is yes we can I opened the below URL.

https://idpuat.philips.com.cn/nacos

and using the username and password demo for login. yes now full we have full nacos admin access.

Press enter or click to view image in full size
nacos admin dashboard

I quickly made a report of this vulnerability and reported this vulnerability to Philips’s security team. and after fixing the security vulnerability

video proof of concept:

https://youtu.be/tD033vhLLlQ

Guess what guys after some days they add me on their HALL OF FAME

Press enter or click to view image in full size
Philips hall of fame

Thank you,

Parag Bagul!!

HaxWizard

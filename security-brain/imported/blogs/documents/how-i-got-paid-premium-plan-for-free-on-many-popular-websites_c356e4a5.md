---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-13_how-i-got-paid-premium-plan-for-free-on-many-popular-websites.md
original_filename: 2018-06-13_how-i-got-paid-premium-plan-for-free-on-many-popular-websites.md
title: How I got paid premium plan for free on many popular websites
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- csrf
- business-logic
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- csrf
- business-logic
language: en
raw_sha256: c356e4a546e0b6566e59e5b62170cc9c07af1cf2daa5ab51cdf094f935eae7c4
text_sha256: 0829b1dad03d6b81d2d819d3841a80c57075602d5b0d46089c48c4530ab43fb0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I got paid premium plan for free on many popular websites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-13_how-i-got-paid-premium-plan-for-free-on-many-popular-websites.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, csrf, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c356e4a546e0b6566e59e5b62170cc9c07af1cf2daa5ab51cdf094f935eae7c4`
- Text SHA256: `0829b1dad03d6b81d2d819d3841a80c57075602d5b0d46089c48c4530ab43fb0`


## Content

---
title: "How I got paid premium plan for free on many popular websites"
url: "https://medium.com/@khaled.hassan/how-i-got-paid-premium-plan-for-free-on-many-popular-websites-90e62a52416a"
authors: ["Khaled Hassan"]
bugs: ["Logic flaw"]
publication_date: "2018-06-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5841
scraped_via: "browseros"
---

# How I got paid premium plan for free on many popular websites

Top highlight

How I got paid premium plan for free on many popular websites
Khaled Hassan
Follow
4 min read
·
Jun 14, 2018

321

2

Hi,

I’m going to talk again about a common vulnerability that affects many applications, as not a lot of us can notice it, so I hope you like this writeup.

One of the most important recon steps to me is reading the website products, blogs, support portal, engineering blog, etc. So what caught my attention is some popular websites offers paid premium plan to students for free, and maybe with a little bit of search you’ll find dozens of websites that offer this education plan.

And when you find a website that offer education plan, You’ll find that they’re processing student requests applications through two ways.

The first way is processing students applications manually, That’s said. You as student to get this free education plan, You should submit your university ID to their email address and someone from the team will review your application and after that he will enable the education plan on your account. Companies like Slack, Github, and a lot of other depends on this way.
Second way and this is the focus of my writeup, as some websites and the most are processing student plan verification automatically. This simply happens by registering your account with emails like khaled.hassan@harvard.edu and when you verify your email, education plan will be enabled on your account directly. So emails that ends with ( 
e
du ) domain is only accepted.

The story started when I was reading the support articles of a private program that I invited to it . and I found them wrote that any student can get their gold premium plan for free ( This plan worth $1500 per month )

Press enter or click to view image in full size

Then I clicked on https:// redacted.com/edu to see what is inside this signup page,

So I found that you can’t register your account through this page otherwise with emails like ( khaled@harverd.edu ) and after you sign up successfully, website will send a confirmation link to your email and you can’t access the website without it. frustrating thing, right?

After trying to access the account I registered without the confirmation link, this didn’t work and I thought on another way to bypass.

So before I write about how I bypassed this and got the premium plan for free, I would like to write brief about a feature on this website. When you register an account on the website you can create your own workspace/company profile on your account and invite others to collaborate with you to design together.

From here I tried to invite my test account to my own company. After I did that, I received the following invitation link:

https://redacted.com/signup/invite?id=4d0940077e1443a78c29da51

Note: When you create your account through this invitation link, Website will not require from you to confirm your email because its already confirmed by the invitation link.

Get Khaled Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I opened the invitation link, I have found that my invited email address is being reflected on the signup page

So I asked myself based on what the email address gets printed on the page? and what If I changed the invitation token parameter to the ID of any user? Maybe we get email disclosure vulnerability? Quickly I sent this get request to server to list the account ID of my test account I have invited to my company

GET/api/companies/9129600280152c09ef1dd588/users HTTP/1.1
Host: redacted.com
Connection: close
Content-Length: 244
Accept: application/json, text/plain, */*
Origin: https:// redacted.com
X-XSRF-TOKEN: 3dytjyp1UHElYXBnHPrQKQ==
Accept-Language: en_US
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Content-Type: application/json;charset=UTF-8
Cookie:

The response was as you can see, The (“EntryID”) Parameter is the ID of invited user

Press enter or click to view image in full size

Then I replaced the invitation token on the URL with EntryID of invited the test account. so the final URL would be

https:// redacted.com/signup/invite?id=5b209840ddb3290f4d5f4be4

What happened after that? I found that the application is still printing the email of the invited account on the page. That’s mean I have a valid invitation token. so I registered the test account with EntryID value instead of invitation token and by this we I bypassed the email verification of education accounts through replacing invitation tokens with EntryID parameter value.

So here is the steps that I got the education plan by although I’m not a student
I have invited my random email (khaled@harverd.edu) to the company profile I own
From the same account I issued a GET request to company users endpoint to get the ID of khaled@harverd.edu account
After I got the EntryID I pasted it on this URL
https://redacted.com/signup/invite?id=4d0940077e1443a78c29da51
After I created the account successfully and verified it using invitation URL. I activated the education plan on my khaled@harverd.edu account easily and got premium plan that worth $1500 per month for free!
How this has been fixed?

After I reported this issue, The website converted processing students applications from automatically to manually method like reset websites.

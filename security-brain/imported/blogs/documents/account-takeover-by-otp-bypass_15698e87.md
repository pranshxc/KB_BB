---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-13_account-takeover-by-otp-bypass.md
original_filename: 2020-09-13_account-takeover-by-otp-bypass.md
title: Account takeover by OTP bypass
category: documents
detected_topics:
- otp
- command-injection
- api-security
tags:
- imported
- documents
- otp
- command-injection
- api-security
language: en
raw_sha256: 15698e870c3ace0a0aeb443178295a21256f8012f65e5aee3f8b7824bad96459
text_sha256: aca4bc072076a3a347cdb30c0f7f2b8bb70fb15c8795f4f44966a04be245b4d4
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover by OTP bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-13_account-takeover-by-otp-bypass.md
- Source Type: markdown
- Detected Topics: otp, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `15698e870c3ace0a0aeb443178295a21256f8012f65e5aee3f8b7824bad96459`
- Text SHA256: `aca4bc072076a3a347cdb30c0f7f2b8bb70fb15c8795f4f44966a04be245b4d4`


## Content

---
title: "Account takeover by OTP bypass"
url: "https://medium.com/@bhavarth33/how-i-was-able-to-takeover-any-account-by-otp-bypass-bba698a725f"
authors: ["Bhavarth Kandoria"]
bugs: ["OTP bypass"]
publication_date: "2020-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4264
scraped_via: "browseros"
---

# Account takeover by OTP bypass

Account takeover by OTP bypass
Bhavarth Kandoria
Follow
3 min read
·
Sep 13, 2020

72

2

Hello readers, Its interesting how there are many different ways to bypass authentication. Luckily, I got to experiment to bypass authentication by static code analysis.This write up talks about How I was able to bypass authentication by static code analysis.

I was looking for a good big platform to test. So, I kept thinking about the website on which I can dirty my hands on. Finally, I came up with an online booking site of a very popular and attractive tourist place. For the reference we will refer it as redacted.com in this blog post.

Let’s dive deep on how this can be achieved.

Somehow my personal favorite vulnerability is authentication bypass. Also, in this category, OTP bypass is my most favorite. So I have my personal checklist to look for the grey area for OTP bypass vulnerability. I will cover up two points from that checklist which I tried during the process of finding the bypass in redacted.com

Let’s discuss the first one which is Intercepting the response.

In the Burp suite, I configured to intercept the request and response. In this method, hackers usually check the server response for incorrect OTP and then try to simulate the response for correct OTP. So I tried with invalid OTP and sent that request to repeater to check the response. I was getting {"status":true,"data":{"valid":false}} response from server for the invalid OTP.

Response with incorrect OTP

On the next attempt, I tried to change response with {"status":true,"data":{"valid":true}} and forwarded the request with burp suite. BAD LUCK :(
I was unable to bypass the authentication by intercepting the response and forward it.

After that, I tried to intercept the request for OTP again and this time I tried with correct OTP to check the server response in case of correct OTP. I entered the correct OTP, captured the request, sent the request to repeater and verified the response for the correct OTP. The response looks like:

{
  "status":true,
  "data":{
  "valid":true,
  "token":"*******************",
  "name":"username"
  }
}

By looking at the response, first thing that came to my mind was that this is a token based request which will be validated with each request. Due to that my scope of testing will increase because now I need to figure out token based weakness of the application to bypass the OTP. But still my checklist to bypass OTP vulnerability had one more point which is static analysis. In this point I basically started to look at the HTML, JS files to see if there is any coding weakness for authentication.

Get Bhavarth Kandoria’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found one function which was potential implementation to validate the OTP. The function looks like:

Function for OTP validation

By analyzing this code, I understood that the function is only verifying the length of the token and name in the request. It was not validating the full token. Check the condition: if(token.length>0 && name.length>0).

In the second attempt, I entered incorrect OTP, captured the request, forwarded the request, captured the response, updated the response from {"status":true,"data":{"valid":false}} to {"status":true,"data":{"valid":true,"token":"test","name":"username"}}
BINGO… I was able to log in successfully. This was my first static code analysis bug. I quickly wrote the steps and reported to the concerned party with proper POC.

Below is the report to help readers and new community members on How to write the report on your findings.

Press enter or click to view image in full size
Report

In few hours, I got the acknowledgement from the company regarding the vulnerability. Company also appreciated the efforts by listing my name in hall of fame.

Conclusion:

Always try to look for the different attack vectors. Even if you failed on one method, try to look for different methods. Make your personal checklist to find bugs and improve it day by day. At the end, no application is bug free...Right?? :)

Thanks for reading.

If you enjoyed it please do clap.

LinkedIn: https://www.linkedin.com/in/bhavarth-kandoria-8a8590135/

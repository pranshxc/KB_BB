---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-11_rate-limit-bypass-at-readmecom.md
original_filename: 2022-03-11_rate-limit-bypass-at-readmecom.md
title: Rate Limit Bypass at Readme.com
category: documents
detected_topics:
- rate-limit
- password-reset
- otp
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- rate-limit
- password-reset
- otp
- command-injection
- mfa
- api-security
language: en
raw_sha256: 8143c881dc1a36678f42d271708f37e193fd02c32f29627cf2830a3e0b62d15b
text_sha256: b70e3e8caaafb5a05652d7f7e6b970eada3ddde65bf44a5b816666b82d4555a2
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Rate Limit Bypass at Readme.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-11_rate-limit-bypass-at-readmecom.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, otp, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `8143c881dc1a36678f42d271708f37e193fd02c32f29627cf2830a3e0b62d15b`
- Text SHA256: `b70e3e8caaafb5a05652d7f7e6b970eada3ddde65bf44a5b816666b82d4555a2`


## Content

---
title: "Rate Limit Bypass at Readme.com"
url: "https://medium.com/@girishbo58/rate-limit-bypass-at-readme-com-35c4fb0c7f85"
authors: ["Girishbo"]
programs: ["Readme.com"]
bugs: ["Lack of rate limiting", "Password reset"]
publication_date: "2022-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2836
scraped_via: "browseros"
---

# Rate Limit Bypass at Readme.com

Rate Limit Bypass at Readme.com
Girish B O
Follow
3 min read
·
Mar 12, 2022

195

5

Hey Community !!

I am sharing my experience and knowledge, hope it will add some value to your Bug Hunting. This is my first article, if there are any errors. Ignore it …

About me?

My name is Girish B O from INDIA working as Security Analyst |Bug Bounty Hunter |Security Researcher .

Hobbies -Stalk & Hunt for Bugs , Travelling !!

What is Rate Limit ??

Rate limiting is used to control the amount of incoming and outgoing traffic to or from a network. If the number of requests you make exceeds that limit, then an error will be triggered. Rate limiting algorithm is used to check if the user session or IP address has to be limited based on the information in the session cache. In case a client makes too many requests within a given time frame, HTTP servers can respond with status code 429(Too Many Requests).

Where to find this Bug ?

Register /Sign up Pages.
Login Page.
Account Verification.
Forget Passwords.
Two Factor Authentication(2FA) Codes , Coupon Codes etc…

However many applications are protected from this vulnerability and found an interesting bypass for this.

How to Bypass ??

Let’s get started …

Steps To Reproduce:

Register to read.me here https://dash.readme.com/signup.
Confirm your email and now navigate to Forgot Password.
Navigate to https://dash.readme.com/forgot/ .Enter registered email.
Press enter or click to view image in full size

4. Intercept the request with burp and send it to the repeater.

Get Girish B O’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. Analyze the X-Ratelimit-Limit is set to 5.Once the limit is reached to 0 the browser responds with “Too many Attempts’’.

Press enter or click to view image in full size

6. This can be bypassed by Injecting Request Header. Add X-Forwarded-For: 127.0.0.1 now 5 more attempts are added. After the limit is reached again, change the “X-Forwarded-For: 127.0.0.2” now again 5 more attempts are added and so on…

Press enter or click to view image in full size
X-Ratelimit-Remaining increased when changed to (127.0.0.1)
Press enter or click to view image in full size
X-Ratelimit-Remaining increased when changed to (127.0.0.2)

Drafted the report and sent it to Readme.com security Team. Unfortunately the Readme.com team replied this was duplicate. No worries !!

So what’s the Impact ??

This will lead to mass mailing to the targeted user, which will degrade the reputation of the company.
If the company is using any 3rd party Email Service API then this will lead to Business Cost impact once the Email limit has exceeded.
Attackers can chain this vulnerability to Brute force attack guessing OTP’s , Password Tokens etc…

Some more TIPS to Bypass this !!

Using Null Characters ( %0 , %00 , %09 , %020 , %0a , %0C , %0d%0a ) etc…
Injecting Host Request Headers.

X-Originating-IP: IP
X-Forwarded-For: IP
X-Remote-IP: IP
X-Remote-Addr: IP
X-Client-IP: IP
X-Host: IP
X-Forwarded-Host: IP

3. Change Random Parameters (Example : /api/v1/users/id change it to /api/v2/users/id ) etc..

4. Using Extenders like Burp (IP Rotate). This extension allows you to easily spin up API Gateways across multiple regions.

Until Next Time !!

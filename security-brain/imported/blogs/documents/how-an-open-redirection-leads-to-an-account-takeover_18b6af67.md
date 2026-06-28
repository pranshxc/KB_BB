---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-26_how-an-open-redirection-leads-to-an-account-takeover.md
original_filename: 2022-05-26_how-an-open-redirection-leads-to-an-account-takeover.md
title: How an Open Redirection Leads to an Account Takeover?
category: documents
detected_topics:
- password-reset
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- password-reset
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 18b6af67c98c36563b8ddc278f24ada77ff6247863846313ac5e52f911aaf0dc
text_sha256: 07dec402afd391d80c81e2c2e4f5fff9931c538019196dff5decc4c38c105623
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How an Open Redirection Leads to an Account Takeover?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-26_how-an-open-redirection-leads-to-an-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `18b6af67c98c36563b8ddc278f24ada77ff6247863846313ac5e52f911aaf0dc`
- Text SHA256: `07dec402afd391d80c81e2c2e4f5fff9931c538019196dff5decc4c38c105623`


## Content

---
title: "How an Open Redirection Leads to an Account Takeover?"
url: "https://infosecwriteups.com/how-an-open-redirection-leads-to-an-account-takeover-73ea883055d1"
authors: ["Mahendra Purbia (@Mah3Sec_)"]
bugs: ["Open redirect", "Account takeover"]
publication_date: "2022-05-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2606
scraped_via: "browseros"
---

# How an Open Redirection Leads to an Account Takeover?

How an Open Redirection Leads to an Account Takeover?
Mahendra Purbia (Mah3Sec)
Follow
2 min read
·
May 26, 2022

207

4

Hey folks,
I’m here to share one of my old finding. In which i found a unique way of an open redirection which leads to an account takeover.

So the Web App i testing was a Trading Platform. Let’s call it target.com for the demonstration purpose.

So there is a subdomain which used to login on platform. lets call it web.target.com and created a test account. After logged in i notice a feature “Verify whats-app number” so that user can verify account, reset password(both on email and directly through whats-app), get trading updates directly through whats-app. So i continued testing this functionality. While testing i noticed 2 things “number” & “domain” interesting that in post request. Is that mean that i can also change the domain?

Always trust on your Spider-Sense

let’s see if i can able to perform Open Redirection

Steps:

Go to https://web.target.com & login.
2. Now go to profile and add whats-app number.submit victim number/test number.
3. Intercept that request in Burp Suite and send it to repeater.
4. Now i change the “domain”: in request to “domain”:”https://bing.com" the request & response look like:
Press enter or click to view image in full size
check both request and response

5. Now the victim receives a message from Target.com official whats-app account. victim click on link and redirected to attackers domain.

Press enter or click to view image in full size

But that’s a low severity issue and doesn’t seem a security concern. So i just did one thing and try to leverage it to some serious vulnerability.

Get Mahendra Purbia (Mah3Sec)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. After verification of Whats app number i requested for password reset token. And captured that request in burpsuite.

7. Changed the “domain” to Ngrok URL and got message with reset link.

8. same time got a request in Ngrok dashboard, which carry password reset token.

Press enter or click to view image in full size

9. I used that token to reset password of victim account.

Impact: This vulnerability can leads to account takeover.

The company fixed the vulnerability and rewarded me💲💲💲.

Twitter: https://twitter.com/Mah3Sec
Youtube: https://www.youtube.com/@mah3sec
Thanks for reading my write-up, Happy Hunting!

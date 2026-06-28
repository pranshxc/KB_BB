---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-07_account-takeover-dont-send-a-message-to-anyone-before-reading-this-external-audi.md
original_filename: 2023-03-07_account-takeover-dont-send-a-message-to-anyone-before-reading-this-external-audi.md
title: '[Account Takeover] Don’t Send a Message to anyone Before Reading This [External
  Audit]'
category: documents
detected_topics:
- access-control
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- mfa
- api-security
language: en
raw_sha256: e5b9db39b43ed1932b8760cb691f87a0f0fe7d30da2eec898260b7e05f179c49
text_sha256: 5dfbebb58164fa696b9cc6cd4f9d66261efcd346d85a4159f924717fff7c54c0
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# [Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-07_account-takeover-dont-send-a-message-to-anyone-before-reading-this-external-audi.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `e5b9db39b43ed1932b8760cb691f87a0f0fe7d30da2eec898260b7e05f179c49`
- Text SHA256: `5dfbebb58164fa696b9cc6cd4f9d66261efcd346d85a4159f924717fff7c54c0`


## Content

---
title: "[Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]"
url: "https://infosecwriteups.com/dont-send-a-message-to-anyone-before-reading-this-account-takeover-vulnerability-external-audit-cf584a0c983c"
authors: ["Vipul Sahu"]
bugs: ["HTTP response manipulation", "Authentication bypass", "Account takeover"]
publication_date: "2023-03-07"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1412
scraped_via: "browseros"
---

# [Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]

[Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]
Vipul Sahu
Follow
3 min read
·
Mar 7, 2023

45

The security of a web application relies heavily on the strength and effectiveness of its authentication and authorization mechanisms. If these are not carefully designed, implemented, and maintained, the application can become vulnerable to a range of different attacks. One particularly dangerous attack vector is authentication bypass, where an attacker can gain access to the system without providing valid credentials.

During my recent penetration test, I discovered a critical account takeover vulnerability in the target system. This vulnerability can be exploited through response manipulation and requires the victim to send a message to the attacker. In the interest of protecting the target’s privacy, we will refer to it as “redacted.com” throughout this blog post.

Press enter or click to view image in full size

During my security testing, I inspected the response to a valid login request. Although the user_id was present, which is considered sensitive information, no cookies were set. Upon realizing this, I probed for response manipulation by inputting incorrect credentials and modifying the response with the correct one. To my surprise, I was granted access for a brief moment before being immediately logged out of the dashboard. This unexpected behavior led me to believe that the application was performing additional checks.

Get Vipul Sahu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After further investigation, I stumbled upon an endpoint named user_login_status.php. Utilizing the match and replace function, I modified the response by changing any instance of user_signed_out to user_is_signed_in, thus mimicking a successful login. Although this allowed me to gain access to my account, I encountered an obstacle — I still required a user_id to carry out the account takeover.

Press enter or click to view image in full size
user_login_status.php

In the redacted system, I discovered a vulnerability in the way it handles the response to a get_message request. When a user sends a message to another user, redacted sends a get_message request to retrieve the message. However, the response to this request not only includes the message content but also the sender_id and sender_email, where the sender_id is actually the user_id.

Press enter or click to view image in full size
Leaking user_id and email address

By exploiting this vulnerability, I was able to intercept the response and gain access to the user’s account by using the sender_email and a random password on the login page. By modifying the response from

{“user_profile”:{“sign_in_status”:”invalid_password”}}

to

{“user_profile”:{“sign_in_status”:”login_success”,”user_id”:”<user_id_string>"}}

I was able to gain full access to the user’s account, allowing me to execute a complete takeover.

In conclusion, the vulnerability in redacted that allowed me to bypass authentication and take over any user’s account is a severe threat to the security of the application. To mitigate this vulnerability, the application should improve the design and implementation of its authentication and authorization mechanisms. The application can start by ensuring that responses to requests do not contain sensitive information such as user IDs or email addresses. It is also essential to validate responses properly to prevent tampering. Furthermore, implementing multi-factor authentication and session management can reduce the risk of account takeover.

Linkedin: https://www.linkedin.com/in/vipul-sahu-a7a420174/

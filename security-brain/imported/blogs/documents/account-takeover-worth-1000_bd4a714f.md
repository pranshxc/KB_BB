---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-19_account-takeover-worth-1000.md
original_filename: 2022-08-19_account-takeover-worth-1000.md
title: Account takeover worth $1000
category: documents
detected_topics:
- password-reset
- mfa
- oauth
- jwt
- sqli
- command-injection
tags:
- imported
- documents
- password-reset
- mfa
- oauth
- jwt
- sqli
- command-injection
language: en
raw_sha256: bd4a714ff10cd9392b25ce80b7df9e015bd0362a482db7e7e55478e743b79371
text_sha256: b9c2b13d287b1a8c4435f519d16ad54de3a9278e7c8ba314affe298032627215
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover worth $1000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-19_account-takeover-worth-1000.md
- Source Type: markdown
- Detected Topics: password-reset, mfa, oauth, jwt, sqli, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `bd4a714ff10cd9392b25ce80b7df9e015bd0362a482db7e7e55478e743b79371`
- Text SHA256: `b9c2b13d287b1a8c4435f519d16ad54de3a9278e7c8ba314affe298032627215`


## Content

---
title: "Account takeover worth $1000"
url: "https://medium.com/@faique/account-takeover-worth-1000-611452063cf"
authors: ["Faique (@imfaiqu3)"]
bugs: ["Account takeover", "Authentication bypass", "Information disclosure", "Password reset"]
bounty: "1,000"
publication_date: "2022-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2285
scraped_via: "browseros"
---

# Account takeover worth $1000

Faique
 highlighted

Account takeover worth $1000
Faique
Follow
4 min read
·
Aug 19, 2022

417

4

Press enter or click to view image in full size
Introduction

Hello everyone, I am Faique a bug bounty hunter from India and I welcome you to my write-up on how I got an account takeover in one of the largest organizations using misconfigured 2FA and OAuth.

I cannot disclose that target because it was a private invite. Before getting into the vulnerability I want you to get a foothold on how everything works especially authentication this will help you to understand the bug more clearly. There are multiple ways to sign in to the website but they can be categorized in two ways, First using normal email and password and the other is by using OAuth which includes Google, GitHub and …

Press enter or click to view image in full size

A security feature that the website has is 2FA which played a major role in this bug. A customer can use it to add an extra security layer. Now let’s come to the procedure and the bug.

I started with basic recon but didn’t find anything. So I moved toward authentication testing, created an account and tested for duplicate registration, forgot password bugs, SQL injection and so on. Then I enabled 2FA and brute-forced the 2FA code I tried this with both email,password login and with Oauth login but nothing worked:(

Press enter or click to view image in full size

Next day I enabled 2FA on google oauth account and intercepted every request and send juicy one to repeater like when the website send 2FA code to the server.

Press enter or click to view image in full size

I tested for some more 2FA bugs and then got fed up and stopped 2FA on the account, Then meanwhile after I was going to all my repeater requests I got stumbled on the above request again and sent that again and received a JWT token I thought why not change the authenticator code with some random code like 000000 and send the request again and guess what I received the JWT token

Press enter or click to view image in full size

Even after disabling 2FA on the account, I was able to get a JWT code using this request. This JWT token is basically the cookie that is used to authenticate users. To confirm this was actually a vulnerability I waited 1 day and then send the request again and yeah I received the JWT token. I was so excited at that point.

I just needed a way to directly login to the hacked account. So I started browsing the website logged in and I saw there was a feature to set password to the oauth account so that anyone can login using email & password.

Press enter or click to view image in full size

I used set password request and replaced the JWT token to the one i received and send it.The password got added.

Press enter or click to view image in full size

I can now login directly using the email and password bypassing oauth headache. This bug not only affect google oauth login but affects all oauth provider used by the site: GitHub, Microsoft, Bitbucket, Azure active directory

Get Faique’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Note: The bug is only possible if the customer had enabled and then disabled 2FA on their account

Impact:

Once the attacker has access to the account

1. Attacker can see, and edit confidential details like API keys

2. Edit organisation & product names

3. Invite members to the account

4. Remove users from the organisation

5. Add a password to the account

6. Delete the account

Reported the bug to the site

Timeline

00:09, 1 August: Reported the bug

02:20, 1 August: First rejected as they though this is false positive

03:00, 1 August: Accepted it and asked for patience

01:20, 5 August: Marked the bug as high business critical security issue and offered me $1000

Press enter or click to view image in full size
Thank you for reading till here I hope you enjoyed and learned something new from it. Feel free to Dm me if you have any query
Follow me on
Twitter: https://twitter.com/imfaiqu3
Instagram: https://www.instagram.com/faique.exe
LinkedIn: https://www.linkedin.com/in/faiqu3/

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

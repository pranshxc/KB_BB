---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_ato-of-wordpress-website-4-digits-bounty-in-5-minute.md
original_filename: 2021-08-29_ato-of-wordpress-website-4-digits-bounty-in-5-minute.md
title: ATO of WordPress Website “4 digits €€€€ Bounty in 5 Minute!”
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 6a2fb6c149aec054c2dcc4151c6c7cdfb876c79ed010b4fac01a3424b25fcb5e
text_sha256: c1f8589bc63c9dd34c84137e76a641cf1c20c56d01a73e82887955189ff12f9f
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# ATO of WordPress Website “4 digits €€€€ Bounty in 5 Minute!”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_ato-of-wordpress-website-4-digits-bounty-in-5-minute.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6a2fb6c149aec054c2dcc4151c6c7cdfb876c79ed010b4fac01a3424b25fcb5e`
- Text SHA256: `c1f8589bc63c9dd34c84137e76a641cf1c20c56d01a73e82887955189ff12f9f`


## Content

---
title: "ATO of WordPress Website “4 digits €€€€ Bounty in 5 Minute!”"
url: "https://riteshgohil-25.medium.com/ato-of-wordpress-website-4-digits-bounty-in-5-minute-cc888c4054c9"
authors: ["Ritesh Gohil (@RiteshG37659480)"]
bugs: ["Exposed registration page", "Account takeover"]
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3375
scraped_via: "browseros"
---

# ATO of WordPress Website “4 digits €€€€ Bounty in 5 Minute!”

Ritesh Gohil
 highlighted

ATO of WordPress Website “4 digits €€€€ Bounty in 5 Minute!”
Ritesh Gohil
Follow
2 min read
·
Aug 29, 2021

342

1

Hi Everyone,

As I promised, I would like to explain how I was awarded my first 4 digit bounty in 5 minutes!
Without Delay, Let's get started to understand this vulnerability.

Scenario:
Target Website was hosted on WordPress. The version of the WordPress website was the latest one. I have noticed that a number of plugins were used on xyz.com Also, the wp-login page was also there. I have checked all registration pages and signup pages of the target website.

Note: Every plugin has a WordPress installation page but it's disabled by the administrator. That means any user/admin can able to install WordPress and create their admin account on that website.

Get Ritesh Gohil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While performing Recon on a subdomain of a private bug-bounty program, I found one of the URLs where I can able to register a new account with admin privilege.

Steps To Reproduce:

First, I have used waybackurl to find the endpoint of the website.
The endpoint was /wp-admin/install.php
If you are able to find this endpoint in any WordPress website then click on the Install WordPress button and register your email address.
(Note: You will get a similar endpoint on many WordPress websites but new registration button/functionality might be disabled on that website.)
Once you registered, you will get a confirmation link to set a new password.
Now Visit https://xyz.com/wp-login.php
Now, login with your registered email address, and Boom! I got access to the admin panel of the WordPress website.

6. I can perform all activities and upload all images on this domain and change configuration files as you want.

Press enter or click to view image in full size

Thank you for reading my blog.
Guys, if you will able to find a similar bug after reading this blog kindly message me its feel good :)

Cheers! Happy Hunting Guys :)
Linkedin: https://ie.linkedin.com/in/riteshgohil25
Twitter: https://twitter.com/RiteshG37659480

Support me if you like my work! Buy me a coffee and Follow me on Twitter.

Hunting With Ritesh :)
Hey 👋 I just created a page here. You can now buy me a coffee!

www.buymeacoffee.com

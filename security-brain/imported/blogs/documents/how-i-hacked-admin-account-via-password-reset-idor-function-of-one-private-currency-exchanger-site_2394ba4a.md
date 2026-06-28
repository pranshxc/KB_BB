---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-19_how-i-hacked-admin-account-via-password-reset-idor-function-of-one-private-curre.md
original_filename: 2018-05-19_how-i-hacked-admin-account-via-password-reset-idor-function-of-one-private-curre.md
title: How i HACKED admin account via password reset IDOR function of one private
  currency exchanger site
category: documents
detected_topics:
- password-reset
- idor
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- idor
- command-injection
- otp
language: en
raw_sha256: 2394ba4a2169243ca300e43ce7216b927e391dcdaebf00e7b4afe6ece758b0dc
text_sha256: 15e61d9ea51acc636453ea973d761ad5fc2ee7eb1b6e8ef3e47e28e8fb59b485
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# How i HACKED admin account via password reset IDOR function of one private currency exchanger site

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-19_how-i-hacked-admin-account-via-password-reset-idor-function-of-one-private-curre.md
- Source Type: markdown
- Detected Topics: password-reset, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `2394ba4a2169243ca300e43ce7216b927e391dcdaebf00e7b4afe6ece758b0dc`
- Text SHA256: `15e61d9ea51acc636453ea973d761ad5fc2ee7eb1b6e8ef3e47e28e8fb59b485`


## Content

---
title: "How i HACKED admin account via password reset IDOR function of one private currency exchanger site"
page_title: "How I Hacked an Admin Account via a Password Reset IDOR Vulnerability on a Private Currency Exchange Site | by Aayush Pokhrel | Medium"
url: "https://medium.com/@aayushpokhrel/how-i-hacked-admin-account-via-password-reset-idor-of-one-private-currency-exchanger-site-51723c7c8704"
authors: ["Aayush Pokhrel (@aayushpok)"]
bugs: ["IDOR", "Account takeover", "Password reset"]
publication_date: "2018-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5878
scraped_via: "browseros"
---

# How i HACKED admin account via password reset IDOR function of one private currency exchanger site

How I Hacked an Admin Account via a Password Reset IDOR Vulnerability on a Private Currency Exchange Site
Aayush Pokhrel
Follow
2 min read
·
May 19, 2018

111

One day, I was searching for a site to hunt for vulnerabilities when I came across one. I started testing, but on the first day, I didn’t find anything, and I was unable to create an account on the site. However, on the next day, I managed to create a new account without verification.

I started thinking about how I could take over another user’s account. An idea came to my mind: testing the password reset function. So, I entered my email in the ‘Forgot Password’ section and clicked on ‘Send Password Reset Email.’ Finally, I received an email that looked like this:

https://site.com/password.php?email=myemail@email.com?hash=snogv***REDACTED-SUSPECT-TOKEN***First, I tried to understand the hash in the password reset email, but I couldn’t figure it out. So, I sent another password reset email to my account and received the same email with the exact same hash. I was shocked! 😲😃

To confirm, I sent another password reset email to my account again and got the same hash once more. At this point, I started feeling a bit excited because it meant the hash was not changing for every reset request.

To dig deeper, I tried sending a password reset request for another account — and to my surprise, I got the same hash again! This confirmed that the same hash was being used for every account.

Get Aayush Pokhrel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, I decided to test this further by attempting the following…

https://site.com/password.php?email=admin@email.com?hash=snogv***REDACTED-SUSPECT-TOKEN***I saw two input fields:

New Password=***REDACTED*** Password=***REDACTED*** entered a new password and tried to log in to the target account. To my surprise, it worked! I was able to access not only user accounts but also the admin account. 😱

Bug Status: Patched

Bounty: No bounty or reply yet, but at least it’s patched 🙂

#Happy_Hacking 🚀”

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-06-26_hijacking-a-facebook-account-with-sms.md
original_filename: 2013-06-26_hijacking-a-facebook-account-with-sms.md
title: Hijacking a Facebook Account with SMS
category: documents
detected_topics:
- otp
- access-control
- xss
- command-injection
- password-reset
- cloud-security
tags:
- imported
- documents
- otp
- access-control
- xss
- command-injection
- password-reset
- cloud-security
language: en
raw_sha256: 02e90337ab4a4e48a4c4b8a0598dcc179cdafc61f6430e109a540ed890c30b31
text_sha256: cef7ce666478098d2e73dd796d0547135cac2feaf0341d1a26381ccfa2b98019
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking a Facebook Account with SMS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-06-26_hijacking-a-facebook-account-with-sms.md
- Source Type: markdown
- Detected Topics: otp, access-control, xss, command-injection, password-reset, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `02e90337ab4a4e48a4c4b8a0598dcc179cdafc61f6430e109a540ed890c30b31`
- Text SHA256: `cef7ce666478098d2e73dd796d0547135cac2feaf0341d1a26381ccfa2b98019`


## Content

---
title: "Hijacking a Facebook Account with SMS"
page_title: "Hijacking a Facebook Account with SMS – Jack"
url: "https://whitton.io/articles/hijacking-a-facebook-account-with-sms/"
final_url: "https://whitton.io/articles/hijacking-a-facebook-account-with-sms/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Account takeover"]
bounty: "20,000"
publication_date: "2013-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6404
---

# [Hijacking a Facebook Account with SMS](https://whitton.io/articles/hijacking-a-facebook-account-with-sms/ "Hijacking a Facebook Account with SMS")

## June 26, 2013

__Reading time ~1 minute

This post will demonstrate a simple bug which will lead to a full takeover of any Facebook account, with **no user interaction**.

Facebook gives you the option of linking your mobile number with your account. This allows you to receive updates via SMS, and also means you can login using the number rather than your email address.

The flaw lies in the `/ajax/settings/mobile/confirm_phone.php` end-point. This takes various parameters, but the two main are `code`, which is the verification code received via your mobile, and `profile_id`, which is the account to link the number to.

The thing is, `profile_id` is set to your account (obviously), but changing it to your target’s doesn’t trigger an error.

To exploit this bug, we first send the letter `F` to `32665`, which is Facebook’s SMS shortcode in the UK. We receive an 8 character verification code back.

[ ![](/images/facebooksms/facebook-sms-1.jpg) ](/images/facebooksms/facebook-sms-1.jpg)

We enter this code into the activation box (located [here](https://www.facebook.com/settings?tab=mobile)), and modify the `profile_id` element inside the `fbMobileConfirmationForm` form.

[ ![](/images/facebooksms/facebook-sms-2-1.png) ](/images/facebooksms/facebook-sms-2-1.png)

Submitting the request returns a 200. You can see the value of `__user` (which is sent with all AJAX requests) is different from the `profile_id` we modified.

[ ![](/images/facebooksms/facebook-sms-3-1.png) ](/images/facebooksms/facebook-sms-3-1.png)

Note: You may have to reauth after submitting the request, but the password required is yours, not the targets.

An SMS is then received with confirmation.

[ ![](/images/facebooksms/facebook-sms-4.jpg) ](/images/facebooksms/facebook-sms-4.jpg)

Now we can initate a password reset request against the user and get the code via SMS.

[ ![](/images/facebooksms/facebook-sms-5-1.png) ](/images/facebooksms/facebook-sms-5-1.png)

Another SMS is received with the reset code.

[ ![](/images/facebooksms/facebook-sms-6-1.jpg) ](/images/facebooksms/facebook-sms-6-1.jpg)

We enter this code into the form, choose a new password, and we’re done. The account is ours.

[ ![](/images/facebooksms/facebook-sms-7.png) ](/images/facebooksms/facebook-sms-7.png)

### Fix

Facebook responsed by verifying that you have permission to modify the phone number on the profile denoted by `profile_id`.

### Timeline

  * 23rd May 2013 - Reported
  * 28th May 2013 - Acknowledgment of Report
  * 28th May 2013 - Issue Fixed

### Note

The bounty assigned to this bug was $20,000, clearly demonstrating the severity of the issue.

[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[authentication](https://whitton.io/tags/#authentication "Pages tagged authentication")[sms](https://whitton.io/tags/#sms "Pages tagged sms") Updated on June 26, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/hijacking-a-facebook-account-with-sms/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/hijacking-a-facebook-account-with-sms/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/hijacking-a-facebook-account-with-sms/ "Share on Google Plus")

[Read More](https://whitton.io/articles/overwriting-banner-images-on-etsy/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016

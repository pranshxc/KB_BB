---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-04_thisclosed_1-full-account-takeover-of-any-user-via-insecure-direct-object-refere.md
original_filename: 2022-01-04_thisclosed_1-full-account-takeover-of-any-user-via-insecure-direct-object-refere.md
title: thisclosed_#1 - Full Account Takeover of ANY user via Insecure Direct Object
  Reference (IDOR) on reset password functionality
category: documents
detected_topics:
- idor
- sso
- access-control
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- idor
- sso
- access-control
- command-injection
- password-reset
- otp
language: en
raw_sha256: c4323161309f5517888c4da190807b0986bed8c0f4ef5ca872ff71e6dff5cf6d
text_sha256: 4104a3247fc5447612a0f5841dd305cea7180bce8bdc60a72a8795f63941bbdb
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# thisclosed_#1 - Full Account Takeover of ANY user via Insecure Direct Object Reference (IDOR) on reset password functionality

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-04_thisclosed_1-full-account-takeover-of-any-user-via-insecure-direct-object-refere.md
- Source Type: markdown
- Detected Topics: idor, sso, access-control, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c4323161309f5517888c4da190807b0986bed8c0f4ef5ca872ff71e6dff5cf6d`
- Text SHA256: `4104a3247fc5447612a0f5841dd305cea7180bce8bdc60a72a8795f63941bbdb`


## Content

---
title: "thisclosed_#1 - Full Account Takeover of ANY user via Insecure Direct Object Reference (IDOR) on reset password functionality"
page_title: "thisclosed_#1 | Hackrate Blog"
url: "https://blog.hckrt.com/blog/thisclosed_1/"
final_url: "https://blog.hckrt.com/blog/thisclosed_1/"
authors: ["Samuele Gugliotta (@indevi0us)"]
bugs: ["IDOR", "Password reset", "Account takeover"]
publication_date: "2022-01-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3030
---

Hello, folks! It’s Samuele Gugliotta here, Offensive Security Researcher & Bug Bounty Hunter, probably better known as venomnis. There’s nothing better than starting a new year off on the right foot and, in fact, this time it’s to present a critical vulnerability in my first writeup of this 2022! It was recently found in a private program on my favorite bug bounty platform: Hackrate. So, cut the chatter, let’s get down to business.

**Full Account Takeover of ANY user via Insecure Direct Object Reference (IDOR) on reset password functionality!**

### Summary

As you can see in the above banner, it’s about an Insecure Direct Object Reference (IDOR), which is actually one of the most underrated access control vulnerability that specifically arises when an application uses user-supplied input to access objects directly.

In my case, would have allowed me to reset the password of literally **any user** present in the application simply by guessing the incremental identifiers associated to them. This condition, combined with another abnormal behavior detected, namely that the application stored additional detail and matches them with the relevant database entries in the outer HTML of the pages (e.g. `<label class="label is-marginless">E-mail:</label><p class="control">venomnis@letmehack.it</p><input type="hidden" name="id" value="57">`) made it possible for me to get to the full account takeover.

### Description

Following the user creation and then browsing the authenticated features of the web application at `<redacted.com>`, I particularly focused on the reset password form, as it is a notoriously abused feature for obvious reasons. After interacting with it by requesting the confirmation link to reset my password by e-mail, I noticed that incremental numeric identifiers were assigned to registered users. It was possible to get evidence of this from the received URL, that was something like the following `https://<redacted.com>/reset-password/0-57-axq24ncy32bh1hc8nrp78xyz`, within which the numerical identifier `57` could be noticed, between `0-` and the token. To confirm this, I created a second account that I would then use as a victim, and repeating the same password reset procedure I got a link similar to this one `https://<redacted.com>/reset-password/0-58-bce64t3ane46tt9nr6ce2kk33`. Inevitably that `58` caught all my attention.

![](https://i.gifer.com/Bd0t.gif)

So, I went to retrieve the password reset POST request submitted before for the first user with `id=57`, from the proxy history of my BurpSuite Professional that in the meantime was listening passively. I found that the same ID was passed as a parameter in the body of the POST request.  ![request](/static/eeeec38782b8bc660d7639ed72d29dd5/1bed9/request.png)

Assuming that `_token` had now been used, I repeated the password reset request for the first user, whom I called the attacker, but this time intercepting it with my web application proxy. I then changed the id parameter in the body of that request from `id=57` to `id=58` and chose a different password, before forwarding. The application responded with a pop-up informing me that the password had been successfully changed. And indeed, I was no longer able to perform authentication with the _victim user_ using the password chosen at the first registration, but the one sent in the malformed POST request by the _attacker user_ , well that one worked just fine. ^^

### Impact

Full account takeover of any registered user.

In the worst case scenario, the same could be repeated on all the other users with id <57 and of course on the subsequent ones that would be created, resulting in a complete compromise.

### Acknowledgements

I would like to thank the Hackrate Team for giving me the opportunity to try my hand at this private program and for carrying out the triage of the report, as well as the subsequent phases, in a serious, professional and useful way in terms of timing both for me, but above all for the Team that took care of the fix deployment. Thanks also to the Customer Team for giving consideration to my report and for having resolved the vulnerability in a masterful way.

That’s all for now.

_venomnis_

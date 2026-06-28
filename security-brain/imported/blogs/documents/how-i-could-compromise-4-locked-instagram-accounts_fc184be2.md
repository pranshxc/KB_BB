---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-03-27_how-i-could-compromise-4-locked-instagram-accounts.md
original_filename: 2016-03-27_how-i-could-compromise-4-locked-instagram-accounts.md
title: How I Could Compromise 4% (Locked) Instagram Accounts
category: documents
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- password-reset
- rate-limit
- api-security
language: en
raw_sha256: fc184be2547df27ee7505d38c2e37ca440d0fd507ecf2de0f4ec806e742a072f
text_sha256: cfce1d57751ad39b63b6793e70c58a27cadf252c95ebd8c9e5fe87e4e2b13d55
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I Could Compromise 4% (Locked) Instagram Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-03-27_how-i-could-compromise-4-locked-instagram-accounts.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `fc184be2547df27ee7505d38c2e37ca440d0fd507ecf2de0f4ec806e742a072f`
- Text SHA256: `cfce1d57751ad39b63b6793e70c58a27cadf252c95ebd8c9e5fe87e4e2b13d55`


## Content

---
title: "How I Could Compromise 4% (Locked) Instagram Accounts"
page_title: "How I Could Compromise 4% (Locked) Instagram Accounts – Arne Swinnen"
url: "https://www.arneswinnen.net/2016/03/how-i-could-compromise-4-locked-instagram-accounts"
final_url: "https://www.arneswinnen.net/2016/03/how-i-could-compromise-4-locked-instagram-accounts/"
authors: ["Arne Swinnen (@ArneSwinnen)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "DoS", "Broken authorization"]
bounty: "5,000"
publication_date: "2016-03-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6309
---

[3](https://www.arneswinnen.net/2016/03/how-i-could-compromise-4-locked-instagram-accounts/#comments)

# How I Could Compromise 4% (Locked) Instagram Accounts

Posted on [March 27, 2016](https://www.arneswinnen.net/2016/03/how-i-could-compromise-4-locked-instagram-accounts/ "10:27 pm") by [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "View all posts by Arne Swinnen")

**TL;DR:** [Missing authentication](https://www.owasp.org/index.php/Top_10_2013-A7-Missing_Function_Level_Access_Control) combined with a simple [Insecure Direct Object Reference](https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References) vulnerability allowed to overtake a selection of temporary locked Instagram accounts. An extrapolation of the PoC account range learned that 4% of all existing & active Instagram accounts (approx. 500 million) were in a vulnerable locked state (approx. 20 million). Facebook fixed the vulnerability within a day and granted a $5.000 bounty 10 days later.

# Issue

It was a while ago that I actually hunted for vulnerabilities in Instagram when I logged back in to one of my test accounts. I have spent most of my free time in 2016 [presenting about Instagram vulnerabilities](https://www.arneswinnen.net/2016/02/the-tales-of-a-bug-bounty-hunter-10-interesting-vulnerabilities-in-instagram/) I found in 2015. After providing valid credentials, I was immediately redirected to a page which told me I had to verify my account, probably due to inactivity. The option that was offered to me was to verify by email, as I didn’t link any phone number to this account yet:

[![1](https://www.arneswinnen.net/wp-content/uploads/2016/03/1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/03/1.png)

The URL revealed the issue: this page was actually accessible without being authenticated (“checkpoint_logged_out_main”) and contained my Instagram test account’s unique user id. Now, even if I were to land on the same “Verify by Email” page of other accounts, it would have no direct security impact, as I don’t have access to my victims’ email addresses. However, an enumeration of one million accounts in the range 2.000.000000-2.001.000000 (Instagram has incremental user ids 🙂 ) yielded the following interesting results:

## Verify account via Captcha: 1.099 accounts (0.1%)

[![2](https://www.arneswinnen.net/wp-content/uploads/2016/03/2.png)](https://www.arneswinnen.net/wp-content/uploads/2016/03/2.png)

These might have been accounts that were observed to perform spamming. No direct security impact.

## Verify account via email / SMS: 1.960 accounts (0.2%)

[![3](https://www.arneswinnen.net/wp-content/uploads/2016/03/3.png)](https://www.arneswinnen.net/wp-content/uploads/2016/03/3.png)

This was the same case as for my test account: No direct security impact.

## Update email address & verify account: 1.690 accounts (0.17%)

[![4](https://www.arneswinnen.net/wp-content/uploads/2016/03/4.png)](https://www.arneswinnen.net/wp-content/uploads/2016/03/4.png)

Now this is where things got interesting. This page allowed me to update the email address of the temporary locked account, which is a big deal. Once an attacker could set the email address linked to an Instagram account, he/she could perform a password reset via email and gain full access to it. Big security impact, but only 0.17% accounts affected in the one million range.

## Update phone number & verify account: 38.808 accounts (3.88%)

[![5](https://www.arneswinnen.net/wp-content/uploads/2016/03/5.png)](https://www.arneswinnen.net/wp-content/uploads/2016/03/5.png)

This case was the most troublesome, as an attacker could on one hand gather sensitive user information (pre-filled phone number in some cases), and on the other hand simply update the phone number linked to the victim Instagram account. After successfully linking a new phone number, an attacker could perform the “reset password via SMS” scenario and gain complete access to the account. Big security impact, and almost 4% of all accounts affected in the one million range. A quick manual verification also learned that these were mostly human accounts which had been inactive for a couple of weeks, of which many had a good amount of followers on Instagram.

Note that I could not immediately get any of my test accounts in the “phone number verification” state and thus did not perform an actual account takeover scenario, since I couldn’t reproduce this on my test accounts directly. This is the only thing you can do when adhering to responsible disclosure – never touch existing accounts! I explicitly mentioned this to Facebook while reporting, in order to avoid any confusion. I believe this is the responsibility of all bug bounty hunters, despite the fact that it might result in lower bounties in some edge cases. The required trust relationship between researchers and bug bounty providers in the eco-system relies on this, which is still too often under pressure currently.

# Remediation

Facebook fixed the issue within 24 hours, by enforcing authentication on the pages that allow to update profile information such as email address and/or phone number.

# Timeline

  * 14/03/2016: Bug submitted to Facebook
  * 14/03/2016: Facebook reply: “We are sending it to the appropriate product team for further investigation.”
  * 15/03/2016: Facebook reply: “We have looked into this issue and believe that the vulnerability has been patched.”
  * 16/03/2016: Confirmation that bug is fixed to Facebook
  * 25/03/2016: Facebook reply: “After reviewing the issue you have reported, we have decided to award you a bounty of $5,000 USD.”

### [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "All posts by Arne Swinnen")

![](https://secure.gravatar.com/avatar/85c6e3f06dfe5994e9c112f745d801f39266bc0c77c1deadbfed337f3aa5da49?s=70&d=mm&r=g)

[](https://www.twitter.com/ArneSwinnen)[](https://www.linkedin.com/in/arneswinnen)

Belgian. IT Security. Bug Bounty Hunter.

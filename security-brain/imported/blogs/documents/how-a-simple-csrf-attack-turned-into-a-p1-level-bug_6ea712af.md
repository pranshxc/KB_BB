---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-05_how-a-simple-csrf-attack-turned-into-a-p1-level-bug.md
original_filename: 2020-04-05_how-a-simple-csrf-attack-turned-into-a-p1-level-bug.md
title: How a Simple CSRF Attack Turned into a P1 Level Bug
category: documents
detected_topics:
- csrf
- xss
- command-injection
- otp
tags:
- imported
- documents
- csrf
- xss
- command-injection
- otp
language: en
raw_sha256: 6ea712af1022b3250aee15306344ef86424e51f7b61069408cb29ee97ba98f25
text_sha256: b376b564ea45200e79277bf6ef22a8ff0b2f0c776425a1c32ac748ba993b04b6
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How a Simple CSRF Attack Turned into a P1 Level Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-05_how-a-simple-csrf-attack-turned-into-a-p1-level-bug.md
- Source Type: markdown
- Detected Topics: csrf, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `6ea712af1022b3250aee15306344ef86424e51f7b61069408cb29ee97ba98f25`
- Text SHA256: `b376b564ea45200e79277bf6ef22a8ff0b2f0c776425a1c32ac748ba993b04b6`


## Content

---
title: "How a Simple CSRF Attack Turned into a P1 Level Bug"
page_title: "How a Simple CSRF Attack Turned into a P1 Level Bug – Lady Secspeare"
url: "https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/"
final_url: "https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/"
authors: ["Lady Secspeare (@bejuveria_)"]
bugs: ["CSRF", "Account takeover"]
publication_date: "2020-04-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4665
---

# How a Simple CSRF Attack Turned into a P1 Level Bug

Posted by[Lady Secspeare](https://ladysecspeare.wordpress.com/author/ladysecspeare/)[April 5, 2020April 5, 2020](https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/)Posted in[Uncategorized](https://ladysecspeare.wordpress.com/category/uncategorized/)Tags:[Bug Bounty](https://ladysecspeare.wordpress.com/tag/bug-bounty/), [Bug Bounty Hunting](https://ladysecspeare.wordpress.com/tag/bug-bounty-hunting/), [Bugcrowd](https://ladysecspeare.wordpress.com/tag/bugcrowd/), [Bypassing CSRF](https://ladysecspeare.wordpress.com/tag/bypassing-csrf/), [Cross-site Request Forgery](https://ladysecspeare.wordpress.com/tag/cross-site-request-forgery/), [CSRF](https://ladysecspeare.wordpress.com/tag/csrf/), [CSRF Bypass](https://ladysecspeare.wordpress.com/tag/csrf-bypass/), [P1](https://ladysecspeare.wordpress.com/tag/p1/)

Cross-site Request Forgery is easy to lookout for. However, if there are security measures in place to prevent CSRF attacks, they can be exciting (yet nerve-wracking) to bypass.

For those who don’t know, **Cross-site Request Forgery** is an attack where a malicious user can trick the victim into performing actions that they do not intend to do. And some of the preventive measures are:

  1. Use of anti-CSRF tokens
  2. Use of additional fields such as “Current Password”
  3. Use of same site cookies

**How I Began the Hunt**

When I received an invite to hunt on a private program on Bugcrowd, which was set to begin on 9th of February, 12AM IST, I was prepared to begin. Considering I was blind to the name of the program and there were 24 other chosen security researchers, I decided to hunt on the website head-on – without any recon.

I started looking for endpoints to perform a CSRF attack, I found the most impactful one: Change Password option. When I clicked on it, the following fields were a part of the entire HTTP Request:

![](https://ladysecspeare.wordpress.com/wp-content/uploads/2020/04/screenshot-from-2020-04-05-17-45-33__01__02.png?w=1001)**Mandatory email address field**

I suspected that the Email field will interfere as it was a mandatory one, but still tried performing CSRF with it. Since, the CSRF POC contained the attacker’s email address when updating the victim’s password it obviously didn’t work.

It will only work if I updated the value as victim’s email address in the Email field. So, as an attacker, every time I send the malicious link to the victim, I would have to use the victim’s email address before tricking them into clicking it.

It didn’t sit well with me. I wanted to increase the impact.

**How I Increased the Impact**

I tried to following:

  1. I removed the entire field from the CSRF POC.
  2. I only removed the value from the field.
  3. I entered random values in the field. (ajhgdsjhgd)

None of the above worked. I almost gave up thinking they have secured it against advanced CSRF attacks.

I then decided to try something else: I changed the email to a random value with the correct email address format. It didn’t have to be a valid email address; just anything as random as abcdefg@xyz.com. 

![](https://ladysecspeare.wordpress.com/wp-content/uploads/2020/04/screenshot-from-2020-04-05-18-25-46__01-2.png?w=842)**CSRF PoC with random email address**

I clicked on “Submit” from another browser, acting as the victim, and got the following message:

![](https://ladysecspeare.wordpress.com/wp-content/uploads/2020/04/screenshot-from-2020-04-05-17-47-30__01.png?w=771)**Message for Successfull Password Change using CSRF attack**

I didn’t want to celebrate just yet. To be sure, I tried logging into victim’s account as the attacker, using the new password.

Voila! I was logged in, implying I had successfully changed the victim’s password.

**Impact**

This scenario allowed me to take over the victim’s account without any effort of changing the email address value to the victim’s valid address. Furthermore, the severity level increased because just clicking on the link will have the victim locked out of their own account.

Bugcrowd rated this simple CSRF as P1 as it was a complete account takeover issue. 

**Why this was possible?**

Because there was no server-side validation of the Email field. And hence, the remediation for such problem would be to ensure the necessary validation is in place.

**Takeaway**

If you ever come across such fields, try to perform CSRF by giving random values, assuming there is no server-side validation. You may just come across a P1 issue. 

Now, wouldn’t it be a cherry on the top if the program is offering bounty?

Share your thoughts.

Cheers!

### Share this:

  * [ Share on X (Opens in new window) X ](https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/?share=facebook)
  * 

Like Loading...

### _Related_

Posted by[Lady Secspeare](https://ladysecspeare.wordpress.com/author/ladysecspeare/)[April 5, 2020April 5, 2020](https://ladysecspeare.wordpress.com/2020/04/05/how-a-simple-csrf-attack-turned-into-a-p1-level-bug/)Posted in[Uncategorized](https://ladysecspeare.wordpress.com/category/uncategorized/)Tags:[Bug Bounty](https://ladysecspeare.wordpress.com/tag/bug-bounty/), [Bug Bounty Hunting](https://ladysecspeare.wordpress.com/tag/bug-bounty-hunting/), [Bugcrowd](https://ladysecspeare.wordpress.com/tag/bugcrowd/), [Bypassing CSRF](https://ladysecspeare.wordpress.com/tag/bypassing-csrf/), [Cross-site Request Forgery](https://ladysecspeare.wordpress.com/tag/cross-site-request-forgery/), [CSRF](https://ladysecspeare.wordpress.com/tag/csrf/), [CSRF Bypass](https://ladysecspeare.wordpress.com/tag/csrf-bypass/), [P1](https://ladysecspeare.wordpress.com/tag/p1/)

##  Published by Lady Secspeare 

Spearing the Security for Good [ View more posts ](https://ladysecspeare.wordpress.com/author/ladysecspeare/)

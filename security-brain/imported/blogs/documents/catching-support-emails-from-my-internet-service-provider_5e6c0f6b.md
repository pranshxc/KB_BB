---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-21_catching-support-emails-from-my-internet-service-provider.md
original_filename: 2019-06-21_catching-support-emails-from-my-internet-service-provider.md
title: Catching support emails from my internet service provider
category: documents
detected_topics:
- sso
- command-injection
- business-logic
tags:
- imported
- documents
- sso
- command-injection
- business-logic
language: en
raw_sha256: 5e6c0f6b4c1f0118318cba7fb74eebe467f26ff62f928d7bc107757ca0a8fa7b
text_sha256: 1b50ff31523a39f10e98b05dcd788f7941bfe50099f79082f83a714f4ff6895b
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Catching support emails from my internet service provider

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-21_catching-support-emails-from-my-internet-service-provider.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `5e6c0f6b4c1f0118318cba7fb74eebe467f26ff62f928d7bc107757ca0a8fa7b`
- Text SHA256: `1b50ff31523a39f10e98b05dcd788f7941bfe50099f79082f83a714f4ff6895b`


## Content

---
title: "Catching support emails from my internet service provider"
page_title: "Catching support emails from my internet service provider | Blog"
url: "https://blog.lent.ink/post/klanteservice/"
final_url: "https://blog.lent.ink/post/klanteservice/"
authors: ["Sander Lentink"]
programs: ["T-Mobile"]
bugs: ["Logic flaw"]
publication_date: "2019-06-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5192
---

# [Blog ](https://blog.lent.ink/)

[#whitehat](/tags/whitehat)

## June 21, 2019

# Catching support emails from my internet service provider

We all assume you cannot register admin, [postmaster](https://webmasters.stackexchange.com/questions/2030/should-i-set-up-standard-email-accounts-what-are-they) or support@yourisp.com, however, a Dutch provider let me do a similar thing. In Dutch we had an old spelling and a new one; pannekoek (old) and pannenkoek (new), which means pancake. So I tried to register klanteservice instead of klantenservice, which was still available!

![vodafonethuis](/img/vodafonethuis.jpg)

I didn’t look at it for years, my ISP changed its name, making me even catch more emails! The emails I was able to catch were klanteservice at vodafonethuis.nl (old name), tmobilethuis.nl and t-mobilethuis.nl.

![tmobilethuis](/img/tmobilethuis.jpg)

This issue cannot be credited to the ISP, but to the lack of Dutch of the customers that made this mistake. However, this typo is easily made, just like suport instead of support.

### Contact with ISP

Via [Hackerone](https://hackerone.com/tmobile) I found an address to contact them.

When I contacted them (6:30PM);
  
  
  Your customers sent sensitive data to a false support email address on your platform.
  I was able to register klanteservice instead of klantenservice.
  My advice is to:
  1) verify your blacklist of email addresses people can register
  2) strip me (the user) of that email address
  3) let customer support go over those unanswered emails
  

they responded very quickly (7:56PM):
  
  
  Thank you for reaching out.
  You have reached the T-Mobile USA; the issue below is with the T-Mobile/Netherlands.
  We have forwarded your communication to them ( REDACTED ) and requested that they contact you.
  Thank you for engaging in responsible disclosure and helping us keep T-Mobile customers, in the USA and in Europe, safe.
  

This response brings a smile to my face, a company that understands the concept of white hat hackers.

Their Dutch CERT team handled it great and sent me some gifts.

![tmobilegift](/img/tmobile-thankyou.png)

### Similar articles:

  * [Form manipulation](/post/vimexx/)

Blog by [lent.ink](https://lent.ink)

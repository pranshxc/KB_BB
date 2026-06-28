---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-01_paypal-mobile-verification-and-payment-restrictions-bypass.md
original_filename: 2017-06-01_paypal-mobile-verification-and-payment-restrictions-bypass.md
title: Paypal Mobile Verification And Payment Restrictions Bypass
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: f065cae642db6abb5ddfe231a9546572c4a471a3d16665bd270bd12b2ca13ac1
text_sha256: f506f2ce9517b81a95c26079c3905109900803a0c4347efbe8c7c578b74247fd
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Paypal Mobile Verification And Payment Restrictions Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-01_paypal-mobile-verification-and-payment-restrictions-bypass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f065cae642db6abb5ddfe231a9546572c4a471a3d16665bd270bd12b2ca13ac1`
- Text SHA256: `f506f2ce9517b81a95c26079c3905109900803a0c4347efbe8c7c578b74247fd`


## Content

---
title: "Paypal Mobile Verification And Payment Restrictions Bypass"
page_title: "Paypal Mobile Verification And Payment Restrictions Bypass - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2017/06/paypal-mobile-verification-and-payment.html"
final_url: "https://www.rafaybaloch.com/2017/06/paypal-mobile-verification-and-payment.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Paypal"]
bugs: ["Logic flaw"]
publication_date: "2017-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6190
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg837iW4RrgHfPejz8tv8pgS49zcdm6iCMc73hq5SWDoYkuFuuaBr-MQmjnN2eTR0VcAL7p3llioTiAH4BmQUfFP8N8MtTM3kRqsu9w-iwbHpADnL7g5FVoxDyxaNUlVtWUuu089RjzaWg/s400/download.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg837iW4RrgHfPejz8tv8pgS49zcdm6iCMc73hq5SWDoYkuFuuaBr-MQmjnN2eTR0VcAL7p3llioTiAH4BmQUfFP8N8MtTM3kRqsu9w-iwbHpADnL7g5FVoxDyxaNUlVtWUuu089RjzaWg/s1600/download.jpg)

  
In this post, i would like to share a very simple logic flaw I found earlier this year I have found a way to circumvent mobile verification by utilizing a different portal for logging into a paypal account. The flaw lies in the fact that paypal does not perform two step verification/authorization checks on all different portals that are used to log into a paypal account. Ideally, there should be a centralized authentication mechanism to authenticate the user or else additional authorization checks have to be applied to all different portals that are used to log into paypal ccount.  
  
In this case, We could use the mobile activation page to log into the paypal account without happen to use a mobile phone.  
  
**<https://www.paypal.com/us/cgi-bin/?cmd=_mobile-activate-outside>**  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimr3ZWZ49Bi5pPbSmhNkCJtddJAhpbCVC8OuyLzUG6J_Cl-jFZk3HD2tRUkyPlKnwXs1Z1RmnOHJrctVmH9nWyx_BstEz9eRgAsv4486p5PHgoOLMmi-_QktdZgdQhyphenhyphenXyvz2ik7ULE5JQ/s640/sss.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimr3ZWZ49Bi5pPbSmhNkCJtddJAhpbCVC8OuyLzUG6J_Cl-jFZk3HD2tRUkyPlKnwXs1Z1RmnOHJrctVmH9nWyx_BstEz9eRgAsv4486p5PHgoOLMmi-_QktdZgdQhyphenhyphenXyvz2ik7ULE5JQ/s1600/sss.png)

  

####  Demonstration

  
  
Unfortunately, the bug was marked as duplicate so it was not eligible for a bounty, however that really doesn't matter as the fun and the learning is more important. However, there are still other ways to circumvent mobile verification, however i did not wish to report.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5fFRvfHZwdf7VzaI32pGNJmd0VA2n6e0_RXlOAWbCxQXFYNg-40JUQkrkHut1IK8qW2Hd_JcNGmjBfyAE5KAns6LjDNwOkPh513ICO5ajl_nBFr7GvKLCXI7V8zfpRz3BO3HsMmvhhFQ/s640/fix.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5fFRvfHZwdf7VzaI32pGNJmd0VA2n6e0_RXlOAWbCxQXFYNg-40JUQkrkHut1IK8qW2Hd_JcNGmjBfyAE5KAns6LjDNwOkPh513ICO5ajl_nBFr7GvKLCXI7V8zfpRz3BO3HsMmvhhFQ/s1600/fix.png)

####  Bypassing Payment Restrictions

After you have bypassed paypal might restrict you from transferring funds to another account, however there is a simple way of bypassing it as well, all you have to do is to create a donation button or any other payment button from paypal and directly use that to transfer money, paypal does not enforce any restriction on it.

####  Example

**[https://www.paypal.com/id/cgi-bin/webscr?cmd=_flow&SESSION=OvGwImW-aZGi7_Jf-oBOYlXFljX6KfnUMxeUoxyow7Woq8ZZYb7SihFpKQy&dispatch=50a222a57771920b6a3d7b606239e4d529b525e0b7e69bf0224adecfb0124e9b61f737ba21b08198d1a93361f052308ac20c1249d8113f4c](https://www.paypal.com/id/cgi-bin/webscr?cmd=_flow&SESSION=OvGwImW-aZGi7_Jf-oBOYlXFljX6KfnUMxeUoxyow7Woq8ZZYb7SihFpKQy&dispatch=50a222a57771920b6a3d7b606239e4d529b525e0b7e69bf0224adecfb0124e9b61f737ba21b08198d1a93361f052308ac20c1249d8113f4c)**

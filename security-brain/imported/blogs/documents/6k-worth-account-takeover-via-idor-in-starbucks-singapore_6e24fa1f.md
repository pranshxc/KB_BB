---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-07_6k-worth-account-takeover-via-idor-in-starbucks-singapore.md
original_filename: 2020-10-07_6k-worth-account-takeover-via-idor-in-starbucks-singapore.md
title: 6k$ Worth Account Takeover via IDOR in Starbucks Singapore
category: documents
detected_topics:
- mobile-security
- sso
- idor
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- mobile-security
- sso
- idor
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 6e24fa1f1ae8397bd1e5ecaf6d4178789b38dac4f5711fc213b597a969a4f4fa
text_sha256: ec95a9bfaa1fe836ba30d7e591abca7d1f5de569ad704b5005e0d224e7fac1b9
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 6k$ Worth Account Takeover via IDOR in Starbucks Singapore

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-07_6k-worth-account-takeover-via-idor-in-starbucks-singapore.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, idor, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6e24fa1f1ae8397bd1e5ecaf6d4178789b38dac4f5711fc213b597a969a4f4fa`
- Text SHA256: `ec95a9bfaa1fe836ba30d7e591abca7d1f5de569ad704b5005e0d224e7fac1b9`


## Content

---
title: "6k$ Worth Account Takeover via IDOR in Starbucks Singapore"
page_title: "6k$ Worth Account Takeover via IDOR in Starbucks Singapore - Kamil Onur Özkaleli as ko2sec"
url: "http://www.kamilonurozkaleli.com/posts/starbucks-singapore-account-takeover/"
final_url: "http://www.kamilonurozkaleli.com/posts/starbucks-singapore-account-takeover/"
authors: ["Kamil Onur Özkaleli (@ko2sec)"]
programs: ["Starbucks"]
bugs: ["IDOR", "Account takeover"]
bounty: "6,000"
publication_date: "2020-10-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4214
---

# [Kamil Onur Özkaleli as ko2sec](http://www.kamilonurozkaleli.com/)

## This blog is mostly about security writeups and research articles.

[__](https://github.com/ko2sec "Github")[__](https://twitter.com/ko2sec "Twitter")[__](https://linkedin.com/kamilonurozkaleli "LinkedIn")

  * [Home](/)
  * [All posts](/posts)
  * [Tags](/tags)

# 6k$ Worth Account Takeover via IDOR in Starbucks Singapore

Posted at — Oct 7, 2020

### **Recon**

While browsing Starbucks Singapore, I noticed a page loaded with content from a 3rd party site. Let’s call this site _example.com_ in order not to disclose it. When I did some research on this site, I saw the same login page on _card.starbucks.com.sg_ in the directory example.com/starbucks, and at this point I had two possibilities.

  1. This application can be an environment where current developments of _card.starbucks.com.sg_ are made and tested.
  2. Or it may have been used as an old test environment and is in an idle state.

Both possibilities increased the probability of a bug here, but the main problem is that I did not know whether a bug I will find here would affect the production environment. To understand this, I created a user account at card.starbucks.com.sg and tried to log into example.com/starbucks with this account. BINGO! I was able to successfully login with the account I just created. Both applications seemed to be using the same authentication mechanism.

![Scheme-1, both applications are using same database table.](/images/starbucks-1.png)

### **Exploitation**

From this point I browsed example.com/starbucks and discovered an endpoint which does not exist in the production app. The POST data this endpoint received was as follows.

`email=hacker@hacker.com`

When I write the email address of the account I want to takeover in the email parameter here and send a request, I saw the partial information of the account belonging to that email address on my profile page. I could not fully takeover the account yet, and my password change request was not successful due to the invalid CSRF token generated in this application.

To get around this, I copied the PHPSESSID cookie value from example.com/starbucks to card.starbucks.com.sg and BOOM! I was able to see all the information belongs to victim in the production environment, the valid CSRF tokens generated here allowed me to change the password and I was able to completely takeover an account whose e-mail address I know.

### **Impact**

Except for seeing all personal information belonging to users and completely taking over the accounts, if there is a loaded credit in the user account, these credits can be spent in Starbucks stores via the mobile application.

### **Multiplying the Reward**

I came across two other test environments on example.com. Let’s call them _example.com/starbucks2_ and _example.com/starbucks3_. With my account at card.starbucks.com.sg, I was not able to login to either test environment. example.com/starbucks2 did not allow me to create a new account, so I tried my luck at example.com/starbucks3 and successfully created a new account. Things get a little complicated here, I will try to explain it as simply as possible.

I think the applications example.com/starbucks2 and example.com/starbucks3 were using test tables, so users in production could not login in these applications.

With the account I created at example.com/starbucks3, I was able to log in to example.com/starbucks2, but not card.starbucks.com.sg. However, the PHPSESSID I copied from example.com/starbucks2 was valid on card.starbucks.com.sg and I could use that account. Considering all the scenarios, I created a chain here as follows:

  1. Create a dummy account with the victim’s email address at example.com/starbucks3. (Add to testusers table.)
  2. At example.com/starbucks2, associate the account for that email with your own account via the same endpoint. (Associate the PHPSESSID with the email in the testusers table.)
  3. Copy the PHPSESSID to card.starbucks.com.sg and takeover. (Takeover the real account of the same email address in the production users table.)

![Scheme-2, relations between applicaitons and tables.](/images/starbucks-2.png)

May 17th - Report Submitted  
May 18th - Triaged  
May 20th - Rewarded $4000 bounty  
Jun 17th - Rewarded $2000 bounty as 1.5x multiplier

You can find Hackerone report [here](https://hackerone.com/reports/876300).  
If you liked this article you can follow me on [Twitter](https://www.twitter.com/ko2sec).

  * [bug bounty](/tags/bug-bounty)
  * [starbucks](/tags/starbucks)

kamilonurozkaleli.com © all rights reserved. | [Ezhil theme](https://github.com/vividvilla/ezhil) | Built with [Hugo](https://gohugo.io)

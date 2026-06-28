---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-12-30_how-i-discovered-a-1000-open-redirect-in-facebook.md
original_filename: 2014-12-30_how-i-discovered-a-1000-open-redirect-in-facebook.md
title: How I discovered a 1000$ open redirect in Facebook
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: b0ba8041764936c1ab7a5d6b8f8fee6441fd65b92738e30546c7837e7bc2b906
text_sha256: 80586f5d8f3179837d20456996c5f4f330c82b3570de8052841a5b064e21179b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I discovered a 1000$ open redirect in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-12-30_how-i-discovered-a-1000-open-redirect-in-facebook.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `b0ba8041764936c1ab7a5d6b8f8fee6441fd65b92738e30546c7837e7bc2b906`
- Text SHA256: `80586f5d8f3179837d20456996c5f4f330c82b3570de8052841a5b064e21179b`


## Content

---
title: "How I discovered a 1000$ open redirect in Facebook"
page_title: "How I discovered a $1000 open redirect in Facebook – Yassine Aboukir – Application security engineering, consulting and bug bounties"
url: "https://www.yassineaboukir.com/blog/how-I-discovered-a-1000$-open-redirect-in-facebook/"
final_url: "https://www.yassineaboukir.com/blog/how-I-discovered-a-1000$-open-redirect-in-facebook/"
authors: ["Yassine Aboukir (@Yassineaboukir)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
bounty: "1,000"
publication_date: "2014-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6352
---

# How I discovered a $1000 open redirect in Facebook

Yassine Aboukir · December 30, 2014

[bug bouties](/categories/#bug bouties) [appsec](/categories/#appsec)

I am not really used to writing about vulnerabilities I discovered but this time is worth it since it is a bit exceptional for me as it is about a security issue found on Facebook.

As you have read in the title, Facebook is vulnerable to an open redirect because some parameters ddin’t not fully validate the input allowing an attacker to redirect the victim to a malicious page. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it.

## Vulnerable endpoints
  
  
  https://www.facebook.com/ads/manage/log/?uri=xxxxx&event=view_power_editor&ad_account_id=1
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=xxxxx
  

Facebook has, indeed, implemented some protection against open redirection since I was not able to perform the attack using some common techniques like you the ones below :
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://www.evil.com/
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=../evil.com
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://l.facebook.com/l.php?u=https://evil.com
  

None of the above bypass techniques worked. I was about to give up when I noticed in my Twitter feed some Facebook shortned links that looked like: `https://fb.me/7kFH9QAMH` (redirects to evil.com). These links were automatically generated if you link your facebook account with Twitter so I quickly got back to my testing and tried to bypass the protection using the shortned link which worked perfectly.

After reporting it to facebook on `13/12/2014` it was fixed on `17/12/2014` and Facebook rewarded me with a **500$** bounty for it.

## Proof Of Concept 1:
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://fb.me/7kFH9QAMH
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://l.facebook.com/l.php?u=https:// fb.me/7kFH9QAMH
  

You would be redirected to `evil.com`.

I went to back to check if somehow I could bypass again the protection. So, I took a deep look at the `fb.me` domain and I found some subdomains like `https://on.fb.me` for facebook pages and I tried to guess other valid subdomains. Subsequently, I found this valid subdomain `https://d.fb.me/7kFH9QAMH` which worked perfectly allowing me to bypass the protection.

## Proof Of Concept 2:
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://d.fb.me/7kFH9QAMH
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://d.fb.me/7kFH9QAMH
  

I quickly escalated the bug to Facebook security team on `22/12/2014` and they fixed on `24/12/2014` but they decided not to reward it because it similar to the original one. I was not happy with their decision, so I managed to find a another way to bypass the protection again, hopefully this time they’ll reconsider awarding a bounty for my efforts.

I tried again some new tricks but they all failed then, unintentionally, I added the `www` to the shortned Facebook link such as `https://www.fb.me/7kFH9QAMH` and the open redirect worked just fine. With other words, I bypassed Facebook previous fix once again.

## Proof Of Concept 3 :
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://www.fb.me/7kFH9QAMH
  
  
  
  https://www.facebook.com/browsegroups/addcover/log/?groupid=1&groupuri=https://www..fb.me/7kFH9QAMH
  

I followed-up with the security engineer who escalated the bug on `24/12/2014` and it got fixed on `30/12/2014` and, luckily, Facebook decided to reward **500$** for it.

Share: [Twitter](http://twitter.com/share?text=How I discovered a $1000 open redirect in Facebook&url=https://www.yassineaboukir.com//blog/how-I-discovered-a-1000$-open-redirect-in-facebook/), [Facebook](https://www.facebook.com/sharer.php?u=https://www.yassineaboukir.com//blog/how-I-discovered-a-1000$-open-redirect-in-facebook/)

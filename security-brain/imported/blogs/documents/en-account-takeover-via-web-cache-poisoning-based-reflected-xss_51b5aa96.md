---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-26_en-account-takeover-via-web-cache-poisoning-based-reflected-xss.md
original_filename: 2020-12-26_en-account-takeover-via-web-cache-poisoning-based-reflected-xss.md
title: EN | Account Takeover via Web Cache Poisoning based Reflected XSS
category: documents
detected_topics:
- xss
- command-injection
- race-condition
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- race-condition
- clickjacking
language: en
raw_sha256: 51b5aa960fcc2924ad5a0352a25d96ed9c4076f84e5de146f386f720c0d43c7e
text_sha256: 1d70f827dcc0269ce8d08e682aec9bbbcaf2024a4ab0326390d00db2a6742c17
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# EN | Account Takeover via Web Cache Poisoning based Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-26_en-account-takeover-via-web-cache-poisoning-based-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, race-condition, clickjacking
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `51b5aa960fcc2924ad5a0352a25d96ed9c4076f84e5de146f386f720c0d43c7e`
- Text SHA256: `1d70f827dcc0269ce8d08e682aec9bbbcaf2024a4ab0326390d00db2a6742c17`


## Content

---
title: "EN | Account Takeover via Web Cache Poisoning based Reflected XSS"
page_title: "EN | Account Takeover via Web Cache Poisoning based Reflected XSS > Lütfü Mert Ceylan"
url: "https://lutfumertceylan.com.tr/posts/acc-takeover-web-cache-xss/"
final_url: "https://lutfumertceylan.com.tr/posts/acc-takeover-web-cache-xss/"
authors: ["Lütfü Mert Ceylan (@lutfumertceylan)"]
bugs: ["Reflected XSS", "Web cache poisoning", "Account takeover"]
publication_date: "2020-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4050
---

# EN | Account Takeover via Web Cache Poisoning based Reflected XSS

December 26, 2020

![](https://lutfumertceylan.com.tr/images/web-cache.png)  

Firstly, it’s nice to publish my last write-up this year. In June of this year, I found a Reflected XSS vulnerability in a video-game company. Then, I realized that this server is caching the weak parameter’s value. In this way, I incresead the probability of triggering this vulnerability and escalated to Account Takeover weakness. Later, I reported the vulnerability and they fixed this vulnerability. Also, they rewarded me with a €€€ bounty. I can’t say the company, because I have no permission to disclose them.

### Recon

I discovered a Reflected XSS with a basic payload execution  
(`1</script><svg/onload=confirm("document.cookie")>`) in the “language” input. I thought this vuln was a normal Reflected XSS. As usual, the vulnerability was triggered when going to the vulnerable URL and user session was stolen with a suitable payload. Because, the session cookie did not have any `httponly` or `secure` flags.

For those who don’t know what httponly and secure flag is:

> `HttpOnly:` An HttpOnly Cookie is a tag added to a browser cookie that prevents client-side scripts from accessing data. _[from CookiePro]_  
> 

> `secure:` When a secure flag is used, then the cookie will only be sent over HTTPS, which is HTTP over SSL/TLS. When this is the case, the attacker eavesdropping on the communication channel from the browser to the server will not be able to read the cookie (HTTPS provides authentication, data integrity and confidentiality). _[from infosecinstitute]_

### Impact Escalation with Web Cache Poisoning!

But then, I saw that each page also contains `language` parameter. And I realized that the value of this parameter is put in the web cache. So this means:

> Even if the vulnerability was triggered just once, the payload would be embedded in all pages of this site.  
> 

Actually, this does not cached entire page like standart Web Cache Poisoning weaknesses, only the part where the payload is embedded is cached. But of course, this is still a web cache poisoning. This scheme prepared by Detectify may be useful for you.

![](https://blog.detectify.com/wp-content/uploads/2020/07/web_cache_poisoning.png)  

Also, you can read Dedectify’s article: <https://blog.detectify.com/2020/07/28/do-you-trust-your-cache-web-cache-poisoning-explained/>

### And a simple Account Takeover

As we mentioned at the beginning, there was no `httponly` and `secure` flag or a `Content-Security-Policy (CSP)` that can block payload on the site.

![](/images/xsscac.png)  

So admittedly, the system was already very weak.

### Attack scenario with Web Cache Poisoning

With Web Cache Poisoing, we can create a simple attack scenario. For example, if the victim sends a request in the background from an external page to the vulnerable URL in several ways(like embedding the vulnerable url in a picture), The payload is cached in the web, and the payload is triggered each time the victim goes the target site.

I reported the vulnerability, and they agreed that it should be fixed.

If you want to learn Web Cache Poisoning:  
<https://portswigger.net/web-security/web-cache-poisoning>

### The end and results :

17 June 2020 - Report sent  
18 June 2020 - Confirmed  
24 June 2020 - I was awarded a €€€ bounty  

**__Tags:** [account takeover](https://lutfumertceylan.com.tr/tags/#account-takeover),  [bugbounty](https://lutfumertceylan.com.tr/tags/#bugbounty),  [hack](https://lutfumertceylan.com.tr/tags/#hack),  [poc](https://lutfumertceylan.com.tr/tags/#poc),  [reflected xss to account takeover](https://lutfumertceylan.com.tr/tags/#reflected-xss-to-account-takeover),  [reflected xss](https://lutfumertceylan.com.tr/tags/#reflected-xss),  [web cache poisoning to account takeover](https://lutfumertceylan.com.tr/tags/#web-cache-poisoning-to-account-takeover),  [web cache poisoning](https://lutfumertceylan.com.tr/tags/#web-cache-poisoning),  [write-up](https://lutfumertceylan.com.tr/tags/#write-up)

#### Share on

[ __Twitter](https://twitter.com/intent/tweet?text=https://lutfumertceylan.com.tr/posts/acc-takeover-web-cache-xss/ "Share on Twitter") [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://lutfumertceylan.com.tr/posts/acc-takeover-web-cache-xss/ "Share on Facebook") [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://lutfumertceylan.com.tr/posts/acc-takeover-web-cache-xss/ "Share on LinkedIn") [Previous](https://lutfumertceylan.com.tr/posts/clickjacking-acc-takeover-drag-drop/ "EN | Clickjacking to Account Takeover via Drag&Drop ") [Next](https://lutfumertceylan.com.tr/posts/race-condition-limit-bypass/ "EN | Race Condition to Users Limit Bypass in Add User Function ")

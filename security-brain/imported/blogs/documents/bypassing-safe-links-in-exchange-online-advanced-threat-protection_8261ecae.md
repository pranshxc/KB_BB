---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-16_bypassing-safe-links-in-exchange-online-advanced-threat-protection.md
original_filename: 2017-03-16_bypassing-safe-links-in-exchange-online-advanced-threat-protection.md
title: Bypassing Safe Links in Exchange Online Advanced Threat Protection
category: documents
detected_topics:
- jwt
- command-injection
- otp
- mobile-security
- supply-chain
tags:
- imported
- documents
- jwt
- command-injection
- otp
- mobile-security
- supply-chain
language: en
raw_sha256: 8261ecae26f5d56d6919aa3788f7c36a3b9384dbe6bf8ac88f88078609b0f021
text_sha256: 0416cbbb2427fdf10be7a5e72a5c279777febc1d67efa85679e0579fc38921c7
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Safe Links in Exchange Online Advanced Threat Protection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-16_bypassing-safe-links-in-exchange-online-advanced-threat-protection.md
- Source Type: markdown
- Detected Topics: jwt, command-injection, otp, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8261ecae26f5d56d6919aa3788f7c36a3b9384dbe6bf8ac88f88078609b0f021`
- Text SHA256: `0416cbbb2427fdf10be7a5e72a5c279777febc1d67efa85679e0579fc38921c7`


## Content

---
title: "Bypassing Safe Links in Exchange Online Advanced Threat Protection"
page_title: "Bypassing Safe Links in Exchange Online Advanced Threat Protection – Mikail's Blog"
url: "https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/"
final_url: "https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/"
authors: ["Mikail Tunç (@emtunc)"]
programs: ["Microsoft"]
bugs: ["Open redirect"]
publication_date: "2017-03-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6208
---

Categories 

[Tech](https://emtunc.org/blog/category/tech/)

# Bypassing Safe Links in Exchange Online Advanced Threat Protection

  * Post author  By [Mikail](https://emtunc.org/blog/author/e-mikail-t/)
  * Post date  [March 16, 2017](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/)
  * [2 Comments on Bypassing Safe Links in Exchange Online Advanced Threat Protection](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/#comments)

In this article I will go through my findings and analysis on the **[Safe Links](https://technet.microsoft.com/en-us/library/mt148491\(v=exchg.150\).aspx)** feature of Microsoft’s Office 365 Exchange Online Advanced Threat Protection.

Essentially what Safe Links does is it rewrites all URLs in in-bound e-mails that pass through the Exchange Online Protection platform. So if you send an e-mail to an organization with Safe Links enabled then the e-mail will look like this (original):
  
  
  Hello Bob,
  This is the link I was talking to you about: https://example.com

The URL gets rewritten to look like this (passed through Safe Links):
  
  
  Hello Bob,
  This is the link I was talking to you about: https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fexample.com/[...]

### Bypass Method 1

It is not uncommon for organizations to add their own domains to the Safe Links whitelist policy. This is done for one of many reasons… either you trust your own domains or you don’t want to inconvenience staff when sending documents internally imagine sending a .pdf on your corporate site to 1,000’s of staff – a significant portion would click the link and be presented with this page:

[![](https://emtunc.org/blog/wp-content/uploads/2017/03/2017-03-16-11_25_38-Office365.png)](https://emtunc.org/blog/wp-content/uploads/2017/03/2017-03-16-11_25_38-Office365.png)

This bypass exploits the whitelisted domains in the Safe Links policy by using URL obfuscation techniques.

Imagine you have Example Ltd which owns the domain example.com. The administrators of example.com have added the example.com domain to the whitelist in their Safe Links policy such that e-mails containing the URL example.com don’t get re-written by EOP.

Using a URL obfuscation technique like the below can trick EOP into thinking that the domain is whitelisted when in fact it isn’t:
  
  
  Hello Bob,
  This is the link I was talking to you about: https://[[email protected]](/cdn-cgi/l/email-protection)/malware.exe

As you can see, simply obfuscating the URL by posting bogus credentials tricks Safe Links in to thinking that the domain is example.com instead of emtunc.org/malware.exe.

Another obfuscation technique is:
  
  
  Hello Jane in finance,
  URGENT - please see outstanding invoice due to us: https://example.com.emtunc.org/malware.exe

Here the  _advanced_ threat protection isn’t checking the entire domain – instead it is tricked by a basic obfuscation technique of inserting the white-listed domain as a subdomain of the malicious domain.

### Bypass Method 2

With this technique, an attacker could simply block or re-direct requests from the Exchange Online Protection infrastructure – yup, it’s as simple as that. It’s less of a vulnerability and more of a non-ideal configuration.

Helpfully, Microsoft makes the EOP IP ranges [available online](https://technet.microsoft.com/en-us/library/dn163583\(v=exchg.150\).aspx) so all you need to do is block those ranges on your webserver with some .htaccess rules.

Even if the IP ranges weren’t available online, the EOP requests contain absolutely no headers which makes it very easy to distinguish EOP traffic and genuine traffic.

This is what genuine traffic looks like (notice the browser headers are present):
  
  
  1.2.3.4 - - [23/Feb/2017:11:58:26 +0000] "GET /blog/02/2017/ninite-appsheet-patching-just-got-easier/ HTTP/1.1" 200 18347 "android-app://com.google.android.gm" "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"

This is what EOP requests look like (notice how no headers are sent so easy to distinguish from legitimate traffic):
  
  
  40.107.196.15 - - [13/Jan/2017:12:24:03 +0000] "GET /malware.exe HTTP/1.1" 404 406 "-" "-"

### Timeline

  * **15/01/2017** – First reported
  * **20/01/2017** – I requested an update
  * **01/02/2017** – I requested an update
  * **07/01/2017** – MSRC claimed a ‘bug’ caused my replies to be missed. MSRC asked for some further clarifications which I addressed
  * **15/02/2017** – I requested an update
  * **23/02/2017** – I notified MSRC that I will be publishing this article on the 27th
  * **24/02/2017** – I was asked to delay the publishing of this post and notified that a new MSRC case was created
  * **15/03/2017 –** MSRC advised that the issue doesn’t _“meet the security servicing bug bar”_ and that they are closing the case
  * **16/03/2017 –** Published

### Share this:

  * [ Email a link to a friend (Opens in new window) Email ](/cdn-cgi/l/email-protection#4d723e382f27282e397068780f1e252c3f2829687f7d1d223e39687809687f7d0f343d2c3e3e24232a687f7d1e2c2b28687f7d012423263e687f7d2423687f7d08352e252c232a28687f7d022321242328687f7d0c293b2c232e2829687f7d19253f282c39687f7d1d3f2239282e392422236b6e7d7e75762f222934702539393d3e687e0c687f0b687f0b28203938232e63223f2a687f0b2f21222a687f0b7d7e687f0b7f7d7c7a687f0b2f343d2c3e3e24232a603e2c2b2860212423263e6028352e252c232a2860222321242328602c293b2c232e28296039253f282c39603d3f2239282e39242223687f0b6b6e7d7e75763e252c3f287028202c2421)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=twitter)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=jetpack-whatsapp)
  * [ Share on Reddit (Opens in new window) Reddit ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=reddit)
  * [ Share on Telegram (Opens in new window) Telegram ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=telegram)
  * [ Share on Facebook (Opens in new window) Facebook ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/?share=facebook)
  * [ Print (Opens in new window) Print ](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/#print?share=print)
  * 

  * Tags  [ATP](https://emtunc.org/blog/tag/atp/), [exchange online](https://emtunc.org/blog/tag/exchange-online/), [office 365](https://emtunc.org/blog/tag/office-365/)

* * *

[ ← Ninite Appsheet – Patching Just Got Easier ](https://emtunc.org/blog/02/2017/ninite-appsheet-patching-just-got-easier/) [ → JWT Refresh Token Manipulation ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/)

* * *

##  2 replies on “Bypassing Safe Links in Exchange Online Advanced Threat Protection” 

![](https://secure.gravatar.com/avatar/7f4cbfa78a2a478d2f3e3e28b44d25d3f9f4eb0689ce9824436e478940e79baa?s=120&d=monsterid&r=g)Johnsays:

[October 20, 2017 at 3:37 PM](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/#comment-5296)

How would you rate the feature in it’s current state? I did not see a big update on the service as a result of your publication, but I could have overlooked it. Thanks for sharing your experiences and info.

![](https://secure.gravatar.com/avatar/a45fb5bbd774488115a9ba2a80e5e830d6f2cb2db47ed5f68d8f84dba88df6af?s=120&d=monsterid&r=g)Mikailsays:

[October 21, 2017 at 8:51 PM](https://emtunc.org/blog/03/2017/bypassing-safe-links-exchange-online-advanced-threat-protection/#comment-5297)

I haven’t used Office 365 for a while now so I honestly couldn’t tell you, however I did see at least one additional bypass technique published since my blog post.  
I certainly wouldn’t discourage anyone from using ATP as it’s all about defence in depth which I strongly believe in; it’s just a shame they couldn’t prevent some basic bypasses… or care enough to fix them when they were reported 🙂

By Post Author

* * *

Comments are closed.

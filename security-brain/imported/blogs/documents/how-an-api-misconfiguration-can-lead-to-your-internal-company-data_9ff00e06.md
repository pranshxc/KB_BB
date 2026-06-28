---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-12_how-an-api-misconfiguration-can-lead-to-your-internal-company-data.md
original_filename: 2020-07-12_how-an-api-misconfiguration-can-lead-to-your-internal-company-data.md
title: How An API Misconfiguration Can Lead To Your Internal Company Data
category: documents
detected_topics:
- api-security
- xss
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- api-security
- xss
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: 9ff00e06e1c639f006fc0f5bfcbd8ca310c84970e4d0c4c1b5e014406f6927a5
text_sha256: 07e7221dbf722a57b3774c3e0672509a20160a5656969516714e2d2957d3af03
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# How An API Misconfiguration Can Lead To Your Internal Company Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-12_how-an-api-misconfiguration-can-lead-to-your-internal-company-data.md
- Source Type: markdown
- Detected Topics: api-security, xss, command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `9ff00e06e1c639f006fc0f5bfcbd8ca310c84970e4d0c4c1b5e014406f6927a5`
- Text SHA256: `07e7221dbf722a57b3774c3e0672509a20160a5656969516714e2d2957d3af03`


## Content

---
title: "How An API Misconfiguration Can Lead To Your Internal Company Data"
page_title: "Accessing internal company documents via misconfigured algolia API"
url: "https://www.secjuice.com/api-misconfiguration-data-breach/"
final_url: "https://www.secjuice.com/api-misconfiguration-data-breach/"
authors: ["Me9187 (@Me9187)"]
bugs: ["Information disclosure"]
publication_date: "2020-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4412
---

# How An API Misconfiguration Can Lead To Your Internal Company Data

How An API Misconfiguration Can Lead To Your Internal Company Data

  * [ ](/author/deleted/)

#### [Deleted](/author/deleted/)

Jul 12, 2020

[Tip Writer](https://ko-fi.com/secjuice)

![How An API Misconfiguration Can Lead To Your Internal Company Data](/content/images/size/w2000/2020/09/hack-2.png)

I came across this last year while doing reconnaissance for a bug bounty program, I assumed it was just another API which was meant to be public, but after digging deeper I found that a particular program was using the admin API key instead of the public search key, this led me to finding a large amount of internal documents for security policies, business operations and even slack messages. 

After finding the same misconfiguration on a few sites I bought a dataset that contained 20k+ hosts which were using algolia, where i kept finding the same misconfiguration & sensitive information being leaked through the API.

### What is Algolia

Algolia is a search API that powers the search function of over 50,000 sites, the Algolia API lets you set custom search suggestions where it uses a company defined index that is filled with content to be searched through. If the API is misconfigured and has the “listIndexes” permission this allows you to view all indexes that are available, sometimes this has included sensitive internal company documents, such as security policies and how to connect to VPN & internal systems. 

I also found documents relating to company business operations and personnel policies. There are other permissions which can also be damaging, the “editSettings” permission allows you to define javascript which is ran when search is used, as you can imagine this can be quite dangerous for a large site with a lot of traffic.

### How To Use 

The API is a simple REST API and the applicationID and key are within the source code - as they are meant to be public (but only with the search permission), the keys can also be found within mobile applications, sometimes you might find a higher privileged key in the mobile app.

You can view the permissions that a key has by capturing the search request or looking for “applicationID” in the source then sending a GET request to

 _[https://APPID-dsn.algolia.net/1/keys/APIKEY?x-algolia-application-id=APPID&x-algolia-api-key=***REDACTED***

This will return the permissions the key has in a json format. If the API is configured correctly it should only return the “search” permission or the key will be base64 encoded which means that its a "Secure Key" and you are unable to list permissions.

![](https://secjuice.com/content/images/2020/07/image-2.png)Misconfigured Algolia Search API

A list of permissions and other endpoints can be found on [https://www.algolia.com/doc/api-reference/api-methods/get-api-key/](https://secjuice.com/p/a8be3762-de7f-409a-8e30-c9f542ba2a79/A%20list%20of%20permissions%20and%20other%20endpoints%20can%20be%20found%20on%20https://www.algolia.com/doc/api-reference/api-methods/get-api-key/)

The most damaging permissions are

  * addObject: Allows adding/updating an object in the index. (Copying/moving indices are also allowed with this permission.)

  * deleteObject: Allows deleting an existing object.

  * deleteIndex: Allows deleting an index (will break search completely)

  * editSettings: Allows changing index settings. - this also allows you to run javascript when the search is used.

  * listIndexes: Allows listing all accessible indices.

  * logs: this will allow you to view the search logs, which can include IP Addresses and sensitive cookies.

## Impact

After identifying other sites which were using Algolia I discovered many of them shared the same misconfiguration and the most dangerous permission is the "editSettings" permission which allows you to set the JavaScript which is run when the search feature on the site is used.

For a large site with hundreds of thousands of daily visitors, this would've allowed an attacker to inject their own malicious code for stealing credentials, card information etc. I've also found companies who are using the search only API key in their site but are using the admin API key in their mobile apps.

XSS can be achieved with this request - if the key has the "editSettings" permission.
  
  
  curl --request PUT \
  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key=***REDACTED*** \
  --header 'x-algolia-application-id: <example-application-id>' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'

https://github.com/streaak/keyhacks#Algolia-API-key

  
I was curious as to what was causing so many developers to make this mistake as by default Algolia generates a search only API key for you to put in your sites. Then i saw this while i was browsing the documentation

![](https://secjuice.com/content/images/2020/07/image.png)

That's right, it’ll handily include your admin API key for you, in example code snippets, so you can copy and paste directly to your site, how thoughtful.

I’ve reported this to around 100 companies so far, including a large social platform, a large server hosting company & multiple large clothing stores. Sadly I can't disclose names yet as these were private programs.

![](https://lh4.googleusercontent.com/qJ_P2JHsaWU7tcOPY-Phv5v7p0LUxsTn94CRj-MDcZ0tTKa1jupYGBlShiSaYm3dby1CtQtBDZxgGwkGGoqMZrkY16c-kNNbGprkR16ADCJTyVUu9zfPIMf387pF6gEB-EurvPbM)![](https://lh5.googleusercontent.com/yrXZHIM9bgamRqF89UbcHigigXjH2sAaafDjSbSBcX1Jkpr8OG280JTVQcTp2I_P5AwJn_aiu-kEMlMwJI9iPgd7tdbe9LiZwkj_yMcIQ4N9WuwCXoZCfqmLH5QQyQtWmL-pnRgs)

### How to Fix?

In the Algolia dashboard make sure your search only key is a search only key by checking it only has the “search” permission, if not revoke the key and generate a new search only key. Algolia also has a feature to generate "Secure Keys" which may be worth exploring.

![](https://secjuice.com/content/images/2020/07/image-1.png)

**Mentions**

  * [Kushagra](https://twitter.com/xKushagra?ref=secjuice.com)
  * [rak1507](https://twitter.com/rak_1507?ref=secjuice.com)

![](https://secjuice.com/content/images/2020/09/hack-3.png)The awesome image used in this article is called Hacker Floor and was created by [Juan Casini](https://dribbble.com/juancasini?ref=secjuice.com).

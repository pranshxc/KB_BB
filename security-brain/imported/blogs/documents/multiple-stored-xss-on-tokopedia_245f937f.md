---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-19_multiple-stored-xss-on-tokopedia.md
original_filename: 2019-02-19_multiple-stored-xss-on-tokopedia.md
title: Multiple Stored XSS On Tokopedia
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 245f937ff0a9e283005b128308f1ce1a0cdfb735efc0a2d3a2bc09e63ce3bab8
text_sha256: e150693d6a53a8123ef0f18584cf5e1c7d9cd34ba00442c43316c2257f661011
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Stored XSS On Tokopedia

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-19_multiple-stored-xss-on-tokopedia.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `245f937ff0a9e283005b128308f1ce1a0cdfb735efc0a2d3a2bc09e63ce3bab8`
- Text SHA256: `e150693d6a53a8123ef0f18584cf5e1c7d9cd34ba00442c43316c2257f661011`


## Content

---
title: "Multiple Stored XSS On Tokopedia"
page_title: "Multiple Stored XSS On Tokopedia – Apapedulimu"
url: "https://apapedulimu.click/multiple-stored-xss-on-tokopedia/"
final_url: "https://apapedulimu.click/multiple-stored-xss-on-tokopedia/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["Tokopedia"]
bugs: ["Stored XSS", "Blind XSS"]
publication_date: "2019-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5401
---

![](https://apapedulimu.click/wp-content/uploads/2019/02/tokopedia-825x510.jpg)

# Multiple Stored XSS On Tokopedia

So, It’s just old bug who I have been reported around 2018. I’ll share what I found on Tokopedia. Just in case you need some article to go to sleep. But it’ll just short description and PoC Here it is :

## Stored XSS On Complain Product (Keterangan Bukti Field)

This vulnerable perform on feature complain product, When buyer not satisfied with the stuff who has been buy by buyer. Buyer can complain with upload some Image. And the **vulnerability is on Description** image field.

### PoC :

  1. Go to complain menu
  2. Upload some image
  3. Input Payload on description of image ( **< img src=x onerror=alert(document.domain)>** )
  4. Payload will be execute when user navigate to the resolution menu.

### Video :

## Stored XSS On Location Shop (m.tokopedia.com )

This vulnerable on **Location Shop Parameter** at <https://m.tokopedia.com/> . So, this bug is just set the location shop to payload. And when someone navigate to the Shop detail. It’ll pop up the XSS.

### PoC :

  1. Open The mobile apps Tokopedia
  2. Edit the location of shop to XSS payload ( **< img src=x onerror=alert(document.domain)>** )
  3. Open the location via browser

Video :

## Stored XSS via AngularJS Injection On Etalase Name

Vulnerability exist because Tokopedia install the AngularJs old version and not filtering the illegal character very well. So, I just Insert the payload of AngularJs Injection to Etalasane Name and XSS will be fired up.

### PoC :

  1. Go To Add product
  2. Set the Etalase Name to AngularJs Payload ( **{{‘a’.constructor.prototype.charAt=[].join;$eval(‘x=1} } };alert(document.domain)//’);}}** )
  3. Save, And Open the product

### Video :

## Blind XSS on CS System ( Tokocash )

Tokopedia have some CS system, use the salesforce application. And when having some discussion between Tokopedia & Salesforce, the root cause is on the Tokopedia Custom Code.

### PoC :

  1. Login Tokocash.com
  2. REquest new ticket with payload of XSS Hunter
  3. Wait for execute payload on XSSHunter Dashboard.

Actually I have found more Stored XSS, but sadly that’s mark as Duplicate. I just fresh Bug who has been marked as valid only.

Thanks! Get in touch with me on Twitter : [Apapedulimu](https://twitter.com/LocalHost31337)

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [February 19, 2019](https://apapedulimu.click/multiple-stored-xss-on-tokopedia/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Stored XSS](https://apapedulimu.click/tag/stored-xss/), [Tokopedia](https://apapedulimu.click/tag/tokopedia/), [XSS](https://apapedulimu.click/tag/xss/)

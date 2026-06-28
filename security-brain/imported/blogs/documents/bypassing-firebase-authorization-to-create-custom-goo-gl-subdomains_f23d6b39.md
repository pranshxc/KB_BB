---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-21_bypassing-firebase-authorization-to-create-custom-googl-subdomains.md
original_filename: 2018-09-21_bypassing-firebase-authorization-to-create-custom-googl-subdomains.md
title: Bypassing Firebase authorization to create custom goo.gl subdomains
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: f23d6b39dfa410c266040c2bb19ae65299343a56430d37469d4976ac643e8678
text_sha256: 6d6a9be979c05d179d73fed714ab1345f4736393245a3aec1839d9d09b4e71c3
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Firebase authorization to create custom goo.gl subdomains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-21_bypassing-firebase-authorization-to-create-custom-googl-subdomains.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `f23d6b39dfa410c266040c2bb19ae65299343a56430d37469d4976ac643e8678`
- Text SHA256: `6d6a9be979c05d179d73fed714ab1345f4736393245a3aec1839d9d09b4e71c3`


## Content

---
title: "Bypassing Firebase authorization to create custom goo.gl subdomains"
page_title: "Bypassing Firebase authorization to create custom app.goo.gl subdomains - Web Security Blog"
url: "https://websecblog.com/vulns/bypassing-firebase-authorization-to-create-custom-goo-gl-subdomains/"
final_url: "https://websecblog.com/vulns/bypassing-firebase-authorization-to-create-custom-goo-gl-subdomains/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["Logic flaw", "IDOR"]
publication_date: "2018-09-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5687
---

# Bypassing Firebase authorization to create custom app.goo.gl subdomains

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[September 21, 2018September 23, 2024](https://websecblog.com/vulns/bypassing-firebase-authorization-to-create-custom-goo-gl-subdomains/)

![](https://websecblog.com/wp-content/uploads/dynamic-links.png)

Since the support of goo.gl has already ended, I’ve been looking for ways to shorten URLs using Google services.

Some time ago I found a bug that allowed me to shorten links using Google’s official [g.co](https://g.co) shortener.

This time I took a look at [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/).

## Firebase Dynamic Links

They work by allowing you to create short URLs on either `*.app.goo.gl` or `*.page.link` subdomains.

Before `app.goo.gl` subdomains in Firebase were discontinued, there was a randomly generated `app.goo.gl` subdomain for each Firebase project, something like `i63lqb.app.goo.gl` _._ It could also be accessed via `goo.gl/app/i63lqb/ourLink` __(= `i63lqb.app.goo.gl/ourLink` on mobile devices).

You could also create four more `*.page.link` subdomains, but this time you could choose your own subdomain.

## Setting up a new subdomain

When I was setting up a new subdomain I noticed an interesting API call.
  
  
  /v1/checkValidDomainForProject

This returned an `OK` response in case the subdomain I wanted to create was both valid and not already in use. In case it was `OK`, the _Create_ button was enabled and I was able to create it. Otherwise, it showed an error.

Once I clicked the button to create it, another API call was fired, this time to:
  
  
  /v1/createDomainForProject

also containing the desired subdomain in its body.

If I let the POST call through, it would successfully add the subdomain to my project.

But let’s go back to the last API call. Since we know there are two types of domains we can use to shorten links in Firebase, let’s try to replace the value of the  _domainUriPrefix_ parameter from `page.link` with __`app.goo.gl` _._

Surprisingly, this actually worked. A `<myCustomPrefix>.app.goo.gl` subdomain was added and could be used in the project.

Since custom `*.app.goo.gl` subdomains like `maps.app.goo.gl` or `news.app.goo.gl` are used only for official products by Google, they should be registered only by them.

This leaves us with the following attack scenario:

> A regular user can create custom subdomains on [app.goo.gl](https://www.google.com/url?q=http://app.goo.gl&sa=D&usg=AFQjCNGlb_Dx8VpxWbjUfUTvICqWC_h17A) via the Firebase Console. This should be possible to do only by Google.

* * *

Timeline|  
---|---  
2018-08-10| Vulnerability reported  
2018-08-13| Priority changed to P1  
2018-08-14| Accepted  
2018-08-22| Fixed  
2018-08-29| Reward issued  
  
Written by [Thomas Orlita](https://thomasorlita.com/)

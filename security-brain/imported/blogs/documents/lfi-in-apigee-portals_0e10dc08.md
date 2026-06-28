---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-31_lfi-in-apigee-portals.md
original_filename: 2019-01-31_lfi-in-apigee-portals.md
title: LFI in Apigee portals
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: 0e10dc083321796ad7f6681fb60509240223301efbe436a463d0e9eff73b5ae5
text_sha256: e1b50a707e8518d1bdb866c4079d7588e9ec38ad49aedba6ed09d370bda95074
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# LFI in Apigee portals

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-31_lfi-in-apigee-portals.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0e10dc083321796ad7f6681fb60509240223301efbe436a463d0e9eff73b5ae5`
- Text SHA256: `e1b50a707e8518d1bdb866c4079d7588e9ec38ad49aedba6ed09d370bda95074`


## Content

---
title: "LFI in Apigee portals"
page_title: "LFI in Apigee portals – Offensi"
url: "https://offensi.com/2019/01/31/lfi-in-apigee-portals"
final_url: "https://offensi.com/2019/01/31/lfi-in-apigee-portals/"
authors: ["wtm@offensi.com (@wtm_offensi)"]
programs: ["Google"]
bugs: ["LFI"]
publication_date: "2019-01-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5437
---

## **Introduction**

[Apigee](https://www.apigee.com) provides clients with an API management platform that enables them to design, secure, deploy, monitor, and scale API’s. Furthermore Apigee provides clients with a customizable developer portal to enable developers to consume API’s easily and securely, and to measure API performance and usage. Apigee was acquired by Google in 2016 and therefore it is considered in scope for the [Google VRP](https://www.google.com/about/appsecurity/reward-program/), meaning that any valid vulnerability found in the Apigee platform will be rewarded.

### 

## **Creating a custom portal**

In order to interact with the development community, API providers can expose their API to the public by building a custom portal. Apigee portals are based on Drupal 7 and come with a preloaded set of options for users to customize. Users can modify the default theme, add pages and users, manage assets and publish API’s, as can be seen in the screenshot taken from the Portal management interface.

![manage-portals](https://i0.wp.com/offensi.com/wp-content/uploads/2019/01/manage-portals.png?resize=766%2C509&ssl=1)

When done editing, the portal manager publishes the portal on a subdomain of apigee.io. [Healthapix.apigee.io](https://healthapix.apigee.io/) shows a clear example of what the end result of a portal looks like.

## **Customizing the stylesheet**

According to the documentation on [https://docs-new.apigee.com](https://docs-new.apigee.com/portal-themes#theme-editor), users can edit the style of the theme by using SCSS instead of CSS:

_The style rules are defined using_ _[Sassy Cascading Style Sheet (SCSS)](https://sass-lang.com/)__. SCSS is a superset of Cascading Style Sheets (CSS), offering the following advantages:_

  * _Global variables that can be re-used throughout the style sheet._
  * _Nested rules to save style sheet development time._
  * _Ability to create mixins and functions_

This implicates that on the server side compilation and conversion is taking place. After compilation completes regular CSS files are published to the portal. This process looks like something that might be worth taking a closer look at.

## **The import directive**

When going through the language specific documentation on sass-lang.com, there is one directive that stands out from the rest:

_CSS has an import option that lets you split your CSS into smaller, more maintainable portions. The only drawback is that each time you use_ _`@import`_ _in CSS it creates another HTTP request. Sass builds on top of the current CSS_ _`@import`_ _but instead of requiring an HTTP request, Sass will take the file that you want to import and combine it with the file you’re importing into so you can serve a single CSS file to the web browser._

In short, the import directive allows us to reference other SCSS files by using this syntax: @import ‘somefile’. When seeing this directive, the SASS compiler will automatically try to locate ‘somefile.scss’, ‘somefile.sass’, or ‘somefile’. Depending on the version of the compiler you are using you might see some small differences in behavior.

## 

## **Exploitation**

What happens if we reference an arbitrary file with @import ‘/etc/shadow’? This file does not contain valid SCSS code, so compilation will most likely fail.

![schermafbeelding2019-01-31om2.19.02pm](https://i0.wp.com/offensi.com/wp-content/uploads/2019/01/schermafbeelding2019-01-31om2.19.02pm.png?resize=766%2C30&ssl=1)

As can be seen in the image above compilation fails indeed, throwing an error which exposes the contents of /etc/shadow, which is only readable by user root.

This particular bug was fixed within a matter of hours after submitting the details to Google. Thanks to Google for running the VRP the way they do!

[twitter-follow screen_name=’wtm_offensi’]

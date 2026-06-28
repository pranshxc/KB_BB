---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-12_topdesk-vulnerable-to-xml-signature-wrapping-attacks.md
original_filename: 2023-04-12_topdesk-vulnerable-to-xml-signature-wrapping-attacks.md
title: TOPdesk vulnerable to XML Signature Wrapping Attacks
category: documents
detected_topics:
- sso
- saml
- command-injection
- path-traversal
- automation-abuse
- business-logic
tags:
- imported
- documents
- sso
- saml
- command-injection
- path-traversal
- automation-abuse
- business-logic
language: en
raw_sha256: 06d65ecb3cabdae68d1106b4127a62811fe89c1dae9522d7b8fbb79dc5390d4c
text_sha256: 94c1e88288c227e23ae13048939b8f546c88da5883b5562b580bf5dcfaa0775f
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# TOPdesk vulnerable to XML Signature Wrapping Attacks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-12_topdesk-vulnerable-to-xml-signature-wrapping-attacks.md
- Source Type: markdown
- Detected Topics: sso, saml, command-injection, path-traversal, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `06d65ecb3cabdae68d1106b4127a62811fe89c1dae9522d7b8fbb79dc5390d4c`
- Text SHA256: `94c1e88288c227e23ae13048939b8f546c88da5883b5562b580bf5dcfaa0775f`


## Content

---
title: "TOPdesk vulnerable to XML Signature Wrapping Attacks"
page_title: "TOPdesk vulnerable to XML Signature Wrapping Attacks
  |
  Char49"
url: "https://char49.com/articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks"
final_url: "https://char49.com/articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks"
authors: ["Paulo A. Silva (@pauloasilva_com)"]
programs: ["TOPdesk"]
bugs: ["XML Signature Wrapping", "SAML", "SSO"]
publication_date: "2023-04-12"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1270
---

12 Apr

## TOPdesk vulnerable to XML Signature Wrapping Attacks

__By Char49 __[Advisories](/articles/category:Advisories) __[TOPdesk, ](/articles/tag:TOPdesk) [SAML, ](/articles/tag:SAML) [XSW, ](/articles/tag:XSW) [XML-based, ](/articles/tag:XML-based) [CVE-2023-34923](/articles/tag:CVE-2023-34923)

TOPdesk Single Sign-on integration based on SAML (Security Assertion Markup Language) was vulnerable to XML Signature Wrapping (XSW) attacks, allowing bad actors with credentials to authenticate with the Identity Provider (IdP) to impersonate any TOPdesk user, tampering with the SAML Response.

The vulnerability was discovered in TOPdesk v12.10.12 but it should also affect previous versions. The [vendor acknowledged the issue](https://my.topdesk.com/tas/public/ssp/content/detail/knowledgeitem?unid=56a16ba1c2824e9a82655892ba75d3c0) and promptly released a patch to address it.

## Preamble

Authentication is the process of verifying that an individual is whom it claims to be. In the context of web applications, it is commonly performed by submitting a username and one or more items of private information that only a given user should know, such as a password.

One application, the service provider, can delegate the authentication process to another integrated, yet independent application: the identity provider. This authentication scheme, known as Single Sign-on (SSO), allows users to log in once and access integrated services without re-entering authentication factors. The Security Assertion Markup Language (SAML) is an XML-based method for exchanging user security information between an identity provider and the service provider.

## Context

A client of ours requested a security assessment (pentest) of their on-premises TOPdesk instance.

TOPdesk, the product, is an information technology service management (ITSM) software developed by a company with the same name. In general, these solutions allow organizations to manage IT services in a central place: customers place requests, and agents (organization staff) are responsible to fulfill those requests.

TOPdesk's solution has three different applications: a Self-Service Portal that allows authenticated users to place requests and interact with agents, an Operators application where organization staff manages the requests, and an Admin console.

In regards to authentication, TOPdesk supports both local authentication using a combination of username and password and SAML-based SSO. The assessed TOPdesk instance (service provider) had SSO enabled for both the Self-Service Portal and Operator application, using Azure Active Directory (Azure AD) as the identity provider.

The authentication process was straightforward:

  1. users visiting one of the mentioned TOPdesk applications press the "Azure AD Login" button
  2. TOPdesk issues a SAML Request and redirects the user to the Azure AD login page
  3. after completing the authentication process with Azure AD, users are redirected to the TOPdesk application with a SAML Response.

## The issue

As said before, SAML is XML-based. Unfortunately, it is not that rare to find parsing issues with XML: either due to vulnerable or poorly configured XML parsers or the way the XML data structure is accessed/consumed.

Azure AD SAML Response was base64 encoded, but it could be easily decoded in order to inspect its content. Below is a simplified version of the original SAML Response:

![SAML Response](/user/pages/04.articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks/figure-1.png)

Highlighted in the above image, you can see that there's a single `<samlp:Response>` element and the `onpremisesssamaccountname` attribute value starts with an "a". Although this user had successfully authenticated with Azure AD, it was not allowed to access TOPdesk, thus access would be denied.

SAML Response XML includes a signature that was properly validated nevertheless, it is still possible to introduce some changes without invalidating the signature. Some of these changes may lead the business logic accessing the XML data structure at a later stage to have a different view of the data.

The following image shows the exact changes we've done to the original SAML Response in order to impersonate a TOPdesk Operator:

  1. we've cloned the original SAML Response XML
  2. removed the `<Signature>` XML element from the clone
  3. injected the modified clone right before the `<Signature>` element in the original SAML Response
  4. changed the `onpremisessamaccountname` attribute value to a valid TOPdesk username ("D").

![Changed SAML](/user/pages/04.articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks/figure-2.png)

With these changes, we were able to access TOPdesk as user "D", an operator, even when authenticated with an unprivileged Azure AD user "a".

This is not the only way to do it: both the changes made to the original SAML Response and the injection point may vary. This type of issue, in which attackers circumvents SAML integrity protection and the origin authentication of the XML Signature injecting arbitrary content, is known as XML Signature Wrapping (XSW).

## Impact

Bad actors with access to valid Identity Provider account credentials (their own or stolen) would be able to impersonate any TOPdesk user.

Impersonating a TOPdesk Operator would give bad actors access not only to existing customer requests (messages and uploaded files), potentially exposing sensitive data, but also allow them to interact with customers on behalf of the organization.

## Mitigation

TOPdesk acknowledged the finding and released a patch. Those running TOPdesk software on-premises should apply the patch immediately.

## CVE

[**CVE-2023-34923**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34923)

It was a great pleasure collaborating with TOPDesk. They demonstrated a genuine interest and diligence from the very beginning, and generously sent us an awesome swag gift.

![topdesk-swag_p](/user/pages/04.articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks/topdesk-swag_p.jpg)

#### Share this Post

[__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://char49.com/articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks) [__Twitter - X](https://twitter.com/intent/tweet?url=https://char49.com/articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks&text=TOPdesk vulnerable to XML Signature Wrapping Attacks) [__Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https://char49.com/articles/topdesk-vulnerable-to-xml-signature-wrapping-attacks)

#### Author

**Char49**

****

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-09_msrc-joint-security-research-write-up-azure-ad-consent-bypass-disclosure-with-ki.md
original_filename: 2022-04-09_msrc-joint-security-research-write-up-azure-ad-consent-bypass-disclosure-with-ki.md
title: MSRC – Joint security research write up – Azure AD Consent bypass disclosure
  with Kim Jamia – Q1/2022
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: a6a356d7875c8eda13611adf532397a89a24653c37643754d703146d25e1f662
text_sha256: 62d35d734aaa7a337e6e9e4a6b4dd49090da4bcc37f7bf9af09897d9f3e0607c
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# MSRC – Joint security research write up – Azure AD Consent bypass disclosure with Kim Jamia – Q1/2022

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-09_msrc-joint-security-research-write-up-azure-ad-consent-bypass-disclosure-with-ki.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `a6a356d7875c8eda13611adf532397a89a24653c37643754d703146d25e1f662`
- Text SHA256: `62d35d734aaa7a337e6e9e4a6b4dd49090da4bcc37f7bf9af09897d9f3e0607c`


## Content

---
title: "MSRC – Joint security research write up – Azure AD Consent bypass disclosure with Kim Jamia – Q1/2022"
page_title: "MSRC – Joint security research write up – Azure AD Consent bypass disclosure with Kim Jamia – Q1/2022 – SecureCloudBlog"
url: "https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/"
final_url: "https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/"
authors: ["Joosua Santasalo (@SantasaloJoosua)", "Kim Jämiä (@KimJamia)"]
programs: ["Microsoft"]
bugs: ["Broken authorization"]
publication_date: "2022-04-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2733
---

[Uncategorized](https://securecloud.blog/category/uncategorized/)

# MSRC – Joint security research write up – Azure AD Consent bypass disclosure with Kim Jamia – Q1/2022

![Tuntematon's avatar](https://1.gravatar.com/avatar/11e06d0a052f195711c44bab3ccfaf85495349fb21121c9534aca4b2860dd011?s=100&d=identicon&r=G)

julkaissut [Joosua Santasalo](https://securecloud.blog/author/santasalojh/)

[9 huhtikuun, 2022](https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/)

[Comments 0](https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/#respond)

[![](https://securecloud.blog/wp-content/uploads/2022/04/image-5.png?w=665)](https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/)

I decided to post a short write-up on this MSRC case as this case was first one I worked with co-contributor [@KimJamia](https://twitter.com/KimJamia)

## Consent hack timeline

  * Initial submission Q1 2022
  * Microsoft proactively addressed this issue and a fix for this issue was released on 3/17

## Scope

**Bypass consent framework for multi-tenant apps.**

  * Get user attributes with access token, and refresh-token for scopes of the application

### Discovery

I discovered this originally in end of 2021 by accident, but thought it was misconfiguration on my side, as I was requesting later additional scopes, which would ”fix” the behavior.

**Confirmation**

In early 2022 Kim Jämiä had discovered the same behavior independently, and thought also, that it is publicly known quirky behavior. We confirmed both, that this should not be desired behavior, as it allows bypassing the consent, and does not result in any service principal in the victim tenant, thus we decided that we should submit this as a case to MSRC

### Explanation

Combination of knownClientApplications and preAuthorizedApplications attribute allowed bypassing consent for 3rd party scopes that are defined using two of these attributes (and two app registrations)

  * **Text from initial submission** :_If we look at the explanation (links below 📑) this seems by design, but results in edge case, where multi-tenant applications can get user tokens without any consent being initiated._

[preAuthorizedApplications attribute](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest#preauthorizedapplications-attribute)

_”preAuthorizedApplications do not require the user to consent to the requested permissions. Permissions listed in preAuthorizedApplications do not require user consent. However, any additional requested permissions not listed in preAuthorizedApplications require user consent”_

### Configuration

**Login parameters example**
  
  
  resource:"41f71e46-cf85-474b-8c6d-09e5b653592a",
  scope:"https://api-26965.thx.dewi.red/hacked offline_access profile openid email",
  client_id:"41f71e46-cf85-474b-8c6d-09e5b653592a",
  redirect_uri,
  response_mode:"query",
  response_type:"code",
  endpoint:2,
  tenantId:"common",
  
  

[preAuthorizedApplications attribute](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest#preauthorizedapplications-attribute)
  
  
  "preAuthorizedApplications":[{"appId":"abcdefg2-000a-1111-a0e5-812ed8dd72e8","permissionIds":["8748f7db-21fe-4c83-8ab5-53033933c8f1"]}],
  

[knownClientApplications attribute](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest#knownclientapplications-attribute)
  
  
  "knownClientApplications":["41f71e46-cf85-474b-8c6d-09e5b653592a"],
  

## Ending words

Be sure to follow [MSRC](https://twitter.com/msftsecresponse/) on twitter, and stay tuned for more security research on my blog!

### Jaa tämä:

  * [ Jaa X:ssä(Avautuu uudessa ikkunassa) X ](https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/?share=twitter)
  * [ Share on LinkedIn(Avautuu uudessa ikkunassa) LinkedIn ](https://securecloud.blog/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/?share=linkedin)
  * 

Tykkää Lataa...

##  0 comments on “MSRC – Joint security research write up – Azure AD Consent bypass disclosure with Kim Jamia – Q1/2022” 

### Jätä kommentti [Peruuta vastaus](/2022/04/09/msrc-join-security-research-write-up-azure-ad-consent-bypass-disclosure-with-kim-jamia-q1-2022/#respond)

Δ

## Artikkelien selaus

[Edellinen artikkeli ](https://securecloud.blog/2022/04/01/kql-materialize-query/)

[Seuraava artikkeli ](https://securecloud.blog/2022/04/11/first-line-of-defence-review-azure-ad-gaps-in-conditional-access-with-log-analytics-azure-sentinel/)

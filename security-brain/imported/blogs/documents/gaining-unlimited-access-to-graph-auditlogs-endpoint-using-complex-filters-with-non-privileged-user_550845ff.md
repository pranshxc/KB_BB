---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-21_gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-.md
original_filename: 2022-04-21_gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-.md
title: Gaining Unlimited access to graph AuditLogs endpoint using complex filters
  with non-privileged user account
category: documents
detected_topics:
- access-control
- cloud-security
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- cloud-security
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 550845ff9954ea3278200d748ba0c492edfe1fb6d37561ae46b34afcf23e0ced
text_sha256: e0f4e66baba5a79c18e106f54c2c347faa22900a2ab75da46f7597f1e074a9e3
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Gaining Unlimited access to graph AuditLogs endpoint using complex filters with non-privileged user account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-21_gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `550845ff9954ea3278200d748ba0c492edfe1fb6d37561ae46b34afcf23e0ced`
- Text SHA256: `e0f4e66baba5a79c18e106f54c2c347faa22900a2ab75da46f7597f1e074a9e3`


## Content

---
title: "Gaining Unlimited access to graph AuditLogs endpoint using complex filters with non-privileged user account"
page_title: "Microsoft Cloud Security Research – Public Disclosure – Gaining Unlimited access to graph AuditLogs endpoint using complex filters with non-privileged user account – SecureCloudBlog"
url: "https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/"
final_url: "https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/"
authors: ["Joosua Santasalo (@SantasaloJoosua)"]
programs: ["Microsoft"]
bugs: ["Information disclosure", "Privilege escalation"]
publication_date: "2022-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2694
---

[Uncategorized](https://securecloud.blog/category/uncategorized/)

# Microsoft Cloud Security Research – Public Disclosure – Gaining Unlimited access to graph AuditLogs endpoint using complex filters with non-privileged user account

![Tuntematon's avatar](https://1.gravatar.com/avatar/11e06d0a052f195711c44bab3ccfaf85495349fb21121c9534aca4b2860dd011?s=100&d=identicon&r=G)

julkaissut [Joosua Santasalo](https://securecloud.blog/author/santasalojh/)

[21 huhtikuun, 2022](https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/)

[Comments 0](https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/#respond)

[![](https://securecloud.blog/wp-content/uploads/2022/04/msrc.jpg?w=590)](https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/)

**Background**

Not so long a go I was investigating various Azure related portals, and one of them caught my attention. While that portal did not yield any obvious vectors for exploitation, it raised my interest to see if I could go beyond user reading their own logs¹

* * *

¹Users can read their own sign-in logs to manually look for uncommon behaviour (this is standard behaviour)

* * *

**Scope**

The issue described allowed unprivileged user to modify graph search filters so that user could access logs which would normally require admin roles.

**Affected service**

  * Graph API AuditLogs endpoint
  * Endpoint and operation tested to be vulnerable `/beta/auditLogs/signIns`

**MSRC Categorization**

  * Severity: Important
  * Security Impact: Information Disclosure

* * *

## Timeline

MSRC (Microsoft Security Response Center) provided fast response and proceeded to fix the issue in fast timeline

  * 02/2022 Finding submitted to MSRC
  * 03/2022 MSRC confirms the reported behaviour
  * 03/2022 MSRC confirms that fix has been issued for the described vulnerability

* * *

## Details

What I discovered was, that Graph API allowed non-privileged user to access privileged logs when utilizing advanced [lambda operators](https://docs.microsoft.com/en-us/graph/query-parameters#filter-using-lambda-operators) – Essentially calling /auditLogs endpoint beyond their own permissions.

❌ **Trying to get user logs with basic filters**
  
  
  code:'Authentication_RequestFromUnsupportedUserRole'
  innerError:{date: '2022-01-27T12:13:45', request-id: '05b046db-27ba-405c-8532-35ce96025018', client-request-id: '05b046db-27ba-405c-8532-35ce96025018'}
  message:'User is not in the allowed roles'
  
  

✅ **When complex filtering with lambda operators and multiple OR conditions was used user got access to sensitive logs**

`var operation = `https://graph.microsoft.com/beta/auditLogs/signIns?&$filter=signInEventTypes/any(t: t eq 'interactiveUser' or t eq 'nonInteractiveUser' or userId eq 'fff4c705-62e2-4215-9dc8-90f208d15267' )``

* * *

✅ **Below is example snippet of the Graph API call with exploitable filter being used.**

![image](https://user-images.githubusercontent.com/58001986/164383232-538e5834-f42c-4dd0-9a3b-611970464982.png)

⚠️**The result was full dump of sensitive sign-in logs**

![image](https://user-images.githubusercontent.com/58001986/164383716-1005252c-8a86-465e-b673-dabda6e2b86a.png)

## Ending words

As always, when there is something more complex being applied to authorization process things tend to get more interesting. This shall definitely be something I will stay on a lookout

Be sure to follow [MSRC](https://twitter.com/msftsecresponse/) on twitter, and stay tuned for more security research on my blog!

### Jaa tämä:

  * [ Jaa X:ssä(Avautuu uudessa ikkunassa) X ](https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/?share=twitter)
  * [ Share on LinkedIn(Avautuu uudessa ikkunassa) LinkedIn ](https://securecloud.blog/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/?share=linkedin)
  * 

Tykkää Lataa...

##  0 comments on “Microsoft Cloud Security Research – Public Disclosure – Gaining Unlimited access to graph AuditLogs endpoint using complex filters with non-privileged user account” 

### Jätä kommentti [Peruuta vastaus](/2022/04/21/microsoft-cloud-security-research-public-disclosure-gaining-unlimited-access-to-graph-auditlogs-endpoint-using-complex-filters-with-non-privileged-user-account/#respond)

Δ

## Artikkelien selaus

[Edellinen artikkeli ](https://securecloud.blog/2022/04/13/add-user-as-read-to-azure-devops-projects/)

[Seuraava artikkeli ](https://securecloud.blog/2022/04/22/collection-aad-authentication-related-tools/)

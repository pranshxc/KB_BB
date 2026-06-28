---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-25_ericsson-sensitive-data-exposure-via-traceaxd.md
original_filename: 2023-05-25_ericsson-sensitive-data-exposure-via-traceaxd.md
title: Ericsson Sensitive Data Exposure via Trace.axd
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: cf4a0658489699942f76be1f4c81c70722009015178962e1ffcffcb12965a4bf
text_sha256: 1d2e212b89ee4503d314b47c32ad9db0dcd05183b7ebc65e70bd1ba66b9c1297
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Ericsson Sensitive Data Exposure via Trace.axd

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-25_ericsson-sensitive-data-exposure-via-traceaxd.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `cf4a0658489699942f76be1f4c81c70722009015178962e1ffcffcb12965a4bf`
- Text SHA256: `1d2e212b89ee4503d314b47c32ad9db0dcd05183b7ebc65e70bd1ba66b9c1297`


## Content

---
title: "Ericsson Sensitive Data Exposure via Trace.axd"
url: "https://checkmarx.com/blog/ericsson-sensitive-data-exposure-via-trace-axd/"
final_url: "https://checkmarx.com/blog/ericsson-sensitive-data-exposure-via-trace-axd/"
authors: ["David Sopas (@dsopas)"]
programs: ["Ericsson"]
bugs: ["Information disclosure"]
publication_date: "2023-05-25"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1116
---

Research by David Sopas and João Morais 

_Checkmarx Security Research team reached out to Ericsson’s Responsible Disclosure Program, notifying them of the the finding on 14th March 2023. Ericsson acknowledged the finding and replied that the issue was fixed on 11th April 2023._

ASP.NET web applications that run with tracing enabled, may publicly expose sensitive information. [This feature](https://learn.microsoft.com/en-us/previous-versions/aspnet/bb386420\(v=vs.100\)) allows any user to view diagnostic information about a single request for an ASP.NET page. When this feature is enabled, Trace Viewer (Trace.axd) may be publicly accessible, without server’s root authentication. The Checkmarx Security Research team discovered this vulnerability and will explore what that means for users in this post. 

This research was conducted following Ericsson Vulnerability Disclosure Program. 

One of Ericsson’s subdomains is forecast.ericsson.net. However, when accessing it via a web browser it redirects to https:// forecast.ericsson.net /Login /Login. aspx. No complex reconnaissance process was required to understand that we were dealing with an ASP.NET web application. 

There are several, well-known endpoints/resources of interest to check for when dealing ASP.NET web applications, and – /Trace.axd is one of them. Trace.axd is a web-page that is intended to provide extensive logging information in regard to web requests to the application. ~~–~~ If this is exposed, it may provide attackers unauthenticated access to the last 80 web requests made to the server. This has the potential to result in a sensitive information, such as PII data, and session details being disclosed. This information may then be used to potentially take over user accounts, and further compromise Ericsson’s applications. 

After finding Trace Viewer (Trace.axd) on our target subdomain (https://forecast.ericsson.net/Trace.axd), we checked what information was available. 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

The picture above shows the Trace Viewer main page (Trace.axd), which is where the physical directory of the web application (E:webrootsSupplyExtranet) and the last requested web application files are printed (Supply/ChangePassword.aspx). 

As you can see, it is possible to view additional details for each request. This potentially can allow malicious actors access to sensitive information. The body of POST requests, especially those to the Login/Login.aspx endpoint, are good candidates to monitor for disclosure sensitive information, including usernames and passwords. We can see this scenario, where user account credentials, username and password, are both shown in plaintext in the figure below. 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Information disclosure via Trace Viewer (Trace.axd) for ASP.NET web applications is a high severity security issue that can lead to the compromise of sensitive information and online systems. This feature should not be enabled in production environments. 

Tags:

AppSec

Awareness

data exposure

English

Vulnerability

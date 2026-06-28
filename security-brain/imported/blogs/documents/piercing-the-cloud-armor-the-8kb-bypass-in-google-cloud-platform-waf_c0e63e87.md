---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-24_piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf.md
original_filename: 2022-02-24_piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf.md
title: Piercing the Cloud Armor - The 8KB bypass in Google Cloud Platform WAF
category: documents
detected_topics:
- command-injection
- cloud-security
- xss
- sqli
tags:
- imported
- documents
- command-injection
- cloud-security
- xss
- sqli
language: en
raw_sha256: c0e63e87e73a36784c22fa9a587b2a3d1244298f803bb545d36f278fc6c33805
text_sha256: add921f8f8b8484c31db11802f738f8ea66088624cc291e45a12b312debd59ef
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Piercing the Cloud Armor - The 8KB bypass in Google Cloud Platform WAF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-24_piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, xss, sqli
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `c0e63e87e73a36784c22fa9a587b2a3d1244298f803bb545d36f278fc6c33805`
- Text SHA256: `add921f8f8b8484c31db11802f738f8ea66088624cc291e45a12b312debd59ef`


## Content

---
title: "Piercing the Cloud Armor - The 8KB bypass in Google Cloud Platform WAF"
page_title: "Piercing the Cloud Armor: Exploiting the 8KB Bypass in Google Cloud Platform WAF"
url: "https://kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf"
final_url: "https://kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf/"
authors: ["Kloudle (@Kloudleinc)"]
programs: ["Google"]
bugs: ["WAF bypass"]
publication_date: "2022-02-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2872
---

## Introduction

Web application firewall suites provide a critical layer of security for modern web applications and can protect them from a wide variety of attacks, such as: code execution, SQL injection, cross-site scripting, et cetera even when the underlying application is vulnerable. GCP customers can use Cloud Armor to protect applications served with Google Cloud Load Balancing.

Cloud Armor supports the definition of custom expressions for rules, while also providing a set of pre-configured web application firewall rules that draw from the OWASP ModSecurity Core Rule Set.

![Google Cloud Armor rule](https://imgs.kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf/1673700013-google-cloud-armor-rule.png)

## The 8 KB limitation

The web application firewall component of Cloud Armor inspects incoming HTTP requests and compares them against rule-based policies defined by the user. The Cloud Armor service can be configured to allow or deny a request to the underlying application based on the rules triggered by a given request.

![Cloud Armor 8 KB limitation](https://imgs.kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf/1673700017-cloud-armor-8-kb-limitation.png)

The web application firewall component of Cloud Armor has a non-configurable HTTP request body size limit of 8 KB. This means that Cloud Armor will only inspect the first 8192 bytes or characters of an HTTP POST request body.

This is similar to the well-documented [8 KB limitation](https://kloudle.com/blog/the-infamous-8kb-aws-waf-request-body-inspection-limitation) of the AWS web application firewall, however, in the case of Cloud Armor, the limitation is not as widely known and is not presented to customers as prominently as the limitation in AWS.

As of the time of writing this article, customers are not shown a prompt or notice when configuring Cloud Armor rules from within the web UI, and can only find a reference to the 8 KB limit in a nondescript notice[included in a documentation article.](https://cloud.google.com/armor/docs/security-policy-overview)

This issue can be exploited by crafting an HTTP POST request with a body size exceeding the 8 KB size limitation of Cloud Armor, where the payload appears after the 8192th byte/character in the request body.

![HTTP POST request with a body size exceeding the 8 KB size limitation of Cloud Armor](https://imgs.kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf/1673700015-http-post-request-with-body-size-exceeding-8kb-size-limitation-cloud-armor.png)

![HTTP POST response with a body size exceeding the 8 KB size limitation of Cloud Armor](https://imgs.kloudle.com/blog/piercing-the-cloud-armor-the-8kb-bypass-in-google-cloud-platform-waf/1673700018-http-post-response-with-body-size-exceeding-8kb-size-limitation-cloud-armor.png)

An attacker’s ability to utilise the WAF bypass successfully is conditionally limited, however. The endpoint being targeted should accept and process HTTP POST requests in a manner which could trigger an underlying vulnerability. The bypass will not yield meaningful results for an attacker if a given underlying endpoint does not accept HTTP POST requests.

## Request body limitations with HTTP PUT and PATCH

Another limitation of Cloud Armor is that request body inspection is limited only to HTTP POST requests. As a result, an attacker could craft an HTTP PUT or PATCH request with a malicious payload in the request body to bypass the WAF without having to append 8192 bytes of padding to the payload. As mentioned above in reference to HTTP POST requests, an attacker’s ability to meaningfully utilise this technique is dependent on the underlying application being configured to accept and process HTTP PUT/PATCH requests, in a manner that could trigger an underlying vulnerability.

## Impact of the WAF bypass

An attacker with knowledge of this limitation would be better placed to exploit any vulnerabilities that may be present in an underlying application. For illustration, consider a web application that has not been patched and is still vulnerable to the infamous Log4j RCE vulnerability (CVE-2021-45046).

A Cloud Armor setup that is configured to use the pre-configured “cve-canary” rule [will appropriately block](https://cloud.google.com/blog/products/identity-security/cloud-armor-waf-rule-to-help-address-apache-log4j-vulnerability) most attempts at exploiting the Log4j RCE, however, an attacker with knowledge of Cloud Armor’s 8 KB HTTP POST request body size limitation would still be in a position to bypass the Cloud Armor WAF, exploit the underlying application, and achieve remote code execution.

## How can this be fixed?

Cloud Armor is a valuable security tool, but it is important that customers are aware of the 8 KB size limitation so that they can take steps to further secure their applications.

Customers can configure a custom Cloud Armor rule to block HTTP requests where the request body is larger than 8192 bytes.
  
  
  int(request.headers["content-length"]) >= 8192

The above rule will trigger on incoming requests where the value of the Content-Length header is equal to or greater than 8192.

As noted in our previous article on the 8 KB size limit of the Amazon Web Services WAF, there may be certain resources for which legitimate requests are expected to be 8 KB or larger in size. In these cases, rules can be [fine-tuned](https://cloud.google.com/armor/docs/rules-language-reference) using Cloud Armor’s custom rule language so that the WAF expects and appropriately handles legitimate requests.

## Conclusion

While an attacker who is targeting a service behind a web application firewall may only attempt to find bypasses specific to the payload or the type of attack being carried out, the 8 KB limitation affecting Cloud Armor (as well as several other cloud WAF services) can act like a “catch-all” WAF bypass.

Cloud Armor is a useful service for protecting resources and data on the Google Cloud Platform, however, customers must be aware of the limitations of its request filtering capabilities, and should take steps to mitigate potential risk that may arise from the 8 KB WAF limitation.

We will be publishing an article later today on Kloudle Academy to provide a detailed explanation of how Cloud Armor can be configured to protect underlying applications from the service’s 8 KB limitation.

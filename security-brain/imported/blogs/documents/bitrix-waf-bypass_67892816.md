---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-27_bitrix-waf-bypass.md
original_filename: 2020-04-27_bitrix-waf-bypass.md
title: Bitrix WAF bypass
category: documents
detected_topics:
- xss
- command-injection
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 67892816096e6d1d055747487b5a2e9e9bcc6a565e91aa95ad5b24249c945cab
text_sha256: 148bdb114f1f2fb103babef6122d0fe16ae00f5d3e9324aa407322fa630df340
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bitrix WAF bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-27_bitrix-waf-bypass.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `67892816096e6d1d055747487b5a2e9e9bcc6a565e91aa95ad5b24249c945cab`
- Text SHA256: `148bdb114f1f2fb103babef6122d0fe16ae00f5d3e9324aa407322fa630df340`


## Content

---
title: "Bitrix WAF bypass"
page_title: "Bitrix WAF bypass - Deteact - continuous information security services"
url: "https://blog.deteact.com/bitrix-waf-bypass/"
final_url: "https://blog.deteact.com/bitrix-waf-bypass/"
authors: ["Roma Ramazanoff (@r0hack)"]
programs: ["Mail.ru"]
bugs: ["Reflected XSS"]
bounty: "300"
publication_date: "2020-04-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4629
---

# Bitrix WAF bypass

[April 27, 2020June 4, 2020](https://blog.deteact.com/2020/04/27/) [r0hack](https://blog.deteact.com/author/r0hack/)

_In Russian:<https://blog.deteact.com/ru/bitrix-waf-bypass/> _

_UPD:[CVE-2020-13758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13758) assigned_

Sometimes when exploiting reflected XSS the input parameters get injected directly into the body of the _< script>_ tag. Typically, this means that the exploit is trivial: HTML entity encoding will not prevent it, and many firewalls (including now obsolete Chrome XSS Auditor) won’t either. But CMS Bitrix has its own built-in proactive filter (WAF) for this case, and it operates similar to XSS Auditor.

## **WAF bypass**

While fuzzing one of the Mail.ru services eligible for the Bug Bounty I encountered an entry point where the GET parameter was reflected in the body of _< script>…</script>_ tag. But it was not possible to make a simple PoC because the application was built using Bitrix and the WAF module was activated.

Any attempts to insert an interesting code lead to the whole script body being replaced by the placeholder _<!— deleted by Bitrix WAF —>_.

For testing purposes, we deployed a Bitrix CMS application with WAF module activated and added the following code to one of the pages (/waf-bypass.php):

![](https://lh3.googleusercontent.com/D1OTjA6dfjqWmX-xivhugAN6nbG0rd5NefYQVnLEi2pTeQZCfakUG1M5y_COyt3nOmnJNuUmTsCzF1TZEPxL54JHz-Z-tWV-WmPYRVuVN0WsAZGUTeW6YMOZY3Uku_FLZwHvV4Jo)

If a single quote (which terminates the JS string) and an _alert_ call (as well as any other function) are passed to the vulnerable page parameter, the WAF cuts out the entire script:

![](https://lh3.googleusercontent.com/wJjvKBUksZoezaYG_g_Eq0BMakibZClddg0xgCRGJB-E5DZHurIrhbPIFhTwzgr5RSmkEbpuRx9Qfl2bspZ4Oay2__grmLYxN8Yp5CMJH7KP9LjmsjsWkzj5WT_JJnIiNofCtych)

However, during the fuzzing we found out that the mitigation does not work when the vulnerable parameter contains a _null byte_ (_%00_):

![](https://lh4.googleusercontent.com/8Prs3ERBTZxajNTOrZX2D-ZJa8TsRnapnmMcAbIDDKYA9Y2_7N5ytjPj3bxOWeiOK_EHoB3l0zmsmkYVoU2a6z9qxGVNcn6IluxSOIlx8TimIISrFSJocq-O6pcQlm8wWrFdzpxy)

Thus, we get a full payload for XSS exploitation:

/waf-bypass.php?page=BYPASS%00")});alert(1);$(document).ready(function%20(){%2f%2f

1 | /waf-bypass.php?page=BYPASS%00")});alert(1);$(document).ready(function%20(){%2f%2f  
---|---  
  
This is what the result looks like on the page:

![](https://lh4.googleusercontent.com/n1_VnCBDI-XcGroX2sLpglSlcceyzK2GWdOUeqWarz1BIcCG-BMK5O3XgTAXNC_NOyeQejxQou24PSIkC4rribFVA0VJZs3ScAAsw9PxkDvuWqLbfk9pA1l_-JvqX3UtcZe-84Od) ![](https://lh3.googleusercontent.com/W1ox-YBO_NqytFyBZECuN_VsuWaE5JB0h3nYkyg37gnTd55Wf9Mw7sBqkjwPtRFyoE87QxVFWXca-EupXLBUu0oEXZ4BAU9KySINjS447c8ICez-K_RLbjfQWsNp-BkMd-4BKq4D)

## **The root cause**

The mitigation is implemented in the post-filtration module to protect against XSS. The module works similarly to the XSS Auditor and tries to find the user input (like GET or POST parameters) in the body of the script tags on the page.

For some reason this module cuts out the null bytes from the input parameter values, so in our case the script tag body can’t be matched against input parameter value since the body contains \x00, and the parameter value does not.

Vulnerable code line is located in _./bitrix/modules/security/classes/general.post_filter.php/post_filter.php_ where null byte _chr(0)_ is cut out in the _addVariable_ method:

![](https://lh3.googleusercontent.com/e_jDQOqCayEQZwx-aNB7mLFWuY-pFY6tnwZocWiALuqRrdaYuTp1_pcVBMdyt9TsaVk4vAxQ0TQpncwBKuxVHV74f-fnh3Z08A9lMjuY9WZx13elqaY1FU1tMSsJtrbSWAXz97kC)

The _isDangerBody_ function tries to find user input in the executable script body, and this is where the original _$body_ value and the array of parameters (with \x00 removed) are passed to the _findInArray_ function:

![](https://lh4.googleusercontent.com/k7U6phxUG3TxfXzx3h1lqPUaRUSmY0I3Q68c9dJDA_m8N3xNHqjraZMLXakoCOgF3ceELNB5RheYkIuSYbsP2c9-aIW2AtUAE_NRo4D6RZPGKPAdAYtqBSavdu49rvbJy8slGHRH)

Remember that WAFs are almost always bypassable and the may contain weaknesses and vulnerabilities themselves. You should not rely on third-party mitigation solutions and firewalls, you should build a secure development process and regularly conduct [penetration testing](https://pentest.deteact.com/) of applications.

Specifically in this case you can remove the _str_replace_ call from the _addVariable_ function (or to apply the same modification to the _$body_ variable in the _isDangerBody_ function) to correct the weakness in the WAF itself.

[Bug Bounty](https://blog.deteact.com/category/research/bug-bounty/) [Research](https://blog.deteact.com/category/research/) [Web Security](https://blog.deteact.com/category/research/web/)

## Post navigation

[PREVIOUS POST Previous post: Common flaws of SMS auth](https://blog.deteact.com/common-flaws-of-sms-auth/)

[NEXT POST Next post: HTTP Request Smuggling](https://blog.deteact.com/gunicorn-http-request-smuggling/)

### Leave a Reply [Cancel reply](/bitrix-waf-bypass/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Δ

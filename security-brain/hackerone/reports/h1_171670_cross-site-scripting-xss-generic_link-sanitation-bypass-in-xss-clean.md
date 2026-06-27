---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '171670'
original_report_id: '171670'
title: Link sanitation bypass in xss_clean()
weakness: Cross-site Scripting (XSS) - Generic
team_handle: codeigniter
created_at: '2016-09-24T10:29:32.313Z'
disclosed_at: '2016-11-04T10:53:18.736Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Link sanitation bypass in xss_clean()

## Metadata

- HackerOne Report ID: 171670
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: codeigniter
- Disclosed At: 2016-11-04T10:53:18.736Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

While researching a website that uses your framework xss_clean() function to sanitize user's input in comments, I was able to bypass it and could trigger XSS payloads using javascript links in allowed tags such as anchors. This could be achieved by using the new HTML5 standard entities such as `&NewLine;` `&Tab;` `&colon;`

### PoC
Run the following piece of code under CI framework
```
echo $this->security->xss_clean('<a href="javascript&NewLine;&colon;eval(String.fromCharCode(97, 108, 101, 114, 116, 40, 100, 111, 99, 117, 109, 101, 110, 116, 46, 100, 111, 109, 97, 105, 110, 41));">XSS Link</a>');
```
**For a demo**
1. Go to http://www.aorank.com/tutorial/codeigniter_xss_clean/index.php/form/ (*a demo of a tutorial illustrating xss_clean();*)
2. In employee name's field, enter
 ```
<a href="javascript&NewLine;&colon;eval(String.fromCharCode(97, 108, 101, 114, 116, 40, 100, 111, 99, 117, 109, 101, 110, 116, 46, 100, 111, 109, 97, 105, 110, 41));">XSS Link</a>
```
3. Submit the form
4. The payload is injected into the page and XSS vector is triggered as soon as user clicks the link.

### Why?
Actually the website was using an old version of xss_clean() that did not take the new standard entities into consideration. However, when I downloaded the latest version of CI to see if this is fixed, I noticed that you check if they exist and handle them accordingly but there is a flaw in the regular expression used to detect standard entities that causes the XSS bypass.

In line 677 in ./system/core/Security.php
`if (preg_match_all('/&[a-z]{2,}(?![a-z;])/i', $str, $matches))`

We can see that this regular expression matches alpha characters preceded by ampersand (&) and **not followed** by a semi-colon (;) --*I have no idea why you do this BTW, since entities are usually followed by a semicolon :D*--

So when user injects `&NewLine;` and/or `&Tab;` they are not detected by the regular expression and hence not converted to their corresponding characters. That's why the XSS filter fails to detect the presence `javascript:` in the attribute.

### Remediation
Regular expression should be fixed to count for entities followed by a semi-colon :))

Looking forward to hearing from you soon ^_^

Sincerely,
Abood Nour

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

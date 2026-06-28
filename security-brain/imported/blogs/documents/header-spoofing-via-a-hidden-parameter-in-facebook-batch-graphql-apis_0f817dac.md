---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-21_header-spoofing-via-a-hidden-parameter-in-facebook-batch-graphql-apis.md
original_filename: 2022-11-21_header-spoofing-via-a-hidden-parameter-in-facebook-batch-graphql-apis.md
title: Header spoofing via a hidden parameter in Facebook Batch GraphQL APIs
category: documents
detected_topics:
- oauth
- access-control
- ssrf
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- oauth
- access-control
- ssrf
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 0f817dacf4f9629023d2febb38211f070e3f731c8e9f1f891b295c639c883a20
text_sha256: 5ff73680269d4e968d87a6f30949c064e6977adad89c9ca77b4139ee3cb782c0
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Header spoofing via a hidden parameter in Facebook Batch GraphQL APIs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-21_header-spoofing-via-a-hidden-parameter-in-facebook-batch-graphql-apis.md
- Source Type: markdown
- Detected Topics: oauth, access-control, ssrf, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `0f817dacf4f9629023d2febb38211f070e3f731c8e9f1f891b295c639c883a20`
- Text SHA256: `5ff73680269d4e968d87a6f30949c064e6977adad89c9ca77b4139ee3cb782c0`


## Content

---
title: "Header spoofing via a hidden parameter in Facebook Batch GraphQL APIs"
page_title: "[#0017] Header spoofing via a hidden parameter in Facebook Batch GraphQL APIs | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0017"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0017"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Meta / Facebook"]
bugs: ["GraphQL", "Security misconfiguration"]
bounty: "3,000"
publication_date: "2022-11-21"
added_date: "2022-11-22"
source: "pentester.land/writeups.json"
original_index: 1882
---

#0017  
Vendor: Meta  
Status: fixed  
Reported: May 01, 2022  
Disclosed: Nov 21, 2022 (204 days) 

# Header spoofing via a hidden parameter in Facebook Batch GraphQL APIs

**Description/Impact:**

GraphQL queries can be batched as described by the documentation:  
<https://developers.facebook.com/docs/graph-api/batch-requests/>

I have found a non-documented parameter called `headers` which allows me to set custom headers on the given batch requests.

_Host Header:_

Specifying the `Host:` header results in unpredictable behaviour. For example:

  * `Host: 127.0.0.1` -> A redirect to `https://www.facebook.com/graph/server.php?[params]`
  * `Host: apps.intern.facebook.com` -> Redirect to `https://apps.intern.facebook.com/login/`
  * `Host: graph.intern.facebook.com` -> Error saying: `The request could not be understood by the server due to malformed syntax.`

Unfortunately, it seems like the `Host` headers you can specify in these batch requests also behave the same way if you are not sending batch requests, but directly setting the `Host` header to these domains when sending requests to the server hosting this batching service.

It feels like these requests are not leaving the machine itself, and are just hitting different “virtual hosts” that are available on this IP. I wasn’t able to access `internalfb.com` infrastructure via this batch endpoint, it seems to be on a different infrastructure.

It also feels like these are not actual HTTP requests that you can create with the batch service, but maybe calls to the `/graph/server.php` endpoint. The `method` and `relative_url` feel to be just parameters to this `/server.php`, or something similar. `relative_url` seems to get converted into a parameter named `_fb_url`.

_Other Internal Headers:_

If you specify `X-FB-Debug: True` on a request to these IPs, you get back a bunch of encrypted debug headers. I assume those are coming from some middleman, like a loadbalancer, and not from the application itself.

To prove this point, if you set the `X-FB-Debug: True` header on a batch requests, you are not going to get back any debug headers in the batch response.

That behaviour makes me think that the batch requests are hitting the application directly, and do not go through some middleman loadbalancer. This _might_ allow me to set some internal headers via batching that the application expects from the loadbalancer, and which would be stripped normally from the requests.

I tried setting `X-FB-Client-IP-Forwarded` header in the batch calls to spoof my IP when performing GraphQL actions, but without any success. But if there are other internal headers that the application expects and trusts from the loadbalancer, then it might be possible to spoof those via this graph batching method.

This batch service could might be exploited for SSRF or for spoofing internal headers for the Graph application.

**Repro Steps:**

A raw batch requests: (modified from the Workplace android app, feel free to use the access token its just a Publishing Bot token from my test account)
  
  
  POST /?include_headers=true&decode_body_json=false&streamable_json_response=false&locale=en_US&client_country_code=HU HTTP/1.1
  Host: b-graph.workplace.com
  Priority: u=3, i
  Authorization: OAuth [redacted]
  X-Fb-Sim-Hni: 21601
  X-Fb-Connection-Type: unknown
  User-Agent:
  Content-Type: application/x-www-form-urlencoded
  X-Fb-Device-Group: 6066
  X-Tigon-Is-Retry: False
  X-Fb-Friendly-Name: handleLogin
  X-Fb-Request-Analytics-Tags: unknown
  Accept-Encoding: gzip, deflate
  X-Fb-Http-Engine: Liger
  X-Fb-Client-Ip: True
  X-Fb-Server-Cluster: True
  Content-Length: 213
  Connection: close
  
  batch=[{"headers": ["Host: graph.intern.facebook.com", "X-FB-Debug: True"], "method":"GET","body":"asd","name":"fetchViewerLoginAudienceInfo","omit_response_on_success":false,"relative_url":"/intern/api/graphql"}]
  

_This report has been part of the Meta BountyConEDU 2022 live hacking event in Madrid, Spain._

* * *

### Discussion:

**Me - 2022-05-01**

Other Meta owned non-Facebook Graph services are available on these IPs hosting the batch service. For example you can hit the GraphQL of ExpressWiFi with the `Host: b-graph.expresswifi.com` header.

It seems like these IPs/servers that I am hitting handle all “non-internalfb.com” Meta graph services.

* * *

**Me - 2022-05-01**

If you set the Host header to `m.intern.facebook.com`, you will get back a 404 HTML page, which is essentially redirecting you to the login page, and after a successful login to:

This confirms the behaviour that the batch service is sending a request to the selected “virtual host” to the path:
  
  
  /graph/server.php?_fb_url=[relative_url]&locale=[locale_from_querystring]&access_token=[access_token_from_header]&_fb_domain=Facebook&_fb_profilable_request_id=326014522&_fb_batch_child_request=1&_fb_batch_expires=1651402020&_fb_batch_sig=Afh-Je5z3GOz274X4h4
  

I’m not sure where the `method` parameter is added, maybe it is a POST, and its inside the body.

And depending on the target application, it either responds with something, redirects you, or presents a login page, etc.

* * *

**Vendor - 2022-05-01**

After reviewing this issue, we have decided to award you a bounty of $3000. Below is an explanation of the bounty amount. Meta fulfills its bounty awards through Bugcrowd and HackerOne.

spoofing host header in specific situations

Thank you again for your report. We look forward to receiving more reports from you in the future!

* * *

**Vendor - 2022-10-03**

Hi Dávid,

We have looked into this issue and believe that the vulnerability has been patched.

If you believe that the patch does not resolve this issue, please let us know using the “Incomplete Fix” option in your report “More Options” menu.

Thanks!  
_[redacted]_

* * *

**Vendor - 2022-10-19**

Hi Dávid,

Thanks again for your report. Following your request to publish, feel free to proceed by publishing this report as it has been fully investigated and fixed.

Thanks,

_[redacted]_  
Security

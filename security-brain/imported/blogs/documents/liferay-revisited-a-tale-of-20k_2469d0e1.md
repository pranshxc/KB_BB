---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-06_liferay-revisited-a-tale-of-20k.md
original_filename: 2022-08-06_liferay-revisited-a-tale-of-20k.md
title: 'Liferay revisited: A tale of 20k$'
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 2469d0e14baf3069c97e8a6cf92c40004379462fb38db1124c7ce46cd76942a1
text_sha256: 3a4dba6a61353190a4438e7ddd53ad3367df895b72ebc447bf34bba14e52028b
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Liferay revisited: A tale of 20k$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-06_liferay-revisited-a-tale-of-20k.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2469d0e14baf3069c97e8a6cf92c40004379462fb38db1124c7ce46cd76942a1`
- Text SHA256: `3a4dba6a61353190a4438e7ddd53ad3367df895b72ebc447bf34bba14e52028b`


## Content

---
title: "Liferay revisited: A tale of 20k$"
url: "https://vsrc.vng.com.vn/blog/liferay-revisited-a-tale-of-20k/"
final_url: "https://vsrc.vng.com.vn/blog/liferay-revisited-a-tale-of-20k/"
authors: ["VNG Security Response Center (@vngsecresponse)"]
bugs: ["RCE"]
bounty: "20,000"
publication_date: "2022-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2358
---

[![VNG Security Reponse Center - @VSRC](/images/logo/logo.svg)](/)

[![VNG Security Reponse Center - @VSRC](/images/logo/logo.svg)](/)

  * [Responsible Disclosure](/responsible-disclosure/)
  * [Hall of Fame](/hall-of-fame/)
  * [Blog](/blog/)
  * [Contact](/contact/)
  * [Join us](https://career.vng.com.vn/en/job-search)

  * [Responsible Disclosure](/responsible-disclosure/ "Responsible Disclosure")
  * [Hall of Fame](/hall-of-fame/ "Hall of Fame")
  * [Blog](/blog/ "Blog")
  * [Contact](/contact/ "Contact")
  * [Join us](https://career.vng.com.vn/en/job-search "Join us")

# Liferay revisited: A tale of 20k$

2022-08-06

![](../../images/blog-images/liferay-revisited-featured.png)

At the beginning of this year, we found an interesting exploit chain to achieve pre-auth RCE on an asset of a big Fintech company. Due to their disclosure policy, we have to redact some sensitive information related to that company and only focus on the technical details of this case. Let us refer to the domain of that company as `foo.bar`.

## Discovery of jkstatus bypass

After a quick reconnaissance, an endpoint on a subdomain caught our attention:
  
  
  https://sub.foo.bar/jkstatus;
  

(`“;”` is a well-known trick to bypass reverse-proxy in Tomcat. It was first presented at [BlackHat USA 2018 by Orange Tsai](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf)).

![JK Status Manager](../../images/blog-images/liferay-revisited-1.png)

This low-severity vulnerability discloses some sensitive information related to the internal services. So what do we need to do now? Draft a report and send it to the bug bounty program, right?

## From jkstatus to a Liferay instance

No, we're much better than that. There are a lot of defined rules (84 maps) to route requests to each internal endpoint. Luckily there’s one interesting endpoint that will route our requests to a Liferay instance:
  
  
  https://sub.foo.bar/web/aviva
  

The game is easy now - you may think - just exploit some Liferay CVEs and get the bounty. But life doesn't always work like that. After a while, we realize that our requests must go through these layers before reaching the Liferay instance.

![Flow of a HTTP request to the Liferay instance](../../images/blog-images/liferay-revisited-2.png)

Now our goal is to find a payload that let us traverse back to the base context of Liferay instead of `“/web/aviva”` and then reach a vulnerable endpoint like `“/api/liferay”` or `“/api/jsonws/”`.

But this asset is protected by Akamai WAF - it is way too good to block common bypasses like:
  
  
  /o/..;/api/liferay
  /o/..;/api/jsonws/invoke
  /api;/liferay
  /api;/jsonws/invoke
  

Because of `“;”` and `“..”`, Akamai blocked us before we could reach the Apache LoadBalancer. We almost gave up at this point but decided to review the defined rules of Apache LoadBalancer one last time.

![URI Mappings of Apache LoadBalancer](../../images/blog-images/liferay-revisited-3.png)

Let focus on the rule `/group/control_panel*`. This rule means it will match the wildcard if our requests starts with `/group/control_panel` and then passes them to the workers. Now we have:

  * We have a way to reach the Liferay instance with an arbitrary suffix payload.
  * We need to traverse back to the Liferay context and then reach `/api/jsonws` endpoint.
  * We can’t input `..;` because of Akamai WAF. But how about encoding it ?

Let try this payload:
  
  
  /group/control_panel/%2e%2e%3b/%2e%2e%3b/api/jsonws/
  

![Bypass payload process by Akamai WAF](../../images/blog-images/liferay-revisited-4.png)

What happens when `/group/control_panel/%2e%2e%3b/%2e%2e%3b/api/jsonws/` goes through Akamai?

The answer is that Akamai WAF will let this payload go through because Akamai won’t do URL decoding. Next, our payload will go to Apache LoadBalancer - it will do URL decoding and then route it to the internal services according to the defined URI mappings.

![Bypass payload process by Apache LoadBalancer](../../images/blog-images/liferay-revisited-5.png)

Now our payload is `/group/control_panel/..;/..;/api/jsonws/`.

At this stage, our payload matches the rule `/group/control_panel*` so Apache LoadBalancer will route our payload to Liferay.

Liferay is based on Tomcat, and I guess you know the trick of using `“;”` \- Liferay treats `“;”` as a path parameter, it will strip it from the URL, so now our payload is:

`/group/control_panel/../../api/jsonws/` which normalized to `/api/jsonws/`.

## Bypassing Akamai and pwning the Liferay instance

We know that this instance is vulnerable to [CVE-2020-7961](https://portal.liferay.dev/learn/security/known-vulnerabilities/-/asset_publisher/HbL5mxmVrnXW/content/id/117954271) (with the Last-Modified trick). Most public POC for CVE-2020-7961 has content like this:

![Common public POC for CVE-2020-7961](../../images/blog-images/liferay-revisited-6.png)

But these payloads won't work because Akamai WAF blocks some special characters on POST body:
  
  
  { } ; :
  

These characters are needed to be used in the JSON payload for [CVE-2020-7961](https://portal.liferay.dev/learn/security/known-vulnerabilities/-/asset_publisher/HbL5mxmVrnXW/content/id/117954271). Since we can’t use it anymore, we need to find another way to exploit it. From [a blog post of codewhitesec](https://codewhitesec.blogspot.com/2020/03/liferay-portal-json-vulns.html) \- the author of CVE-2020-7961 pointed out that we can invoke JSON Web Service in GET requests like this:
  
  
  /api/jsonws/service-class-name/service-method-name/arg1/val1/arg2/val2/
  

Still, we have to deal with one last thing: the GET URL mustn't be too long.

After spending time looking at the documentation of Liferay, we found a way to bypass this limitation. According to [this](https://help.liferay.com/hc/en-us/articles/360017899652-Invoking-JSON-Web-Services), we can call the JSON WebService in multiple ways - which means we can overcome the limitation of the JSON payload. This is good for us because we can’t use JSON anymore (Akamai WAF blocks `{` and `}` characters - as mentioned above).

## Bypass the limitation

Combine all the above techniques, the final URL of the payload is:
  
  
  /group/control_panel/..%3b/..%3b/api/jsonws/expandocolumn/add-column/-p_auth/-tableId/-name/-type/-defaultData:com.mchange.v2.c3p0.WrapperConnectionPoolDataSource/
  

NOTE:

  * `-p_auth, -tableId, -name, -type, ...`: assign a null value to these parameters.
  * `-defaultData:com.mchange.v2.c3p0.WrapperConnectionPoolDataSource`: init the object defaultData with type `com.mchange.v2.c3p0.WrapperConnectionPoolDataSource`.

In the POST body we use `defaultData.userOverridesAsString` to trigger setter of defaultData to set our payload when `C3P0ImplUtils.parseUserOverridesAsString()` was called and our serialized payload will be deserialized.

To summarize:

  * We found a way to set parameters like `“-p_auth”,“-tableId”,“-name”,“-type”` on the URL of the request (Akamai WAF allows me to have the `“:”` character in the URL).
  * Luckily our exploit chain is hex-encoded so we can put it in the POST body.

And the final thing we need is a handy deserialization payload to return the output of our commands in the HTTP response since the target doesn't have an outbound connection:

![Final payload to achieve pre-auth RCE on the target](../../images/blog-images/liferay-revisited-7.png)

## From a real case to an interesting CTF challenge

After a few weeks, we found another way to exploit this target with only a GET request. Our payload is short enough to execute the commands and write the output to Liferay's webroot. We put this idea into our TetCTF 2022 challenge. If you’re interested, you can [try it here](/download/tetctf2022.zip).

## Credit: k0nv0y@VSRC

Tags:[blog](/blog/tags/blog)[liferay](/blog/tags/liferay)[bugbounty](/blog/tags/bugbounty)[writeup](/blog/tags/writeup)[1day](/blog/tags/1day)

### VNG Security Response Center

VNG Campus, Lot Z06, Street 13, Tan Thuan Export Processing Zone

Tan Thuan Dong Ward, District 7, HCMC, Vietnam

VNG Corporation

[Home](/)[Contact](/contact/)

[](https://twitter.com/vngsecresponse)[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHN0eWxlPSIiIHhtbDpzcGFjZT0icHJlc2VydmUiIHdpZHRoPSI0OTAiIGhlaWdodD0iNDkwIj48cmVjdCBpZD0iYmFja2dyb3VuZHJlY3QiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIHg9IjAiIHk9IjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0ibm9uZSIvPgo8ZyBjbGFzcz0iY3VycmVudExheWVyIiBzdHlsZT0iIj48dGl0bGU+TGF5ZXIgMTwvdGl0bGU+PGcgaWQ9InN2Z18xIiBjbGFzcz0ic2VsZWN0ZWQiIGZpbGw9IiNFQjVBMjYiIGZpbGwtb3BhY2l0eT0iMSI+Cgk8ZyBpZD0ic3ZnXzIiIGZpbGw9IiNFQjVBMjYiIGZpbGwtb3BhY2l0eT0iMSI+CgkJPGcgaWQ9InN2Z18zIiBmaWxsPSIjRUI1QTI2IiBmaWxsLW9wYWNpdHk9IjEiPgoJCQk8cG9seWdvbiBwb2ludHM9IjMyMy42LDI0NSA0OTAsMzg5LjMgNDkwLDEwMC43ICAgICIgaWQ9InN2Z180IiBmaWxsPSIjRUI1QTI2IiBmaWxsLW9wYWNpdHk9IjEiLz4KCQkJPHBhdGggZD0iTTMwOC44LDI1Ny44bC01Ny41LDQ5LjhjLTMuNSwzLjEtOC44LDMuMS0xMi40LDBsLTU3LjctNDkuOEwxNy4xLDQwMC4yaDQ1NS40TDMwOC44LDI1Ny44eiIgaWQ9InN2Z181IiBmaWxsPSIjRUI1QTI2IiBmaWxsLW9wYWNpdHk9IjEiLz4KCQkJPHBvbHlnb24gcG9pbnRzPSIwLDEwMC43IDAsMzg5LjMgMTY2LjQsMjQ1ICAgICIgaWQ9InN2Z182IiBmaWxsPSIjRUI1QTI2IiBmaWxsLW9wYWNpdHk9IjEiLz4KCQkJPHBvbHlnb24gcG9pbnRzPSI0NzIuOSw4OS44IDE3LjEsODkuOCAyNDUsMjg3LjQgICAgIiBpZD0ic3ZnXzciIGZpbGw9IiNFQjVBMjYiIGZpbGwtb3BhY2l0eT0iMSIvPgoJCTwvZz4KCTwvZz4KPC9nPjxnIGlkPSJzdmdfOCI+CjwvZz48ZyBpZD0ic3ZnXzkiPgo8L2c+PGcgaWQ9InN2Z18xMCI+CjwvZz48ZyBpZD0ic3ZnXzExIj4KPC9nPjxnIGlkPSJzdmdfMTIiPgo8L2c+PGcgaWQ9InN2Z18xMyI+CjwvZz48ZyBpZD0ic3ZnXzE0Ij4KPC9nPjxnIGlkPSJzdmdfMTUiPgo8L2c+PGcgaWQ9InN2Z18xNiI+CjwvZz48ZyBpZD0ic3ZnXzE3Ij4KPC9nPjxnIGlkPSJzdmdfMTgiPgo8L2c+PGcgaWQ9InN2Z18xOSI+CjwvZz48ZyBpZD0ic3ZnXzIwIj4KPC9nPjxnIGlkPSJzdmdfMjEiPgo8L2c+PGcgaWQ9InN2Z18yMiI+CjwvZz48L2c+PC9zdmc+)](mailto:vsrc@vng.com.vn)

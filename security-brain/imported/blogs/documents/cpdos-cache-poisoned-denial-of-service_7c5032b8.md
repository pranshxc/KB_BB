---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-22_cpdos-cache-poisoned-denial-of-service.md
original_filename: 2019-10-22_cpdos-cache-poisoned-denial-of-service.md
title: 'CPDoS: Cache Poisoned Denial of Service'
category: documents
detected_topics:
- cloud-security
- command-injection
- mfa
- automation-abuse
- cors
- business-logic
tags:
- imported
- documents
- cloud-security
- command-injection
- mfa
- automation-abuse
- cors
- business-logic
language: en
raw_sha256: 7c5032b8b1939a28355854194dd39b4f1ddf1c40b753cf7ef68e16fc08f5e769
text_sha256: 66e601d95f801831ab0c19c57064217145c0e1b0a24d9adb84a40a2217cd52b8
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# CPDoS: Cache Poisoned Denial of Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-22_cpdos-cache-poisoned-denial-of-service.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, mfa, automation-abuse, cors, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7c5032b8b1939a28355854194dd39b4f1ddf1c40b753cf7ef68e16fc08f5e769`
- Text SHA256: `66e601d95f801831ab0c19c57064217145c0e1b0a24d9adb84a40a2217cd52b8`


## Content

---
title: "CPDoS: Cache Poisoned Denial of Service"
url: "https://cpdos.org"
final_url: "https://cpdos.org/"
authors: ["Hoai Viet Nguyen (@hvnguyen86)", "Luigi Lo Iacono, and Hannes Federrath"]
programs: ["Microsoft", "Amazon", "Akamai", "Cloudflare", "Yahoo! / Verizon Media", "Play Framework"]
bugs: ["DoS", "Web cache poisoning", "CPDoS"]
publication_date: "2019-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4977
---

[CPDoS](/) Toggle navigation

  * Attacks 
  * HTTP Header Oversize (HHO)
  * HTTP Meta Character (HMC)
  * HTTP Method Override (HMO)
  * Impact
  * Vulnerability Overview
  * Mitigations
  * Paper/Talks
  * Related Work
  * Coverage
  * Vendor Responses
  * Contact

![](/img/logo_2.png)

# **CPDoS** :  
**C** ache **P** oisoned **D** enial **o** f **S** ervice

# What is CPDoS?

**C** ache-**P** oisoned **D** enial-**o** f-**S** ervice (**CPDoS**) is a new class of [web cache poisoning attacks ](https://portswigger.net/research/practical-web-cache-poisoning)aimed at disabling web resources and websites.

* * *

# How does it work?

The basic attack flow is described below and depicted in the following figure:

  1. An attacker sends a simple HTTP request containing a **malicious header** targeting a victim resource provided by some web server. The request is processed by the intermediate cache, while the malicious header remains unobtrusive.

  2. The cache forwards the request to the origin server as it does not store a fresh copy of the targeted resource. At the origin server, the request processing provokes an **error** due to the malicious header it contains.

  3. As a consequence, the origin server returns an **error page** which gets stored by the cache instead of the requested resource.

  4. The attacker knows that the attack was successful when she retrieved an error page in response.

  5. Legitimate users trying to obtain the target resource with subsequent requests...

  6. ...will get the cached error page instead of the original content.

![](/img/CPDoS.png)

With CPDoS, a malicious client can block any web resource that is distributed via Content Distribution Networks (CDNs) or hosted on proxy caches. Note, that **a single crafted request** is sufficient to restrain all subsequent requests from accessing the targeted content.

* * *

# Which CPDoS variations exist?

We detected three variations of CPDoS:

  * HTTP Header Oversize (HHO)

  * HTTP Meta Character (HMC)

  * HTTP Method Override (HMO)

## HTTP Header Oversize (HHO)

An HTTP request header contains vital information for intermediate systems and web servers. This includes cache-related header fields or meta data on client supported media types, languages and encodings. The [HTTP standard](https://httpwg.org/specs/) does not define any size limit for HTTP request headers. As a consequence, intermediate systems, web servers, and web frameworks define limits by their own. Most web servers and proxies such as [Apache HTTPD](https://httpd.apache.org/) provide a request header size limit of around 8,192 bytes to mitigate, e.g., [Request Header Buffer Overflow](https://nvd.nist.gov/vuln/detail/CVE-2010-2730) or [ReDoS](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-staicu.pdf) attacks. However, there are also intermediate systems that specify limits larger than 8,192 bytes. For instance, the [Amazon Cloudfront CDN](https://aws.amazon.com/cloudfront/) allows up to 20,480 bytes. This semantic gap in terms of request header size limits can be exploited to conduct a cache poisoning attack which can lead to a denial of service. ​

HHO CPDoS attacks work in scenarios where a web application uses a cache that accepts a larger header size limit than the origin server. To attack such a web application, a malicious client sends a `HTTP GET` request including a header larger than the size supported by the origin server but smaller than the size supported by the cache. To do so, an attacker has two options. First, she crafts a request header with many malicious headers as shown in the following Ruby code snippet. The other option is to include one single header with an oversized key or value.
  
  
  require 'net/http'
  uri = URI("https://example.org/index.html")
  req = Net::HTTP::Get.new(uri)
  
  num = 200
  i = 0
  
  # Setting malicious and irrelevant headers fields for creating an oversized header
  until i > num  do
  req["X-Oversized-Header-#{i}"] = "Big-Value-0000000000000000000000000000000000"
  i +=1;
  end
  
  res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => uri.scheme == 'https') {|http|
  http.request(req)
  }
  

The figure below shows an HHO CPDoS attack flow in which a malicious client sends a request created by the above code snippet. The cache forwards this request including all headers to the endpoint since the header size remains below the size limit of 20,480 bytes. The web server, however, blocks this request and returns an error page, as the request header exceeds its header size limit. This error page with status code `400 Bad Request` is now stored by the cache. All subsequent requests targeting the denialed resource are now provided with an error page instead of the genuine content.

![HRS attack](/img/HHO.png)

The video demonstrates the HHO CPDoS attack with an example web application hosted on Cloudfront. In the attack, embedded web resources are selectively replaced by error pages rendering first some parts of the web page and finally the entire page unavailable.

* * *

## HTTP Meta Character (HMC)

The HTTP Meta Character (HMC) CPDoS attack works similar to the HHO CPDoS attack. Instead of sending an oversized header, this attack tries to bypass a cache with a request header containing a harmful meta character. Meta characters can be, e.g., control characters such as line break/carriage return (`\n`), line feed (`\r`) or bell (`\a`).

![](/img/HMC.png)

An unaware cache forwards such a request to the origin server without blocking the message or sanitizing the meta characters. The origin server, however, may classify such a request as malicious as it contains harmful meta characters. As a consequence, the origin server returns an error message which is stored and reused by the cache.

* * *

## HTTP Method Override Attack (HMO)

The [HTTP standard](https://httpwg.org/specs/) provides several HTTP methods for web servers and clients for performing transactions on the web. `GET`, `POST`, `DELETE` and `PUT` are arguably the most used HTTP methods in web applications and REST-based web services. Many intermediate systems such as proxies, load balancers, caches, and firewalls, however, do only support `GET` and `POST`. This means that HTTP requests with `DELETE` and `PUT` are simply blocked. To circumvent this restriction many REST-based APIs or web frameworks such as the [Play Framework 1](https://www.playframework.com/documentation/1.5.x/home), provide headers such as `X-HTTP-Method-Override`, `X-HTTP-Method` or `X-Method-Override` for tunnel blocked HTTP methods. Once the request reaches the server, the header instructs the web application to override the HTTP method in the request line with the one in the corresponding header value.
  
  
  POST /items/1 HTTP/1.1
  Host: example.org
  **X-HTTP-Method-Override: DELETE**
  
  HTTP/1.1 200 OK
  Content-Type: text/plain
  Content-Length: 62
  
  Resource has been successfully removed with the DELETE method.
  
  

The code snippet shows a request that can bypass a security policy that prohibits `DELETE` requests by using the `X-HTTP-Method-Override` header. On the server-side this `POST` request will be interpreted as a `DELETE` request.

These method overriding headers are very useful in scenarios when intermediate systems block distinct HTTP methods. However, if a web application supports such a header and also uses a web caching system like a reverse proxy cache or CDN for optimizing performance, a malicious client can exploit this constellation to conduct a CPDoS attack. The figure below illustrates the principle flow of an HTTP Method Override Attack (HMO) CPDoS attack using the `X-HTTP-Method-Override` header.

![HRS attack](/img/HMO.png)

Here, the attacker sends a `GET` request with an `X-HTTP-Method-Override` header containing `POST`. A vulnerable cache interprets this request as a benign `GET` request targeting the resource https://example.org/index.html. The web application, however, will interpret this request as a `POST` request, since the `X-HTTP-Method-Override` header instructs the server to replace the HTTP method in the request line. Accordingly, the web application returns a response based on `POST`. Let’s assume that the target web application doesn’t implement any business logic for `POST` on /index.html. In such cases, web frameworks like the [Play Framework 1](https://www.playframework.com/documentation/1.5.x/home) return an error message with the status code `404 Not Found`. The cache assumes that the returned response with the error code is the result of the `GET` request targeting https://example.org/index.html. Since the status code `404 Not Found` is allowed to be cached according to the [HTTP Caching RFC 7231](https://tools.ietf.org/html/rfc7231), caches store and reuse this error response for recurring requests. Each benign client making a subsequent `GET` request to https://example.org/index.html will receive a stored error message with status code `404 Not Found` instead of the genuine web application’s start page.

The video below demonstrates an HMO attack on a web application. Here, the attacker uses the [Postman](https://www.getpostman.com/downloads/) tool to block the start page from being accessed.

* * *

# Impact

The map below shows the impact of CPDoS attacks on CDNs. Once the error page is injected, the CDN distributes it to many other edge cache server locations around the world. The map illustrates how far the error page is distributed to several edge locations within the CDN. The ![](/img/red-pin.png) icons show the affected locations displaying the error page. Fortunately, not all edge servers are infected by this attack which is shown by the ![](/img/green-pin.png) icons. This icon denotes the locations where clients receive the genuine page. The ![](/img/blue-pin.png) icon shows the location of the origin server and the ![](/img/attacker.png) icon displays the attacker’s locations.

The first figure shows the affected regions in Europe and some parts of Asia when sending a CPDoS attack from Frankfurt, Germany to a victim origin server in Cologne, Germany. The second one illustrates the poisoned regions in the USA when executing a CPDoS attack from Northern Virginia, USA to the same victim origin server in Cologne, Germany. ![](/img/affected_regions_europe_cut.png)

![](/img/affected_regions_usa_cut.png)  

This analysis has been conducted with [TurboBytes Pulse](https://pulse.turbobytes.com/) and [the speed testing tool of KeyCDN](https://tools.keycdn.com/speed). Both services provide a testing environment covering a lot of test agents scattered around the world.

* * *

# CPDoS vulnerability overview

This overview summarizes what pair of web caching system and HTTP implementation is vulnerable to what CPDoS attack. More details are described in the paper which can be downloaded below. **Note, that the table below illustrates the results from our research experiments conducted in February 2019. In the meantime, the affected organizations have taken precautions to mitigate CPDoS attacks. The majority of the CPDoS vulnerabilities has been addressed by the respective organizations. Click on the info icons in the table or see the sectionVendor Responses to CPDoS for more details.**

HTTP ImplementationCache | Apache HTTPD | Apache TS | Nginx | Squid | Varnish | Akamai | Azure | CDN77 | CDNSun | Cloudflare | CloudFront | Fastly | G-Core Labs | KeyCDN | StackPath  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Apache HTTPD + (ModSecurity) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO, HMC | ○ | ○ | ○ | ○  
Apache TS | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○  
Nginx + (ModSecurity) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO | ○ | ○ | ○ | ○  
IIS | ○ | ○ | ○ | ○ | (HHO) | (HHO) | ○ | (HHO) | ○ | (HHO) | HHO, HMC | (HHO) | ○ | ○ | ○  
Tomcat | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO | ○ | ○ | ○ | ○  
Squid | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○  
Varnish | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO, HMC | ○ | ○ | ○ | ○  
Amazon S3 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO | ○ | ○ | ○ | ○  
Google Cloud Storage | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○  
Github Pages | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO, HMC | ○ | ○ | ○ | ○  
Gitlab Pages | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HMC | ○ | ○ | ○ | ○  
Heroku | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO | ○ | ○ | ○ | ○  
ASP.NET | ○ | ○ | ○ | ○ | (HHO) | (HHO) | ○ | (HHO) | ○ | (HHO) | (HHO), (HMC) | (HHO) | ○ | ○ | ○  
BeeGo | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HMC | ○ | ○ | ○ | ○  
Django | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | (HHO), (HMC) | ○ | ○ | ○ | ○  
Express.js | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HMC | ○ | ○ | ○ | ○  
Flask | ○ | ○ | ○ | ○ | ○ | (HMO) | ○ | ○ | ○ | ○ | HMO, (HHO), (HMC) | ○ | ○ | ○ | ○  
Gin | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HMC | ○ | ○ | ○ | ○  
Laravel | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | (HHO), (HMC) | ○ | ○ | ○ | ○  
Meteor.js | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HMC | ○ | ○ | ○ | ○  
Play 1 | ○ | ○ | ○ | ○ | HMO | HMO | ○ | HMO | ○ | HMO | HHO, HMO | HMO | ○ | ○ | ○  
Play 2 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO, HMC | ○ | ○ | ○ | ○  
Rails | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | (HHO), (HMC) | ○ | ○ | ○ | ○  
Spring Boot | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | HHO | ○ | ○ | ○ | ○  
Symfony | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | (HHO), (HMC) | ○ | ○ | ○ | ○  
  
* * *

# Mitigations

One of the main reasons for HHO and HMC CPDoS attacks lies in the fact that a vulnerable cache illicitly stores responses containing error codes such as `400 Bad Request` by default. This is not allowed according to the HTTP standard. The web caching standard only allows to cache the error codes `404 Not Found`, `405 Method Not Allowed`, `410 Gone` and `501 Not Implemented`. Hence, caching error pages according to the policies of the HTTP standard is the first step to avoid CPDoS attacks.

Content providers must also use the appropriate status code for the corresponding error case. For instance, `400 Bad Request` which is used by many HTTP implementations for declaring an oversized header is not the suitable status code. IIS even uses `404 Not Found` when a specific header is exceeded. The right error code for an oversized request header is `431 Request Header Fields Too Large`. According to our analysis, this error message is not cached by any web caching systems.

Another effective countermeasure against HHO and HMC CPDoS attacks is to exclude error pages from caching. One approach is to add the header `Cache-Control: no-store` to each error page. The other option is to disable error page caching in the cache configuration. CDNs like CloudFront or Akamai provide configuration settings to do so.

A Web Application Firewalls (WAF) can also be deployed to mitigate CPDoS attacks. However, WAFs must be placed in front of the cache in order to block malicious content before they reach the origin server. WAFs that are placed in front of the origin server can be exploited to provoke error pages that get cached either.

For more details on possible mitigations and countermeasures, please read our paper.

* * *

# Paper

For more details on CPDoS attacks, you are welcome to read our research paper. A preprint can be downloaded below.

_Hoai Viet Nguyen, Luigi Lo Iacono, and Hannes Federrath_  
**Your Cache Has Fallen: Cache-Poisoned Denial-of-Service Attack**  
26th ACM Conference on Computer and Communications Security (CCS) 2019  

Abstract  Bibtex  [Download](/paper/Your_Cache_Has_Fallen__Cache_Poisoned_Denial_of_Service_Attack__Preprint_.pdf)

#### Abstract

Web caching enables the reuse of HTTP responses with the aim to reduce the number of requests that reach the origin server, the volume of network traffic resulting from resource requests, and the user-perceived latency of resource access. For these reasons, a cache is a key component in modern distributed systems as it enables applications to scale at large. In addition to optimizing performance metrics, caches promote additional protection against Denial of Service (DoS) attacks.

In this paper we introduce and analyze a new class of web cache poisoning attacks. By provoking an error on the origin server that is not detected by the intermediate caching system, the cache gets poisoned with the server-generated error page and instrumented to serve this useless content instead of the intended one, rendering the victim service unavailable. In an extensive study of fifteen web caching solutions we analyzed the negative impact of the Cache-Poisoned DoS (CPDoS) attack---as we coined it. We show the practical relevance by identifying one proxy cache product and five CDN services that are vulnerable to CPDoS. Amongst them are prominent solutions that in turn cache high-value websites. The consequences are severe as one simple request is sufficient to paralyze a victim website within a large geographical region. The awareness of the newly introduced CPDoS attack is highly valuable for researchers for obtaining a comprehensive understanding of causes and countermeasures as well as practitioners for implementing robust and secure distributed systems.
  
  
  @inproceedings{conf/ccs2019/nguyen,
  author = {H.V. Nguyen and L. Lo Iacono and H. Federrath},
  title = {{Your Cache Has Fallen: Cache-Poisoned Denial-of-Service Attack}},
  booktitle = {{26th ACM Conference on Computer and Communications Security (CCS)}},
  year = {2019},
  url = {https://doi.org/10.1145/3319535.3354215},
  abstract = {{Web caching enables the reuse of HTTP responses with the aim to reduce the number of requests
  that reach the origin server, the volume of network traffic resulting from resource requests, and the user-
  perceived latency of resource access. For these reasons, a cache is a key component in modern distributed
  systems as it enables applications to scale at large. In addition to optimizing performance metrics, caches
  promote additional protection against Denial of Service (DoS) attacks.
  
  In this paper we introduce and analyze a new class of web cache poisoning attacks. By provoking an error on
  the origin server that is not detected by the intermediate caching system, the cache gets poisoned with the
  server-generated error page and instrumented to serve this useless content instead of the intended one,
  rendering the victim service unavailable. In an extensive study of fifteen web caching solutions we analyzed
  the negative impact of the Cache-Poisoned DoS (CPDoS) attack---as we coined it. We show the practical
  relevance by identifying one proxy cache product and five CDN services that are vulnerable to CPDoS. Amongst
  them are prominent solutions that in turn cache high-value websites. The consequences are severe as one simple
  request is sufficient to paralyze a victim website within a large geographical region. The awareness of the
  newly introduced CPDoS attack is highly valuable for researchers for obtaining a comprehensive understanding
  of causes and countermeasures as well as practitioners for implementing robust and secure distributed systems.
  }}
  }
  

* * *

# Talks

On November 14th, 2019, we will give a talk on CPDoS attacks at the CCS 2019. For more information, please take a look at the CCS’ agenda: [https://sigsac.org/ccs/CCS2019/…](https://sigsac.org/ccs/CCS2019/index.php/program/program-2/#Thursday)

* * *

# Related Work

HHO, HMC and HMO are not the only CPDoS variations. In March 2019, [Nathan Davison](https://nathandavison.com/blog/corsing-a-denial-of-service-via-cache-poisoning) has detected a CPDoS variation which use CORS headers. Also, Nathan posted a blog post on using the Connection header to conduct a CPDoS attack.

Moreover, James Kettle has published a [blog article](https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning) discussing other variations of CPDoS attacks on real world websites. James is Head of Research at PortSwigger Web Security. He wrote many blog articles on [practical web cache poisoning vulnerabilities](https://portswigger.net/research/practical-web-cache-poisoning) as well as a new variation of HTTP Request Smuggling denoted as [HTTP Desync Attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn).

* * *

# Coverage

www.hostingadvice.com  
_March 30, 2020_  
**Researchers Identify a New Cache Poisoning Attack Impacting CDNs That Could Block Web Resources and Sites**  
<https://www.hostingadvice.com/blog/researchers-identify-new-cache-poisoning-attack/>

nathandavison.com  
_February 24, 2020_  
**Cache poisoning DoS in CloudFoundry gorouter (CVE-2020-5401)**  
<https://nathandavison.com/blog/cache-poisoning-dos-in-cloudfoundry-gorouter>

Golem.de  
_October 23, 2019_  
**Cache-Angriffe können Webseiten lahmlegen**  
<https://www.golem.de/news/cpdos-angriff-cache-angriffe-koennen-webseiten-lahmlegen-1910-144575.html>

The Hacker News  
_October 23, 2019_  
**New Cache Poisoning Attack Lets Attackers Target CDN Protected Sites**  
<https://thehackernews.com/2019/10/cdn-cache-poisoning-dos-attack.html>

ZDNet  
_October 23, 2019_  
**CPDoS attack can poison CDNs to deliver error pages instead of legitimate sites**  
<https://www.zdnet.com/article/cpdos-attack-can-poison-cdns-to-deliver-error-pages-instead-of-legitimate-sites/>

Bleeping Computer  
_October 23, 2019_  
**New CPDoS Web Cache Poisoning Attacks Impact Sites Using Popular CDNs**  
<https://www.bleepingcomputer.com/news/security/new-cpdos-web-cache-poisoning-attacks-impact-sites-using-popular-cdns/>

Cyware  
_October 23, 2019_  
**New ‘CPDoS’ Web Cache Poisoning Attack Impacts Content Delivery Networks (CDN)**  
<https://cyware.com/news/new-cpdos-web-cache-poisoning-attack-impacts-content-delivery-networks-cdn-440ffccc/>

Security Affairs  
_October 23, 2019_  
**Exploring the CPDoS attack on CDNs: Cache Poisoned Denial of Service**  
<https://securityaffairs.co/wordpress/92859/hacking/cpdos-attack-cdns.html>

The Media HQ  
_October 23, 2019_  
**CPDoS attack can poison CDNs to deliver error pages instead of legitimate sites**  
<https://themediahq.com/cpdos-attack-can-poison-cdns-to-deliver-error-pages-instead-of-legitimate-sites/>

Reblaze _October 23, 2019_  
**CPDoS – A new DoS attack on the rise**  
<https://www.reblaze.com/blog/cpdos-new-dos-attacks-rise/>

SensorsTechForum  
_October 24, 2019_  
**Cache Poisoned Denial of Service (CPDoS) Attacks Used Against Content Delivery Networks**  
<https://sensorstechforum.com/cpdos-attacks-cdn/>

Naked Security  
_October 24, 2019_  
**Vulnerability in content distribution networks found by researchers**  
<https://nakedsecurity.sophos.com/2019/10/24/researchers-find-vulnerability-in-content-distribution-networks/>

ACM TECHNEWS  
_October 24, 2019_  
**CPDoS Attack Can Poison CDNs to Deliver Error Pages Instead of Legitimate Sites**  
<https://cacm.acm.org/news/240392-cpdos-attack-can-poison-cdns-to-deliver-error-pages-instead-of-legitimate-sites/fulltext>

Security Week  
_October 24, 2019_  
**Researchers Warn of New Cache-Poisoned DoS Attack Method**  
<https://www.securityweek.com/researchers-warn-new-cache-poisoned-dos-attack-method>

Cybers Guard  
_October 25, 2019_  
**Experts Warn of the Latest Cache-Poisoned Method of Attack**  
<https://cybersguards.com/experts-warn-of-the-latest-cache-poisoned-method-of-attack/>

* * *

# Vendor Responses to CPDoS

Play Framework  
_March 14, 2019_  
**Define allowed methods used in ‘X-HTTP-Method-Override’**  
<https://github.com/playframework/play1/issues/1300>

Microsoft  
_June 11, 2019_  
**CVE-2019-0941 | Microsoft IIS Server Denial of Service Vulnerability**  
<https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0941>

Amazon Web Services  
_September 7, 2019_  
**How CloudFront Processes and Caches HTTP 4xx and 5xx Status Codes from Your Origin**  
<https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HTTPStatusCodes.html>

Akamai  
_October 23, 2019_  
**CPDOS POISONING ATTACK**  
<https://blogs.akamai.com/2019/10/cpdos-poisoning-attack.html>

Cloudflare  
_October 24, 2019_  
**Cloudflare response to CPDoS exploits**  
<https://blog.cloudflare.com/cloudflare-response-to-cpdos-exploits/>

CDN77  
_October 23, 2019_  
**Our statement regarding today’s article published by @TheHackersNews CDN77 is not vulnerable to CPDoS attacks.** <https://twitter.com/CDN77com/status/1186971315217092612>

Verizon Digital Media  
_October 28, 2019_  
**CPDoS attack update**  
<https://www.verizondigitalmedia.com/blog/cpdos-attack-update/>

* * *

# Contact

![...](/img/viet.jpg)

### Hoai Viet Nguyen

[](mailto:viet.nguyen@th-koeln.de) [](https://das.th-koeln.de)

![...](/img/luigi.jpg)

### Luigi Lo Iacono

[](mailto:luigi.lo_iacono@th-koeln.de) [](https://das.th-koeln.de)

×

#### Imprint

# Legal Disclosure

Information in accordance with section 5 TMG

TH Köln - University of Applied Sciences  
F07/IMP  
Data and Application Security Group  
Gustav-Heinemann-Ufer 54  
50968 Cologne

## Represented by

Prof. Dr. Luigi Lo Iacono

## Contact

Telephone: 0221/8275-2527  
E-Mail: luigi.lo_iacono at th-koeln.de  
Website: [das.th-koeln.de](http://das.th-koeln.de)

## Person responsible for content in accordance with 55 Abs. 2 RStV

  * Hoai Viet Nguyen
  * Luigi Lo Iacono

## Indication of source for images and graphics

Bomb, Recycle, and Server and icons made by [Freepik](https://www.flaticon.com/authors/freepik "Freepik") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")

404 icon made by [DinosoftLabs](https://www.flaticon.com/authors/dinosoftlabs "DinosoftLabs") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")

Cloud icon made by [Smashicons](https://www.flaticon.com/authors/smashicons "Smashicons") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")

Explosion icon made by [Good Ware](https://www.flaticon.com/authors/good-ware "Good Ware") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")

## Disclaimer

Accountability for content  
The contents of our pages have been created with the utmost care. However, we cannot guarantee the contents’ accuracy, completeness or topicality. According to statutory provisions, we are furthermore responsible for our own content on these web pages. In this context, please note that we are accordingly not obliged to monitor merely the transmitted or saved information of third parties, or investigate circumstances pointing to illegal activity. Our obligations to remove or block the use of information under generally applicable laws remain unaffected by this as per §§ 8 to 10 of the Telemedia Act (TMG).

Accountability for links  
Responsibility for the content of external links (to web pages of third parties) lies solely with the operators of the linked pages. No violations were evident to us at the time of linking. Should any legal infringement become known to us, we will remove the respective link immediately.

Copyright  
Our web pages and their contents are subject to German copyright law. Unless expressly permitted by law (§ 44a et seq. of the copyright law), every form of utilizing, reproducing or processing works subject to copyright protection on our web pages requires the prior consent of the respective owner of the rights. Individual reproductions of a work are allowed only for private use, so must not serve either directly or indirectly for earnings. Unauthorized utilization of copyrighted works is punishable (§ 106 of the copyright law).

* * *

# Datenschutzerklärung

  * A. Name und Anschrift des Verantwortlichen
  * B. Name und Anschrift der Datenschutzbeauftragten der TH Köln
  * C. Aufsichtsbehörde in Datenschutzangelegenheiten
  * D. Allgemeines zur Datenverarbeitung
  * E. Bereitstellung der Webseite und Erstellung von Logfiles
  * F. Rechte betroffener Personen

## A. Name und Anschrift des Verantwortlichen

Verantwortlicher im Sinne der EU-Datenschutzgrundverordnung (DS-GVO) und anderer nationaler Datenschutzgesetze sowie sonstiger datenschutzrechtlicher Bestimmungen ist:  
  
TH Köln  
Gruppe für Daten- und Anwendungssicherheit  
Prof. Dr. Luigi Lo Iacono  
Betzdorfer Str. 2  
50679 Köln  
T: +49 221-8275-2527  
E-Mail: luigi.lo_iacono@th-koeln.de  
Webseite: cpdos.org

## B. Name und Anschrift der Datenschutzbeauftragten der TH Köln

Walter Keens  
Claudiusstraße 1  
50678 Köln  
T: +49 221 8275 3108  
E: datenschutzbeauftragter@th-koeln.de

Bernadette Schmitz  
Claudiusstraße 1  
50678 Köln  
T: +49 221 8275 3994  
E: datenschutzbeauftragter@th-koeln.de

## C. Aufsichtsbehörde in Datenschutzangelegenheiten

Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW)  
Kavalleriestr. 2-4  
40213 Düsseldorf  
Telefon: 0211/38424-0  
Fax: 0211/38424-10  
E-Mail: poststelle@ldi.nrw.de

## D. Allgemeines zur Datenverarbeitung

1\. Umfang der Verarbeitung personenbezogener Daten

Die TH Köln verarbeitet personenbezogene Daten von Webseiten-Nutzenden grundsätzlich nur, soweit dies zur Bereitstellung einer funktionsfähigen Webseite sowie der Inhalte und Angebote erforderlich ist. Die Verarbeitung personenbezogener Daten von Webseiten-Nutzenden erfolgt regelmäßig nur gemäß erteilter Einwilligung. Eine Ausnahme gilt in solchen Fällen, in denen eine vorherige Einholung einer Einwilligung aus tatsächlichen Gründen nicht möglich ist und die Verarbeitung der Daten durch gesetzliche Vorschriften erlaubt ist.

2\. Rechtsgrundlage für die Verarbeitung personenbezogener Daten

Soweit die TH Köln personenbezogene Daten gemäß erteilter Einwilligung verarbeitet, stellt Art. 6 Abs. 1 lit. a DS-GVO die Rechtsgrundlage dar.

Bei der Verarbeitung von personenbezogenen Daten, die zur Erfüllung eines Vertrages, dessen Vertragspartei die betroffene Person ist, erforderlich ist, ergibt sich die Rechtsgrundlage aus Art. 6 Abs. 1 lit. b DS-GVO. Dies gilt auch für Verarbeitungstätigkeiten, die zur Durchführung vorvertraglicher Maßnahmen erforderlich sind.

Soweit eine Verarbeitung personenbezogener Daten zur Erfüllung einer rechtlichen Verpflichtung erforderlich ist, der die TH Köln als Körperschaft des öffentlichen Rechts unterliegt, dient Art. 6 Abs. 1 lit. c DS-GVO als Rechtsgrundlage.

Für den Fall, dass lebenswichtige Interessen der betroffenen Person oder einer anderen natürlichen Person eine Verarbeitung personenbezogener Daten erforderlich machen, stellt Art. 6 Abs. 1 lit. d DS-GVO die Rechtsgrundlage dar.

Ist die Verarbeitung zur Wahrung eines berechtigten Interesses der TH Köln oder eines Dritten erforderlich und überwiegen die Interessen, Grundrechte und Grundfreiheiten des Betroffenen das erstgenannte Interesse nicht, so ergibt sich die Rechtsgrundlage aus Art. 6 Abs. 1 lit. f DS-GVO.

3\. Datenlöschung und Speicherdauer

Die personenbezogenen Daten der betroffenen Person werden gelöscht oder gesperrt, sobald der Zweck der Speicherung entfällt. Eine Speicherung kann darüber hinaus erfolgen, wenn dies durch den europäischen oder nationalen Gesetzgeber in unionsrechtlichen Verordnungen, Gesetzen oder sonstigen Vorschriften, denen die TH Köln unterliegt, vorgesehen wurde. Eine Sperrung oder Löschung der Daten erfolgt auch dann, wenn eine durch die genannten Normen vorgeschriebene Speicherfrist abläuft, es sei denn, dass eine Erforderlichkeit zur weiteren Speicherung der Daten für einen Vertragsabschluss, eine Vertragserfüllung oder zur Erfüllung einer Aufbewahrungspflicht besteht.

## E. Bereitstellung der Webseite und Erstellung von Logfiles

1\. Beschreibung und Umfang der Datenverarbeitung

Bei jedem Aufruf unserer Internetseite erfasst die TH Köln automatisiert Daten und Informationen vom Computersystem des aufrufenden Rechners.

Folgende Daten werden hierbei erhoben:

  1. Die IP-Adresse der Nutzenden
  2. Datum und Uhrzeit des Zugriffs
  3. Webseiten, die vom System der Nutzenden über unsere Webseite aufgerufen werden
  4. Das Betriebssystem der Nutzenden
  5. Informationen über den Browsertyp und die verwendete Version
  6. Webseiten, von denen das System der Nutzenden auf unsere Internetseite gelangt
  7. Den Internet-Service-Provider der Nutzenden

Die Daten werden ebenfalls in den Logfiles von Systemen der TH Köln gespeichert. Eine Speicherung dieser Daten zusammen mit anderen personenbezogenen Daten der Nutzenden findet nicht statt. 

2\. Rechtsgrundlage für die Datenverarbeitung

Rechtsgrundlage für die Speicherung der Daten ist Art. 6 Abs. 1 lit. a DS-GVO.

3\. Zweck der Datenverarbeitung

Die vorübergehende Speicherung der IP-Adresse durch das System ist notwendig, um eine Auslieferung der Webseite an den Rechner der Nutzenden zu ermöglichen. Hierfür muss die IP-Adresse der Nutzenden für die Dauer der Sitzung gespeichert bleiben.

Die Speicherung in Logfiles erfolgt, um die Funktionsfähigkeit der Webseite sicherzustellen. Zudem dienen die Daten zur Optimierung der Webseite und zur Sicherstellung der Sicherheit der informationstechnischen Systeme der TH Köln. Eine Auswertung der Daten zu Marketingzwecken findet in diesem Zusammenhang nicht statt.

Das berechtigte Interesse der TH Köln an der Datenverarbeitung nach Art. 6 Abs. 1 lit. f DS-GVO stützt sich auf diese Zwecke.

4\. Dauer der Speicherung

Die Daten werden gelöscht, sobald sie für die Erreichung des Zwecks ihrer Erhebung nicht mehr erforderlich sind. Im Falle der Erfassung der Daten zur Bereitstellung der Webseite ist dies der Fall, wenn die jeweilige Sitzung beendet ist.

Im Falle der Speicherung der Daten in Logfiles ist dies nach spätestens sieben Tagen der Fall. In diesem Fall werden die IP-Adressen der Nutzer gelöscht oder verfremdet, sodass eine Zuordnung des aufrufenden Clients nicht mehr möglich ist.

5\. Widerspruchs- und Beseitigungsmöglichkeit

Die Erfassung der Daten zur Bereitstellung der Webseite und die Speicherung der Daten in Logfiles ist für den Betrieb der Internetseite zwingend erforderlich. Es besteht folglich seitens der Nutzenden keine Widerspruchsmöglichkeit. 

## F. Rechte betroffener Personen

Werden personenbezogene Daten von Ihnen verarbeitet, gehören Sie zu den Betroffenen i.S.d. DS-GVO und es stehen Ihnen folgende Rechte gegenüber der TH Köln zu:

1\. Auskunftsrecht

Sie können von der TH Köln eine Bestätigung darüber verlangen, ob personenbezogene Daten, die Sie betreffen, von uns verarbeitet werden. Liegt eine solche Verarbeitung vor, können Sie von der TH Köln über folgende Informationen Auskunft verlangen:

  1. die Zwecke, zu denen die personenbezogenen Daten verarbeitet werden;

  2. die Kategorien von personenbezogenen Daten, welche verarbeitet werden;

  3. die Empfänger bzw. die Kategorien von Empfängern, gegenüber denen die Sie betreffenden personenbezogenen Daten offengelegt wurden oder noch offengelegt werden;

  4. die geplante Dauer der Speicherung der Sie betreffenden personenbezogenen Daten oder, falls konkrete Angaben hierzu nicht möglich sind, Kriterien für die Festlegung der Speicherdauer;

  5. das Bestehen eines Rechts auf Berichtigung oder Löschung der Sie betreffenden personenbezogenen Daten, eines Rechts auf Einschränkung der Verarbeitung durch die TH Köln oder eines Widerspruchsrechts gegen diese Verarbeitung;

  6. das Bestehen eines Beschwerderechts bei einer Aufsichtsbehörde;

  7. alle verfügbaren Informationen über die Herkunft der Daten, wenn die personenbezogenen Daten nicht bei der betroffenen Person erhoben werden;

  8. das Bestehen einer automatisierten Entscheidungsfindung einschließlich Profiling gemäß Art. 22 Abs. 1 und 4 DS-GVO und – zumindest in diesen Fällen – aussagekräftige Informationen über die involvierte Logik sowie die Tragweite und die angestrebten Auswirkungen einer derartigen Verarbeitung für die betroffene Person.

Ihnen steht das Recht zu, Auskunft darüber zu verlangen, ob die Sie betreffenden personenbezogenen Daten in ein Drittland oder an eine internationale Organisation übermittelt werden. In diesem Zusammenhang können Sie verlangen, über die geeigneten Garantien gem. Art. 46 DS-GVO im Zusammenhang mit der Übermittlung unterrichtet zu werden.

Dieses Auskunftsrecht kann insoweit beschränkt werden, als es voraussichtlich die Verwirklichung der Forschungs- oder Statistikzwecke unmöglich macht oder ernsthaft beeinträchtigt und die Beschränkung für die Erfüllung der Forschungs- oder Statistikzwecke notwendig ist.

2\. Recht auf Berichtigung

Sie haben ein Recht auf Berichtigung und/oder Vervollständigung gegenüber der TH Köln, sofern die verarbeiteten personenbezogenen Daten, die Sie betreffen, unrichtig oder unvollständig sind. Die TH Köln hat die Berichtigung unverzüglich vorzunehmen.  
Ihr Recht auf Berichtigung kann insoweit beschränkt werden, als es voraussichtlich die Verwirklichung der Forschungs- oder Statistikzwecke unmöglich macht oder ernsthaft beeinträchtigt und die Beschränkung für die Erfüllung der Forschungs- oder Statistikzwecke notwendig ist.

3\. Recht auf Einschränkung der Verarbeitung

Unter den folgenden Voraussetzungen können Sie die Einschränkung der Verarbeitung der Sie betreffenden personenbezogenen Daten verlangen:

  1. wenn Sie die Richtigkeit der Sie betreffenden personenbezogenen Daten für eine Dauer bestreiten, die es der TH Köln ermöglicht, die Richtigkeit der personenbezogenen Daten zu überprüfen;

  2. die Verarbeitung unrechtmäßig ist und Sie die Löschung der personenbezogenen Daten ablehnen und stattdessen die Einschränkung der Nutzung der personenbezogenen Daten verlangen;

  3. die TH Köln die personenbezogenen Daten für die Zwecke der Verarbeitung nicht länger benötigt, Sie diese jedoch zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen benötigen, oder

  4. wenn Sie Widerspruch gegen die Verarbeitung gemäß Art. 21 Abs. 1 DS-GVO eingelegt haben und noch nicht feststeht, ob die berechtigten Gründe der TH Köln gegenüber Ihren Gründen überwiegen.

Wurde die Verarbeitung der Sie betreffenden personenbezogenen Daten eingeschränkt, dürfen diese Daten – von ihrer Speicherung abgesehen – nur mit Ihrer Einwilligung oder zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen oder zum Schutz der Rechte einer anderen natürlichen oder juristischen Person oder aus Gründen eines wichtigen öffentlichen Interesses der Union oder eines Mitgliedstaats verarbeitet werden.  
Wurde die Einschränkung der Verarbeitung nach den o.g. Voraussetzungen eingeschränkt, werden Sie von der TH Köln unterrichtet bevor die Einschränkung aufgehoben wird.

Ihr Recht auf Einschränkung der Verarbeitung kann insoweit beschränkt werden, als es voraussichtlich die Verwirklichung der Forschungs- oder Statistikzwecke unmöglich macht oder ernsthaft beeinträchtigt und die Beschränkung für die Erfüllung der Forschungs- oder Statistikzwecke notwendig ist.

4\. Recht auf Löschung

  1. Löschungspflicht  
Sie können von der TH Köln verlangen, dass die Sie betreffenden personenbezogenen Daten unverzüglich gelöscht werden, und die TH Köln ist verpflichtet, diese Daten unverzüglich zu löschen, sofern einer der folgenden Gründe zutrifft:

  * Die Sie betreffenden personenbezogenen Daten sind für die Zwecke, für die sie erhoben oder auf sonstige Weise verarbeitet wurden, nicht mehr notwendig.
  * Sie widerrufen Ihre Einwilligung, auf die sich die Verarbeitung gem. Art. 6 Abs. 1 lit. a oder Art. 9 Abs. 2 lit. a DS-GVO stützte, und es fehlt an einer anderweitigen Rechtsgrundlage für die Verarbeitung.
  * Sie legen gem. Art. 21 Abs. 1 DS-GVO Widerspruch gegen die Verarbeitung ein und es liegen keine vorrangigen berechtigten Gründe für die Verarbeitung vor, oder Sie legen gem. Art. 21 Abs. 2 DS-GVO Widerspruch gegen die Verarbeitung ein.
  * Die Sie betreffenden personenbezogenen Daten wurden unrechtmäßig verarbeitet.
  * Die Löschung der Sie betreffenden personenbezogenen Daten ist zur Erfüllung einer rechtlichen Verpflichtung nach dem Unionsrecht oder dem Recht der Mitgliedstaaten erforderlich, dem die TH Köln unterliegt.
  * Die Sie betreffenden personenbezogenen Daten wurden in Bezug auf angebotene Dienste der Informationsgesellschaft gemäß Art. 8 Abs. 1 DS-GVO erhoben.

  2. Information an Dritte  
Hat die TH Köln die Sie betreffenden personenbezogenen Daten öffentlich gemacht und ist sie gem. Art. 17 Abs. 1 DS-GVO zu deren Löschung verpflichtet, so trifft sie unter Berücksichtigung der verfügbaren Technologie und der Implementierungskosten angemessene Maßnahmen, auch technischer Art, um für die Datenverarbeitung TH Köln, die die personenbezogenen Daten verarbeiten, darüber zu informieren, dass Sie als betroffene Person von Ihnen die Löschung aller Links zu diesen personenbezogenen Daten oder von Kopien oder Replikationen dieser personenbezogenen Daten verlangt haben.

  3. Ausnahmen  
Das Recht auf Löschung besteht nicht, soweit die Verarbeitung erforderlich ist

  * zur Ausübung des Rechts auf freie Meinungsäußerung und Information;
  * zur Erfüllung einer rechtlichen Verpflichtung, die die Verarbeitung nach dem Recht der Union oder der Mitgliedstaaten, dem die TH Köln unterliegt, erfordert, oder zur Wahrnehmung einer Aufgabe, die im öffentlichen Interesse liegt oder in Ausübung öffentlicher Gewalt erfolgt, die der TH Köln übertragen wurde;
  * aus Gründen des öffentlichen Interesses im Bereich der öffentlichen Gesundheit gemäß Art. 9 Abs. 2 lit. h und i sowie Art. 9 Abs. 3 DS-GVO;
  * für im öffentlichen Interesse liegende Archivzwecke, wissenschaftliche oder historische Forschungszwecke oder für statistische Zwecke gem. Art. 89 Abs. 1 DS-GVO, soweit das unter Abschnitt a) genannte Recht voraussichtlich die Verwirklichung der Ziele dieser Verarbeitung unmöglich macht oder ernsthaft beeinträchtigt, oder
  * zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen.

5\. Recht auf Unterrichtung  
Haben Sie das Recht auf Berichtigung, Löschung oder Einschränkung der Verarbeitung gegenüber der TH Köln geltend gemacht, ist dieser verpflichtet, allen Empfängern, denen die Sie betreffenden personenbezogenen Daten offengelegt wurden, diese Berichtigung oder Löschung der Daten oder Einschränkung der Verarbeitung mitzuteilen, es sei denn, dies erweist sich als unmöglich oder ist mit einem unverhältnismäßigen Aufwand verbunden.  
Ihnen steht gegenüber der TH Köln das Recht zu, über diese Empfänger unterrichtet zu werden.

6\. Recht auf Datenübertragbarkeit

Sie haben das Recht, die Sie betreffenden personenbezogenen Daten, die Sie der TH Köln bereitgestellt haben, in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten. Außerdem haben Sie das Recht diese Daten einem anderen TH Köln ohne Behinderung durch den TH Köln, dem die personenbezogenen Daten bereitgestellt wurden, zu übermitteln, sofern

  1. die Verarbeitung auf einer Einwilligung gem. Art. 6 Abs. 1 lit. a DS-GVO oder Art. 9 Abs. 2 lit. a DS-GVO oder auf einem Vertrag gem. Art. 6 Abs. 1 lit. b DS-GVO beruht und

  2. die Verarbeitung mithilfe automatisierter Verfahren erfolgt.

In Ausübung dieses Rechts haben Sie ferner das Recht, zu erwirken, dass die Sie betreffenden personenbezogenen Daten direkt von der TH Köln einem anderen Verantwortlichen übermittelt werden, soweit dies technisch machbar ist. Freiheiten und Rechte anderer Personen dürfen hierdurch nicht beeinträchtigt werden.  
Das Recht auf Datenübertragbarkeit gilt nicht für eine Verarbeitung personenbezogener Daten, die für die Wahrnehmung einer Aufgabe erforderlich ist, die im öffentlichen Interesse liegt oder in Ausübung öffentlicher Gewalt erfolgt, die der TH Köln übertragen wurde.

7\. Widerspruchsrecht

Sie haben das Recht, aus Gründen, die sich aus ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung der Sie betreffenden personenbezogenen Daten, die aufgrund von Art. 6 Abs. 1 lit. e oder f DS-GVO erfolgt, Widerspruch einzulegen; dies gilt auch für ein auf diese Bestimmungen gestütztes Profiling.

Die TH Köln verarbeitet die Sie betreffenden personenbezogenen Daten nicht mehr, es sei denn, sie kann zwingende schutzwürdige Gründe für die Verarbeitung nachweisen, die Ihre Interessen, Rechte und Freiheiten überwiegen, oder die Verarbeitung dient der Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen.

Sie haben auch das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, bei der Verarbeitung Sie betreffender personenbezogener Daten, die zu wissenschaftlichen oder historischen Forschungszwecken oder zu statistischen Zwecken gem. Art. 89 Abs. 1 DS-GVO erfolgt, dieser zu widersprechen.

Ihr Widerspruchsrecht kann insoweit beschränkt werden, als es voraussichtlich die Verwirklichung der Forschungs- oder Statistikzwecke unmöglich macht oder ernsthaft beeinträchtigt und die Beschränkung für die Erfüllung der Forschungs- oder Statistikzwecke notwendig ist.

8\. Recht auf Widerruf der datenschutzrechtlichen Einwilligungserklärung

Sie haben das Recht, Ihre datenschutzrechtliche Einwilligungserklärung jederzeit zu widerrufen. Durch den Widerruf der Einwilligung wird die Rechtmäßigkeit der aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung nicht berührt.

9\. Automatisierte Entscheidung im Einzelfall einschließlich Profiling

Sie haben das Recht, nicht einer ausschließlich auf einer automatisierten Verarbeitung – einschließlich Profiling – beruhenden Entscheidung unterworfen zu werden, die Ihnen gegenüber rechtliche Wirkung entfaltet oder Sie in ähnlicher Weise erheblich beeinträchtigt. Dies gilt nicht, wenn die Entscheidung

  1. für den Abschluss oder die Erfüllung eines Vertrags zwischen Ihnen und der TH Köln erforderlich ist,

  2. aufgrund von Rechtsvorschriften der Union oder der Mitgliedstaaten, denen die TH Köln unterliegt, zulässig ist und diese Rechtsvorschriften angemessene Maßnahmen zur Wahrung Ihrer Rechte und Freiheiten sowie Ihrer berechtigten Interessen enthalten oder

  3. mit Ihrer ausdrücklichen Einwilligung erfolgt.

Allerdings dürfen diese Entscheidungen nicht auf besonderen Kategorien personenbezogener Daten nach Art. 9 Abs. 1 DS-GVO beruhen, sofern nicht Art. 9 Abs. 2 lit. a oder g DS-GVO gilt und angemessene Maßnahmen zum Schutz der Rechte und Freiheiten sowie Ihrer berechtigten Interessen getroffen wurden. Hinsichtlich der in (a) und (c) genannten Fälle trifft die TH Köln angemessene Maßnahmen, um die Rechte und Freiheiten sowie Ihre berechtigten Interessen zu wahren, wozu mindestens das Recht auf Erwirkung des Eingreifens einer Person seitens der TH Köln, auf Darlegung des eigenen Standpunkts und auf Anfechtung der Entscheidung gehört.

10\. Recht auf Beschwerde bei einer Aufsichtsbehörde

Unbeschadet eines anderweitigen verwaltungsrechtlichen oder gerichtlichen Rechtsbehelfs steht Ihnen das Recht auf Beschwerde bei einer Aufsichtsbehörde, insbesondere in dem Mitgliedstaat Ihres Aufenthaltsorts, Ihres Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes, zu, wenn Sie der Ansicht sind, dass die Verarbeitung der Sie betreffenden personenbezogenen Daten gegen die DS-GVO verstößt.

Die Aufsichtsbehörde, bei der die Beschwerde eingereicht wurde, unterrichtet den Beschwerdeführer über den Stand und die Ergebnisse der Beschwerde einschließlich der Möglichkeit eines gerichtlichen Rechtsbehelfs nach Art. 78 DS-GVO.

Close

Copyright © Data & Application Security Group, TH Köln - University of Applied Sciences  
Last updated March 30, 2020

Copyright © DAS Group  
Last updated 30.03.2020

Imprint

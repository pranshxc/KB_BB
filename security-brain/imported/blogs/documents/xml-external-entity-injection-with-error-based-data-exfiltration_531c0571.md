---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-29_xml-external-entity-injection-with-error-based-data-exfiltration.md
original_filename: 2024-01-29_xml-external-entity-injection-with-error-based-data-exfiltration.md
title: XML External Entity injection with error-based data exfiltration
category: documents
detected_topics:
- ssrf
- command-injection
- information-disclosure
tags:
- imported
- documents
- ssrf
- command-injection
- information-disclosure
language: en
raw_sha256: 531c0571ce3d8b357d6e6a1977e3f3d2091d31d50f414310b8046dd86e212492
text_sha256: 541a1000d9012970be94fc0e71891d9103c9d7e62d95eb6bb572737104270f50
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# XML External Entity injection with error-based data exfiltration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-29_xml-external-entity-injection-with-error-based-data-exfiltration.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `531c0571ce3d8b357d6e6a1977e3f3d2091d31d50f414310b8046dd86e212492`
- Text SHA256: `541a1000d9012970be94fc0e71891d9103c9d7e62d95eb6bb572737104270f50`


## Content

---
title: "XML External Entity injection with error-based data exfiltration"
url: "https://infosecwriteups.com/xml-external-entity-injection-with-error-based-data-exfiltration-985b063ec820"
authors: ["Serj Novoselov (@novoselov_s)"]
bugs: ["XXE"]
publication_date: "2024-01-29"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 487
scraped_via: "browseros"
---

# XML External Entity injection with error-based data exfiltration

XML External Entity injection with error-based data exfiltration
Serj Novoselov
Follow
4 min read
·
Jan 29, 2024

149

1

Introduction

In a recent project, I’ve uncovered a significant security issue that revolves around XML External Entity attacks.

This article delves into my journey of identifying and exploiting the XXE threat in our project in an unusual way to output the attack results — via Java exceptions in the log files.

Press enter or click to view image in full size
What is XXE?

XML External Entity (XXE) is a security vulnerability that occurs in applications handling XML input. In an XXE attack, an attacker can exploit an application’s XML parser to include external entities, which can lead to a range of malicious actions, such as reading local files, initiating server requests, or even executing arbitrary code on the server. This type of vulnerability can have severe consequences if not addressed, making it a crucial concern in the realm of cybersecurity.

XXE
The issue: initial foothold

As I dove into comprehensive testing for my recent project, I encountered an alarming functionality. The project’s solution allowed for the upload of schema files that incorporated XML markup, opening the door to XXE vulnerabilities.

Intrigued, I decided to delve deeper into this potential threat. My initial breakthrough came when I discovered an XXE that allowed Server-Side Request Forgery (SSRF) vulnerability. SSRF is a type of security vulnerability that occurs when an attacker tricks a server into making unintended requests to other resources on the server’s internal network or to external websites.

This vulnerability was achieved by injecting the following XXE payload inside the schema file:

With this payload in hand, I simply created a schema file from a template and appended it with the payload.

After creating the schema, I proceeded with uploading it into the system:

Press enter or click to view image in full size
Uploading the evil schema file

The application, by default, auto-processes the schema after upload. After loading, the error will occur due to the invalid schema file (because of the injection):

Press enter or click to view image in full size
XML Error

Despite the error, the injected XML entity was still processed, causing the server’s backend to perform an HTTP request. This was the defining moment in the discovery, as I successfully achieved an SSRF.

Press enter or click to view image in full size
SSRF successful

I soon realized that reading files was not feasible, as no direct output was available. All we received was a generic error message. The schema file needed to adhere to a specific template, rendering techniques like DTD with multiple instructions were impractical, due to the XML parsing error after the first instruction.

Weaponizing The Server Logs

But I was undeterred, determined to find a way to disclose files on the target machine. My continued exploration led me to a solution: the application had a logging functionality, and logs could be displayed. This revelation opened a new path for me.

Get Serj Novoselov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My quest to extract valuable information from the processed injected XML entities took shape.

I created a schema from a template containing a payload that declares an entity, loading an external XML DTD.

An external DTD allows the application to reference a separate file for defining XML structure, providing an avenue for potential exploitation:

Press enter or click to view image in full size

Then I prepared the evil.dtd file itself on the remote host:

Same as previously I uploaded a schema file from a template and appended it with my payload:

Press enter or click to view image in full size
Referencing an external DTD

The schema uploads but the loading process fails due to an error as usual:

However, this way it will still load the external DTD (evil.dtd) and process it:

The payload in the DTD file triggers a server exception by referencing a non-existent file. This file name is created by combining the ‘nonexistent/’ path with a string that represents the listing of the C:/ drive.
Basically, the unhandled exception text will look like:

Error, non-existing file at: file:///nonexistent/(C:/)LISTING.

And this text will appear in the error log:

Press enter or click to view image in full size
Listing of C:/

Besides directory listing, this technique could be used to read a file as well. By manipulating the content of the DTD file, an attacker could target specific files within the system:

Press enter or click to view image in full size
Press enter or click to view image in full size
File read successful

🌐 My social networks: https://linktr.ee/s_novoselov

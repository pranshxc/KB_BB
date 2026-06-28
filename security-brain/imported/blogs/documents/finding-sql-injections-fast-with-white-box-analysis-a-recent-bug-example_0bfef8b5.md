---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-13_finding-sql-injections-fast-with-white-box-analysis-a-recent-bug-example.md
original_filename: 2019-10-13_finding-sql-injections-fast-with-white-box-analysis-a-recent-bug-example.md
title: Finding SQL injections fast with white-box analysis — a recent bug example
category: documents
detected_topics:
- command-injection
- sqli
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- sqli
- path-traversal
- api-security
language: en
raw_sha256: 0bfef8b55c3c877021ed6c2dddb365d8698458e72e9e73b29062ca65dcb9ef08
text_sha256: 450022b8dc33160bac4109819a907d1a839f4bb474d639489cd30ba229cc94e9
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Finding SQL injections fast with white-box analysis — a recent bug example

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-13_finding-sql-injections-fast-with-white-box-analysis-a-recent-bug-example.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0bfef8b55c3c877021ed6c2dddb365d8698458e72e9e73b29062ca65dcb9ef08`
- Text SHA256: `450022b8dc33160bac4109819a907d1a839f4bb474d639489cd30ba229cc94e9`


## Content

---
title: "Finding SQL injections fast with white-box analysis — a recent bug example"
url: "https://medium.com/@frycos/finding-sql-injections-fast-with-white-box-analysis-a-recent-bug-example-ca449bce6c76"
authors: ["Florian Hauser (@frycos)"]
programs: ["Zoho"]
bugs: ["SQL injection"]
publication_date: "2019-10-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4989
scraped_via: "browseros"
---

# Finding SQL injections fast with white-box analysis — a recent bug example

Finding SQL injections fast with white-box analysis — a recent bug example
frycos
Follow
4 min read
·
Oct 13, 2019

386

2

On September 13rd I submitted a bug for Zoho’s OpManager product. It was fixed quite fast by the development team and a new version 12.4 (Build no 124089) was released on October 3rd (CVE-2019–17602).

This is a short story how I found this bug from a methodological perspective, especially regarding white-box analysis. In the last months I started to shift my focus from black-box testing to a more white-boxed approach. Reading code not only makes fun but rather gives insight into a more detailed understanding of bugs as well as a chance to find bugs with quite some preconditions.

Since Java (and other languages of course) “compiles” into byte-code, it can easily be decompiled back into it’s source. So I downloaded (more or less randomly) the latest ManageEngine OpManager from their website and decompiled all JAR files for a deeper white-box analyses.

So besides decompilation of code, how is a standard Java web application structured? From an attacker’s perspective there is not only code but also configuration files (.xml, .properties, etc.). Especially, for Java web applications several configurations are done within the file web.xml. For a deployed web application, it’s usually stored in the protected WEB-INF directory.

So how could this file help us? E.g. one can read how Java files/classes are used and mapped to URLs. Of special interested to us are so called Servlets. These special classes have methods like doGet or doPost which are executed for every request matching their URL mapping pattern defined in web.xml. So the methodology tells us to go through all Servlets, look (at least) at their do* methods and find some vulnerabilities from there. This approach is somehow top-down, from user-controlled input to bad things in the backend.

After digging into some Servlets, I found one called OPMDeviceDetailsServlet. The web.xml file told us that it’s URL maps to /servlet/APMExtAlertsInteg.

Press enter or click to view image in full size

And this is were white-box analysis comes into play. We can follow the control flow step-by-step which easily allows us to submit proper parameters per request, fulfilling several conditional branches observable in the source code. Here, we see the Servlet entry point calling the doPost methods.

Get frycos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Servlet can be called from and unauthenticated and authenticated perspective which makes it more or less critical. For this article we concentrate on the authenticated part.

Press enter or click to view image in full size

We observe that the allow variable has to be true such that with a proper combination of Servlet URL parameters, one could reach the code of the getXMLFileforAllDevices method. Namely, the fetchType parameters has to be set to the value deep, and userName, password and domainName have to be set accordingly.

The timeVal parameters does not have to be set explicitly since if it is null, it is set to All programmatically. In the end, the getAllMOs method will be called.

Press enter or click to view image in full size

Now, the getAllMO method is used to build and execute an SQL query parameterized with category. Since this SQL query is built dynamically via String concatenation, malicious code could be injected easily.

Press enter or click to view image in full size

The exploitation step is as simple as injecting something like …&category=nocategory’); [NEW QUERY — .
The screenshots below show a simple example of a pg_sleep(10) selection. Since the bundled database usually is PostgreSQL, stacked queries make injection easy and with e.g. help of COPY TO commands a web shell could be written. UDF reverse shells would also be possible, i.e. Remote Code Execution is just a matter of small additional effort and left to the interested reader.

Press enter or click to view image in full size
Press enter or click to view image in full size

Additionally, the encryption routine for the username and password had to be re-implemented for a proper decrypt call at the Servlet’s entry point. Since the key is fixed (not good!), the routine was re-implemented quickly.

Overall, this short article should make you being interested in a white-box analysis approach if you get a chance to access code. Instead of fuzzing parameters, sometimes a short code analysis can reveal a straight-forward exploitation. From beginning of code reading to a first successful exploitation, it took me approx. an hour (and I’m far from being an expert!).

I hope you enjoyed this walk-through of this very recent and real-world example how to find a critical bug in well-known product. It’s as easy as that!

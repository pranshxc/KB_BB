---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-18_variant-cloud-analysis.md
original_filename: 2022-05-18_variant-cloud-analysis.md
title: Variant Cloud Analysis
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
- supply-chain
language: en
raw_sha256: 43342d9286d8d4dfd7fe509d97daf9a5ca01153248162bbd1b6c788370a3c054
text_sha256: c074c17a43bcc9a78cf329a1e623624234276e310a0200656887ec7e231435b1
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Variant Cloud Analysis

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-18_variant-cloud-analysis.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `43342d9286d8d4dfd7fe509d97daf9a5ca01153248162bbd1b6c788370a3c054`
- Text SHA256: `c074c17a43bcc9a78cf329a1e623624234276e310a0200656887ec7e231435b1`


## Content

---
title: "Variant Cloud Analysis"
url: "https://jspin.re/variant-cloud-analysis/"
final_url: "https://jspin.re/variant-cloud-analysis/"
authors: ["jspin (@jespinhara)"]
bugs: ["Default credentials"]
publication_date: "2022-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2633
---

# Variant Cloud Analysis

  * [ ![jspin](/content/images/size/w100/2019/06/pipirate-1.png) ](/author/jspin/)

#### [jspin](/author/jspin/)

May 18, 2022 • 3 min read

Another yet quick blog post.

A few years ago, 3 or 4, maybe 5, I was "working" with [@marcioalm](https://twitter.com/marcioalm) in a "Simple Web Vulnerability Scanner" tool intended to be part of an automation vulnerability check for a large and specific environment.

Keep in mind that adventure was before the release of the well-acclaimed [Nuclei](https://github.com/projectdiscovery/nuclei), and Nuclei, since its first releases implemented better features than our tool. By the way, the tool was/is named S**tryker**.

![](https://jspin.re/content/images/2022/05/image.png)Stryker

The idea behind the Stryker was quite simple, read a JSON file, aka "Stryker module", build the request then parse the response.

Stryker modules are simple to write; for example, a simple check for the **CVE-2017-9506.**

![](https://jspin.re/content/images/2022/05/image-1.png)

As I said before, nowadays, Stryke is outdated, and for us, it was well replaced by Nuclei.

So, what is the relation between Stryker and Variant Cloud Analysis? 

Back in those days, Stryker was getting good results against the organization we were testing. Then I had the idea to test against a well tested Bug Bounty program scope. 

The **Variant Cloud Analysis (VCA)** term was coined (?) (probably there is another name for this same thing running for ages in the industry) when we started to observe different results when running Stryker against the same bug bounty program scope many times using different: 

  * Cloud providers
  * Instances types
  * Regions 

For transparency, almost tests were performed using Amazon AWS as the cloud provider.

The most exciting finding was testing for **Apache Tomcat Manager Default Password** on a public and well-tested Bug Bounty Program. We got one hit, which was 100% unexpected since I believe people constantly scan this kind of issue. 

![](https://jspin.re/content/images/2022/05/image-2.png)**Apache Tomcat Manager Default Password Stryker Template (old)**

As expected, I did submit a report using the HackerOne platform.

![](https://jspin.re/content/images/2022/05/image-3.png)Initial Report

Triage returned, saying it was unable to reproduce the report.

![](https://jspin.re/content/images/2022/05/image-4.png)

My fault. I did not provide all the information necessary. To reproduce the report, it was required to use an AWS instance type **t2.xlarge** in the **us-east-1a** region.

![](https://jspin.re/content/images/2022/05/image-5.png)Report Triaged

As a result, the report was closed, and the bounty was only used to pay for the AWS adventure bill. :)

![](https://jspin.re/content/images/2022/05/image-6.png)Report Closed.

The takeaway from this short and hard to read blog post is when running your recon/scanning/automation, try tricks such as:

  * Different Cloud Providers
  * As many regions as possible
  * Different Instance Types
  * Automation is the key

There is no link to Stryker since it is pretty much dead. Use Nuclei instead.

Cya...

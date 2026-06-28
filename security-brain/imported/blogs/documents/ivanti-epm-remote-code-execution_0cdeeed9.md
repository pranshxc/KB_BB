---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-05_ivanti-epm-remote-code-execution.md
original_filename: 2022-06-05_ivanti-epm-remote-code-execution.md
title: Ivanti EPM Remote Code Execution
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 0cdeeed97d1414082805027d62c1a19485e4ca606432b3ab9ad4aff994790c6e
text_sha256: b7e9ed61b892df9ad44b0ba2fa1ba0c6c97820b615df5b29eea1ebbf1930ce4c
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Ivanti EPM Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-05_ivanti-epm-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `0cdeeed97d1414082805027d62c1a19485e4ca606432b3ab9ad4aff994790c6e`
- Text SHA256: `b7e9ed61b892df9ad44b0ba2fa1ba0c6c97820b615df5b29eea1ebbf1930ce4c`


## Content

---
title: "Ivanti EPM Remote Code Execution"
page_title: "Ivanti EPM Remote Code Execution — Machevalia"
url: "https://machevalia.blog/blog/ivanti-epm-remote-code-execution"
final_url: "https://machevalia.blog/blog/ivanti-epm-remote-code-execution"
authors: ["Nick Berrie (@machevalia)"]
bugs: ["RCE", "Components with known vulnerabilities"]
bounty: "6,500"
publication_date: "2022-06-05"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 2585
---

# Ivanti EPM Remote Code Execution

[Bug Bounty](/blog/category/Bug+Bounty)[Write Ups](/blog/category/Write+Ups)

Jun 5

Written By [](/blog?author=63a1076f081fe62c6e3ae37b)

## Overview

In December of 2021, Ivanti announced a remote code execution vulnerability in their Endpoint Manager (EPM) Cloud Appliance in the security advisory https://forums.ivanti.com/s/article/SA-2021-12-02. Later, in March of 2022, Synack Red Team Members collaborated on a working exploit for the vulnerability later released by[ @dinosyn](https://twitter.com/Dinosn/status/1505273954478530569) on Twitter. 

The vulnerability itself is very straightforward. The underlying application logic of the EPM tool appears to have been doing an unsafe evaluation of the 'c' cookie value provided which resulted in remote code execution as the user "nobody", a low-privileged user, on the _/index/client.php_ page. I am guessing the code contained an unsafe-eval function on the cookie's value to validate authentication which probably looked something along the lines of the following snippet although I would expect some sort of validation logic to be included: 
  
  
  {$_COOKIE['c'] .= ';';eval($_COOKIE['c']);exit;}

The PHP eval function does as the name implies: evaluates the string value as PHP code. Therefore, if an application uses the eval function without additional validation or sanitization of user input which is passed to the eval string then remote code execution is possible.

## Bounties

Because of how simple this vulnerability was to exploit, I knew I would have an extremely small window of opportunity to find some bounties without getting duplicates. I keep all of my recon data on targets for just such occasions. If you aren't holding onto historical data from your bounties, I highly recommend that you do. 

I did a little reconnaissance on some EPM instances that were easy to find on the internet via Google and found that the majority of the pages were titled "LANDesk(R) Cloud Services Appliance". I ran through all of the existing data I had on bounty programs for page titles that contained "LAN". I ended up finding 12 targets without any additional recon needed. Turned out that they were all still alive and that they were all vulnerable. 

To conduct a proof-of-exploit for these vulnerable targets, I spun up BurpSuite and navigated to the vulnerable target's _/index/client.php_ page. I captured the page in its natural state and then sent the request to the Repeater tab. 

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae420/1671497590452/image-1024x461.png?format=original)

In Repeater, I added the following cookie values to demonstrate the RCE: _Cookie: ab=ab; c=cGhwaW5mbygpOw==; d=; e=;_ The 'c' cookie parameter's value is the string _phpinfo()_ base64 encoded. Sending this request through would demonstrate the RCE due to the phpinfo page would be displayed in the background of the _/index/client.php_ page. 

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae423/1671497590467/image-1-1024x453.png?format=original)

That's it, about as simple as an RCE can get. 

## Vulnerability Remediation and Payouts

Because this vulnerability is a commercial product, I simply recommended that the vulnerable organizations applied the patch provided by Ivanti. Many of the organization's that I submitted the vulnerability to realized that they no longer needed the EPM Cloud Appliance online so they shut it down.

All in all, I submitted 12 vulnerabilities over about 48 hours and netted a total of $6,500 with 3 payouts still pending all these months later (gotta love some program's attentiveness). 

[Bug Bounty](/blog/tag/Bug+Bounty)[Hacking](/blog/tag/Hacking)[Write-up](/blog/tag/Write-up)[Year-in-Review](/blog/tag/Year-in-Review)

[ ](/blog?author=63a1076f081fe62c6e3ae37b)

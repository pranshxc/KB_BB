---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-08_subdomain-takeover-how-a-misconfigured-dns-record-could-lead-to-a-huge-supply-ch.md
original_filename: 2023-03-08_subdomain-takeover-how-a-misconfigured-dns-record-could-lead-to-a-huge-supply-ch.md
title: 'Subdomain Takeover: How a Misconfigured DNS Record Could Lead to a Huge Supply
  Chain Attack'
category: documents
detected_topics:
- supply-chain
- access-control
- xss
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- access-control
- xss
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 3153a07703a18331c9acf32d3df420002637ee943d475551d2f22155d4eed3f7
text_sha256: 01202f87d5b141ddb20d591075893d9b4844cf6fa8f7c2d427b86aece718657a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Takeover: How a Misconfigured DNS Record Could Lead to a Huge Supply Chain Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-08_subdomain-takeover-how-a-misconfigured-dns-record-could-lead-to-a-huge-supply-ch.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, xss, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `3153a07703a18331c9acf32d3df420002637ee943d475551d2f22155d4eed3f7`
- Text SHA256: `01202f87d5b141ddb20d591075893d9b4844cf6fa8f7c2d427b86aece718657a`


## Content

---
title: "Subdomain Takeover: How a Misconfigured DNS Record Could Lead to a Huge Supply Chain Attack"
page_title: "Shockwave | Attack Surface & Continuous Threat Exposure Management, Simplified - Subdomain Takeover: How a Misconfigured DNS Record Could Lead to a Huge Supply Chain Attack"
url: "https://www.shockwave.cloud/blog/subdomain-takeover-how-a-misconfigured-dns-record-could-lead-to-a-huge-supply-chain-attack"
final_url: "https://www.shockwave.cloud/blog/subdomain-takeover-how-a-misconfigured-dns-record-could-lead-to-a-huge-supply-chain-attack"
authors: ["Gal Nagli (@naglinagli)"]
programs: ["GitHub"]
bugs: ["Subdomain takeover", "Supply chain attack"]
publication_date: "2023-03-08"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1410
---

[![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65f6d171f859eed35348fc83_download.svg)](/)[About](/about-us)[Use Cases](/use-cases)[Integrations](/integrations)[Customers](/customers)[Blog](/blog)[Pricing](/pricing)

[Contact sales![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65f8a2b064b27219926fe1fd_thin-arrow-right-icon%201.svg)](/contact)![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65f02093f3a2a79341585fca_hamburger-menu.svg)

[About](/about-us)[Use Cases ](/use-cases)[Integrations](/integrations)[Customers](/customers)[Blog](/blog)[Pricing](/pricing)

![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65f8089800f9327154b9e694_Mask%20\(10\).svg)

[![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65ef849843a3eb11edaa8992_Path%20\(2\).svg)](/blog)

EASM

Research

●

June 5, 2023

## 

![](https://cdn.prod.website-files.com/65edf4eaa756275eb60c0889/65fb19faf7002586b938f854_1710287493775%20\(1\).jpeg)

Gal Nagli

CEO

## Subdomain Takeover: How a Misconfigured DNS Record Could Lead to a Huge Supply Chain Attack

### S3 Bucket Takeover on [assets.npmjs.com](http://assets.npmjs.com/): A Potential Supply Chain Attack

##### Not long ago, we discovered a vulnerability in the subdomain [assets.npmjs.com](http://assets.npmjs.com/), which if left unaddressed, could lead to a huge supply chain attack. As software engineers and DevOps professionals, it is essential to understand the impact of such vulnerabilities and ways to mitigate them.

In this blog post, we will discuss how the S3 Bucket takeover on [assets.npmjs.com](http://assets.npmjs.com/) could lead to a supply chain attack and how to prevent it.  
  
‍

## What is S3 Bucket takeover?

Subdomain takeover occurs when an attacker exploits a misconfigured DNS record and takes control of a subdomain.  
In this case, [assets.npmjs.com](http://assets.npmjs.com/) was pointing to an unclaimed S3 Bucket, which made it vulnerable to subdomain takeover.  
The attacker can then upload any malicious content on this domain, leading to a supply chain attack.  
  
‍

## How it could lead to a supply chain attack?

[**assets.npmjs.com**](http://assets.npmjs.com/) naming convention could make it very easy for malicious actors to host their own “fork” of npm - supported by thousands of malicious packages, because of the fact that the subdomain takeover was on an asset with naming that makes it more realistic to host legitimate packages (unlike having Subdomain Takeover on [internal.dev.something.npmjs.com](http://internal.dev.something.npmjs.com/)) made this one more severe than others.

Attackers could obfuscate the website as one which is used by npm to host JavaScript packages, and any malicious code uploaded on this domain can affect millions of users who rely on these packages.

The attacker can upload a malicious package or modify an existing package to include their malicious code, leading to a supply chain attack.  
  
‍

## What happened in this case?

The domain [**assets.npmjs.com**](http://assets.npmjs.com/) was discovered to be pointing to an unclaimed S3 Bucket, making it vulnerable to subdomain takeover.

We at shockwave have dedicated thousands of hours through trial and error to make our scanning engines as fast as you can possibly get, up to a point where we scan and automatically claim S3 buckets every **60 seconds** , this is why we managed to claim it before malicious actors did, and save the interest of Github’s npmjs and the software development lifecycle.

**‍**

![shockwave-panel](https://cdn.prod.website-files.com/65edf4eaa756275eb60c0889/65fdcc6bfd010330f1440742_650ed86a94ef9ab77555ce00_64084264334037679f4b99f3_6408410f1004c5becf2d5951_Screenshot%252525202023-03-08%25252520at%2525252010.02.12.png)

![slack-Alert](https://cdn.prod.website-files.com/65edf4eaa756275eb60c0889/65fdcc6bc7618549d2546c01_650ed86a5314ef3af2804f92_64084264259d86ff76d463c6_640840975329831e88617ff1_Screenshot%252525202023-03-08%25252520at%252525209.48.40.png)

‍

The issue was reported in a couple of minutes to Github’s Bug Bounty Program on HackerOne, who resolved the matter in couple of hours, treating the bug as “High Severity” through their CVSS evaluation.

![h1-bug](https://cdn.prod.website-files.com/65edf4eaa756275eb60c0889/65fdcc6bc7618549d2546c44_650ed86b457809d7ea43dc16_64084264e22e743401e525d3_640840973d9e52366200cdf8_Screenshot%252525202023-03-08%25252520at%252525209.50.31.png)

##  
  
Mitigation

To mitigate this vulnerability, it is essential to remove the DNS record from the subdomain that is pointing to the unclaimed S3 Bucket.

This will prevent an attacker from taking over the subdomain and uploading any malicious content.  
When dealing with DNS removal and allocation in daily basis, always aim to remove the DNS entry from the registrar before removing the actual asset it points to.

##  
Impact

A subdomain takeover can have severe consequences, and if left unaddressed, it could lead to a supply chain attack in this particular case.

An attacker can upload a malicious packages by hosting malicious content on the domain, leading to a range of attacks, including XSS, phishing, etc.

##  
  
Conclusion

In conclusion, the S3 Bucket takeover on [**assets.npmjs.com**](http://assets.npmjs.com/) highlights the importance of securing DNS records and subdomains.

We weren’t be able to detect and claim the domain if it wasn’t for our contextual scanning engines, this is exactly why continuous monitoring actually matters if done right.

‍

## About Us

Using a platform like Shockwave for continuous monitoring can help catch vulnerabilities before they can be exploited, we are dedicated on bringing real security value to our customers, and care deeply about the data we product - 0 false positives, no alert fatigue, real and valuable continuous monitoring, that’s why our customers love to bolster their Attack Surface Resistance with our product offering.

![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65ed9f84f518f11425ec03de_Path%202%20\(1\).svg)

![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65ede8c4893156bcc63603f6_Rectangle%20\(1\).svg)![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65ede8c4893156bcc63603f6_Rectangle%20\(1\).svg)

The security first platform

## **Supercharge your security**  

Identify, Secure and Continuously Monitor your Externally Facing Attack Surface.  
Significantly Improve your security posture within minutes with an easy, smooth onboarding process.  

[Get Started![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65fb5d18b570bf80bb743638_65f8a2b064b27219926fe1fd_thin-arrow-right-icon%201%201.svg)](/pricing)

![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65ede8c4893156bcc63603f6_Rectangle%20\(1\).svg)

© 2024 Shockwave. All rights reserved.

Privacy Policy

Terms & Conditions

[Cookies](/cookies)

[![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65eecd9b6d1cabac276ceeed_Combined%20Shape%20\(2\).svg)](https://twitter.com/shockwave_sec)[![](https://cdn.prod.website-files.com/65ec53c6b381bd5728fedb19/65f824595d85ee094fd30a4d_XMLID_801_.svg)](https://www.linkedin.com/company/shockwave-cloud/?viewAsMember=true)

© 2024 Shockwave. All rights reserved.

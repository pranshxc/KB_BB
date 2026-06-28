---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-01-24_0day-writeup-xxe-in-ubercom.md
original_filename: 2017-01-24_0day-writeup-xxe-in-ubercom.md
title: '0day writeup: XXE in uber.com'
category: blogs
detected_topics:
- oauth
- sso
- saml
- command-injection
- otp
- api-security
tags:
- imported
- blogs
- oauth
- sso
- saml
- command-injection
- otp
- api-security
language: en
raw_sha256: 8effcf6d5615d49d133650ff1ef75eeecd79c4f1e4d7b4c9aa933e6cb031d252
text_sha256: ac1f5b31f9c2ba489edc315b2db338a6a74e3624bed01c17ebafa2e40113afc3
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# 0day writeup: XXE in uber.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-01-24_0day-writeup-xxe-in-ubercom.md
- Source Type: markdown
- Detected Topics: oauth, sso, saml, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8effcf6d5615d49d133650ff1ef75eeecd79c4f1e4d7b4c9aa933e6cb031d252`
- Text SHA256: `ac1f5b31f9c2ba489edc315b2db338a6a74e3624bed01c17ebafa2e40113afc3`


## Content

---
title: "0day writeup: XXE in uber.com"
page_title: "My 'Public Evernote': 0day writeup: XXE in uber.com"
url: "https://httpsonly.blogspot.com/2017/01/0day-writeup-xxe-in-ubercom.html"
final_url: "https://httpsonly.blogspot.com/2017/01/0day-writeup-xxe-in-ubercom.html"
authors: ["-"]
programs: ["Uber"]
bugs: ["XXE"]
bounty: "9,000"
publication_date: "2017-01-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6234
---

Hello everyone,

Today I’d love to share an interesting XXE in a popular product of [Code42.com](http://code42.com/) company, which could give access to backups of all users in a given company.

Back in May 2016, I was looking through Uber’s bugbounty, and faced following HTTP application:

  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7_SrepNdelxgehdD07UAQwHTvAlwvNf9dalsuDLKI48Mz3_m9mZEyhyphenhyphencp47zdiYDrEZBjdrjm0p9IZZY3jg8NjhypxO3l6jsQugzP-QRu40QfpKo_KVCrf5ow5qjWOjo_rpZeIxO2DKEA/s320/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7_SrepNdelxgehdD07UAQwHTvAlwvNf9dalsuDLKI48Mz3_m9mZEyhyphenhyphencp47zdiYDrEZBjdrjm0p9IZZY3jg8NjhypxO3l6jsQugzP-QRu40QfpKo_KVCrf5ow5qjWOjo_rpZeIxO2DKEA/s1600/1.png)

  
  

  

Bruteforcing was surely not an option; there were no CVEs published of this vendor (you’ll discover later, why). After accessing [https://backup.uberinternal.com:4285/**api/serverEnv**](https://backup.uberinternal.com:4285/api/serverEnv) API it became clear that Uber was using last version of a product (5.2.0). The only option to break the service and get a bounty for pwning application was to find a 0day.

I quickly accessed Code42’s publicly available documentation, extracted all documented API methods and started bruteforcing them, trying to find which of such methods can be accessed without authentication. Likely, there was one API call, which can be accessed by any external user: [https://www.crashplan.com/apidocviewer/#SsoAuthLoginResponse](https://www.crashplan.com/apidocviewer/#SsoAuthLoginResponse)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeM83tYa9t-rI0GkTo1zCoWtFqUMVmvFMTYbSQCzTRlFTOLPPRTGAsT8IOJOTPPiEyRlAwIzrB2obsfJZVoDMWGTSRoU-_6aXDAJHmrJy4uYvtDN-NjVv2cq1gtX1rqr3wRvOnjg0xoeZL/s320/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeM83tYa9t-rI0GkTo1zCoWtFqUMVmvFMTYbSQCzTRlFTOLPPRTGAsT8IOJOTPPiEyRlAwIzrB2obsfJZVoDMWGTSRoU-_6aXDAJHmrJy4uYvtDN-NjVv2cq1gtX1rqr3wRvOnjg0xoeZL/s1600/2.png)

  

Documentation clearly stated, that `/api/SsoAuthLoginResponse `accepts GET parameter `SAMLResponse`, which value is a base64-encoded string, and is meant to contain XML authentication data. I quickly constructed a trivial xml with external entities pointed to my VPS using non-standard port (since ports 80 and 443 were filtered by firewall), and got a response:

  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioy_h6vFdwbmEnyFw2VPyRvqSL70m8DrcakFFHg03MzS1wqI5ijsZViG-uDPYoGuNpm_c5ObwSdK8EDQ4z9GhzHyXrmr28dMxm0B7kTBAw_cpiAcv5dFheabPtNMRp2sDyu6bCZEWNZJlF/s320/3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioy_h6vFdwbmEnyFw2VPyRvqSL70m8DrcakFFHg03MzS1wqI5ijsZViG-uDPYoGuNpm_c5ObwSdK8EDQ4z9GhzHyXrmr28dMxm0B7kTBAw_cpiAcv5dFheabPtNMRp2sDyu6bCZEWNZJlF/s1600/3.jpg)

  

_Despite exploitation string is pretty straightforward, I will not publish final HTTP request here._

It became clear, that server is vulnerable to XXE Out-of-Band (OOB) attack. Since application was using Java, I knew I could read directories, and hence I immediately launched `xxe-ftp server` to extract data. Greetz to guys at OnSec for coding `xxe-ftp server`! If you don’t know about XXE OOB exploitation, please read their research at [http://lab.onsec.ru/2014/06/xxe-oob-exploitation-at-java-17.html](http://lab.onsec.ru/2014/06/xxe-oob-exploitation-at-java-17.html)

For those who don’t like clicking on external links, I am providing a quick description. This is how `xxe-ftp server` works: attacker's host has launched script, which works as HTTP server to retrieve OOB payload on port 8088, and a FTP server which accepts connections on port 8077:

  

  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4TNDo7X1R6LyMJBAKxLNfN81cZxX2reVEedM1QCusynO1a14wUB_2WfDjAbK1vnoLxDc_MhgoRm7z9DHnDIG30pGLDcfi2pDBfQZKeAIgKT0-MQZL1KydqgUhCXVJWHo_KKxbE7c9gvrf/s320/4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4TNDo7X1R6LyMJBAKxLNfN81cZxX2reVEedM1QCusynO1a14wUB_2WfDjAbK1vnoLxDc_MhgoRm7z9DHnDIG30pGLDcfi2pDBfQZKeAIgKT0-MQZL1KydqgUhCXVJWHo_KKxbE7c9gvrf/s1600/4.jpg)  
  

As a proof-of-concept for Uber, I retrieved the contents of /home/ directory of the server, which was a nice impact illustration to my report at Hackerone:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ811cyXo_xUdS1AVaTyt4tq-ICWYNj0nyjYAZihju1eS8UA7vmT0qasbNOHp-itZ3dUc-6OYILQ4U9A7upT7PxmISUUK3SLA0oVE0e8sPeBqo1FCHJUuEpx3N1jDJdm91taSnkcT78ztu/s320/5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ811cyXo_xUdS1AVaTyt4tq-ICWYNj0nyjYAZihju1eS8UA7vmT0qasbNOHp-itZ3dUc-6OYILQ4U9A7upT7PxmISUUK3SLA0oVE0e8sPeBqo1FCHJUuEpx3N1jDJdm91taSnkcT78ztu/s1600/5.jpg)

  

  

Uber security guys were excited with this vulnerability: they contacted vendor and confirmed that this vulnerability was a 0day. What’s more, Uber team was engaged enough to ask me to elaborate the vulnerability.

I like to show impact of a given vulnerability, so you don’t have to ask me twice. Given permission to show further exploitation, I quickly found the folder, where backup logs were stored. Here is a screenshot of one of local files on the server, containing information about recently backup’ed user:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpZ-2QObBgI318VQ-tja7MpL79ky9iSTmJv3hpyFD4pi5WBrHxhuO2Kq6VPrxFDmvqQQRzVOMqPLfOTub_tefNeeWrJvwudNgv-JWrGuTYc-6Ewv_sBCxmwaYs1hQk2PfDIwLymadwmUR8/s320/6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpZ-2QObBgI318VQ-tja7MpL79ky9iSTmJv3hpyFD4pi5WBrHxhuO2Kq6VPrxFDmvqQQRzVOMqPLfOTub_tefNeeWrJvwudNgv-JWrGuTYc-6Ewv_sBCxmwaYs1hQk2PfDIwLymadwmUR8/s1600/6.png)

  

It was clear that I can read backup files of a little more than all domain accounts of a company, who has Code42 service at their perimeter.

In order to understand the impact of this 0day in the World, I searched for port 4285 in Shodan, and found that one of globally known security firms have this application installed on their perimeter:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGcRCu87tJ2JyiXmH4QZDaWAm9bXJT5A6hkErI1SeVNx8OQR6ihv-HzdlyBQSfp9hUlyF67cON_Fd-1OaMssINherP0GOL9B8Dry1kg6wk6YIHUneBUMZLK1TQUXtrYoOqQIAyBN2hcFy4/s320/7-1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGcRCu87tJ2JyiXmH4QZDaWAm9bXJT5A6hkErI1SeVNx8OQR6ihv-HzdlyBQSfp9hUlyF67cON_Fd-1OaMssINherP0GOL9B8Dry1kg6wk6YIHUneBUMZLK1TQUXtrYoOqQIAyBN2hcFy4/s1600/7-1.jpg)

  

May 6th, 2016 – Report sent to Uber through Hackerone

May 23rd, 2016 – Code42 company have updated their software, and vulnerability was patched in latest version (5.2.0.1)

Jun 28th, 2016 – Got $9000 bounty from Uber

Aug 24th, 2016 – Code42 asked to wait until update is installed on all their clients

Jan 24th, 2017 – Code42 notified that writeup will be published, no reaction.

  

This is a shortcut of our conversation in August 2016 (denial of responsibility): 

“ _With regards to the blog post, we would prefer this is not written until our latest version of the product has been installed by all of our customers. This has been fixed in the latest release of the product, however, not all customers have it installed. We would prefer that you wait until that time to write about what you have found._ ”

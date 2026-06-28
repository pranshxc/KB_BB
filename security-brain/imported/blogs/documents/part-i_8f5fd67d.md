---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-19_part-i.md
original_filename: 2022-02-19_part-i.md
title: Part-I
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- cloud-security
language: en
raw_sha256: 8f5fd67d98b48c84e6841bdf845c0cdeaa9346c366d0059db67dd2a851f34d37
text_sha256: 4926fc3ab22a436e6a0d1d0e611e3aaa58423e08d04dde945a90fc3e710ac2c7
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Part-I

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-19_part-i.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `8f5fd67d98b48c84e6841bdf845c0cdeaa9346c366d0059db67dd2a851f34d37`
- Text SHA256: `4926fc3ab22a436e6a0d1d0e611e3aaa58423e08d04dde945a90fc3e710ac2c7`


## Content

---
title: "Part-I"
page_title: "Passive Recon with Spyse (Part-I) | remonsec"
url: "https://remonsec.com/posts/passive-recon-with-spyse-part-I/"
final_url: "https://remonsec.com/posts/passive-recon-with-spyse-part-I/"
authors: ["remonsec (@remonsec)"]
bugs: ["Subdomain takeover", "AWS misconfiguration"]
bounty: "2,100"
publication_date: "2022-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2889
---

## Passive Recon with Spyse (Part-I)__

**بسم الله الرحمن الرحيم**

Assalamu Alaikum peace be upon you

## Introduction __

Welcome guys, today I will be talking about recon & spyse. How can you do your recon with spyse & why ! will it help or what ?

## Recon __

Recon is nothing just a process to gather information about your target. While doing bugbounty, performing recon over your target will be beneficial.

##  Spyse __

Spyse is an internet assets search engine. while doing bugbounty spyse can be your passive recon tool. How to use spyse for your passive recon ! let me show you

##  Spyse Tools __

If you visit<https://spyse.com/tools> you will see the tooling section for spyse. From there you can get a idea what type of enumeration it perform and how can you collect your searched data

**FEATURED TOOLS**

  * [**Advance Search**](https://spyse.com/advanced-search/domain) _Customize your search to find any target._

  * [**API**](https://spyse.com/api) _Get the data via Spyse API._

  * [**Bulk Search**](https://spyse.com/bulk-search) _Make multiple searching for a list of targeted domains and IPs simultaneously._

**DATA GATHERING**

  * [**Domain Lookup**](https://spyse.com/tools/domain-lookup) _Explore detailed information about a domain_

  * [**DNS Lookup**](https://spyse.com/tools/dns-lookup) _Find all DNS records for any domain_

  * [**ASN Lookup**](https://spyse.com/tools/asn-lookup) _Find Autonomous System Numbers with connected data_

  * [**Subdomain Finder**](https://spyse.com/tools/subdomain-finder) _Find subdomains of any domain_

  * [**Reverse DNS Lookup**](https://spyse.com/tools/reverse-dns-lookup) _Find a DNS PTR record of any IPv4 address_

  * [**SSL Certificate Lookup**](https://spyse.com/tools/ssl-lookup) _Find certificates by a domain name or fingerprint_

  * [**IP Lookup**](https://spyse.com/tools/ip-lookup) _Find geolocation, open ports and hosted domains on the IP_

  * [**MX Lookup**](https://spyse.com/tools/mx-lookup) _Find MX records by the domain name_

  * [**Reverse AdSense Lookup**](https://spyse.com/tools/reverse-adsense-lookup) _Find all domains with the same AdSense ID_

  * [**Reverse IP Lookup**](https://spyse.com/tools/reverse-ip-lookup) _Find all hosted domains on a specific IP address_

  * [**NS Lookup**](https://spyse.com/tools/ns-lookup) _Get a full DNS records list of a domain_

  * [**Company Lookup**](https://spyse.com/tools/company-lookup) _Find related company assets by its name_

  * [**Port Scanner**](https://spyse.com/tools/port-scanner) _Find open ports and vulnerabilities_

  * [**WHOIS Lookup**](https://spyse.com/tools/whois-lookup) _Find WHOIS record for any domain_

  * [**CVE Search**](https://spyse.com/tools/cve-search) _Find vulnerable domains and IP addresses by CVE ID_

  * [**Technology Checker**](https://spyse.com/tools/technology-checker) _Search for technologies on the websites._

So as you can see here a lot to do with spyse.

## Advance Search __

[](https://postimg.cc/2bpJwgW0)

Here you can see spyse have around 4.8B data collection. So with advance search you can filter the data from their collection and can collect specific data you need.

Let me give you a practical example by searching for all possible subdomain takeover on GitHub service

[](https://postimg.cc/svDV7Zsv)

[](https://postimg.cc/mhTRWFc8)

[](https://postimg.cc/Hc2qkBJ3)

[](https://postimg.cc/cKWktfGz)

[](https://postimg.cc/N2XRxP1k)

[](https://postimg.cc/9wHDcX7y)

Hope this example is clear that how you can use spyse advance search feature to request specific data and use it for your own benefit. **NOTE** : hacking randomly like this can be dangerous

## EndNote __

I am little bit sick & can’t write more. I am closing this write up here, whatever there a lot more to cover about spyse & recon. I will be publishing 2nd part of this write up as soon as I can.

Allah Hafiz

* * *

wanna support my work! well just buy me a coffee

[](https://www.buymeacoffee.com/remonsec)

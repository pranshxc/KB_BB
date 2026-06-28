---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-17_opensips-security-audit-report-is-fully-disclosed-and-out-there.md
original_filename: 2023-03-17_opensips-security-audit-report-is-fully-disclosed-and-out-there.md
title: OpenSIPS Security Audit Report is fully disclosed and out there
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 793d4372ac28e037fab54de82d3f678941297aa47bc1bbd2377dc91b203d340b
text_sha256: a0da9454f763835a4c5ee50fbb3880a48fb5c9ef916e193c6e8572f5bd406f0f
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# OpenSIPS Security Audit Report is fully disclosed and out there

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-17_opensips-security-audit-report-is-fully-disclosed-and-out-there.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `793d4372ac28e037fab54de82d3f678941297aa47bc1bbd2377dc91b203d340b`
- Text SHA256: `a0da9454f763835a4c5ee50fbb3880a48fb5c9ef916e193c6e8572f5bd406f0f`


## Content

---
title: "OpenSIPS Security Audit Report is fully disclosed and out there"
page_title: "OpenSIPS Security Audit Report is fully disclosed and out there – Enable Security"
url: "https://www.rtcsec.com/post/2023/03/opensips-security-audit-report/"
final_url: "https://www.enablesecurity.com/blog/opensips-security-audit-report/"
authors: ["Sandro Gauci (@sandrogauci)"]
programs: ["OpenSIPS", "Kamailio"]
bugs: ["SIP", "Memory corruption", "Memory leak", "Buffer Overflow", "Buffer over-read"]
publication_date: "2023-03-17"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 1360
---

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_f1b0822e4d5c5b22.jpg)

**Sandro Gauci**, Enable Security

# OpenSIPS Security Audit Report is fully disclosed and out there

Published on Mar 17, 2023 in _[sip security](/tags/sip-security/)_ , _[sip security testing](/tags/sip-security-testing/)_ , _[security tools](/tags/security-tools/)_ , _[opensips](/tags/opensips/)_ , _[kamailio](/tags/kamailio/)_ , _[fuzzing](/tags/fuzzing/)_ , _[denial of service](/tags/denial-of-service/)_ , _[research](/tags/research/)_

It’s almost a year since the OpenSIPS project published a minimized version of our security audit report from 2022. Now, the full version has been published, with all the information intact on how to reproduce the vulnerabilities and extra details in an 80+ page report.

The OpenSIPS security audit report can be found [here](https://github.com/EnableSecurity/reports/raw/master/opensips-security-audit/opensips-audit-technical-report-full.pdf).

[![OpenSIPS security audit report front page](opensips-security-audit-report.png)](https://github.com/EnableSecurity/reports/raw/master/opensips-security-audit/opensips-audit-technical-report-full.pdf)

## What is the OpenSIPS security audit?

OpenSIPS is a SIP server that often has a critical security function within an IP communications system. Thus, it makes absolute sense to perform a thorough security audit for such software. We had been dealing with OpenSIPS servers from time to time in our work so we were rather familiar with the software and the project itself. Then back in January 2021, the lead developer for OpenSIPS, Bogdan-Andrei Iancu, asked us if we would be interested in doing some proper security work. Naturally, our answer was _yes please_!

We planned to do the following for OpenSIPS 3.2.2:

  * whitebox fuzz testing, or coverage-guided fuzzing based on libfuzzer and AFL
  * blackbox fuzz testing using the [SIPVicious PRO fuzzing tool](https://docs.sipvicious.pro/stable/cui-reference/sip/fuzz/request/)
  * manual code review of various security-critical functions
  * basic DDoS security tests

For further background of how this happened, do watch [the presentation](https://youtu.be/JZ1hFDWlcFs?t=9530) or [slides](https://www.slideshare.net/sandrogauci/the-opensips-security-audit-opensips-summit-sandro-gauci) that we presented at the OpenSIPS Distributed Summit 2021, before starting the actual security audit.

Here’s a bit of a timeline of how things went:

  * Early discussions: January 2021
  * Fund raising started: June 2021
  * Fund raising finished: September 2021
  * Started work: September 2021
  * First status report: November 2021
  * Second status report: February 2022
  * Minimized report delivered: March 2022
  * Minimized report published: April 2022
  * Full report published: March 2023

## Vulnerability findings and security fixes

As a result of this security audit, we reported the following security findings:

  * Segmentation fault due to invalid `Content-Length` header (CVSS: 8.6)
  * Crash when specially crafted REGISTER message is challenged for authentication (CVSS: 8.6)
  * Buffer over-read in function `delete_sdp_line` leads to DoS or undefined behaviour (CVSS: 8.6)
  * Buffer over-read in the function `parse_param_name` leads to DoS or undefined behaviour (CVSS: 8.6)
  * Buffer over-read in the function `extract_field` leads to DoS or undefined behaviour (CVSS: 8.6)
  * Buffer over-read in function `extract_rtpmap` leads to DoS or undefined behaviour (CVSS: 8.6)
  * Buffer over-read in the function `extract_fmtp` leads to DoS or undefined behaviour (CVSS: 8.6)
  * Off-by-one error in the function `append_hf` leads to a crash (CVSS: 8.6)
  * Segmentation fault in the function `build_res_buf_from_sip_req` might lead to DoS (CVSS: 6.2)
  * Segmentation fault when calling the function `calc_tag_suffix` leads to DoS (CVSS: 8.6)
  * Crash in the function `t_reply_matching` may lead to DoS (Info)
  * Heap-buffer-overflow in function `parse_hname2` leads to AddressSanitizer false positives (Info)
  * Segmentation fault in the function `rewrite_ruri` leads to DoS (CVSS: 8.6)
  * Memory leak in `parse_mi_request` might lead to Denial of Service (CVSS: 7.1)
  * Buffer over-read in function `stream_process` leads to DoS (CVSS: 8.6)

This led to the following advisories from OpenSIPS’s end:

  * [Memory leak in cJSON lib (CVE-2023-28096)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-2mg2-g46r-j4qr) CVSS: 4.5
  * [Vulnerability 3 in the codec_delete_XX() functions (CVE-223-27596)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-3ghx-j39m-cw4f) CVSS: 7.5
  * [Vulnerability in the Content-Length Parser (CVE-2023-28097)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-c6j5-f4h4-2xrq) CVSS: 7.5
  * [Vulnerability in the ds_is_in_list() function (CVE-2023-28099)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-pfm5-6vhv-3ff3) CVSS: 5.9
  * [Vulnerability in the parse_uri() function (CVE-2023-27597)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-358f-935m-7p9c) CVSS: 7.5
  * [Vulnerability in the parse_via() function (CVE-2023-27598)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-wxfg-3gwh-rhvx) CVSS: 7.5
  * [Vulnerability in the parse_to_param() function (CVE-2023-27599)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-qvj2-vqrg-f5jx) CVSS: 7.5
  * [Vulnerability 2 in the codec_delete_XX() functions (CVE-2023-27600)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-67w7-g4j8-3wcx) CVSS: 7.5
  * [Vulnerability in the codec_delete_XX() functions (CVE-2023-27601)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-xj5x-g52f-548h) CVSS: 7.5
  * [Vulnerability in the building the local negative replies (CVE-2023-28095)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-7pf3-24qg-8v9h) CVSS: 7.5
  * [Vulnerability in the Digest Authentication Parser (CVE-2023-28098)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-jrqg-vppj-hr2h) CVSS: 5.9

One thing to note is that while we’re using the _overall CVSS score_ , the advisories use the _CVSS base score_. Another is that according to our analysis, the vulnerabilities found should only result in Denial of Service rather than arbitrary code execution.

In addition to actual vulnerabilities, we also reported two informational findings. In each case, these were results from our fuzzing exercises where further analysis gave us a strong indication that they were not exploitable. We still report these findings because fixing them allows further fuzzing to be done that might reveal actual real vulnerabilities. With the developers, we also highlighted the value of having code that is easy to fuzz using instrumented code coverage techniques such as those supported by libfuzzer.

## The actual work

Our methodology consisted of iterating between blackbox or network-based fuzzing for SIP with SIPVicious PRO and whitebox or coverage-guided fuzzing with libfuzzer. Both approaches were used to inform each other and increase the amount of attack surface that could be covered. We also made use of our own internal tooling and something called [weggli](https://github.com/weggli-rs/weggli) to identify code that needed more attention.

One important aspect in testing something like OpenSIPS, is that various configuration files were prepared so that specific OpenSIPS functionality could be tested in isolation. This means that the OpenSIPS modules in scope could be targeted in our tests. Another lesson is that fuzzing on its own is not enough. One needs to build the correct corpus and dictionaries, actually fix bugs in the fuzzers and also analyse coverage reports to make sure that the fuzzer is working well i.e. is it actually doing anything significant?

Furthermore, we tried to understand the root cause of each finding. Luckily for us, we had the OpenSIPS developers who were always helpful and ready to lend a hand. We took a collaborative approach where the OpenSIPS developers were reproducing the issues found, helping us debug where necessary, discussing the vulnerability impact at length and so on. This is, in our opinion, one of the best ways to do a security audit.

Finally, the OpenSIPS developers decided to track the security issues using Github’s security advisories feature - which we cannot recommend enough. This helps open-source developers create meaningful advisories with a simple template that indicates important factors like software versions, severity rating using a CVSS calculator, giving credits to the researchers and getting a CVE assigned to the vulnerability. It makes a previously complex task so much easier for everyone.

## Do any of these vulnerabilities affect Kamailio too?

OpenSIPS and Kamailio are both coming from the same original codebase, with OpenSIPS having forked from OpenSER back in 2008. Therefore, it makes a lot of sense to ask if any of the vulnerabilities that were fixed in OpenSIPS also affect Kamailio. In fact, this is what Dovid Bender did on the [Kamailio users mailing list](https://lists.kamailio.org/mailman3/hyperkitty/list/sr-users@lists.kamailio.org/thread/K25PIEL4CK3USWYZQKMYUEE4K67V2SOI/).

As of yet, we do not have a definitive answer. My initial impression, based on a spot check done some time ago, was that the issues did not appear applicable to the newest versions of Kamailio. But we are starting to take a second look and our opinion is actually changing. We plan to delve deeper into this topic, report to the Kamailio developers if anything is found and then publish a future blog post about it.

## The future of security testing, according to us

In the past few years, we did quite a few projects that were similar to the OpenSIPS security audit, and we like to think that we learned a lot through such exercises. One of those lessons - and this may come as no surprise - is that penetration tests and security audits are often just an exercise that is done at one point in time. Software such as OpenSIPS is constantly changing, as is our understanding of cyber-security - thus this approach, although an admirable effort and often a great start, is not enough.

We have been working on fixing this from our end, at least partially. We are building tools and a sort of framework to regularly test specific software, such as OpenSIPS, by performing network-based fuzzing, code-coverage guided fuzzing, DDoS testing, together with static code analysis and other capabilities. What is interesting about this is that all of the different techniques can be semi-automated and streamlined so as input from one method can inform the other. We find that this can greatly expand the security coverage that can be achieved.

On the other hand, this does not replace penetration testing which is a very flexible skill and can cover a lot more than a combination of automated tests. Proper penetration testing, in our opinion, requires creativity and intuition to be applied during the actual tests, adjusting techniques and methodology as needed. But, it does not scale.

Thus, we see a future where more and more testing can be prepared, and done regularly with the occasional penetration test to help adjust those tests as need be.

## Thanks to the OpenSIPS developers and community

Thank you for making so far in this article.

Finally we’d also like to thank [Bogdan-Andrei Iancu](https://www.linkedin.com/in/ACoAAAGO5OUBvuuCTbQpKIt1P7Y9gkfK5kojZLc), [Liviu Chircu](https://www.linkedin.com/in/ACoAAAqwmT8BwgI9ppzBsM-ycgnyQiTLEkbir70), [Răzvan Crainea](https://www.linkedin.com/in/ACoAAAf2P3YBOSTh2AFBnSqfrpG2sxEZiV-PjDA) and the OpenSIPS developers for this opportunity and their feedback. Also the [OpenSIPS Project](https://www.linkedin.com/company/opensips/) community for sponsoring this work!

## Further references

  * [OpenSIPS Security Audit page](https://opensips.org/Community/Security-Audit)
  * [OpenSIPS Security Audit, facts and results](https://blog.opensips.org/2022/04/28/opensips-security-audit-facts-and-results/)
  * [OpenSIPS Security Audit, fully disclosed](https://blog.opensips.org/2023/03/15/opensips-security-audit-fully-disclosed/)

* * *

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_d4528d812320cb98.jpg)

Sandro Gauci

[ __](https://www.linkedin.com/in/sandrogauci)[__](https://twitter.com/sandrogauci)[__](https://savvycal.com/sandrogauci/pub)CEO, Chief Mischief Officer at Enable Security

Sandro Gauci leads the operations and research at [Enable Security](https://www.enablesecurity.com). He is the original developer of [SIPVicious OSS](https://www.enablesecurity.com/sipvicious/), the SIP security testing toolset. His role is to focus on the vision of the company, design offensive security tools and engage in security research and testing. Therefore, he is the proud owner of the title of _Chief Mischief Officer_ at Enable Security.

He offers public office hours and is reachable [here](https://savvycal.com/sandrogauci/pub).

###### Contents

  * What is the OpenSIPS security audit?
  * Vulnerability findings and security fixes
  * The actual work
  * Do any of these vulnerabilities affect Kamailio too?
  * The future of security testing, according to us
  * Thanks to the OpenSIPS developers and community
  * Further references

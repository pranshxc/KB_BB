---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-27_unleashing-the-power-of-recon-how-i-earned-2500-in-5-minutes.md
original_filename: 2023-06-27_unleashing-the-power-of-recon-how-i-earned-2500-in-5-minutes.md
title: 'Unleashing the Power of Recon: How I Earned $2500 in 5 Minutes'
category: documents
detected_topics:
- command-injection
- sso
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- cloud-security
- supply-chain
language: en
raw_sha256: dee1b432e926c1e5a7f7de57230ec8fcc6e133397421589a9c66c583d9c2583b
text_sha256: 48a1489656d9c8401e3c6777bfb187db708e40433c41b16db36f8d04bd12e24f
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Unleashing the Power of Recon: How I Earned $2500 in 5 Minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-27_unleashing-the-power-of-recon-how-i-earned-2500-in-5-minutes.md
- Source Type: markdown
- Detected Topics: command-injection, sso, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `dee1b432e926c1e5a7f7de57230ec8fcc6e133397421589a9c66c583d9c2583b`
- Text SHA256: `48a1489656d9c8401e3c6777bfb187db708e40433c41b16db36f8d04bd12e24f`


## Content

---
title: "Unleashing the Power of Recon: How I Earned $2500 in 5 Minutes"
url: "https://infosecwriteups.com/unleashing-the-power-of-recon-how-i-earned-2500-in-5-minutes-cve-2017-5638-ognl-injection-23ece4811f14"
authors: ["Karthikeyan.V (@karthithehacker)"]
bugs: ["OGNL injection", "RCE", "Components with known vulnerabilities"]
bounty: "2,500"
publication_date: "2023-06-27"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1000
scraped_via: "browseros"
---

# Unleashing the Power of Recon: How I Earned $2500 in 5 Minutes

Unleashing the Power of Recon: How I Earned $2500 in 5 Minutes | CVE-2017–5638 | OGNL injection | RCE
Karthikeyan.V
Follow
3 min read
·
Jun 16, 2023

165

3

Press enter or click to view image in full size

Hello, infosec fam

In this write-up, I’ll share the thrilling tale of how I earned $2500 within a mere 5 minutes of recon in a private bug bounty program. As a dedicated security researcher, my passion lies in breaking security barriers and ethically reporting my findings to organizations. While I typically focus on account takeover-based vulnerabilities, this particular engagement presented a unique challenge — no apparent authentication actions. Undeterred, I decided to shift my focus towards Remote Code Execution (RCE).

During my recon phase, I fired up the Burp Suite tool. While spidering the target application, I stumbled upon files with the extensions “.do, action” and “.jsp.” This discovery immediately caught my attention. To gather further insights into the backend technology, I looked Wappalyzer extension. Its analysis indicated the potential utilization of Apache Struts 2 — an infamous technology associated with backend development.

Encouraged by this revelation, I resolved to search for an OGNL (Object-Graph Navigation Language) injection vulnerability, known as CVE-2017–5638. Exploiting this vulnerability could potentially allow an attacker to seize server-level control through an RCE bug.

To automate the scanning process, I followed these steps:
Set the scope in Burp Suite, clearly defining the boundaries of the target application.
Press enter or click to view image in full size

2. Navigate to the Spider tab and inject OGNL payloads into the specified content types.

Press enter or click to view image in full size

3. Initiate the spidering process to systematically scan the target application.

4. If the application is vulnerable, a distinctive response header will be observed, featuring the value “karthithehacker.”

By automating this scanning procedure, I was able to swiftly identify the critical vulnerability, CVE-2017–5638, with exceptional efficiency, all within a mere 5 minutes of recon.

Poc Image
Press enter or click to view image in full size
Payloads i Used : https://github.com/karthi-the-hacker/PayloadAllTheThings/tree/main
Conclusion:

CVE-2017–5638 exposed the critical nature of remote code execution vulnerabilities and the potential consequences organizations face when security flaws are not promptly addressed. This incident urged organizations to adopt stringent security measures, prioritize patch management, and foster a culture of proactive vulnerability management.

Get Karthikeyan.V’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As security professionals, it is crucial to stay vigilant, keep abreast of emerging vulnerabilities, and collaborate with the community to foster a more secure digital landscape.

Whats next :

Soon, I will be presenting an in-depth exploration of the CVE-2017–5638 vulnerability, where I will demonstrate the process of exploiting it to gain a powerful reverse shell. Stay tuned for an exciting writeup

Keep an eye out for the upcoming writeup and join me in the quest for a more secure digital world.

Previous Write-up about 300$ bounty :

https://medium.com/bugbountywriteup/from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422

Connect with me:

Twitter: https://twitter.com/karthithehacker

Instagram: https://www.instagram.com/karthithehacker/

LinkedIn: https://www.linkedin.com/in/karthikeyan--v/

Website: https://www.karthithehacker.com/

Github : https://github.com/karthi-the-hacker/

npmjs: https://www.npmjs.com/~karthithehacker

Youtube: https://www.youtube.com/karthithehacker

Thank you

Karthikeyan.V

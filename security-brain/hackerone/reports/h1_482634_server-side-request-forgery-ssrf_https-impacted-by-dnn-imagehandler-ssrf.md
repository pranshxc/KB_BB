---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '482634'
original_report_id: '482634'
title: https://████████ Impacted by DNN ImageHandler SSRF
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2019-01-19T18:00:45.913Z'
disclosed_at: '2019-10-08T18:43:17.892Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# https://████████ Impacted by DNN ImageHandler SSRF

## Metadata

- HackerOne Report ID: 482634
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2019-10-08T18:43:17.892Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
https://███████ runs DNN 8.0.0 to 9.1.1 and is impacted by CVE 2017-0929 allowing for a SSRF through the DNN ImageHandler. Origin servers will request any image file supplied by the attacker. This allows for internal NIPR sites to be mapped and accessed through a vulnerable host. The attack is limited by file extension.

Impact
Vulnerable site allows interaction with internal NIPR sites. Pulling default image files from internal NIPR sites verifies the site is online and responsive. Discloses origin IP addresses, and could be manipulated further.  This could also be used as a defacement technique making the sight display images of radical ideologies or pornography.  

Step-by-step Reproduction Instructions
Access the DNN image handler on the vulnerable site.
Supply Burp collaborator payload (working on free burp right now and cannot provide a collab payload) or external attacker controlled image for SSRF trigger.
Payload Example:
https://█████/DnnImageHandler.ashx?mode=file&url=http://1.bp.blogspot.com/-q19YK-T_wAU/UdpDm76jIgI/AAAAAAAAAWo/yjeRx4Vet80/s400/meme11.jpg

https://████████/DnnImageHandler.ashx?mode=file&url=http://www.███/data/uploads/images/DC3_seal.png

Product, Version, and Configuration
DNN 8.0.0 to 9.1.1 with ImageHandler exposed.

Suggested Mitigation/Remediation Actions
Upgrade to DNN 9.2.0 or later. If upgrading isn't possible, consider blocking requests to ImageHandler if it is unused.

## Impact

Recommend High Severity: Vulnerable site allows interaction with internal NIPR-Only sites. Pulling default image files from internal NIPR sites verifies the site is online and responsive. Discloses origin IP addresses, and could be manipulated further to cause harm on internal NIPR sites. This could also be used as a defacement technique making the sight display images of radical ideologies or pornography.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

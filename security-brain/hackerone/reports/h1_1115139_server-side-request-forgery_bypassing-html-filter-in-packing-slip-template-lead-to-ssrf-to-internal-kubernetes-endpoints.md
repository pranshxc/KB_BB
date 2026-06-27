---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1115139'
original_report_id: '1115139'
title: Bypassing HTML filter in "Packing Slip Template" Lead to SSRF to Internal Kubernetes
  Endpoints
weakness: Server Side Request Forgery
team_handle: shopify
created_at: '2021-03-02T22:30:04.491Z'
disclosed_at: '2021-12-02T20:38:55.344Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- server-side-request-forgery
---

# Bypassing HTML filter in "Packing Slip Template" Lead to SSRF to Internal Kubernetes Endpoints

## Metadata

- HackerOne Report ID: 1115139
- Weakness: Server Side Request Forgery
- Program: shopify
- Disclosed At: 2021-12-02T20:38:55.344Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**

Shopify has a feature called `Print Packing Slip`, with this tool, users can easily print a packing slip after customers make an order. The generated packing slip can be downloaded as a PDF file.

Users can edit an `Edit packing slip template` to adjust with a shop design. 

However, there's have a filter in the PDF Generator like `<iframe>` tag is filtered or sanitize, but we can bypassing HTML filter inject malicious HTML code, and accessing the Internal Kubernetes Endpoints.

The initial test that I do is trying to add an `Iframe` to the `Packing Slip` template and expecting those `Iframe` will generate in the PDF file.

This tag was filtered so the HTML will not added to the PDF:

```
<iframe src="https://evil.com/" width=1001 height=1001>
```

But it can be bypassed by adding `<svg><style><h1/>` in the beginning of tag:

```
<svg><style><h1/><iframe src="https://evil.com/" width=1001 height=1001>
```

The Iframe was successfully loaded:

{F1215141}

Since this only accepting HTTPS protocol, I was unable to extract the Google Cloud Metadata. But I can hit the Kubernetes API which is using HTTPS protocol.

**Step to Reproduce**

1) Log in to the Shopify account
2) Navigate to `https://mystore.myshopify.com/admin/settings/packing_slip_template`
3) Add this HTML tag

```
<svg><style><h1/><iframe src="https://kubernetes.default.svc/info" width=1001 height=1001>
```

4) Preview Template and PDF will generated

{F1215151}

```
<svg><style><h1/><iframe src="https://kubernetes.default.svc/livez?verbose" width=1001 height=1001>
```

{F1215154}

## Impact

The attacker can perform an SSRF attack on the internal network.

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

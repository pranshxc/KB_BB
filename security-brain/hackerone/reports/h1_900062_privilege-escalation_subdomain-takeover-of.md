---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '900062'
original_report_id: '900062'
title: Subdomain takeover of ████
weakness: Privilege Escalation
team_handle: deptofdefense
created_at: '2020-06-16T23:52:34.842Z'
disclosed_at: '2020-07-08T17:39:50.514Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover of ████

## Metadata

- HackerOne Report ID: 900062
- Weakness: Privilege Escalation
- Program: deptofdefense
- Disclosed At: 2020-07-08T17:39:50.514Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I was able to claim the subdomain: ████ using Microsoft Azure ( CDN profiles)

**Description:**

## Impact
Platform(s) Affected:
Subdomain
Azure CDN

## Step-by-step Reproduction Instructions

1. Using dig, I was able to determine that the subdomain '███████' was vulnerable to takeover. The record showed status: NXDOMAIN and was pointing to the CNAME: █████.
2. Using this information, I was able to create a new Azure CDN Profile with the name '██████████'. This would resolve to the CNAME record mentioned above.
3. I then created a Web App domain through Azure  where I uploaded a small proof html file through FTP, I then set the CDN's origin type to WebApp and selected the url that I created earlier, this would serve the proof file (█████/proof.html) , Last and final step I set the custom domain to ███████ and enabled ssl.
4. I was then able to view the uploaded site at https://████████/proof.html

## Suggested Mitigation/Remediation Actions
To mitigate this issue you can:

Remove the DNS record from the DNS zone if it is no longer needed.
Claim the domain name in a permanent DNS record so it cannot be used elsewhere.

## Impact

This is extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the ████ domain. This would allow them to post malicious content which would be mistaken for a valid site. They could steal cookies, bypass domain security, steal sensitive user data, malware distribution, etc.

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

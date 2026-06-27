---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '838817'
original_report_id: '838817'
title: Insecure crossdomain.xml on https://vdc.mtnonline.com/
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2020-04-04T13:04:40.446Z'
disclosed_at: '2022-03-20T05:31:53.400Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Insecure crossdomain.xml on https://vdc.mtnonline.com/

## Metadata

- HackerOne Report ID: 838817
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2022-03-20T05:31:53.400Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:

```

<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*" headers="*"/> 
	</cross-domain-policy>

```

## Impact

This will make any one able to receive content from https://vdc.mtnonline.com/ , attacker can steal CSRF tokens and user PII.

More information about this issue is available here:

https://medium.com/@x41x41x41/exploiting-crossdomain-xml-missconfigurations-3c8d407d05a8

Best regards,
Vishu10x00 ❤️

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

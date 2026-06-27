---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '458696'
original_report_id: '458696'
title: xmlrpc.php is enabled - Nextcloud
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2018-12-07T17:23:40.923Z'
disclosed_at: '2020-03-01T13:20:04.659Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# xmlrpc.php is enabled - Nextcloud

## Metadata

- HackerOne Report ID: 458696
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2020-03-01T13:20:04.659Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Nextcloud Team,

Summary: An attacker can devise a XML request to list all the methods that are enabled on the server. Replace Get with POST request and add method call in the request.

To reproduce the vulnerability you need to use Firefox browser and Burpsuite

    Open: https://nextcloud.com/xmlrpc.php.

This URL is publicly accessible, thus confirming the presence of the vulnerability. Proceed further in order to get request/response for above vulnerability.

    Capture the Get method in burpsuite tool

    Send the Get method in repeater tab.

    As "XML-RPC server accepts POST requests only" write POST instead of GET in Request window.

    Write the method list command below for Post request in Request window like:

<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

    We will get all the available methods for https://nextcloud.com/xmlrpc.php

Regards
jaimaakali

## Impact

Unauthorized Access

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '304708'
original_report_id: '304708'
title: Information exposure via error pages (www.lahitapiola.fi Tomcat)
weakness: Information Exposure Through an Error Message
team_handle: localtapiola
created_at: '2018-01-14T11:59:38.299Z'
disclosed_at: '2018-03-02T04:59:45.904Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Information exposure via error pages (www.lahitapiola.fi Tomcat)

## Metadata

- HackerOne Report ID: 304708
- Weakness: Information Exposure Through an Error Message
- Program: localtapiola
- Disclosed At: 2018-03-02T04:59:45.904Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
Information exposure via error pages

**Description:** 
Hello there!

I take the risk that this report might be closed as a N/A but because you are running outdated tomcat I wanted to take this risk and report this to you.

So here we go..
When you navigate to the page e.g.
https://www.lahitapiola.fi/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=15096s13006012asd&ssbinary=true

You will see the error page which shows the exact version of the tomcat:
{F253872}

Here is some examples about the vulnerabilities of this version tomcat:
https://www.securityfocus.com/bid/100901/info
https://www.securityfocus.com/bid/97530

There is two main reasons why I decided to report this to you:
I am pretty sure that eariler your 404 error pages didn't show tomcat version.
This tomcat is outdated and this information can be used of damage your reputation or in worst case to compromise this host.

If you need any information please let me know.

Cheers!

**Domain:** 
lahitapiola.fi

## Impact

An attacker get information about unpatched tomcat.

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

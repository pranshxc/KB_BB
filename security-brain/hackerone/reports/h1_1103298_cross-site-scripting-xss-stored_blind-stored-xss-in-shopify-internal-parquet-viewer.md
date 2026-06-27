---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1103298'
original_report_id: '1103298'
title: Blind Stored XSS in shopify internal Parquet Viewer
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2021-02-14T18:44:29.558Z'
disclosed_at: '2024-02-08T15:10:03.594Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS in shopify internal Parquet Viewer

## Metadata

- HackerOne Report ID: 1103298
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2024-02-08T15:10:03.594Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
Hey, hope you are doing well, I have found that one of my blind xss payload fired in one of your internal tool `Parquet viewer` on 14th feb 11:23 PM IST

I don’t know the entry point were I put my bXSS payload, But this is fired in one of your employee ( `[██████` ) computer.

##Details:
I am attaching all the details here.

* Vulnerable Page URL
`file://localhost/private/var/folders/4m/pdc_bjcj17dcxbtlllqqq81w0000gp/T/parquet-viewer-6296239398097329598.html`

* User IP Address
`█████████`

* User-Agent
`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36`

You can see the name of Shopify employee `████████` at `gs://starscream-adhoc/user/███/shop_dimension/part-00039-4039dc30-6a7a-4108-838d-fb1daec9a216-c000.snappy.parquet`
* ███████

* Open the dom.html and go o the `Sample Data` ███████
████

## Impact

████

Kind Regards
Aman

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

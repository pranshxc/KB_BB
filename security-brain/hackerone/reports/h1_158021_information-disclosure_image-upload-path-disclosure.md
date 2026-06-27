---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158021'
original_report_id: '158021'
title: Image Upload Path Disclosure
weakness: Information Disclosure
team_handle: instacart
created_at: '2016-08-10T00:46:51.019Z'
disclosed_at: '2016-09-12T19:58:14.180Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Image Upload Path Disclosure

## Metadata

- HackerOne Report ID: 158021
- Weakness: Information Disclosure
- Program: instacart
- Disclosed At: 2016-09-12T19:58:14.180Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Firstly,I couldn't see anything about Path Disclosure in your policy,so I've decided to report it.

Steps to reproduce :

1-Create a list for a store
2-Add background image from link (File has to be .svg) like aaa.com/aaa.svg
3-Then it will give an error

Let's take a look to that error

{"meta":{"code":400,"error_type":"List Error","error_message":"There was an error while updating this list","errors":["Image must be a JPEG or PNG","Image Failed to manipulate with rmagick, maybe it is not an image? Original Error: no decode delegate for this image format `/var/app/20160809T225101Z/tmp/uploads/1470789216-24489-0001-8854/full_redirect_2.svg' @ error/svg.c/ReadSVGImage/2871"]}}


As you can understand from error's Response this is the path disclosure

/var/app/20160809T225101Z/tmp/uploads/1470789216-24489-0001-8854/full_redirect_2.svg

I'm gonna add a screenshot from Request and Response for being more clear about it.

Thanks,Instacart.

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

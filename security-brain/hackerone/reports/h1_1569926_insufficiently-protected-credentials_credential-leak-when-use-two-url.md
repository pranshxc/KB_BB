---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1569926'
original_report_id: '1569926'
title: Credential leak when use two url
weakness: Insufficiently Protected Credentials
team_handle: curl
created_at: '2022-05-13T19:09:38.556Z'
disclosed_at: '2022-06-27T06:55:01.273Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insufficiently-protected-credentials
---

# Credential leak when use two url

## Metadata

- HackerOne Report ID: 1569926
- Weakness: Insufficiently Protected Credentials
- Program: curl
- Disclosed At: 2022-06-27T06:55:01.273Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
Curl can leak user credentials if use two url.

## Steps To Reproduce:


  1. curl -I -v -u aaa:bbb hackerone.com curl.se
  2. the output is:
> Connected to hackerone.com (104.16.100.52) port 80 (#0)                                                
> Server auth using Basic with user 'aaa'                                                                   
> HEAD / HTTP/1.1                                                                                           
> Host: hackerone.com                                                                                       
> Authorization: Basic YWFhOmJiYg==                                                                        
 > User-Agent: curl/7.83.1                                                                                  
 > Accept: */*

> Connection #0 to host hackerone.com left intact                                                         
>Trying 151.101.65.91:80...                                                                             
> Connected to curl.se (151.101.65.91) port 80 (#1)                                                        
>Server auth using Basic with user 'aaa'                                                                  
 > HEAD / HTTP/1.1                                                                                          
 > Host: curl.se                                                                                            
 > Authorization: Basic YWFhOmJiYg==                                                                         
> User-Agent: curl/7.83.1                                                                                   
> Accept: */*
                                                                                                       
  3. from the output we can see, the second url get the same credentials

## Impact

Leak of confidential information (user credential)

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

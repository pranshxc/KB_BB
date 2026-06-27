---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223350'
original_report_id: '223350'
title: Web server is vulnerable to Beast Attack
weakness: Cryptographic Issues - Generic
team_handle: weblate
created_at: '2017-04-24T09:56:12.052Z'
disclosed_at: '2017-04-24T20:37:00.595Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cryptographic-issues-generic
---

# Web server is vulnerable to Beast Attack

## Metadata

- HackerOne Report ID: 223350
- Weakness: Cryptographic Issues - Generic
- Program: weblate
- Disclosed At: 2017-04-24T20:37:00.595Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Supported versions:                                                      
 TLSv1.0 TLSv1.1 TLSv1.2                                                 
Deflate compression: no                                                  
Supported cipher suites (ORDER IS NOT SIGNIFICANT):                      
  TLSv1.0                                                                
     RSA_WITH_AES_128_CBC_SHA                                            
     DHE_RSA_WITH_AES_128_CBC_SHA                                        
     RSA_WITH_AES_256_CBC_SHA                                            
     DHE_RSA_WITH_AES_256_CBC_SHA                                        
  (TLSv1.1: idem)                                                        
  TLSv1.2                                                                
     RSA_WITH_AES_128_CBC_SHA                                            
     DHE_RSA_WITH_AES_128_CBC_SHA                                        
     RSA_WITH_AES_256_CBC_SHA                                            
     DHE_RSA_WITH_AES_256_CBC_SHA                                        
     RSA_WITH_AES_128_CBC_SHA256                                         
     RSA_WITH_AES_256_CBC_SHA256                                         
     DHE_RSA_WITH_AES_128_CBC_SHA256                                     
     DHE_RSA_WITH_AES_256_CBC_SHA256                                     
     TLS_RSA_WITH_AES_128_GCM_SHA256                                     
     TLS_RSA_WITH_AES_256_GCM_SHA384                                     
     TLS_DHE_RSA_WITH_AES_128_GCM_SHA256                                 
     TLS_DHE_RSA_WITH_AES_256_GCM_SHA384                                 
     TLS_RSA_WITH_AES_128_CCM                                            
     TLS_RSA_WITH_AES_256_CCM                                            
     TLS_DHE_RSA_WITH_AES_128_CCM                                        
     TLS_DHE_RSA_WITH_AES_256_CCM                                        
     TLS_RSA_WITH_AES_128_CCM_8                                          
     TLS_RSA_WITH_AES_256_CCM_8                                          
     TLS_DHE_RSA_WITH_AES_128_CCM_8                                      
     TLS_DHE_RSA_WITH_AES_256_CCM_8                                      
----------------------                                                   
Server certificate(s):                                                   
  a2bdec95cbd59ce1f45b5ff03ca15a849f446c2d: CN=avatar.cihar.com          
----------------------                                                   
Minimal encryption strength:     strong encryption (96-bit or more)      
Achievable encryption strength:  strong encryption (96-bit or more)      
BEAST status: vulnerable                                                 
CRIME status: protected

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218801'
original_report_id: '218801'
title: homograph-attack (unicode vuln)
team_handle: brave
created_at: '2017-04-16T20:32:35.590Z'
disclosed_at: '2017-08-10T05:10:52.303Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
---

# homograph-attack (unicode vuln)

## Metadata

- HackerOne Report ID: 218801
- Weakness: 
- Program: brave
- Disclosed At: 2017-08-10T05:10:52.303Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi team
Summary:
Affacted product  appears identicaly different  websites domains
attacker  uses unicode to register domains that look identical to real domains ,These fake domains can be used  to fool users into signing into a fake website, thereby handing over their login credentials to an attacker...
example to demonstrate how an attacker can register their own domain that looks identical to another company’s domain in the browser, 
  ‘epic.com’(healthcare site)  by registering fake site  unicode domain: http://www.xn--e1awd7f.com/

and affected product show unicode domain looks like real domain 
{F176374}
{F176375}

Products affected:

    Brave 1.0.19 (Tested on android 6.0.1;nexus5)

Steps To Reproduce:
1.In browser open http://www.xn--e1awd7f.com/ unicode domain demo 
2. you can see brave browser show fake site like real site in address bar

 
The fix:
 make sure it's display the punycode ..and warning or proper handlings
References:
 http://www.crypto-it.net/eng/attacks/homograph-attack.html
  https://www.wordfence.com/blog/2017/04/chrome-firefox-unicode-phishing/

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

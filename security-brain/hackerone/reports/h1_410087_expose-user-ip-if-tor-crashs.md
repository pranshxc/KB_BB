---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '410087'
original_report_id: '410087'
title: Expose user IP if TOR crashs
team_handle: torproject
created_at: '2018-09-15T13:52:30.148Z'
disclosed_at: '2018-09-21T07:19:11.740Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
tags:
- hackerone
---

# Expose user IP if TOR crashs

## Metadata

- HackerOne Report ID: 410087
- Weakness: 
- Program: torproject
- Disclosed At: 2018-09-21T07:19:11.740Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings,

I have noticed that for unpredictable reason a TOR relay can exposes the IP of an user. I noticed this by going to the server http://195.176.3.24/ and getting information about the headers. I arrived to this header who is : "X-Your-Address-Is" . 

How :
--

- So I went to this tor-relay without being with TOR.
- My IP was shown inside the X-Your-Address-Is
- Then I go to this tor-relay with being with TOR.
- A Tor IP was shown inside the X-Your-Address-Is

{F346664}

Then :
--

I noticed upon this that there was a clear pattern, so I tried to search more information on Shodan exposing information :

- The url for the search was : https://www.shodan.io/search?query=%22Address%22+Content-Encoding%3A+identity
- I obtained servers 
- The X-Your-Address-Is was clearly exposed indicating IPS. 

{F346661}

Expectation :
--

The TOR relay should be able to distinguish a non-tor-ip from a tor-ip. It should not be possible to leak IP user information if the user is not clearly within a TOR session.

Best regards

@Rbcafe

## Impact

- Expose an IP if  TOR crash for unexpected reason. 
- There is no security net if TOR crashes.

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

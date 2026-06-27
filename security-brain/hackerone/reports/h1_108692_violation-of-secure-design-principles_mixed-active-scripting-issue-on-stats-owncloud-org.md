---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '108692'
original_report_id: '108692'
title: Mixed Active Scripting Issue on stats.owncloud.org
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2016-01-06T05:31:33.422Z'
disclosed_at: '2016-02-06T16:11:39.771Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Mixed Active Scripting Issue on stats.owncloud.org

## Metadata

- HackerOne Report ID: 108692
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2016-02-06T16:11:39.771Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have come across with a HTTPS security issue - compromises HTTPS security by loading images from non secure source in stats.owncloud.org
Vulnerability Type: Mixed Active Scripting Issue

Description:
Mixed Active Content is content that has access to and can affect all or parts of the Document Object Model (DOM) of an HTTPS page. This type of mixed content can alter the behavior of an HTTPS page and potentially steal sensitive data from the user. Hence, in addition to the risks for Mixed Passive Content, Mixed Active Content is also exposed to a number of additional attack vectors.
A MITM attacker can intercept requests for HTTP active content. The attacker can then re-write the response to include malicious JavaScript /fonts code. Malicious script can steal the user’s credentials, acquire sensitive data about the user, or attempt to install malware on the user’s system (by leveraging vulnerable plugins the user has installed, for example).

Criticality level: Medium

Criticality level justification:
Data which is transmitted in this link could be read by An attacker who is in Same network in some cases this could help to steal information.

Steps:
1) Visit link https://stats.owncloud.org
2) Press F12 to open Developers tool in Google Chrome OR IE OR in Firefox browser and observe console. You will come across security error - "A Secure Hypertext Transfer Protocol (HTTPS) page has content from a non-secure source.

Mixed content security error messages: : Firefox= 'Loading mixed (insecure) display content "http://stats.owncloud.org/misc/user/logo.png'
. This content should also be served over HTTPS.

Scenario:
There are 3 easy steps to attack the user through a mixed content vulnerability…
1) Set-up a Man-in-the-Middle attack. These are most easily done on public networks such as those in coffee shops or airports.
2) Use a mixed content vulnerability to inject a malicious javascript file. Malicious code will run in an HTTPS website that the user browsers to. The key point is that the HTTPS site has a mixed content vulnerability on it, which means that it executes content downloaded over HTTP. This is where the Man-in-the-Middle attack and Mixed Content vulnerability combine into a dangerous scenario.
“If some attacker is able to either tamper with Javascript or stylesheet files he can effectively also tamper with the other content on your page (e.g. by modifying the DOM ). So it’s either all or nothing. Either all of your elements are served using SSL, then you are secure. Or you load some Javascript or stylesheet files from a plain HTTP connection, then you aren’t secure anymore.”
3) Steal the user’s identity (or do other bad things).

Solution ::
Make sure all content in the page including images, js, fonts are from HTTPS sources.

Reference : http://msdn.microsoft.com/en-us/library/ie/dn423949(v=vs.85).aspx
Video :: http://www.youtube.com/watch?v=zEV3HOuM_Vw

Thanks.

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

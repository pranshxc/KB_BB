---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '84797'
original_report_id: '84797'
title: Config
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-08-26T10:59:13.115Z'
disclosed_at: '2015-10-11T00:24:03.895Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Config

## Metadata

- HackerOne Report ID: 84797
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2015-10-11T00:24:03.895Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

With this bug, a local attacker can infect users with malware. it
works this way, after the sign up page or most pages, a Download
prompt appears. (for example, at your Hackerone Page hackerone.com/owncloud),
However, the downloads url, in my case, it was 

http://download.owncloud.org/community/owncloud-daily-stable8.1.tar.bz2

Did you see what I see? the page is delievered by http. so an attacker
does this, downloads the file, bind a malware to it. host it to his
server, and when a legit user try to donwload it, deliever the payload
binded with the games. user runs that, game over. who's to blame?
well, duh... owncloud!

The easiest solution is just changing the URL from
http://download.owncloud.org/community/owncloud-daily-stable8.1.tar.bz2
to https://download.owncloud.org/community/owncloud-daily-stable8.1.tar.bz2
because the site works both ways, only... the second one gets
downloaded from an encrypted source. I don't even know why you put the
HTTP version anyways.

Note: I am doing this for the points, not the bounty. so please don't damage it.

Thanks again,
Paulos

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

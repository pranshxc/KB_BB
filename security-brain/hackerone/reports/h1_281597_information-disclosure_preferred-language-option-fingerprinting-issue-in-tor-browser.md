---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '281597'
original_report_id: '281597'
title: Preferred language option fingerprinting issue in Tor Browser
weakness: Information Disclosure
team_handle: torproject
created_at: '2017-10-22T02:53:01.305Z'
disclosed_at: '2017-10-24T06:57:45.395Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Preferred language option fingerprinting issue in Tor Browser

## Metadata

- HackerOne Report ID: 281597
- Weakness: Information Disclosure
- Program: torproject
- Disclosed At: 2017-10-24T06:57:45.395Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I'm not so sure if this is an in-scope issue or by-design. But based on my understanding of [1], I feel that Tor doesn't want to make user configuration details of Tor Browser detectable by websites. But in about:preferences#content, there's a "Languages" section that allows users to "choose your preferred language for displaying pages". When users add a language here, there's no warning to tell them that this info will be sent to the websites. The language list will be available to websites in the "Accept-Language" HTTP request header, and in JavaScript API "navigator.languages".

To fix this issue, I think there're three options: 1) remove this option from the settings; 2) let users configure a list of domains for which the language list is sent; other sites get the default value; 3) add a warning in the setting page: "the info of your added languages is sent to all sites, which may be used to fingerprint you" or something like this.

[1] https://www.torproject.org/projects/torbrowser/design/#fingerprinting-linkability, Sources of Fingerprinting Issues

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143064'
original_report_id: '143064'
title: Information Disclosure
weakness: Information Disclosure
team_handle: drchrono
created_at: '2016-06-04T14:00:12.596Z'
disclosed_at: '2016-07-31T07:58:12.924Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Information Disclosure

## Metadata

- HackerOne Report ID: 143064
- Weakness: Information Disclosure
- Program: drchrono
- Disclosed At: 2016-07-31T07:58:12.924Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey, 

I found Following Security issue on your site.

Information Disclosure :-

your Wordpress installation in Disclosing its version Number in https://drchrono.com/blog/readme.html 
This can a hacker in speeding up the process or information gathering though discovering your wordpress version number a attacker could use specific exploits made just for your version.

Missing Best Practice :- 

There are Two outdated plugins in your Wordpress site

                 1.  Wordpress-importer
                  2.  Wufoo-shortcode

This could Serve as a Potential Thread to your site because outdated plugins are often Vulnerable to attacks 
and could also be vulnerable to 0days 

The Website Plugins Should be update regularly to prevent your site from getting attacked.

Prove of Concept :-

https://drchrono.com/blog/wp-content/plugins/wufoo-shortcode/readme.txt
https://drchrono.com/blog/wp-content/plugins/wordpress-importer/readme.txt

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

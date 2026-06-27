---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '88395'
original_report_id: '88395'
title: Information leakage through Graphviz blocks
weakness: Information Disclosure
team_handle: phabricator
created_at: '2015-09-11T01:18:57.641Z'
disclosed_at: '2015-09-13T19:55:14.805Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Information leakage through Graphviz blocks

## Metadata

- HackerOne Report ID: 88395
- Weakness: Information Disclosure
- Program: phabricator
- Disclosed At: 2015-09-13T19:55:14.805Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

(This report amounts to *Unsandboxed Command Execution Considered Harmful*, which you already suspected: https://secure.phabricator.com/T7785)

Graphviz blocks can be used to view a render of any image file readable by the webserver, through the `image` and `shapefile` graph node attributes. This alone leaks some information (for example, installed software packages), and may help bypass access restrictions on Phabricator image files (if local disk file storage is used and the path is somehow known to the attacker).

Combined with a strategically-placed syntax error in the graph specification to get to the `dot` error output, these attributes can more generally be used by an attacker to test for existence and readability of any file in the server.

Steps to reproduce
================
* Install Graphviz along with Phabricator
* Paste the attached snippet in a Remarkup field
* Experience slight feelings of unease and discomfort

Impact
======
Normally, just the limited information disclosure described above. In (what I imagine to be) a typical Phabricator installation, not even that: it is probably fully defused by the fact that `dot` is not present. However, some users may have installed Graphviz for purposes unrelated to Phabricator, unaware of the security implications.

In general, `dot` is much more complex than `cowsay` and running it unsandboxed increases your attack surface in a significant way. Besides Graphviz bugs, you will also have to worry about any libraries that Graphviz plugins use, especially for complex image formats such as PostScript and SVG.

(In fact, current `dot` **will** happily tell GhostScript to run a PS file that may contain arbitrary commands. This requires a specific *"dot with gs support + old gs"* setup not found in any current distro AFAIK.)

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

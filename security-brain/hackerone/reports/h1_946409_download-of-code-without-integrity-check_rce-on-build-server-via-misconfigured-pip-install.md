---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '946409'
original_report_id: '946409'
title: RCE on build server via misconfigured pip install
weakness: Download of Code Without Integrity Check
team_handle: yelp
created_at: '2020-07-29T10:18:34.275Z'
disclosed_at: '2021-02-09T20:01:01.407Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 351
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- download-of-code-without-integrity-check
---

# RCE on build server via misconfigured pip install

## Metadata

- HackerOne Report ID: 946409
- Weakness: Download of Code Without Integrity Check
- Program: yelp
- Disclosed At: 2021-02-09T20:01:01.407Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following Python library has been installed on at least one Yelp owned build server directly from the public PyPI registry.

* https://pypi.org/project/yelp-cgeom/

This package should normally be downloaded from the internal Yelp registry, but a misconfiguration appears to have caused it to be downloaded from `pypi.org` instead.

This package name was previously unclaimed on PyPI. In order to detect such misconfigurations, I have uploaded my own code under the `yelp-cgeom` name.

Whenever `yelp-cgeom` is installed, my `setup.py` script is executed on the machine where it is downloaded. The script sends a callback to my server containing:

* the originating IP
* the machine's hostname
* the current working directory

To avoid breaching the program policy, no further actions are taken.

# Vulnerable machine

At `Wed jul 29 2020 04:27:23 GMT`, and again 20 seconds later, I have received the following callback:

* originating IP: `54.71.19.248`
* hostname: `10-81-21-60-uswest2bdevc.uswest2-devc.yelpcorp.com`
* home directory: `/nail/home/jenkins`
* directory: `/ephemeral/tmpdir/pip-install-o6jnSv/yelp-cgeom`

This indicates that my preinstall script was executed on the server above.

## Impact

If this package had been claimed by an attacker, this would have led to arbitrary code execution on the affected server, as well as allowing the attacker to add backdoors inside the affected project(s) during the build process.

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

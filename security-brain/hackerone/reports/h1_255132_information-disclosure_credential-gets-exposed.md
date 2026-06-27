---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255132'
original_report_id: '255132'
title: Credential gets exposed
weakness: Information Disclosure
team_handle: phabricator
created_at: '2017-07-31T11:21:47.758Z'
disclosed_at: '2017-08-02T18:21:06.852Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Credential gets exposed

## Metadata

- HackerOne Report ID: 255132
- Weakness: Information Disclosure
- Program: phabricator
- Disclosed At: 2017-08-02T18:21:06.852Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

1. Create a repo
2. Mirror it to an URL
3. Assign a credential to the mirror
4. I've now had an existing repo, and wanted to change it to mirror only, so that phabricator pulls from an URL instead of self-hosting.

I now recived this error msg:
    Pull of 'Luke081515Bot' failed: Working copy at "/srv/repos/LUKE" has a mismatched origin URI, "https://Luke081515:<redacted>@bitbucket.org/Luke081515/lukebot". The expected origin URI is "https://newUrl/Luke/Luke081515Bot.git". Fix your configuration, or set the remote URI correctly. To avoid breaking anything, Phabricator will not automatically fix this.

In this case the <redacted> part was my password for bitbucket, completly visible for everyone who is able to see the repo. Phabricator should not expose the whole URLs including passwords. 

So in theory everyone who can edit a repo, but can't view a credential can get access to it by producing this git error and then see the password at the raw error.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '136333'
original_report_id: '136333'
title: Persistent XSS on public wiki pages
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gitlab
created_at: '2016-05-05T02:55:10.735Z'
disclosed_at: '2016-07-27T21:44:23.111Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent XSS on public wiki pages

## Metadata

- HackerOne Report ID: 136333
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gitlab
- Disclosed At: 2016-07-27T21:44:23.111Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Details
There's a persistent cross-site scripting (XSS) vulnerability in the wiki pages. This can lead to an account take over via the leaked API token.

# Proof of concept
As an attacker, create a new public repository. Make sure you have a client that is allowed to push to that repository. For this PoC, lets say the repository is located at `git@gitlab.com/dummy/test.git`. On the client, execute the following commands:

git clone git@gitlab.com/dummy/test.git
cd test
echo "<script>alert('Hello world!');</script>" > index.html
git add index.html
git commit -m "This message is super important"
git push

Now go to https://gitlab.com/dummy/test/wikis/index.html. As you will see, this executes the JavaScript that is stored in the file.

{F91538}

# Impact
GitLab doesn't have a content security policy, which means that clients allow inline Javascript to be executed. This gives access to the current user its API token. The API token can be used to access the user its projects, do actions as the user, give access to potential confidential information, etc.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2471956'
original_report_id: '2471956'
title: Code exec on Github runner via Pull request name
weakness: Code Injection
team_handle: hyperledger
created_at: '2024-04-19T16:38:36.603Z'
disclosed_at: '2024-04-28T18:08:27.840Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- code-injection
---

# Code exec on Github runner via Pull request name

## Metadata

- HackerOne Report ID: 2471956
- Weakness: Code Injection
- Program: hyperledger
- Disclosed At: 2024-04-28T18:08:27.840Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have discovered command injection vulnerability in one of your Github repos.
Apologies for any inconvenience if this type of bug is not of interest to you. Allow me to explain the problem.
GitHub Actions, a powerful tool for automating workflows, can inadvertently introduce security vulnerabilities if not configured securely. Insecure GitHub Actions configuration can lead to various risks, including unauthorized access, data breaches, and code injection attacks.
Currently  https://github.com/hyperledger/cacti/tree/HEAD/.github/workflows/test_weaver-pre-release.yaml#L28 allows attacker to inject arbitrary command and run it on the Github runner. Note the usage of double quotes and untrusted `pull_request.name`.

## Steps to reproduce
- Create a new branch within your fork
- Create a pull request with the `U";cat $GITHUB_WORKSPACE/.git/config | xxd -p | base64; echo "D` title
- config file contains the access token in base64 form
- Wait until `check_release` workflow will be triggered
- Check job logs for encoded `$GITHUB_TOKEN` (by default Github will replace it with *** if you will try just echo it, that is why I used xxd + base64)
- I refrained from creating a PR on your repository to prevent the disclosure of sensitive information to the public and to avoid publicly exposing the vulnerability.
Example run could be found in my fork, attached as screenshot.

## Impact

Such scenario leaves possibility to access `$GITHUB_TOKEN` environment variable, potentially compromising the whole GitHub organization.
Good explanation of the problem could be found at github docs: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions

There are few limits to the attack:
- `$GITHUB_TOKEN` is a short lived token and for the real life attack, whole attack should be scripted until job is still running

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183502'
original_report_id: '1183502'
title: Private RSA key for Vagrant exposed in GitHub repository
weakness: Insecure Storage of Sensitive Information
team_handle: sifchain
created_at: '2021-05-04T06:57:39.842Z'
disclosed_at: '2021-05-07T18:10:47.103Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Private RSA key for Vagrant exposed in GitHub repository

## Metadata

- HackerOne Report ID: 1183502
- Weakness: Insecure Storage of Sensitive Information
- Program: sifchain
- Disclosed At: 2021-05-07T18:10:47.103Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
The private RSA key used for SSH on Vagrant is exposed in sifnode GitHub repository.

## Steps To Reproduce:
1. Visit [this link](https://github.com/Sifchain/sifnode/blob/4fb7523322f74e70600a10fff4dbdd42425c077f/ui/.vagrant/machines/default/virtualbox/private_key) which shows the `private_key` file used for your Vagrant virtual machine

## Suggested solution
Remove the private key from the repository. Even though you remove it, it will still be in the commit history. Therefore, refer to the article by GitHub on [removing sensitive data from a repository](https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)

## Impact

By having the private SSH key published onto your GitHub repo, an attacker would be able to access your Vagrant virtual machine pretending to be you. The private key has the word "private"  for reason and therefore it shouldn't be accessible by unauthorized people.

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

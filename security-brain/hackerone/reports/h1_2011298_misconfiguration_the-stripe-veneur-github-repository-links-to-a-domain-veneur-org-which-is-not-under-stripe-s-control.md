---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2011298'
original_report_id: '2011298'
title: The `stripe/veneur` GitHub repository links to a domain `veneur.org`, which
  is not under stripe's control
weakness: Misconfiguration
team_handle: stripe
created_at: '2023-06-02T17:08:21.698Z'
disclosed_at: '2023-07-03T10:24:59.459Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: Stripe Open Source
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# The `stripe/veneur` GitHub repository links to a domain `veneur.org`, which is not under stripe's control

## Metadata

- HackerOne Report ID: 2011298
- Weakness: Misconfiguration
- Program: stripe
- Disclosed At: 2023-07-03T10:24:59.459Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Initially reported at https://github.com/stripe/veneur/issues/1058. Since that report, the repository's sidebar has been updated to no longer link to the uncontrolled domain. Many of the 179 forks of this repository still contain the link to the uncontrolled domain.

## Summary:
- The github.com/stripe/veneur repository contains security-sensitive code which is designed to run within a company's private network, often as a sidecar on each of their application servers.
- The repository's README and documentation does not contain instructions for installing veneur. Instead, it linked to an external domain, `https://veneur.org`, which contained those instructions.
- The `https://veneur.org` domain appears to be no longer under Stripe's control.
- If the website is not under Stripe's control, it is an easily exploitable vector for a phishing or supply chain contamination attack. The targets of this attack would be user's of the open source release of veneur (not specifically Stripe), and Stripe customers.
- Example attack:
  - step one: control `https://veneur.org`, either because you are the current owner or you purchase the domain.
  - step two: recreate the old site, but edit the installation instructions to reference malicious source code or a docker image built with malicious code.
  - step three: a veneur user follows the instructions
  - outcome: attacker-controlled code/image running inside a privileged environment.
- Example attack two:
  - step one: control `https://veneur.org`, either because you are the current owner or you purchase the domain.
  - step two: replace the contents of the website with a fake Stripe login screen.
  - step three: a veneur user, who is likely to also be a Stripe user, enters their username and password into the fake login screen.
  - outcome: attacker gains access to privileged credentials. Because the `https://veneur.org` website is linked to by an official, Stripe-controlled repository, there is a much greater likelihood that the attack will succeedd than if it had to operate on a different domain.

## Steps To Reproduce:
1. Visit https://github.com/stripe/veneur
2. Click on the `https://veneur.org` link in the sidebar.

Since I initially reported this issue in the Github repository, at https://github.com/stripe/veneur/issues/1058 , the sidebar has been edited to no longer link to `https://veneur.org`. Many of the 179 forks of this repository still contain the link to the uncontrolled domain.

## Supporting Material/References:

Initial report with images:
- https://github.com/stripe/veneur/issues/1058

The link in the sidebar:
- https://user-images.githubusercontent.com/824173/242777008-1e2b02af-be8c-484c-b131-842d570bdb89.png

The contents of the website currently:
- https://user-images.githubusercontent.com/824173/242777079-12830e1c-7928-460c-81b0-26523062f510.png

## Impact

An attacker can easily impersonate Stripe, taking advantage of the fact that this website is linked to by an official Stripe-owned web page. They can use this as the beginning of a phishing or a supply-chain contamination attack targeting Stripe's customers.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '378209'
original_report_id: '378209'
title: Ajouter le même utilisateur que celui déjà inscrit dans les équipes
team_handle: security
created_at: '2018-07-06T14:29:04.296Z'
disclosed_at: '2018-07-17T20:07:40.756Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Ajouter le même utilisateur que celui déjà inscrit dans les équipes

## Metadata

- HackerOne Report ID: 378209
- Weakness: 
- Program: security
- Disclosed At: 2018-07-17T20:07:40.756Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Description:**

Possibilité d'ajouter le même utilisateur que celui déjà inscrit dans les équipes.

### Steps To Reproduce

1. Aller sur https://hackerone.com/team_name/team_members
2. Observer les emails des utilisateurs.
3. Utiliser le même email que celui précédemment inscrit, mais varier les majuscules / minuscules .
4. On remarque qu'il est possible d'ajouter la même adresse que celle déjà inscrite.

### Optional: Your Environment (Browser version, Device, etc)

 * Firefox 

### Optional: Supporting Material/References (Screenshots)

 * ██████████

### FIX ###

* Ajouter du grep sur l'email.

Cordialement

Rbcafe

## Impact

- Consommation serveur inutile.
- Bypass des emails déjà existants.
- Bypass du contrôle des emails déjà existants.

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

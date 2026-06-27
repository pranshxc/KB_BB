---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1018489'
original_report_id: '1018489'
title: Ability to connect an external login service for unverified emails/accounts
  at accounts.shopify.com
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2020-10-25T20:23:48.269Z'
disclosed_at: '2022-04-13T13:11:52.301Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Ability to connect an external login service for unverified emails/accounts at accounts.shopify.com

## Metadata

- HackerOne Report ID: 1018489
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2022-04-13T13:11:52.301Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

## Description
I have found that it is possible to add external login service even if the email address is not verified. This allows someone to create an account with an email he does not own and create some kind of backdoor accounts that would allow him to get access to shops and more.

In the external login services of the profil, it is said that **You do not have an external login service connected to your Shopify ID. Please verify your email address to connect a login service.**. So one should not be able to connect and external login account if the email was not verified.

{F1051426}

## Steps de reproduce
1. Create a new account at `partners.myshopify.com` with the victim email (saltymermaid+victim@wearehackerone.com)

2.  The account is created, now go to your profile at  https://accounts.shopify.com/accounts/{account_id}`

3. In the external login service section or anywhere else in the page, with your browser developper console, add the following HTML snippet `<a href="/accounts/{victim_account_id}/external-login/1" data-method="post">Connect to Google</a>` and replace the **{victim_account_id}** with the victim's account id from the url.

4. Now click on the link you injected in the page and it will bring you too the google account authentication page

5. Connect to your google account or create a new one. You will be redirected to the victims account uppon success.

6. Notice that the external login account was added even if the email was not verified.

7. Now, on another browser, go to https://partners.shopify.com/organizations, enter the victims email address and notice that **Log in with Google** button is shown. You should be able to connect that the "backdoor" account.

## Impact

Ability to create backdoors login accounts via external login services for an account that was not verified could lead to important information disclosures. I think the chances of this happening  are low since a victim would be carreful after receiving the shopify confirmation email but in somes cases, this could lead to important leak of informations.

If you need extra details, just le me know. I will make a POC video soon.

Thank you.

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

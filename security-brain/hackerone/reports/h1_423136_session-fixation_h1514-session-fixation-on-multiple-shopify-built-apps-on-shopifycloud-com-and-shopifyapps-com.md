---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423136'
original_report_id: '423136'
title: H1514 Session Fixation on multiple shopify-built apps on *.shopifycloud.com
  and *.shopifyapps.com
weakness: Session Fixation
team_handle: shopify
created_at: '2018-10-12T21:39:08.264Z'
disclosed_at: '2019-04-25T02:39:59.145Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 140
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- session-fixation
---

# H1514 Session Fixation on multiple shopify-built apps on *.shopifycloud.com and *.shopifyapps.com

## Metadata

- HackerOne Report ID: 423136
- Weakness: Session Fixation
- Program: shopify
- Disclosed At: 2019-04-25T02:39:59.145Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team!,

I'm reporting a Session Fixation issue on multiple shopify-built apps hosted on *.shopifycloud.com and *.shopifyapps.com. Normally Session Fixation is boring but I discovered a way to simply use by-design XSS to authenticate as a user on those affected apps.

#Details
As the policy pointed out XSS on *.shopifycloud.com and *.shopifyapps.com are N/A. That means finding XSS on them should be fairly trivial. Anyway after the XSS on embedded SDK I started to think what I can do with it. I played around some other shopify-built apps and discovered that some of them use signed session and the other use session id. Looking further I realized some which use session id do not generate a new session id after logging in. They are basically assigning the login status in whatever session id you provide in the cookie header. A straight-out Session Fixation. For example, in Shopify Flow, when you hit the index page, a `_flow_session` cookie is assigned. When you log in (/auth/callback), the session doesn't change. As an attacker, if I can write my session id cookie to your browser and you log in, I can use the session id to authenticate as you.

So the attack goes like this:
1. Attacker goes to Shopify Flow and copies the session id it generates
2. Attacker uses XSS on *.shopifycloud.com and writes the cookie scoped to all subdomain to victim `document.cookie='_flow_session=EVIL;domain=.shopifycloud.com;path=/';`
3. Attacker forces victim to log into Shopify Flow (i.e. https://www.shopify.com/admin/apps/flow which redirects to VICTIM_STORE.shopify.com/admin/apps/flow which triggers the login flow)
4. Attacker can now use the session to authenticate as victim

#Steps to Reproduce
1. Be logged into your store as an admin and have Shopify Flow installed
2. Navigate to https://poorvictim.myshopify.com/products/canvas
3. After a while it should redirect to the Shopify Flow page
4. (Attacker) Use another browser, go to https://flow.shopifycloud.com/robots.txt and run this code in console `document.cookie='_flow_session=7b2f6c606fab4186d7be385aa66d53d9'`
5. (Attacker) Navigate to https://flow.shopifycloud.com/?shop=YOUR_STORE.myshopify.com and you should see your (Victim) data for a split second (you are supposed to use this in iframe) (Remember to change the YOUR_STORE in the URL)

## Impact

An attacker can authenticate as the victim.

I have found Session Fixation on the following apps:
* Shopify Flow
* Transporter 
* Launchpad

There are probably some others I haven't tested or forgotten. Let me know if you want me to list them all.

I'm also looking if there's some subdomains on *.shopify.com that suffer from it.

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

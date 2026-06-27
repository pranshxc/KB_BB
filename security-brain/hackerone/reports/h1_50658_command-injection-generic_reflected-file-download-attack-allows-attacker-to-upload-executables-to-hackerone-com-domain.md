---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50658'
original_report_id: '50658'
title: Reflected File Download attack allows attacker to 'upload' executables to hackerone.com
  domain
weakness: Command Injection - Generic
team_handle: security
created_at: '2015-03-09T10:20:23.347Z'
disclosed_at: '2015-04-16T10:21:21.121Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# Reflected File Download attack allows attacker to 'upload' executables to hackerone.com domain

## Metadata

- HackerOne Report ID: 50658
- Weakness: Command Injection - Generic
- Program: security
- Disclosed At: 2015-04-16T10:21:21.121Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi hackerone team,

I'm a friend of Peiying and am looking for a position at hackerone. While playing around with your product, I found a serious vulnerability in your application: it allows attackers to craft executables on the hackerone.com domain rather than the sandboxed one on S3.

1. attacker reports a bug titled `hackerone\"||calc||`
2. attacker can then direct victim to [https://hackerone.com/notifications.bat](https://hackerone.com/notifications.bat)
3. when downloaded and executed, it will open calculator on victim's windows environment

The potentials of this vector is outlined in [Reflected File Download: A New Web Attack Vector](https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/), which does not limit to executing commands on victim's machines.

To fix, since hackerone is a Rails deployment, at the rendering step of the notifications action:

instead of:

`render json: notifications`

do:

    respond_to do |format|
        format.json do
            render json: notifications
        end
    end

so requests of non-json formats would return a 406 Not Acceptable. see [respond_to](http://apidock.com/rails/ActionController/MimeResponds/InstanceMethods/respond_to).

Look forward to hearing back from you soon,

Ricky

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

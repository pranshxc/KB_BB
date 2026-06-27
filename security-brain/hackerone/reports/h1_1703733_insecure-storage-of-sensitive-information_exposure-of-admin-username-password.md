---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1703733'
original_report_id: '1703733'
title: Exposure Of Admin Username & Password
weakness: Insecure Storage of Sensitive Information
team_handle: mtn_group
created_at: '2022-09-18T10:24:40.453Z'
disclosed_at: '2022-12-25T10:48:00.481Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 42
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Exposure Of Admin Username & Password

## Metadata

- HackerOne Report ID: 1703733
- Weakness: Insecure Storage of Sensitive Information
- Program: mtn_group
- Disclosed At: 2022-12-25T10:48:00.481Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team, 
Ther an exposure of your username and password on this    subdomain https://engage2.mtnonline.com/nc/


Exposed Credentials

    uid: "mtnng",
        passwd: "bd31568138edbfc0552a1ecc6886ea5c",



Steps To Reproduce:

Visit https://engage2.mtnonline.com/nc/ 

Now, press CTRL+U to view the source code of this page,


Look for this code




       console.log(message);
    }
}

    (function (){
    const plid = 73;

    const mtnContainer = document.getElementById("mtn20238");
    const mtnUri = mtnContainer.childNodes[0].getAttribute("href");
    mtnContainer.addEventListener("click", ()=>fetch(mtnUri).catch(()=>{}));

    window.mobucksApi.placeAd({
        containerElementId: "mtn20238",
        uid: "mtnng",
        passwd: "bd31568138edbfc0552a1ecc6886ea5c",
        plid:plid,
        }, () => { 
            typeof mtnNoBanner == "function" && mtnNoBanner(plid,mtnContainer);

## Impact

The exposed password is in md5 which I was able to decrypt easily

uid: mtnng
hash = bd31568138edbfc0552a1ecc6886ea
plain password: v0d@c0mS@

And as an attacker, this can be abused in lots of ways such as exposing some client's info

https://adsmobucks.mtnbusiness.com.ng/feed?uid=mtnng&passwd=bd31568138edbfc0552a1ecc6886ea5c&plid=8

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

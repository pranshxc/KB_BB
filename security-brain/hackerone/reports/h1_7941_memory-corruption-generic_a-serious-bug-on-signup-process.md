---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7941'
original_report_id: '7941'
title: A Serious Bug on SIGNUP Process!
weakness: Memory Corruption - Generic
team_handle: localize
created_at: '2014-04-18T01:18:41.452Z'
disclosed_at: '2014-04-22T04:54:07.930Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- memory-corruption-generic
---

# A Serious Bug on SIGNUP Process!

## Metadata

- HackerOne Report ID: 7941
- Weakness: Memory Corruption - Generic
- Program: localize
- Disclosed At: 2014-04-22T04:54:07.930Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found a bug on your registration/Sign UP process.. You should fix this one soon as Possible!
 
With This bug, Attacker will able to create thousands of ID's on you application..

POC
------

it can be done in three (3) ways..

### 1)

By CSRF ..
> * Copy You Registration FORM source (only form code is enough)  and save it as "anyname.html" [[Attached]]
* load this page on browser > http://www.localize.io/pages/sign_up
* get the "CSRFToken" from source and paste it on "CSRFToken" Value section of your anyname.html and save.
* open anyname.html file on browser and fill the form and Click "Sign UP" ..
* if the username is available, ID will be created.. 
* Now reload the anyname.html page and try with different username..

every time you change the USERNAME and click sign UP.. ID will be Created!

### 2)
By Live HTTP Headers (Mozilla Add-on)

> This process is Simple.. [[ Check Attached Screenshot ]] 
Just Change the username and reply..
ID will created everytime..

### 3)
By Creating a php File..
> Attacker can create a PHP File and run it on your application..
it will automatically change the username to a RANDOM one.. so attacker can register IDs as much as he want to create..
I can code with PHP and Curl and i can assure you it will  work flawlessly.. (only if you want)

That's all for now..

Thanks and Regards,
FaisaL Ahmed

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

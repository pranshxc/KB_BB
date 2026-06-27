---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '84709'
original_report_id: '84709'
title: '[API ISSUE] agents can Create agents even after they are disabled !'
weakness: Privilege Escalation
team_handle: zendesk
created_at: '2015-08-25T19:41:28.508Z'
disclosed_at: '2015-09-10T01:23:51.084Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- privilege-escalation
---

# [API ISSUE] agents can Create agents even after they are disabled !

## Metadata

- HackerOne Report ID: 84709
- Weakness: Privilege Escalation
- Program: zendesk
- Disclosed At: 2015-09-10T01:23:51.084Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey guys 

####Description :
The Owner of the Zopim dashboard account has an ability to Create agents and disable then, while disabling the an agent , it restricts him to access him to login to the dash board (this is ohk ) but you are not expiring the access_tokens . if access_tokens are reused we could gain access to the account again ! 

Think of a situation where an Owner creates an agent and gives administration access, when the Owner comes to know that its attacker profile , he just disables it !  but disabling the account doesnt seems secure here , the account can be used via `access_token`

####Steps to Reproduce !

+ Login to Owner account and Create an agent with administrator privilages 
+ Now Open another browser and login to agent account 
+ Create an client in agent account and Do the authorization and get down the `access_token`
+ Now go to Owner account and `disable` the agent
+ Now use this request 

```
curl https://www.zopim.com/api/v2/agents \
  -d '{
        "email": "attacker@attacker.com", \
        "password": "secretpassword", \
        "first_name": "attacker", \
        "last_name": "Anon", \
        "display_name": "Mr Robot", \
        "enabled": 1, \
        "im_server_id": "smith", \
      }' \
  -v  \
  -X POST -H "Authorization: Bearer `access_token_here`"
```
+
+ You could create an account ! 


####Simple Steps To verify 

+ Login to  Agent account and Open this 
   >> https://victim2-80.terminal.com/zopadmin.html
+ Now Click on " Done have access_token? Click Here"
+ IT will prompt "Allow Or Deny "  , Click on Allow
+ Now it will show you the "Access Token ", Copy it 
+ Now open Owner account and disable agent account 
+ Now go here again >> https://victim2-80.terminal.com/zopadmin.html
+ And give access_token there and Click on Submit 
+ An account will be created with email = lol@gmail.com  & password=csrfcsrf

####Video POC :

https://www.youtube.com/watch?v=wZQTlmE0Lz8&feature=youtu.be 

(Sorry for low clarity :p )

####Remediation :
Just expire the `access_tokens` when the account is disabled like you do when you "delete" the account 


Let me know if you need anything 


Regards
N B

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

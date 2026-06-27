---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111417'
original_report_id: '111417'
title: Checking whether user liked the media or not even when you are blocked
weakness: Information Disclosure
team_handle: vkcom
created_at: '2016-01-18T14:16:23.657Z'
disclosed_at: '2016-05-25T18:42:36.353Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Checking whether user liked the media or not even when you are blocked

## Metadata

- HackerOne Report ID: 111417
- Weakness: Information Disclosure
- Program: vkcom
- Disclosed At: 2016-05-25T18:42:36.353Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Poc :
Take 2 accounts A and B 
1.) Now from A id make a random post say http://vk.com/id307083341?w=wall307083341_36
2.)Now from C id try to like the post of A .
3.)Now from B id visit https://vk.com/dev/likes.getList
4.) now put the owner id A and the post id == > 307083341 which 36 in this case 
5.)and in the the friends_only field change 1 to 0 
6.)then hit run you will find that vk.com will return the array of guys who have liked it now open another tab  
7.)Now block B from A account .
8.)Now try to again query https://vk.com/dev/likes.getList the same from 3 you will find that now vk.com will not allow you ! error 
but now 
9.)But these methods are not protected === > Visit now  https://vk.com/dev/likes.isLiked  and now put the owner_id=[307---], item_id=36 , user_id of the guy to which you have to check whether he has liked or not the media  and this time their is no error and vk.com will show liked : 1 

Hence no where in the application this information is being disclosed but here is the end point leaking the information 
raj_v

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

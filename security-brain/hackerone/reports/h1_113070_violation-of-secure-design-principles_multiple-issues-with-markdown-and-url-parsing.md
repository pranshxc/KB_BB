---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113070'
original_report_id: '113070'
title: Multiple issues with Markdown and URL parsing
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-01-27T17:24:36.477Z'
disclosed_at: '2016-04-21T04:25:48.288Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# Multiple issues with Markdown and URL parsing

## Metadata

- HackerOne Report ID: 113070
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-21T04:25:48.288Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

LOOK .
1) html 
example:
`[*<http://myfuneral.ru/>*_<www.hackerone@yandex.ru>_](https://hackerone.com/pisarenko)`
copy + past 
look rezult:
[*<http://myfuneral.ru/>*_<www.hackerone.com@yandex.ru>_](https://hackerone.com/pisarenko)
mailto:www.hackerone.com@yandex.ru" 
2) here the situation is more complicated , the fact that I have mail
`www.hackerone@yandex.ru  address@example.com`  copy past 
look rezult:

www.hackerone@yandex.ru  address@example.com

(click one link  and two link)

2.1) I don't know correctly or not , but look this (possibly a user visited a malicious link)

www.hackerone.com%2Fbugs%3Fsubject=user&report_id=81070&view=all&substates%5B%5D=new&substates%5B%5D=triaged&substates%5B%5D=needs-more-info&substates%5B%5D=resolved&substates%5B%5D=not-applicable&substates%5B%5D=informative&substates%5B%5D=duplicate&substates%5B%5D=spam&text_query=@myfuneral.ru/&sort_type=latest_activity&sort_direction=descending&limit=25&page=1

 (click and Proceed)



3) I attached image , the button is not valid if you insert the profile in the WebSite 

`http://vk.com/i.luck?hackerone@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`

look go to https://hackerone.com/pisarenko/thanks and click "Go back to profile" (not work)

 i think has decided that this report is not eligible for a bounty , but you need to fix

thanks .

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

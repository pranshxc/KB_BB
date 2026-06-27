---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '25281'
original_report_id: '25281'
title: Change Any username and profile link in hackerone
weakness: Privilege Escalation
team_handle: security
created_at: '2014-08-19T18:28:47.434Z'
disclosed_at: '2014-09-25T22:33:35.433Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- privilege-escalation
---

# Change Any username and profile link in hackerone

## Metadata

- HackerOne Report ID: 25281
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2014-09-25T22:33:35.433Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI ,found a vulnerability by which anyone's username or profile link can be changed in  hackerone
Follow the Steps

1.contact support@hackerone.com by your  email hacker@gmail.com  and ask your name from "abc" to "xyz"
2.You will get a reply saying " for confirmation can you say send an email from your email account associated with your username " ie. from victim@gmail.com .
3reply ok and use a spoofing service made by you or  a hacker to send spoofed emails
example https://emkei.cz/
4.know the victims email account and use it to send as senders email address to send a spoofed email saying change my username frm abc to xyz
5.it will be done by the support staff .

By knowing email of victim you can change anyone's username and profile link

i did this while ago with a help of my friends account with his permission. where i followed the similar steps to change the username from ssssss to kaviraj where i didnt use his  email with his username registered to hackerone.

Just a spoofed senders email is enough!

countermeasure

You must validate the email header and must use a proper email service provider like gmail to filter these kind of emails as a countermeasure.

Impact

By this way anyone's username and profile link can be changed without any knowledge to the victim.
the victims hall of fame page name and profile URL could be changed by the attacker as username is changed.So there will be no proof or value of the victims finds and bounty and hall of fame(incase if attacker changes the name and URL to his name .he can say all are his finds and hall of fame are credited to him)
while the victim logs in he will be shocked to see his new name!

I hope you reply me and fix this issue

Thanks
Anand

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

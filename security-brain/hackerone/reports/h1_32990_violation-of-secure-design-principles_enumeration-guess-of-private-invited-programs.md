---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '32990'
original_report_id: '32990'
title: Enumeration/Guess of Private (Invited) Programs
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-10-27T23:13:41.608Z'
disclosed_at: '2015-05-09T08:17:39.151Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Enumeration/Guess of Private (Invited) Programs

## Metadata

- HackerOne Report ID: 32990
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-09T08:17:39.151Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey, 

This bug allows anyone to enumerate usernames of invited programs.For example there are two kinds of program at HackerOne - **Public programs** and **Invited** programs. Generally invited programs are only accessible to certain users based on reputation system. 

Now, for most public programs the username of the program remains same as program name, that is for Slack's program it is *slack*, for Square it is *square*. So my finding to enumerate works like the following (taking example of **████** invitation only program):

████ program is located at https://hackerone.com/████, but it is only accessible to invited users else if an uninvited user visits the page he gets a 404 error, that's sweet. Isn't it ?

But using the following logic: 

https://hackerone.com/████/common_responses.json (500 Internal Server Error)
https://hackerone.com/████/common_responses.json (500 Internal Server Error)
https://hackerone.com/trololol/common_responses.json (404 Not Found)

Based on the responses we can understand that for every existing program (public/invited) the server throws 500 error code but for non-existent program it throws 404 error code. So someone who wants to guess if a company is there in the invited program simply needs to send the following request (assuming company name is same as username, as it is currently in most of the cases at HackerOne):

https://hackerone.com/<company-name-here>/common_responses.json (500 if exists or 404 if it doesn't, then if the username is not in any of the public program then surely it will be in invited program :-) )

This thing can be automated with a list of company names as potential usernames.

Thanks,
Prakhar Prasad

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

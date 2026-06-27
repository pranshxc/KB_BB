---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151459'
original_report_id: '151459'
title: Creating Post on a restricted channel
weakness: Privilege Escalation
team_handle: slack
created_at: '2016-07-15T06:44:55.717Z'
disclosed_at: '2016-09-29T08:34:46.538Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- privilege-escalation
---

# Creating Post on a restricted channel

## Metadata

- HackerOne Report ID: 151459
- Weakness: Privilege Escalation
- Program: slack
- Disclosed At: 2016-09-29T08:34:46.538Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I would like to report a privilege escalation issue in which a member of the team is able to create a post on a channel even if the permission to do so is denied to him by the admin.After the admin has limited the number of users who can post to a specific public channel,an unauthorized user who does not have sufficient authority to post anything on it is able to create the post based on commands available to him.I have attached a POC for further clarification.

The admin in this case has denied the team members from creating any posts on the general channel.
In order to bypass this restriction,login as a team member, and create a command post on any channel and intercept the request. Modify the request by changing the channel ID( replace it with the channel ID of general ) and send the request.
We get the success message and on the channel also we can see that the post has been created.

Steps to reproduce:
1.Login as team member.
2.Create a command post on any public channel.
3.Intercept the request.
4.Replace the channel ID in the request with the one of general channel.

Let me know if any other help is needed.

Thanks,
Harsh.

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

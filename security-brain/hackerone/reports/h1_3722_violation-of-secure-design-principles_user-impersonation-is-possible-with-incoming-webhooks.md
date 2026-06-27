---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3722'
original_report_id: '3722'
title: User impersonation is possible with incoming webhooks
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2014-03-11T17:34:58.308Z'
disclosed_at: '2014-04-10T20:53:37.570Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# User impersonation is possible with incoming webhooks

## Metadata

- HackerOne Report ID: 3722
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2014-04-10T20:53:37.570Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Using the incoming webhook service it is possible to send messages to the team from an arbitrary username. A malicious user could modify the image of the webhook service to match an existing user and then send a message with the username of an existing user. Other users would not be able to tell the difference between messages from the real user and a spoofed message unless they actually examined the user/bot.

Example request:

POST /services/hooks/incoming-webhook?token=G98rIOYar6DPwDINWFcBnEXT HTTP/1.1
Host: mailinator.slack.com
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 87
Connection: keep-alive

payload={"channel": "#general", "username": "TARGET", "text": "I'm a spoofed message!"}


The incoming webhook should not accept username as a parameter, this should be static and stored server-side. At very least a server-side check should verify that the username parameter does not match an existing username.

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

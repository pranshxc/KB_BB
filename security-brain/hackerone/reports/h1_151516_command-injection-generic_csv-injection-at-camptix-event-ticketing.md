---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151516'
original_report_id: '151516'
title: CSV Injection at Camptix Event Ticketing
weakness: Command Injection - Generic
team_handle: iandunn-projects
created_at: '2016-07-15T14:13:39.389Z'
disclosed_at: '2016-08-18T16:38:38.992Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- command-injection-generic
---

# CSV Injection at Camptix Event Ticketing

## Metadata

- HackerOne Report ID: 151516
- Weakness: Command Injection - Generic
- Program: iandunn-projects
- Disclosed At: 2016-08-18T16:38:38.992Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
As you mentioned the scope of vulnerability as
>Any plugin listed on my WordPress.org profile. 
I am reporting this issue.

I have seen from your [WordPress.org](https://profiles.wordpress.org/iandunn/#content-plugins) profile the second plugin listed is **Camptix Event Ticketing**
So I looked at the source code of the plugin (https://github.com/Automattic/camptix)
Although I don't have much knowledge about wordpress plugin development what I understood that you have good filtering for XSS (html tags) when submitting user data (in ticket form)
But no filtering to filter out CSV macros (starts with `=`)
So I installed it in my WP and checked out it with a very simple ticketing with only *Firstname* ,*Lastname* and *Email*

**Reproduction of Bug**
1. From any open to buy ticket sign up for one.
2. In the *First name , Last name* field type `=AND(2>1)` and `=7*7` respectively.
3. Save them.
4. Now from admin panel export the attendees information as CSV. Open the CSV with any application (eg. Excel) and you'll see the First name and Last name field executes the command.
This can be further used to perform command execution on Windows system (high risk)
[See this](http://www.contextis.com/resources/blog/comma-separated-vulnerabilities/)
Since the bug could be exploited by random user and the victim is admin, I think it should be patched.

The **Fix** could be simple. Just escape `=` and `-` `+` signs from user input. this will solve the issue I guess.

Hope you resolve and reward.

------------------------------
Zawad

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

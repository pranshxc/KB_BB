---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152577'
original_report_id: '152577'
title: Content Injection at First & Last Name Parameters that could Lead Fraud Issue
weakness: Violation of Secure Design Principles
team_handle: harvest
created_at: '2016-07-20T15:17:48.837Z'
disclosed_at: '2018-07-29T19:31:08.036Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Injection at First & Last Name Parameters that could Lead Fraud Issue

## Metadata

- HackerOne Report ID: 152577
- Weakness: Violation of Secure Design Principles
- Program: harvest
- Disclosed At: 2018-07-29T19:31:08.036Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I. Introduction
===
Harvest is a Simple Online Time Tracking Software that could allow people to manage their project timeline with their team. As we can see from the short introduction, Harvest allow the team member to collaborate each other to talk about their project and (mostly) all of those users information are managed by the administrator.

Related the information that the administrator can “managed” the team member account, Harvest trying to protect all of those team member by giving the notification in every changed that conduct by the administrator to specific team member account. The notification is given from email.

But the problem exist when the user is “allowed” to change their First and Last Name with any character that people want to submit (such as ` “ > < / : . ` and other).

Generally, Content (which is Text in this case) Injection is an Attack that using the missing input validation at an trusted URL, page, or even form in the specific web application. Usually, this attack can work with the non-aware user that targeted as a victim. In short, based on OWASP, this attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. 
.
II. Summary of the Issue
===
As described above, the issue could allow the Attacker to inject any “Very Convince” message at both of First and Last Name field that didn’t give the validation of the input yet.
.
III. Information
3.1. URL Name: justforPoC.harvestapp.com

.
III. Attack Narrative (Scenario) and Step to Reproduce
===
4.1. Make sure that there are several team member that could be managed by the Administrator (Harvest 1 - Manage People);

4.2. An administrator edit one of their team member name. As a normal flow, the member will get the notification via email (Harvest 2 - Notification);

4.3. The next step is, an administrator change their First and Last Name to create the “very convince” message to be injected at the change name notification (Harvest 3 - Username Changed at Admin). After that, administrator change the victim first / last name __again__ and the system will automatically give the notification to the victim.

As we can see, the normal message is:
>This is a confirmation that your Harvest name was changed by __H1Attacker H1Last__ on the account __JustforPoC__ at 9:55 pm on July 20, 2016.

>Your Harvest name is now H1Victim2 H1LastVictim. If this is incorrect, please contact __H1Attacker H1Last__, or write to Harvest Support.

and the fake message is (Harvest 4 - Notification for User with Fake Admin Username):
>This is a confirmation that your Harvest name was changed by __Your Administrator. Please kindly take a look into http://evilurl.com to make sure everything goes right. After that, you can comeback to check your status again__ on the account __JustforPoC__ at 10:06 pm on July 20, 2016.

>Your Harvest name is now H1Victim2 H1LastVictim. If this is incorrect, please contact __Your Administrator. Please kindly take a look into http://evilurl.com to make sure everything goes right. After that, you can comeback to check your status again__, or write to Harvest Support.

.
V. Recommendation
===
Well, even it will be a classic looks and sounds, but giving the validation of the input at those affected form (First `user_first_name` and Last Name `user_last_name`) will minimize the risk. In this case, every invalid input should be rejected automatically when user trying to save the update.

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

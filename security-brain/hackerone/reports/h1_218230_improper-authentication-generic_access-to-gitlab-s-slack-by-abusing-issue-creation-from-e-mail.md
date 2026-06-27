---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218230'
original_report_id: '218230'
title: Access to GitLab's Slack by abusing issue creation from e-mail
weakness: Improper Authentication - Generic
team_handle: gitlab
created_at: '2017-04-03T00:23:27.224Z'
disclosed_at: '2017-09-21T05:59:20.034Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- improper-authentication-generic
---

# Access to GitLab's Slack by abusing issue creation from e-mail

## Metadata

- HackerOne Report ID: 218230
- Weakness: Improper Authentication - Generic
- Program: gitlab
- Disclosed At: 2017-09-21T05:59:20.034Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

I found a way to become a verified GitLab team member on [Slack](http://gitlab.slack.com). 
By doing so, I gained access to dozens of channels possibly containing sensitive information. Note that I deleted my account `intidc_hackerone` immediately afterwards and did not join, read or engage with any of those channels.



#How it works

- The [GitLab Slack login page](https://gitlab.slack.com/) allows anyone with a `@gitlab.com` e-mail address to join the team:

{F172989}

 - GitLab allows new issues to be created when e-mailed to a unique e-mail address containing a secret token at `incoming+{username}/{projectname}+{token}@gitlab.com`

{F172990}

- As you can see, this is a valid **@gitlab.com** e-mail address, so we can use the issues system to sign up for services like Slack, Facebook Workplace, ...

{F172991}

- These e-mail verification e-mails are e-mailed as new issue tickets to my project:

{F172992}

{F172993}

- After clicking the verification link, all you need to do is set-up 2FA and you'll be able to access GitLab's Slack:

{F172987}

*I took a screenshot of some channels as a proof of concept, but did not actually enter them*
 
 
#Suggested fix

I've seen companies taking different approaches to prevent this from happening:

- Only allow employees to join the Slack group by invitation, [like Facebook does](http://facebook.slack.com).
- Enable SSO or other authentication methods, [like PayPal does](https://paypal.slack.com)

These fixes can be carried out quickly but aren't waterproof: an attacker will still be able to gain access to similar services such as Facebook workplace or Yammer if they use similar authentication methods. 

In the longer run, a safer approach would be:

- Requiring users to mail their issue tickets to a gitlab subdomain e-mail, such as `@reply.gitlab.com`


Please let me know if you have any questions,
Best regards,

Inti

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

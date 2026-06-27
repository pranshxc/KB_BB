---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96337'
original_report_id: '96337'
title: Stored XSS in Slack (weird, trial and error)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2015-10-28T14:32:33.024Z'
disclosed_at: '2015-11-10T18:32:42.063Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Slack (weird, trial and error)

## Metadata

- HackerOne Report ID: 96337
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2015-11-10T18:32:42.063Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi slack. I found a weird, trial and error Stored XSS in Slack... I hope you can get clear of this and get it too.. and I hope you can find the XSS too. Anyway here it is (according to what I did):

1. Go to your Slack or create a new Slack team.
2. In slackbot.. enter this payload:
                        <img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
3. Then, Create a new post and enter the same payload too (as title, and in one paragraph, one code)
4. Share it to slackbot,, and comment using the XSS payload given
5. Then create a snippet.. enter the payload as well... and it is HTML or any format..
6. Add comment using the XSS payload.
7. Click Create snippet

then I refreshed my slack.. I suddenly got an XSS payload.. In some cases, this will work immediately.. but sometimes... you will have to repeat the process. trial and error..

I hope you understand my report... I have provided videos and pictures for clearer details.

Thanks!

Video link: https://youtu.be/UtYrymMgMb8

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

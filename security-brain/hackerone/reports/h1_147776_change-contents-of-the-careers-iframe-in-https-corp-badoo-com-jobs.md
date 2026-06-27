---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147776'
original_report_id: '147776'
title: Change contents of the careers iframe in https://corp.badoo.com/jobs
team_handle: bumble
created_at: '2016-06-27T20:14:44.861Z'
disclosed_at: '2016-07-07T08:54:35.556Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
---

# Change contents of the careers iframe in https://corp.badoo.com/jobs

## Metadata

- HackerOne Report ID: 147776
- Weakness: 
- Program: bumble
- Disclosed At: 2016-07-07T08:54:35.556Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi again badoo team , 
In `https://corp.badoo.com/jobs/?p=` if you check the page you'll see an iframe from `https://jobs.jobvite.com/badoo/` , the `p` parameter is used to control the iframe link for example if you added `https://corp.badoo.com/jobs/?p=some_path` the iframe link will be `https://jobs.jobvite.com/badoo/some_path` , I have tried to set the `p` parameter to something like `../something_else` but the code checks if the parameter contains double dots and if it does , it just sets the iframe url to `https://jobs.jobvite.com/badoo/` in order to prevent showing content from other jobvite account's , however I have found a way to bypass this by adding a *Newline* `%0A` character between the two dots. 

#PoC:
https://corp.badoo.com/jobs/?jkl&p=.%0A./jobvite --> This will show jobvite's open jobs instead of showing badoo's 

Someone can simply create a jobvite account and make it appear on corp.badoo.com by sending the victim a link like `https://corp.badoo.com/jobs/?jkl&p=.%0A./<jobvite_account_handle>` and trick him to provide sensitive information such as emails , names , phone number , images ..etc. since the victim believes that it's badoo's careers page and trusts it.

Here is another PoC:
https://corp.badoo.com/jobs/?jkl&p=.%0A./jobvite/job/o0PBZfw9/apply --> This will show an application form (The attacker can control it) 
 
The severity of this issue lies in the nature of the page , since the victim trusts it and believes that it's badoo's careers page , he will provide sensitive information about himself thinking that he is applying for a job at badoo , then the attacker can use these sensitive information for even more malicious actions.
It can even be used for phishing due to the fact that you control the form fields in jobvite, so someone can create a phishing inside corp.badoo.com and trick users to submit their passwords.

Thanks

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

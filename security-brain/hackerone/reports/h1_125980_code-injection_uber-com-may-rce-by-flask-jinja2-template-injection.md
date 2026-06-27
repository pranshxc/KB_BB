---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125980'
original_report_id: '125980'
title: uber.com may RCE by Flask Jinja2 Template Injection
weakness: Code Injection
team_handle: uber
created_at: '2016-03-25T15:29:39.286Z'
disclosed_at: '2016-04-06T21:15:11.846Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 106
tags:
- hackerone
- code-injection
---

# uber.com may RCE by Flask Jinja2 Template Injection

## Metadata

- HackerOne Report ID: 125980
- Weakness: Code Injection
- Program: uber
- Disclosed At: 2016-04-06T21:15:11.846Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, Uber Security Team

I found an RCE in rider.uber.com.
First, if you change your profile name to {{ '7'*7 }}, and you will receive a mail
"Your Uber account information has been updated"
sent by support@uber.com

And in mail body, you can see your name become '7777777'

This is a vulnerability about Flask Template Engine(Jinja2) Injection , more detail can be seen in these blogs
https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/
https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/

I think it can be a Remote Code Execution vulnerability but there is a length limit :(
But I still can "write" some Python code in "name" filed, there are more examples in attachments and bellow are my payloads

{{ '7'*7 }}
{{ [].__class__.__base__.__subclasses__() }} # get all classes
{{''.__class__.mro()[1].__subclasses__()}} 
{%for c in [1,2,3] %}{{c,c,c}}{% endfor %}
...

Thanks for your patience for reading my report. : )

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

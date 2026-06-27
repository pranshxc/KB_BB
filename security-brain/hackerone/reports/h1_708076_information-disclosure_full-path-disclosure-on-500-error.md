---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '708076'
original_report_id: '708076'
title: Full Path disclosure on 500 error
weakness: Information Disclosure
team_handle: liberapay
created_at: '2019-10-05T06:35:49.716Z'
disclosed_at: '2019-10-05T12:58:47.835Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
asset_identifier: '*.liberapay.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Full Path disclosure on 500 error

## Metadata

- HackerOne Report ID: 708076
- Weakness: Information Disclosure
- Program: liberapay
- Disclosed At: 2019-10-05T12:58:47.835Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

On manipulating cookie 
+ **parameter:** `gitHub_<anything>` 500 error returned with path disclosing of **Python** Files.

##Error Below:
> Traceback (most recent call last):
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/state_chain.py", line 328, in loop
    new_state = function(**deps.as_kwargs)
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/pando/state_chain.py", line 128, in render_response
    output = resource.render(context, state['dispatch_result'], state['accept_header'])
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/aspen/http/resource.py", line 129, in render
    return self.render_for_type(available[0], context)
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/aspen/simplates/simplate.py", line 140, in render_for_type
    exec(self.page_two, context)
  File "/opt/python/bundle/4/app/www/on/%platform/associate.spt", line 36, in <module>
    cookie_obj = json.loads(b64decode_s(cookie_value))
  File "/usr/lib64/python3.6/json/__init__.py", line 354, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python3.6/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python3.6/json/decoder.py", line 355, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 98 (char 97)

## Impact

Information is being disclosed about internal files.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '274990'
original_report_id: '274990'
title: Remote code execution on rubygems.org
weakness: Deserialization of Untrusted Data
team_handle: rubygems
created_at: '2017-10-06T08:49:52.800Z'
disclosed_at: '2017-11-09T05:56:39.178Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: rubygems.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Remote code execution on rubygems.org

## Metadata

- HackerOne Report ID: 274990
- Weakness: Deserialization of Untrusted Data
- Program: rubygems
- Disclosed At: 2017-11-09T05:56:39.178Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When parsing a gem POSTed to the `/api/v1/gems` endpoint, the rubygems.org application immediately calls `Gem::Package.new(body).spec` inside `app/models/pusher.rb`. The authors of the application correctly observed that parsing untrusted YAML is dangerous (since it can serialize more or less arbitrary objects), so they monkey-patched the spec parser to use `Psych.safe_load` set from `config/initializers/forbidden_yaml.rb`.

However, `YAML.load` is called directly when parsing the gem's checksum file in `Gem::Package#read_checksums`. Using classes accessible within the application, I was able to turn this into a call to `Marshal.load` on attacker-controlled data. From there, I was able to use known Marshal exploitation techniques to achieve code execution on the server (I'm omitting some details here for brevity so that I can submit this report right away).

A proof of concept, `poc.gem`, is attached. Run the exploit with the following command:
`cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://rubygems.org/api/v1/gems`

I ran the attached PoC twice. It just does a `wget` to my server.

Please let me know if I should clarify anything! Thanks for running this program.

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

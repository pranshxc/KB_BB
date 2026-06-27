---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '697055'
original_report_id: '697055'
title: Worker container escape lead to arbitrary file reading in host machine [again]
weakness: Privilege Escalation
team_handle: semmle
created_at: '2019-09-18T09:34:52.929Z'
disclosed_at: '2019-10-21T01:32:16.250Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 175
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Worker container escape lead to arbitrary file reading in host machine [again]

## Metadata

- HackerOne Report ID: 697055
- Weakness: Privilege Escalation
- Program: semmle
- Disclosed At: 2019-10-21T01:32:16.250Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
After a successful build, LGTM allow user to view the file list.
By default, only source code files and build config files are reserved (``lgtm.yml`` and ``.lgtm.yml``).
If there are both files in folder, LGTM will process ``lgtm.yml`` file and skip ``.lgtm.yml``, but it still keeps both of files in directory.
By making symlink to ``.lgtm.yml`` file, after successful build, it will point to HOST MACHINE file!

## Steps To Reproduce:

1. Create a simple project which LGTM can build successful.
In this report, I use this project (https://github.com/testanull/test11)
2. Create file: ``lgtm.yml``  with a valid config content, for example:

```
extraction:
  java:
    index:
      build_command:
      - ./custom-build
```

3. Make a symlink point to a HOST MACHINE file/directory with name: ``.lgtm.yml``
4. After successful build, ``.lgtm.yml`` file will contain the host machine file content!

##PoC of reading ``/etc/passwd`` is attached below

## Impact

Give attacker ability to explore the host machine, expose more sensitive informations from it.

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

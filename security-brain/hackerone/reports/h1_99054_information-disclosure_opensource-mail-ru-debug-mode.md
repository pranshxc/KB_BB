---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99054'
original_report_id: '99054'
title: '[opensource.mail.ru] Debug Mode'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-11-11T07:26:51.228Z'
disclosed_at: '2017-03-03T13:14:20.053Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# [opensource.mail.ru] Debug Mode

## Metadata

- HackerOne Report ID: 99054
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-03T13:14:20.053Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Какая-то интересная отладочная информация.

http://opensource.mail.ru/search?q[]=1

Самое интересное то, что от значения переменной q зависит ошибка в том или ином файле.

Удалось получить 3 вида ошибок:


http://opensource.mail.ru/search?q[]=1

undefined method `gsub' for ["1"]:Array ->  file: wiki.rb


http://opensource.mail.ru/search?q=%C0

invalid byte sequence in UTF-8 ->  file: shellwords.rb


http://opensource.mail.ru/search?q=%00

string contains null byte ->  file: git_layer_grit.rb

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

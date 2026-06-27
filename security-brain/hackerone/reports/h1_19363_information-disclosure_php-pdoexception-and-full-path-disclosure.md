---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '19363'
original_report_id: '19363'
title: PHP PDOException and Full Path Disclosure
weakness: Information Disclosure
team_handle: localize
created_at: '2014-07-07T21:02:16.970Z'
disclosed_at: '2015-01-18T21:43:15.886Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# PHP PDOException and Full Path Disclosure

## Metadata

- HackerOne Report ID: 19363
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2015-01-18T21:43:15.886Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi
phrasekey , agian!

in phraseChange action if set to array pdo quote show error!
line 755 index.php

Warning: PDO::quote() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php on line 30

Fatal error: Uncaught exception 'PDOException' with message 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1' in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php:57 Stack trace: #0 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php(57): PDO->exec('DELETE FROM phr...') #1 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php(325): Database::delete('DELETE FROM phr...') #2 /srv/data/web/vhosts/www.localize.im/htdocs/index.php(768): Database::phraseDelete(340, Array) #3 {main} thrown in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php on line 57

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

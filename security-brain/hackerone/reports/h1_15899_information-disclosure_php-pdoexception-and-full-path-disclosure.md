---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15899'
original_report_id: '15899'
title: PHP PDOException and Full Path Disclosure
weakness: Information Disclosure
team_handle: localize
created_at: '2014-06-10T21:54:06.104Z'
disclosed_at: '2014-07-07T17:33:08.427Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# PHP PDOException and Full Path Disclosure

## Metadata

- HackerOne Report ID: 15899
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-07-07T17:33:08.427Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi

in phrases on phrasemove or phraseChange action

- parameter phrasekey set to array  like phraseChange[phraseKey][11]:test
pdo quote show error :

Warning: PDO::quote() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php on line 30

Fatal error: Uncaught exception 'PDOException' with message 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1' in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php:53 Stack trace: #0 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php(53): PDO->exec('UPDATE phrases ...') #1 /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php(351): Database::update('UPDATE phrases ...') #2 /srv/data/web/vhosts/www.localize.im/htdocs/index.php(789): Database::setPhraseGroup(339, Array, '326') #3 {main} thrown in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php on line 53

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

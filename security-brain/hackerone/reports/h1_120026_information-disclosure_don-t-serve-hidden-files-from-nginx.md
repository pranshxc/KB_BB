---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120026'
original_report_id: '120026'
title: don't serve hidden files from Nginx
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-03-02T07:38:48.637Z'
disclosed_at: '2016-07-13T02:32:04.171Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# don't serve hidden files from Nginx

## Metadata

- HackerOne Report ID: 120026
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-07-13T02:32:04.171Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Gratipay team,

I noticed that your nginx setting is not secure.

When you input https://grtp.co/.gitignore in your browser, it will download this hidden file. Even though this file does not contain some sensitive files, we still need to change nginx settings like bellow to forbid future hidden files being downloaded.

**The following code would deny any request to hidden files**

```
location ~* .*/\..* {
               return 403;
       }

```
 **The following code can block sensitive files using nginx**
```

location ~ /(\.ht|\.git|_cron|_setup|_data|_tpl|_tmp|_log|_library|\.idea) {
        deny all;
   }
```

Hope you do your business well. Have a good day.

Rds
jsshen

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

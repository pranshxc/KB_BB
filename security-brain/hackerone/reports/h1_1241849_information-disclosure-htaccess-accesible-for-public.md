---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1241849'
original_report_id: '1241849'
title: Information Disclosure .htaccess accesible for public
team_handle: basecamp
created_at: '2021-06-23T10:18:26.096Z'
disclosed_at: '2021-07-18T14:00:57.599Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
asset_identifier: launchpad.37signals.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Information Disclosure .htaccess accesible for public

## Metadata

- HackerOne Report ID: 1241849
- Weakness: 
- Program: basecamp
- Disclosed At: 2021-07-18T14:00:57.599Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello team!
While doing a preliminary recon on the sub domain of  "launchpad.37signals.com"  I've come across a few sensitive files that should not be facing the public web; I'll leave you a list organized by criticality and some proof.

Information disclosure of path .htaccess on the subdomain of https://launchpad.37signals.com/

POC url : https://_domainkey.launchpad.37signals.com/.htaccess

Medium priority
.htaccess file for https://_domainkey.launchpad.37signals.com 

Options +ExecCGI +MultiViews +FollowSymLinks
AddHandler cgi-script .cgi
php_value include_path "include:../include"
RewriteEngine on
RewriteCond sprockets.js !-f
RewriteRule ^sprockets\.js /nph-sprockets.cgi [P,L]

# Uncomment the next line to enable Sprockets caching
# SetEnv sprockets_generate_output_file true

step to reproduce :

go to the url :https://_domainkey.launchpad.37signals.com/
after add .htacces to the endpoint of url 

like https://_domainkey.launchpad.37signals.com/.htaccess


the page says download the content of .htaccess as a popup.

## Impact

The publicly accessible .htaccess  might be serious as long as those credentials are really being used somewhere (and it seems to me the DBMS isn't facing the public internet anyway). The real impact is that finding such files always grabs the attention of a threat actor, which might give up not so easily influenced by the fact that there might be "more".

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

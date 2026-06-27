---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '309714'
original_report_id: '309714'
title: '[support.wordcamp.org] - publicly accessible .svn repository'
weakness: Improper Access Control - Generic
team_handle: wordpress
created_at: '2018-01-27T08:46:18.037Z'
disclosed_at: '2018-02-01T08:28:39.063Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.wordcamp.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# [support.wordcamp.org] - publicly accessible .svn repository

## Metadata

- HackerOne Report ID: 309714
- Weakness: Improper Access Control - Generic
- Program: wordpress
- Disclosed At: 2018-02-01T08:28:39.063Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Found that .svn repo is publicly accessible. We can verify it by loading https://support.wordcamp.org/.svn/entries in any browser. This is very dangerous as an attacker may download entire source code. More details about this vulnerability provided here:

http://www.adamgotterer.com/post/28125474053/hacking-the-svn-directory-archive

By using https://github.com/anantshri/svn-extractor we can try to download entire svn repository without any authentication and restore the source code. We can also see commit history, users that performed commits and all repository related metadata.

```
$ python svn-extractor.py --url "https://support.wordcamp.org/"
```
I wasn't able to donwload php source code,  because you are using old version of SVN and server will try to execute php scripts even with `svn-base` extension - https://support.wordcamp.org/.svn/text-base/view-attachment.php.svn-base

But we still can get layout of remote application:
```
tree
.
├── ajax-predefined.php
├── ajax-quote.php
├── api.php
├── base-init.php
├── bg-left.gif
├── bin
├── config-sample.php
├── design.css
├── favicon.ico
├── font
│   ├── genericons-regular-webfont.eot
│   ├── genericons-regular-webfont.svg
│   ├── genericons-regular-webfont.ttf
│   └── genericons-regular-webfont.woff
├── footer.php
├── header.php
├── images
│   ├── 24px-white.gif
│   ├── button-grad-active.png
│   ├── button-grad.png
│   ├── icon_attachment.png
│   ├── white-grad-active.png
│   └── white-grad.png
├── includes
│   ├── class.bp-options.php
│   ├── constants.php
│   ├── crud.php
│   ├── db.php
│   ├── form.php
│   ├── mime.php
│   ├── misc.php
│   ├── plugin.php
│   ├── schema.php
│   ├── sp-stats-class.php
│   ├── support-functions.php
│   ├── upgrade.php
│   ├── viewing.php
│   ├── wp-functions.php
│   ├── wp-meta.php
│   └── wp-user.php
├── index.php
├── init.php
├── installer.php
├── js
│   ├── common.js
│   ├── jquery-1.7.2.min.js
│   ├── jquery.autosize-min.js
│   ├── jquery-fieldselection.js
│   ├── jquery-latest.js
│   └── thread.js
├── login.php
├── message-attachment.php
├── message-image.php
├── plugins
│   ├── customcss.php
│   ├── customjs.php
│   ├── fauxlders.php
│   ├── force-ssl.php
│   ├── kissmetrics.php
│   ├── sidebar-history.php
│   ├── sidebar-mods.php
│   ├── sidebar-summary.php
│   └── thread-status.php
├── predefined-edit.php
├── readme.txt
├── settings.php
├── sidebar-thread.php
├── stats.php
├── thread-addnote.php
├── thread-bulk.php
├── thread-create.php
├── thread-delete.php
├── thread-new.php
├── thread-notify.php
├── thread.php
├── thread-reply.php
├── thread-status.php
├── thread-tags.php
├── user-edit.php
├── user.php
└── view-attachment.php
```
And list of usernames that performed commits:
```
List of Usernames used to commit in svn are listed below
1 : xknown
2 : kovshenin
3 : iandunn
4 : briancolinger
5 : westi
6 : polldaddy
7 : thingalon
8 : apokalyptik
9 : josephscott
10 : johnny5
11 : eoigal
12 : lessbloat
13 : shaunandrews
14 : jkudish
```

The fix is very easy, add following line to .htaccess file:
```
RewriteRule (\.svn)/(.*?) - [F,L]
```

## Impact

Anyone can get remote application layout, usernames involved in development. If SVN gets updated or server configuration change it is also possible to download the source code.

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

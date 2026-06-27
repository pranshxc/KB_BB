---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23386'
original_report_id: '23386'
title: Redirect while opening links in new tabs
weakness: Open Redirect
team_handle: security
created_at: '2014-08-09T23:53:26.688Z'
disclosed_at: '2014-09-12T22:26:42.694Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- open-redirect
---

# Redirect while opening links in new tabs

## Metadata

- HackerOne Report ID: 23386
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2014-09-12T22:26:42.694Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello HackerOne,

I'd like to report to you a nice little bug about opening links in new tabs.

When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

POC: 
http://daniel-tomescu.com/hackerone/landpage.php (just click on the link, don't worry, no harm will be done). 

Don't right-click it and open it in new tab, don't use the mouse wheel to open it, don't Ctrl+Click, just do a normal click on the link.

The javascript code that does all the magic:
window.opener.location.replace(newURL);

Ways to solve this:
1. Don't open links from hackerone.com in new tabs using the  target="_blank";
2. Set the window.opener attribute to null on the new tab before redirecting to the landing page, like this:
a) open in a new tab hackerone.com/redirect?link=landingpage
b) use a javascript code: <script>window.opener = null; </script>
c) redirect to the landing page: <script>window.location.reload(landingpage)</script>

I hope you see why this is dangerous: this method has huge potential for tricking hackerone.com that click on external links from this site to be a victim of a scam page because the redirecting is made in the background, while the user is focused on another tab.

More then that, some browsers like Mozilla for Android don't even display the URL, just the page title, so the user has no way of knowing that he was redirected to a scam page.

If an attacker uses this trick while submitting a bug on hackerone.com/someTarget, he may obtain the logon credentials for a representative of "someTarget" and gain access to his account, private reports submitted by other researchers etc.

Tested on Chrome version 36 (latest version), Firefox for Windows and Android (latest versions). Websites that protect themselves against this kind of attack: google.com websites, twitter.com (they open links in new tabs, but the window.opener property is set to null)

Thank you!

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

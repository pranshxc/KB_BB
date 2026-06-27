---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126099'
original_report_id: '126099'
title: Stored XSS in drive.uber.com WordPress admin panel
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-26T00:11:18.223Z'
disclosed_at: '2016-05-14T05:11:55.500Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in drive.uber.com WordPress admin panel

## Metadata

- HackerOne Report ID: 126099
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-05-14T05:11:55.500Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is another bug in the All In One Event Calendar plugin used on *drive.uber.com*. An attacker can inject arbitrary JavaScript in the administrative Dashboard of WordPress. The script would be evaluated under administrator privileges (as only logged-in administrators can view the Dashboard). Such script can use AJAX calls to achieve a server-side compromise unless some kind of special protections are in place.

The script can be injected by causing an error condition in the calendar plugin. One way to trigger an error is described below. Whenever this happens, the plugin disables itself and places an error message "banner" in the administrative Dashboard and shows it to any administrator who logs on afterwards.

The error details can be manipulated by the attacker and special HTML characters aren't filtered. The error message includes e.g. the URL which triggered the error, which is controllable by the attacker.

#Reproducing#

The attack requires sending a malformed HTTP request *without* encoding special characters in the URL. Therefore this can't be done with a normal web browser. For example a PERL script like this produces the request:
~~~~perl
#!/usr/bin/perl
open(NC,"|openssl s_client -connect drive.uber.com:443 -quiet") || die;
print NC "GET /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(/stored-xss/.source)>\r\n";
 HTTP/1.1\r\n";
print NC "Host: drive.uber.com\r\n";
print NC "\r\n";
close(NC);
~~~~
The HTTP response is a redirect back to the "front page", meaning the plugin couldn't render the calendar JSON data as supposed, but encountered an error condition.

Reproducing this of course requires that the plugin is reactivated (it's is currently disabled because I tested this).

Next, when an administrator logs on the system and is presented with the WordPress Dashboard, they should get an alert box, showing that the attacker-supplied JavaScript has been stored in the Dashboard.

Injecting another code won't work until the plugin is reactivated.

#Details#

The error in this case is an invalid format string in an SQL query, caused by the malformed *events_per_page* parameter. The XSS payload is included later in the URL above and gets included in the error message.

I have tested this bug on a local test server running WordPress and the All In One Event Calendar plugin. The difference is that instead of nginx my test server runs Apache. This, or other aspects of your server architecture *might* introduce differences in URL encoding etc. which could prevent the example from working (I'll test with nginx later).

#Impact#

Instead of showing an alert box, the script could use AJAX functions to e.g. create a new administrator user with a known password, or write arbitrary PHP code on the server via the plugin or theme editors. I've referred to such demonstrations in my previous reports.

#Fix#

I haven't reported this to the plugin author yet. One way to protect against this is to comment out the error detail generation in the file wp-content/plugins/all-in-one-event-calendar/lib/exception/handler.php, end of file (not tested).

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

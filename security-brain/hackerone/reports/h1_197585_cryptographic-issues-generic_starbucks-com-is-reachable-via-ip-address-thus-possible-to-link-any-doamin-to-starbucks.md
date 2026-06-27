---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197585'
original_report_id: '197585'
title: Starbucks.com is reachable via ip address thus possible to link any doamin
  to Starbucks.
weakness: Cryptographic Issues - Generic
team_handle: starbucks
created_at: '2017-01-11T17:08:45.379Z'
disclosed_at: '2017-01-26T23:57:29.683Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 8
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Starbucks.com is reachable via ip address thus possible to link any doamin to Starbucks.

## Metadata

- HackerOne Report ID: 197585
- Weakness: Cryptographic Issues - Generic
- Program: starbucks
- Disclosed At: 2017-01-26T23:57:29.683Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

It is possible for anybody to buy a domain name containing negative terms and point it to someone's website in order to damage their reputation. For instance someone could buy the domain child-pornography.com and point it to the address 107.162.135.91 which is the address behind starbucks.com

To illustrate this, I added the entry 107.162.135.91 o my /etc/hosts file and tested. Here is what I obtained:Refer screenshot 1
personally found this user experience terrible as someone could think that starbucks are in favour of child pornography (i just demonstrated it on my domain i.e hackingig.com)

I tested with other websites and experienced other behaviors that I would categorize as follows:

1 - Useful 404 page (happens with www.teavana.com) one of your domain:
For me the worst way of handling this as the image of the targeted website is directly associated with the offending domain. The more useful the 404 page, the bigger the impression that the targeted website would be willing to help with child pornography.

2 - Redirection (happens with microsoft.com):
For instance when accessing child-pornography.com you get redirected to www.microsoft.com. It isn't as bad as above as the offending domain name never appears alongside the targeted website's content, but still bad in my opinion as it gives the impression the targeted website bought the offending domain and redirected it to their website to get more traffic.

3 - Server error (happens with lemonde.fr):
You get an error from the webserver which page doesn't contain any content that can be associated with the targeted website (e.g. default Apache 404 page, completely blank page). I believe that is good as the identify of the targeted website isn't revealed.

Above are the various behaviors I experienced, but I also thought about a fourth way of dealing with this which is described below.

4 - Disclaimer page (haven't found any website implementing that technique):

Display a message such as :

"You ended here because someone bought and linked the  child-pornography.com domain to our website. We do not own this domain and do not associate ourselves with it. This request has been logged by our servers and we will raise this issue with the competent authorities to have this domain taken down. If you want to access our website, please click here."
The good thing about this method is that it can be implemented at application layer (good if you don't have control over web server which happens with some hosting solutions), allows you to protect yourself from any liability, and offer the visitor to be redirected to your own website.

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

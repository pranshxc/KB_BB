---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '428651'
original_report_id: '428651'
title: Subdomain takeover dew to missconfigured project settings for Custom domain .
team_handle: flock
created_at: '2018-07-09T14:00:19.000Z'
disclosed_at: '2018-10-26T17:24:42.075Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 75
tags:
- hackerone
---

# Subdomain takeover dew to missconfigured project settings for Custom domain .

## Metadata

- HackerOne Report ID: 428651
- Weakness: 
- Program: flock
- Disclosed At: 2018-10-26T17:24:42.075Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

While testing flock.com I got a domain **flock.co** what is under flock company . So I stared looking at it's subdomains and got subdomain **newdev.flock.co** . When I visited the subdomain in browser I got a error like below screenshot :-
{F365851}
This took my attention . So I checked the DNS record for this domain .

```
R3liGiOus_HuNt3r$ dig newdev.flock.co
; <<>> DiG 9.10.6 <<>> newdev.flock.co
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13182
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;newdev.flock.co. IN A
;; ANSWER SECTION:
newdev.flock.co. 299 IN CNAME cname.readme.io.
cname.readme.io. 299 IN CNAME readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com.
readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com. 59 IN A 52.0.214.29
readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com. 59 IN A 52.5.249.117
;; Query time: 69 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Jul 09 04:58:06 +06 2018
;; MSG SIZE rcvd: 175
```

From above record we can say the subdomain is pointing to **CNAME cname.readme.io** . So I start looking at custom domain documents on **readme.io** website to understand how they works . From their document I understand that :-

* You need a subdomain pointing to your readme.io subdomain **[yoursubdomain.readme.io]** .
* Your subdomain should be configured in domains settings in following page **https://dash.readme.io/project/<project
_Name>/v1.0/domains**

So to takeover I need to check if **cname.readme.io** is alreday claimed of not . But Unfortunately it was already claimed :( . But I have seen many such services doesn't force users to verify their ownership of domains by using same CNAME txt record like their service subdomain . So still there's a hope .
I opened a account in **readme.io** and I got a subdomain **newdev.readme.io** . Then I go to **domains settings** **https://dash.readme.io/project/newdev/v1.0/domains** and in Custom Domain Field used **newdev.flock.co** as value and save changes .
Now when I visited **newdev.flock.co** It redirected me to **http://newdev.flock.co/inactive** this page what saying now that Not Yet Active.

{F365852}

This is showing as I am using a trail account . In the webpage title you will see my project name what I used while creating the project . So now this domain is serving my contents from newdev.readme.io project page .

**How to avoid such issues ? :-** Always update your DNS records . remove CNAME or any other DNS records what is not in used .

If you find a security vulnerability feel free to contact them via security@flock.com

 You can find me on [Facebook](https://www.facebook.com/prial261) anytime .
**My blog :-** https://medium.com/@prial261

Thanks for reading .

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '918946'
original_report_id: '918946'
title: Subdomain takeover due to an unclaimed Amazon S3 bucket on ███
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2020-07-08T14:05:14.708Z'
disclosed_at: '2020-09-03T17:29:19.205Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Subdomain takeover due to an unclaimed Amazon S3 bucket on ███

## Metadata

- HackerOne Report ID: 918946
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2020-09-03T17:29:19.205Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An unclaimed Amazon S3 bucket on █████████ gives an attacker the possibility to gain full control over this subdomain.

**Description:**
`███████` pointed to an S3 bucket that did no longer exists. The bucket points to an Amazon S3 website bucket in the US East region. I claimed this bucket and successfully took over this subdomain. 

Note:
I am reporting this issue to DoD since: "████████ ██████" The ████████ is linked to ███, so I believe this belongs here. I discovered this domain initially from the DoD websites list. Please excuse if this is a misconception. 

## Impact
This is extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the ██████████ domain. This would allow them to post malicious content which would be mistaken for a valid site. They could:
 * XSS
 * Phishing
 * Bypass domain security 
 * Steal sensitive user data, cookies, etc. 

## Step-by-step Reproduction Instructions
`dig ███` results in: 

```
; <<>> DiG 9.11.3-1ubuntu1.12-Ubuntu <<>> ███
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53839
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;███████.    IN  A

;; ANSWER SECTION:
██████████. 1022 IN CNAME   ████-website-us-east-1.amazonaws.com.
██████████-website-us-east-1.amazonaws.com. 1022 IN CNAME s3-website-us-east-1.amazonaws.com.
s3-website-us-east-1.amazonaws.com. 2542 IN A   █████

;; Query time: 304 msec
;; SERVER: 10.68.0.1#53(10.68.0.1)
;; WHEN: Wed Jul 08 22:01:20 KST 2020
;; MSG SIZE  rcvd: 154
```

1. █████████ points to an Amazon S3 bucket in the S3 US East 1 region. Visiting http://███████ revealed that the bucket did not exist (refer to `before.png`). 
2. I created an S3 bucket with the name `████████` on my S3 account in the US East 1 region and uploaded an `index.html` and  an XSS POC (`xss_poc_998877665544332211.html`).
3. Visiting http://███ shows the successful subdomain takeover. View the page source to see the following comment: ` <!-- Demonstrated subdomain takeover by chron0x -->`
4. Visiting http://████████/xss_poc_998877665544332211.html you can see the simple XSS payload in action. 

## Suggested Mitigation/Remediation Actions
Remove the █████ DNS entry and I will remove the bucket from my Amazon account as soon as this issue is resolved. If you want to reclaim the domain instead, please let me know in the comments and I free the bucket before.

## Impact

High. An attacker can use the domain for various malicious activities ranging from XSS, over phishing to cookie stealing, etc. All of this while using a trusted domain name (██████).

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

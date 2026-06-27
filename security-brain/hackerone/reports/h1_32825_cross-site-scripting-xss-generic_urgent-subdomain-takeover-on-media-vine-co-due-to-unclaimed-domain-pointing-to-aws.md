---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '32825'
original_report_id: '32825'
title: URGENT - Subdomain Takeover on media.vine.co due to unclaimed domain pointing
  to AWS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-10-25T23:46:23.949Z'
disclosed_at: '2014-11-03T23:37:26.039Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# URGENT - Subdomain Takeover on media.vine.co due to unclaimed domain pointing to AWS

## Metadata

- HackerOne Report ID: 32825
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-11-03T23:37:26.039Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
This is an urgent issue and I hope you will act on it likewise.
Your subdomain media.vine.co is pointing to AWS S3, but no bucket was connected to it. Actually, the reason to it is due to the CNAME of the meda.vine.co-DNS-entry:

```
media.vine.co
 -> media.vine.co is an alias for vines.s3.amazonaws.com.
```

This might have worked before, since there is a bucket with the name "vines". However, these are the rules for how CNAMEs to S3 are working currently:

> Customizing Amazon S3 URLs with CNAMEs
> 
> Depending on your needs, you might not want "s3.amazonaws.com" to appear on your website or service. For example, if you host your website images on Amazon S3, you might prefer http://images.johnsmith.net/ instead of http://johnsmith-images.s3.amazonaws.com/.
> 
> The bucket name must be the same as the CNAME. So http://images.johnsmith.net/filename would be the same as http://images.johnsmith.net.s3.amazonaws.com/filename if a CNAME were created to map images.johnsmith.net to images.johnsmith.net.s3.amazonaws.com.

So what happens here is actually that, since media.vine.co is pointing to S3, S3 is actually checking if there's a bucket with that name. Which in this case was not true. So I was able to claim the bucket media.vine.co and thus, can place content on this URL.

 _You should immediately remove the DNS-entry for media.vine.co pointing to AWS S3._ 

Since I have complete control over the subdomain I can do whatever I want on it. The restriction I have now is that I'm not able to serve anything on the root-URL ( http://media.vine.co/ ) – however – if I would have created the bucket in the correct region (West-1) in AWS, this would've worked.

Creating a login form that would fool anyone, since it's present on a Vine.co domain.

POC-link:
http://media.vine.co/login

POC-image attached.

This is really severe. Foolproof phishing. XSS on vine.co. Potential malware spread through a domain you – in this case – do not control. Extremely painful for the Company Brand.

Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

Regards,
Frans

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

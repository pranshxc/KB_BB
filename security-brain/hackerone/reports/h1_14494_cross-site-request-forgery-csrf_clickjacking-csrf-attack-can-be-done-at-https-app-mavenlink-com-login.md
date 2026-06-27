---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14494'
original_report_id: '14494'
title: Clickjacking & CSRF attack can be done at https://app.mavenlink.com/login
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mavenlink
created_at: '2014-06-02T22:25:15.066Z'
disclosed_at: '2014-09-19T15:35:11.812Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Clickjacking & CSRF attack can be done at https://app.mavenlink.com/login

## Metadata

- HackerOne Report ID: 14494
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mavenlink
- Disclosed At: 2014-09-19T15:35:11.812Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
My name is Vineet bhardwaj. i am security researcher and i pen test your website( https://app.mavenlink.com/login) and i found there is click jacking attack and CSRF attack can be done.

POC:

<html><head>
<title> CSRF testing </title>
<style>

frame {

opacity: 0.5;
border: none;
position: absolute;
top: 0px;
left: 0px;
z-index: 1000;
}
</style>
</head>
<body>
<script>
window.onbeforeunload = function()
{
return " Do you want to leave ?";
}
</script>
<p> site is vulnerable for CSRF! by Vineet bhardwaj</p>
<iframe id="frame" width="100%" height="100%" src="https://app.mavenlink.com/login"></iframe>
</body>
</html>

Procedure: 1. for test your website is vulnerable to clickjacking or CSRF or not ......
open pen-test-for-CSRF.html (in attachment)

2. in iframe tag give link to https://app.mavenlink.com/login (already given in .html file)

save "pen-test-for-CSRF.html" open in your browser if your website open with the text "site is vulnerable " and given below with your whole site than your domain is vulnerable to clickjacking attack & CSRF.

Impact: An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking

Note : check the attachment.;- 1. pent-test-for-CSRF.html
2. image for proof

waiting for positive response ........

Thanks,
Vineet

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

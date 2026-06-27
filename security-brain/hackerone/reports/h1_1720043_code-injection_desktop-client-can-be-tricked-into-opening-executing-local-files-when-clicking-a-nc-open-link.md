---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1720043'
original_report_id: '1720043'
title: Desktop client can be tricked into opening/executing local files when clicking
  a nc://open/ link
weakness: Code Injection
team_handle: nextcloud
created_at: '2022-10-02T20:51:25.495Z'
disclosed_at: '2023-02-10T09:28:27.289Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- code-injection
---

# Desktop client can be tricked into opening/executing local files when clicking a nc://open/ link

## Metadata

- HackerOne Report ID: 1720043
- Weakness: Code Injection
- Program: nextcloud
- Disclosed At: 2023-02-10T09:28:27.289Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/nextcloud/desktop/pull/4771 added support for "local edit", this feature is however implemented in an insecure way.

[The code](https://github.com/nextcloud/desktop/blob/ee98244877e8ccaaa8487f2487c31ce112b746c5/src/gui/folderman.cpp#L1476-L1480) is calling into `QDesktopServices::openUrl(QUrl::fromLocalFile(foundFiles.first()));` and `foundFiled.first()` will be the path of the file specified via the deeplink:

```cpp
    // In case the VFS mode is enabled and a file is not yet hydrated, we must call QDesktopServices::openUrl from a separate thread, or, there will be a freeze.
    // To avoid searching for a specific folder and checking if the VFS is enabled - we just always call it from a separate thread.
    QtConcurrent::run([foundFiles] {
        QDesktopServices::openUrl(QUrl::fromLocalFile(foundFiles.first()));
    });
```

`QDesktopServices::openUrl` is however not suited for not trusted user input as it will also execute files directly.

## Proof of concept

The following proof of concept was performed under Windows 10:

1. In the web interface create a `test.vbs` file such as `MsgBox "Hallo", VBOKOnly, "Ok"`.
2. Open `nc://open/mSnmByRJcj6cwKwX@demo1.nextcloud.com/test.vbs` in the browser (adjust username and instance path)
3. The VB Script will be executed and a popup will appear.

**Note:** This can also be exploited by a remote attacker if they upload a file to the same instance a user has access to.

## Recommendations

There are several mitigation recommendations here:

- Add a CSRF token to the `nc://open/` link and have the client verify the token on request.
- Ensure only safe file types can be opened using a local file viewer. 

## Disclosure Policy
Please note that all bugs reported by [Authentick GmbH](https://www.authentick.net) will be publicly disclosed within 90 days of vendor notification. In extraordinary cases we may increase that upon request by the vendor.

## Impact

The Nextcloud Desktop Client in version 3.6.0 is vulnerable to a Remote Code Execution that can be exploited by anyone that is able to upload files to an instance the user has access to. **In many cases this will be everyone due to public chats, files drop upload, etc.**

Exploitation just requires the victim to visit a malicious web page (or click a link on an email or anything like that)

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

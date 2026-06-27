---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '397478'
original_report_id: '397478'
title: Privilege Escalation via Keybase Helper
weakness: Privilege Escalation
team_handle: keybase
created_at: '2018-08-20T23:04:05.380Z'
disclosed_at: '2018-12-18T19:28:56.310Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 115
tags:
- hackerone
- privilege-escalation
---

# Privilege Escalation via Keybase Helper

## Metadata

- HackerOne Report ID: 397478
- Weakness: Privilege Escalation
- Program: keybase
- Disclosed At: 2018-12-18T19:28:56.310Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A privilege escalation vulnerability exists within the KeybaseHelper application available when installing the Keybase Desktop Application on MacOS.

The issue is exposed via a LaunchDaemon plist which is installed within `/Library/LaunchDaemons/keybase.Helper.plist`. This file is responsible for launching `/Library/PrivilegedHelperTools/keybase.Helper` for the registered mach port keybase.Helper.

If we take the source code located at https://github.com/keybase/client/blob/master/osx/Helper/KBHelper.m, we can see a number of exposed "methods" via an XPC connection, including:

* remove - Ability to remove any file on the filesystem as the root user
* move - Ability to move any file on the filesystem as the root user
* createDirectory - Ability to create a directory as the root user, and provide attributes such as the owner UID/GID and permissions
* addToPath - Add applications to the /usr/local/bin directory
* kextInstall - Add and start kext 

Interacting with the helper via XPC takes place via the MPMessagePack framework, which is available from https://github.com/gabriel/MPMessagePack/blob/master/XPC/MPXPCClient.m.

If we craft a very simple POC, we can see that it is trivial to place files within dangerous locations:

```
    NSError *error;
    MPXPCClient *client = [[MPXPCClient alloc] initWithServiceName:@"keybase.Helper" privileged:true];
    [client connect:&error];
    
    // Moves any file from "source" to "destination" as the root user
    [client sendRequest:@"move" params:@[@{@"source":@"/tmp/src", @"destination":@"/Library/dst"}] completion: ^(NSError *error, id value) {
        NSLog(@"WORKS");
    }];
 ``` 

It does appear than an effort has been made to avoid executing arbitrary applications by the helper, for example, we can see the following comments within the "" method:

```
    // Make sure the passed-in redirector binary points to a proper binary
    // signed by Keybase, we don't want this to be able to run arbitrary code
    // as root.
```

This doesn't stop us from elevating privileges however, for example, we can simply use the 'move' method to copy any file (or overwrite any file). As a simple example, below we can see a simple operation moving a plist file into /Library/LaunchDaemons/com.xpnsec.test.plist:

```
    [client sendRequest:@"move" params:@[@{@"source":@"/tmp/elevate.plist", @"destination":@"/Library/LaunchDaemons/com.xpnsec.test.plist"}] completion: ^(NSError *error, id value) {
        NSLog(@"WORKS");
    }];
```

On reboot, we see that our service is installed and executed as the root user.

Alternatively, we can simply copy our malicious payload using the above method to `/Library/PrivilegedHelperTools/keybase.Helper` and spawn via our XPC call.

## Impact

The impact would be elevation of privileges from any user with permission to access the keybase.Helper XPC service (which is currently all users) to the root user on macOS.

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

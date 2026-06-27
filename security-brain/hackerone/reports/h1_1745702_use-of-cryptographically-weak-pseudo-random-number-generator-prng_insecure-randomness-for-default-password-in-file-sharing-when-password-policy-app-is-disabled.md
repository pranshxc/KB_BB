---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1745702'
original_report_id: '1745702'
title: Insecure randomness for default password in file sharing when password policy
  app is disabled
weakness: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
team_handle: nextcloud
created_at: '2022-10-21T11:35:30.802Z'
disclosed_at: '2023-03-30T08:45:42.098Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-cryptographically-weak-pseudo-random-number-generator-prng
---

# Insecure randomness for default password in file sharing when password policy app is disabled

## Metadata

- HackerOne Report ID: 1745702
- Weakness: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
- Program: nextcloud
- Disclosed At: 2023-03-30T08:45:42.098Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Sharing links can be protected with a password. However, the function used for generating this password is using cryptographically insecure RNG.

`server-25.0.0\apps\files_sharing\src\utils\GeneratePassword.js` (lines 36-55):

```php
export default async function() {
	// password policy is enabled, let's request a pass
	if (config.passwordPolicy.api && config.passwordPolicy.api.generate) {
		try {
			const request = await axios.get(config.passwordPolicy.api.generate)
			if (request.data.ocs.data.password) {
				return request.data.ocs.data.password
			}
		} catch (error) {
			console.info('Error generating password from password_policy', error)
		}
	}

	// generate password of 10 length based on passwordSet
	return Array(10).fill(0)
		.reduce((prev, curr) => {
			prev += passwordSet.charAt(Math.floor(Math.random() * passwordSet.length))
			return prev
		}, '')
}
```

The first part of the function handles the password generation in a safe way when a password policy is present. However, there is another variant generating the password using `Math.random` function, which is not appropriate for use in a security-sensitive context.

Citation from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random):
*"Note: Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead, and more precisely the window.crypto.getRandomValues() method."*

## Supporting Material/References:
  * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
 * https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues

## Impact

An attacker might be able to access the shared files even without knowledge of the password.

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

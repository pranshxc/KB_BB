---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277534'
original_report_id: '277534'
title: Timing Attack in Google Authenticator - Per User Prompt
weakness: Cryptographic Issues - Generic
team_handle: iandunn-projects
created_at: '2017-10-16T01:06:52.286Z'
disclosed_at: '2017-10-29T00:35:04.682Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 6
asset_identifier: WordPress.org plugins
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Timing Attack in Google Authenticator - Per User Prompt

## Metadata

- HackerOne Report ID: 277534
- Weakness: Cryptographic Issues - Generic
- Program: iandunn-projects
- Disclosed At: 2017-10-29T00:35:04.682Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

*Google Authenticator - Per User Prompt* contains a timing attack vulnerability in how it validates the application password for a user account.

```
if ( sha1( $attempted_password_plaintext ) === $valid_password_hash || wp_check_password( $attempted_password_plaintext, $valid_password_hash ) ) {
	$this->is_using_application_password = true;
	return $user;
}
```
__wp-content/plugins/google-authenticator-per-user-prompt/google-authenticator-per-user-prompt.php__

As the above code runs on the `authenticate` hook, and uses a strict equality check, it's possible to brute force an application password using a timing attack and gain access to the account, without needing the real password or even a valid OTP token.

The plugin adds two `authenticate` hooks, one for the above app password check, then a second that does the OTP validation stuff, but *only* if the not using an app password. This means that we only need the app password to login, which we can brute force via timing attack.

```
if ( 'enabled' == trim( get_user_option( 'googleauthenticator_enabled', $user->ID ) ) && ! $this->is_using_application_password ) {
    // ... OTP stuff
}
```

The correct way to check the app password is to use `hash_equals()`, which is safe from timing attacks - https://secure.php.net/manual/en/function.hash-equals.php

Example:

```
if ( hash_equals( sha1( $attempted_password_plaintext ), $valid_password_hash ) || ... {
```

It's worth noting that `hash_equals()` is already in use in `Google_Authenticator_Per_User_Prompt::verify_login_nonce()`.

All accounts that have an app password enabled (which is not by default) are vulnerable to takeover using this method.

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

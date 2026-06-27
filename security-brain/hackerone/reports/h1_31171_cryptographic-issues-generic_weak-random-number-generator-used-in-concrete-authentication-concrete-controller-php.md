---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31171'
original_report_id: '31171'
title: Weak random number generator used in concrete/authentication/concrete/controller.php
weakness: Cryptographic Issues - Generic
team_handle: concretecms
created_at: '2014-10-12T19:12:16.608Z'
disclosed_at: '2014-10-26T01:43:24.385Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Weak random number generator used in concrete/authentication/concrete/controller.php

## Metadata

- HackerOne Report ID: 31171
- Weakness: Cryptographic Issues - Generic
- Program: concretecms
- Disclosed At: 2014-10-26T01:43:24.385Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

```php

    private function genString($a = 20)
    {
        $o = '';
        $chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}|":<>?\'\\';
        $l = strlen($chars);
        while ($a--) {
            $o .= substr($chars, rand(0, $l), 1);
        }
        return md5($o);
    }
```

Using substr(rand()) then running md5() on the output would be better replaced by using bin2hex() and either openssl_random_pseudo_bytes($a) or mcrypt_create_iv($a, MCRYPT_DEV_URANDOM)

For example:

```php
    private function genString($a = 20)
    {
        if (function_exists('mcrypt_create_iv')) {
            return bin2hex(mcrypt_create_iv($a, MCRYPT_DEV_URANDOM);
        }
        return bin2hex(openssl_random_pseudo_bytes($a));
    }
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

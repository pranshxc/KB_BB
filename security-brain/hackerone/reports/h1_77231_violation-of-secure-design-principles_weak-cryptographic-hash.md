---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77231'
original_report_id: '77231'
title: Weak Cryptographic Hash
weakness: Violation of Secure Design Principles
team_handle: wordpoints
created_at: '2015-07-21T07:29:14.331Z'
disclosed_at: '2015-07-23T06:47:08.280Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Weak Cryptographic Hash

## Metadata

- HackerOne Report ID: 77231
- Weakness: Violation of Secure Design Principles
- Program: wordpoints
- Disclosed At: 2015-07-23T06:47:08.280Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Issue:

The following files are vulnerable to this issue:

\src\includes\class-breaking-updater.php line 246 and 247

protected function check_module( $module ) {

		$rand_str = str_shuffle( md5( microtime() ) );
		$nonce = md5( $rand_str . 'wordpoints_check_modules-' . $module );

\src\admin\includes\class-wordpoints-modules-list-table.php line 541

switch ( $column_name ) {

					case 'cb':
						$checkbox_id = 'checkbox_' . md5( $module_data['name'] );

\src\components\points\includes\class-wordpoints-points-logs-query.php line 705

private function _calc_cache_query_md5() {

		if ( ! isset( $this->_cache_query_md5 ) ) {
			$this->_cache_query_md5 = md5( $this->get_sql() );
		}
	}

Explanation:

Weak cryptographic hashes are susceptible to attacks like rainbow table searches. Hashing algorithms like MD5 and SHA-1 has been marked obsolete according to latest coding standards. This risk the integrity of security critical data to be compromised.

Recommendation:

Discontinue the use of MD5 and SHA-1 algorithms. Use SHA-256 or above to perform one way hashing for better security and integrity of data.

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

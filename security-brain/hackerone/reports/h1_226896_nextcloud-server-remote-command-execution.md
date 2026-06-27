---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226896'
original_report_id: '226896'
title: Nextcloud Server Remote Command Execution
team_handle: nextcloud
created_at: '2017-05-08T14:12:27.054Z'
disclosed_at: '2017-05-10T09:02:11.391Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
---

# Nextcloud Server Remote Command Execution

## Metadata

- HackerOne Report ID: 226896
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-05-10T09:02:11.391Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hy NextCloud Security Team i found a critical vulnerability (RCE) :

Nextcloud Server 11.0.2 is affected by a critical vulnerability, which gives to the attacker complete permission to run a system command. 

The root cause is insufficient validation of arguments to the exec function.

Vulnerable Code (498 - 525) /lib/private/legacy/helper.php:
===================
public static function findBinaryPath($program) {
		$memcache = \OC::$server->getMemCacheFactory()->create('findBinaryPath');
		if ($memcache->hasKey($program)) {
			return $memcache->get($program);
		}
		$result = null;
		if (self::is_function_enabled('exec')) {
			$exeSniffer = new ExecutableFinder();
			// Returns null if nothing is found
			$result = $exeSniffer->find($program); 
			if (empty($result)) {
				$paths = getenv('PATH');
				if (empty($paths)) {
					$paths = '/usr/local/bin /usr/bin /opt/bin /bin';
				} else {
					$paths = str_replace(':',' ',getenv('PATH'));
				}
				$command = 'find ' . $paths . ' -name ' . escapeshellarg($program) . ' 2> /dev/null';
				exec($command, $output, $returnCode);
				if (count($output) > 0) {
					$result = escapeshellcmd($output[0]);
				}
			}
		}
		// store the value for 5 minutes
		$memcache->set($program, $result, 300);
		return $result;
	}

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57263'
original_report_id: '57263'
title: Rank Creation function not validating user inputs.
weakness: Command Injection - Generic
team_handle: wordpoints
created_at: '2015-04-18T22:15:28.429Z'
disclosed_at: '2015-06-04T18:58:38.653Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# Rank Creation function not validating user inputs.

## Metadata

- HackerOne Report ID: 57263
- Weakness: Command Injection - Generic
- Program: wordpoints
- Disclosed At: 2015-06-04T18:58:38.653Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

SQL Injection Attack,  command injection and arbitrary code execution Possible.

By source code review, I found that rank creation parameters (name, type, group) for wordpoints_add_rank() in ranks.php are not sanitized or validated. It may allow an attacker to Inject arbitrary code during rank creation which is then passed to SQL for database update leading to SQL Injection Attack.

$inserted = $wpdb->insert(
		$wpdb->wordpoints_ranks
		, array(
			'name'       => $name,
			'type'       => $type,
			'rank_group' => $group,
			'blog_id'    => $wpdb->blogid,
			'site_id'    => $wpdb->siteid,
		)
	);

$rank_id = (int) $wpdb->insert_id;

	foreach ( $meta as $meta_key => $meta_value ) {
		wordpoints_add_rank_meta( $rank_id, $meta_key, $meta_value );
	}


Similarly for retrieving Rank by get_data() in class-wordpoints-rank.php using specially crafted ID may lead database exposure) 
public static function get_data( $id ) {

		$rank_data = wp_cache_get( $id, 'wordpoints_ranks' );
		if ( false !== $rank_data ) {
			return $rank_data;
		}
		global $wpdb;
		$rank_data = $wpdb->get_row(
			$wpdb->prepare(
				"
					SELECT id, name, type, rank_group, blog_id, site_id
					FROM {$wpdb->wordpoints_ranks}
					WHERE id = %d
				"
				, $id
			)
		);
		if ( null === $rank_data ) {
			return false;
		}
		wp_cache_add( $rank_data->id, $rank_data, 'wordpoints_ranks' );
		return $rank_data;
	}
}

 Note: Data from user or cache cannot be trusted and properly validate before passing to function or database:

Refer: http://php.net/manual/en/filter.filters.sanitize.php
Command Injection : https://www.owasp.org/index.php/Command_Injection
PHP SQL Injection: http://php.net/manual/en/security.database.sql-injection.php

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

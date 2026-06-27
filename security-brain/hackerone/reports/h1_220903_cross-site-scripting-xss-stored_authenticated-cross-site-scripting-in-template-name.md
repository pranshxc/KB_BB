---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220903'
original_report_id: '220903'
title: Authenticated Cross-site Scripting in Template Name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2017-04-14T02:10:04.808Z'
disclosed_at: '2017-11-18T15:26:23.050Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Authenticated Cross-site Scripting in Template Name

## Metadata

- HackerOne Report ID: 220903
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2017-11-18T15:26:23.050Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Explanation
During my research on latest WordPress I found that `$file_description`  and `$description` from `wp-admin/theme-editor.php`  are not filtering name of the template allowing attacker to do XSS attack.

```
...
		$file_description = get_file_description( $filename );

		if ( $filename !== basename( $absolute_filename ) || $file_description !== $filename ) {
			$file_description .= '<br /><span class="nonessential">(' . $filename . ')</span>';

		}

		if ( $absolute_filename === $file ) {
			$file_description = '<span class="highlight">' . $file_description . '</span>';

		}

		$previous_file_type = $file_type;
?>
		<li><a href="theme-editor.php?file=<?php echo urlencode( $filename ) ?>&amp;theme=<?php echo urlencode( $stylesheet ) ?>"><?php echo $file_description; ?></a></li>
<?php
	endforeach;
?>
```
From this code we can see that `$file_description = get_file_description( $filename );` is getting declared and later on under <li><a> tags template name is printed on the page `...<?php echo $file_description; ?></a></li>`

`$file_description` variable should be filtered before displayed to the user. For example using `htmlspecialchars()` function (example:  F175759 )

However, if victim click on the file that contain XSS payload, XSS will be executed because `$description = get_file_description( $relative_file );` is displaying name of the active file you are editing.

###Steps to replicate
1. Go to Appearance > Editor
2. Select file you want to edit (don't select files that already have name - Archives, Theme Footer for example). I used "back-compat.php" F175758
3. At the very top of the file add following comment:
```/* Template Name: <script>confirm(document.cookie);</script> */``` Like this: F175758
4. Click on Update File.
5. XSS Popup will be prompted. F175757

###Technology used: 
Google Chrome 57.0.2987.133 (64-bit) - Latest

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

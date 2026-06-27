---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1765631'
original_report_id: '1765631'
title: Potential directory traversal in OC\Files\Node\Folder::getFullPath
weakness: 'Path Traversal: ''dir\..\..\filename'''
team_handle: nextcloud
created_at: '2022-11-08T06:56:54.544Z'
disclosed_at: '2023-05-04T07:59:49.938Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal-dir-filename
---

# Potential directory traversal in OC\Files\Node\Folder::getFullPath

## Metadata

- HackerOne Report ID: 1765631
- Weakness: Path Traversal: 'dir\..\..\filename'
- Program: nextcloud
- Disclosed At: 2023-05-04T07:59:49.938Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/nextcloud/server/blob/67551f379f3105d117b9d19095dd381450fe40dd/lib/private/Files/Node/Folder.php#L68-L73
is validating and normalizing the string in the wrong order.

Validation checks for `/../` kind of situations and `normalizePath` later on replaces `\` with `/`, so it would be possible to get `/../` again.

```php
	public function getFullPath($path) {
		if (!$this->isValidPath($path)) {
			throw new NotPermittedException('Invalid path');
		}
		return $this->path . $this->normalizePath($path);
	}
```

## Impact

The function seems to be used in newFile() and newFolder() items, allowing to create paths outside of ones own space and overwriting stuff from others.

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

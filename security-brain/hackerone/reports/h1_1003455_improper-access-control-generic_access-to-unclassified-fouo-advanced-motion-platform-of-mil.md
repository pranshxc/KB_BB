---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1003455'
original_report_id: '1003455'
title: Access to Unclassified / FOUO Advanced Motion Platform of █████████.mil
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-10-09T13:06:22.504Z'
disclosed_at: '2020-11-02T21:43:09.710Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-access-control-generic
---

# Access to Unclassified / FOUO Advanced Motion Platform of █████████.mil

## Metadata

- HackerOne Report ID: 1003455
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2020-11-02T21:43:09.710Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,
I have recently found a website in the namespace of the Amazon Web Services cloud for the US government which exposes a classification header of Unclassified / FOUO. Hence, I thought it might be a good idea to report this vulnerability to you.
Furthermore, the source code tells us that the website seems to be part of ████████.mil even though the SSL name is "███████":
```html

	<script type="text/javascript">
		// use one of these ██████████ URLs depending on the install environment
		var ███████_URL = "https://████████.██████████.mil/";
//		var █████_URL = "https://████.█████████.smil.mil/";
	</script>
```

The proof of concept is as simple as opening the link `https://███/`.
For reference, I have found the site via Shodan: https://www.shodan.io/host/█████████

██████████
███
█████

## Impact

This system is classified as Unclassified / FOUO. Hence, an attacker can access a system which is only for official use only.

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

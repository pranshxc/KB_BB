---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111386'
original_report_id: '111386'
title: Legacy API exposes private video titles
weakness: Information Disclosure
team_handle: vimeo
created_at: '2016-01-18T10:06:58.186Z'
disclosed_at: '2016-02-10T20:14:32.101Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- information-disclosure
---

# Legacy API exposes private video titles

## Metadata

- HackerOne Report ID: 111386
- Weakness: Information Disclosure
- Program: vimeo
- Disclosed At: 2016-02-10T20:14:32.101Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I have discovered Vimeo's legacy API (`vimeo.com/api`) exposes private video titles.

Example URL: https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/152133387

Vimeo provides the uploader with 5 privacy options for viewing videos:

1. Anyone
2. Only me
3. Only people I follow
4. Only people I choose
5. Only people with a password

While "Only me" is selected the above URL will return `404 Not Found`. If any of the last three options are selected, the server will respond with:

```
{"type":"video","version":"1.0","provider_name":"Vimeo","provider_url":"https:\/\/vimeo.com\/","html":"<iframe src=\"https:\/\/player.vimeo.com\/video\/152133387\" width=\"352\" height=\"288\" frameborder=\"0\" title=\"My secret video\" webkitallowfullscreen mozallowfullscreen allowfullscreen><\/iframe>","width":352,"height":288,"video_id":152133387,"uri":"\/videos\/152133387"}
```

As you can see, this includes the title "My secret video". Given a URL of a private video, an attacker can view the title of the video which may in turn reveal the contents of the video. As video IDs increment one-by-one, it would be very easy to discover the titles of thousands of private videos by checking the response of the video page against the response of the API.

-Nathan

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

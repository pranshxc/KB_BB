---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '541862'
original_report_id: '541862'
title: Open redirect protection (https://www.pixiv.net/jump.php) is broken for novels
weakness: Open Redirect
team_handle: pixiv
created_at: '2019-04-18T08:43:04.308Z'
disclosed_at: '2019-10-01T08:41:50.990Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: www.pixiv.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect protection (https://www.pixiv.net/jump.php) is broken for novels

## Metadata

- HackerOne Report ID: 541862
- Weakness: Open Redirect
- Program: pixiv
- Disclosed At: 2019-10-01T08:41:50.990Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

I found that pixiv has a open redirect protection, any external link in illustration is converted to `https://www.pixiv.net/jump.php?<link provided by user>`. For example `https://i3mx4usociis8twimpcu2ty0erkh86.burpcollaborator.net/abc` in `https://www.pixiv.net/member_illust.php?mode=medium&illust_id=74148892` is converted to `https://www.pixiv.net/jump.php?https%3A%2F%2Fi3mx4usociis8twimpcu2ty0erkh86.burpcollaborator.net%2Fabc`. See the attachment "illust.png".

However, that is not true for novels. Links in novel is shown to be converted to `jump.php` link in preview (see attachment "preview.png") but they actually aren't. See `https://www.pixiv.net/novel/show.php?id=109971051` and "novel.png" for an example. 

Since the "jump.php" protection mechanism is working for illusts and the preview of novels, I think lacking this protection for novels is not an intended behavior.

## Steps To Reproduce:

  1. Add a novel
  2. Choose "Add URL" and edit the content to something like `[[jumpuri:https://pixiv.net/ > https://i3mx4usociis8twimpcu2ty0erkh86.burpcollaborator.net/abc]]`
  3. Save
  4. You will see a link in the novel which reads `https://pixiv.net/` but actually it is `https://i3mx4usociis8twimpcu2ty0erkh86.burpcollaborator.net/abc`. See `https://www.pixiv.net/novel/show.php?id=10997105` for your reference.

## Impact

Faking users to the wrong site

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

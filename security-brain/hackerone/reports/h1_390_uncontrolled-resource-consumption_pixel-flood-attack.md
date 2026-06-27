---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390'
original_report_id: '390'
title: Pixel flood attack
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2013-11-12T16:04:27.096Z'
disclosed_at: '2013-11-30T12:50:43.920Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Pixel flood attack

## Metadata

- HackerOne Report ID: 390
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2013-11-30T12:50:43.920Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey guys,

I just found a way to make your service timeout. I didn't know if I should put this under the Internet section of just the HackerOne section, because the exploit also crashes my Windows Image Viewer. A lot of other services should be vulnerable as well.

For the sake of responsible disclosure I haven't made an article about this yet. But if you fix this problem I would like to publish this for my ego, and because of the maximum giggles I experienced after finding this.

The exploit is really simple. I have an image of 5kb, 260x260 pixels. In the image itself I exchange the 260x260 values with 0xfafa x 0xfafa (so 64250x64250 pixels). Now from what I remember your service tries to convert the image once uploaded. By loading the 'whole image' into memory, it tries to allocate 4128062500 pixels into memory, flooding the memory and causing DoS. This also happens with Windows Photo Viewer on my computer.

As attachments I sent three foto's of your service timing out (had to be sure it was my image), and the image with the 'spoofed' pixels.

As a patch I would just set a maximum amount of pixels an image can have.

With kind regards,

Sipke (Graa)

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

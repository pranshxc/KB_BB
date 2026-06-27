---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1887917'
original_report_id: '1887917'
title: XSS from Mastodon embeds
weakness: Cross-site Scripting (XSS) - Generic
team_handle: irccloud
created_at: '2023-02-27T01:14:23.334Z'
disclosed_at: '2023-10-09T04:00:23.621Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
asset_identifier: irccloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS from Mastodon embeds

## Metadata

- HackerOne Report ID: 1887917
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: irccloud
- Disclosed At: 2023-10-09T04:00:23.621Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

By default, the IRCCloud web client embeds Mastodon toots when a link to one is sent. Anyone can run a Mastodon server, and so the server from which toot data is fetched might be malicious. It is possible for an attacker to cause a web client user to execute arbitrary JavaScript in the context of the IRCCloud web client by tricking the web client into embedding a `javascript:` URL.

**POC**:
1. Ensure "Embed social media links" is enabled in settings under "Chat & embeds" (I think this is on by default)
2. Send a message with a link to https://sm4.ca/@a/123456789012345678 (the link itself 404s but IRCCloud only tries to use Mastodon API so it doesn't matter)
3. Wait a few seconds for the embed to load
4. Look at your session cookie

When the web client sees what looks like a toot URL, it tries to get canonical toot URL by making a query to `[domain]/api/v1/statuses/[toot ID]`. Here is what I serve at `https://sm4.ca/api/v1/statuses/123456789012345678`:

```json
{
  "account": {
    "url": "https://sm4.ca/@a"
  },
  "url": "javascript:top.document.body.innerHTML = \"hi your cookie is \" + document.cookie;//"
}
```

(`.account.url` is only present because the web client ensures it matches the original link)

The web client creates an `iframe` using `.url` as the src, which in this case is a `javascript:` URL. The specified script runs in a seperate document that has access to its parent, and can access anything the parent can. The `//` is needed at the end since the web client appends `/embed` to the embed URL.

(also apart from this particular issue, I don't think Mastodon embeds should be enabled unless "Embed 3rd party image and video links" is enabled since even when the Mastodon server isn't malicious your IP address is still leaked to an arbitrary server)

## Impact

An attacker who can send a message to an web-client-using IRCCloud user can obtain their session token and act as them. By sending a message with a malicious URL to a large channel an attacker could compromise many users at once.

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

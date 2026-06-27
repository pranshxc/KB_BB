---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '530881'
original_report_id: '530881'
title: Hidden Stored XSS in nested post embeds
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2019-04-08T00:34:59.462Z'
disclosed_at: '2019-07-17T20:13:59.635Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Hidden Stored XSS in nested post embeds

## Metadata

- HackerOne Report ID: 530881
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2019-07-17T20:13:59.635Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Comments can be crafted in a way that when quoted will trigger a hidden stored XSS payload. Requires initial user interaction*.

**Description:**
When quoting a comment, an attacker can edit the `insert > embed-external > data > url` field to contain a string which when parsed, can result in the injection of html elements. Including iframes which can be used to execute malicious Javascript code.

* Requires partial user interaction. However, if the user who quotes the malicious comment posts it, it then does not require any further users to interact and will trigger on page load.

This code gets executed when the attackers post gets `quote`d, it will first trigger within the "quoters" `richEditor` and if the user posts the quote it will create a post containing the contents of the payload, which will trigger for any users who view that page.

Apologies for the bad description, this video might clear it up a bit - note how when the post is quoted it does not look like how it should.
#F464202

## Steps to reproduce:

1. Ensure you are logged into an account (does not need any special permissions)
2.  View any discussion (forum post)
3. `Quote` any existing comment (or the main post itself)
4. Click `Post Comment` and intercept the request in a tool such as BurpSuite
5. Edit the `Body` parameter so that the first `url` key is the following:
```
"url":"\"></a>this is not the body of the quoted post?<iframe src=javascript:alert(1) style=\"display:none",
```
6. Forward the request
7. Notice that the payload has not triggered yet
8. Quote the new comment (your one)
9. XSS should now trigger when it has embedded in the `richEditor`
10. Click `Post Comment`
11. A new comment should now be posted containing the payload which will trigger on page load

## Anything else we should know?
When scraping the quoted post in the `richEditor` the request looks like the following:
#F464209
As can be seen it gathers the data to use for the `api/v2/rich/quote` call later on and the malicious `url` can be seen, when this is ran through the quote api call this returns:
#F464210

Here we can see that it injects the attackers iframe containing the Javascript.
If the victim posts a response containing the malicious quote we can see that it is rendered into the html
#F464211

Obviously in this example the payload is an alert and would be noticable to the victim. However more subtle payloads can be placed inside the url that users would not notice.

The only important part of the `url` is that it must start with `\"></a>` to escape the href the url is meant to be inserted into. Anything placed after that will be rendered directly within the page.

This may have a similar root issue to #530853

## Impact

An attacker could trick users into posting content containing their malicious payload. An attacker could create a response intended to receive a lot of quotes, perhaps a controversial one only posted to incite other users to quote him.

The resulting comments quoting the attackers post will place payloads into the discussion thread and if detected would not point to the attacker but instead would point to the users who quoted them.

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

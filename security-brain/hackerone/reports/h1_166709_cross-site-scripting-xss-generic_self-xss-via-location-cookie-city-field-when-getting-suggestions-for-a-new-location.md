---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166709'
original_report_id: '166709'
title: Self-XSS via location cookie city field when getting suggestions for a new
  location
weakness: Cross-site Scripting (XSS) - Generic
team_handle: yelp
created_at: '2016-09-07T23:47:48.707Z'
disclosed_at: '2016-11-30T19:13:19.660Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self-XSS via location cookie city field when getting suggestions for a new location

## Metadata

- HackerOne Report ID: 166709
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: yelp
- Disclosed At: 2016-11-30T19:13:19.660Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

Hi,

Only self-XSS, but thought I would report it anyway!

I noticed the cookie "location" had some JSON in it, so I changed the city field to `<script>debugger</script>`, made sure it was encoded the same, then went to add a new location/change an existing location at https://www.yelp.com/profile_location. Making sure the debugger is open, and then clicking on the Address field on the new location page, the debugger should open up as the XSS fires.

My cookie before tampering was: `%7B%22city%22%3A+%22San+Francisco%22%2C+%22zip%22%3A+%22%22%2C+%22country%22%3A+%22US%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+%22%22%2C+%22state%22%3A+%22CA%22%2C+%22address1%22%3A+%22%22%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%7D`

I changed it to be `%7B%22city%22%3A%22%3Cscript%3Edebugger%3C/script%3E%22%2C%22zip%22%3A%22%22%2C%22country%22%3A%22US%22%2C%22address2%22%3A%22%22%2C%22address3%22%3A%22%22%2C%22state%22%3A%22CA%22%2C%22address1%22%3A%22%22%2C%22unformatted%22%3A%22SanFrancisco%2CCA%22%7D`

What I see on chrome is attached.

The data is getting there from the request to `https://www.yelp.com/location_suggest/json?prefix=`, with our cookie, and all other auth related cookies. The response is `{"suggestions": [{"suggestion_type": "location", "content_id": null, "name": "\u003cscript\u003edebugger\u003c/script\u003e, CA", "alias": null}, {"suggestion_type": "location", "content_id": null, "name": "Schenectady, NY", "alias": null}, {"suggestion_type": "location", "content_id": null, "name": "5488 SW Alger Ave, Beaverton, OR", "alias": null}], "unique_request_id": "8d056ce4b81b2693"}` (the other two addresses being random test addresses I guess).

My suggestion would be to validate the city name passed in the cookie as an actual city.

Let me know if you need more info.

Cheers,

Hugh

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

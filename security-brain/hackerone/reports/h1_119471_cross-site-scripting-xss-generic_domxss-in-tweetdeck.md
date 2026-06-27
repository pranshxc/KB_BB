---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119471'
original_report_id: '119471'
title: DOMXSS in Tweetdeck
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2016-02-29T15:15:46.940Z'
disclosed_at: '2017-04-02T16:32:42.040Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOMXSS in Tweetdeck

## Metadata

- HackerOne Report ID: 119471
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2017-04-02T16:32:42.040Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report a DOMXSS issue in TweetDeck.

#Details
In Tweetdeck, a tweet contains info of what client (app) the user used to sent the tweet. The render process is vulnerable to DOMXSS.

In https://ton.twimg.com/tweetdeck-web/web/dist/bundle.6f91b4e832.js, the following line is responsible for retrieving the client website:

```javascript
                case "followSourceLink":
                    TD.util.openURL($(n.getMainTweet().source).attr("href"));
                    break;
```

where ```n.getMainTweet().source``` is the client name. This name can be controlled through changing the application name (picture attached), and arbitrary characters can be inserted (including angle brackets).  Moving on, ```$()``` is a jQuery DOMXSS sink. If we inject a payload like ```<svg onload=alert(document.domain)>``` then XSS will be executed showing the executing domain.

So to sum up,
1. Attacker creates an application where the app name is a XSS payload.
2. Attacker uses the app to post a tweet, then the tweet contains a malicious info of which app the tweet is sent from
3. Victim clicks on the app info and XSS triggers.

#PoC
1. Make sure you are using latest IE (otherwise CSP kicks in)
2. Follow @attackerfoobar or search for the user on TweetDeck
3. Expand the first tweet, click "Click here to get followers ❤️" (which is a bait app name)
4. XSS executes

Video demonstration is also attached.

#Fix
Probably sanitize ```n.getMainTweet().source``` before putting it into ```$()```.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '26962'
original_report_id: '26962'
title: open redirect in rfc6749
weakness: Open Redirect
team_handle: ibb
created_at: '2014-09-04T19:15:25.612Z'
disclosed_at: '2015-04-06T17:40:18.093Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- open-redirect
---

# open redirect in rfc6749

## Metadata

- HackerOne Report ID: 26962
- Weakness: Open Redirect
- Program: ibb
- Disclosed At: 2015-04-06T17:40:18.093Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

OAuth Providers (servers) that strictly follow rfc6749 are vulnerable to open redirect.
Let me explain, reading [0]

If the request fails due to a missing, invalid, or mismatching
   redirection URI, or if the client identifier is missing or invalid,
   the authorization server SHOULD inform the resource owner of the
   error and MUST NOT automatically redirect the user-agent to the
   invalid redirection URI.

   If the resource owner denies the access request or if the request
   fails for reasons other than a missing or invalid redirection URI,
   the authorization server informs the client by adding the following
   parameters to the query component of the redirection URI using the
   "application/x-www-form-urlencoded" format, per Appendix B:

Now let’s assume this.
I am registering a new client to the victim.com provider. 
I register redirect uri attacker.com.

According to [0] if I pass e.g. the wrong scope I am redirected back to attacker.com.
Namely I prepare a url that is in this form:

http://victim.com/authorize?response_type=code&client_id=bc88FitX1298KPj2WS259BBMa9_KCfL3&scope=WRONG_SCOPE&redirect_uri=http://attacker.com

and this is works as an open redirector.
Of course in the positive case if all the parameters are fine this doesn’t apply since the resource owner MUST approve the app via the consent screen (at least once).

I have notified also this issue to the OAuth mailing list.

See also http://www.ietf.org/mail-archive/web/oauth/current/msg13367.html
and http://www.ietf.org/mail-archive/web/oauth/current/maillist.html.
The consensus seems to be that some of the OAuth family spec should be updated... (currently under discussion)

A solution would be to return error 400 rather than redirect to the redirect URI or always show the consent screen (at least once until the app is accepted by the user) even in case of wrong parameter rather than redirect...

[0] https://tools.ietf.org/html/rfc6749#section-4.1.2.1

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

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-16_forced-sso-session-fixation.md
original_filename: 2024-08-16_forced-sso-session-fixation.md
title: Forced SSO Session Fixation
category: documents
detected_topics:
- sso
- oauth
- rate-limit
- csrf
- access-control
- command-injection
tags:
- imported
- documents
- sso
- oauth
- rate-limit
- csrf
- access-control
- command-injection
language: en
raw_sha256: bbf26c13c68d624abfa3be30ace64d459331b97f70bd5242aa310be3e51a2461
text_sha256: 015926591fb2c9596141a374f98912eebc7c03ba6c7ee07621c234714067eb41
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Forced SSO Session Fixation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-16_forced-sso-session-fixation.md
- Source Type: markdown
- Detected Topics: sso, oauth, rate-limit, csrf, access-control, command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `bbf26c13c68d624abfa3be30ace64d459331b97f70bd5242aa310be3e51a2461`
- Text SHA256: `015926591fb2c9596141a374f98912eebc7c03ba6c7ee07621c234714067eb41`


## Content

---
title: "Forced SSO Session Fixation"
url: "https://infosecwriteups.com/forced-sso-session-fixation-5d3b457b79cb"
authors: ["Serj Novoselov (@novoselov_s)"]
bugs: ["SSO", "Session fixation", "Account takeover"]
publication_date: "2024-08-16"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 66
scraped_via: "browseros"
---

# Forced SSO Session Fixation

Forced SSO Session Fixation
Serj Novoselov
Follow
3 min read
·
Aug 16, 2024

77

During a recent project, I encountered an interesting small issue that allowed for a one-click account takeover by fixating a session identifier and forcing a victim’s browser to initiate the first steps of a Single Sign-On (SSO) flow. This vulnerability was possible due to the absence of anti-CSRF token verification.

Press enter or click to view image in full size
The Login Page

The login page exhibited the “Log in with SSO” feature:

Press enter or click to view image in full size
Investigating the SSO Flow

Upon investigating the SSO flow, I discovered the following sequence of steps:

Initiation of SSO process by clicking the button:
GET request to /idp/auth/mid-oidc?req=[UNIQUE_ID]&redirect_uri=[REDIRECT_URI]
SSO Service Provider process
Multiple requests made on the service provider domain, akin to signing in with Google where requests are sent to google.com. If the user was previously signed in, actions are performed automatically.
Hitting callback URL
After authorization on the Service Provider side, a request to a callback URL is made:
GET /idp/callback?code=[STUFF]&state=[STUFF].
However, this is not a last step, that returns the session token, one more additonal step was required.
Issue a session token
Request to get the session token.
GET /idp/approval?req=[UNIQUE_ID]
The UNIQUE_ID value is the same as was on the first step. This means, that if you know this value, you could hit this method and get a session. As no anti-csrf protection was present, so it was possible to perform a session fixation.
Press enter or click to view image in full size
Exploitation Scenario

An “Attacker” opens the environment URL on their machine and extracts the “Log in with SSO” button link:

Press enter or click to view image in full size

From the copied link, the attacker extracts the “req” parameter and starts the self-written exploit:

Press enter or click to view image in full size
Press enter or click to view image in full size

The attacker then sends the link containing the “req” parameter to the “Victim”.

Get Serj Novoselov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Upon opening the link in the browser, the “Victim” encounters an error message:

Press enter or click to view image in full size
How does the exploit work?

The malicious script executed by the attacker utilizes 10 threads to make multiple requests to the /idp/approval?req={req}.

Initially, the server responses to these requests are 500 errors. However, when the victim initiates the SSO flow, but before handling the request to the “approval” URL, all subsequent requests to the mentioned endpoint return a valid link with a session token.

As a result of the exploit, the “Attacker” obtains the session URL and can complete the login flow, effectively logging in as the “Victim”:

Press enter or click to view image in full size

By directly visiting the returned URL, the attacker finishes the login flow and logs in as “Victim”.

Remediation

The issue remediation can be done by:

Implementing Anti-CSRF Protection.
Validating Session Identifier at each step of the SSO process to prevent fixation.
Applying rate limiting on the /idp/approval endpoint to prevent rapid and unauthorized requests for session tokens.

🌐 My social networks: https://linktr.ee/s_novoselov

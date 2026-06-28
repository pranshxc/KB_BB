---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-07_xss-in-zoomus-signup-flow.md
original_filename: 2020-07-07_xss-in-zoomus-signup-flow.md
title: XSS in Zoom.us Signup Flow
category: documents
detected_topics:
- oauth
- xss
- command-injection
- mfa
- otp
- csrf
tags:
- imported
- documents
- oauth
- xss
- command-injection
- mfa
- otp
- csrf
language: en
raw_sha256: 42a24f0080b12c6dd47346bf17b8f62262c4a68dc5ba9b1f5c65a57c49b28bf3
text_sha256: 0d21b56df22aadcfca7e76baa86dac40c7320acc4b7e178998f9a8c8a571d7bd
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Zoom.us Signup Flow

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-07_xss-in-zoomus-signup-flow.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, mfa, otp, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `42a24f0080b12c6dd47346bf17b8f62262c4a68dc5ba9b1f5c65a57c49b28bf3`
- Text SHA256: `0d21b56df22aadcfca7e76baa86dac40c7320acc4b7e178998f9a8c8a571d7bd`


## Content

---
title: "XSS in Zoom.us Signup Flow"
page_title: "Zoom: XSS in Zoom.us Signup Flow · Advisory · google/security-research · GitHub"
url: "https://github.com/google/security-research/security/advisories/GHSA-fpgp-vrmv-v8f2"
final_url: "https://github.com/google/security-research/security/advisories/GHSA-fpgp-vrmv-v8f2"
authors: ["Eduardo Vela (@sirdarckcat)"]
programs: ["Zoom"]
bugs: ["XSS"]
publication_date: "2020-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4428
---

###  Uh oh! 

There was an error while loading. [Please reload this page]().

[ google ](/google) / **[security-research](/google/security-research) ** Public

  * [ Notifications ](/login?return_to=%2Fgoogle%2Fsecurity-research) You must be signed in to change notification settings
  * [ Fork 556 ](/login?return_to=%2Fgoogle%2Fsecurity-research)
  * [ Star  4.5k ](/login?return_to=%2Fgoogle%2Fsecurity-research)

  * [ Code ](/google/security-research)
  * [ Issues 18 ](/google/security-research/issues)
  * [ Pull requests 70 ](/google/security-research/pulls)
  * [ Actions ](/google/security-research/actions)
  * [ Security and quality 131 ](/google/security-research/security)
  * [ Insights ](/google/security-research/pulse)

Additional navigation options

  * [ Code  ](/google/security-research)
  * [ Issues  ](/google/security-research/issues)
  * [ Pull requests  ](/google/security-research/pulls)
  * [ Actions  ](/google/security-research/actions)
  * [ Security and quality  ](/google/security-research/security)
  * [ Insights  ](/google/security-research/pulse)

  1. [security-research](/google/security-research)
  2. [Security](/google/security-research/security)
  3. [Advisories](/google/security-research/security/advisories)
  4. [GHSA-fpgp-vrmv-v8f2](/google/security-research/security/advisories/GHSA-fpgp-vrmv-v8f2)

#  Zoom: XSS in Zoom.us Signup Flow 

High 

[sirdarckcat](/sirdarckcat) published GHSA-fpgp-vrmv-v8f2 Jul 7, 2020

## Package

zoom.us

## Affected versions

<2020.04.08

## Patched versions

2020.07.07

## Description

## Summary

Zoom.us did not sanitize the name of the user on the federated signup flow. This allowed an attacker to execute arbitrary JavaScript on a victim's browser in the context of <https://zoom.us/> when opening a malicious link.

## Severity

Calculated as **High** by Google ([source](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:L/E:P/RL:O/RC:C)). The attacker needs to convince a victim to visit a malicious link, then the exploit can log the victim back in as the real user, and gain access to the victim's Zoom.us account. This could allow an attacker to do anything the victim can do through the website.

## Proof of Concept

The victim had to visit a URL of the form: `https://zoom.us/signin/term?token=...&type=2`.

In order to construct such a URL, the attacker had to:

  1. Visit the following URL while being logged-in with the attacker's account (the attacker's account needs to have the xss payload on its name): `https://accounts.google.com/o/oauth2/v2/auth?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth`
  2. That URL would then redirect to: `https://zoom.us/google/oauth?state=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&code=..CODE..`
  3. That URL would then redirect to `https://zoom.us/signin/term?token=...TOKEN..&type=2`

The last URL in step (3) could then be sent to unsuspecting victims, which would then trigger the XSS.

## Additional Analysis

### OAuth flow

Usually an attack like this would be prevented by a CSRF token in the state parameter of the OAuth web flow, but Zoom.us did not contain any unpredictable tokens, so exploitation was straightforward.

### User interaction

If the victim was an active Zoom.us user, then the attack required no user interaction. If the victim was not an active Zoom user, then the victim had to pass the "age check" before the XSS could trigger.

[![Screenshot 2020-07-10 at 09 23 33](https://user-images.githubusercontent.com/33089/87127925-1106ed80-c28f-11ea-8c42-cab03d4dc674.png)](https://user-images.githubusercontent.com/33089/87127925-1106ed80-c28f-11ea-8c42-cab03d4dc674.png)

### XSS payload in name

To put a payload in a Google account name an attacker can use a [service account](https://developers.google.com/identity/protocols/oauth2/service-account), a premium GSuite account through an API, or a legacy GMail account.

The proof of concept provided to Zoom used GSuite.  
[![Screenshot 2020-04-08 at 09 50 48](https://user-images.githubusercontent.com/33089/86800154-02dc8580-c073-11ea-8651-0a7a90bd08ca.png)](https://user-images.githubusercontent.com/33089/86800154-02dc8580-c073-11ea-8651-0a7a90bd08ca.png)

[@totallyunknown](https://github.com/totallyunknown) provided a screenshot with a legacy GMail account.  
[![xss payload screenshot](https://user-images.githubusercontent.com/33089/86798853-8bf2bd00-c071-11ea-9498-e9d186aa2e79.png)](https://user-images.githubusercontent.com/33089/86798853-8bf2bd00-c071-11ea-9498-e9d186aa2e79.png)

### Severity

High 

### CVE ID

No known CVE 

### Weaknesses

No CWEs

### Credits

  * [![@totallyunknown](https://avatars.githubusercontent.com/u/1724494?s=40&v=4)](/totallyunknown) [ totallyunknown](/totallyunknown) Analyst
  * [![@sirdarckcat](https://avatars.githubusercontent.com/u/33089?s=40&v=4)](/sirdarckcat) [ sirdarckcat](/sirdarckcat) Analyst

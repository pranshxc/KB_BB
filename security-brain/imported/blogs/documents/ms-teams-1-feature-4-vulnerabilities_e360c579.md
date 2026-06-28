---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-22_ms-teams-1-feature-4-vulnerabilities.md
original_filename: 2021-12-22_ms-teams-1-feature-4-vulnerabilities.md
title: 'MS Teams: 1 feature, 4 vulnerabilities'
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: e360c5795854cd849f48eea3a53d17520313eb181d6eeb1538512ec44ab9e37a
text_sha256: 7b6f2339c0248074a17bd432e0dc79581c1fe6754cc56ca017b31177b2c868ba
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# MS Teams: 1 feature, 4 vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-22_ms-teams-1-feature-4-vulnerabilities.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `e360c5795854cd849f48eea3a53d17520313eb181d6eeb1538512ec44ab9e37a`
- Text SHA256: `7b6f2339c0248074a17bd432e0dc79581c1fe6754cc56ca017b31177b2c868ba`


## Content

---
title: "MS Teams: 1 feature, 4 vulnerabilities"
page_title: "MS Teams: 1 feature, 4 vulnerabilities | Positive Security"
url: "https://positive.security/blog/ms-teams-1-feature-4-vulns"
final_url: "https://positive.security/blog/ms-teams-1-feature-4-vulns"
authors: ["Fabian Bräunlein"]
programs: ["Microsoft"]
bugs: ["SSRF", "Information disclosure", "DoS", "Spoofing"]
publication_date: "2021-12-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3067
---

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436cf0ef16e7ad_menu_icon_flipped.png)

[HOME](/)[About](/about)[Services](/services)[Blog](/blog)[Contact](/contact)

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c270016e798_purple.png)](/)

# MS Teams: 1 feature, 4 vulnerabilities

December 22, 2021

By 

[Fabian Bräunlein](mailto:fabian@positive.security)

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61c0a17ed776749890e08573_msteams-preview.png)

# TL;DR:

  * We stumbled upon 4 vulnerabilities in Microsoft Team's link preview feature
  * The vulnerabilities allow accessing internal Microsoft services, spoofing the link preview, and, for Android users, leaking their IP address and DoS'ing their Teams app/channels
  * We reported the issues to Microsoft in March 2021, who has only remediated one so far

\-- MARKDOWN --

# ToC

\- [Motivation](#motivation)  
\- [1 - Server-Side Request Forgery](#1-ssrf)  
\- [2 - URL preview spoofing](#2-spoofing)  
\- [3 - IP address leak](#3-ip-address-leak-android)  
\- [4 - Message of Death (DoS)](#4-denial-of-service-aka-message-of-death-android)  
\- [Disclosure](#disclsoure)  
\- [Conclusion](#conclusion)

# Motivation

While investigating [[the Windows 10 RCE we recently published](https://positive.security/blog/ms-officecmd-rce)](https://positive.security/blog/ms-officecmd-rce), we were [[at one point](https://positive.security/blog/ms-officecmd-rce#teams-code-execution-via---inspect-debugger-and-mitm-with-sop-bypass)](https://positive.security/blog/ms-officecmd-rce#teams-code-execution-via---inspect-debugger-and-mitm-with-sop-bypass) looking for a way to bypass Teams'/Electron's Same-Origin Policy. The idea was to escalate from JavaScript to arbitrary code execution by sending commands to a locally started Node.js debug websocket server. For a successful connection to that server, a UUID is required that is printed during application start and provided by an HTTP server running on the same websocket port.

One potential way to bypass the SOP in Teams and fetch the UUID from JavaScript is by abusing the link preview feature:

  1. Let the client generate a link preview for the target page (e.g. <http://127.0.0.1:1234/json/list>)
  2. Use the summary text or perform OCR on the preview image to extract information

In Teams, this preview is actually generated server-side by Microsoft (which is possible due to the lack of E2E encryption), so the feature cannot be abused to leak information from the user's local network (e.g. the Node.js debug server). However, while investigating this feature, I stumbled upon a few unrelated vulnerabilities in its implementation.

# 1 SSRF

****Description:**** While we can't leak information from the _user's_ local network, we could theoretically leak information from _Microsoft_ 's local network. Getting slightly distracted from my original goal, I tested the `/urlp/v1/url/info` endpoint for Server-Side Request Forgery and was quite surprised to see that this obvious attack vector has not been protected against.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61bfe88f4482483c4a4de964_1_all.png)](https://positive.security/#zoom)Fetching link previews for 127.0.0.1:80, 127.0.0.1:8080 and the Azure Metadata service (169.254.169.254)

****Impact:**** The URL is not filtered, leading to a limited SSRF (response time, code, size and open graph data leaked), which can be used for internal portscanning and sending HTTP-based exploits to the discovered web services.

Having a slightly closer look at the link preview, I identified 3 more vulnerabilities:

# 2 Spoofing

****Description:**** The preview link target can be set to any location independent of the main link, preview image and description, the displayed hostname or onhover text.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61bfce55d742df076da1e92e_2_Spoofing.png)](https://positive.security/#zoom)Changing the actual target URI while keeping the preview data

Fully spoofing the link target

****Impact:**** When clicking the preview, a different link is opened than what was expected by the user. This can be used either for improved phishing attacks, or to hide malicious links.

****Additional notes:**** ‍

\- Earlier this year, we discovered a [critical vulnerability in WinSCP](https://positive.security/blog/url-open-rce#bonus-vulnerability-winscp) (CVE-2021-3331, fixed in v5.17.10), which can be triggered with the allowed `ftps://` URI scheme. Since there is no `ftps://` default handler in Windows, it's a bit surprising that this scheme is explicitly allowed in Teams and it might be a good idea for its developers to remove it from the internal `allowedHrefProtocols`-list for further hardening  
\- The displayed hostname is updated to the current link target when Teams is restarted or the channel reloaded. During a live conversation, the hostname can be spoofed by editing an already sent link to point to a different (spoofed) target  
\- The displayed hostname's TLD is truncated in the desktop/web client, providing additional spoofing possibilities

# 3 IP Address Leak (Android)

****Description:**** When creating a link preview, the backend fetches the referenced preview thumbnail and makes it available from a Microsoft domain. This ensures that the IP address and user agent data is not leaked when the receiving client loads the thumbnail. However, by intercepting the sending of the message, it's possible to point the thumbnail URL to a non-Microsoft domain. The Android client does not check the domain/does not have a CSP restricting the allowed domains and loads the thumbnail image from any domain.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61bfda1004d338dd13c3dab1_3_IP_leak.png)](https://positive.security/#zoom)Changing the original thumbnail URL to reference a picture on our website[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61bfe5b78367b2f73d19545d_3_IP_leak_3.png)](https://positive.security/#zoom)This picture is directly fetched from the referenced website when the message is opened

****Impact:**** Allows leaking an user's IP address and user agent data by sending a message with a specially crafted link preview (for Teams users on Android).

**Note:** This issue seems patched now. See the [disclosure section](#disclosure) below.

# 4 Denial of Service aka Message of Death (Android)

****Description:**** When receiving a message that includes a link preview with an invalid preview link target (e.g. "boom" instead of "https://..."), the Android app crashes. The app keeps crashing when trying to open the chat/channel with the malicious message, which makes the chat/channel unusable for Android users.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/61bfd9eec26837fb021ec227_4_Android_DoS.png)](https://positive.security/#zoom)

MS Team crashes on opening a channel containing the malicious message (don't mind the two channels with the same name)

****Impact:**** Allows DoS'ing users and channels with a single message (for Teams users on Android).

# Disclosure

All four issues have been reported to Microsoft on March 10, 2021 via the MSRC program.

Only the Android IP address leak has seemingly been patched.

`2021-03-10`: We report the issues to Microsoft  
`2021-03-12` - `2021-03-25`: Back-and-forth on details of the spoofing issue  
`2021-03-25`: MS closes the DoS ticket without a patch:

> Thank you again for submitting this issue to Microsoft. We determined that this issue does not require immediate security service and we assessed this as low severity for temporary DoS that requires restart of application. A fix for this issue will be considered in a future version of this product or service. At this time, we will not be providing ongoing updates of the status of the fix for this issue, and we have closed this case.

`2021-03-25`: MS closes the SSRF ticket without a patch:

> Microsoft has decided that it will not be fixing this vulnerability in the current version and we are closing this case. At this time, you are able to blog about/discuss this case and/or present your findings publicly about the current version.

`2021-04-04`: MS closes the IP address leak ticket without a patch:

> MSRC has investigated this issue and concluded that this does not pose an immediate threat that requires urgent attention due to the general data sensitivity of the IP address data. We have shared the report with the team responsible for maintaining the product or service. They will review for a potential fix and take appropriate action as needed to help keep customers protected.

`2021-04-14`: MS closes the URL preview spoofing ticket without a patch:

> MSRC has investigated this issue and concluded that this does not pose an immediate threat that requires urgent attention because once the user clicks on the URL, they would have to go to that malicious URL which would be a giveaway that it's not the one the user was expecting.

`2021-12-15`: We retest all issues; only the IP address leak seems patched  
`2021-12-22`: We are publishing this blog post

# Conclusion

While the discovered vulnerabilities have a limited impact, it's surprising both that such simple attack vectors have seemingly not been tested for before, and that Microsoft does not have the willingness or resources to protect their users from them.

##### Follow us on Mastodon ([@positive_sec](https://infosec.exchange/@positive_sec)) to keep up to date with our posts.

‍

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f7ddb13deeceb266b162f8d_favicon-32x32_white.png)© 2025 Positive Security](/)[Legal disclosure](/contact#legal)

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c6cbd16e799_top.png)![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c36af16e7a5_bottom.png)

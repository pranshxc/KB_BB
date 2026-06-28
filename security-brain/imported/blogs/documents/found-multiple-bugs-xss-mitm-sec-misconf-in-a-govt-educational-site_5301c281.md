---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-26_found-multiple-bugs-xss-mitm-sec-misconf-in-a-govt-educational-site.md
original_filename: 2024-04-26_found-multiple-bugs-xss-mitm-sec-misconf-in-a-govt-educational-site.md
title: 'Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site'
category: documents
detected_topics:
- sso
- idor
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- sso
- idor
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 5301c281d0ec5ff6fa7d17d71d82ea73c53739a8999fb7a103046f5d60862621
text_sha256: d0072ae5a37e568bf52b2b5fcbe9fa9563baac3415f2d79433b3c3a5946234aa
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-26_found-multiple-bugs-xss-mitm-sec-misconf-in-a-govt-educational-site.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `5301c281d0ec5ff6fa7d17d71d82ea73c53739a8999fb7a103046f5d60862621`
- Text SHA256: `d0072ae5a37e568bf52b2b5fcbe9fa9563baac3415f2d79433b3c3a5946234aa`


## Content

---
title: "Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site"
url: "https://medium.com/@p.ra.dee.p_0xx01/found-multiple-bugs-xss-mitm-sec-misconf-in-an-educational-site-5a3804085da0"
authors: ["Professor0xx01"]
bugs: ["XSS", "MiTM", "Components with known vulnerabilities"]
publication_date: "2024-04-26"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 318
scraped_via: "browseros"
---

# Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site

Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site
Professor.0xx01
Follow
5 min read
·
Apr 26, 2024

14

Press enter or click to view image in full size

Hello Hackers…….!!!! Hope you all are good.

Intro: I am p_ra_dee_p whom you all know as Professor0xx01. Today I am gonna to explain you my story about finding multiple bugs in an educational (College) Website. So, let’s dive into it.

First Bug :: Cross Site Scripting (Xss)

During the enumeration phrase, i have detected some open “CkeEditor” (webeditor). In this editor, a user can insert and run html codes into the browser according to their need.

Let’s Check how it looks like……

Press enter or click to view image in full size
web-editor

After searching some instances in google, i got a CVE: CVE-2022–24728 defines that it’s vulnerable to XSS & instantly i switched to Burp to get the result.

CVE-2022–24728:

CKEditor4 is an open source what-you-see-is-what-you-get HTML editor. A vulnerability has been discovered in the core HTML processing module and may affect all plugins used by CKEditor 4 prior to version 4.18.0. The vulnerability allows someone to inject malformed HTML bypassing content sanitization, which could result in executing JavaScript code. This problem has been patched in version 4.18.0. There are currently no known workarounds.

After going to Burp……………….

I found that there are multiple Xss vulnerability exists on this ckeditor page…!!!!!! Here I also detected the version of CkeEditor is 4.3.3 which was a Vulnerable Javascript Dependency,,,, confirms the severity is serious.

Press enter or click to view image in full size
Poc
Proof Of Concept :: XSS by Professor0xx01
Xss<!--{cke_protected} --!><img src=x onerror=alert(`Professor0xx01`)> -->Attack
Xss<!--{cke{cke_protected}_protected} --!><img src=x onerror=alert(`Professor0xx01`)> Attack
Press enter or click to view image in full size
POC by Professor0xx01 (p_ra_dee_p)

Note: I have attached only one POC image (unless article will be too long); even though all the CVEs are valid for this “CKEDITOR — 4.3.3” web editor.

Detected CVEs:
CVE - CVE-2021-33829
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

CVE - CVE-2021-32809
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

CVE - CVE-2021-32808
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

CVE - CVE-2021-41164
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

CVE - CVE-2021-41165
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

CVE - CVE-2021-37695
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

Second Issue :: Man-In-The-Middle Attack (MITM-Terrapin Attack)

During Recon, i have also detected that SSH port 22 is open. Here I have noticed the auth-methods & ssh version. But, the more interesting thing is that this SSH protocol is vulnerable to CVE-2023–48795.

CVE-2023–48795

The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, aka a Terrapin attack. This occurs because the SSH Binary Packet Protocol (BPP), implemented by these extensions, mishandles the handshake phase and mishandles use of sequence numbers.

Get Professor.0xx01’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Learn More about …..…….

NVD
Undergoing Reanalysis This vulnerability has been modified and is currently undergoing reanalysis. Please check back…

nvd.nist.gov

CVE - CVE-2023-48795
The mission of the CVE® Program is to identify, define, and catalog publicly disclosed cybersecurity vulnerabilities.

cve.mitre.org

NOTE: I didn’t go further for breaking the integrity of SSH, cause I don’t wish to do anything illegal.

Third Issue: Security Misconfiguration

When i am reviewing the endpoints, i also noticed that there is one another security misconfiguration exists.

The Issue is : If the secure flag is set on a cookie, then browsers will not submit the cookie in any requests that use an unencrypted HTTP connection, thereby preventing the cookie from being trivially intercepted by an attacker monitoring network traffic. If the secure flag is not set, then the cookie will be transmitted in clear-text if the user visits any HTTP URLs within the cookie’s scope. An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain that issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.

Press enter or click to view image in full size
Sec Misconf POC

That’s all for this article nowwww….!!!!

Thanks for reading !! follow me for more insightful writeups !!

See you in the next article !! Bye !!

Happy Hunting~~

Keep Learning & Keep Securing ~~

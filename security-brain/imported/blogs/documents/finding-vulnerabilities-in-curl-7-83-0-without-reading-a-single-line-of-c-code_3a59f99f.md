---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-12_finding-vulnerabilities-in-curl-7830-without-reading-a-single-line-of-c-code.md
original_filename: 2022-06-12_finding-vulnerabilities-in-curl-7830-without-reading-a-single-line-of-c-code.md
title: Finding vulnerabilities in curl 7.83.0 without reading a single-line of C code
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 3a59f99f75ae178a31d25bc02f56419ecb97783313f33086e60891053eb3e48a
text_sha256: 64366a4224cc98e217e66c62b89fda324f4177c76abcec60aa6900ccc1fdb028
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Finding vulnerabilities in curl 7.83.0 without reading a single-line of C code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-12_finding-vulnerabilities-in-curl-7830-without-reading-a-single-line-of-c-code.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `3a59f99f75ae178a31d25bc02f56419ecb97783313f33086e60891053eb3e48a`
- Text SHA256: `64366a4224cc98e217e66c62b89fda324f4177c76abcec60aa6900ccc1fdb028`


## Content

---
title: "Finding vulnerabilities in curl 7.83.0 without reading a single-line of C code"
page_title: "Finding vulnerabilities in curl 7.83.0 without reading a single-line of C code | Vulnerability Research"
url: "https://haxatron.gitbook.io/vulnerability-research/vr2"
final_url: "https://haxatron.gitbook.io/vulnerability-research/vr2"
authors: ["Haxatron (@Haxatron1)"]
programs: ["Internet Bug Bounty (curl)"]
bugs: ["SSRF", "Information disclosure", "HSTS bypass"]
publication_date: "2022-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2563
---

For the complete documentation index, see [llms.txt](https://haxatron.gitbook.io/vulnerability-research/llms.txt). This page is also available as [Markdown](https://haxatron.gitbook.io/vulnerability-research/vr2.md).

Copy

On this page

# Finding vulnerabilities in curl 7.83.0 without reading a single-line of C code

This post details 3 vulnerabilities discovered when digging into curl 7.83.0. They were assigned CVE-2022-27779, CVE-2022-27780 as well as CVE-2022-30115.

### 

Description

curl is a popular command-line tool used by many people around the world to make requests to a server. It also offers a library which developers can use to build applications that communicate with servers. This blog post details the 3 vulnerabilities I found: CVE-2022-27779, CVE-2022-27780 and CVE-2022-30115 and the discovery of it.

### 

Introduction

I have never in my life written a single-line of C code. So approaching curl felt like a daunting task to me. I had always felt that auditing a program like curl would require an immense knowledge of low-level programming.

However, that changed when I reading Hackerone's hacktivity one day and came across this particular report by another user - <https://hackerone.com/reports/1547048>.

The vulnerability in that report itself was simple, when curl was configured to use a Cookie / Authorization header and was told to follow redirects, it could leak the cookie when the redirection occurred from a secure to insecure channel for the same hostname (ie. https-http redirect), or when the redirection target was a different port of the same hostname, effectively violating the Same-Origin-Policy (origin = protocol + hostname + port). This vulnerability itself was with curl's application logic, which means that it had nothing to do with low-level stuff (essentially, not a error to do with C.)

So I started to focus my efforts into curl, with the goal of finding similar application-logic vulnerabilities.

### 

Part 1: CVE-2022-27779: Cookie set for a trailing dot TLD

I started my research into curl's cookie engine. As cookies are essential in authentication, bugs due to mishandling of cookies will most likely turn out to be security issues!

### 

Background

**A Primer on Cookies**

Firstly, it is important to understand how cookies work. HTTP is a stateless protocol, which means that every request sent by the client is considered independent from one another by the server. Cookies are therefore used to give the "state" to the client so that the server can track session information across these various requests.

Cookies work based on the same-site context. A site has a different meaning from the origin, used to be defined as TLD+1 (I'll get to that part later). In a typical domain name such example.com, "com", the shared component before the first dot is known as a TLD. A TLD+1 means everything after "com" and including "com", so "example.com" would be the TLD+1 as "com"

A cookie can be set for TLD+1 and above (ie. TLD+2, TLD+3, TLD+4 and so on). But browsers forbid setting a cookie for TLD. The reason being that it prevents malicious sites from injecting cookies into other sites. 

Imagine a scenario where attacker.com can set a cookie for the "com" TLD in a victim's cookie store. When the victim wants to login into for example facebook.com, the victim will unknowingly present the attacker's cookie to facebook.com. Now, recall that cookies are used by servers to track "state" in session management, when the victim tries to login via the attacker cookie, the server will assign the victim's identity to the attacker's cookies. This effectively makes it so that the attacker can now visit facebook.com with the victim's identity tied to the attacker's cookies and can do anything they want as the victim (basically taking over the victim's account.)

**The Public Suffix List and eTLD+1**

There came a time where the shared parts of a domain name was not limited to TLDs, where you had a TLD for every country in the world as well as a TLD+1 for each industry in a country. So for example:

co.uk => Commercial sites in the UK

gov.uk => Government sites in the UK

This led to things being _really messy_ for browsers, you can read the report in Firefox here:

[![Logo](https://haxatron.gitbook.io/vulnerability-research/~gitbook/image?url=https%3A%2F%2Fbugzilla.mozilla.org%2Fextensions%2FBMO%2Fweb%2Fimages%2Ffavicon.svg&width=20&dpr=3&quality=100&sign=c3731617&sv=2)252342 - fix cookie domain checks to not allow .co.ukbugzilla.mozilla.org](https://bugzilla.mozilla.org/show_bug.cgi?id=252342)

Not only could TLD+1 (eg. co.uk) be shared amongst different domain names belonging to different organizations, countries such as Japan allows TLD+2 to be shared based on __{prefecture}.{city}.jp. Oh the absurdity of it all!

A solution was eventually reached by the Mozilla team, known as the public-suffix list, which is basically a list containing hardcoded values of known shared portions of the domain. The definition of "site" was eventually updated to eTLD+1, where eTLD (effective TLD) includes the standard TLDs and those from the public-suffix lists.

### 

Discovery

**Dot experiments**

I first tried to set a cookie for "com" but it failed.

However when I tried to set a cookie for "co.uk" in curl and it worked!

So it turns out I can set cookies for co.uk. _So is it a vulnerability?_

The answer is no. Because it is documented here: <https://curl.se/docs/CVE-2014-3620.html>

> libcurl's cookie parser has no Public Suffix awareness, so apart from rejecting TLDs from being allowed it might still allow cookies for domains that are otherwise widely rejected by ordinary browsers.

But what details about the internal logic can we infer from this? My guess was that curl's cookie parser will reject the target domain if it does not contain a dot. 

So what contains a dot but is still a TLD? A _trailing dot TLD._

A trailing dot after the hostname - https://example.com. is legal and is often used by people who do not want to resolve names via the DNS search list. You can read more about it here: <http://www.dns-sd.org/trailingdotsindomainnames.html>

I tried to set a cookie for _trailing dot TLD_ and it worked! 

This meant that people who use cookies and specified dots in their domain names (to avoid resolution via the DNS search list) were vulnerable to the cookie injection vulnerability I mentioned earlier.

This was CVE-2022-27779.

**Part 1 Epilogue**

After I reported this I came to know that this was due to recently introduced bug related to new handling of trailing dots.

![](https://haxatron.gitbook.io/vulnerability-research/~gitbook/image?url=https%3A%2F%2F4111718619-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwUaikFcU8mF4x4Uuqdj9%252Fuploads%252F8Ar1SKUfV5vcEneb99ZP%252Fimage.png%3Falt%3Dmedia%26token%3D0ff44096-b8fb-472f-bb2b-b86fdc16e79f&width=768&dpr=3&quality=100&sign=f57dac01&sv=2)

This is important for later.

And also, it turns out this very same issue was foreshadowed by a comment on <https://daniel.haxx.se/blog/2014/03/24/reducing-the-public-suffix-pain/>

![](https://haxatron.gitbook.io/vulnerability-research/~gitbook/image?url=https%3A%2F%2F4111718619-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwUaikFcU8mF4x4Uuqdj9%252Fuploads%252FjyM1ieFuZL2axVSXUdZe%252Fimage.png%3Falt%3Dmedia%26token%3Dccd9d56e-646d-4b5f-9040-dcc1c388e70d&width=768&dpr=3&quality=100&sign=6378703d&sv=2)

### 

Part 2: CVE-2022-27780: Percent-encoded path separator in URL host

This flaw involved a URL parsing flaw. Among the 3 bugs, I think this was the most dangerous of the 3 as it opened up the possibility of SSRF and even allowed an attacker to break internal cookie engine logic and trick a victim to send a cookie meant for example.com to attacker.com when using a proxy.

### 

Background

**URLs**

The definition of the URL has always been hazy with the introduction of the new WHATWG spec which breaks the RFC3986 spec. This has been and will still continue to be the cause of many SSRF problems. A more detailed summary of the problems can be found here: <https://github.com/bagder/docs/blob/master/URL-interop.md>, written by the maintainer of curl. I recommend both developers and security researchers to familiarise themselves with the main interoperability differences. 

curl operates via the RFC3986(+) spec. 

![](https://haxatron.gitbook.io/vulnerability-research/~gitbook/image?url=https%3A%2F%2F4111718619-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwUaikFcU8mF4x4Uuqdj9%252Fuploads%252F4qLKa3J45N77HOoDp5AX%252Fimage.png%3Falt%3Dmedia%26token%3D9bf02c4b-a247-4804-90e9-5530972aee6d&width=768&dpr=3&quality=100&sign=73707f15&sv=2)

URLs according to RFC3986

To prevent interoperability issues, a URL parser API is provided: <https://curl.se/libcurl/c/curl_url_get.html>.

**HTTP Proxies**

A proxy works by working as an intermediary between client and server. For a HTTP Proxy when a client wants to connect to http://example.com/test, they will send the entire URL to the proxy as shown:

The proxy will then make a request to the desired URL http://example.com/test, receive the response and then forward it back to the client.

### 

Discovery

**The Flaw**

Evaluating URL parsers are one of my favourite things to do as it involves a lot of trial-and-error and creativity to find - akin to scientific experiments! 

Somewhere along my experimentation, I tried to send a proxy URL containing a %2F and inspect the proxy request.

The result was surprising:

And internally (and likewise the URL API), this was how curl was evaluating the URL

_______________________________________________________________________________________________________

Original URL => http://127.0.0.1%2F.example.com

Scheme => http:// 

Hostname => 127.0.0.1/.example.com

Stored URL (sent to the proxy) => http://127.0.0.1/.example.com

_______________________________________________________________________________________________________

Are you thinking what I am thinking? 

If the hostname was checked to determine if it ended with .example.com. The malformed hostname (127.0.0.1/.example.com) will pass the check. And when the stored URL is sent to a proxy, the proxy evaluates it as http://127.0.0.1/.example.com! This can allow for SSRFs

It was also determined that this issue is not limited to proxies. curl provides a function that allows user to retrieve the stored URL (for URL manipulation purposes) in the CURLUPART_URL option. So if the URL is parsed and the URL from CURLUPART_URL is used, it also opens up the door for SSRF.

**Breaking Cookie Engine Logic**

It is not limited to just that! curl also contains a internal check in the cookie engine which is susceptible to this flaw in the domain tail-matching logic. 

The domain tail matching logic determines whether a cookie get sent to a particular domain based on whether they end with the tail the cookie is set for.

So for instance, for the cookie jar above, curl will send the cookie only if the domain of the URL it is connecting to matches example.com or ends with .example.com,

That means, if an attacker convinces a curl user to visit http://attacker.com%2F.example.com and the user uses a HTTP proxy the following will happen:

  1. curl will internally derive the hostname as attacker.com/.example.com

  2. attacker.com/.example.com ends with .example.com so curl will send the cookie.

  3. curl connects to the proxy with instructing the proxy to connect to the URL http://attacker.com/.example.com with the cookie

  4. The proxy makes a request with the cookie to attacker.com and leaks the cookie (without the attacker even having to conduct any MITM attacks)

It should be noted that this requires the Secure attribute to not be set as this only works with HTTP protocol. However, many sites do not set the Secure attribute anyway.

### 

Part 3: CVE-2022-30115: HSTS bypass via trailing dot

Return of the evil trailing dot!

### 

Background

**HSTS**

HSTS**** which stands for HTTP Strict Transport Security, is a defence-in-depth mechanism implemented by browser to defend against MITM attacks. When a client tries to access a page over insecure HTTP protocol, there is a chance that an active network attacker can sniff the clients request or even modify the response contents. HSTS protects against that by automatically instructing a client to use HTTPS protocol instead of HTTP for a given hostname even if explicit HTTP is specified.

### 

Discovery

**Searching for more dot problems**

Recall that in Part 1, we know that a recently updated version of curl contained new handling of trailing dots:

![](https://haxatron.gitbook.io/vulnerability-research/~gitbook/image?url=https%3A%2F%2F4111718619-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwUaikFcU8mF4x4Uuqdj9%252Fuploads%252FxUcsMMR3bwtSfdzprOZF%252Fimage.png%3Falt%3Dmedia%26token%3D5a0f278a-ba9d-4ff7-aeba-c253a6009632&width=768&dpr=3&quality=100&sign=b7fdeb48&sv=2)

Since we already found a flaw with curl's cookie engine due to mishandling of the trailing dot. A good question to ask is:

**Where else may the trailing dot cause security problems?**

Now first and foremost, curl is a HTTP client, but it is not the only HTTP client out there. There are other HTTP clients such as Firefox, Chrome. 

Surely, the trailing dot must have caused problems there too right?

And yes they did!

With a simple Google search along the lines of "firefox trailing dot vulnerability" and "chrome trailing dot vulnerability", I found the following links:

<https://bugs.chromium.org/p/chromium/issues/detail?id=461481>

<https://www.mozilla.org/en-US/security/advisories/mfsa2015-13/>

Now, curl does not have the HPKP (HTTP Public Key Pinning) feature. But it does have the HSTS feature!

And true enough, the HSTS implementation was also affected by the new trailing dot handling implemented in curl 7.82.0, so if a HSTS cache contained:

And the following command was used

curl will connect to accounts.google.com. via insecure HTTP even though by HSTS, it is supposed to connect via HTTPS, allowing for MITM attacks.

### 

Concluding Thoughts

Though these were neither ground-breaking nor intricate vulnerabilities, this experience had reminded me not to be afraid to test popular, widely-used applications. 

### 

Acknowledgements

These vulnerabilities were discovered by me (@Haxatron) and reported via Hackerone across 3 reports <https://hackerone.com/reports/1553301>, <https://hackerone.com/reports/1553841> and <https://hackerone.com/reports/1557449>. Thanks to @bagder (maintainer) for acknowledging and fixing the vulnerabilities promptly as well as Hackerone for the platform.

## 

[PreviousCVE-2021-4119: [Bookstack] Email harvesting via SQL "LIKE" clause exploitation](/vulnerability-research/vr1)

Last updated 4 years ago

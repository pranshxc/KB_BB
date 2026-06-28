---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-06_another-vision-for-ssrf.md
original_filename: 2022-06-06_another-vision-for-ssrf.md
title: Another vision for SSRF
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: 5020c4599a741d30c1a9bf2b1c131defc3158fb8889805e7f1a41809521cbfce
text_sha256: 8b15e2496af763026ec24c89b3ca1789d872de054e795cdecdecb4e10364c7c8
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Another vision for SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-06_another-vision-for-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `5020c4599a741d30c1a9bf2b1c131defc3158fb8889805e7f1a41809521cbfce`
- Text SHA256: `8b15e2496af763026ec24c89b3ca1789d872de054e795cdecdecb4e10364c7c8`


## Content

---
title: "Another vision for SSRF"
url: "https://gccybermonks.com/posts/ssrfvision/"
final_url: "https://gccybermonks.com/posts/ssrfvision/"
authors: ["phor3nsic (@phor3nsic_br)"]
bugs: ["SSRF"]
publication_date: "2022-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2584
---

# [Another vision for SSRF](https://gccybermonks.com/posts/ssrfvision/)

by [@phor3nsic_br](https://twitter.com/phor3nsic_br)

![](https://gccybermonks.com/assets/ssrfvision/20220601162352.png)

## Summary

For a long time, I tested SSRF failures to search for services and ports from the internal network and use the information to obtain interesting data or reach a RCE. But in the last few days, I came across situations where I didn’t have an internal scenario, I had a good flaw but its impact would be low.

Until a great idea came up, I would like to share it with you!

## What is SSRF 

As much as I believe that more than half of the readers who are seeing this article already know what SSRF _(Server Side Request Forgery)_ is, I leave the description and reference to make it easier for everyone to understand:

_“The target application may have functionality for importing data from a URL, publishing data to a URL or otherwise reading data from a URL that can be tampered with. The attacker modifies the calls to this functionality by supplying a completely different URL or by manipulating how URLs are built (path traversal etc.).”_

[Owasp](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)

## Common Vision

When reading all the writings about SSRF, we have a line of reasoning to be understood, perhaps because this is the most talked-about by all, where an attacker manipulates the server-side request to gain access to internal data.

However, companies knowing the possible problem, segregate these hosts, so that the attacker cannot get anything from the internal network, limiting access to ports and implementing a series of restrictions where SSRF would not be accepted by bug bounty programs, or by the client.

Okay, is SSRF limited to just that? Is there nothing else we can do?

## Another Vision

_SSRF To Account Takeover_

Before continuing, during this writing the channel another cool view on SSRF+Phishing that can be seen on the @gregxsunday channel, [Bug Bounty Reports Explained](https://www.youtube.com/watch?v=z1FpSFG2KpY), but still, we will deal with another point of view!

The concept I bring is to use the server-side, to reach the client-side, and we will still get a high criticality, because the final goal is to reach the user and their data, through SSRF in a sub/domain.

To reach the client-side, we need our SSRF to reflect the headers used by the client this is common in SSRF that will serve as a proxy so the attacker can define a proxy in the application.

By doing this we have something similar to a subdomain takeover, as we can take over all the content that transits to that subdomain. This already very impactful in the case of a domain but in the case of an out of scope subdomain, or a dev environment, it may not have as much effect, as there are not many direct requests for regions like this and the company can inform that this is not under their control, reducing the impact of the vulnerability.

We move on to another functionality. We need authentication/session cookies for applications on the same domain as the SSRF.

Example: 

If the SSRF is on ssrf.dev.example.com, we need to find an application with authentication on *.example.com that has cookies set as follows:
  
  
  Set-cookie: session=SECRET_SESSION, domain=.example.com, HttpOnly
  

Note that the cookie is being set so that it can move freely between all subdomains of *.example.com.

Most of us know that if a cookie has the HttpOnly flag it cannot be obtained through a XSS flaw, if you don’t know read:

[HttpOnly](https://developer.mozilla.org/docs/Web/HTTP/Cookies)

So, even if we have a XSS in any subdomain of example.com, we can’t capture the cookies, but we can still reuse them with fetch read more [here](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#sending_a_request_with_credentials_included)

In case Set-Cookie is deploying SameSite this way:
  
  
  Set-cookie: session=SECRET_SESSION, domain=.example.com, HttpOnly, SameSite=Lax
  

We could neither get the cookies nor reuse them with fetch through a XSS due to the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite). implementation.

Ok, Ok, Ok…

We cannot obtain or reuse cookies through a XSS, but we can steal these cookies through a SSRF!

![](https://media.giphy.com/media/fvkWXwmv7V9zfTd9z6/giphy.gif)

The request carries cookies, and they can be obtained through logs from the server that’s monitoring the requests.

The attacker must determine that the SSRF directs requests to its server and then makes its content available through the vulnerable domain. By sending the server URL to the victim, the victim somehow accesses the URL. Soon attacker will get the session cookie through your logs!

![](https://gccybermonks.com/assets/ssrfvision/20220601_154844.png)

Simple and a little weird, right? To make it easier, we’ll follow with an example lab.

## Lab

When accessing the app.localhost.io we receive a cookie with the HttpOnly flag and `domain=.localhost.io` :

![](https://gccybermonks.com/assets/ssrfvision/20220601164657.png)

If we try to get that cookie through a XSS, we won’t even see it due to HttpOnly:

![](https://gccybermonks.com/assets/ssrfvision/20220601164922.png)

However, if we use a SSRF described above, our cookies are sent to the destination server.

![](https://gccybermonks.com/assets/ssrfvision/20220601165050.png)

If we redirect the request to our server, we can view the requests and get the victim’s cookies:

![](https://gccybermonks.com/assets/ssrfvision/20220601165541.png)

## Conclusion

I could let this SSRF go by not being able to access what I wanted to see, but when we stop following a list of thoughts, we can think differently.

The concept of hacking is talked about a lot: “think outside of the box”, however, we stop thinking in a small box and think in bigger boxes, the truth is, don’t fall into any box, think above implanted limits, the beauty can be on the other side of the edges.

Posted on 06\. June 2022

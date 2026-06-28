---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-09_bypassing-403.md
original_filename: 2020-08-09_bypassing-403.md
title: Bypassing 403
category: documents
detected_topics:
- idor
- ssrf
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- ssrf
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 6c40a52d5bb7d9b5316285a5cd5da6fb58c4bb3e11fa36ec1ba26e3c3461e7d3
text_sha256: 4c2b6ec863d1b918e40c34cb60cd2e38562319d38c8ea66996fe71a589d0d26e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing 403

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-09_bypassing-403.md
- Source Type: markdown
- Detected Topics: idor, ssrf, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `6c40a52d5bb7d9b5316285a5cd5da6fb58c4bb3e11fa36ec1ba26e3c3461e7d3`
- Text SHA256: `4c2b6ec863d1b918e40c34cb60cd2e38562319d38c8ea66996fe71a589d0d26e`


## Content

---
title: "Bypassing 403"
page_title: "Bypassing 403 – Observations in Security"
url: "https://observationsinsecurity.com/2020/08/09/bypassing-403-to-get-access-to-an-admin-console-endpoints/"
final_url: "https://observationsinsecurity.com/2020/08/09/bypassing-403-to-get-access-to-an-admin-console-endpoints/"
authors: ["Michael Hyndman (@michaelhyndman)"]
bugs: ["Authentication bypass"]
publication_date: "2020-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4338
---

# Bypassing 403

![](https://observationsinsecurity.com/wp-content/uploads/2020/08/pexels-photo-1022698-e1650612856164.jpeg?w=1568)

A few weeks ago I came across this cool “accidental” exploit vector which was documented about 8 years ago by [IRCmaxwell](https://blog.ircmaxell.com/2012/11/anatomy-of-attack-how-i-hacked.html) and describes a way to trick servers (behind a reverse proxy or load balancer) into thinking a HTTP request which is ordinarily unauthorised, is actually authorised. 

I read the blog post while doing some research into the X-Forwarded-For http request header and immediately identified this “accidental exploit” as a really cool use-case for applying to bug bounty targets. 

To explain this exploit we need to first understand the purpose of the X-Forwarded-For request header. 

> The **`X-Forwarded-For`** (XFF) header is a de-facto standard header for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or a load balancer. When traffic is intercepted between clients and servers, server access logs contain the IP address of the proxy or load balancer only. To see the original IP address of the client, the `X-Forwarded-For` request header is used.
> 
> <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For>

This header is used and implemented in a variety of ways and because of this, it can also be exploited in a variety of ways. Researchers often use this header to inject SQL payloads, perform proxy enumeration, client IP spoofing, SSRF and many other interesting use-cases which I’ll cover later. 

However the use-case that really got my attention was a variation of IP spoofing which causes the target web server to reveal information that it shouldn’t. I like to find vulnerabilities that most scanners aren’t configured to find and this I think is another one of these cases. 

So IRCMaxwell experienced a situation where he unintentionally configured all of his outgoing http requests to include the X-Forwarded-For header configured with an ip address of 127.0.0.1 (the local host) – you can read his blog to find out how and why. 

However this resulted in a situation where he discovered that StackOverflow was revealing parts of an administrative console to him that should not have been available for public viewing or access. 

What was happening is that once the StackOverflow server recieved this request, it interpreted the “X-Forwarded-For: 127.0.0.1” to mean that webserver itself had initated the request, and that by implication, the requestor was authorised to see all the content available at that endpoint. IRCMaxwell was effectively masquarading as the webserver itself as far as the webserver was concerned. 

I thought this was a pretty cool vulnerablity and so thought about how I could apply this to bug bounty targets. 

So I wrote a tool which sends numerous requests to a target address with different variations of the XFF header localhost addressing to accommodate for cases where a WAF was blocking requests based on localhost signatures. 

The tool uses heusristics to learn variations in the http response that could be indicative of additional sensitive information that is being disclosed. 

![](https://observationsinsecurity.com/wp-content/uploads/2020/08/bypas.jpg?w=610)

As I developed this tool and scanned across hundreds of bug bounty targets I began to discover some interesting nuances. Web applications would handle and respond to XFF input very differently, resulting in some unexpected bug bounty leads. 

However, the biggest win came early in the scanning when the tool discovered an admin console on a subdomain that is blocked to the public (response code 403), until you sent it a http request with an XFF header set to 127.0.0.1:80 at which point, the admin console became accessible. 

After writing up the report – demonstrating the impact – it occurred to me that the same issue might occur on other subdomains of the parent domains.

After some searching I realised that not one subdomain, but two, no wait… over 800 subdomains for this particular organisation were impacted by the same issue. Each of these subdomains contained web applications, APIs or other services which were normally blocked to public access, but were bypassable using this technique! 

### Share this:

  * [ Share on X (Opens in new window) X ](https://observationsinsecurity.com/2020/08/09/bypassing-403-to-get-access-to-an-admin-console-endpoints/?share=twitter)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://observationsinsecurity.com/2020/08/09/bypassing-403-to-get-access-to-an-admin-console-endpoints/?share=linkedin)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://observationsinsecurity.com/2020/08/09/bypassing-403-to-get-access-to-an-admin-console-endpoints/?share=jetpack-whatsapp)
  * 

Like Loading...

### _Related_

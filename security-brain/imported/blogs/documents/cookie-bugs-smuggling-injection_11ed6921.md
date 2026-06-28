---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-05_cookie-bugs-smuggling-injection.md
original_filename: 2023-05-05_cookie-bugs-smuggling-injection.md
title: Cookie Bugs - Smuggling & Injection
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 11ed692170bc62ab601acef0a1b375530c882837995720264853f730b6174e62
text_sha256: 6a81c0a7562ce570fbfc1d388043c5fd59d60b43f33cec4e6b5a9a5a24de3688
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Cookie Bugs - Smuggling & Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-05_cookie-bugs-smuggling-injection.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `11ed692170bc62ab601acef0a1b375530c882837995720264853f730b6174e62`
- Text SHA256: `6a81c0a7562ce570fbfc1d388043c5fd59d60b43f33cec4e6b5a9a5a24de3688`


## Content

---
title: "Cookie Bugs - Smuggling & Injection"
url: "https://blog.ankursundara.com/cookie-bugs/"
final_url: "https://blog.ankursundara.com/cookie-bugs/"
authors: ["Ankur Sundara (@ankursundara)"]
programs: ["Eclipse Foundation (Jetty)"]
bugs: ["Cookie smuggling", "Cookie injection"]
publication_date: "2023-05-05"
added_date: "2023-05-06"
source: "pentester.land/writeups.json"
original_index: 1186
---

[research](/tag/research/)

# Cookie Bugs - Smuggling & Injection

Research on how browsers encode & send cookies, how they are parsed by various web frameworks, and some bugs

  * [ ![Ankur Sundara](/content/images/size/w100/2021/08/logo.jpeg) ](/author/ankur/)

#### [Ankur Sundara](/author/ankur/)

05 May 2023 • 5 min read

Share

![Cookie Bugs - Smuggling & Injection](/content/images/size/w2000/2023/05/cookies.jpg)

Recently, I investigated how browsers encode & send cookies, and how they are parsed by various web frameworks. Here's some documentation of bugs (+CVE) and interesting behavior I found. 

## Some Interesting Browser Behavior

First, let's start off with some surprising behavior (not bugs). Some of this is apparently considered "common knowledge", but these facts were mostly new to me.

### Subdomains

If a cookie on `example.com` is set with a _domain_ attribute specified, it will be sent to any subdomain `*.example.com` as well

### Superdomains

If a subdomain `sub.example.com` sets a cookie with _domain_ attribute of `.example.com`, it will be sent on requests to the parent domain

### __Host and __Secure prefixed cookies

**`__Secure-` prefix**: must be set with the `secure` flag from a secure page (HTTPS).

**`__Host-` prefix**: must be set with the `secure` flag, must be from a secure page (HTTPS), must not have a domain specified (and therefore, are not sent to subdomains), and the path must be `/`.

`__Host-` prefixed cookies cannot be sent to superdomains or subdomains, so, if you want to isolate your application cookies, prefixing everything with `__Host-` is not a bad idea. 

### Cookie Ordering

Cookies sent by the browser (both chrome and ff, as of writing this) are ordered by:

  1. Path length, longest to shortest
  2. Last updated time, least recent to most recent

(this is useful information for the later spoofing/smuggling attacks, and I didn't see this documented anywhere online)

### The empty cookie

Browsers actually allow a cookie with an empty name! 
  
  
  document.cookie = "a=v1"
  document.cookie = "=test value;" // empty name
  document.cookie = "b=v2"

This results in the sent cookie header:
  
  
  a=v1; test value; b=v2;

More interestingly, if you have a vector that somehow lets you set the empty cookie, you can control any other cookie!
  
  
  function setCookie(name, value) {
  document.cookie = `${name}=${value}`;
  }
  
  setCookie("", "a=b"); // this sets the empty cookie to a=b

Although internally in the browser, this is set as the empty named cookie, it will result in the sent cookie header
  
  
  a=b;

Meaning, every webserver will parse it as the cookie `a` being set to the value `b`.

However, you still _cannot_ abuse this to spoof `__Host-` or `__Secure-` cookies

* * *

## Chrome Bug - document.cookie corruption

If a unicode surrogate codepoint is in a set cookie, `document.cookie` will be permanently corrupted and return an empty string.
  
  
  document.cookie
  // "a=b;"
  document.cookie = "\ud800=meep";
  document.cookie
  // ""

Also, this kind of breaks devtools 🤔 (you can't delete it)

* * *

## Cookie Smuggling

I found that several webservers perform incorrect cookie string parsing. Whenever the parser encountered a dquoted cookie value, it continued to read the cookie string – even if a semicolon is encountered! The semicolon is supposed to separate KV pairs, so surely that can't be right.

Say a browser sends 3 cookies, **RENDER_TEXT, JSESSIONID, ASDF** , resulting in the following cookie header being sent.

> RENDER_TEXT=**"hello world** ; JSESSIONID=**13371337** ; ASDF=**end"** ;

This would then be parsed by Jetty/Undertow as a _single_ cookie, disregarding the **JSESSIONID** and **ASDF** cookies and instead interpreting them as part of the **RENDER_TEXT** cookie value due to the dquotes.

> RENDER_TEXT=**hello world; JSESSIONID=13371337; ASDF=end**

This has security implications because say, the **RENDER_TEXT** cookie value is rendered on the page, and the **JSESSIONID** cookie is _HttpOnly_ , an attacker that has gained XSS can leverage this bug to exfiltrate JSESSIONID!

It turns out that the underlying issue at hand here is leftover support of RFC2965, which uses RFC2616 for a quoted-string definition:
  
  
  av-pairs  =  av-pair *(";" av-pair)
  av-pair  =  attr ["=" value]  ; optional value
  attr  =  token
  value  =  token | quoted-string
  quoted-string  = ( <"> *(qdtext | quoted-pair ) <"> )
  qdtext  = <any TEXT except <">>

old cookie parsing (RFC2965)

The newer RFC6265 neutered the cookie quoting mechanism to quote only characters that don't need to be quoted:
  
  
  cookie-pair  = cookie-name "=" cookie-value
  cookie-name  = token
  cookie-value  = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )
  cookie-octet  = %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E
  ; US-ASCII characters excluding CTLs,
  ; whitespace DQUOTE, comma, semicolon,
  ; and backslash
  
  token  = 1*<any CHAR except CTLs or separators>
  separators  =  "(" | ")" | "<" | ">" | "@"
  | "," | ";" | ":" | "\" | <">
  | "/" | "[" | "]" | "?" | "="
  | "{" | "}" | SP | HT

modern cookie parsing (RFC6265)

Quoting @gregw (Jetty Maintainer)

> What a mess! The RFC have baked in a security issue if you have some devices implementing an old RFC and others implementing the new, then they differ on a fundamental parsing issue!

The Java Webservers **Jetty** , **TomCat** , **Undertow** were all found to be susceptible, and the Python web framework **Zope**.

Furthermore, `http.cookie.SimpleCookie` and `http.cookie.BaseCookie` in the Python stdlib parse RFC2616 format cookies, so any server that uses it to parse the cookie string is susceptible too.

This includes the Python web servers/frameworks: **cherrypy** , **web.py** , **aiohttp server** , **bottle** , and **webob**(**Pyramid, TurboGears)**

That's a lot!

* * *

## Cookie Injection

I also found that many webservers perform incorrect cookie parsing - where they use incorrect delimiters for beginning the next cookie name/value pair.

This allows multiple cookies to be spoofed with only control over 1 cookie value.

The Java Undertow webserver, for example, immediately begins parsing the next cookie after the end of a quoted cookie value, without waiting to encounter a semicolon. 

Say a user has control over the sent **LANGUAGE** cookie

> LANGUAGE=**"en-us" CSRF_TOKEN="SPOOFED_VALUE"**

This is then parsed by Undertow as 2 separate cookies (even though there's no semicolon – the cookie separator that browsers use)

> LANGUAGE=**en-us**  
>  CSRF_TOKEN=**SPOOFED_VALUE**

The Python **Zope** webserver allows `,` as a Cookie delimiter, which may appear normally in cookie values sent by the browser.

> LANGUAGE=**en-us,CSRF_TOKEN=SPOOFED_VALUE**

is parsed as 2 separate cookies

> LANGUAGE=**b** ,CSRF_TOKEN=**SPOOFED_VALUE**

Python's stdlib `http.cookie.SimpleCookie` and `http.cookie.BaseCookie` suffer from a similar issue, where they immediately start parsing the next cookie on a _space_ character.

> LANGUAGE=**en-us CSRF_TOKEN=SPOOFED_VALUE**

is parsed as 2 separate cookies

> LANGUAGE=**b** CSRF_TOKEN=**SPOOFED_VALUE**

Meaning – **cherrypy** , **web.py** , **aiohttp server** , **bottle** , and **webob**(**Pyramid, TurboGears)** are again all vulnerable.

Cookie Injection has security implications when:

  1. a web application performs **Cookie-based CSRF protection**. This is where you validate that the submitted CSRF-token field in a form matches some CSRF-token Cookie value.  
  
If you can control the CSRF-token Cookie with a Cookie injection, then you can bypass the CSRF protection! Furthermore, in python's `http.cookie` packages, the last duplicate Cookie name overrides any previous ones, so this type of attack is especially easy.
  2. spoofing of `__Secure-` and `__Host-` cookies (e.g. abusing an insecure context)
  3. a configuration where Cookies are passed onto a backend server, and Cookie Injection could lead to authorization bypasses (frontend server isn't susceptible to injection - strips authentication cookies, backend server that's susceptible to spoofing gets the auth cookie injected)

* * *

I disclosed these bugs to the various webservers and libraries, but only Jetty responded, filing [CVE-2023-26049](https://nvd.nist.gov/vuln/detail/CVE-2023-26049) and [GHSA-p26g-97m4-6q7c](https://github.com/advisories/GHSA-p26g-97m4-6q7c). Kudos to them for the fast response and patch, even though Jetty was not vulnerable to the more impactful bug (injection).

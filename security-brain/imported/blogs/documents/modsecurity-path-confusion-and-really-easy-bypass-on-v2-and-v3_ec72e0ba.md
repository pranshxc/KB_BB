---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-02_modsecurity-path-confusion-and-really-easy-bypass-on-v2-and-v3.md
original_filename: 2024-02-02_modsecurity-path-confusion-and-really-easy-bypass-on-v2-and-v3.md
title: 'ModSecurity: Path Confusion and really easy bypass on v2 and v3'
category: documents
detected_topics:
- sqli
- oauth
- sso
- xss
- command-injection
- path-traversal
tags:
- imported
- documents
- sqli
- oauth
- sso
- xss
- command-injection
- path-traversal
language: en
raw_sha256: ec72e0ba9ff7a040b5e896d5a7b6c9ff5cd5c8612874d77751b3701b387ea519
text_sha256: 32d775d00e408e2f61dd98106dfc801f25593ed9493a8ffbf00c38b947e69920
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# ModSecurity: Path Confusion and really easy bypass on v2 and v3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-02_modsecurity-path-confusion-and-really-easy-bypass-on-v2-and-v3.md
- Source Type: markdown
- Detected Topics: sqli, oauth, sso, xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `ec72e0ba9ff7a040b5e896d5a7b6c9ff5cd5c8612874d77751b3701b387ea519`
- Text SHA256: `32d775d00e408e2f61dd98106dfc801f25593ed9493a8ffbf00c38b947e69920`


## Content

---
title: "ModSecurity: Path Confusion and really easy bypass on v2 and v3"
url: "https://blog.sicuranext.com/modsecurity-path-confusion-bugs-bypass/"
final_url: "https://blog.sicuranext.com/modsecurity-path-confusion-bugs-bypass/"
authors: ["Andrea Menin (@AndreaTheMiddle)"]
programs: ["ModSecurity"]
bugs: ["WAF bypass", "Path confusion"]
publication_date: "2024-02-02"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 465
---

[WAAP](/tag/waap/)

# ModSecurity: Path Confusion and really easy bypass on v2 and v3

  * [ ![Andrea Menin](/content/images/size/w100/2023/07/copertina.jpg) ](/author/themiddle/)

#### [Andrea Menin](/author/themiddle/)

02 Feb 2024 • 12 min read

Share

![ModSecurity: Path Confusion and really easy bypass on v2 and v3](/content/images/size/w2000/2024/01/modsec_path_confusion_cope.png)

TL;DR both ModSecurity v2 and v3 share a similar bug that can result in a really simple WAF bypass. The bug in the v3 branch has been fixed in version 3.0.12 and has been assigned the CVE number [CVE-2024-1019](https://nvd.nist.gov/vuln/detail/CVE-2024-1019?ref=blog.sicuranext.com). However,**the bug in the v2 line remains unfixed**. The core issue lies in ModSecurity's implicit URL-decode behavior before setting certain variables, which **not only represents an unwanted behavior but is also totally undocumented**. This behavior can lead both v2 and v3 users to **really easy WAF engine and/or WAF rule bypass**.

## ModSecurity v3 Path Confusion

We are used to reading about Path Confusion in attack categories such as [Web Cache Deception](https://portswigger.net/daily-swig/path-confusion-web-cache-deception-threatens-user-information-online?ref=blog.sicuranext.com) or in [OAuth issues](https://dl.acm.org/doi/pdf/10.1145/3627106.3627140?ref=blog.sicuranext.com). In this particular scenario, ModSecurity v3 was vulnerable to Path Confusion specifically in the handling of the HTTP Request Line, where it attempts to **extract the request path (and the optional query string) from the URL**.

![](https://blog.sicuranext.com/content/images/2024/01/image-16.png)

In ModSecurity, you have various variables at your disposal for rule development and inspection, and one of these is **`REQUEST_FILENAME`**. Essentially, `REQUEST_FILENAME` takes the initial part of the requested URL, until the optional question mark (?) that serves as the delimiter before the query string begins. This variable is really helpful when you need to inspect the request URI path for potential vulnerabilities, such as SQL Injection or Cross Site Scripting.

Unfortunately, ModSecurity v3 (until 3.0.12), **improperly implements this variable** , creating a vulnerability that can be easily exploited, resulting in a really simple WAF bypass. Let's see why in this blog post!

## The bug in REQUEST_FILENAME variable

There was an issue in the way ModSecurity parses the request line (for example `GET /foo/bar?foo=bar HTTP/1.1`) in order to set the `REQUEST_FILENAME` variable that should contains the requested URL without the query string part (In the before example: `/foo/bar`).

![](https://blog.sicuranext.com/content/images/2024/01/image-30.png)from the ModSecurity wiki

Instead of simply taking the initial part of the URL up to the optional question mark, **it performs an URL-decode beforehand**. During this process, all instances of `%3f` (the hexadecimal representation of the question mark) are converted to `?`. So, **when the parser begins reading from the start of the path, it stops at the question mark** , even though in this case, it's not the query string delimiter.

**Let me try to make it easier.**  
Suppose an HTTP request to Nginx + ModSecurity like this:  
`curl 'http://example.com/foo%3f';alert(1);foo='`  
  
Now, ModSecurity needs to set the `REQUEST_FILENAME` variable, so it follows these steps:

  * Performs a URL decode of the requested resource, transforming `/foo%3f';alert(1);foo='` into `/foo?';alert(1);foo='`.
  * Extracts the path, excluding the query string, by starting from the beginning of the URL-decoded resource and stopping at the optional question mark character. In our example, it will be `/foo`.
  * Sets the `REQUEST_FILENAME` variable with the resulting string, which is `/foo` without the XSS payload.

A picture is worth a thousand words:

![](https://blog.sicuranext.com/content/images/2024/01/image-19.png)

So, basically, by inserting `%3f` before any payload, ModSecurity interprets what follows as a query string and excludes it from the `REQUEST_FILENAME` variable**causing all rules to completely ignore it**.

Below is the vulnerable code snippet:

![](https://blog.sicuranext.com/content/images/2024/01/image-28.png)

## The Bypass Technique

The OWASP Core Rule Set **widely use this variable in its rules, basically everywhere,** including Generic, PHP, XSS, LFI, RFI, SQLi, Java, Protocol Violation, and Protocol Enforcement rule sets ([as you can see here](https://github.com/search?q=repo%3Acoreruleset%2Fcoreruleset%20REQUEST_FILENAME&type=code&ref=blog.sicuranext.com)).

Consider a scenario where ModSecurity **v3.x** with the OWASP Core Rule Set need to protect an API that is vulnerable to SQL Injection in request path. In order to test this kind of scenario, the OWASP Core Rule Set developed a [specific challenge](https://sandbox.coreruleset.org/challenges/php-sqli-02/index.php?ref=blog.sicuranext.com) to test the effectiveness of the WAF rules in protecting the application from SQL Injection exploit:

![](https://blog.sicuranext.com/content/images/2024/01/image-17.png)SQL Injection Challenge

As you can see from the screenshot above, by appending the user ID at the end of the path, the vulnerable application executes a SELECT query on its MySQL database, retrieving the username associated with the specified numerical ID. As you can probably guess, **this application is vulnerable to SQL Injection** , which can be exploited by adding SQL syntax after the numerical user ID, for example: `/1+OR+1=1--`. 

However, the application is protected by ModSecurity and the OWASP Core Rule Set, and if you try to send a SQL Injection payload, the request gets blocked at Paranoia Level 2 by Rule 942101 "SQL Injection Attack Detected via libinjection":

![](https://blog.sicuranext.com/content/images/2024/01/image-18.png)request blocked by WAF

**What can we do to bypass the entire ruleset and exploit the SQL Injection?** It's quite easy. We simply need to convert the user ID into a string, add `%3f` after it, and then append SQL syntax that enables us to execute a SELECT on the application's database in order to exfiltrate data. In the example below, **I successfully exfiltrated the password of the first user from the`users` database table**:

![](https://blog.sicuranext.com/content/images/2024/01/image-20.png)WAF Bypass and user's password exfiltrated

So, basically this is what I sent to the application:

![](https://blog.sicuranext.com/content/images/2024/01/image-21.png)

## It was a well known bug.

Perhaps you're thinking that this bug came as a surprise, but it wasn't. A user publicly reported this bug (without referring to security implications) on the [ModSecurity GitHub repository on March 19, 2022](https://github.com/owasp-modsecurity/ModSecurity/issues/2705?ref=blog.sicuranext.com):

![](https://blog.sicuranext.com/content/images/2024/01/image-29.png)

At that time, nobody considered the possibility of a bypass or a potential bug. However, what's even more astonishing is that anyone reading that public issue could have guessed the bypass. **So, we can say that this issue is public since 2022.**

## Are other variables affected?

Not only `REQUEST_FILENAME` is affected by this bug. This is a list of variable affected:

  * `REQUEST_FILENAME`
  * `REQUEST_BASENAME`
  * `PATH_INFO`

## Same bug on ModSecurity v2? No... but Yes!

ModSecurity v2 line doesn't have exactly the same bug since `REQUEST_FILENAME` is set before the URL decoding process takes place. Therefore, `%3f` in the path doesn't impact the content of the `REQUEST_FILENAME` variable in any way. So, basically, this is the state of `REQUEST_FILENAME` variable on ModSecurity v2 among the first two phases:

![](https://blog.sicuranext.com/content/images/2024/01/image-22.png)

**Is v2 vulnerable to Path Confusion?** Apparently Not. However, a v3 **similar design flaw** , where the variable contains the URL-decoded version of the request part, **exists in v2 as well**. 

So, is there a comparable bug in v2?**Yes.**  
Can it potentially lead to bypasses on v2?**Yes! let's see how.**

Perhaps you've noticed **some different behavior in the diagram above between phase 1 and phase 2**. As shown, during phase 2, the content of `REQUEST_FILENAME` seems URL decoded. But before going too deep into this, let me do a step back.

I won't going too deeply into what is a phase, but it's crucial to know that ModSecurity can run rules on 5 different phases: 

  * **Phase 1** contains the initial part of the request, which includes the request line and request headers. 
  * **Phase 2** contains everything from the previous phase, along with the request body. 
  * **Phase 3** builds upon the previous phases by adding the response headers, and 
  * **Phase 4** includes the previous phases along with the response body. 
  * **Phase 5** is executed just before the logging process takes place.

With that in mind, it's important to note that in ModSecurity v2, the variable `REQUEST_FILENAME` holds a different value in Phase 2 compared to Phase 1.

![](https://blog.sicuranext.com/content/images/2024/01/image-23.png)

First of all, it's quite odd that at phase 2, `%3f` is decoded to `?`, yet the `+` character is not transformed into a whitespace... I would expect something like `1? OR 1=1--` and not `1?+OR+1=1--`. The issue here lies in the fact that **basically this behavior is undocumented**. In OWASP Core Rule Set branch v3.4/dev (never released as an official release), this posed a problem. Take a look at this rule:

![](https://blog.sicuranext.com/content/images/2024/01/image-24.png)

Basically, **this rule is designed to block requests to files with specific extensions** , such as .backup, .bak, .bat, .cer, .cfg, .cmd, and so on. This aim to prevent the application from "inadvertently" exposing sensitive data, backup files, or even configuration files.

As you can see this rule runs at Phase 1. Why? Originally, this rule was designed to operate at Phase 2, and everything worked as intended. Here the rule at branch v3.3/dev:

![](https://blog.sicuranext.com/content/images/2024/01/image-25.png)

However, the OWASP Core Rule Set made the decision to move this rule to Phase 1 in order to improve web server performance. The reason behind this move was: **why block something at Phase 2 when you can block it earlier at Phase 1 and save CPU resources?** It was a smart and logical choice, if only the absence of the urldecoded function had been documented somewhere. **This inadvertently exposed CRS to a really stupid bypass** , with an important impact and severity since all known compatible WAF engines perform an implicit urldecode at Phase 2 but not at Phase 1.

Moving this rule from Phase 2 to Phase 1 means that in a request path like `/db.bak` you are inspecting the raw version of its value, meaning that converting the dot character into `%2e` like `/db%2ebak` will never trigger the rule above.

Requesting a file with `.bak` extension is correctly blocked by the WAF, as you can see in the screenshot below:

![](https://blog.sicuranext.com/content/images/2024/01/modsec_bypass_bak_1.png)

Due to this bug, you can just encode the dot character to `%2e` to bypass the rule, since it doesn't have a URL decode transformation function enabled (at phase 2 it was not needed):

![](https://blog.sicuranext.com/content/images/2024/01/modsec_bypass_bak_2.png)

## It is not an OWASP Core Rule Set fault.

We're talking about an engine bug here, nothing attributable to the OWASP Core Rule Set, which was merely responsible for making a wise decision to enhance performance. But if you are wondering:****

**How long did this rule remain at phase 1** , **allowing for this relatively simple bypass?**  
The answer is more than **3 years**. But is not completely true.  
  
This rule is been in this state since [this commit](https://github.com/coreruleset/coreruleset/commit/5a47465f9cee33d46ac62b03fd300195bbee8c2f?ref=blog.sicuranext.com) pushed more then 3 years ago (or [this pull request](https://github.com/coreruleset/coreruleset/pull/1941?ref=blog.sicuranext.com)). Now, I'm not sure if users typically opt to run only stable and supported CRS releases, but **over the past 3 years, it's possible that some have considered updating their WAF rules**.  
  
The OWASP Core Rule Set team will patch this rule on 4.0 (probably) but, at the time, if you are running ModSecurity on Apache and the OWASP Core Rule Set from commit `5a47465` (included) to `1dffb38` (excluded) **you're likely to be vulnerable to this bypass**.

Anyway, if you base your WAF on CRS tags (as of the time of writing this post) here is the status of all the tags present in the Core Rule Set GitHub repository, starting from version 3.3.0 (at the time of writing this post):

Tags | tFunc Status | Bypass on v2  
---|---|---  
`v3.3.0` | `phase:2 + t:none` | false  
`v3.3.0-rc1` | `phase:2 + t:none` | false  
`v3.3.0-rc2` | `phase:2 + t:none` | false  
**`v3.3.1-rc1`** | **`phase:1 + t:none`** | **TRUE**  
`v3.3.2` | `phase:2 + t:none` | false  
`v3.3.3` | `phase:2 + t:none` | false  
`v3.3.4` | `phase:2 + t:none` | false  
`v3.3.5` | `phase:2 + t:none` | false  
**`v4.0.0-rc1`** | **`phase:1 + t:none`** | **TRUE**  
**`v4.0.0-rc2`** | **`phase:2 + t:none`** | **TRUE**  
Branch | tFunc Status | Bypass on v2  
---|---|---  
`v3.3/dev` | `phase:2 + t:none` | false  
`v3.3/master` | `phase:2 + t:none` | false  
**`v3.4/dev`** | **`phase:1 + t:none`** | **TRUE**  
`v4.0/dev` | `phase:1 + t:urlDecodeUni` | false  
**`v4.0/main`** | **`phase:1 + t:none`** | **TRUE**  
  
Additionally, **if you've developed your own ModSecurity rules** and you're inspecting the `REQUEST_FILENAME` or `REQUEST_BASE` variable at Phase 1, it's imperative to **always enable the t:urldecode transformation function when inspecting`REQUEST_FILENAME` and `REQUEST_BASENAME` to prevent bypasses** like the one we've discussed earlier. Also, the fact that is not possible to inspect the raw version of those variables at Phase 2 is a significant limitation, IMO.

## Setting a new variable, better than patching!

Rather than applying a partial patch to the engine, I believe a more comprehensive solution would have involved setting alternative `REQUEST_FILENAME` and `REQUEST_BASENAME` variables using a simple rule. 

If you're familiar with ModSecurity and the OWASP Core Rule Set, you might be aware that variables can be set via a `SecRule`. In the example below, two new variables, `tx.request_filename_raw` and `tx.request_basename_raw`, are generated by correctly parsing the content of the `REQUEST_URI_RAW` variable:
  
  
  SecRule REQUEST_URI_RAW "@rx ^([^?]+)" \
  "id:123456,\
  phase:1,\
  pass,\
  capture,\
  t:none,\
  nolog,\
  ver:'OWASP_CRS/4.0.0-rc2',\
  setvar:'tx.request_filename_raw=%{tx.1}',\
  chain"
  SecRule TX:request_filename_raw "@rx /([^/]*)$" \
  "capture,\
  t:none,\
  setvar:'tx.request_basename_raw=%{tx.1}'"
  

As you can see, the first variable `tx.request_filename_raw` is set by the first regular expression that place into a group the requested URI from the beginning to the question mark. The second variable `tx.request_basename_raw` is set by the second regular expression that takes the ending part of the path, for example: `/foo/bar` will set `tx.request_basename_raw` as `bar`.

## Now, let's talk about the CVE-2024-1019.

![](https://blog.sicuranext.com/content/images/2024/01/image-26.png)CVSS score of CVE-2024-1019

First of all: **why does this WAF bypass have a score of 8.6?** In 2022, during a bug bounty program on **Intigriti** , the security researcher **Terjanq** discovered a ModSecurity engine bypass due to a bug in the multipart parser ([CVE-2022-48279](https://nvd.nist.gov/vuln/detail/CVE-2022-48279?ref=blog.sicuranext.com)), impacting both v2 and v3. **In that case, the score was rated at 7.5**. 

Now, this new CVE it's about a bypass exclusively related to ModSecurity v3 (not really, but... ok), with a similar level of attack complexity as the one discovered by Terjanq. The difference here lies in the scope and integrity impact. Why is the scope marked as "changed" in this case, and why is the integrity impact considered "high", when the previous bypass did not have these same distinctions? **I really don't know.**

**The CVE description has an ending sentence that** , if you agreed with what I wrote before about the v2 bypass impacting the OWASP Core Rule Set, **is quite ambiguous**. 

![](https://blog.sicuranext.com/content/images/2024/01/image-27.png)

Is it true to say that ModSecurity v2 is not impacted by this vulnerability? Technically, yes. However, **the same design error** present in v3 also **exists in v2** , which, as we discussed earlier, **results in a different type of bypass**. So, I'm wondering: why not address both issues and why assert that v2 doesn't have this problem when a very similar issue is present and well-known in v2? **I really don't know.**

## Timeline

The official timeline published by OWASP here [https://owasp.org/www-project-modsecurity/tab_cves](https://owasp.org/www-project-modsecurity/tab_cves?ref=blog.sicuranext.com) is:

  * 2023-11-13 : OWASP CRS submits report to Trustwave Spiderlabs, includes SQLi proof of concept
  * 2023-11-14 : Trustwave Spiderlabs acknowledges report, promises investigation
  * 2023-11-28 : OWASP CRS asks for update
  * 2023-11-29 : **Trustwave Spiderlabs rejects report, describes it as anomaly without security impact**
  * 2023-12-01 : OWASP CRS reiterates previously shared SQLi proof of concept
  * 2023-12-01 : Trustwave Spiderlabs acknowledges security impact
  * 2023-12-04 : OWASP CRS shares XSS proof of concept
  * 2023-12-07 : Trustwave Spiderlabs promises security release early in the new year
  * 2024-01-02 : OWASP CRS asks for update
  * 2024-01-03 : Trustwave Spiderlabs announces preview patch by Jan 12, release in the week of Jan 22
  * 2024-01-12 : Trustwave Spiderlabs shares preview patch with primary contact from OWASP CRS
  * 2024-01-22 : OWASP CRS confirms preview patch fixes vulnerability
  * 2024-01-24 : Trustwave Spiderlabs announces transfer of ModSecurity project to OWASP for 2024-01-25
  * 2024-01-25 : Trustwave Spiderlabs transfers ModSecurity repository to OWASP
  * 2024-01-25 : OWASP creates OWASP ModSecurity, assigns OWASP ModSecurity production level, primary contact from OWASP CRS becomes OWASP ModSecurity co-lead
  * 2024-01-26 : OWASP ModSecurity leaders decide to release on 2023-01-30
  * 2024-01-27 : OWASP ModSecurity creates GPG to sign upcoming release
  * 2024-01-29 : NCSC-CH assigns CVE 2024-1019, advisory text and release notes are being prepared, planned release procedure is discussed with Trustwave Spiderlabs
  * 2024-01-30 : OWASP ModSecurity Release 3.0.12

This timeline omits the fact that the bug was originally discovered by **liudongmiao** on March 19, 2022: [link](https://github.com/owasp-modsecurity/ModSecurity/issues/2705?ref=blog.sicuranext.com). Furthermore, when the ModSecurity development team (TrustWave at the time) responded to the OWASP Core Rule Set mail, stating that what was reported was not a security issue, they also provided a link to the liudongmiao's GitHub issue, confirming their awareness about this problem.

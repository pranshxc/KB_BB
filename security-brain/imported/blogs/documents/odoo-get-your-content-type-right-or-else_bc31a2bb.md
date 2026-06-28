---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-24_odoo-get-your-content-type-right-or-else.md
original_filename: 2023-04-24_odoo-get-your-content-type-right-or-else.md
title: 'Odoo: Get your Content Type right, or else!'
category: documents
detected_topics:
- xss
- command-injection
- api-security
- sso
- file-upload
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- api-security
- sso
- file-upload
- automation-abuse
language: en
raw_sha256: bc31a2bb7aeddfc65cfb69fabac66844734a6be930957d708680047ad32ced71
text_sha256: 3c0e9e3f2e6af04b67fbd6f6e600beb130507198da77cc0e09f9bb271d4e9f29
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Odoo: Get your Content Type right, or else!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-24_odoo-get-your-content-type-right-or-else.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, sso, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `bc31a2bb7aeddfc65cfb69fabac66844734a6be930957d708680047ad32ced71`
- Text SHA256: `3c0e9e3f2e6af04b67fbd6f6e600beb130507198da77cc0e09f9bb271d4e9f29`


## Content

---
title: "Odoo: Get your Content Type right, or else!"
page_title: "Odoo: Get your Content Type right, or else! | Sonar"
url: "https://www.sonarsource.com/blog/odoo-get-your-content-type-right-or-else/"
final_url: "https://www.sonarsource.com/blog/odoo-get-your-content-type-right-or-else/"
authors: ["Dennis Brinkrolf (@DBrinkrolf)", "Thomas Chauchefoin (@swapgs)"]
programs: ["Odoo"]
bugs: ["XSS", "Security code review"]
publication_date: "2023-04-24"
added_date: "2023-04-28"
source: "pentester.land/writeups.json"
original_index: 1226
---

## TL;DR overview

  * Odoo's content-type handling contains a vulnerability where improper or absent MIME type enforcement allows browsers to sniff and execute malicious content uploaded by attackers, leading to cross-site scripting.
  * The root cause is a mismatch between the content type set by the server and the type expected by the browser—exploiting content sniffing behavior to execute HTML or JavaScript from files that should be treated as binary.
  * The fix requires explicitly setting correct Content-Type headers for all file downloads and uploads, adding X-Content-Type-Options: nosniff, and validating MIME types server-side before serving user-uploaded content.
  * This class of vulnerability is common in web applications with file upload functionality; SonarQube detects missing or incorrect content-type headers as security hotspots.

As a web developer, do you _really_ know what content types are? Sure, something like `text/html` should ring a bell, but are you also aware that getting them wrong can lead to security vulnerabilities in your application? 

In this blog post, we will first give you a recap of what content types are and what they are used for. We will then show how important it is to get them right in your code by explaining how a small mistake led to a Cross-Site Scripting vulnerability in Odoo, a popular open-source business suite written in Python. Odoo has features for many business-critical areas, such as e-commerce, billing, or CRM, making it an interesting target for threat actors.

The vulnerability is tracked as CVE-2023-1434 and is caused by an incorrect content type being set on an API endpoint. Attackers could abuse it by crafting a malicious link that allows them to impersonate any victim on a vulnerable Odoo instance that clicks that link. If the victim has high privileges, attackers may be able to exfiltrate important business data. This bug is exploitable in the default configuration of Odoo; no addon is required. 

Odoo maintainers addressed this vulnerability on December 23, 2022, and the fix is already part of the 16.0 release. 

(If you are already up-to-speed on content types, feel free to jump to _Diving into CVE-2023-1434_!)

## Content types?

The content type, also known as MIME type, is a crucial piece of information for web browsers. They need this information to display the server's response the right way. 

It starts in the request, where the browser sets the `Accept` header to tell the server what acceptable types are. For instance, when your browser requests a CSS stylesheet, it will likely attach `Accept: text/css`. Your browser could also feel adventurous and send `*/*` (meaning, any type!), or send multiple values, each with a weight like `q=0.1,` to give the server a choice. 

The server can then use this value to decide on which `Content-Type` header to attach to the response. It can also use values from the request path (i.e., extensions) to take this decision or simply ignore it. 

### Content Sniffing

In cases where the content type of a resource is not explicitly stated by one of the two sides, Content Sniffing usually kicks in. It means that an application has to decide on its own which type of content some unknown blob of data is, and yes, it is as likely to have the wrong result as it sounds.

**Server-side Content Sniffing**

It can happen server-side, by a reverse proxy or the application itself, when the developer specifies no content type. This process is error-prone and likely leads to unintended results. There are several documented examples of this going wrong. For instance, [Simon Scannell exploited it in CVE-2021-39249 on Invision Power Board](https://ssd-disclosure.com/ssd-advisory-ip-board-stored-xss-to-rce-chain/), where he could upload attachment files without extensions. However, by default, the Apache HTTP server will attach `text/html` to files without extensions, letting Simon upload files later distributed as HTML documents.

We also highly recommend reading [Server-Side MIME Sniff Caused by Go Language Project Containerization](https://tttang-com.translate.goog/archive/1880/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) by @RuiShang9. 

The Go standard library has a [very limited set](https://go.dev/src/mime/type.go) of file extensions and their associated MIME types. In minimalistic environments of containers, i.e. based on [`alpine`](https://hub.docker.com/_/alpine), the system may not provide enough additional type definitions. 

In this context, it is then likely that attackers could upload static files whose extension is allowed by the application but unknown by the Go server-side MIME sniffing feature. The file may then be served as `text/html` and introduces a Stored Cross-Site Scripting vulnerability. 

**Client-side Content Sniffing**

It can also happen client-side, in the user's browser, when the response doesn't contain a `Content-Type` header or an invalid one. The MIME sniffing algorithm is documented in a [WHATWG living document](https://mimesniff.spec.whatwg.org/#identifying-a-resource-with-an-unknown-mime-type) and lists byte patterns to look for and the computed MIME type to attach if they are found in the response. For instance, the presence of `<!DOCTYPE HTML` or `<HTML` along with a character closing the tags raises `text/html`, `%PDF-` raises `application/pdf,` and so on. 

[Yaniv Nizry identified a quirk in Apache's `mod_mime` module](https://twitter.com/YNizry/status/1582733545759330306), where files with extensions but an empty (`.jpg`) or dot name (`…jpg)` would be served without a content type. The browser would then "sniff" the content and could be tricked into rendering them as HTML documents. 

With these examples, it is clear that Content Sniffing is here to accommodate users and always tries to show them valid pages in their browsers–not for security. 

We even developed a rule as part of our Code Quality offering to remember telling browsers _not_ to rely on it: Allowing browsers to sniff MIME types is security-sensitive. We suggest addressing it by setting the header `X-Content-Type-Options` to `nosniff` in all responses to tell browsers not to attempt content sniffing on the resources. It won't prevent cases where the content type is incorrectly stated. 

### What could go wrong? 

Let's take the example of an image returned with the wrong content type information, for instance, `text/html`. The browser displays gibberish–the ASCII representation of the file's bytes:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3b1dc5da-e41c-4123-9c27-c95c5504be23/odoo-1.png)

But that also means that if there's any HTML tag in this file, they will be rendered by the browser. For instance, below, we have the result of the emoji in a `<h1>:`

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7e0da2ac-a4d3-4554-afe9-964a7fb71dbe/odoo-2.png)

Attackers could replace this tag with `<script>` to include arbitrary JavaScript code instead. Executing such code in the victim's browser allows impersonating them on the same origin (as in "Same-Origin Policy"). 

Now that we have a good understanding of content types and why they can be security-relevant, we can look into a vulnerability we found in Odoo.

## Diving into CVE-2023-1434

As part of the advanced features for developers, Odoo users can enable profiling for their session to identify potential performance bottlenecks in their application. They can later visualize flame graphs of their traces with a [speedscope](https://github.com/jlfwong/speedscope) instance:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2567a841-ef32-41d4-9cf3-9afcdbfdc0a4/odoo-3.png)

One of the ways to interact with the profiler is through an API handler, like `/web/set_profiling/`. At `[1]`, the decorator exposes it to `/web/set_profiling` without authentication, at `[2]` it creates the variable state with a call to `set_profiling()`, and then at `[3`] it returns a JSON-encoded output of this variable:

Copy to clipboard
  
  
  class Profiling(Controller):
  
  @route('/web/set_profiling', type='http', auth='public', sitemap=False) # [1]
  def profile(self, profile=None, collectors=None, **params):
  # [...]
  try:
  state = request.env['ir.profile'].set_profiling(profile, collectors=collectors, params=params) # [2]
  return Response(json.dumps(state)) # [3]
  except UserError as e:
  return Response(response='error: %s' % e, status=500)

Digging into Odoo's `Response` implementation, we can see that it directly inherits from werkzeug's `Response`, which is the underlying web framework:

Copy to clipboard
  
  
  class Response(werkzeug.wrappers.Response):
  """
  Outgoing HTTP response with body, status, headers and qweb support.
  [...]
  Also exposes all the attributes and methods of
  :class:`werkzeug.wrappers.Response`.
  """
  default_mimetype = 'text/html'

The attribute `default_mimetype` is set to `text/html`–very interesting! Indeed, werkzeug's default MIME type is originally set to `text/plain` if the developer didn't override it in the constructor:

Copy to clipboard
  
  
  class BaseResponse(object):
  # [...]
  #: the charset of the response.
  charset = "utf-8"
  
  #: the default status if none is provided.
  default_status = 200
  
  #: the default mimetype if none is provided.
  default_mimetype = "text/plain"

We are now in a situation where we are returning JSON data with a `text/html` content type. But do we control parts of that data? 

The method `set_profiling()` is defined in `ir_profile.py`. In the snippet below, at `[1]`, `[2]`, and `[3]`, `request.session` is populated with the method parameters `profile`, `collectors,` and `params`. These values are then returned in a `dict`:

Copy to clipboard
  
  
  @api.model
  def set_profiling(self, profile=None, collectors=None, params=None):
  # [...]
  if profile:
  # [...]
  elif profile is not None:
  # [1]
  request.session.profile_session = None 
  
  if collectors is not None:
  # [2]
  request.session.profile_collectors = collectors
  
  if params is not None:
  # [3]
  request.session.profile_params = params
  
  return {
  'session': request.session.profile_session,
  'collectors': request.session.profile_collectors,
  'params': request.session.profile_params,
  }

So yes, we have full control over them. URL parameters like `profile=0`, `collectors=<script>alert(document.domain)</script>` is enough to trigger the vulnerability. The resulting DOM, as seen by the client's browser, is as follows: 

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2d415ddc-c776-46c7-a7fd-dc492424467d/odoo-5.png)

Note that, while the server does not send them, the browser added the `html`, `head`, and `body` tags around the actual data because the server signaled that the response is an HTML page! Accessing the page is enough to trigger the JavaScript code:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/03a5a320-35ec-4d7c-90f7-32079b96b3f2/odoo-4.png)

### Remediating Cross-Site Scripting Vulnerabilities

In the case of Cross-Site Scripting vulnerabilities, we believe that the best way of addressing these risks is at the very end of the chain: when displaying the data. Special characters must be made ineffective, whether by escaping or encoding them, but always depending on the context in which the data is injected. 

For instance, JavaScript string literals and HTML support different escaping methods, and using the wrong one will likely introduce a Cross-Site Scripting vulnerability. Always make sure to know the context and use the most appropriate function. 

The case of Odoo is a bit unusual. Common solutions would have been to implement a strict validation of the parameters or convert tags into HTML entities in the JSON string. Still, none of these should be considered satisfactory because the root cause boils down to this wrong content type: it must be addressed by setting the right content type on the API endpoint. 

We also recommend investing in a strong [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), which will not prevent vulnerabilities but make them harder or impossible to exploit. It always takes time and a few iterations to get it right, so the sooner, the better! 

###  

### Patching CVE-2023-1434

Odoo maintainers addressed the vulnerability with [ec8dd1a](https://github.com/odoo/odoo/commit/ec8dd1ad7731be32d43a12435def7c720cdcad32) by adding an explicit content type, `application/json`, on this endpoint. 

If an `UserError` exception is raised, the exception message is prefixed with `error:`; this is not a valid JSON document. In that specific case, the maintainers set the content type to `text/plain` to tell browsers not to render it. 

Copy to clipboard
  
  
  diff --git a/addons/web/controllers/profiling.py b/addons/web/controllers/profiling.py
  index b320ee0cfba4e..640f8b4e210fc 100644
  --- a/addons/web/controllers/profiling.py
  +++ b/addons/web/controllers/profiling.py
  @@ -16,9 +16,9 @@ def profile(self, profile=None, collectors=None, **params):
  profile = profile and profile != '0'
  try:
  state = request.env['ir.profile'].set_profiling(profile, collectors=collectors, params=params)
  -  return json.dumps(state)
  +  return Response(json.dumps(state), mimetype='application/json')
  except UserError as e:
  -  return Response(response='error: %s' % e, status=500)
  +  return Response(response='error: %s' % e, status=500, mimetype='text/plain')
  
  @route(['/web/speedscope', '/web/speedscope/<model("ir.profile"):profile>'], type='http', sitemap=False, auth='user')
  def speedscope(self, profile=None):

_(We will update this publication with a link to the official advisory as soon it is published)._

## Timeline

**Date**| **Action**  
---|---  
2022-12-22| We report the vulnerability to the vendor.  
2022-12-23| The vulnerability is fixed in [ec8dd1a](https://github.com/odoo/odoo/commit/ec8dd1ad7731be32d43a12435def7c720cdcad32).  
2022-12-25| Vendor informs us that the SaaS platform is not vulnerable and that a fix is under validation.  
  
## Summary

In short, getting the content type right is crucial for web developers to ensure the security of their applications. Client-side vulnerabilities can have a significant impact on the security of an application and should not be ignored. 

We would like to thank Olivier Dony of Odoo S.A. for promptly deploying a patch and for their very effective communication.

Enjoy all things Python, and want more? [Register now](https://sonarsource.zoom.us/webinar/register/1016814727581/WN_9WmyrHN7QrKxkZ1fTEbmpw#/registration) for our upcoming webinar Code Quality for your Python projects, with Nafiul Islam - Wednesday, May 10th - 5 PM CEST / 10 AM CDT.

## Related Blog Posts

  * [It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS](https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/)
  * [OpenEMR - Remote Code Execution in your Healthcare System](https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/)
  * [Ghost CMS 4.3.2 - Cross-Origin Admin Takeover](https://www.sonarsource.com/blog/ghost-admin-takeover/)

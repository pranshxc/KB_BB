---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-04_the-12000-intersection-between-clickjacking-xss-and-denial-of-service.md
original_filename: 2018-07-04_the-12000-intersection-between-clickjacking-xss-and-denial-of-service.md
title: The $12,000 Intersection between Clickjacking, XSS, and Denial of Service
category: documents
detected_topics:
- xss
- command-injection
- mfa
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- clickjacking
- api-security
language: en
raw_sha256: 753f73ce71e42ed2fe2f82115063ea5389f92d650ee5646c202027a0cfd1a0f9
text_sha256: 6f9efa6412735ac5388b9fa975f586329e77409c496f589531b97feb1bf4a3bc
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# The $12,000 Intersection between Clickjacking, XSS, and Denial of Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-04_the-12000-intersection-between-clickjacking-xss-and-denial-of-service.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, clickjacking, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `753f73ce71e42ed2fe2f82115063ea5389f92d650ee5646c202027a0cfd1a0f9`
- Text SHA256: `6f9efa6412735ac5388b9fa975f586329e77409c496f589531b97feb1bf4a3bc`


## Content

---
title: "The $12,000 Intersection between Clickjacking, XSS, and Denial of Service"
url: "https://samcurry.net/the-12000-intersection-between-clickjacking-xss-and-denial-of-service/"
final_url: "https://samcurry.net/the-12000-intersection-between-clickjacking-xss-and-denial-of-service"
authors: ["Sam Curry (@samwcyo)"]
programs: ["Bustabit"]
bugs: ["Clickjacking", "XSS", "DoS"]
bounty: "12,000"
publication_date: "2018-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5819
---

[Back to blog](/)

# The $12,000 Intersection between Clickjacking, XSS, and Denial of Service

July 4, 2018

![The $12,000 Intersection between Clickjacking, XSS, and Denial of Service](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Faabd.png&w=3840&q=75)

One of the more challenging tasks in web app pentesting is approaching an application that has limited interaction. It's very easy to give up after trying every common method to exploit something, but putting in the time to understand an application is often rewarding and beneficial to ones personal growth as a hacker.

### Introduction

The specific application that I've been targeting over the last few weeks is a bitcoin gambling website where a stock will progressively rise over time. The gambler decides the amount of money they would like to put in and a multiplier to payout at. As the multiplier goes up, they have an option to click a button and receive whatever returns they had made it to. Each time the multiplier goes up, there is a chance the stock will "bust" and all of the investment will be lost.

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fbustabit-1024x560.png&w=3840&q=75)

The application had a few really interesting functionalities, but the one I really wanted to spend time on was the ability to chat with other users.

### "Digging Deep" into Chat: Denial of Service against User Clients - $2,000 bounty

One of the things that I had identified after scrolling through the chat messages was that the service auto-created hyperlinks when a link was pasted. This was interesting since the website made a really special HTML element that is oftentimes dangerously implemented so that an attacker could do one of the following...
  
  
  <a href=":1">:2</a>
  

  1. `" onmouseover=alert(1) a="` \- this would fire at `:1` if not sanitized properly
  2. `javascript:alert(1)` \- this would fire at `:1` if not sanitized properly
  3. `<script>alert(1)</script>` \- this would fire at `:2` if not sanitized properly

Sadly, none of these worked.

It appeared that the service did not hyperlink the external endpoints directly, but modified it to the following endpoint where `www.google.com` would be an example posted URL...
  
  
  https://www.bustabit.com/external?url=https://www.google.com
  

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fexternal-1024x406.png&w=3840&q=75)

...the result of posting a URL...

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Flolz.png&w=3840&q=75)

... the page that you're taken to after clicking said URL.

#### What about pasting links to the same domain?

We'll come back to the above endpoint shortly, but something interesting about the external forwarding service was that it did not forward URLs for the same domain.

There was some sort of detection mechanism for determining if a URL was from the same site, e.g. `www.bustabit.com/a` would not trigger the domain to be modified to `www.bustabit.com/external?url=www.bustabit.com/a` since it was on the same domain.

Here is the generated HTML for `www.bustabit.com/a`...
  
  
  <a href="/a">www.bustabit.com/a</a>
  

... compared to the generated HTML for `www.google.com/a`...
  
  
  <a href="https://www.bustabit.com/external?url=https://www.google.com/a">https://www.google.com/a</a>
  

The really cool part about the above URL is that it's not hyperlinking the full domain, but simply the endpoint. What an attacker could potentially do here is abuse the functionality of double slashes for external resources using a payload like...
  
  
  https://www.bustabit.com//attacker.com/hacked
  

... to create ...
  
  
  <a href="//attacker.com/hacked">www.bustabit.com//attacker.com/hacked</a>
  

This worked!

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fhacked.png&w=3840&q=75)

The following HTML is the exact same hyperlink above: [//hacker.com/ ](//hacker.com/) Notice how it takes you to an external resource and not an endpoint on `samcurry.net`? More information on this is available here: <http://www.ietf.org/rfc/rfc2396.txt>.

This _WOULD'VE WORKED_ as a bypass to the link filter, but this was an all-JavaScript application that was doing an `onclick` event to load the endpoint in the same tab since the domain was the exact same and it didn't have to refresh whatsoever. Damn!

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Furgh.png&w=3840&q=75)

It's incredibly frustrating seeing your PoC HTML written in the client, hovering over a hyperlink with a link to `whywontyouload.com`, then clicking it and nothing happening. After investigating this for a bit I got really annoyed and worked to identify what exactly was happening when I clicked the URL.

#### Some time later...

After a long time endlessly spamming random payloads and attempting to find something that would take a user to an external domain, the website went gray.

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Funnamed-1024x485.png&w=3840&q=75)

It turns out that I had actually broken my client by sending `https://www.bustabit.com/%0t`.

The JavaScript didn't know how to handle this since the URL encoding for `%0t` did not decode to anything and simply failed the entire application (see [here](https://www.w3schools.com/tags/ref_urlencode.asp) for more information regarding correct URL encoding).

After refreshing the page I was amazed: my client was still broken.

It turns out that the application pushed all hyperlinks to a JavaScript function automatically, and if there was a failed URL (e.g. had `%0t`), the application would crash.

#### How could this be weaponized?

An attacker could direct message anyone placing a bet (this is public information - all live bets and wagers are in the upper right box) and it would crash the victims client, making them unable to cash out their bet. Additionally, an attacker could simply post a bad link to the main chat channel and disconnect everyone, making the game unplayable for a long period of time or cancelling the ability to interact for all users.

### "Digging Deep" into Chat: XSS plus Click Jacking - $10,000 bounty

Remember that external endpoint I had posted above?

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Flolz.png&w=3840&q=75)

It turns out that you could simply pass it a JavaScript URI and an attacker could execute JavaScript within the context of the application.

These bugs always suck because they require you to convince someone to click something.

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fxsspoc-1024x430.png&w=3840&q=75)

One of the things you can do to make these PoCs better is to simply check if the website can be put inside of an `<iframe>` tag. If this is possible, then it would additionally be possible to create a clickjacking PoC using something like [Samy Kamkar's quick jacking PoC generation tool](http://samy.pl/quickjack/).

It turns out that the service was able to be placed inside of an `<iframe>`. With this, I generated an example PoC using that awesome little snippet of `Click here to continue`.

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fexample-1024x250.png&w=3840&q=75)

Which, in a real world scenario, could look a little something like this...

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fpocpoc.png&w=3840&q=75)

So, what can you do with XSS?

![](/_next/image?url=%2Fimages%2Fthe-12000-intersection-between-clickjacking-xss-and-denial-of-service%2Fbet.png&w=3840&q=75)

Session takeover! It turns out that the web sockets session is stored within the local storage of your browser. An attacker could abuse the XSS to force the victim into making a call to an external service with their session information. An attacker could authenticate to the application by modifying their own secrets to the victims and authenticating to the service.

### Conclusion

More often than not I see people approaching bug bounty with a very "spray everything lightly" methodology. This will probably work eventually, but the thing you have to keep in mind is that  _every one_ can download automated tools like aquatone or dirsearch. If you want to find vulnerabilities on things where there are thousands of other researchers, it is often your best bet to dig deep on certain functionalities.

If you have any questions feel free to use the contact form above or simply [follow me on Twitter](https://twitter.com/samwcyo)!

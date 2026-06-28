---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-09_dont-reply-a-clever-phishing-method-in-apples-mail-app.md
original_filename: 2021-12-09_dont-reply-a-clever-phishing-method-in-apples-mail-app.md
title: 'Don’t Reply: A Clever Phishing Method In Apple’s Mail App'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 915860e8b8f2967aa846e9d8046dc4f18986f4e7e95f3808286530ef962ff506
text_sha256: 4e2eb718a4fbb501dd33963a44f61c178a7ad776d432667820e7a18ad02b2ed6
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Don’t Reply: A Clever Phishing Method In Apple’s Mail App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-09_dont-reply-a-clever-phishing-method-in-apples-mail-app.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `915860e8b8f2967aa846e9d8046dc4f18986f4e7e95f3808286530ef962ff506`
- Text SHA256: `4e2eb718a4fbb501dd33963a44f61c178a7ad776d432667820e7a18ad02b2ed6`


## Content

---
title: "Don’t Reply: A Clever Phishing Method In Apple’s Mail App"
page_title: "Don’t Reply: A Clever Phishing Method In Apple's Mail App - Jon's Personal Blog"
url: "https://jonbottarini.com/2021/12/09/dont-reply-a-clever-phishing-method-in-apples-mail-app/"
final_url: "https://jonbottarini.com/2021/12/09/dont-reply-a-clever-phishing-method-in-apples-mail-app/"
authors: ["Jon Bottarini (@jon_bottarini)"]
programs: ["Apple"]
bugs: ["Phishing"]
bounty: "5,000"
publication_date: "2021-12-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3097
---

About four or five years ago, friend and fellow bug bounty hunter [Sam Curry](https://twitter.com/samwcyo) asked if I had “ _ever thought about what was possible to load inside an <img> tag, besides an image_“. What a peculiar question. I didn’t really understand what he was asking, and I assume Sam got bored of me guessing the wrong answers, so he sent a simple payload that looked like this:
  
  
  <img src=https://www.jonbottarini.com/pocs/restricted.php></img>

At the surface, this appears to be a normal HTML <img> element, until you look a bit closer and realize that the `src=` parameter is not pointing to an image at all, but rather a webpage ending in .php. If you navigate to this page directly, you’ll be prompted with something that looks like this:

![](https://jonbottarini.com/wp-content/uploads/2021/04/Screen-Shot-2021-04-20-at-9.32.36-PM-1024x643.png)

What you’re looking at is an implementation of [WWW-Authenticate](https://tools.ietf.org/html/rfc7235#section-4.1). In 2017, if you were to embed this <img> payload in an HTML editor on a 3rd party website, nearly anyone who viewed the page with the rendered <img> tag would see an authentication prompt, asking you to sign in to my site. It looked like this:

![A prompt asking users on an AirBnb community website to login to my website](https://jonbottarini.com/wp-content/uploads/2021/10/airbbnb-Enter-login-details-to-attackers-server-1024x589.png)

Simply incredible. I don’t think Sam realized at the time what he was sitting on in the world of bug bounty – this was essentially a lazy way to phish users on forums, help centers, etc – anywhere that you could enter an image tag. It was unique because in situations where you were allowed to insert an <img> tag but not able to pop an XSS payload (due to CSP or other protections in place), rarely did an application prevent you from loading an external “image” that was really my malicious WWW-Authenticate page. Remember: this was 2017, a lot has changed since then. 

After sharing this revelation with Sam, we reported instances of sites vulnerable this issue to a few bug bounty programs, and it was largely hit or miss. Some programs (Yahoo!, if I remember correctly, back before they rebranded their program to Oath, and then to Verizon Media¹) paid $1,000 _for each instance_ of the issue – other programs didn’t pay anything at all, and stated that it was a browser issue. This is understandable – in a way, this issue could be _fix_ ed by the browser. The Chrome team [decided to fix this ](https://bugs.chromium.org/p/chromium/issues/detail?id=174179)outright back in 2013 by preventing cross-origin authentication prompts to image resources. Sam [petitioned Mozilla](https://bugzilla.mozilla.org/show_bug.cgi?id=1357835) to do the same in 2017, which they (begrudgingly) implemented the change to disallow loading external WWW-Authenticate prompts via image somewhere around Firefox Version 57. Apple never responded to us when we reached out to inform them that Safari was the last (major) browser to suffer from this.

## The Problem in Apple Mail

I got bored with the 50/50 odds of getting a bounty through the web programs we were reporting to. A few months passed and I had an epiphany – in the form of a spam email. In short, an email evaded my spam filter because the email had no content besides a photo. Just a big, massive JPG image. This led to an idea – **what if I sent a “photo” that was behind a WWW-Authenticate response header in an email?** What type of prompt would the recipient see? Would they see any anything at all? 

It doesn’t work. Simply put, I am not sure why it doesn’t work when the recipient _receives_ the email – but the prompt **does appear when _replying_ to the email**. When you reply to an email with that <img> payload I mentioned above, the user is presented with this prompt, which asks them to enter their name and password “to view this page”:

![](https://jonbottarini.com/wp-content/uploads/2021/10/0-2-1024x508.png)

This prompt poses a two-fold problem. This first being that users are already familiar with entering their username and password in ambiguous and confusing prompts on Apple devices – [Apple keychain](https://apple.stackexchange.com/questions/124591/osx-is-repeatedly-asking-for-login-keychain-password) being a major offender. 

But this is not a keychain prompt – when a user enters their username and password in this prompt, **their credentials are sent directly to my server**. 

The second problem is that it’s possible to customize the message displayed underneath the URL – in the example above, I put “You need to enter your Apple Mail password again!”. This is made possible through the realm directive:

> **realm= <realm>**
> 
> A string describing a protected area. A realm allows a server to partition up the areas it protects (if supported by a scheme that allows such partitioning), and informs users about which particular username/password are required. If no realm is specified, clients often display a formatted hostname instead.
> 
> [Mozilla developer portal](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#directives)

All in all – you get a very clever Apple Mail phishing method. Now – a savvy person would realize that “jonbottarini.com” has nothing to do with Apple, and would probably be skeptical of entering a username and password in the prompt – but official-sounding Apple domain names are cheap! 

![](https://jonbottarini.com/wp-content/uploads/2021/10/0-1-1024x707.png)

This issue affected versions of Apple Mail from macOS High Sierra 10.13 to macOS Big Sur 11.2. Yes, you read that right – it took multiple operating systems and _four_ years to fix this issue completely. But before you get out the pitchforks – it’s not entirely Apple’s fault it took so long – there was a two year period where both Apple and myself thought the issue was fixed – when it really wasn’t. 

## Timeline: 

  * Sometime mid to late 2017 (email comms are a bit messy here) – reported issue to Apple 
  * **Oct 2017** – Apple can’t reproduce the issue, I reply with additional info 
  * **Nov 2017** – More back and forth, explaining to Apple that the issue only occurs when replying/forwarding the email 
  * **Sometime in 2018** – Apple states this issue is not eligible for a CVE 🙁 
  * **July 2018** – Apple states they fixed the issue in macOS High Sierra 10.13 and macOS High Sierra 10.13.2 
  * **May 2020** – I start to write this blog post, but when I test the old proof of concepts, I notice that the payload is not fully fixed on macOS Catalina 10.15.4 and I am still getting the prompt. Replied back to Apple with proof that the issue still exists. 
  * **October 2020** – Apple states they have fixed the issue again – I find a bypass pretty quickly (by sending a email with an embedded image loaded inside a pre-made feature in Apple mail called “email templates”). Apple continues work on the remediation. 
  * **April 2021** – I follow up asking for a status update. Apple states the issue has been resolved in macOS Big Sur 11.2
  * **August 2021** – Apple sends me an email out of the blue stating that the issue is eligible for a $5,000 bounty (w0w!) 
  * **December** **2021** – Bounty paid + this writeup is disclosed. 

¹ – At time of writing, Verizon Media has rebranded back to Yahoo. We have come full circle.  

_Very special thanks to Sam Curry (@samwcyo) and Tanner (@itscachemoney) for reviewing a draft of this post._

[Follow me on Twitter](https://twitter.com/jon_bottarini) to stay up to date with my latest bugs + bug bounty finds.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_using-burp-suite-match-and-replace-settings-to-escalate-your-user-privileges-and.md
original_filename: 2019-06-17_using-burp-suite-match-and-replace-settings-to-escalate-your-user-privileges-and.md
title: Using Burp Suite match and replace settings to escalate your user privileges
  and find hidden features
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: f817038db149311395fbdf39bac0749e8fbece82275b2d1d84ffaef8edf5a6d0
text_sha256: 0402dac7b9b43adb39df226b9cd1ed3a951cc472ec6b1ef5da562a85bbccee70
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Using Burp Suite match and replace settings to escalate your user privileges and find hidden features

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_using-burp-suite-match-and-replace-settings-to-escalate-your-user-privileges-and.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f817038db149311395fbdf39bac0749e8fbece82275b2d1d84ffaef8edf5a6d0`
- Text SHA256: `0402dac7b9b43adb39df226b9cd1ed3a951cc472ec6b1ef5da562a85bbccee70`


## Content

---
title: "Using Burp Suite match and replace settings to escalate your user privileges and find hidden features"
page_title: "Using Burp Suite match and replace settings to escalate your user privileges and find hidden features - Jon's Personal Blog"
url: "https://www.jonbottarini.com/2019/06/17/using-burp-suite-match-and-replace-settings-to-escalate-your-user-privileges-and-find-hidden-features/"
final_url: "https://www.jonbottarini.com/2019/06/17/using-burp-suite-match-and-replace-settings-to-escalate-your-user-privileges-and-find-hidden-features/"
authors: ["Jon Bottarini (@jon_bottarini)"]
programs: ["New Relic"]
bugs: ["Client-side enforcement of server-side security"]
bounty: "500"
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5204
---

On May 14th, Lew Cirne, the CEO of New Relic, announced a new platform called New Relic One. The platform, featuring a fresh new design and better data visualizations, came as a surprise to investors and New Relic users alike. 

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/nr1-1024x372.png)

But it did not come as a surprise to me, for I had found out about it months prior, using a common trick that I’ve used multiple times in other bug bounty programs to access unreleased beta and admin features; the Burp Suite match and replace rule. 

The concept is simple: By changing the server response body from “false” to “true” (I cheekily refer to this as the FALSE2TRUE trick, because everything has to have a catchy name nowadays 😏) – you open up much more on the client side that might previously be hidden or unaccessible, and that’s exactly what happened when I found out about New Relic One. This is not a secret, and has been a method for a long time.

> Bug Bounties are a race in most cases. Quick tip – to speed stuff up to find hidden functionality, endpoints without having to scrape through JS. Match & Replace in Burp false to true. Some cases functionality breaks, others it doesnt. You just saved a bunch of time 🙂
> 
> — BugBountyHQ (@BugBountyHQ) [May 24, 2019](https://twitter.com/BugBountyHQ/status/1132047688139137025?ref_src=twsrc%5Etfw)

For those of you new to using the Burp Suite match and replace rule, [this article](https://matthewsetter.com/write-burp-suite-match-and-replace-rules/) goes deeper into where to find it in Burp and how to use it – but it lives under the Proxy settings in Options:

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-11.37.03-AM-1024x779.png)

The match and replace rule goes well beyond just changing false responses to true – it can also be used for privilege escalation to change your user permissions from “User” to “Admin”. Let’s use the following example: 

Imagine the server performs a check of the permissions of the user with the current session. The request to the server might look something like this:
  
  
  POST /api/getUserDetails HTTP/1.1
  Host: myserver.jonbottarini.com
  Cookie: mycookies
  
  {"user":"123"}

And the response might look like this: 
  
  
  HTTP/1.1 200 OK
  
  {"data":{"currentUser":{"userData":[
  {"userLevel":READONLY,"subscriptionLevel":"BASIC"}
  ]}}}

In the response, the client operates under the assumption that the user is in “READONLY” mode, and has a “BASIC” subscription. If we add a match and replace rule to change the “userLevel”:READONLY response to “userLevel”:ADMIN, we can trick the client to display UI elements that are meant only for Administrators:

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-12.21.14-PM.png)

We can go one step further and display UI elements that are meant only for a “Professional” level subscription as well: 

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-11.52.57-AM.png)

If we were to add the match/replace rules above, the response to the client will now look like this:
  
  
  HTTP/1.1 200 OK
  
  {"data":{"currentUser":{"userData":[{"userLevel":ADMIN,"subscriptionLevel":"PROFESSIONAL"}]}}}

[@daeken](https://twitter.com/daeken) has another nifty trick with the Burp match/replace rule: injecting payloads into forms instead of typing out the entire payload:

https://twitter.com/daeken/status/1110031661994070016 

**Back to New Relic**. I was using the _FALSE2TRUE_ trick when I realized that there was a feature flag on my account which was always returning **false**. By simply changing this response to **true** using Burp match/replace rule, I noticed that there was additional UI elements that appeared on the page. 

This is the New Relic landing page when logging in without FALSE2TRUE: 

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-12.31.37-PM-1024x646.png)

Now, when using the FALSE2TRUE trick, changing all “false” values to “true”:

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-12.43.06-PM-1024x646.png)

Bug found! 

![](https://www.jonbottarini.com/wp-content/uploads/2019/06/Screen-Shot-2019-06-16-at-12.33.55-PM-1024x451.png)

The Burp match and replace rule gave me access to a completely unreleased feature with a ton of new functionality, where I found other bugs as well, prior to the public release. 

**A word of warning** : Be careful when using the FALSE2TRICK on big websites, because you can _really_ mess up your session, or even your entire account. 

I’m curious how you use the match/replace tool in your Burp projects – leave a comment below or [ping me on Twitter](https://twitter.com/jon_bottarini) if you would like to share. If it’s a really good tip, I’ll put it in this post so others can learn! 

Until next time 👋

_(The New Relic security team reviewed this post in full before it was published and have agreed to let me use one of my reports as an example. I am especially grateful for the New Relic team to be so open and accepting of using their program and bugs I’ve found in examples on my blog)._

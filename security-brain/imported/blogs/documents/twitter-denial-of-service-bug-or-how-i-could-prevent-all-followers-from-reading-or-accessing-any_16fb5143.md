---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-25_twitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-.md
original_filename: 2019-03-25_twitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-.md
title: Twitter Denial of Service bug or How i could prevent all followers from reading
  or accessing literally ANY tweets!
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 16fb514339f2f03df4b323cbec183f9579e0e5998646606e40df68beacce4298
text_sha256: f3812a0f4d725d5aa87fff5a100442edab4eaf3980cab8f9846810f7a9d242ab
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Twitter Denial of Service bug or How i could prevent all followers from reading or accessing literally ANY tweets!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-25_twitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `16fb514339f2f03df4b323cbec183f9579e0e5998646606e40df68beacce4298`
- Text SHA256: `f3812a0f4d725d5aa87fff5a100442edab4eaf3980cab8f9846810f7a9d242ab`


## Content

---
title: "Twitter Denial of Service bug or How i could prevent all followers from reading or accessing literally ANY tweets!"
page_title: "Twitter Denial of Service bug or How i could prevent all followers from reading or accessing literally ANY tweets! – Seekurity"
url: "https://www.seekurity.com/blog/general/twitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets/"
final_url: "https://seekurity.com/blog/2019/03/25/seif-elsallamy/general/twitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets"
authors: ["Seif Elsallamy (@seifelsallamy)"]
programs: ["Twitter"]
bugs: ["DoS"]
bounty: "1,120"
publication_date: "2019-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5344
---

Hi Everyone,

It’s Seif Elsallamy here, I have been away for a while, I really miss doing the stuff i’m good at, Yes breaking things, here take a look at [my old posts](https://www.seekurity.com/blog/author/seif-elsallamy/).

I’m back again to all of you with a cool denial of service bug I’ve discovered in Twitter but before diving in the technical details let us go through some terms to have a full understanding of what we are talking about here.

What is [(DoS) Denial of Service](https://www.owasp.org/index.php/Denial_of_Service)?

The Denial of Service (DoS) attack is focused on making a resource (site, application, server) unavailable for the purpose it was designed.

I was trying to find [XSS](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\)) on Twitter mobile site but my plans didn’t work out, After I logged in, I opened a conversation with my self and start sending/fuzzing various payloads.

Here are some notes of the behavior i faced during the fuzz:

  1. I noticed that when you’re sending any link on Twitter, Twitter is generating a link via its own link shortener service which uses the well known “t.co” domain then redirecting you to the link of the final destination you already sent, that’s actually normal it’s just tracking links, checking for unwanted content or filtration and prevents [open redirection](https://whatis.techtarget.com/definition/open-redirect) something similar to Linkshim protection system that Facebook uses. However when you’re sending a link (on Twitter’s mobile site) belongs to one of the following Twitter domains “twitter.com” or “mobile.twitter.com” It doesn’t generate the above mentioned “t.co” links hmmm!
  2. That’s quite interesting because Twitter like many modern websites doesn’t re-load pages but it only loads the javascript resources via either AJAX or XMLHttpRequests.What does that mean? When you’re trying to access https://mobile.twitter.com/notifications from outside Twitter It’s actually loads a page but accessing the same URL from inside Twitter will also access the same page but by just loading some javascript (without requesting the actual page again and again)

So my theory was to find an XSS on Twitter by loading a URL from inside twitter via sending a message with a URL belongs to twitter itself and contains variables.

### In other words (just for illustrating)

going to `https://mobile.twitter.com/?'"><img/src=x/onerror=alert(1)>'''From outside Twitter won’t trigger an XSS, but from inside Twitter it might trigger an XSS because it loads in a different way.

One of the XSS payloads that I sent had the following Unicode character `"%u003e"` it caused an error I can no longer see any messages on the conversation!! hmmm so interesting BUT WHY?!

This string is a [hexadecimal unicode](https://www.lsa.umich.edu/german/hmr/schreiben/umlaute/unicode.html) `%u003e` means `>` but Twitter couldn’t handle/load it, So I tried a URL contains `%xx`eg. `https://mobile.twitter.com/%xx` and it triggered the same error. (`%xx` is not a valid hexadecimal value) So Twitter was trying to find a value for `%xx` but it couldn’t so it raises an error every time you’re calling this url.

So now lets copy and paste this URL and post it in a form of a tweet; You can guess now what will happen? I can see your eyes blinking and shining hmm isn’t it?

**Result** : BOOM, I’ve prevented literally all my followers from loading ANY new tweets. So now I only have one annoying problem, which is > (Twitter’s mobile site).

Unfortunately this bug doesn’t work on Twitter’s main website it only works on the mobile site version, But after a little research I found a URL to switch the “main site version” to the “mobile site version” aka the Twitter UI!

Here: <https://twitter.com/i/onboarding/verify>

Twitter was trying a new beta UI on the main site that you can switch to and from it freely, just click on your profile picture and click try the new Twitter and that’s it, you will be switched to a GUI looks exactly as the Twitter mobile site UI. Time to see all the blah blah we were talking about in action…

### POC Video

This bug has been reported to twitter team and fixed the bug and you can find the original URL on HackerOne Platform here: <https://hackerone.com/reports/500686> Thanks everyone for your time and till the next one… 

## **A minute if you please!**

Building a website, API, an application or dealing with any kind of sensitive information? Anything related to the security and Safety of your business? Or already launched one without considering security? Worried about your personal security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)! 

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2019%2F03%2F25%2Fseif-elsallamy%2Fgeneral%2Ftwitter-denial-of-service-bug-or-how-i-could-prevent-all-followers-from-reading-or-accessing-literally-any-tweets&linkname=Twitter%20Denial%20of%20Service%20bug%20or%20How%20i%20could%20prevent%20all%20followers%20from%20reading%20or%20accessing%20literally%20ANY%20tweets%21 "Gmail")[](https://www.addtoany.com/share)

access  Bug  denial  Denial Of Service  DOS  followers  prevent  Service  tweets

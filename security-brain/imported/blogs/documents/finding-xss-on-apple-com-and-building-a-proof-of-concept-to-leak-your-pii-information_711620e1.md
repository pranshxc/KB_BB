---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-23_finding-xss-on-applecom-and-building-a-proof-of-concept-to-leak-your-pii-informa.md
original_filename: 2021-11-23_finding-xss-on-applecom-and-building-a-proof-of-concept-to-leak-your-pii-informa.md
title: Finding XSS on .apple.com and building a proof of concept to leak your PII
  information
category: documents
detected_topics:
- idor
- xss
- command-injection
- otp
- cors
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- otp
- cors
- api-security
language: en
raw_sha256: 711620e1c7a397916bc0b833a06b6590935752958b9f05bbefb9fbfbe3b578c7
text_sha256: a814eca5b54d94ef23a75efb1c7f169901f6014229a041f2f1952ac5b7e10112
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Finding XSS on .apple.com and building a proof of concept to leak your PII information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-23_finding-xss-on-applecom-and-building-a-proof-of-concept-to-leak-your-pii-informa.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, otp, cors, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `711620e1c7a397916bc0b833a06b6590935752958b9f05bbefb9fbfbe3b578c7`
- Text SHA256: `a814eca5b54d94ef23a75efb1c7f169901f6014229a041f2f1952ac5b7e10112`


## Content

---
title: "Finding XSS on .apple.com and building a proof of concept to leak your PII information"
url: "https://zseano.medium.com/finding-xss-on-apple-com-and-building-a-proof-of-concept-to-leak-your-pii-information-d7bc93cff2df"
authors: ["Zseano (@zseano)"]
programs: ["Apple"]
bugs: ["XSS"]
publication_date: "2021-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3146
scraped_via: "browseros"
---

# Finding XSS on .apple.com and building a proof of concept to leak your PII information

1

Finding XSS on .apple.com and building a proof of concept to leak your PII information
Sean (zseano)
Follow
7 min read
·
Nov 24, 2021

827

2

Back in February of this year I hacked with members of BugBountyHunter.com on a public bug bounty program and we chose Apple as our target. This post will detail how we discovered some XSS and built a PoC to leak PII information across multiple .apple.com subdomains. The teamwork from this event was phenomenal and I can’t wait to do another soon.

Initial ‘recon’

If you’ve followed me for a while you’ll know that I am not someone to run lots of tools and do much ‘recon’. I prefer just diving straight in. After reading Sam Curry’s post (https://samcurry.net/hacking-apple/) one key thing that stood out to me was the fact he ran Burp whilst playing with various features on his iPhone. To be honest I was quite like ‘o wow’ to the fact I hadn’t thought to try this before even though i’ve proxied traffic through my iphone for a long time. I went and tried replicated some of the bugs Sam described such as find my friends idor. I saw the requests (and confirmed fixed :D) and started the hunt.

One file that stood out for me in the requests was a “bag.xml” file (https://apps.apple.com/bag.xml) which is requested when opening various apps on your iPhone. It appeared to contain endpoints as well as headers & parameters required to interact with them. (In the URL above you can’t see headers needed but there’s a way to get it to respond differently with various information but I won’t mention that here. :D Go play yourself!!). There wasn’t any guessing, the information was here for me. Now this is the kind of ‘recon’ stuff I like because there’s no fuzzing for /backup.zip and instead I know these endpoints are going to have some sort of code execute. When there’s code to be executed there’s me the other side wanting to find out how things work and break it.

Reading this in detail? If you check Sam currys post you will see “WebObjects” is used in a lot of requests. :-) Be pro-active and you will find some interesting things in places

I shared the file with members and we began hunting through. I personally gathered all of the endpoints listed in this bag.xml file and ran them through Intruder (https://zseano.medium.com/using-xampp-and-burp-intruder-when-scanning-for-subdomains-to-look-for-interesting-behaviour-code-f24c511d15ed) with a simple cURL request querying these endpoints with custom headers. I started browsing the responses to various different requests but also went to start checking google & github, as well wayback, to see if there was anything extra info on these endpoints. Some members started their tools and others went hunting on newly disclosed subdomains and it was honestly great to see everyone go hands on and working as a team.

Tip: Some .apple.com domains & endpoints will only respond with certain user-agents and headers set. You can check this when testing on your iPhone and checking user-agent. Don’t blindly scan with default user agents — know your target!

Press enter or click to view image in full size

As my intruder went BRRRRRR I noticed some endpoints responded with various interesting errors and this is where the collaboration with members of BugBountyHunter came into play. I fuzzed GET/POST requests and various different content types and on 4 endpoints we discovered we could control the POST Data but our input was getting URL encoded on response. Doh.

But, one member, YouGina, then mentioned our FORM post should have enctype=text/plain set and it should work. This is something I overlooked when testing so massive kudos to him as he was correct and now we have a working XSS!

Press enter or click to view image in full size
Hacking as a family

As there is a diverse group of members on BugBountyHunter and each has their own expertise & talent, as members such as 0xblackbird, iBruteForce, JTCSec and Prime were hunting through apps manually, a lot of others such as HolyBugx, xnl-h4ck3r and flag_c0 were running tools to discover more subdomains. After finding a valid XSS and celebrating in chat, various other researchers then mentioned the 4 endpoints we’d discovered were actually on lots of Apple subdomains. This wasn’t just example.apple.com, this affected 30+ subdomains. Nice! Teamwork ❤

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

(There is lots to mention, why not check our epic hackers yourself — https://www.bugbountyhunter.com/ourhackers)

But what can we do with this XSS?

Making a proof of concept

Apple won’t pay for just alert(0) right?. So we need to do something to impress those over at Apple. I’ve always mentioned to set goals so I told members it was a case of using the XSS and finding something to leak (token/session info-> account takeover, pii info) and working from there, so the focus at first was set on finding a CORS ‘misconfig’ on an Apple endpoint that contained something useful to an attacker that Apple cares about. PII information for example. (Tip: usually when querying your info a request is sent and you’ll see a response in JSON format. test origin: on these.. we’ve all seen ‘em!)

As well as this I mentioned to check for any interesting tokens when logging into various apps/services and note it down for us to maybe use further down the line.

Let the hunt begin.

Hunting through we noticed lots of Apple endpoints will respond if Origin: is set, but actually most are locked down to specific Apple subdomains. This is a good approach so kudos to Apple for that. Not all of them were as secure and some were semi-relaxed (would allow for multiple .apple.com subdomains rather than just a single subdomain). One thing I mention in my methodology (which is free btw — https://www.bugbountyhunter.com/zseano) is to learn your target as you’re hunting through. The fact some Apple endpoints would respond to Origin:, and some were more relaxed than others, said to me that SOMEWHERE, somewhereeee on Apple, there will be the golden snitch that we’re looking for. Any .apple.com domain whitelisted in Origin:

Persistence pays off. Next tip: Don’t give up too early. I get some DMs with people saying they can’t find anything and i’m like “well how long have you been hacking on it?” and they reply ‘2 days’. Go for one target for 3–6 months then DM me! ;)

I personally opened as many Apple apps on my iPhone and other members went to check lots of web applications. It took a bit of time but eventually we found endpoints which contained PII information and also allowed *.apple.com in the Origin header which affected every domain we’ve found XSS on. As our subdomains were all whitelisted in the Origin: header (*.apple.com was allowed) from here it was a simple case of building a simple PoC to send a request and retrieve PII info. We use alert to demonstrate but it wouldn’t be hard to send this to an attackers domain. (https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)

Press enter or click to view image in full size
Full name, address, appleID

We now had 4 separate XSS (unique endpoints!) across multiple domains which could be used to retrieve PII info on multiple Apple services. Our POC didn’t really require any user interaction apart from visiting our site (totallynotevil.com) and the XSS on .apple.com would execute. (As we could automate the FORM post right?!). For me personally I felt like this finding would be something Apple is interested in because lots of users were affected based on the subdomains we discovered we could leak PII information on. We sent off our report and waited a few months only to be told our finding was not novel enough and there’s no bounty which was a shame, but it is what it is. All of the XSS have been confirmed fixed for over 90 days and the Origin: header is now locked down on the discovered endpoints and only allow certain subdomains. Nice work!

However, actually, after sending this blog post to them for review they mentioned that they would re-adjudicate (I literally just asked if the blog was okay to post, so this is really cool of them!). will update!

Tip: When i’ve reported leaking PII information with a “wonky” Access-Allow-Control-Origin: i’ve seen the bug bounty program only fix the XSS and you can use further XSS to leak PII information. This is actually something which helps you get a “feel” for things over at your chosen program. How are they fixing issues? Are they treating XSS as all the same with a flat rate of $500 for example no matter the poc (alert vs account takeover) or are they being pro-active and thinking further, “Oh, does this account.json really need to allow for *.domain.com? That dev-test.example.com domain probably doesn’t need access…”.

The total time hacking was around 5 days max (not full days, 3–4 hoursish a day) but this is how we went from using something as intended (opening an App on iphone), seeing an interesting file, investigating and understanding the information it contained, then finding XSS and finding a way to increase the impact via leaking PII information from a wonky AACO. It was a case of poking around, seeing what’s what, and then when discovering something, understanding the goal of how we can achieve more impact. From digging deeper actually it will help you learn more of the assets your testing and getting familiar with what’s out there.

This event was actually the first ever Hackevent over at BugBountyHunter.com where Level 2+ members and myself hacked together on a chosen program as part of ‘bounty training’ (applying what you’ve learnt on bug bounty programs). There was over 20+ hackers involved and I really enjoyed hacking with them all. Current hackevent formats have changed but I strongly feel I have built a ‘1337’ ;) team over the last year whilst getting to know them on a personal level through triage and events and I’m looking forward to what the future will bring for us all when it comes to hacking together! :-)

stay safe and keep hacking!

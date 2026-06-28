---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-31_saving-more-than-100000-website-from-a-watering-hole-attack.md
original_filename: 2022-08-31_saving-more-than-100000-website-from-a-watering-hole-attack.md
title: Saving more than 100,000 website from a Watering Hole attack
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: b6340c14ac76ef3abbfa244e830d17694069f5340cee2d55527aba931661a1c4
text_sha256: 78a2ff9493327c0bd7c6ea60f2f53a769fd0aa33bd0a77e228d91559b7cc592a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Saving more than 100,000 website from a Watering Hole attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-31_saving-more-than-100000-website-from-a-watering-hole-attack.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `b6340c14ac76ef3abbfa244e830d17694069f5340cee2d55527aba931661a1c4`
- Text SHA256: `78a2ff9493327c0bd7c6ea60f2f53a769fd0aa33bd0a77e228d91559b7cc592a`


## Content

---
title: "Saving more than 100,000 website from a Watering Hole attack"
page_title: "Saving 100,000 websites from a Watering Hole attack | by mohamad mahmoudi | Medium"
url: "https://med-mahmoudi26.medium.com/saving-more-than-100-000-website-from-a-watering-hole-attack-a22f63a37f94"
authors: ["mohamad mahmoudi (@Lotus_619)"]
programs: ["HubSpot"]
bugs: ["Web cache poisoning", "Watering hole attack"]
bounty: "5,000"
publication_date: "2022-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2236
scraped_via: "browseros"
---

# Saving more than 100,000 website from a Watering Hole attack

Saving 100,000 websites from a Watering Hole attack
mohamad mahmoudi
Follow
5 min read
·
Aug 31, 2022

165

W
atering hole is a computer attack strategy in which an attacker guesses or observes which websites an organization often uses and infects one or more of them with malware. This makes the hacks harder to detect and research. The name is derived from predators in the natural world, who wait for an opportunity to attack their prey near watering holes.

Background

During my bug bounty sessions, I often come across websites built with Hubspot CMS.

I asked google for the number of websites built with this software. I learned that a good number of companies used it to build blogs and landing websites. Eager to start my first large scale testing operation, I hosted a website on Hubspot and begun hacking it.

I have found multiple 0day vulnerabilities that affected more than 100 000 websites throughout the world wide web. One of them was a critical web cache issue with a potential of watering hole attack.

Initial Discovery

The initial discovery was Hubspot allowing uploading SVG images. I was able to trigger XSS on my own website by embedding javascript into my svg files. Example:

<?xml version="1.0" standalone="no"?> <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  
<rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<script type="text/javascript">
alert(document.domain);  
</script> 
</svg>

For the rest of the article, I’ll refer to my website as akme.com and for the malicious svg file as xss.svg

The endpoint to trigger the XSS would be

https://akme.com/hs-fs/hubfs/xss.svg.

At this point all I had was a boring self XSS with 0 impact. So I went looking for ways of escalation.

After hours of reconnaissance, I noted these two pieces of information:

All websites hosted on hubspot use the endpoint /hs-fs/hubfs to request their media files.
Each Hubsopt account had a virtual CDN hosted at <portal_Id>.fs1.hubspotusercontent-na1.net

Combining them together, I concluded that the front end proxy had special rules for the route /hs-fs/hubfs.

Secondary Context

For better understanding of the flow, I have imagined the following schema:

Press enter or click to view image in full size

I assumed that the request from the Front End Proxy to the file system server contained an additional parameter in the request header, so I called it X-Param(we’ll find its real name later, no spoilers for now).

I have also assumed that the file system server would rely on this parameter to find out the hostname of the CDN relative to akme.com.

Get mohamad mahmoudi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In order to find the real name of our X-Param, I started fuzzing the request that is sent from my browser to the front end proxy using Param Miner.

A web cache poisoning issue was detected at the endpoint akme.com/hs-fs/hubfs/xss.svg.

Web Cache Poisoning

Quoting Portswigger, Web cache poisoning is an advanced technique whereby an attacker exploits the behavior of a web server and cache so that a harmful HTTP response is served to other users. You can read more here: https://portswigger.net/web-security/web-cache-poisoning

The following screenshot shows an error we get by adding the parameter X-Forwarded-Host to a request of an image from a website hosted on hubspot:

Press enter or click to view image in full size

Notice the cache status in the response CF-Cache-Status: MISS

By sending the same request multiple times, the header eventually turns to F-Cache-Status: HIT. Which meant that the error message was cached instead of the actual image. Everytime a user requests the image, they would receive the error message I have triggered. One could’ve easily used the same technique to corrupt all the media hosted on the website.

It was a cool impact, but I felt I could do more. Then it hit me ! Remember the X-Param ? It became obvious by this time that the X-Param was X-Forwarded-Host ! After messing with this parameter for a while, I was able to force any website hosted on Hubspot to render media hosted on my CDN.

The following request is an example, the targeted website would be www.victim.com :

GET /hs-fs/hubfs/xss.svg HTTP/2 
Host: www.victim.com
X-Forwarded-Host: www.akme.com

When the X-Forawarded-Host was predefined(which is the case), the front end proxy wouldn’t bother changing its value to the actual host value. It would forward the request to the file system server which would go looking for xss.svg in the CDN relative to www.akme.com instead of www.victim.com. Which meant the response would be our malicious xss.svg instead of 404 error. Sending the same request multiple times would cache the response leading to a stored XSS at www.victim.com/hs-fs/hubfs/xss.svg

Water in the hole

To execute the watering hole attack, hackers could target websites hosted on Hubspot and remotely replace their media with pieces of malware.

Suppose the company www.victim.com has a file called safe.svg hosted in their website. To override this file, the attacker could do the following:

Host a website on Hubspot. Let’s call it www.attacker.com
Embed malicious script in an svg file, name it safe.svg then upload it to his website.
Send the following request to www.victim.com:
GET /hs-fs/hubfs/safe.svg HTTP/2 
Host: www.victim.com
X-Forwarded-Host: www.attacker.com

Eventually, someone would visit www.victim.com/hs-fs/hubfs/safe.svg and the embedded payload would be triggered in their browser. Repeat the same process on all websites and you have millions of potential victims.

26 Jan 2022 — The vulnerability was reported to Hubspot

08 Mar 2022 — Bounty of 5000$ received

08 Mar 2022 — The vulnerability got fixed

I’d like to thank the researcher Sam Curry for his awesome presentation about Attacking Secondary Context In Web Application.

I’d like to also thank James ‘albinowax’ Kettle for releasing the great tool of ParamMiner

I am down for collaboration, you can find me on :

Twitter: https://twitter.com/medmahmoudi_619

Linkedin: https://www.linkedin.com/in/mohamed-mahmoudi-944029161/

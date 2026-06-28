---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-16_when-not-to-rely-on-automated-tools.md
original_filename: 2023-12-16_when-not-to-rely-on-automated-tools.md
title: When not to rely on Automated Tools
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 821c05ea81a913bc55448889e4c6ef069aef09ffd9f47eee97f69d0c5a1d636b
text_sha256: eb49a85e838efa1664636b5e5732ecc4ff5d827217064f1ac331284b7a19023e
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# When not to rely on Automated Tools

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-16_when-not-to-rely-on-automated-tools.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `821c05ea81a913bc55448889e4c6ef069aef09ffd9f47eee97f69d0c5a1d636b`
- Text SHA256: `eb49a85e838efa1664636b5e5732ecc4ff5d827217064f1ac331284b7a19023e`


## Content

---
title: "When not to rely on Automated Tools"
url: "https://medium.com/@rodriguezjorgex/when-not-to-rely-on-automated-tools-429b331e0613"
authors: ["Rodriguezjorgex"]
bugs: ["Prototype pollution"]
publication_date: "2023-12-16"
added_date: "2024-01-03"
source: "pentester.land/writeups.json"
original_index: 617
scraped_via: "browseros"
---

# When not to rely on Automated Tools

When not to rely on Automated Tools
Rodriguezjorgex
Follow
3 min read
·
Dec 16, 2023

103

2

How I found Prototype Pollution with an automated tool

While hashtag#bugbounty Hunting on Synack Red Team, I was hunting on a target with a wildcard subdomain scope. I like doing manual hunting, and I normally don’t do much recon, other than using the chaos tool to get a list of subdomains. So I start with chaos using the following command

chaos -d REDACTED > subdomains.txt

After viewing the results, I opened Burp and ran the built-in browser. I decided to enable Dom Invader with prototype pollution.

Press enter or click to view image in full size

DOM Invader with prototype pollution enabled

With DOM Invader enabled, I navigated to several subdomains and I kept getting hits on DOM Invader. But every time I would check the DOM Invader tab on the Developer tools, I wouldn’t get the “Exploit” or “Scan for Gadgets” option.

Press enter or click to view image in full size

DOM Invader tab showing no Gadgets

Finally finding prototype pollution

After about an hour of manually navigating through subdomains, I finally get a hit on the DOM Invader tab that shows the “Scan for Gadgets” option.

Press enter or click to view image in full size

DOM Invader tab showing Scan for Gadgets

Get Rodriguezjorgex’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I clicked on Scan for Gadgets and DOM Invader finds the following payload to use:

https://redacted.com/#__proto__[div][2]=%3Cimg+src+onerror%3Dalert%28document.domain%29%3E

After navigating to the URL, I confirmed the alert XSS, and start writing my report.

Prototype Pollution: No automation

I submitted the report and it got triaged fairly quickly. But what was more impressive was I got a patch verification request within 24 hours. The client had fixed the code that fast?

For those unfamiliar, in Synack, once you’ve submitted a report, the client can request a patch verification after they have fixed the issue. I accepted the patch verification, and again I navigated to the subdomain with DOM Invader enabled.

And again, DOM Invader tells me there’s a prototype pollution vulnerability and to scan for gadgets. I scan for gadgets again, but to my surprise, DOM Invader doesn’t find any gadgets.

So we’re done right?

If there’s still prototype pollution, then what did the client fixed? I looked, and the client seems to have fixed the sink, or, the part of the code that was reflecting the XSS. The only thing I needed to do was find an additional sink. But DOM Invader couldn’t find it, so was there another sink?

It turns out that the day before, I was studying hashtag#HackTheBox Academy for prototype pollution, and they had a particular topic on Client-Side Prototype Pollution on their Whitebox Attacks module. In this module, they also had an instance where DOM Invader doesn’t work, and you need to find the gadget manually. They provided a Github repo for finding the gadgets

https://github.com/BlackFan/client-side-prototype-pollution/tree/master/gadgets

I used the same techniques I learned in the HackTheBox Academy module and searched for a gadget that I could use on the clients web application. After testing 2 different gadgets, I find the correct gadget:

https://redacted.com/#__proto__[preventDefault]=x&__proto__[handleObj]=x&__proto__[delegateTarget]=<img/src/onerror%3dalert(document.domain)>

The alert pops again, and I go back to informing the client the issue is not fixed, and to ensure to fix the root cause, not just the sinks.

Conclusion

If I had relied on automated tools alone, the client would have been left believing the web application was secure after their patch. But by doing a thorough job and doing some manual exploration, I was able to find additional ways to exploit a single vulnerability.

It’s also good to keep up to date and learning. HackTheBox Academy is a great resource. I highly recommend it for any Bug Hunter who want to get better at their craft.

Thanks to Kuldeep Pandya for advising me to write this content.

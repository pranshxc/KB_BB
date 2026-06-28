---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-29_worldwide-server-side-cache-poisoning-on-all-akamai-edge-nodes-50k-bounty-earned.md
original_filename: 2022-09-29_worldwide-server-side-cache-poisoning-on-all-akamai-edge-nodes-50k-bounty-earned.md
title: Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes ($50K+ Bounty
  Earned)
category: documents
detected_topics:
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: 226f2e0273fe01d68eea420c447afc3a1dc5c0bfd33b108586f610e184df2ddf
text_sha256: c9ffef2054ec7d2c2fae3c49ace97219dfc91b0411545a54308baa3754237934
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes ($50K+ Bounty Earned)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-29_worldwide-server-side-cache-poisoning-on-all-akamai-edge-nodes-50k-bounty-earned.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `226f2e0273fe01d68eea420c447afc3a1dc5c0bfd33b108586f610e184df2ddf`
- Text SHA256: `c9ffef2054ec7d2c2fae3c49ace97219dfc91b0411545a54308baa3754237934`


## Content

---
title: "Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes ($50K+ Bounty Earned)"
url: "https://medium.com/@jacopotediosi/worldwide-server-side-cache-poisoning-on-all-akamai-edge-nodes-50k-bounty-earned-f97d80f3922b"
authors: ["Francesco Mariani (@_medusa_1_)", "Jacopo Tediosi (@jacopotediosi)"]
programs: ["Akamai", "Paypal", "Airbnb", "Tesla", "Valve", "Zomato", "Whitejar", "Starbucks", "PlayStation", "Marriott", "Hyatt Hotels", "Goldman Sachs", "Microsoft", "Apple", "LastPass", "Brussels Airlines", "Mastercard", "eToro BBP", "BMW Group", "Rockstar Games"]
bugs: ["Web cache poisoning"]
bounty: "50,000"
publication_date: "2022-09-29"
added_date: "2022-10-02"
source: "pentester.land/writeups.json"
original_index: 2099
scraped_via: "browseros"
---

# Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes ($50K+ Bounty Earned)

Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes ($50K+ Bounty Earned)
Jacopo Tediosi
Follow
8 min read
·
Sep 29, 2022

511

8

Introduction And Context

In March 2022, my friend Francesco Mariani and I were teaming up on a private Bug Bounty program organized by Whitejar to search for bugs on a website that was using Akamai CDN.

The Akamai WAF rules were bothering us while experimenting with the most common attack types, so we quickly got bored and started trying more esoteric payloads and mixing them.

Finally, we ended up finding a vulnerability that really made us exclaim: “WOW, we ‘broke’ half the web!”.

But let’s start from the beginning:

The First Clue

At one point, we were intrigued by an unusual “DNS Failure” response, received by sending twice an HTTP/1.1 GET request to the host being tested (“REDACTED” in the below screenshot) with the “Connection: Content-Length” header and containing another GET request to www.example.com as body.

Press enter or click to view image in full size
The strange “DNS Failure” response

Weird behaviors like this can often be overlooked while testing so many things, but luckily this time we decided to dig deeper.

Vulnerability Explanation

I have to admit, it took me a while to figure out what was going on, and I also had to reread Nathan Davison’s excellent article on “hop-by-hop” headers that I had studied in the past.

As explained in the RFC 2068 — Section 13.5.1, there are some special headers named “hop-by-hop”, which are removed from proxies before forwarding requests to the next proxy or the destination.
The “Connection” header allows stating more “hop-by-hop” headers in addition to the default ones.

Specifying the “Content-Length” header as “hop-by-hop”, it happened that Akamai’s first proxy removed it, turning the request body into a second request. Akamai’s second proxy then resolved the two requests separately.

Since the first proxy received two responses but only one was expected, a desynchronization occurred, and the second response was queued and subsequently sent in response to requests from other clients/users, causing an HTTP Smuggling Vulnerability.

This case requires a certain degree of knowledge about network architectures, web protocols, and other fancy stuff, so I try to explain it more easily with the following chart.

Press enter or click to view image in full size
My attempt to graphically explain this complex security problem
A Team Effort

However, I could not immediately understand why the DNS error was showing up and why www.example.com was not being resolved.
The answer was actually quite simple, but my co-worker’s intuition was crucial: Akamai’s proxy that routes requests appeared to resolve DNS only internally within Akamai’s network.

In fact, as shown in the following screenshot, using www.akamai.com in the request body (where we previously used www.example.com), we received in response the Akamai homepage instead of the REDACTED homepage.

Press enter or click to view image in full size
HTTP Smuggling at it’s finest: receiving www.akamai.com homepage when requesting www.redacted.com

Please also note that we opted to use the OPTIONS method for the first request, as it seemed more plausible to us that it could have a body than GET requests.

What About The Impact?

We were using a VPN to verify that the desynchronization was an “open” one, meaning that it affected the responses given to IP addresses other than the ones we were attacking from.

Also, believing it possible that the bug concerned all Akamai customers around the world, we changed our target from www.REDACTED.com to more popular sites.

To our amazement, we noticed that it worked on them all and that, sometimes, “smuggled” responses were being server-side cached from Akamai Edge Nodes for the entire geographic area close to the IP sending the malicious request. This allowed us to semi-permanently (depending on cache times) create new arbitrary contents within almost any domain served by Akamai, resulting in a HUGE impact!

In the following GIF, as Proof of Concept, we created, for the whole Italian area, the newly cached page demo.paypal.com/jacopotediosi_hackerone.js, containing the content of www.sky.com/robots.txt (another Akamai customer, because we didn’t own a host on the Akamai network to use for publishing our arbitrary contents).

Press enter or click to view image in full size
Demo.paypal.com PoC, using different IPs and browsers to make sure there are no local caches
Reporting to Akamai

Once we understood the seriousness of the situation, we decided to report it ethically and responsibly, first of all to Akamai.
Unfortunately, we quickly realized that Akamai doesn’t have a Bug Bounty program, Hall of Fame, swag giveaways, or anything similar.

Press enter or click to view image in full size
Akamai validating the vulnerability
Reporting to Akamai Customers

We are white hats, but we were still not willing to work for free, because this vulnerability was very critical, and our skills are rare, complex, and sought after, and we think they deserve to be valued.
So, while Akamai was patching following our report, we chose to race against the time by asking for bounties from single Akamai customers.
While this may sound strange, from our point of view on technologies, those who use a framework/plugin/CDN/whatever assume both their benefits and risks. Thanks to our work Akamai and all their customers have been made aware of a security issue and have been able to fix it, so it’s just fair that they pay for our service because, without us, the vulnerability would still be there.

We used bbscope to extract links for all the public programs on the most popular bug bounties platforms. Next, we wrote a short bash script to filter from the list only the domains whose DNS pointed to Akamai:

while read line; do
  count=$(dig $line | grep "akamai" 2>/dev/null)
  if [[ -n $count ]]
  then
  echo "Found: " $line
  fi
done <$1
Whitejar

Whitejar immediately gave us €5,000 for their private program.

Bugcrowd

On Bugcrowd, they were not competent enough to understand the vulnerability and closed both our reports for Tesla.com as “duplicated” (of a ticket clearly not related to ours) and for LastPass.com as “not applicable” because they were unable to reproduce.
Fun fact: at one point, their triager did not know how to use Burp Suite and told us that “sending an OPTIONS request to any URI, they received 400 Bad Request”, not realizing that they were sending the request to the target of the report they probably had read before ours.

Press enter or click to view image in full size
Sam from Bugcrowd doesn’t know how to use Burp Suite
Intigriti

Intigriti, about the Brussels Airlines program, told us that “Brussels Airlines is already aware of any request smuggle vulnerabilities in their web assets” (yeah, “ANY”, lol), and closed our ticket as “duplicated”.
Our Mastercard ticket was also closed without providing further information.

HackerOne

On HackerOne, some programs refused our tickets and closed as “N/A”:

Starbucks replied the vulnerability, in their opinion, wasn’t a major security issue.
PlayStation Staff failed to reproduce (even after we created a new page for them under the www.playstation.com domain).
Marriott informed us that cache issues were temporarily out-of-scope.

Many other programs paid us, instead: we received $25,200 from
PayPal, $14,875 from Airbnb, $4000 from Hyatt Hotels, $750 from Valve (Steam), $450 from Zomato, and $100 from Goldman Sachs.

Get Jacopo Tediosi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In particular, Airbnb handled the situation outstandingly, applying custom rules on Akamai’s WAF in less than 24 hours to block requests containing “Connection: Content-Length” even before Akamai’s official fix.
PayPal was also a curious case, because they confirmed our report and issued a bounty long after Akamai’s fix. So we don’t know if they ever saw the vulnerability working or if they just trusted our PoC video.

Other Affected Websites

Unfortunately, Microsoft and Apple acknowledged our reports after Akamai had already deployed a fix, but they thanked us anyway via private e-mails.

Call For Research

This is the first time we’ve seen “hop-by-hop” headers used for smuggling this way (EDIT, 01/10/2022: Reddit user mdulin2 reported that the payload we used had already appeared in Martin Doyhenard’s “Response Smuggling: Pwning HTTP /1.1 Connections” presentation at DEFCON29), so we think they might deserve further research.

For example, we haven’t had time to see if other implementations besides Akamai suffer from this issue.

Moreover, Akamai fixed it by applying some rules that prevent specifying the “Content-Length” keyword within the “Connection” header value, but we are not sure that there are no bypasses or some other unexpected similar ways to split the requests.

Press enter or click to view image in full size
Akamai applied some validations on the requests, but the underlying problem remains in the HTTP core implementation
Aftermath
On October 5, 2022, Akamai published an official advisory on the incident.
In February 2023, this technique ranked #7 in PortSwigger’s Top 10 web-hacking techniques of 2022
Related Resources
You can read Francesco’s version of this blog post on Hacktive Security Blog.
Timelines
21/03/2022: Analyzing the weird “DNS failure” behaviour for the first time.
22/03/2022: Built a fully functional PoC for Whitejar’s BB private program.
23/03/2022: We confirmed that the PoC worked for any Akamai Edge Node.
24/03/2022, 19:33 CEST: Sent the first email to security@akamai.com.
25/03/2022, 19:16 CEST: Received first response from an Akamai security architect.
25/03/2022, 20:29 CEST: Akamai confirmed the vulnerability and informed us they don’t have a Bug Bounty program.
25/03/2022, 23:00 CEST — Until 01/04/2022, 23:30 CEST: Opened most of the tickets on bug bounty platforms.
26/03/2022, 02:00 CEST, Valve (Steam) confirmed they were able to reproduce the bug.
28/03/2022, 07:40 CEST: Zomato asked us to poison their cache for India Region as PoC and a few minutes later they confirmed the presence of the vulnerability.
28/03/2022, 21:35 CEST: Airbnb confirmed they were able to reproduce.
29/03/2022, 19:07 CEST: Airbnb applied a workaround fix and requested a retest.
02/04/2022: Akamai deployed a silent fix, and from now, on our payloads triggered 403 responses. We closed the H1 tickets of those who had not yet answered us (eToro BBP, BMW Group, Rockstar Games) to prevent them from being reported as N/A.
06/04/2022: Akamai informed us of the silent fix they applied.
07/04/2022: Agreed with Akamai on how to proceed with public disclosure.
27/04/2022: PayPal confirmed our H1 report and rewarded us.
18/05/2022: Received most of the bounties.
17/09/2022: Francesco published his blog post on Hacktive Security Blog.
29/09/2022: Publication of this article on Medium.
03/10/2022: Publication on Whitejar Blog.
04/10/2022: Publication on The Daily Swig and The Stack. This article was also featured on Security Now #891 “Poisoning Akamai” podcast.
05/10/2022: Akamai has issued an official advisory.

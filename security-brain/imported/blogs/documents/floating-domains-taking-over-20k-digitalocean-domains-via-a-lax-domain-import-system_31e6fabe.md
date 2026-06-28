---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-08-25_floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-sy.md
original_filename: 2016-08-25_floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-sy.md
title: Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import
  System
category: documents
detected_topics:
- xss
- cloud-security
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- cloud-security
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 31e6fabe830fe9cc0ca2729f01bb5f0e76298dbb463e7a9102341c446bb6f692
text_sha256: 34105eb1450e6d93c17de2068c8b960a14fcb51eb4f72d0a32e2f0bf1ed6361b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-08-25_floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-sy.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `31e6fabe830fe9cc0ca2729f01bb5f0e76298dbb463e7a9102341c446bb6f692`
- Text SHA256: `34105eb1450e6d93c17de2068c8b960a14fcb51eb4f72d0a32e2f0bf1ed6361b`


## Content

---
title: "Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import System"
page_title: "Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import System – The Hacker Blog"
url: "https://thehackerblog.com/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/"
final_url: "https://thehackerblog.com/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/"
authors: ["Matthew Bryant (@IAmMandatory)"]
programs: ["DigitalOcean"]
bugs: ["Subdomain takeover"]
publication_date: "2016-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6267
---

# Floating Domains – Taking Over 20K DigitalOcean Domains via a Lax Domain Import System

![crashed_ship](/wp-content/uploads/2016/08/crashed_ship.jpg)

######  The above image is taken from [here](https://www.flickr.com/photos/jurvetson/16001775028) and was taken by [Steve Jurvetson](https://www.flickr.com/photos/jurvetson/ "Go to Steve Jurvetson's photostream"). 

EDIT: DigitalOcean seems to be getting a lot of flak from this post so I’d just like to point out that I feel DigitalOcean’s reaction in this case was entirely justified (they saw an anomaly and they put a stop to it). The only thing I’d wish was done differently would be that the domains were deleted from my account upon me being banned. There was a few hour delay between testing and reaching out to them and ideally I should’ve reached out ahead of time. The main reason I did not reach out with the theory instead of the proof-of-concept was because I believed that it would be ignored due to lack of evidence (as is my experience with past disclosures). Overall my impression of DigitalOcean’s security team is very positive and I will definitely be much more proactive about reaching out to them in the future.

DigitalOcean is a cloud service provider similar to Amazon Web Services or Google Cloud. They offer cloud DNS hosting as one of their product lines – a nice guide on how to set up your domain to use their DNS can be found [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-host-name-with-digitalocean). Take a moment to read it over and see if you can spot any potential issues with their domain name set up process.

From a quick glance it appears to be a very easy to use system. For example: No pesky domain validation to impede your ability to add any arbitrary domain to your account, no need to recall who is on your domain’s WHOIS, and no need to set your domain to specific nameservers as is needed with systems such as Cloudflare. In fact all you have to do is the following:

> “Within the Networking section, click on Add Domain, and fill in the the domain name field and IP address of the server you want to connect it to on the subsequent page.”

So, if you’d like, you can add my domain _thehackerblog.com_ to your own DigitalOcean account right now (assuming nobody else has done so already). This brings up interesting questions like, “ _can people block me from importing my domain to DigitalOcean?_ ” and, “ _what happens when I delete my domain from DigitalOcean but forget to change the nameservers?_ “. These are good questions, but before we answer them we’ll take a short detour to another cloud provider and see how their implementation differs.

## The Route53 Set Up Process

Amazon Web Services, or AWS, also offers cloud DNS hosting in the form of its product line known as [Route53](https://aws.amazon.com/route53/). As a test, we’ll try the set up process for the domain _thehackerblog.com_. You can see AWS’s official documentation [here](https://docs.aws.amazon.com/gettingstarted/latest/swh/getting-started-configure-route53.html) if you’d like to try this yourself. The first step is to click the _Create Hosted Zone_ button in the top left corner of the Route53 control panel. We’ll now fill in the domain we wish to use along with a short comment and whether or not we wish for this DNS zone to be public. Finally we hit create and are brought to the DNS management panel for our newly created zone. The [NS](https://support.dnsimple.com/articles/ns-record/) record type has been pre-populated with a few randomly generated nameservers. For example, the nameserver list I received after trying this is as follows:

> _ns-624.awsdns-14.net._

> _ns-39.awsdns-04.com._

> _ns-1651.awsdns-14.co.uk._

> _ns-1067.awsdns-05.org._

The above is very important – if I created a zone for _thehackerblog.com_ and you did the same we’d both get different nameservers. This ensures that nobody could takeover my domain if I deleted the zone file from my AWS account because the nameservers are specific to my account. So, if I deleted my domain and you wanted to take it over, you’d have to keep trying until you get the same nameserver set as above in order to do so. Otherwise my domain would be pointed to other nameservers than the ones you control.

## Back to DigitalOcean

Returning to DigitalOcean, the answer to the question “ _what happens when I delete my domain from DigitalOcean but forget to change the nameservers?_ ” becomes clear. If you delete the domain from your account anyone can immediately re-add it to their own account without any verification of ownership and take it over.

It’s one thing to notice a possible issue that _could_ occur but _proving_ that it does occur at a large scale is another beast. How can we find out if this issue is systematic and common without attempting to add every domain on the Internet to our DigitalOcean account? How would we even get a list of every domain name anyway?

To start, one notable way to tell if a domain has been added to a DigitalOcean account is to perform a regular DNS query and see how the DigitalOcean nameserver’s respond. As an example, we’ll use _alert.cm,_ which has their nameservers set to DigitalOcean but are not listed under any DigitalOcean account:
  
  
  mandatory@Matthews-MacBook-Pro-4 ~> dig NS alert.cm @ns1.digitalocean.com.
  
  ; <<>> DiG 9.8.3-P1 <<>> NS alert.cm @ns1.digitalocean.com.
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 53736
  ;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
  ;; WARNING: recursion requested but not available
  
  ;; QUESTION SECTION:
  ;alert.cm.            IN    NS
  
  ;; Query time: 51 msec
  ;; SERVER: 173.245.58.51#53(173.245.58.51)
  ;; WHEN: Tue Aug 23 23:09:00 2016
  ;; MSG SIZE  rcvd: 26

As can be seen in the above [dig](https://en.wikipedia.org/wiki/Dig_%28command%29) output, the DigitalOcean nameservers returned a DNS [REFUSED (RCode 5)](https://support.opendns.com/entries/60827730-FAQ-What-are-common-DNS-return-or-response-codes-) error which indicates that the nameservers refused to respond to the NS record query we performed. This gives us an easy and lightweight way to differentiate between domains that are currently listed under a DigitalOcean account and domains that aren’t.

This solves one part of the problem, but checking every domain on the Internet this way is still very intensive. Additionally, how can we get a list of every domain name on the Internet? The answer is to get a copy of the zone files for various top level domains (TLDs). To start we’ll acquire the zone files for the .com and .net TLDs because they are easily [acquirable from Verisign for research purposes](https://www.verisign.com/en_US/channel-resources/domain-registry-products/zone-file/index.xhtml). The zone files contain every .com and .net domain in existence and their corresponding nameservers. By grepping through these zone files we can figure out exactly how many .com & .net domain names use DigitalOcean for DNS hosting. At the time of this writing, the count for both TLDs are the following:

  * **.com** : 170,829
  * **.net** : 17,101

Combined, this is a total of 187,930 domain names that have DigitalOcean as their DNS provider. We can now query all of these domains to check for DNS REFUSED errors to see if they are not listed under a DigitalOcean account (and are thus able to be taken over). After a short Python script and a few hours of DNS querying we are able to enumerate all of the vulnerable domains (at least in the two TLDs previously mentioned). The final count comes out to be 21,598 domains that returned a DNS REFUSED error upon querying them. After adding these domains to my DigitalOcean account [via their API](https://developers.digitalocean.com/), the real number turned out to be closer to ~19,500 domains (as it appears the DNS method was not 100% accurate). For all of the domains added to my account a single DNS A record for the base domain was added to a EC2 instance. This was done in hopes of understanding why so many domains ended up in this state, and the results were quite surprising.

## The Sinkholed Traffic

While I expected that most of the domains were purely spam/junk domains that had not yet been configured (perhaps all belonging to a single domain reseller for example) – this was not the case. The sinkhole server was just a standard nginx web server returning a blank webpage and logging web requests. After having the server up for just a few days the access logs have grown to 1.8GB in size with a constant stream of requests pouring in. Most of these are unsurprisingly from search engines eager to crawl the web as quickly as possible (~80% of the traffic was from spiders) however the rest are legitimate users navigating to the now redirected websites.

## DigitalOcean’s Response

After sinkholing the domains and proving that the theory was in fact true, I reached out to DigitalOcean’s security team describing the issue (using PGP [as specified by their security page](https://www.digitalocean.com/security/)). Their response was the following:

> Matthew,
> 
> Thank you for sending this in. This is a known workflow within our platform. We are committed to always improving our customer’s experience and have been examining ways of minimizing the type of behavior you are describing.
> 
> Regards,
> 
> Nick
> 
> —

> Nicolas [REDACTED] [[email protected]](/cdn-cgi/l/email-protection)

So essentially they’re aware and _may_ be looking for ways to mitigate this behaviour in the future but they don’t appear to be making any immediate plans.

Additionally my DigitalOcean account had been locked. This prevented me from the next logical step: changing all the DNS to point to 127.0.0.1 – effectively neutering the traffic. When asking support why my account had been locked (though I had some idea) I received the following response:

> There has been a response to your ticket:
> 
> Hi there,
> 
> We have reviewed your account, and we are not able to provide further service.
> 
> I understand this may be inconveniencing, but we are not going to be able to provide you hosting services.
> 
> This is a final decision and is not subject to change.
> 
> Regards,

> Cash [REDACTED] Trust & Safety Specialist

> Digital Ocean Support

So no reasoning for the ban and there would be no further support. This leaves me in the uncomfortable position of being stuck with all the traffic I’ve been sinkholing. Since I can’t access my account to change the domain’s DNS, I’m stuck receiving thousands of requests a minute from various sites. I can’t tear down the EC2 sinkhole server because the Elastic IP may be re-allocated to someone more malicious so I have to pay to keep it up (for how long I’m not sure). While I’ve stopped all services on the server to protect the privacy of the users accidentally hitting these sites, and have [srm-ed](https://en.wikipedia.org/wiki/Srm_%28Unix%29) the access logs, I am unable to stop the flood of traffic going forward. Being in this awkward position, I reached out to DigitalOcean’s team to see if they can assist in deleting the domains from my account (sadly leaving them vulnerable again) or sinkholing the DNS to 127.0.0.1. I received a very helpful response from someone on the security team and it appears they will look into it.

## In Review

This provides some interesting insight as to why the pattern of using unique nameservers for importing domain names is so common (to prevent exactly this issue). It’s worthy to note that any system which uses non-unique nameservers for domain name importing is likely vulnerable to this exact same type of attack pattern (what about registrars? domain parking services?). Further research into this area is likely to yield similar results.

Until next time,

-mandatory

###### [Proofread by udanquu](https://twitter.com/udanquu)

[cloud dns](/tags#cloud dns "Pages tagged cloud dns")[digitalocean dns issue](/tags#digitalocean dns issue "Pages tagged digitalocean dns issue")[digitalocean domain vulnerability](/tags#digitalocean domain vulnerability "Pages tagged digitalocean domain vulnerability")[dns](/tags#dns "Pages tagged dns")[domain validation](/tags#domain validation "Pages tagged domain validation")[hosted dns](/tags#hosted dns "Pages tagged hosted dns") Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/keeping-positive-obtaining-arbitrary-wildcard-ssl-certificates-from-comodo-via-dangling-markup-injection/)

### ["Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

**NOTE:** *If you're just looking for the high level points, see the"[The TL;DR Summary & High-LevelPoints](#the-tldr-summary--high-level...… [Continue reading](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

#### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Published on February 22, 2019

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018

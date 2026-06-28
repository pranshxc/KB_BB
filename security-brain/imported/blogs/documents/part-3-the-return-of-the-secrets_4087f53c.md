---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_part-3-the-return-of-the-secrets.md
original_filename: 2022-05-06_part-3-the-return-of-the-secrets.md
title: 'Part 3: The return of the secrets'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- cloud-security
- sso
- otp
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- cloud-security
- sso
- otp
language: en
raw_sha256: 4087f53cf329890e3685793c07f92b09ea5d56c107b62c7438d783687ef39663
text_sha256: 86382b5eeb324585853ef57b78634f8d297b261b3da1ac9f8e00b012b68a3ea8
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Part 3: The return of the secrets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_part-3-the-return-of-the-secrets.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, cloud-security, sso, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `4087f53cf329890e3685793c07f92b09ea5d56c107b62c7438d783687ef39663`
- Text SHA256: `86382b5eeb324585853ef57b78634f8d297b261b3da1ac9f8e00b012b68a3ea8`


## Content

---
title: "Part 3: The return of the secrets"
page_title: "Cloudflare Pages, part 3: The return of the secrets"
url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-3-the-return-of-the-secrets"
final_url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-3-the-return-of-the-secrets"
authors: ["Sean Yeoh (@seanyeoh)", "James Hebden (@devec0)"]
programs: ["Cloudflare"]
bugs: ["Command injection", "Container escape", "Bash Path injection", "RCE", "Local Privilege Escalation", "Information disclosure"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2658
---

[Research Notes](/resources/research)

Security Research

May 6, 2022

# Cloudflare Pages, part 3: The return of the secrets

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![Bart Simpson sliding down a staircase, before falling off the railing and hitting each stair on the way down. bart is labelled with the words 'cloudflare pages' and the steps are labeled with various security issues.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659feb72bf22b29b278079d0_bart-slide.png)

  * [Introduction](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#introduction)
  * [Let’s try this again](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#lets-try-this-again)
  * [Now, with added Kubernetes!](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#now-with-added-kubernetes)
  * [Scanning & The Network Boundaries](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#scanning--the-network-boundaries)
  * [The Kubelet API: Git secrets redux](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#the-kubelet-api-git-secrets-redux)
  * [Conclusion](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/#conclusion)

### Introduction

Following on from our 2nd story, we’ll be continuing the epic tale of our research into Cloudflare pages in this third installment. If you haven’t read part 1&2, you can read them [here](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/) and [here](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/).

We pick up where we left off, after escaping from container jail, and with Cloudflare concluding the best way forward was to re-architect the platform.

### Let’s try this again

Many months passed. We continued to discuss the vulnerabilities we found and the remediation with Cloudflare, who were very receptive, and in addition to applying fixes to the vulnerabilities we found very quickly, spent these months working on the rearchitected platform. Initially, we were asked if we would be interested in testing their new platform - which we gladly accepted, and then things went quiet for a while. One day, several months ago, the Cloudflare program received an update indicating they had a new pages environment that HackerOne users could opt-in to. Was this the new environment we were discussing with them? It was early on a Saturday morning, but James was up when the message came through, messaged Sean, and then started poking around. This probably means they’re secure now right?

### Now, with added Kubernetes!

At this point, we were excited to make bank take another look at the infra, and eagerly hopped on and threw another reverse shell into the repo, targetting the new opt-in re-architected environment.

Diving in, we immediately noticed some big and obvious changes:

  * We couldn’t see the build scripts. The new user has no permission to read them. Good!
  * We’re in GKE. Kubernetes, a totally different cloud and infrastructure this time. Oof.
  * We’re in a gVisor container as a non-root user! Excellent!
  * We have access to k8s API endpoints, with anonymous role, which isn’t useful by itself.
  * We have no access to instance metadata, Great!

First and foremost, Cloudflare had evidently learnt from their mistakes in letting users like us read the implementation and audit the source for vulnerabilities. So having all the scripts and resources locked down meant we were now flying blind in terms of how the other steps worked and auditing any source for easy command injection bugs. As a researcher, this is a total bummer.

Secondly, running directly on GKE meant a few things:

  * We have moved off Azure entirely, so no more pipeline shenanigans
  * GKE security, if enabled properly, cuts off a lot of avenues for potential privilege escalation in the cluster (<https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity>). Workload identity installs a metadata API proxy in addition to a number of other security features, severely limiting our ability to leak tokens or secrets via the metadata API.

And finally, they started using gVisor. For the uninitiated gVisor is a container runtime like containerd (powering docker), that provides significant defense in depth. It effectively operates as a syscall proxy and emulation layer, limiting which syscalls and what arguments to syscalls can actually reach the kernel by emulating syscalls, and evaluating them against a granted set of capabilities. Think of it as only being able to access the kernel via a proxy server with a very, very strict access control list.

With these mitigations in place, we set out on another adventure returning the ring to Mordor escalating our privileges and farming some secrets.

### Scanning & the network boundaries

We began by port scanning and identifying open services we could find from the reverse shell we spawned in the build script. Typically in a locked down kubernetes environment, we expect this to yield very little with appropriate network policies ([https://kubernetes.io/docs/concepts/services-networking/network-policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)) in place, and we certainly shouldn’t be able to find any control plane services beyond those needed to operate the build.

We identified our pod’s IP address from the network configuration accessible from our shell, and began scanning adjacent hosts on the same subnet. We started with the .1 address in the subnet, as in a Kubernetes/Docker environment, this is normally the host.

Scanning 10.124.165.1 [65535 ports]

Discovered open port 22/tcp on 10.124.165.1

Discovered open port 10256/tcp on 10.124.165.1

Discovered open port 10250/tcp on 10.124.165.1

Discovered open port 2020/tcp on 10.124.165.1

Discovered open port 10255/tcp on 10.124.165.1

Discovered open port 31501/tcp on 10.124.165.1

Discovered open port 2021/tcp on 10.124.165.1

‍

Completed Connect Scan at 00:06, 4.79s elapsed (65535 total ports)

‍

Nmap scan report for 10.124.165.1

Host is up, received user-set (0.0035s latency).

Scanned at 2022-01-22 00:06:18 UTC for 5s

Not shown: 65528 closed ports

Reason: 65528 conn-refused

PORT STATE SERVICE REASON

22/tcp open ssh syn-ack

2020/tcp open unknown syn-ack

2021/tcp open unknown syn-ack

10250/tcp open unknown syn-ack

10255/tcp open unknown syn-ack

10256/tcp open unknown syn-ack

31501/tcp open unknown syn-ack

Evident from our brief scanning attempts, we could see multiple ports responding on the host. Diving through each port yielded varying degrees of information.

Some targets would respond with a straight 404 -

curl 10.124.165.1:2021 -v

* Rebuilt URL to: 10.124.165.1:2021/

* Trying 10.124.165.1...

* Connected to 10.124.165.1 (10.124.165.1) port 2021 (#0)

>GET / HTTP/1.1

>Host: 10.124.165.1:2021

>User-Agent: curl/7.47.0

>Accept: *_/*_

>

<HTTP/1.1 404 Not Found  

<Content-Type: text/plain; charset=utf-8

<X-Content-Type-Options: nosniff

<Date: Sat, 22 Jan 2022 00:07:10 GMT

<Content-Length: 19

<

404 page not found

* Connection #0 to host 10.124.165.1 left intact

While others would provide an inkling of information about what was running
  
  
  buildbot@build-prod-3330469-v7jkn:~/repo$ curl 10.124.165.1:2020 -v
  curl 10.124.165.1:2020 -v
  * Rebuilt URL to: 10.124.165.1:2020/
  *  Trying 10.124.165.1...
  * Connected to 10.124.165.1 (10.124.165.1) port 2020 (#0)
  > GET / HTTP/1.1
  > Host: 10.124.165.1:2020
  > User-Agent: curl/7.47.0
  > Accept: */*
  >
  < HTTP/1.1 200 OK
  < Server: Monkey/1.7.0
  < Date: Sat, 22 Jan 2022 00:07:02 GMT
  < Transfer-Encoding: chunked
  <
  * Connection #0 to host 10.124.165.1 left intact
  {"fluent-bit":{"version":"1.5.7","edition":"Community","flags":["FLB_HAVE_PARSER","FLB_HAVE_RECORD_ACCESSOR","FLB_HAVE_STREAM_PROCESSOR","FLB_HAVE_TLS","FLB_HAVE_AWS","FLB_HAVE_SIGNV4","FLB_HAVE_SQLDB","FLB_HAVE_METRICS","FLB_HAVE_HTTP_SERVER","FLB_HAVE_SYSTEMD","FLB_HAVE_FORK","FLB_HAVE_TIMESPEC_GET","FLB_HAVE_GMTOFF","FLB_HAVE_UNIX_SOCKET","FLB_HAVE_PROXY_GO","FLB_HAVE_SYSTEM_STRPTIME","FLB_HAVE_JEMALLOC","FLB_HAVE_LIBBACKTRACE","FLB_HAVE_REGEX","FLB_HAVE_UTF8_ENCODER","FLB_HAVE_LUAJIT","FLB_HAVE_C_TLS","FLB_HAVE_ACCEPT4","FLB_HAVE_INOTIFY"]}}
  
  

We then realised we had confirmed our suspicion: we were seeing the various monitoring and internal services running within the cluster, on the host. After probing around manually, these services didn’t have much in the way of useful information or privileged access we could use to escape our confinement again. We had to change our strategy. These ports would be running services that had specific and limited API paths and functionality, often just what looked to be golang binaries serving API endpoints. Our next steps meant discovering and understanding what the service was on these ports - without additional detail this was going to be challenging. Thankfully, with the power of [Kiterunner](https://github.com/assetnote/kiterunner) we were able to easily enumerate common API endpoints.

We set up Kiterunner and pointed it at each of the open ports we had identified, and we identified one very interesting endpoint on the host, on port 10255. The endpoint was named /pods, and a quick Google will quickly confirm this is the internal kubelet API used by Kubernetes.

### The Kubelet API: git secrets redux

This API is different to the actual Kubernetes API, in that it does not have the ability to modify Kubernetes objects. Looking over the output, we did however notice we could dump the details of each pod running on the host.

curl -v -k http://10.124.200.1:10255/pods

Given we are computer hackers by trade and inclination, we grepp’ed this output for CREDS and found GIT_CREDS. At this point, it started to feel like we might be experiencing an atomic level bout of deja vu:

![a screenshot showing kubernetes secrets for the build pods, including the git secrets used to access the repo for the build](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659ff27046342fbc07060a78_k8s-secrets.png)

Testing these Git credentials, thankfully we were only able to see our private repositories this time. But, we still have private repository access from without our org, which is potentially sensitive for large organisations with multiple private repositories. We pushed on to see if we could take this further and increase the scope of the finding.

We ran an nmap for port 10255 across 10.124.0.0/16 just in case we could access any other tenants or hosts. We found a number of different hosts accessible providing the same data, indicating that if other builds were being run anywhere in this GKE account for other users and organisations, we could also steal their Git credentials. As Sean said in the HackerOne report -

“guess who’s back. back again. shady’s back. call a friend” –eminem

### Conclusion

Cloudflare reacted quickly and remediated this issue, presumably by a judicious application of iptables rules, or pod network security policies - we’re not sure of the exact remedy because they’d changed the locks again, and we were stuck outside. Once appropriate network isolation was in place, the problem was effectively mitigated.

So, if you’re still with us at this point in the epic, as a final takeaway for defenders -

  * In complex network environments, ensure appropriate network segregation and firewalling is in place that reflects the various security boundaries of your application.

In this case, it would be enough to ensure different tenant networks were isolated at build time. However, preventing all communication from pod to host was a more effective and airtight fix.

Once again we’d like to thank Cloudflare for being really receptive to the reports we sent in, open to remediation advice, and communicative throughout the process of fixing these problems. They showed a very thorough approach to fixing these issues and even re-architected the entire platform, which shows a commitment to the safety of their customers. We’d also like to thank HackerOne for being quick to triage and reproduce these bugs, as well as being an excellent intermediary between us and Cloudflare in the early stages of these reports.

This writeup was written in multiple parts, to read previous parts: [part 1](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/), [part 2](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/), and [part 3](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/).

Written by:

James Hebden

Sean Yeoh

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

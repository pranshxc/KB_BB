---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-09_subdomain-takeover-yet-another-starbucks-case.md
original_filename: 2018-08-09_subdomain-takeover-yet-another-starbucks-case.md
title: 'Subdomain Takeover: Yet another Starbucks case'
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: cd12f08988540a2c3e674411dbf3af7aa3455b61d522e5f76fc2321d802fd022
text_sha256: d3e21003a7bbefa3d90b46cdc0dbb39ee383c63baadfdc35e68e55d8a74cc8db
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Takeover: Yet another Starbucks case

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-09_subdomain-takeover-yet-another-starbucks-case.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `cd12f08988540a2c3e674411dbf3af7aa3455b61d522e5f76fc2321d802fd022`
- Text SHA256: `d3e21003a7bbefa3d90b46cdc0dbb39ee383c63baadfdc35e68e55d8a74cc8db`


## Content

---
title: "Subdomain Takeover: Yet another Starbucks case"
url: "https://0xpatrik.com/subdomain-takeover-starbucks-ii/"
final_url: "https://0xpatrik.com/subdomain-takeover-starbucks-ii/"
authors: ["Patrik Hudak (@0xpatrik)"]
programs: ["Starbucks"]
bugs: ["Subdomain takeover"]
bounty: "2,000"
publication_date: "2018-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5760
---

# Subdomain Takeover: Yet another Starbucks case

[ ![Patrik Hudak](https://0xpatrik.com/content/images/2020/04/IMG_6789.jpg) ](https://twitter.com/0xpatrik)

Recently, I was repeatedly [awarded](https://hackerone.com/reports/388622) $2,000 bounty for subdomain takeover on [Starbucks](https://hackerone.com/starbucks). You may remember my [post](https://0xpatrik.com/subdomain-takeover-starbucks/) about bug bounty report where I described how to subdomain takeover was possible using Azure. This case was pretty similar. However, I had to use another Azure service called _Traffic Manager_. In this post, I explain the step-by-step process for the proof of concept.

![Report](https://0xpatrik.com/content/images/2018/08/report.png)

On Monday evening, I noticed that `wfmnarptpc.starbucks.com` responds with `NXDOMAIN`. The more interesting fact was that it has CNAME set to `s00149tmppcrpt.trafficmanager.net`. From experience, I knew that this has a perfect chance of being a subdomain takeover. As you may remember, Azure mostly uses dedicated IP addresses, so when CNAME to Azure responds with `NXDOMAIN`, your bug bounty radar should be on.

Previously, I haven't mentioned that `trafficmanager.net` is also one of the domains where subdomain takeover is possible. Let's look at what is [Traffic Manager](https://docs.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview) about:

_"Microsoft Azure Traffic Manager allows you to control the distribution of user traffic for service endpoints in different datacenters. [...] You can also use Traffic Manager with external, non-Azure endpoints."_
  
  
  $ dig a wfmnarptpc.starbucks.com
  
  ; <<>> DiG 9.10.6 <<>> a wfmnarptpc.starbucks.com
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 20251
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
  
  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 4096
  ;; QUESTION SECTION:
  ;wfmnarptpc.starbucks.com.	IN	A
  
  ;; ANSWER SECTION:
  wfmnarptpc.starbucks.com. 33165	IN	CNAME	s00149tmppcrpt.trafficmanager.net.
  

Simply put, there is some domain which has link to non-existing subdomain of `trafficmanager.net`. To prove our point, we need to registered the previously removed asset in Azure. Thankfully (for us), Azure is not doing any domain ownership verification :-)

You may [remember](https://0xpatrik.com/subdomain-takeover-basics/) that this situation is still not the winning point since there might be disabled configuration with this subdomain in Azure. In this case, even though _externally_ it seems that takeover is possible, PoC creation would fail.

I started by creating a new Traffic Manager profile in the Azure portal:

![Traffic Manager profile creation](https://0xpatrik.com/content/images/2018/08/trafficmanager-create.png)

Nice! At this point, I knew that the subdomain takeover is possible. The `s00149tmppcrpt.trafficmanager.net` is available; I can take it and progress with PoC. Now I needed to point the domain to one of the servers that I own:

![Traffic Manager endpoint creation](https://0xpatrik.com/content/images/2018/08/endpoint.png)

The only thing left was to create a new [virtual host](https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/) on my endpoint:

![VHost Starbucks](https://0xpatrik.com/content/images/2018/08/vhost-1.png)

Time well spent. Thank you very much.

![Subdomain takeover PoC](https://0xpatrik.com/content/images/2018/08/poc.png)

Until next time!

[Patrik](https://twitter.com/0xpatrik)  
[Follow @0xpatrik](https://twitter.com/0xpatrik?ref_src=twsrc%5Etfw)

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](http://buymeacoff.ee/0xpatrik)

[ ![Patrik Hudak](https://0xpatrik.com/content/images/2020/04/IMG_6789.jpg) ](https://twitter.com/0xpatrik)

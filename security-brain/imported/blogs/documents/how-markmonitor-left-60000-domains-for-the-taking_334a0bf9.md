---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_how-markmonitor-left-60000-domains-for-the-taking.md
original_filename: 2021-08-29_how-markmonitor-left-60000-domains-for-the-taking.md
title: How MarkMonitor left >60,000 domains for the taking
category: documents
detected_topics:
- automation-abuse
- cloud-security
- command-injection
- api-security
tags:
- imported
- documents
- automation-abuse
- cloud-security
- command-injection
- api-security
language: en
raw_sha256: 334a0bf9ecc818c3ad923775d53abff0b68e1132e5350f6c49d2bbedf25f05bc
text_sha256: aaabea3b980872081550f859cbe969287b5cd1aa94981b0886d6016f887a01fd
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How MarkMonitor left >60,000 domains for the taking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_how-markmonitor-left-60000-domains-for-the-taking.md
- Source Type: markdown
- Detected Topics: automation-abuse, cloud-security, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `334a0bf9ecc818c3ad923775d53abff0b68e1132e5350f6c49d2bbedf25f05bc`
- Text SHA256: `aaabea3b980872081550f859cbe969287b5cd1aa94981b0886d6016f887a01fd`


## Content

---
title: "How MarkMonitor left >60,000 domains for the taking"
url: "https://ian.sh/markmonitor"
final_url: "https://ian.sh/markmonitor"
authors: ["Ian Carroll (@iangcarroll)"]
bugs: ["Subdomain takeover"]
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3372
---

**_Thanks to_****[ _Nagli_](https://twitter.com/naglinagli)**** _and_****[ _d0xing_](https://twitter.com/d00xing)**** _for helping figure out what was happening with this issue._**

I participate in a lot of bug bounty programs, where I try to automate the discovery of as many security issues as possible. Many companies do not know all of the assets that they have on the internet. When you know their attack surface better than them, you can find a lot of otherwise trivial issues.

One of the easiest types of issues to automatically discover are [_subdomain takeovers_](https://developer.mozilla.org/en-US/docs/Web/Security/Subdomain_takeovers), where a DNS record or a load balancer points traffic towards an unknowing third party. If [`testing.example.com`](http://testing.example.com) is pointed towards Amazon S3, what will S3 do if that bucket hasn't been created yet? It will just throw a 404 error — and wait for someone to claim it.

If we claim this domain inside S3 before `example.com`'s owners do, then we can claim the right to use it with S3 and upload anything we want. By necessity, the ability to serve HTML and JavaScript is pretty impactful to the web platform — it bypasses SameSite for that domain, allows reading and setting unprotected and widely-scoped cookies, etc.

Knowing this, I was very surprised to see hundreds of alerts from my automation in a few minutes — all claiming to have successfully captured S3 buckets for root domains belonging to major companies. Thinking I had broken it and it had gone off the rails, I quickly took a look and noticed that it had indeed worked, and my content was being served on a ton of domains with bug bounty programs.

## A lot of buckets

At this point I had no idea what to do — why were there so many impacted domains across many organizations, and how was I even going to submit all of these issues? However, I noticed that the domains were slowly being changed to a MarkMonitor parked domain page.

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/00276c4d-7bb9-45f1-8098-7745472c09f9/Untitled/w=1920,quality=90,fit=scale-down)

![Protection is unclear](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/20f12a22-f440-4bf1-8955-dd2a78e3bfc5/Untitled/w=1920,quality=90,fit=scale-down)_Protection is unclear_

It became clear that these were all parked domains with varying degrees of use, and they were all registered via MarkMonitor. This is a bit surprising, because MarkMonitor sells themselves as the domain registrar that does not make mistakes. It would be hard to understate the cost of losing domains for a tech company — anything that is pointed to them will immediately begin directing their traffic elsewhere. MarkMonitor is not a cheap solution to this problem, but it is widely used (apparently by "more than half of the Fortune 100", per the page).

I sent a few bug bounty reports to companies that were most impacted by this issue, but these domains were in an indeterminate state and it was hard to prove there was an issue. While many domains began responding with an S3 404, others began switching from S3 to the parked page. What is interesting is that DNS was not involved — all domains pointed to `93.191.168.52` both before and after the issue.

After I sent an email to `security@markmonitor.com` that went unacknowledged, domains stopped pointing to S3 over an hour after it began. I claimed over 800 root domains in this timeframe, and other researchers had similar amounts of claimed domains.

## Broader impact

Many companies — including MarkMonitor themselves — do not run a vulnerability disclosure or bug bounty program, so they are not included in my scanning and would not have been detected. Luckily, since all of these domains use a static IP address, we can see exactly how many domains on the internet were pointed to the vulnerable service.

![SecurityTrails data of affected domains sorted by Alexa rank](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcd345f-010a-4e8c-874b-efb3e2ea014e/Untitled/w=1920,quality=90,fit=scale-down)SecurityTrails data of affected domains sorted by Alexa rank

SecurityTrails offers a simple SQL browser we can use to look for all of these domains. In total, it identified over **62,000 domains** pointed to MarkMonitor's parking service.

Some amazing entries are in here, including `google.ar` and `coinbase.ca`. Suffice to say, these would have been great targets for phishing.

Even though this only lasted for an hour, this is enough to perform impactful attacks like claiming a TLS certificate for the entire domain. It could then be MiTM'd in the future if, for example, Coinbase began operating in Canada.

## Preventing this from happening

MarkMonitor does not have a way of disclosing security issues, which inhibited reporting this to them in a timely manner. They have not responded to any of our communications.

This issue is not entirely the fault of MarkMonitor. While they need to be careful with handling parked domains, AWS is at fault for not being more stringent with claiming S3 buckets. Google Cloud, for example, has [required domain verification](https://cloud.google.com/storage/docs/domain-name-verification) for years, rendering this useless.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-03_hijacking-email-with-cloudflare-email-routing.md
original_filename: 2022-08-03_hijacking-email-with-cloudflare-email-routing.md
title: Hijacking email with Cloudflare Email Routing
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- automation-abuse
- api-security
language: en
raw_sha256: 082ccac749fbf0fc14799bbd44f62f8aa5c0ca144762108d4ae625fbe8832c03
text_sha256: 8ca04ef557fdbcf5a4a48cbbf0f8d6ea711f39a0af517c9aaa67cdef9d1b60c2
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking email with Cloudflare Email Routing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-03_hijacking-email-with-cloudflare-email-routing.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `082ccac749fbf0fc14799bbd44f62f8aa5c0ca144762108d4ae625fbe8832c03`
- Text SHA256: `8ca04ef557fdbcf5a4a48cbbf0f8d6ea711f39a0af517c9aaa67cdef9d1b60c2`


## Content

---
title: "Hijacking email with Cloudflare Email Routing"
page_title: "Hijacking email with Cloudflare Email Routing | Albert Pedersen"
url: "https://albertpedersen.com/blog/hijacking-email-with-cloudflare-email-routing/"
final_url: "https://albertpedersen.com/blog/hijacking-email-with-cloudflare-email-routing/"
authors: ["Albert Pedersen (@AlbertSPedersen)"]
bugs: ["HTTP response manipulation", "Privilege escalation"]
publication_date: "2022-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2367
---

#  Hijacking email with Cloudflare Email Routing 

August 3, 2022 · Albert Pedersen 

On Tuesday, December 7th 2021 I discovered a critical vulnerability in Cloudflare’s Email Routing service. This vulnerabilty enabled anyone to modify the routing configuration of any domain using the service. A bad actor could have overwritten the destination address to their own email address in order to read any email sent to the victim’s domain. The bug has since been fixed and Cloudflare has kindly allowed me to publish this write-up. [View the report on HackerOne](https://hackerone.com/reports/1419341).

## The beta#

Cloudflare Email Routing was in closed beta back when I discovered this vulnerability, with only a few domains having been granted access. Sadly, I was not invited to the party, so I was simply going to have to crash it instead.

When the Cloudflare dashboard is loaded, a request is made to `https://dash.cloudflare.com/api/v4/zones/<zone_tag>/flags`. The response includes several properties that affect which features appear in the dashboard, and one of them is for the Email Routing beta.
  
  
  {
  "email": {
  "beta": false,
  "visible": false
  }
  }
  

I used Burp to intercept the response and replace `"beta": false` with `"beta": true`, which made the dashboard think I had been given access to the beta.
  
  
  {
  "email": {
  "beta": true,
  "visible": false
  }
  }
  

I assumed there would be server-side checks to prevent me from actually setting up Email Routing, but this turned out not to be the case. The restrictions were all client-side as the API did not check whether I’d been given access to the beta. I was able to successfully set up Email Routing on one of my domains which I’ll refer to it as `example.com` from now on. Any email sent to e.g. `albert@example.com` would now be forwarded to my personal Gmail address.

## The bug#

After having bypassed the beta restrictions and successfully configured Email Routing, I wondered what would happen if I tried to set up Email Routing on an unverified zone. I assumed either the API would throw an error or the configuration simply would not take effect, but of course I had to test it.

An unverified/pending zone is a domain that has been added to your Cloudflare account, but that you have not yet pointed to your assigned name servers to verify ownership. Any changes you make to this zone, such as modifying DNS records or enabling features, should not take effect until you verify ownership. A domain can only be active in a single Cloudflare account, but it can be unverified/pending in several accounts at a time.

To test this, I added `example.com` to my secondary Cloudflare account. `example.com` was now present in both my primary and secondary account, but it was only verified in my primary account. I followed the steps to set up Email Routing just like before, but this time I entered a different email address as the destination. This way any hijacked email would land in a different inbox and I would clearly be able to tell whether it had worked.

I sent an email to `albert@example.com` and waited… but nothing happened. Apparently my email client had just been slow to update, because after a few minutes the email landed in the inbox of the rogue destination address rather than my personal Gmail address. I have to say I was quite surprised as I really didn’t expect this to work. When I set up Email Routing for `example.com` on my secondary Cloudflare account, the original routing configuration for `example.com` was overwritten with my rogue settings.

## The impact#

By exploiting this vulnerability a bad actor would’ve been able to:

  * Read email sent to the target domain by forwarding it to a rogue destination address
  * Prevent email sent to the target domain from arriving at the original destination address

Not only is this a huge privacy issue, but due to the fact that password reset links are often sent to the email address of the user, a bad actor could also potentially gain control of any accounts linked to that email address. This is a good example of why you should be using 2-factor authentication.

Due to the fact that you cannot change DNS records for a pending zone, the domain had to already be using Cloudflare Email Routing. I suspect that Cloudflare’s mail server only keeps a single record for each address, and that it was simply overwritten when I applied my rogue settings.

Unfortunately (or fortunately, depending on your motives), it is quite easily find a list of domains that use Cloudflare Email Routing and [SecurityTrails](https://securitytrails.com/list/mx/amir.mx.cloudflare.net) is a good example of that. There were around 600 domains on the list at the time of finding, and all of them could’ve had their email hijacked if this was discovered by a bad actor.

## The timeline#

I managed to hijack the first email at 18:03 which led me to investigate further. At 18:44, after having reproduced the bug on multiple accounts and domains, I was able to confirm there was definitely an issue and started writing my report. Following is the HackerOne report timeline in CEST.

  * 2021-12-07 20:11 - Report submitted
  * 2021-12-08 18:53 - First response
  * 2021-12-09 15:10 - Report triaged
  * Fix implemented by Cloudflare
  * 2021-12-13 21:59 - Bounty awarded
  * 2021-12-14 11:46 - Report resolved
  * 2022-07-28 18:35 - Report disclosed

## Conclusion#

Thanks to Cloudflare for reacting quickly to my bug report and for driving transparency by allowing me to publish this write-up. If you believe you’ve found a vulnerability in one of Cloudflare’s products or services, please submit a report to [Cloudflare Bug Bounty](https://hackerone.com/cloudflare) on HackerOne.

  * [bug-bounty](https://albertpedersen.com/tags/bug-bounty/)
  * [cloudflare](https://albertpedersen.com/tags/cloudflare/)
  * [disclosure](https://albertpedersen.com/tags/disclosure/)
  * [email](https://albertpedersen.com/tags/email/)
  * [email-routing](https://albertpedersen.com/tags/email-routing/)
  * [vulnerability](https://albertpedersen.com/tags/vulnerability/)

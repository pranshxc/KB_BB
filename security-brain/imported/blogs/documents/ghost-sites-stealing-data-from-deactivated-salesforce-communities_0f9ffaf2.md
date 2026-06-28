---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-31_ghost-sites-stealing-data-from-deactivated-salesforce-communities.md
original_filename: 2023-05-31_ghost-sites-stealing-data-from-deactivated-salesforce-communities.md
title: 'Ghost Sites: Stealing Data From Deactivated Salesforce Communities'
category: documents
detected_topics:
- cloud-security
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 0f9ffaf2096432178211b2208fbc1449a0c6613da556473e2c5fb6161bca782f
text_sha256: a76c293c93289f2e40e7375c5c3d0a599eef4e2ed1b832b741e329d4a7b547b4
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Ghost Sites: Stealing Data From Deactivated Salesforce Communities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-31_ghost-sites-stealing-data-from-deactivated-salesforce-communities.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `0f9ffaf2096432178211b2208fbc1449a0c6613da556473e2c5fb6161bca782f`
- Text SHA256: `a76c293c93289f2e40e7375c5c3d0a599eef4e2ed1b832b741e329d4a7b547b4`


## Content

---
title: "Ghost Sites: Stealing Data From Deactivated Salesforce Communities"
url: "https://www.varonis.com/blog/salesforce-ghost-sites"
final_url: "https://www.varonis.com/blog/salesforce-ghost-sites"
authors: ["Nitay Bachrach"]
bugs: ["Salesforce", "Security misconfiguration"]
publication_date: "2023-05-31"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1098
---

Varonis Threat Labs discovered that improperly deactivated and unmaintained Salesforce "ghost sites” remain accessible and vulnerable to risk. By manipulating the host header, threat actors can gain access to sensitive PII and business data.

Salesforce Sites allow you to create customized communities, enabling partners and customers to collaborate within a company’s Salesforce environment.

When these communities are no longer needed, though, they are often set aside but not deactivated. Because these unused sites are not maintained, they aren’t tested against vulnerabilities, and admins fail to update the site’s security measures according to newer guidelines.

Varonis Threat Labs discovered that many of these improperly deactivated Salesforce Sites are still pulling fresh data and are easily found, accessible, and exploitable by attackers. We dubbed these abandoned, unprotected, and unmonitored Salesforce Communities “ghost sites.”

In this blog, we’ll show you how these ghost sites manifest, how to locate them, and how an attacker can use a simple exploit to access them.

## Where do ghost sites come from?

The creation of a ghost site starts with custom domain names.

Instead of using unappealing internal URLs like “acmeorg.my.site.com/partners,” companies create custom domains so partners can browse "partners.acme.org” instead. This is accomplished by configuring the DNS record so that “partners.acme.org” points to the lovely, curated Salesforce Community Site at “ _partners.acme.org. 00d400.live.siteforce.com._ ”

Note that the new DNS record should have a CNAME entry that points to your FQDN, followed by the organization ID, followed by.live.siteforce.com. With the DNS record changed, partners visiting “partners.acme.org” will be able to browse Acme’s Salesforce site.

The trouble begins when Acme decides to choose a new Community Site vendor.

## Birth of a ghost site

Like any other technology, companies might replace a Salesforce Experience Site with an alternative.

Subsequently, Acme modifies the DNS record of “partners.acme.org” to point toward a new site that might run in their AWS environment, for example, instead of “ _partners.acme.org.00d400.live.siteforce.com_.”

From the users’ viewpoint, the Salesforce Site is gone, and a new community page is available. The new page might be completely disconnected from Salesforce, not running in the environment, and no obvious integrations are detectable.

Varonis Threat Labs researchers discovered that many companies stop at just modifying DNS records. They do not remove the custom domain in Salesforce, nor do they deactivate the site. Instead, the site continues to exist, pulling data and becoming a ghost site.

## Speaking with ghost sites

Now that Acme’s domain no longer points toward Salesforce, simply calling in endpoints such as Aura will not work.![aura-not-working-1](https://www.varonis.com/hs-fs/hubfs/aura-not-working-1.jpg?width=1266&height=993&name=aura-not-working-1.jpg)

![aura-working-2](https://www.varonis.com/hs-fs/hubfs/aura-working-2.jpg?width=1266&height=993&name=aura-working-2.jpg)

But because ghost sites are still active in Salesforce, the _siteforce_ domain still resolves, meaning it’s available under the right circumstances. A straightforward GET request results in an error — but there is another way to gain access.

Attackers can exploit these sites by simply changing the host header. This would trick Salesforce into believing that the site was accessed as https://partners.acme.org/ and that Salesforce would serve the site to the attacker.

![regular-site-3](https://www.varonis.com/hs-fs/hubfs/regular-site-3.jpg?width=1266&height=993&name=regular-site-3.jpg)

While it’s true that these sites are also accessible using the full internal URLs, these URLs are difficult for an external attacker to identify. However, using tools that index and archive DNS records — such as SecurityTrails and similar tools — make identifying ghost sites much easier.

Adding to the risk is the fact that old, obsolete sites are less maintained and, therefore, less secure, increasing the ease of an attack.

## Ghost site secrets

Our research found many such sites with confidential data, including PII and sensitive business data that were not otherwise accessible. The exposed data is not restricted to only old data from when the site was in use; it also includes new records that were shared with the guest user due to the sharing configuration in their Salesforce environment.

## Exorcising ghost sites

To solve the problem of ghost sites — and to mitigate other threats — sites that are no longer in use should be deactivated. It’s important to keep track of all Salesforce sites and their respective users’ permissions — including both community and guest users. Varonis Threat Labs created a guide for protecting your active Salesforce Communities against recon and data theft, and you can read more about keeping sensitive Salesforce data safe [here](https://www.varonis.com/blog/abusing-salesforce-communities?hsLang=en). 

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Nitay Bachrach](https://www.varonis.com/hubfs/nitay-bachrach.jpg)

Nitay Bachrach Nitay is a security researcher based in Tel Aviv, but you might encounter him anywhere in world. He is a cloud security expert, highly experienced in offensive security operations and reverse engineering. Nitay’s expertise also includes IoT devices, Linux, and local network security.

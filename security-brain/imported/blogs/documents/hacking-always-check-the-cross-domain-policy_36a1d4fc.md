---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-19_hacking-always-check-the-cross-domain-policy.md
original_filename: 2020-03-19_hacking-always-check-the-cross-domain-policy.md
title: Hacking — Always Check the Cross-domain Policy
category: documents
detected_topics:
- command-injection
- csrf
tags:
- imported
- documents
- command-injection
- csrf
language: en
raw_sha256: 36a1d4fcb6dacbc7bec3e8f13ae89c42d3a8b379b47392768a86dac60137d075
text_sha256: 8329c0caef234d6f2cb88a451ca662b191f37db86415030032473d2d86c6b78c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking — Always Check the Cross-domain Policy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-19_hacking-always-check-the-cross-domain-policy.md
- Source Type: markdown
- Detected Topics: command-injection, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `36a1d4fcb6dacbc7bec3e8f13ae89c42d3a8b379b47392768a86dac60137d075`
- Text SHA256: `8329c0caef234d6f2cb88a451ca662b191f37db86415030032473d2d86c6b78c`


## Content

---
title: "Hacking — Always Check the Cross-domain Policy"
url: "https://medium.com/the-volatile-triad/hacking-always-check-the-cross-domain-policy-369940372de3"
authors: ["Jack"]
programs: ["Starbucks"]
bugs: ["SOP bypass", "CSRF"]
bounty: "750"
publication_date: "2020-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4701
scraped_via: "browseros"
---

# Hacking — Always Check the Cross-domain Policy

Hacking — Always Check the Cross-domain Policy
Jack
Follow
2 min read
·
Mar 19, 2020

6

Twitter is a good example of a secure cross-domain policy

Concise tip: When testing a new target, always check their cross-domain policy, usually located at /crossdomain.xml! If you can find a subdomain/DNS takeover in a site within <allow-access-from> in that policy, you’ve just bypassed Same Origin Policy and may be in for a big bounty.

My report: https://hackerone.com/reports/244504

Get Jack’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One big thing to note is that if their policy is <allow-access-from domain=”*” />, they likely have other securities in place preventing CSRF/SOP bypass and this is not relevant.

Full story: When I began penetration testing, one approach I took was generally checking out configurations. I learned about a file on the root directory of many websites called crossdomain.xml. Any domains contained within <allow-access-from> tags in this policy can use flash files to access resources that are typically only accessible by the origin site. For example, see Twitter’s cross-domain policy. As you can see, they only allow access to these resources from *.twitter.com domains because resources like session cookies should not be shared with any other websites or the victim’s account could be compromised simply using CSRF.

In Starbuck’s case, they had many different domains in this file, one of them being *.example.com (we’ll say for confidentiality’s sake; this is an irrelevant detail anyway). I found that I could takeover a subdomain of example.com. Bingo — now I have ownership of a subdomain within Starbuck’s cross-domain policy! From here as an attacker you would need to perform CSRF in order to retrieve sensitive data like session cookies; this would involve making a flash file that just sent an HTTP request to a domain with the sensitive information stored on it and then logging the response which would contain all of the sensitive cookies due to the domain being included in the cross-domain policy.

To be entirely honest, when I found this in Starbucks, all I knew was that it was a configuration problem and I did not understand any of the technicalities behind it. I appreciate the Starbucks team being so open to my rather clueless self, and I learned more thoroughly after reporting it. In conclusion, always check the cross-domain policies of targets, because if they contain a wildcard for a domain with a subdomain takeover (and it’s not just a full wildcard * for any domain), they are likely in trouble.

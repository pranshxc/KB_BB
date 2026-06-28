---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-28_stored-cross-site-scripting-in-mediawiki.md
original_filename: 2022-01-28_stored-cross-site-scripting-in-mediawiki.md
title: Stored Cross-Site Scripting in MediaWiki
category: documents
detected_topics:
- xss
- access-control
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- access-control
- command-injection
- file-upload
language: en
raw_sha256: f708c7cf746451048f1aa798ad7634f18ab629731cd6d5d11c3c8c9d00242983
text_sha256: c7eb50b7b0f54fb43f15d4e9fb88ef8410f5b264ddd8086dc9b64f80e019d817
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Stored Cross-Site Scripting in MediaWiki

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-28_stored-cross-site-scripting-in-mediawiki.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `f708c7cf746451048f1aa798ad7634f18ab629731cd6d5d11c3c8c9d00242983`
- Text SHA256: `c7eb50b7b0f54fb43f15d4e9fb88ef8410f5b264ddd8086dc9b64f80e019d817`


## Content

---
title: "Stored Cross-Site Scripting in MediaWiki"
page_title: "Stored Cross-Site Scripting in MediaWiki — Machevalia"
url: "https://machevalia.blog/blog/stored-cross-site-scripting-in-mediawiki"
final_url: "https://machevalia.blog/blog/stored-cross-site-scripting-in-mediawiki"
authors: ["Nick Berrie (@machevalia)"]
bugs: ["Stored XSS"]
bounty: "1,090"
publication_date: "2022-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2962
---

# Stored Cross-Site Scripting in MediaWiki

[Bug Bounty](/blog/category/Bug+Bounty)[Write Ups](/blog/category/Write+Ups)

Jan 28

Written By [](/blog?author=63a1076f081fe62c6e3ae37b)

## MediaWiki wpTextBox1 Form Field Vulnerable to XSS

This post build on my [Access Control Violation](/machevalias-blog/access-control-violation-wiki-page-creation) write-up which was what I needed to conduct the exploit explained in this post. So, if you haven't read that one, check it out real quick (it's a short one).

After determining that I could create my own pages, forms, and edit content in various places such as media that had been uploaded to the server I started looking for stored XSS. I attempted a few of the standard XSS payloads that you might find on any of the big lists out there - [PortSwigger's](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)[ XSS payload list](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet), [Payloadbox's XSS-Payload-List](https://github.com/payloadbox/xss-payload-list), etc. 

* * *

NOTE: I only like a few payloads from those lists for initial tests so they end up my go-to's. I'm not someone who will spend an exorbitant amount of time going through each payload for XSS. In my experience, you generally don't need an extremely fancy payload unless you are going for a bypass. Additionally, I prefer to chase critical impact vulns and ones that require multi-stage attacks or complexity because XSS tends to get grabbed up quickly by other tests. Beyond that, they're just not as exciting as other vulns which are most of the reason I hunt. 

Due to this target being an older version of MediaWiki and there being so many [CVE's on MITRE for MediaWiki](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=mediawiki), I figured there was something there to be exploited to easily gain stored XSS. Digging through CVE reports I found some obscure links to old Red Hat Linux vulnerability verification threads. In one of the threads I found a link to <https://phabricator.wikimedia.org/T1137264> where the author explained that the MediaWiki parser for internal links was vulnerable to XSS using the payload:
  
  
  [[#%3Cscript%3Ealert(1)%3C/script%3E|

I found that this payload was successful in several areas such as in form creation, Wiki pages, and media description fields all under the _wpTextbox1_ form field. Using <https://xsshunter.com/> I crafted a payload to steal my own cookie just to demonstrate impact. This is when I realized that the page was being served over _HTTP_ but the cookies were _secure-only_ so there went that idea. Either way, I was able to demonstrate stored XSS which was enough for acceptance. 

I reported this vulnerability in three separate places in a combined report. The report was excepted and so far all patching attempts have failed. I believe that this is due to the way that MediaWiki appears to be managing its codebase. For all filtering (including file upload, oof) they are creating exclusions and individual replacements for specific payloads, strings, and characters within each separate piece of their code base (at least from what I can tell based on the various Phabricator threads I've read). Overall, a holistic change in the way they are filtering user-provided code would be required to fix this across the entire codebase which is easier said than done. I can only imagine how difficult that would be to do across an entire open-source code base that is meant to serve as a crowd-sourced CMS (yuck). Hats off to those in these threads that I've seen coming up with solutions time and time again. 

For this vulnerability, I have been awarded $1090 so far with patches still pending. I will update this write-up if the patch gets implemented successfully to explain how the organization mitigated it. 

[Bug Bounty](/blog/tag/Bug+Bounty)[Write-up](/blog/tag/Write-up)

[ ](/blog?author=63a1076f081fe62c6e3ae37b)

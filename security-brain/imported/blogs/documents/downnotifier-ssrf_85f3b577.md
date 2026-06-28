---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-04_downnotifier-ssrf.md
original_filename: 2019-04-04_downnotifier-ssrf.md
title: DownNotifier SSRF
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 85f3b57730be05f66c53bc635d296bca1a58b291b546a768b8168405c3fd62d7
text_sha256: ea44da2ae0c72d2c8f675b622dfb10a6ffd2ab8e86fbac78fbd8f428efd95259
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# DownNotifier SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-04_downnotifier-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `85f3b57730be05f66c53bc635d296bca1a58b291b546a768b8168405c3fd62d7`
- Text SHA256: `ea44da2ae0c72d2c8f675b622dfb10a6ffd2ab8e86fbac78fbd8f428efd95259`


## Content

---
title: "DownNotifier SSRF"
page_title: "downnotifer.com SSRF Bug Writeup"
url: "http://archive.ingredous.com/notes/downnotifer-ssrf/"
final_url: "http://archive.ingredous.com/notes/downnotifer-ssrf/"
authors: ["_m_q_t (@_m_q_t)"]
programs: ["DownNotifier"]
bugs: ["SSRF"]
publication_date: "2019-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5331
---

Apr 4, 2019 • [bug_hunting](category/#bug_hunting),[bug_writeup](category/#bug_writeup),[openbugbounty](category/#openbugbounty)

![Screenshot](/images/posts/2017/downssrf/logo.png)

# i. Introduction

DownNotifier has an open bug bounty progam hosted on `https://openbugbounty.org`.

DownNotifie is a service which periodically scans your websites and notifies you if your website has gone down.

Due to the nature of the website and the service it provides, I thought about some application logic bugs which might work,

So in mind came `SSRF`.

# ii. SSRF Explanation

SSRF, sometimes prounced _Surf_ , stands for Server Side Request Forgery.

Essentially, with SSRF you are able to send requests originating from the web-server, in which you can leverage to read local files, or even enumerate services on the local system.

Within SSRF, exists a subattack you can perform which is known as XSPA _(Cross Site Port Attack)_

With `XSPA`, you can use server output (which was easier for us in this case), or server response times to fingerprint if local services are running on the server such as `ftp, mysql, redis`

# iii. Exploiting XSPA to Enumerate Local Services

When browsing to `downnotifier` we are greeted with:

![Screenshot](/images/posts/2017/downssrf/index.png)

Trying usual loopback addresses like `localhost` and `127.0.0.1` does not seem to work too well:

![Screenshot](/images/posts/2017/downssrf/localhost.png)

Also trying to grab files using `file://` turned out as expected:

![Screenshot](/images/posts/2017/downssrf/file.png)

I tried some more payloads I found from `PayloadAllThings` SSRF payload page and found that `0.0.0.0` seemed to be accepted.
  
  
  https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
  

Though, even if it bypassed the filter, will it still work?

To see if it would, I added some common ports.

30 seconds later, we can see that we indeed did get an SSRF and were able to enumerate local services.

![Screenshot](/images/posts/2017/downssrf/proof.png)

`ftp` and `http` are running.

# iv. Conclusion

I reported the bug to `DownNotifier` and within 24 hour hours there was a response & a patch.

![Screenshot](/images/posts/2017/downssrf/email.png)

![Screenshot](/images/posts/2017/downssrf/acknowledgement.png)

I would like to thank `DownNotifier` for the acknowledgement and the quick patch.

Thank you for reading,

  * mqt

  
  
  Sources:
  https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server Side Request Forgery

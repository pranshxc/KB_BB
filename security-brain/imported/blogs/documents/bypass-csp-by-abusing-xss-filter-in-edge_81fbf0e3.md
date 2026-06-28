---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-15_bypass-csp-by-abusing-xss-filter-in-edge_2.md
original_filename: 2018-04-15_bypass-csp-by-abusing-xss-filter-in-edge_2.md
title: Bypass CSP by Abusing XSS Filter in Edge
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 81fbf0e3e791d7250e5ca95b76065881c87372b886a87f0ec138fa619e14d25f
text_sha256: e18a85bdaf80447e3dbeda9d8c8c7e969cd92d4b534a6a12fa7eba12248a2767
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass CSP by Abusing XSS Filter in Edge

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-15_bypass-csp-by-abusing-xss-filter-in-edge_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `81fbf0e3e791d7250e5ca95b76065881c87372b886a87f0ec138fa619e14d25f`
- Text SHA256: `e18a85bdaf80447e3dbeda9d8c8c7e969cd92d4b534a6a12fa7eba12248a2767`


## Content

---
title: "Bypass CSP by Abusing XSS Filter in Edge"
url: "https://medium.com/bugbountywriteup/bypass-csp-by-abusing-xss-filter-in-edge-43e9106a9754"
authors: ["Xiaoyin Liu (@general_nfs)"]
programs: ["Microsoft"]
bugs: ["CSP bypass"]
bounty: "1,500"
publication_date: "2018-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5919
scraped_via: "browseros"
---

# Bypass CSP by Abusing XSS Filter in Edge

Bypass CSP by Abusing XSS Filter in Edge
Xiaoyin Liu
Follow
3 min read
·
Apr 15, 2018

268

2

In this article, I will share a Content Security Policy (CSP) bypass vulnerability in Microsoft Edge, which I discovered in December 2016. The bypass was done by abusing the browser’s XSS filter. This is quite ironical, because both XSS filter and CSP are designed to protect users from XSS attacks, but this vulnerability allows attackers to abuse one XSS protection mechanism to bypass another.

XSS filter was first introduced in IE 8. The purpose of a XSS filter is to mitigate reflective XSS attacks. The XSS filter of IE/Edge roughly works in this way: when the browser loads a URL, the XSS filter first checks if some parameters of the URL may contain XSS payloads, using a set of predefined regular expressions. For instance, http://example.com/index.php?id=100is clearly harmless, but for a URL likehttp://example.com/index.php?id=<script>alert(1)</script>, the value of parameter id may be a XSS payload. Then, to determine whether it is a reflective XSS attack exactly, IE/Edge check if the returned HTML contains the substring <script>alert(1)</script>. If it does, IE/Edge assume it is reflected from the id parameter. Notice that this assumption may not be true: what if <script>alert(1)</script> is hardcoded in the page, and the id parameter actually doesn’t have any effect?

There’re two modes for XSS filter: default mode and block mode. Sites can enable the block mode by setting HTTP header: X-XSS-Protection: 1; mode=block”. In the block mode, IE/Edge block the entire HTML from rendering. In the default mode, IE/Edge try to destroy XSS payloads by modifying the corresponding HTML tags. E.g. if Edge assumes <script>alert(1)</script> is a XSS, it changes this element to <sc#ipt>alert(1)</script>. Thus, the DOM parser won’t parse this segment as a <script> element, so it won’t execute.

Now let’s see the vulnerability, CVE-2017–0135. There are two ways for a website to set a Content Security Policy: via Content-Security-Policy HTTP response header field, or via <meta> tag. An example of such meta element is:
<meta http-equiv=”Content-Security-Policy” content=”script-src ‘self’”>. Now suppose here is the HTML for URL http://example.com/xss.html:

<!DOCTYPE html>
<html>
 <head>
 <title>CSP Test</title>
  <meta http-equiv="Content-Security-Policy" content="script-src 'self'">
 </head>
 <body>
 <script>alert(document.domain);</script>
 </body>
</html>

The CSP should block alert(document.domain)from executing. To bypass the CSP, let’s ask users to visit http://example.com/xss.html?<meta http-equiv=”Content-Security-Policy” content=”script-src ‘self’”>(Just append meta element as a parameter to the URL.)

Then, by default, Edge’s XSS filter simply modifies the meta tag to <me#a http-equiv=”Content-Security-Policy” content=”script-src ‘self’”>, which kills the CSP, and alert is executed.

Press enter or click to view image in full size
Figure 1 Screenshot of a successful CSP bypass

This vulnerability was fixed in MS17-007, released in March 2017. It was assigned CVE-2017-0135.

It’s fixed by blocking the whole HTML page, when the XSS filter detects the query string matches any meta element, regardless of modes.

Get Xiaoyin Liu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Although this vulnerability has been fixed, it’s still a good idea to set “X-XSS-Protection: 1; mode=block”. Also CSP policies delivered via HTTP headers are not vulnerable to this bypass attack.

Timeline

12/2/2016: Vulnerability reported to MSRC
3/14/2017: Vulnerability fixed in MS17–007 (bug bounty: $1500)

References

Nava, E. V. and Lindsay, D., “Abusing Internet Explorer 8’s XSS Filters”
W3C, “Content Security Policy Level 2”
IE 8 XSS Filter Architecture / Implementation

Acknowledgements

Many thanks to MSRC for fixing this bug and awarding me the bounty.
This article was first published on Chinese website FreeBuf, link: http://www.freebuf.com/articles/web/164871.html (in Chinese). I want to thank them for allowing me to post the English version on Medium.

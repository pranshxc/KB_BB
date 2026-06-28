---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-24_xss-in-peerio-2-windows-application-write-up.md
original_filename: 2020-04-24_xss-in-peerio-2-windows-application-write-up.md
title: XSS in Peerio 2 Windows Application (Write Up)
category: documents
detected_topics:
- xss
- sso
- command-injection
tags:
- imported
- documents
- xss
- sso
- command-injection
language: en
raw_sha256: 00a928950687b66a8cb2ce36cc3966946d0bf70e3b0dce295f3539c306b7a974
text_sha256: 3ac85188a10050f8aac974a57e443ec6a4f353e4b15e45f3e1f4b7e8db7d4161
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Peerio 2 Windows Application (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-24_xss-in-peerio-2-windows-application-write-up.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `00a928950687b66a8cb2ce36cc3966946d0bf70e3b0dce295f3539c306b7a974`
- Text SHA256: `3ac85188a10050f8aac974a57e443ec6a4f353e4b15e45f3e1f4b7e8db7d4161`


## Content

---
title: "XSS in Peerio 2 Windows Application (Write Up)"
page_title: "Evan Ricafort | Blog: XSS in Peerio 2 Windows Application (Write Up)"
url: "https://blog.evanricafort.com/2020/04/xss-in-peerio-2-windows-application.html"
final_url: "https://blog.evanricafort.com/2020/04/xss-in-peerio-2-windows-application.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Peerio"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2020-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4632
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0yGMSsoUBa7GTQj85JMZWFJpCCUdKz9tvCBjDuzVYFjQVQKp-vMZTZl6bF2kpapZeiXwsWold5J4nWZ0NvLPqxhm1-BZTCXoa1x4nHitN39ox-gzOQTuPZqbz52QuYSDrNe4m2d87/s400/Untitled+3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0yGMSsoUBa7GTQj85JMZWFJpCCUdKz9tvCBjDuzVYFjQVQKp-vMZTZl6bF2kpapZeiXwsWold5J4nWZ0NvLPqxhm1-BZTCXoa1x4nHitN39ox-gzOQTuPZqbz52QuYSDrNe4m2d87/s1600/Untitled+3.png)

  
  
Howdy!  
  
  
Few years ago I found a simple XSS vulnerability which affects a windows application of a company called Peerio. The application was similar to Slack nowadays which allows you to chat with your colleagues. The XSS was found in the chat input which if you will input an XSS payload on the chat box the payload will automatically trigger since they are using a web based application on it.  
  
The vulnerability was reported directly to their security team and they added a quick fixed on it.  
  
**_\--Proof of Concept--_**  
**_  
_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9XMOMWWXKtKrkrHsALf6tnmApCqM05T-1CVPJ-yGzzUAeNGQMgIT60iaey5NrdkhxMlJlCt5VQRLO9xgzpid4VmgVUH2JD3DNARAFrL4VT66lF_1HbBbIy8WGgUJnNxXMBvoZfjDG/s640/2017-11-21_19-31-28.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9XMOMWWXKtKrkrHsALf6tnmApCqM05T-1CVPJ-yGzzUAeNGQMgIT60iaey5NrdkhxMlJlCt5VQRLO9xgzpid4VmgVUH2JD3DNARAFrL4VT66lF_1HbBbIy8WGgUJnNxXMBvoZfjDG/s1600/2017-11-21_19-31-28.gif)

**_  
_****_\--Report Timeline--_**  
**_  
_**Reported: Nov 21, 2017, 7:41 PM  
First Response: Nov 23, 2017, 6:02 AM  
  

> _Hi Evan,  
>  thanks a lot, and quick catch — looks like this was introduced exactly one week ago.  
> What’s the best way to pay you? I’ll get the bureaucracy moving…  
> We should have a fix out tomorrow. _

Fixed: Dec 2, 2017, 1:36 AM  
  

> _Hi,  
>  We pushed a direct fix in this release: <https://github.com/PeerioTechnologies/peerio-desktop/releases/tag/v2.98.7>  
> And then added strict CSP in the following release for a more global solution: <https://github.com/PeerioTechnologies/peerio-desktop/releases/tag/v2.103.0> (you can check out pull requests #144 and #145 for details)  
> Thanks! _

Bounty: 1000 Canadian Dollar  
  
  
  
I hope you enjoy this write up! stay tune for more contents like this in the future.  
  
Have a great day,  
  
Evan  

  

_**“Life isn’t about finding yourself. Life is about creating yourself.”**_

_– George Bernard Shaw_

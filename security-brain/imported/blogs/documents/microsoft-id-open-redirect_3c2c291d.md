---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-19_microsoft-id-open-redirect.md
original_filename: 2019-07-19_microsoft-id-open-redirect.md
title: Microsoft ID Open Redirect
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 3c2c291d93742e7565969a4f51a1166dd05fe4af0c4441733ea8948d7125b4f7
text_sha256: 3e88fa038cfe340744de5786ed9a8ce762ac3ecc56533583bf4914b2d44e90bb
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft ID Open Redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-19_microsoft-id-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3c2c291d93742e7565969a4f51a1166dd05fe4af0c4441733ea8948d7125b4f7`
- Text SHA256: `3e88fa038cfe340744de5786ed9a8ce762ac3ecc56533583bf4914b2d44e90bb`


## Content

---
title: "Microsoft ID Open Redirect"
page_title: "Burninator Sec: Microsoft ID Open Redirect"
url: "https://burninatorsec.blogspot.com/2019/07/microsoft-id-open-redirect.html"
final_url: "https://burninatorsec.blogspot.com/2019/07/microsoft-id-open-redirect.html"
authors: ["Burninator Sec"]
programs: ["Microsoft"]
bugs: ["Open redirect"]
publication_date: "2019-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5135
---

Recently I submitted a Microsoft Bug Bounty report for an Open Redirect vulnerability in their Identity product. I found it by searching for keywords in intercepted traffic in Burpsuite like "redirect", "dest", "url", etc. The finding was rejected by their security team, and I have approval to post about it here. I can understand why this might be considered an acceptable risk; it happens during logout, so no credentials can automatically be passed onto an attack server in this way. It would definitely require social engineering effort to exploit it. I tried out setoolkit to spoof the sign-in page and redirect them there (by spoofing the page URL that ends with prompt=sign-in and not none or select_account, so that both username and password can be collected, otherwise it auto-populates the username). (However, there are already protections against changing a similar parameter for their sign-_in_ process, so I'm not sure why that functionality wouldn’t be extended to sign-_out_ as well...)  
  
Edit the URL to redirect to ATTACKSERVER/signinGET.html, where the spoof page is located:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt4S2CqYaG_U22374lmEAERLkRB02fza7MWeDDb1iQTcfSC4pR-CmEQU5HbIRPlyx0GqGNWhdbu34uzmkQUl9cmuOQTmVvgBgaIz5ilKDq-qOswJQ_AhrTXd_56ubSpLhtwxSES4viPto/s640/redirecturl.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt4S2CqYaG_U22374lmEAERLkRB02fza7MWeDDb1iQTcfSC4pR-CmEQU5HbIRPlyx0GqGNWhdbu34uzmkQUl9cmuOQTmVvgBgaIz5ilKDq-qOswJQ_AhrTXd_56ubSpLhtwxSES4viPto/s1600/redirecturl.png)

  
User logs in:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqCYts3njh8LzInqO23kCH_OvtiHupet1BJKnOSg9wXN8WTq4SDlN4q1LXGxPrPJ_WmeBGpLhKHwiAnfbn2D7ZLFx3syMe1pOjAMZNmo8c8GOhnHAv-bSJyImuttaARLt0YFmKW1pnD3c/s640/spooflogin.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqCYts3njh8LzInqO23kCH_OvtiHupet1BJKnOSg9wXN8WTq4SDlN4q1LXGxPrPJ_WmeBGpLhKHwiAnfbn2D7ZLFx3syMe1pOjAMZNmo8c8GOhnHAv-bSJyImuttaARLt0YFmKW1pnD3c/s1600/spooflogin.png)

  
Page sends credentials as parameters:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEUQ6jdE-mYhQQOVk8IhLMR8pnoTaExoUihIhkojM2kAG3MJVMIb-dZAaRF_OGfpCKmGxUKoxpSiJyb6BfFxdxelYc247wsILFWNyGPA7Iu74hsV0RSPhhE3eOWEHQe30fdcbfb4hwLSw/s640/attackspoofpage.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEUQ6jdE-mYhQQOVk8IhLMR8pnoTaExoUihIhkojM2kAG3MJVMIb-dZAaRF_OGfpCKmGxUKoxpSiJyb6BfFxdxelYc247wsILFWNyGPA7Iu74hsV0RSPhhE3eOWEHQe30fdcbfb4hwLSw/s1600/attackspoofpage.png)

  
Attacker can view credentials:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKS3Wcz94A7TtgCLgpdONGD9IEH6zmWIRQJhnQed1cwEy3hFplunO7RnP0FOKmHGjdc6hpAPLN139fdKSWmeTwDsGll1r2r-dKd1lQxriZ__3Ctz2uhsR7SJ_cS9MPB9IxYg37pPd-OIQ/s640/attackside.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKS3Wcz94A7TtgCLgpdONGD9IEH6zmWIRQJhnQed1cwEy3hFplunO7RnP0FOKmHGjdc6hpAPLN139fdKSWmeTwDsGll1r2r-dKd1lQxriZ__3Ctz2uhsR7SJ_cS9MPB9IxYg37pPd-OIQ/s1600/attackside.png)

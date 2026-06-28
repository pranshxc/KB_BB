---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-11-17_oracle-xss.md
original_filename: 2013-11-17_oracle-xss.md
title: Oracle xss
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
raw_sha256: 3eefca284190df1747b80ba45594373da150ce83b2d2f2206fbf494c18cd70ac
text_sha256: f669c6c1f352ef62e23e5b5cc7cb9a4af8fea365416262b811b142efea66f757
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Oracle xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-11-17_oracle-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3eefca284190df1747b80ba45594373da150ce83b2d2f2206fbf494c18cd70ac`
- Text SHA256: `f669c6c1f352ef62e23e5b5cc7cb9a4af8fea365416262b811b142efea66f757`


## Content

---
title: "Oracle xss"
page_title: "Shashank's Security Blog: Oracle xss"
url: "http://blog.shashank.co/2013/11/oracle-xss.html"
final_url: "https://blog.shashank.co/2013/11/oracle-xss.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Oracle"]
bugs: ["XSS"]
publication_date: "2013-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6389
---

Every one knows about ORACLE. Oracle Corporation is an American multinational computer technology corporation headquartered in Redwood City, California, United States.  

  

I spotted some security issues on their website, and finally, they have fixed it. One of them was cross-site scripting issue in oracle's sub-domain [http://education.oracle.com](http://education.oracle.com/)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpsFxmsepE_F-04qEnflB01zO5exViZ89etk0TGbK81e6P0VxQ379OKNBT1Qtbmvk8N68KL3kUKN3PeQMMEcDXCVjldlu2TnFFbdjJrTYXtevqzwiDLRfIctKvyw796a098PoRD5zgPC26/s400/oracalxss2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpsFxmsepE_F-04qEnflB01zO5exViZ89etk0TGbK81e6P0VxQ379OKNBT1Qtbmvk8N68KL3kUKN3PeQMMEcDXCVjldlu2TnFFbdjJrTYXtevqzwiDLRfIctKvyw796a098PoRD5zgPC26/s1600/oracalxss2.PNG)

  

they took a long time in fixing but after the fix, they acknowledged me on their website.

  

Oracle Critical Patch Update Advisory - January 2013 - Beta Oracle CVRF

<http://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/1841213.xml>

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkWr6Rz2lNSI3kbi1qszq3sahPfQUKVkAWshyphenhyphene1JmFrDhpL2tz-VQV-qpQd9JQ_SO5cH5iELlxHqGEyGFDE7N2f7Qx12gWAI2lQs_Anhxa-pbbB1DX3cOQrg9xAHDTv9_wyUZTMFqmp6w6/s400/oraclehof.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkWr6Rz2lNSI3kbi1qszq3sahPfQUKVkAWshyphenhyphene1JmFrDhpL2tz-VQV-qpQd9JQ_SO5cH5iELlxHqGEyGFDE7N2f7Qx12gWAI2lQs_Anhxa-pbbB1DX3cOQrg9xAHDTv9_wyUZTMFqmp6w6/s1600/oraclehof.PNG)

  

  

  
And 

Oracle Critical Patch Update Advisory - July 2013 - Beta Oracle CVRF

<http://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/1841215.xml>

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRXMLSxlYO6-JMVfM8i48TZODShVN9EcV_7kLxKNY1p1NNg82ETzXD-Xp6BCcvi7f3Ng9C8_WKUj_2BiVhsIe1ZEpQZf3QJuQhIRzw3c1whTu2_iqGumb2ht_Qf4xqkVmlYYomAO8oRVoW/s320/oraclehof2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRXMLSxlYO6-JMVfM8i48TZODShVN9EcV_7kLxKNY1p1NNg82ETzXD-Xp6BCcvi7f3Ng9C8_WKUj_2BiVhsIe1ZEpQZf3QJuQhIRzw3c1whTu2_iqGumb2ht_Qf4xqkVmlYYomAO8oRVoW/s1600/oraclehof2.PNG)

  

  

  

cheers :)

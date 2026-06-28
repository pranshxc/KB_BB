---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-25_xss-surveydropboxcom.md
original_filename: 2018-09-25_xss-surveydropboxcom.md
title: '[XSS] survey.dropbox.com'
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
raw_sha256: 52f03aad341cb57a579f7a8ad4199a9951118947d7d4abf9bf518c2dca49fc4a
text_sha256: fb9090bd26834600a20f9fcbfaf99ec3ae445d3338d9cd4fa189a7fbf07593c9
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# [XSS] survey.dropbox.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-25_xss-surveydropboxcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `52f03aad341cb57a579f7a8ad4199a9951118947d7d4abf9bf518c2dca49fc4a`
- Text SHA256: `fb9090bd26834600a20f9fcbfaf99ec3ae445d3338d9cd4fa189a7fbf07593c9`


## Content

---
title: "[XSS] survey.dropbox.com"
page_title: "Kumar: [XSS] survey.dropbox.com"
url: "https://www.kumar.ninja/2018/09/xss-surveydropboxcom.html"
final_url: "https://www.kumar.ninja/2018/09/xss-surveydropboxcom.html"
authors: ["Kumar"]
programs: ["Dropbox"]
bugs: ["XSS"]
publication_date: "2018-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5681
---

**_  
_****_Introduction_ :**  
  
survey.dropbox.com was pointing to mysurveylab.com and any mysurveylab.com's forms was accessible through survey.dropbox.com. This lead to stored xss at survey.dropbox.com because mysurveylab.com's forms were vulnerable to xss.  
  
**_Impact:_** Nothing as far as I know. Except phishing!  
  
  
**_POC_ :**  
**_  
_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjTXJH8RJKGLR-7NvjIHRrUorF3u7_LqgY3Tani8ah2HloG1s46k3EJZSTl0PBPrZQx2L2mWiLy3ZkqJbCFTgbxs0GLADT1WlCO7W75a6oYUPHsaQ7ZUfa9VRmjH8jfz4m8K5XGfPUsF_8/s640/Screenshot_from_2017-01-14_03-35-06.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjTXJH8RJKGLR-7NvjIHRrUorF3u7_LqgY3Tani8ah2HloG1s46k3EJZSTl0PBPrZQx2L2mWiLy3ZkqJbCFTgbxs0GLADT1WlCO7W75a6oYUPHsaQ7ZUfa9VRmjH8jfz4m8K5XGfPUsF_8/s1600/Screenshot_from_2017-01-14_03-35-06.png)

  

  

**_Vulnerable section:_**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2cjJzq2jVMfDmMKmtAbXjmY9zlTJ-OaqM7fw31-UFEOb7A8DO1kO2tzcyjuX7wJS_UVtynbcUKlhmzUPSkIXvNSgBGr7b9XB8201BfBd-9ifj-1Da8UwcIMw3jvilm8zP5o7y6i5u3mEz/s640/Screenshot_from_2017-01-14_03-50-10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2cjJzq2jVMfDmMKmtAbXjmY9zlTJ-OaqM7fw31-UFEOb7A8DO1kO2tzcyjuX7wJS_UVtynbcUKlhmzUPSkIXvNSgBGr7b9XB8201BfBd-9ifj-1Da8UwcIMw3jvilm8zP5o7y6i5u3mEz/s1600/Screenshot_from_2017-01-14_03-50-10.png)

**_  
_**  

  

  

**_Timeline_ :**

  * **Reported: Jan 14th 2017**
  * **Closed as Informative: Jan 14th 2017**
  * **MySurveyLab fixed the bug within week(not sure).**

  

  

  

**_  
_**

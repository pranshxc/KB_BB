---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-10_apple-safari-microsoft-edge-browser-address-bar-spoofing-writeup.md
original_filename: 2018-09-10_apple-safari-microsoft-edge-browser-address-bar-spoofing-writeup.md
title: Apple Safari & Microsoft Edge Browser Address Bar Spoofing - Writeup
category: blogs
detected_topics:
- jwt
- command-injection
- automation-abuse
- race-condition
- api-security
- mobile-security
tags:
- imported
- blogs
- jwt
- command-injection
- automation-abuse
- race-condition
- api-security
- mobile-security
language: en
raw_sha256: 97f083ea3cc3bff22c839e07a4145ce3217589bfe3826a7b462d2728246cf36c
text_sha256: f760012d7c3e258f4bd3a5ca187f13222fedb6f6c27af0c8c35e454da0e34997
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Apple Safari & Microsoft Edge Browser Address Bar Spoofing - Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-10_apple-safari-microsoft-edge-browser-address-bar-spoofing-writeup.md
- Source Type: markdown
- Detected Topics: jwt, command-injection, automation-abuse, race-condition, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `97f083ea3cc3bff22c839e07a4145ce3217589bfe3826a7b462d2728246cf36c`
- Text SHA256: `f760012d7c3e258f4bd3a5ca187f13222fedb6f6c27af0c8c35e454da0e34997`


## Content

---
title: "Apple Safari & Microsoft Edge Browser Address Bar Spoofing - Writeup"
page_title: "Apple Safari & Microsoft Edge Browser Address Bar Spoofing - Writeup  - Miscellaneous Ramblings of a Cyber Security Researcher"
url: "https://www.rafaybaloch.com/2018/09/apple-safari-microsoft-edge-browser.html"
final_url: "https://www.rafaybaloch.com/2018/09/apple-safari-microsoft-edge-browser.html"
authors: ["Rafay Baloch (@rafaybaloch)"]
programs: ["Microsoft", "Apple"]
bugs: ["Address Bar Spoofing"]
publication_date: "2018-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5709
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIaIOaBgu2R0etZ7-TCBGe1AKLiy-aswjNJpyawkIn_OaIVmcOUKr4m7HOvhm3LP9rU3PEy4ba2QK2yrAtKpVhdnZmmCdhPrbaLTvJwEVBHd42weA8ywKtqGHt8C1_RN_Mqncllr4KbTWL/s640/8d670855-fbc6-4b6a-a2c0-8b3e23e0594d.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIaIOaBgu2R0etZ7-TCBGe1AKLiy-aswjNJpyawkIn_OaIVmcOUKr4m7HOvhm3LP9rU3PEy4ba2QK2yrAtKpVhdnZmmCdhPrbaLTvJwEVBHd42weA8ywKtqGHt8C1_RN_Mqncllr4KbTWL/s1600/8d670855-fbc6-4b6a-a2c0-8b3e23e0594d.jpeg)

  

##  Introduction

Google security team themselves state that "**We recognize that the address bar is the only reliable security indicator in modern browsers** " and if the only reliable security indicator could be controlled by an attacker it could carry adverse affects, For instance potentially tricking users into supplying sensitive information to a malicious website due to the fact that it could easily lead the users to believe that they are visiting is legitimate website as the address bar points to the correct website.  
  
In my paper "**[Bypassing Browser Security Policies For Fun And Profit](https://www.rafaybaloch.com/2017/06/bypassing-browser-security-policies-for.html)** " I have uncovered various Address Bar Spoofing techniques as well as other bugs affecting modern browsers. In this blog post I would discuss about yet another "**Address Bar Spoofing** " vulnerability affecting Safari and Edge browser.  

##  Technical Details

During my testing, it was observed that both Edge and Safari browser allowed javascript to update the address bar while the page was still loading. Upon requesting data from a non-existent port the address was preserved and hence a due to race condition over a resource requested from non-existent port combined with the delay induced by setInterval function managed to trigger address bar spoofing. It causes browser to preserve the address bar and to load the content from the spoofed page. The browser will however eventually load the resource, however the delay induced with setInterval function would be enough to trigger the address bar spoofing.  
  

##  Edge Browser Address Bar Spoofing (CVE-2018-8383)

  
**_Proof of Concept_**  
  
**Version:** Edge Browser 42.17134.1.0  
  
  
**  
**  

####  _Steps to Reproduce_

**  
****1)** Visit the following link for the vulnerable browser - **<http://sh3ifu.com/bt/Edge-Spoof.html>**  
  
**2)** You will notice that the URL is pointing to **https://www.gmail.com:8080/,** however the content is hosted on **sh3ifu.com**  
**  
****_Disclosure Timelines_**  
**  
****June 2 -** Vulnerability was reported to apple and was given 90 days deadline.  
**Aug 11** \- Reminder about the 90 days deadline  
**Aug 14** \- Microsoft released fix on August Patch Tuesday.  
**Sep 10** \- Writeup was released.  

## 

##  Safari Address Bar Spoofing (CVE-2018-4307)

**Version** : iOS 11.3.1  

  

**_Proof of Concept_**  
**_  
_**  
  
Safari browser had one constraint which did not allow users to type information into the input boxes while the page was in the loading state. However, we were able to circumvent this restriction by injecting a fake keyboard (which happens to be a very common practice in banking websites).  
  
Following are the steps to reproduce it:  
  
**_Steps to Reproduce_**  
**  
****1)** Visit the following link for the vulnerable browser - ** _https://sh3ifu.com/bt/safari_**  
  
**2)** You will notice that the URL is pointing to **https://xyzbank.com:8000//** , however the content is hosted on sh3ifu.com  
  
**3)** Use the virtual keyboard for entering the data onto the form.  
  
_**Fix**_  
**  
**This issue has been addressed in latest versions of Edge Browser and will be fixed in upcoming Apple safari update.  
**  
****_Disclosure Timelines_**  
**  
****June 2 -** Vulnerability was reported to apple and was given 90 days deadline.  
**Aug 14** \- Reminder about the 90 days deadline  
**Aug 31** \- End of 90 days deadline  
**Sep 10** \- Writeup was released.  
  
**_Credits_**  
**_  
_**I am highly indebted to "**File Descriptor** " from Cure53,"**Jun Kokastu"** from Microsoft team, "**Tod Beardsley** " from rapid7 and "**Hammad Shamsi** " for their assistance.

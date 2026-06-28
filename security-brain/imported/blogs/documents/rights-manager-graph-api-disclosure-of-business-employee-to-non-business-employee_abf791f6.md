---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-22_rights-manager-graph-api-disclosure-of-business-employee-to-non-business-employe.md
original_filename: 2019-08-22_rights-manager-graph-api-disclosure-of-business-employee-to-non-business-employe.md
title: Rights Manager Graph API Disclosure of business employee to non business employee
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: abf791f6ed3e4231962646fa115521d48f1d897a75ad74481c71b6b0ed4ff16d
text_sha256: 66c14607c17228ebb65103d78bdce2fc9f414e8963a69087d5c13d81c91a491a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Rights Manager Graph API Disclosure of business employee to non business employee

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-22_rights-manager-graph-api-disclosure-of-business-employee-to-non-business-employe.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `abf791f6ed3e4231962646fa115521d48f1d897a75ad74481c71b6b0ed4ff16d`
- Text SHA256: `66c14607c17228ebb65103d78bdce2fc9f414e8963a69087d5c13d81c91a491a`


## Content

---
title: "Rights Manager Graph API Disclosure of business employee to non business employee"
page_title: "Rights Manager Graph API Disclosure of business employee to non business employee - Update - أب ديت"
url: "https://www.updatelap.com/2019/08/Rights-Manager-Graph-API-Disclosure-of-business-employee-to-non-business-employee.html"
final_url: "https://www.updatelap.com/2019/08/Rights-Manager-Graph-API-Disclosure-of-business-employee-to-non-business-employee.html"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2019-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5068
---

##  _i found bug in_ Graph  _API on Facebook Rights Manager leads to the non-business employee to Disclosure of business employee_

_  
_

_[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkEogAHbWq_fOpEzGWEovTweGQVN08hdVEwgXNmjaZJ5dWFZN8cGwfvvTcn_r9rr-pZyVIqMKC0N0GE3QOU2QBpqRcmHPzMpXHgvLgbHQ6yi_5NK7zpLu5Qq56XHfOFa1Se6eCHVC7p-a0/s1600/PoC_FB_Page.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkEogAHbWq_fOpEzGWEovTweGQVN08hdVEwgXNmjaZJ5dWFZN8cGwfvvTcn_r9rr-pZyVIqMKC0N0GE3QOU2QBpqRcmHPzMpXHgvLgbHQ6yi_5NK7zpLu5Qq56XHfOFa1Se6eCHVC7p-a0/s1600/PoC_FB_Page.png)_

_  
_

####  _Summary:_

#### 

_**Vulnerability****Type:** Identification / Privacy_

_**Product Area:** Pages_

_The malicious user can Disclosure of business employee to non business employee using Reference Files in Rights Manager_

####  _Description:_

_Facebook offers a Copyrighting Video manager for video content creators for pages on Facebook, Through which the creator can follow who copies their videos and republishes them without permission. More info : "[https://rightsmanager.fb.com/](https://l.facebook.com/l.php?u=https%3A%2F%2Frightsmanager.fb.com%2F&h=AT0sRrHVQJzRUh7z9isvpVD1wOkhfbH4aesuG3-Lk5DSJJ81xurKkHHc_tEx5oNLTZn7tIOS2sxu_ONO1KjrLUvO5O_WhoFcUOp_V3A4k53kaVpGWqUT30tBO0RrE0bI16HQFg)"  
  
When accepting your request to activate the tool on your page enter your page from "Business admin account" go to the link "[https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES](https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES)" then add Reference video, after add Reference file Look at the column "Date Added" You'll see that the column contains your account information.  
  
Now if (Admin,Editor) page employee go to the link "[https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES](https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES)" you can identification business admin Just by looking at the "Date Added" column,  
_  

####  _Impact:_

_Disclosure of business employee identity to non business employee._  

####  **_Explain impact:_**

Business employee's identity is disclosed to a non-business page admin through the Rights Manager video_media_copyrights Graph API. Normally, business admins are hidden to non-business page users.

_  
_

###  _Setup:_

_use this link to learn how to add copyright manger in your page "[ https://rightsmanager.fb.com/](https://rightsmanager.fb.com/)"  
_  

###  _Steps:_

_1\. Create Page and add Editor to page employee.  
2\. Create business account.  
3 Link the page with business manger.  
4\. Use this link to learn how to add copyright manger in your page "[https://rightsmanager.fb.com/](https://l.facebook.com/l.php?u=https%3A%2F%2Frightsmanager.fb.com%2F&h=AT1Mxruq1otkhc4aeqgfPDbHR1suDFUlM0ng3SxOjL2V_sV3_NI4RntQVElnaQGarcBIrjDDdApewTEInnNcNC0_TxPRxHVwirKBYQhuOrXvzSx_vkCTsx1hgJOR0hPg6bqNDg)"  
5\. after accepting copyright manger in your page upload any video  
6\. Now from admin business account go to the link "[https://web.facebook.com/YourPage/publishing_tools](https://web.facebook.com/YourPage/publishing_tools) /?section=ALL_REFERENCE_FILES"  
7\. Click in "Add Files" Then add video to Reference Files.  
8\. Now if Admin or Editor in page employee go to the link "[https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES](https://web.facebook.com/YourPage/publishing_tools/?section=ALL_REFERENCE_FILES)" can detect business admin  
_  

####  _PoC Get Request :_

_  
GET /v2.6/YourPage/video_media_copyrights?access_token=Editor_Token &fields=["creator"] HTTP/1.1  
Host: [graph.facebook.com](http://graph.facebook.com/)  
  
**Response** :_  

_{_

_"data": [_

_{_

_"creator": {_

_"name": "Jafar Abo Nada",_

_"id": "100002271816418"_

_},_

_"monitoring_status": "COPYRIGHTED",_

_"id": "2511847998861026",_

_"reference_owner_id": "936928013019707"_

_},_

_  
_

_  
_

[_![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkEogAHbWq_fOpEzGWEovTweGQVN08hdVEwgXNmjaZJ5dWFZN8cGwfvvTcn_r9rr-pZyVIqMKC0N0GE3QOU2QBpqRcmHPzMpXHgvLgbHQ6yi_5NK7zpLu5Qq56XHfOFa1Se6eCHVC7p-a0/s1600/PoC_FB_Page.png)_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkEogAHbWq_fOpEzGWEovTweGQVN08hdVEwgXNmjaZJ5dWFZN8cGwfvvTcn_r9rr-pZyVIqMKC0N0GE3QOU2QBpqRcmHPzMpXHgvLgbHQ6yi_5NK7zpLu5Qq56XHfOFa1Se6eCHVC7p-a0/s1600/PoC_FB_Page.png)

_  
_

_  
_

###  **_Follow me on_**** _Twitter [@jafar_abu_nada](https://twitter.com/jafar_abu_nada) & _**** _Facebook[Jafar Abo Nada](https://web.facebook.com/profile.php?id=100002271816418)_**

**_  
_**

###  _Timeline :_

###  _Jul-8-2019: Report sent_

###  _. Jul-12-2019: Facebook Reproduce Report_

###  _Jul-15-2019: Confirmation of submission by Facebook_

###  _Aug-5-2019: Confirmation of patch by Facebook_

###  _Aug-22-2019: Bounty awarded by Facebook_

###  **_  
_**

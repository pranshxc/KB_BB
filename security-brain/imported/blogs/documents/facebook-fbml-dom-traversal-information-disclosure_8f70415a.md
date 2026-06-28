---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2011-08-23_facebook-fbml-dom-traversal-information-disclosure.md
original_filename: 2011-08-23_facebook-fbml-dom-traversal-information-disclosure.md
title: Facebook FBML DOM Traversal (Information Disclosure)
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 8f70415ac9107bb652dd6a472c4444e3ba412f76e43e3a0ac719fce58064b6df
text_sha256: e937c9a34a3297ce93622a7c9143373f9d93652f44645fef2e1d2c7f77014ea4
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Facebook FBML DOM Traversal (Information Disclosure)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2011-08-23_facebook-fbml-dom-traversal-information-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `8f70415ac9107bb652dd6a472c4444e3ba412f76e43e3a0ac719fce58064b6df`
- Text SHA256: `e937c9a34a3297ce93622a7c9143373f9d93652f44645fef2e1d2c7f77014ea4`


## Content

---
title: "Facebook FBML DOM Traversal (Information Disclosure)"
page_title: "maustin.net  | Facebook FBML DOM Traversal (Information Disclosure)"
url: "https://maustin.net/articles/2011-08/FBML_dom_traversal"
final_url: "https://maustin.net/articles/2011-08/FBML_dom_traversal"
authors: ["Matt Austin (@mattaustin)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2011-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6418
---

In a Facebook FBML application some elements are protected with fb_protected=”true”. When transversing the elements with getElementsByTagName sub elements of the protected element can be accessed.

A malicious application would place a comment box inside a facebook application or in an iframe with http://www.facebook.com/plugins/serverfbml.php. The site would then use the javascript call getElementsByTagName to locate the textarea and use setValue to fill it out. The same technique could be used to set the “Post on wall” checkbox. Finally getElementsByTagName call would then find the only form instance and call the submit function to post the new comment. This would be 100% automated and transparent to the user.

Personal Information (all friends and groups) Leakage

An FBML mutly-friend selector is used. Then applying the same technique as above the malicious application can locate all links inside the elements. The links contain a title attribute with each friends full name (ele.getTitle). The neighboring div contains a background style that can also be read to get the friends profile picture and user ID.

  * How do you reproduce the issues?

Comment box with wall post.

iFramed URL via serverfbml.php: [ http://www.facebook.com/plugins/serverfbml.php?api_key=***REDACTED***c'\)%3B%0Ac.getElementsByTagName\('input'\)%5B12%5D.setChecked\(true\)%3B%0Ac.getElementsByTagName\('textarea'\)%5B0%5D.setValue\('woot%20Content'\)%3B%0Ac.getElementsByTagName\('form'\)%5B0%5D.submit\(\)%3B%0A%3C%2Fscript%3E)

Personal Information (all friends and groups) Leakage

iFramed URL via serverfbml.php:

[http://www.facebook.com/plugins/serverfbml.php?api_key=***REDACTED***

In this example a text area is simply filled with the user data. In a real life example this data would be sent to the attackers server, or used to send misleading information.

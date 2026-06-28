---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2010-07-18_hacking-facebook-with-fbml-and-dom.md
original_filename: 2010-07-18_hacking-facebook-with-fbml-and-dom.md
title: Hacking Facebook with FBML and DOM
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 56a53668392b5fbcb79612796cfecbdb14999878b00891232a9272e4d4ad1a7f
text_sha256: fd9a8ea43d9938e4c93562bc10b949cdbd66212d8d009c5e0c10dabafceea694
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Facebook with FBML and DOM

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2010-07-18_hacking-facebook-with-fbml-and-dom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `56a53668392b5fbcb79612796cfecbdb14999878b00891232a9272e4d4ad1a7f`
- Text SHA256: `fd9a8ea43d9938e4c93562bc10b949cdbd66212d8d009c5e0c10dabafceea694`


## Content

---
title: "Hacking Facebook with FBML and DOM"
page_title: "maustin.net  | Hacking Facebook with FBML and DOM"
url: "https://maustin.net/articles/2010-07/facebook_fbml_xss"
final_url: "https://maustin.net/articles/2010-07/facebook_fbml_xss"
authors: ["Matt Austin (@mattaustin)"]
programs: ["Meta / Facebook"]
bugs: ["XSS"]
publication_date: "2010-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6419
---

Facebook allows developers to build applications using the “Canvas“. Because the canvas apps run on the facebook domain they use a “Sandbox”. This is a subset of HTML called FBML and a limited javascript set called FBJS. The sandbox is basically used to try prevent an attacker form being able to run malicious code.  
  
Facebook also introduced Public Canvas Pages.

> “Facebook now offers applications the ability to serve canvas pages to users not currently logged in to either Facebook or the application, or the user hasn’t agreed to the Terms of Service for the application.” 

This means with a successful attack an app could exploit all users not just those who have already joined our facebook app.

###The Exploit:

FBJS allows us DOM Element Traversal with functions like getElementById and getChildNodes. This allows us to get info from any object in our canvas sandbox, even those rendered by facebook.

###Info Disclosure: Lets say we use a “Public Canvas Page”, and want want to get info about users who have not yet added our app. We will use the following FBML:

We use 2 FBML tags “fb:profile-pic”, and “fb:multi-friend-selector”. FBJS does not allow us to access these elements directly, but because we wrap them in a div that we created we can use the element traversal functions:

###The XSS:

Reading information is one thing but we really want full control. Facebook does allow us to use flash with the Fb:swf tag, but they render the embed tag for us and always include the allowscriptaccess=”never” to prevent unwanted script access from flash. They do however provide: Fb:fbjs-bridge. This allows you from flash to comunicate with FBJS and FBML.

Fb:fbjs-bridge renders its own embed tag, and because it is controlled by facebook, and needs to communicate with javascript it has the attribute allowscriptaccess=”always”.

The problem is this item is rendered inside our canvas area therefore the attack mentioned above can be used to actually change the src (with setSrc which i assume is meant for IMG tags) of the “bridge” flash to an swf file owned by us giving us unrestricted script access.

HTML / JS: 

Flash/AS3:

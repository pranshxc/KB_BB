---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_upgrade-plan-from-free-to-paid-via-response-manipulation.md
original_filename: 2023-03-03_upgrade-plan-from-free-to-paid-via-response-manipulation.md
title: Upgrade plan from Free to Paid via Response Manipulation
category: documents
detected_topics:
- oauth
- xss
- command-injection
tags:
- imported
- documents
- oauth
- xss
- command-injection
language: en
raw_sha256: f3c75a8c86f8d1beb4910c8a2ef65061f5beabfcca7ab02aa88e6ad88d1d4782
text_sha256: 953b68f6a58c159952089fc09954cccac149cd37ae27d2d143f9e0c92c4d760e
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Upgrade plan from Free to Paid via Response Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_upgrade-plan-from-free-to-paid-via-response-manipulation.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `f3c75a8c86f8d1beb4910c8a2ef65061f5beabfcca7ab02aa88e6ad88d1d4782`
- Text SHA256: `953b68f6a58c159952089fc09954cccac149cd37ae27d2d143f9e0c92c4d760e`


## Content

---
title: "Upgrade plan from Free to Paid via Response Manipulation"
page_title: "Upgrade plan from Free to Paid via Response Manipulation | Write-up"
url: "https://ibraradi.gitbook.io/write-up/upgrade-plan-from-free-to-paid-via-response-manipulation"
final_url: "https://ibraradi.gitbook.io/write-up/upgrade-plan-from-free-to-paid-via-response-manipulation"
authors: ["Ibrahim Radi (@ibraradi9)"]
bugs: ["Payment bypass", "HTTP response manipulation"]
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1438
---

For the complete documentation index, see [llms.txt](https://ibraradi.gitbook.io/write-up/llms.txt). This page is also available as [Markdown](https://ibraradi.gitbook.io/write-up/upgrade-plan-from-free-to-paid-via-response-manipulation.md).

Copy

On this page

# Upgrade plan from Free to Paid via Response Manipulation

Bug Bounty Finding

#### 

**Summary:**

I found this while testing on a target let’s call it [redacted.com](http://redacted.com) because the report is Unresolved.

As a normal site that provides services it has (free and paid) services. To be able to use the paid services you have to subscribe to a paid plan. I was able to bypass this and use the site as a paid user.

#### 

Indicators:

Let’s suppose that our target is a web hosting target that give you the ability to change the theme of your hosted website.

Some themes are free and others are paid(Locked and when you click them a pop up shows asking you to pay). 

Now, while changing between to free themes that’s was the request :

Copy
  
  
  PUT /api/v1/change/{accountid}
  ...
  
  theme=Free-Theme

Free-Theme here was just the name of the Free Theme that I just picked to change to , Simply I changed the name to a name of a paid theme and The change toke place

💡 At this point I just reported those findings and went for more, What happened is just an indicator that the validation process is being done on the client side.

> **Emanuel Lasker — 'When you see a good move, look for a better one’**

I started digging on the js files for anything that might help and found some variables and functions like :

Copy
  
  
  IsPaid , Usable(Feature_Name) , ... 

I just stopped this because it’s a static js files and it’s the same for every user,paid or not.

#### 

Finally,We used Burp comparer

I just needed to test this on a larger scale so I created a Paid User, And sent the response of the index page to the comparer and did the same thing with the free user.

Here’s what I got.

#### 

Features map:

I found a map with all the feature on the site as a key and it’s value was something like that :

This map had a lot of “false” and “Limited_Access” Flags for the free users.

#### 

User Info:

The response contained some details about the user who requested this page. Like :

The Plan variable was found more than 5 times in the response for the free user with the value “Free” , While for the paid user :

### 

Exploitation:

I just intercepted the response of the free user and replaced every occurrence of “Free” to “paid”

and changed the values in The feature map from “False” To “True” and from “Limited_Access” to “Full_Access” and It Worked I was able to use the site as paid user.

### 

What about more Impact and Fun!

I created a web browser extension that gets things done instead of me. It completes the response **Manipulation for me. Here is the code :**

#### 

Manifest.json

#### 

**Manipulator.js**

The Manifest.json file just calls the js code and gives the extension some permissions.

#### 

**Manipulator.js:**

  * It creates a new map which contains the pro user features and could be edited to get an access to many other features

  * Saved the full string in a variable called : promap

  * The regex matched for the old map in the response and then changes it to the paid map

  * The script also matches any “free” in the response and replace it with “paid”

Then we just added this to firefox and it worked.

Thanks for reading,

[PreviousOAuth - Mechanism and Attacks](/write-up/oauth-mechanism-and-attacks)[NextXSS IN SOQL Console](/write-up/xss-in-soql-console)

Last updated 3 years ago

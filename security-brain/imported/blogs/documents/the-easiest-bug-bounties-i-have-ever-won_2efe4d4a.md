---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-07-13_the-easiest-bug-bounties-i-have-ever-won.md
original_filename: 2015-07-13_the-easiest-bug-bounties-i-have-ever-won.md
title: The easiest bug bounties I have ever won
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: 2efe4d4af23e01db6f06cc6ba3f06ed472f4a215d58a095b951ee1c09e8e3c6f
text_sha256: 11385596f9929507e3f4575369aceccddce39660b01f09a9fa676bf5fdb17183
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# The easiest bug bounties I have ever won

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-07-13_the-easiest-bug-bounties-i-have-ever-won.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `2efe4d4af23e01db6f06cc6ba3f06ed472f4a215d58a095b951ee1c09e8e3c6f`
- Text SHA256: `11385596f9929507e3f4575369aceccddce39660b01f09a9fa676bf5fdb17183`


## Content

---
title: "The easiest bug bounties I have ever won"
page_title: "Josip Franjković - archived security blog: The easiest bug bounties I have ever won"
url: "https://josipfranjkovic.blogspot.com/2015/07/the-easiest-bug-bounties-i-have-ever-won.html"
final_url: "https://josipfranjkovic.blogspot.com/2015/07/the-easiest-bug-bounties-i-have-ever-won.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2015-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6339
---

The bugs I will write about are the simplest ones I have ever found on Facebook. The point of this blog is to show that some bugs can be found just by changing a username in URL.  

  

###  Friend lists bug

The mobile website [m.facebook.com](https://m.facebook.com/) has a year overview in which you can see how many friends your friend made, where they checked in, and so on. Clicking on "Made xx new friends" leads to the URL: 

  

> https://m.facebook.com/**username** /year/**2014** /profile_lists/?factoid_type=friends_made

  

This will list every friend someone made in **2014**. Changing the **username** would list the user's friends regardless of privacy settings on **both accounts**. This is basically an [IDOR](https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_\(OTG-AUTHZ-004\)) bug. 

Here is a screenshot from my testing account:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZEmtTP5X0FlLW3Xj6DyG4-p-ifcSBvzXx_8aBLXGhuobLMoSAsLGQcSV1ZJ4w8jwdw7nGYaGZ0g9WIs81AFCYbRKTgB9Q76jY4-FGhJPgLcW7weUT94mh04c2OISIljPvdiOra9P0y_vY/s320/flist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZEmtTP5X0FlLW3Xj6DyG4-p-ifcSBvzXx_8aBLXGhuobLMoSAsLGQcSV1ZJ4w8jwdw7nGYaGZ0g9WIs81AFCYbRKTgB9Q76jY4-FGhJPgLcW7weUT94mh04c2OISIljPvdiOra9P0y_vY/s1600/flist.png)

  

### 

###  Most tagged with bug

  

The second bug is almost exactly the same as the first, and using it you could find someone's most tagged with person. This one also worked regardless of privacy settings. The URL was:

> https://m.facebook.com/**username** /stories/**2015** /most_tagged_with/

There are few other of those "factoids" on the mobile website, but I did a couple of quick checks and none seemed to be vulnerable. Perhaps you can find something? :-)  
**  
****Report timeline**  
April 29th, 2015 - Friend list bug submitted  
April 29th, 2015 - Most-tagged-with bug added to ticket  
April 29th, 2015 - Neal of Facebook's security team confirms these are valid bugs  
April 30th, 2015 - **Friend list bug is now fixed ( <16 hours after initial report)**  
May 7th, 2015 - Most tagged with bug fixed  
  
As always, a huge thanks to Facebook for running their bug bounty program, quickly fixing bugs, and for the **very** generous award.

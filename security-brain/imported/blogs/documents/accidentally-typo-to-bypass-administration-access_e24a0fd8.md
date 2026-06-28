---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-13_accidentally-typo-to-bypass-administration-access.md
original_filename: 2017-08-13_accidentally-typo-to-bypass-administration-access.md
title: Accidentally typo to bypass administration access
category: documents
detected_topics:
- xss
- sso
- sqli
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- sso
- sqli
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: e24a0fd8191de4755aea928b9dc18199e2eb4f4a17e5974545bde5029da92eef
text_sha256: 91df85a3aee6974a0e377cd99c2168a93d6c0db5b49f1b9baff35d8c56fe257a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Accidentally typo to bypass administration access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-13_accidentally-typo-to-bypass-administration-access.md
- Source Type: markdown
- Detected Topics: xss, sso, sqli, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `e24a0fd8191de4755aea928b9dc18199e2eb4f4a17e5974545bde5029da92eef`
- Text SHA256: `91df85a3aee6974a0e377cd99c2168a93d6c0db5b49f1b9baff35d8c56fe257a`


## Content

---
title: "Accidentally typo to bypass administration access"
page_title: "Accidentally typo to bypass administration access ~ Random stuff by yappare"
url: "http://c0rni3sm.blogspot.com/2017/08/accidentally-typo-to-bypass.html"
final_url: "https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html"
authors: ["yappare (@yappare)"]
bugs: ["Authentication bypass"]
publication_date: "2017-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6125
---

##  [Accidentally typo to bypass administration access](https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html)

on [August 13, 2017](https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html "permanent link") in [BugBounty](https://blog.yappare.com/search/label/BugBounty), [Tricks](https://blog.yappare.com/search/label/Tricks) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/7830476229707305603) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=7830476229707305603&from=pencil "Edit Post")

A new post from me to kill some times.  
  
This was from an old invited private program in one of the bugbounty platform. This program offers $15,000 in total. There were several targets given, but most of them were limited in term of functionalities and forms.  
  
One of the application in scope attracted me as it responded differently if viewed in a different browser's platform. Which means, you will only allowed to access their mobile site if the application detected your user agent is coming from Mobile. This application just consist of few functionalities such as  

  * query for available *item*
  * view for available schedule
  * information of the certain *item*
  * no login

Based on the above functionalities, this seems like a common website that provides with a general information of their product/items. I spent few days looking on their Desktop Website and found few XSS. Looking at the source page of the website, I've noticed there's a script that contain a hyperlink to a mobile site. It looks something like below:  

> <script type="text/javascript">  
>  var attr = "href";  
>  var value = "/mobileapps";  
>  elem.setAttribute(attr, value);  
> </script>

However, I was not able to access it directly using Desktop browser. I tried to change my user agent into Android's string, it worked!  
  
Now I'm in their mobile site. Found another few XSS. Good. Considering the current findings, I'm probably will be rewarded up to $2000 in total. Good enough. But then, something is bothering me where from my Burp's request, there's a 302 redirect response whenever the Burp's Spider tried to access **/admin** path. Weird. I tried to check if there's any JS files that I can use to bypass this thing as what I did like in my previous [blogpost](http://c0rni3sm.blogspot.com/2017/06/from-js-to-another-js-files-lead-to.html).  
  
No success. sadpanda.  
  
But then, during the testing I've mistakenly typo'ed the **/admin** into **/Admin**(_This happen regularly since using Macbook. The keyboard quite small for my finger's size_)  
To the surprise, due to that typo, I was able to access into the administration page. What a magic. It seems there was a weak configuration at their backend which only restrict access for **/admin** BUT not if the word contain at least one capital letter. **/Admin, /aDmin/, /ADMIN** all of these words can be used to bypass the check.  
  
Now I'm in administration page. There were lots of functionalities inside and ALL of them were vulnerable. Reflected and Stored XSS, SQLi, CSRF, and etc. Submitted all of them. Out of $15000, 70% was mine :)  
  
Lessons:  

  1. Do not forget to test in mobile environment 
  2. Do not forget to test target's mobile site
  3. Do not give up if the application looks really simple, there's probably a hidden administration page in it
  4. Look on the application's response. If weird, try to bypass.

Till next time.  
Cheers. 

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html&t=Accidentally typo to bypass administration access "Share this on Facebook")[__](https://twitter.com/home?status=Accidentally typo to bypass administration access -- https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html "Share this on Google+")[__](https://www.linkedin.com/shareArticle?mini=true&title=Accidentally typo to bypass administration access&url=https://blog.yappare.com/2017/08/accidentally-typo-to-bypass.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7830476229707305603&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7830476229707305603&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7830476229707305603&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7830476229707305603&target=facebook "Share to Facebook")

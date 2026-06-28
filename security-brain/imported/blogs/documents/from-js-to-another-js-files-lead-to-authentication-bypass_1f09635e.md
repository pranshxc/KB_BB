---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-06_from-js-to-another-js-files-lead-to-authentication-bypass.md
original_filename: 2017-06-06_from-js-to-another-js-files-lead-to-authentication-bypass.md
title: From JS to another JS files lead to authentication bypass
category: documents
detected_topics:
- xss
- sqli
- command-injection
- file-upload
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- command-injection
- file-upload
- otp
- automation-abuse
language: en
raw_sha256: 1f09635e1562812f43cdfa388834575bd58907fba98f82dcd11392eb5a49bf3c
text_sha256: 6ef072448691bd7e6b8ed7c78c369128db7861de7b116fc5aba29c5f00c30160
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# From JS to another JS files lead to authentication bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-06_from-js-to-another-js-files-lead-to-authentication-bypass.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, file-upload, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1f09635e1562812f43cdfa388834575bd58907fba98f82dcd11392eb5a49bf3c`
- Text SHA256: `6ef072448691bd7e6b8ed7c78c369128db7861de7b116fc5aba29c5f00c30160`


## Content

---
title: "From JS to another JS files lead to authentication bypass"
page_title: "From JS to another JS files lead to authentication bypass ~ Random stuff by yappare"
url: "http://c0rni3sm.blogspot.com/2017/06/from-js-to-another-js-files-lead-to.html"
final_url: "https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html"
authors: ["yappare (@yappare)"]
bugs: ["Authentication bypass"]
publication_date: "2017-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6183
---

##  [From JS to another JS files lead to authentication bypass](https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html)

on [June 05, 2017](https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html "permanent link") in [BugBounty](https://blog.yappare.com/search/label/BugBounty), [Tricks](https://blog.yappare.com/search/label/Tricks) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/7550462690724901797) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=7550462690724901797&from=pencil "Edit Post")

This was found in a private bug bounty. The scope is limited to a few of features that available to the public. Based on the previous reported issues (5 bugs submitted by others so far when I was initially invited), seems it is hard to find a new issue. It also mentioned in the bounty details that  
_  
_

> _If you manage to get into Administration page, report immediately and do not pivot or further testing in /admin_

  
However, there is an administration page which was restricted to unauthenticated and unauthorised users. Browsing to /**login** or **/admin** will redirect us to **https://bountysite.com/admin/dashboard?redirect=/**  
**  
**Bruteforcing the login page probably an option but I'm not a fan of bruteforcing a login page. Looking at the source page, nothing much useful. I started looking on the application's structure. It seems the JS files were located in few directories such as**/lib, /js, /application** and etc.  
Interesting.  
  
I run the BurpSuite and run the Intruder to identify any accessible JS files in these directories. Set the path of attacking/fuzzing points at **https://bountysite.com/admin/dashboard/js/*attack*.js**  
Yep, make sure you didn't forget the **.js** so we will receive the 200 response if the file is accessible. Interesting, again. Because one of the accessible JS files was **/login.js**  
**  
**Accessing the JS file**https://bountysite.com/admin/dashboard/js/login.js** redirect me to the Administration page :) But, I have no permission to view it. Only partial of the interface can be seen.  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtHwrU8A-fRRz35duJx0N_OLsMyThwmRCl7AXUB1-auf48bhqvAdFshW5L4JlzW7Isn5e45iWapbclfXXs7vxft9TqHTJFOhi2mWrM4eq2xupHXy4iVCY2AYLwpucSfgeYbtdbObhLC10/s400/Screen+Shot+2017-06-06+at+11.19.45+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtHwrU8A-fRRz35duJx0N_OLsMyThwmRCl7AXUB1-auf48bhqvAdFshW5L4JlzW7Isn5e45iWapbclfXXs7vxft9TqHTJFOhi2mWrM4eq2xupHXy4iVCY2AYLwpucSfgeYbtdbObhLC10/s1600/Screen+Shot+2017-06-06+at+11.19.45+AM.png)  
---  
SadPanda.jpg  
  
  
  
But I didn't stop at here. It seems weird why the page is loaded as an HTML while I browsed to a .js file? After playing around, I noticed that the actual reason that allowed me to get into this administration page was because the ***login*** word. Yes, as long the request after **/dashboard/** contains a word with the string of ***login***(exception to 'login', this will only redirect me back to the login page.), will allow us to get into this Administrator's interface, but without a right authorisation.  
  
Further tests were performed from this limited Administration's interface. I looked into the source page and again, trying to understand the structures. From this interface, there are some other JS files that helps me to understand how an administrator can perform an action. Some of the action require a valid **token.** I tried to perform the action using the leaked **token** in one of the JS file, not working. The request will be redirect back to the login page. Looked on another JS file, I found there's another path that actually exist which served some content. It was **/dashboard/controllers/*.php**  
  
Again, I run the Intruder to check if there's any other path which can be accessed from here. From the second Intruder attacks, I found few other paths that were exist but have no authorisation to access it. This was based on the 500 or 200 HTTP response.  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_8ERf5gU4_cvQ-ivnA4W9TWj260pjHXuIUu6-SZExELExO-p4Nlqtu2zsRPp8kUzTDUQL5QKpKIyPtDlDAGm50Gt4DefmoNfVqETwokV5Qf8O0hCW4vsNuxoKA-cfq6iRfWNhCVjg-hY/s400/Screen+Shot+2017-06-06+at+11.33.21+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_8ERf5gU4_cvQ-ivnA4W9TWj260pjHXuIUu6-SZExELExO-p4Nlqtu2zsRPp8kUzTDUQL5QKpKIyPtDlDAGm50Gt4DefmoNfVqETwokV5Qf8O0hCW4vsNuxoKA-cfq6iRfWNhCVjg-hY/s1600/Screen+Shot+2017-06-06+at+11.33.21+AM.png)  
---  
SweetPanda.jpg  
Back on the structures that I learnt in the first phase of recon, I found that these path were defined by **/controllers** and being used thru **/dashboard/*here*/**  
However, another bump, directly accessing the path will redirect me to the login page. Seems the session checking quite tough over here. I was about to give up at this point and also sleepy too, but I want to try a last attempt. What if I used the same method to access the Administrative page to access and perform these actions?  
Interesting, climax. :) I'm able to do so.  
  
By browsing to the **/dashboard/photography/loginx** redirected me to the Admin Photography page with the full functionality that I can use.  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK42Ps_ohr5K5hbot2bw0wwMg5dmVD8xmIetBbimnfcD7FzHv7jl96VkHjy6hOy40yoNGw8lVQMTYZeXDHzZjn0P2ZLfbuvoGF3WALXPGvyofJUQ8G3by8a1KypfgifJt3KqK5KuxCZ18/s400/Screen+Shot+2017-06-06+at+11.41.06+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK42Ps_ohr5K5hbot2bw0wwMg5dmVD8xmIetBbimnfcD7FzHv7jl96VkHjy6hOy40yoNGw8lVQMTYZeXDHzZjn0P2ZLfbuvoGF3WALXPGvyofJUQ8G3by8a1KypfgifJt3KqK5KuxCZ18/s1600/Screen+Shot+2017-06-06+at+11.41.06+AM.png)  
---  
Photography functions.  
  
  
From here, I'm able to perform and access all the available actions and paths in **/dashboard/*** which was full with other vulnerabilities such as SQLi, XSS, File Upload, Open Redirect and etc. However, I didn't attempt more on it as all of these issues were out of scope as what had been defined by the program to immediately report to them if the Administration's authentication was found broken. Also, additional notes that I noticed from the debug error enabled on the Administration's page, what made I'm able to access these Administration pages was because of the misconfiguration of the application at **/dashboard/controllers/*** lines where whenever a * **login*** found in the request, the application should redirect to the main login page, however, it was not working as it was intent.  
  
It was a fun day indeed :)  
I was rewarded with the Max amount of this program.  
  
Chio.

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html&t=From JS to another JS files lead to authentication bypass "Share this on Facebook")[__](https://twitter.com/home?status=From JS to another JS files lead to authentication bypass -- https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtHwrU8A-fRRz35duJx0N_OLsMyThwmRCl7AXUB1-auf48bhqvAdFshW5L4JlzW7Isn5e45iWapbclfXXs7vxft9TqHTJFOhi2mWrM4eq2xupHXy4iVCY2AYLwpucSfgeYbtdbObhLC10/s400/Screen+Shot+2017-06-06+at+11.19.45+AM.png&description=From JS to another JS files lead to authentication bypass "Share on Pinterest")[__](https://www.linkedin.com/shareArticle?mini=true&title=From JS to another JS files lead to authentication bypass&url=https://blog.yappare.com/2017/06/from-js-to-another-js-files-lead-to.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7550462690724901797&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7550462690724901797&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7550462690724901797&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=7550462690724901797&target=facebook "Share to Facebook")

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-04-11_how-i-rewarded-with-usdk-just-with-a-simple-search-form.md
original_filename: 2013-04-11_how-i-rewarded-with-usdk-just-with-a-simple-search-form.md
title: How I Rewarded with USD?K Just With a Simple Search Form
category: documents
detected_topics:
- sqli
- xss
- command-injection
- csrf
- api-security
- mobile-security
tags:
- imported
- documents
- sqli
- xss
- command-injection
- csrf
- api-security
- mobile-security
language: en
raw_sha256: 90f0e8049900f56e3ce7165fef8a449424d620f1783a9a2d06ccb4f796377bed
text_sha256: 8772adb8aaf1bfbb267eb7bc1aebb7884f17d1b2d711ed34ff8c9722e302ef21
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I Rewarded with USD?K Just With a Simple Search Form

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-04-11_how-i-rewarded-with-usdk-just-with-a-simple-search-form.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, csrf, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `90f0e8049900f56e3ce7165fef8a449424d620f1783a9a2d06ccb4f796377bed`
- Text SHA256: `8772adb8aaf1bfbb267eb7bc1aebb7884f17d1b2d711ed34ff8c9722e302ef21`


## Content

---
title: "How I Rewarded with USD?K Just With a Simple Search Form"
page_title: "How I Rewarded with USD?K Just With a Simple Search Form  ~ Random stuff by yappare"
url: "http://c0rni3sm.blogspot.com/2013/04/how-i-rewarded-with-usdk-just-with.html"
final_url: "https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html"
authors: ["yappare (@yappare)"]
programs: ["Paypal"]
bugs: ["SQL injection"]
publication_date: "2013-04-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6408
---

##  [How I Rewarded with USD?K Just With a Simple Search Form ](https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html)

on [April 11, 2013](https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html "permanent link") in [Hall of Fame](https://blog.yappare.com/search/label/Hall%20of%20Fame), [Security](https://blog.yappare.com/search/label/Security), [SQLi](https://blog.yappare.com/search/label/SQLi), [XSS](https://blog.yappare.com/search/label/XSS) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/6087859464077066241) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=6087859464077066241&from=pencil "Edit Post")

Hello.  
Its been a while and I'm quite busy with works lately. Today I want to share with you guys on my recent successful findings on Paypal Bug Bounty Program.  
  
Paypal's Bug Bounty Program currently limited its testing application so in order for you to find any bug quite hard nowdays. Read it [here](http://www.ehackingnews.com/2013/02/paypal-running-out-of-money-in-its-bug.html) from ehackingnews  
  
One of the Apps that still under the scope is BillSafe. Previously, I noticed that [@Vigneshkumarmr](https://twitter.com/Vigneshkumarmr) found XSS and CSRF in that application however he was not the one the 1st person found it. [@KrutarthShukla ](https://twitter.com/KrutarthShukla)was the one that rewarded by Paypal for his submissions on Billsafe.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq1QpjzIa5e6Jn_AUhZf42T47puDp78xubPcaJmBCCLFkFxTy7oUm87rqKY1IDNFm2UTZOyu9DTOieHbQagOXq26xuOOy110-tmdXPjsN-RAp6tCvl9_-HM-jX5_paS3BkSZ-qkiPsBWU/s320/vg-xss.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq1QpjzIa5e6Jn_AUhZf42T47puDp78xubPcaJmBCCLFkFxTy7oUm87rqKY1IDNFm2UTZOyu9DTOieHbQagOXq26xuOOy110-tmdXPjsN-RAp6tCvl9_-HM-jX5_paS3BkSZ-qkiPsBWU/s1600/vg-xss.png)

  
  
Then that day I just trying my luck to see if there's any bug that was missed by other researchers/hunters. Looking around..hmm..no luck..until..I met this search form  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifA_viYYJdCbd-QTBVPRgYJIeKxJ24Jhyb-x0XK0fT0Mk_E4nFGSbjUMOuF5smhcg0BICB3DbU8fagHf_aw34fVtNZ2E9CMCkG0tzgGTnpI_tpxTGQkoVgy0WqRktJhySjk-6a3nKeX3U/s320/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifA_viYYJdCbd-QTBVPRgYJIeKxJ24Jhyb-x0XK0fT0Mk_E4nFGSbjUMOuF5smhcg0BICB3DbU8fagHf_aw34fVtNZ2E9CMCkG0tzgGTnpI_tpxTGQkoVgy0WqRktJhySjk-6a3nKeX3U/s1600/1.png)

Its a search form where we can see our transaction history. I tried to search some random words. Nothing unusual.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-LT-JJVhSVsl3I8R7UbWOr9Iae1YVIlOukZFEGsQTrkExiZNUZZcCV2Xh_qr8D2pigXrhN0d_7gsPRdLxYtTqsxmoj0LCZVoPn9Fof5DYKHNGJAGRtC2sn7Dk5vaaGS848Ko0qUtg8PM/s320/2a.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-LT-JJVhSVsl3I8R7UbWOr9Iae1YVIlOukZFEGsQTrkExiZNUZZcCV2Xh_qr8D2pigXrhN0d_7gsPRdLxYtTqsxmoj0LCZVoPn9Fof5DYKHNGJAGRtC2sn7Dk5vaaGS848Ko0qUtg8PM/s1600/2a.png)

  
Then with the power of **double quotes,** BOOM! The page become blank!  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYpM2hH08hPOq1UJAS-7leg79VqjAu4ERXmfdYJSdp2V1GJIBYjkhDhB5TDE_hSIJR3PyetqGoqktVzIUiuxViGHgwTRmDZFx-lkcetjj7VK9OxQw5zlbdbJROt4i3Dc1pJN6XSQPJuE/s320/3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYpM2hH08hPOq1UJAS-7leg79VqjAu4ERXmfdYJSdp2V1GJIBYjkhDhB5TDE_hSIJR3PyetqGoqktVzIUiuxViGHgwTRmDZFx-lkcetjj7VK9OxQw5zlbdbJROt4i3Dc1pJN6XSQPJuE/s1600/3.png)

Aha! Now its weird. At first I thought it might be just a normal error. So I tried to close the **double quotes**.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1ps-ADrtmrHBhCotxI5UkpXX6n2dkbAPs24z96ghEFFNp-AKeu1BSbrJJwbTYroZlLssA0fiT9FgLUlAGlCoHSKFsEjmBOI3yKENl-O_iQ9tkCS0IuKcgdftEquZTsLH3RTW3EpmtQlg/s320/4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1ps-ADrtmrHBhCotxI5UkpXX6n2dkbAPs24z96ghEFFNp-AKeu1BSbrJJwbTYroZlLssA0fiT9FgLUlAGlCoHSKFsEjmBOI3yKENl-O_iQ9tkCS0IuKcgdftEquZTsLH3RTW3EpmtQlg/s1600/4.png)

BAM!! Welcome to papa Blind SQLi!  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcXxr4mKzdvg3V6JajvTsTbQHeaQK9axi6CcIJOloMxQ-i0hRPjbYJ2A-OgIlatAc-8f8pWVVgDS9bDZFhai6L5MvEf379_YiyS_1GfYsZuS9PWJKFb43QT1-dFUuMG8fHEHG69aLi5lc/s320/5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcXxr4mKzdvg3V6JajvTsTbQHeaQK9axi6CcIJOloMxQ-i0hRPjbYJ2A-OgIlatAc-8f8pWVVgDS9bDZFhai6L5MvEf379_YiyS_1GfYsZuS9PWJKFb43QT1-dFUuMG8fHEHG69aLi5lc/s1600/5.jpg)

And it will be not enough with just like that. I need to give them a working POC. Tried to use a common technique. Not working..darn!..I take a look..have a rest..take my coffee..then suddenly..my brain knocked on me _**" lets try with a simple sql query "**_  
_**  
**_So I tried using something like**“ or column_name like “%**  
How it'll working? Simple. If the column_name I guess is TRUE, the page will load normally..else it'll become blank. So does it works?  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKPfwTm3pqZGna9c1BcQ8NtpsUfoRuF1z86vIqthTS4ktLJogTdP8sulF0anLibYXhlNJIMQZ3f7Xvx54DaeaGXgM4-5n8sI4IGB7_-P2pwifomGbCZFz-lV1VdhGn9W3Js5oDxLT-xcI/s320/6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKPfwTm3pqZGna9c1BcQ8NtpsUfoRuF1z86vIqthTS4ktLJogTdP8sulF0anLibYXhlNJIMQZ3f7Xvx54DaeaGXgM4-5n8sI4IGB7_-P2pwifomGbCZFz-lV1VdhGn9W3Js5oDxLT-xcI/s1600/6.jpg)

OF COURSE!

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXdlWqLcRzdBObJwXxC073TREMAqWfMJdBO9o4s4rLdW6B-UKKWsFtnm9k65zKgiYMXhvl2ersxkj9cobyFu-ZcpQSPd0Rz-smQDU8bnWcNQSNKPhWxpehj1fZdqUcDIk1mMV8x9SYUIo/s320/7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXdlWqLcRzdBObJwXxC073TREMAqWfMJdBO9o4s4rLdW6B-UKKWsFtnm9k65zKgiYMXhvl2ersxkj9cobyFu-ZcpQSPd0Rz-smQDU8bnWcNQSNKPhWxpehj1fZdqUcDIk1mMV8x9SYUIo/s1600/7.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB7_tVY-oi_fd0u9xp0DSSML-tWlejuPbJmpN_SI63Z41I1sRnxbhaQN44n1bB3R3Z-mLsmpd9c2dRdU6NcdnfhUM5AdSjcHIzEMSsF_Q9v-JVLGKFQ6bWolrlUjfeqDDv7flA3pt0v-U/s320/8.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB7_tVY-oi_fd0u9xp0DSSML-tWlejuPbJmpN_SI63Z41I1sRnxbhaQN44n1bB3R3Z-mLsmpd9c2dRdU6NcdnfhUM5AdSjcHIzEMSsF_Q9v-JVLGKFQ6bWolrlUjfeqDDv7flA3pt0v-U/s1600/8.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXsX9wT1uYoZXXzWxJwwZ0d_b2PRu-BL7ZH2BRtIY8B1U8CUOXjQGYGLtmMeBjyTzOAvzBuRVDLvJa0VdjcnZ1YfJNMGf8QsGV3CiPdwTT1IvAzr9v_erqjIPHtdJUpsL7fqahwEg61w8/s320/9.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXsX9wT1uYoZXXzWxJwwZ0d_b2PRu-BL7ZH2BRtIY8B1U8CUOXjQGYGLtmMeBjyTzOAvzBuRVDLvJa0VdjcnZ1YfJNMGf8QsGV3CiPdwTT1IvAzr9v_erqjIPHtdJUpsL7fqahwEg61w8/s1600/9.png)

  

and is it done? Yes.For SQLi. As a bonus, I found that this form is vulnerable to XSS as well.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwtwmGzfBEQdgMPn8pb8L2OR8YuwMzuy-MDn1Kr0RhBUusLykkt8EsmfTzZlTW3LyK-ba2R-CMhcSF5Elw_scvdsw8gFQfKSii0L7fBYXUOYiCmZexG8K7QL6DGj4G_4ztP-5w0IIRUt4/s320/10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwtwmGzfBEQdgMPn8pb8L2OR8YuwMzuy-MDn1Kr0RhBUusLykkt8EsmfTzZlTW3LyK-ba2R-CMhcSF5Elw_scvdsw8gFQfKSii0L7fBYXUOYiCmZexG8K7QL6DGj4G_4ztP-5w0IIRUt4/s1600/10.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzMbEDy62SBKddHHuy8eG6xUhC0dovY3YMWwhQz2LByj3xsmdz-2J2-aFoS4ho-wks3MM_-HOtIY_iaLBvp75B5uGq_AqjqbsbuZNqTXejqBXkw1A2XqqpV1dW2P6EFpwQVc9jHau9b3g/s320/12.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzMbEDy62SBKddHHuy8eG6xUhC0dovY3YMWwhQz2LByj3xsmdz-2J2-aFoS4ho-wks3MM_-HOtIY_iaLBvp75B5uGq_AqjqbsbuZNqTXejqBXkw1A2XqqpV1dW2P6EFpwQVc9jHau9b3g/s1600/12.png)

All of these bugs had been fixed by Paypal. And I already received the payment. How much? I leave it to your imagination.  
  
ADIOS!  
  
@yappare. 

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html&t=How I Rewarded with USD?K Just With a Simple Search Form  "Share this on Facebook")[__](https://twitter.com/home?status=How I Rewarded with USD?K Just With a Simple Search Form  -- https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq1QpjzIa5e6Jn_AUhZf42T47puDp78xubPcaJmBCCLFkFxTy7oUm87rqKY1IDNFm2UTZOyu9DTOieHbQagOXq26xuOOy110-tmdXPjsN-RAp6tCvl9_-HM-jX5_paS3BkSZ-qkiPsBWU/s320/vg-xss.png&description=How I Rewarded with USD?K Just With a Simple Search Form  "Share on Pinterest")[__](https://www.linkedin.com/shareArticle?mini=true&title=How I Rewarded with USD?K Just With a Simple Search Form &url=https://blog.yappare.com/2013/04/how-i-rewarded-with-usdk-just-with.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6087859464077066241&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6087859464077066241&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6087859464077066241&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6087859464077066241&target=facebook "Share to Facebook")

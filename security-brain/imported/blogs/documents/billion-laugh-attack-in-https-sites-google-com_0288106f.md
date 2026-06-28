---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-05_billion-laugh-attack-in-httpssitesgooglecom.md
original_filename: 2018-12-05_billion-laugh-attack-in-httpssitesgooglecom.md
title: Billion Laugh Attack in https://sites.google.com
category: documents
detected_topics:
- saml
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- saml
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 0288106f1f3c1f7a43cd9e989267db0f48ecdde8b55214947e449330922e9774
text_sha256: eeb7472f7277fd49315713a6f796958fcabd202241687496d585d3109ccea907
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Billion Laugh Attack in https://sites.google.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-05_billion-laugh-attack-in-httpssitesgooglecom.md
- Source Type: markdown
- Detected Topics: saml, ssrf, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0288106f1f3c1f7a43cd9e989267db0f48ecdde8b55214947e449330922e9774`
- Text SHA256: `eeb7472f7277fd49315713a6f796958fcabd202241687496d585d3109ccea907`


## Content

---
title: "Billion Laugh Attack in https://sites.google.com"
url: "https://blog.intothesymmetry.com/2018/12/billion-laugh-attack-in.html"
final_url: "https://blog.intothesymmetry.com/2018/12/billion-laugh-attack-in.html"
authors: ["Antonio Sanso (@asanso)"]
programs: ["Google"]
bugs: ["Billion laugh attack", "DoS"]
bounty: "500"
publication_date: "2018-12-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5543
---

###  Billion Laugh Attack in https://sites.google.com 

[ December 05, 2018  ](https://blog.intothesymmetry.com/2018/12/billion-laugh-attack-in.html "permanent link")

tl;dr https://sites.google.com suffered from a Billion Laugh Attack vulnerability that made the containerized environment to crash with a single invocation.  

##  Introduction

Few months ago I applied for a talk at a security conference titled _So you wanna be a Bug Bounty Hunter_ but it **was rejected :(**. The reason behind it is that I have been on/off in the bug bounty business for a while as you can see here:  

> Funny. Found in a forgotten drawer from the time I was a bug hunter :p [#facebook](https://twitter.com/hashtag/facebook?src=hash&ref_src=twsrc%5Etfw) [#bug](https://twitter.com/hashtag/bug?src=hash&ref_src=twsrc%5Etfw) [#bounty](https://twitter.com/hashtag/bounty?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/Tt4saGZVLI](https://t.co/Tt4saGZVLI)
> 
> — Antonio Sanso (@asanso) [November 30, 2018](https://twitter.com/asanso/status/1068422162342715393?ref_src=twsrc%5Etfw)

and I would have liked to share some of the things I have learned during these years (not necessary technical advises only). You can find a couple of these advises [here:](https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html)  
  
  

**_Rule #1 of any bug hunter is to have a good RSS feed list_**

  
and [here](https://blog.intothesymmetry.com/2018/02/bug-bounty-left-over-and-rant-part-iii.html):  
  
  

_**The rule #2 of any bug hunter is to DO NOT be to fussy with 'food' specifically with "left over"**_

  

Today's rule is:

_**_**The rule #3 of any bug hunter is DO LOOK at the old stuff**_**_  
  

and I hope you will understand why with the next picture.

  

##  Looking at https://sites.google.com

For some reasons I can't remember I was looking at https://sites.google.com and my attention was caught by something in the bottom left corner:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRcwu2yS6L6hre0kKjbugdx5bmhbrzSwwiKVbhw48D7fv1w5ur0CJJuir-_GoUR5F5qJiC_v-DP8afKVwv9KQBd7jDD0q-7_IdJ6kuZ500cRcQns_MK8VrlDo8_LVoDq49oQqWZQKTHjrX/s640/Screen+Shot+2018-12-05+at+1.45.14+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRcwu2yS6L6hre0kKjbugdx5bmhbrzSwwiKVbhw48D7fv1w5ur0CJJuir-_GoUR5F5qJiC_v-DP8afKVwv9KQBd7jDD0q-7_IdJ6kuZ500cRcQns_MK8VrlDo8_LVoDq49oQqWZQKTHjrX/s1600/Screen+Shot+2018-12-05+at+1.45.14+PM.png)

  

Well do you know what I mean? Considering what I have said above the words "Classic Sites" it is an immediate trigger for my bug bounty mind. So I decided to give a look at this "Classic Sites"__ and I spotted indeed something interesting:

  
__

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3x2dIcpsd-lxuzgK-pOOr1b2KNu-noda5lrF1j5d29Enh63SykHSLw0AxQE78DrmUQY1mTjIGh_9_Q6UewiX97TmoD3ne4ukiVse_-n41EESuGCPnCK4s0Ooprw03gt2NXesIG0sDxLyx/s640/Screen+Shot+2018-12-05+at+1.48.53+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3x2dIcpsd-lxuzgK-pOOr1b2KNu-noda5lrF1j5d29Enh63SykHSLw0AxQE78DrmUQY1mTjIGh_9_Q6UewiX97TmoD3ne4ukiVse_-n41EESuGCPnCK4s0Ooprw03gt2NXesIG0sDxLyx/s1600/Screen+Shot+2018-12-05+at+1.48.53+PM.png)

Using this gadget functionality it is possible to import and XML based gadget to be display to the website. When I see XML import the normal connection for any security person is XXE, so I decided to give a try.

I quickly discovered that Google sites implements this functionality using [Apache Shinding](https://shindig.apache.org/) (an old Apache project now in attic). A quick inspection in the source code (at the end is an open source project :p) showed that the code was safe regarding SSRF and exfiltration but it would be vulnerable to Billion Laugh Attack. And it is basically when I did a Tweet poll:

> So twitterland, I do have a working billion laughs attack on a biiiiiiig website. What should I do?
> 
> — Antonio Sanso (@asanso) [September 28, 2018](https://twitter.com/asanso/status/1045574359455322112?ref_src=twsrc%5Etfw)

After having a chat with few people I have decided to report this to Google and to ask the permission to poke the site for Billion Laugh Attack. And it is basically what I did. As usual Google security was great and gave me the permission to give a try. To be fair they were a bit skeptic that this would actually work but yeah it would not have been a big deal in any case since the target was a containerized environment. So I tried to import an XML with the most classic of the Billion Laugh Attack [payloads](https://raw.githubusercontent.com/asanso/test-git/master/test.txt). And guess what It kind of worked:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg_DfL3wjgFVJpnnYYakq0onovmr0wPmdnCFpiKtz2Ynqda_sPatML_Qw_t3gvd45JL2u6yECwED6elGFpT_yJD0AZLZBGTXlY3FgyvqVDSeNXxV7v_1PFfui4tTamwGa5sOUaiKyvfGKV/s640/Screen+Shot+2018-12-05+at+2.55.31+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg_DfL3wjgFVJpnnYYakq0onovmr0wPmdnCFpiKtz2Ynqda_sPatML_Qw_t3gvd45JL2u6yECwED6elGFpT_yJD0AZLZBGTXlY3FgyvqVDSeNXxV7v_1PFfui4tTamwGa5sOUaiKyvfGKV/s1600/Screen+Shot+2018-12-05+at+2.55.31+PM.png)

Again not a big deal Google side due the virtualized environment. This was quickly fixed as you can see [here](https://tbqdr6drm0op9ehh878ov28gc9qsrqnv-a-sites-opensocial.googleusercontent.com/gadgets/ifr?url=https://raw.githubusercontent.com/asanso/test-git/master/test.txt):  
  
org.apache.shindig.common.xml.XmlException: JAXP00010001: **The parser has encountered more than "64000"** entity expansions in this document; this is the limit imposed by the JDK. At: (1,1)  
  
I was actually a bit surprised by this since in Java the default value of entityExpansionLimit was set to 64000 already in JRE 1.7_45. Does it mean that Google was running a really old version of Java or maybe they were just defaulting to a different value. I do not know.  

##  Summary

Google usually doesn't pay a bounty for DOS vulnerabilities but they did a little exception this time paying a 500$ bounty. As usual big thank to the Google security team and to [Roberto Clapis](https://twitter.com/empijei) for help.  
  
**For more XML trickery[follow me on Twitter](https://twitter.com/asanso). **

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[bounty](https://blog.intothesymmetry.com/search/label/bounty) [vulnerability](https://blog.intothesymmetry.com/search/label/vulnerability)

Labels: [bounty](https://blog.intothesymmetry.com/search/label/bounty) [vulnerability](https://blog.intothesymmetry.com/search/label/vulnerability)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

[ Post a Comment ](https://www.blogger.com/comment/fullpage/post/5832863639484084941/4724172037418169882)

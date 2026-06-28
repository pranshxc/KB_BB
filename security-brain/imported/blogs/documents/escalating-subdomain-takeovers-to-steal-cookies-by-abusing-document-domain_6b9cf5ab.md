---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-23_escalating-subdomain-takeovers-to-steal-cookies-by-abusing-documentdomain.md
original_filename: 2019-05-23_escalating-subdomain-takeovers-to-steal-cookies-by-abusing-documentdomain.md
title: Escalating subdomain takeovers to steal cookies by abusing document.domain
category: documents
detected_topics:
- cors
- oauth
- ssrf
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cors
- oauth
- ssrf
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 6b9cf5ab9cfd3fa88363c9c0ecb2258ec4c36280966842af6f7ab83a254881b1
text_sha256: a1d634687f1ada49ad4445bb90a3993080eba862760290e4b650d5fe2c4eeaeb
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating subdomain takeovers to steal cookies by abusing document.domain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-23_escalating-subdomain-takeovers-to-steal-cookies-by-abusing-documentdomain.md
- Source Type: markdown
- Detected Topics: cors, oauth, ssrf, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6b9cf5ab9cfd3fa88363c9c0ecb2258ec4c36280966842af6f7ab83a254881b1`
- Text SHA256: `a1d634687f1ada49ad4445bb90a3993080eba862760290e4b650d5fe2c4eeaeb`


## Content

---
title: "Escalating subdomain takeovers to steal cookies by abusing document.domain"
url: "https://blog.takemyhand.xyz/2019/05/escalating-subdomain-takeovers-to-steal.html"
final_url: "https://blog.takemyhand.xyz/2019/05/escalating-subdomain-takeovers-to-steal.html"
authors: ["Ameya (@iamTakeMyHand)"]
programs: ["Postmates"]
bugs: ["Subdomain takeover"]
publication_date: "2019-05-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5249
---

# Escalating subdomain takeovers to steal cookies by abusing document.domain

May 24, 2019 • t4kemyh4nd

  

Hi everyone,  
  
It's been a really long time since I've blogged about anything. Mainly because I got a job as security analyst- therefore I've been very busy. And I also got into Synack!  
  
This blog post focuses on one of my recent findings, how I was able to escalate an out of scope subdomain takeover to steal the session cookies. And how I also thought of a few more methods to escalate it, affecting the main domain.  
  
Before I get started with the bug, I would like to talk a little about same-origin policy. If 2 websites want to communicate with each other, or perhaps if 2 hosts want to _interact_ with each other, there could be mainly 2 ways to go around this. The book "Tangled Web" (a great book, do read it) states the following:  
  
_" Attempts to broaden origins or facilitate cross-domain interactions are more common. The two broadly sup- ported ways of achieving these goals are document.domain and postMessage(...)"_  

##  DOCUMENT.DOMAIN

This JavaScript property permits any two cooperating websites that share a common top-level domain (such as example.com, or even just .com) to agree that for the purpose of future same-origin checks, they want to be considered equivalent.  
  
So basically, if **login.example.com** and **www.example.com** both **explicitly** set their document.domain to example.com, this will lax the same-origin policy checks thereafter.  

##  Exploitation

I was hunting on the Postmates bug bounty program from H1. Now this program has a limited scope. I came across an [[in-scope]] endpoint like the following:  
**  
****https://raster-static.postmates.com/?url=**  
**  
**Now this endpoint was only was only accepting image links coming from subdomains of postmates.com. I thought, if somehow I can find a subdomain takeover, maybe I can find an SSRF or perhaps serve my own malicious content to the victim. So I went ahead and fired up some subdomain discovery tools and started sifting through them. I found one subdomain,**impact.postmates.com** , which was prone to a Github subdomain takeover. I went ahead and added the custom domain name to my test repo and the subdomain was mine.  
  
However, I couldn't have access to any backend, so an SSRF was impossible in this case. The max I could do was serve random JPEG's. Bummer.  
  
After a lot of time of thinking, something struck my mind. The main domain for users in Postmates is, **postmates.com**.  
  
Now, "Tangled Web" also states:  
  
_" Simply because login.example.com has set its document.domain to example.com does not mean that it will be allowed to access content originating from the website hosted at http://example.com/. That website needs to perform such an assignment, too, even if common sense would indicate that it is a no-op."_  
_  
_ So,  _if and only if,_**postmates.com** has explicitly set it's document.domain, maybe I could set **impact.postmates.com** 's document.domain to **postmates.com** and access it's cookies somehow?  
  
**Precursor:**_a.xyz.com_ can **NOT** set it's document.domain to _a.a.xyz.com_ or _b.xyz.com_ , but it **CAN** set it's document.domain to _xyz.com_. An example of changing the values of blog.takemyhand.xyz to other settings:  

[![](https://3.bp.blogspot.com/-PNeYO9Suq4s/XOePXQxSYOI/AAAAAAAAAw4/GCJgL1_8L1sRBU14gasWUDPiAkzglZk9wCLcBGAs/s320/Screenshot%2B2019-05-24%2Bat%2B11.33.38%2BAM.png)](https://3.bp.blogspot.com/-PNeYO9Suq4s/XOePXQxSYOI/AAAAAAAAAw4/GCJgL1_8L1sRBU14gasWUDPiAkzglZk9wCLcBGAs/s1600/Screenshot%2B2019-05-24%2Bat%2B11.33.38%2BAM.png)

That being said, I went ahead to check if **postmates.com** had explicitly set their document.domain. They had! Now, you have to keep in mind, that this attack worked only because the main domain of the program was **postmates.com** (that is, document.domain = **postmates.com**) and not something like **www.postmates.com (** document.domain possibly set to **www.postmates.com** , because then I could not set the document.domain of **impact.postmates.com** to **www.postmates.com**). So now all I had to do was, using JS, set the document.domain to **postmates.com** , and add the following code in my javascript to steal the cookies from the main account:

[![](https://1.bp.blogspot.com/-5CFndUHNFD0/XOebNI4kwTI/AAAAAAAAAxQ/6negb6GpcCY7nUH5GZhBXduZPp_ljpHyQCLcBGAs/s320/Screenshot%2B2019-05-24%2Bat%2B12.50.05%2BPM.png)](https://1.bp.blogspot.com/-5CFndUHNFD0/XOebNI4kwTI/AAAAAAAAAxQ/6negb6GpcCY7nUH5GZhBXduZPp_ljpHyQCLcBGAs/s1600/Screenshot%2B2019-05-24%2Bat%2B12.50.05%2BPM.png)

That's it, I could alert the cookies of **postmates.com** now, and possibly perform an account takeover, since I had complete access to the DOM of the main website.  

[![](https://1.bp.blogspot.com/-sppyIP2Y0_s/XOerQr8kWDI/AAAAAAAAAxo/TY-bT06xWuU2994R6vjQLyoGbK8NST3SgCLcBGAs/s400/Screenshot_2019-05-19_at_10.48.38_PM.png)](https://1.bp.blogspot.com/-sppyIP2Y0_s/XOerQr8kWDI/AAAAAAAAAxo/TY-bT06xWuU2994R6vjQLyoGbK8NST3SgCLcBGAs/s1600/Screenshot_2019-05-19_at_10.48.38_PM.png)

While working on this, I even thought of a few other creative ways to escalate an subdomain takeover to increase it's impact:  
  

  * Bypassing X-Frame-Options : SAMEORIGIN
  * Bypassing CORS validation where the Access-Control-Allow-Origin is set to *.example.com (* being any subdomain)
  * Bypassing URL validation wherever applicable (eg. open redirects to steal OAuth login tokens etc.

  

Regards,

t4kemyh4nd

  
_  
__  
_

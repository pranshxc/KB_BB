---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-05-17_how-i-bypassed-facebook-csrf-once-again.md
original_filename: 2016-05-17_how-i-bypassed-facebook-csrf-once-again.md
title: How I bypassed Facebook CSRF once again!
category: documents
detected_topics:
- csrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- otp
- api-security
language: en
raw_sha256: 290bca7d3f1f888ea69d28f959a220b5fe5acedfd39ff78572f3b4e4eacdd160
text_sha256: d256c8c1214316dbfa5ff881c52cea496b08d2542172b0dfd09bf1172d5afa7d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed Facebook CSRF once again!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-05-17_how-i-bypassed-facebook-csrf-once-again.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `290bca7d3f1f888ea69d28f959a220b5fe5acedfd39ff78572f3b4e4eacdd160`
- Text SHA256: `d256c8c1214316dbfa5ff881c52cea496b08d2542172b0dfd09bf1172d5afa7d`


## Content

---
title: "How I bypassed Facebook CSRF once again!"
page_title: "How I bypassed Facebook CSRF once again!
  | 
  Dynamic World"
url: "https://blog.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html"
final_url: "https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html"
authors: ["Pouya Darabi (@Pouyadarabi)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "7,500"
publication_date: "2016-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6295
---

#  How I bypassed Facebook CSRF once again! 

[ 2016 ](https://www.darabi.me/search/label/2016) [ bounty ](https://www.darabi.me/search/label/bounty) [ bug ](https://www.darabi.me/search/label/bug) [ bugbounty ](https://www.darabi.me/search/label/bugbounty) [ bypass ](https://www.darabi.me/search/label/bypass) [ CSRF ](https://www.darabi.me/search/label/CSRF) [ exploit ](https://www.darabi.me/search/label/exploit) [ facebook ](https://www.darabi.me/search/label/facebook) [ facebook exploit ](https://www.darabi.me/search/label/facebook%20exploit) [ hack ](https://www.darabi.me/search/label/hack) [ vulnerability ](https://www.darabi.me/search/label/vulnerability)  
__ Pouya  __[ 9:52 AM  ](https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html "permanent link") __[ 7 comments ](https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html#comment-form)

  

  
  

![](https://cdn.darabi.me/cdn/561602_507358722611692_2134423977_n.jpg)

  

  
I found a vulnerability in Facebook that allowed me to create arbitrary form in Facebook that send a POST request with CSRF token to any Facebook endpoints or external hosts!  
  
It was very similar to [this bug](https://blog.darabi.me/2015/04/bypass-facebook-csrf.html) which I found in 2015.  
  
  
  

> 'fb_dtsg' Anti-CSRF token supposed to get validated at server-side  
>  and if an action request doesn't that token, Facebook will drop the request without any process on it!  
>  ( not all actions, you may find some of them ;-) )

  
I found this vulnerability in [Continued Flow](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/continued-flow/) section of [Lead Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads)!  
  
  

> A continued flow lead ad means the final step is completed on the advertiser's website. The lead ad will collect all of the data provided and pass it to a destination URL using a hash or POST request. This is valuable for flows where you need data that Facebook is unwilling to collect (e.g. passwords for creating an account).

  
  
![](https://cdn.darabi.me/cdn/csrf_2016_rootcause.png)  
---  
Root Cause  
  
Facebook's  _post_ method was used in continued flow and in the method,  _fb_dtsg_ added to every request.  
  

![](https://cdn.darabi.me/cdn/csrf_2016_bypass.png)  
---  
Scenario  
  
  

  
So we need to create a continued flow lead ad and according to the [document](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/continued-flow/) this is only available to whitelisted users.  
But I bypassed this restriction with a simple trick.  
  
Whenever a user creates lead ad form, a JSON object contains data were sent to create endpoint.  
Fortunately I found another endpoint to get created forms as JSON and then I saw these keys:  
  
  
![](https://cdn.darabi.me/cdn/csrf_2016_json.png)  
---  
form JSON  
  
  
I added these keys to _frombuilder_ json with modified values, form created with continued flow.  
There was no server side check ...  
  
**For example disable timeline review action:**  

> Endpoint URL: https://facebook.com/ajax/settings/timeline/review.php 

> Body: tag_approval_enabled=0

> Final URL: https://facebook.com/ajax/settings/timeline/review.php?tag_approval_enabled=0&__a=1

  
  
Finally I tested it with [Facebook Tools](https://developers.facebook.com/tools/lead-ads-testing) and it worked!  
  

###  POC: 

YouTube removed the original video due a unknown reason!  
So I moved my videos to Facebook :)

  

  

  
  

###  Fun Part: 

When custom field name was _fb_dtsg_ ... :D

  

![](https://cdn.darabi.me/cdn/csv_token_2016.png)

  

###  Timeline: 

  * Mar 29 2016 "Like last year ;)" : Initial report
  * Apr 06 2016 : Requested more info
  * Apr 06 2016 : More details sent
  * Apr 07 2016 : Bug acknowledged by security team
  * Apr 07 2016 : Fun part sent!
  * Apr 12 2016 : Bug fixed
  * Apr 13 2016 : Facebook security team rewarded me with a $7,500.
  * Apr 18 2016 : More info about whitelist sent
  * May 06 2016 : Second bug fixed

  

  * [ __ ](https://www.facebook.com/sharer.php?u=https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html&t=How I bypassed Facebook CSRF once again! "Share on facebook")
  * [ __ ](https://twitter.com/intent/tweet?text=How I bypassed Facebook CSRF once again!&url=https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html "Share on Twitter")
  * [ __ ](https://pinterest.com/pin/create/button/?url=https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html)
  * [ __ ](https://www.linkedin.com/shareArticle?mini=true&url=https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html)

[ Older Post ](https://www.darabi.me/2015/04/bypass-facebook-csrf.html "Older Post")

[ Newer Post ](https://www.darabi.me/2017/11/image-removal-vulnerability-in-facebook.html "Newer Post")
  *[
9:52 AM
]: 2016-05-17T09:52:00-07:00

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-06_bug-bounty-left-over-and-rant-part-iii-google-and-twitter.md
original_filename: 2018-02-06_bug-bounty-left-over-and-rant-part-iii-google-and-twitter.md
title: Bug bounty left over (and rant) Part III (Google and Twitter)
category: documents
detected_topics:
- oauth
- saml
- command-injection
- path-traversal
- mfa
- otp
tags:
- imported
- documents
- oauth
- saml
- command-injection
- path-traversal
- mfa
- otp
language: en
raw_sha256: 23b2b9efd03af4aede832981cbac107cbecb0b67577b6d51169faceb25e191ff
text_sha256: c1a8896f210f178368f96849e65825c7d24f47ae7d077873db1caf28efd81613
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bug bounty left over (and rant) Part III (Google and Twitter)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-06_bug-bounty-left-over-and-rant-part-iii-google-and-twitter.md
- Source Type: markdown
- Detected Topics: oauth, saml, command-injection, path-traversal, mfa, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `23b2b9efd03af4aede832981cbac107cbecb0b67577b6d51169faceb25e191ff`
- Text SHA256: `c1a8896f210f178368f96849e65825c7d24f47ae7d077873db1caf28efd81613`


## Content

---
title: "Bug bounty left over (and rant) Part III (Google and Twitter)"
page_title: "Bug bounty left over  (and rant) Part III (Google and Twitter)"
url: "https://blog.intothesymmetry.com/2018/02/bug-bounty-left-over-and-rant-part-iii.html"
final_url: "https://blog.intothesymmetry.com/2018/02/bug-bounty-left-over-and-rant-part-iii.html"
authors: ["Antonio Sanso (@asanso)"]
programs: ["Google", "Twitter"]
bugs: ["OAuth", "Broken authentication", "Information disclosure"]
bounty: "5,540"
publication_date: "2018-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5982
---

###  Bug bounty left over (and rant) Part III (Google and Twitter) 

[ February 06, 2018  ](https://blog.intothesymmetry.com/2018/02/bug-bounty-left-over-and-rant-part-iii.html "permanent link")

tl;dr in this blog post I am going to talk about some bug bounty left over with a little rant.  
  
Here you can find bug bounty left over part [I](http://blog.intothesymmetry.com/2014/09/bounty-leftover-part-1.html) and [II](http://blog.intothesymmetry.com/2014/09/bounty-leftover-part-2-target-google.html)  
Here you can find bug bounty rant part [I](http://blog.intothesymmetry.com/2016/11/all-your-paypal-tokens-belong-to-me.html) and [II](http://blog.intothesymmetry.com/2017/04/csrf-in-facebookdropbox-mallory-added.html)  

##  Introduction

In [one of my previous post ](http://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html)I was saying that: ****  
  

_**"The rule #1 of any bug hunter... is to have a good RSS feed list."**_

  
**** Well well well allow me in this post to state rule #2 (IMHO)  
  
_**"The rule #2 of any bug hunter is to DO NOT be to fussy with 'food' specifically with left over"**_  
  
aka even if the most experience bug hunter was there (and it definitely was my case here, given the fact we are talking about no one less than **[filedescriptor](https://twitter.com/filedescriptor)**) do not assume that all the vulnerabilities have been found! So if you want some examples here we go.****  

#  **Part I - Google**

I have the privilege to receive from time to time [Google Vulnerability Research Grant](https://www.google.com/about/appsecurity/research-grants/). One of the last I received had many target options to choose from, but one in particular caught my attention, namely **Google Issue Tracker**. The reason why I wanted to give a look at it was due the fact I recently read this blog post: [How I hacked Google’s bug tracking system itself for $15,600 in bounties](https://medium.freecodecamp.org/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5). I was really impressed by the quality of this research so I thought I would give a look myself and guess what after about 5 minutes I found some little vulnerability in **Google Issue Tracker**(not of the same caliber as the other report though). This was indeed probably the easier and simpler and tinier vulnerability I ever reported but still :p  
Basically the Google Issue Tracker has a "Copy comment to..." feature:  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8mX0LthE2jyRLJPDjQnHtK4kk_7V_2EnwjmWpoV58y_qoJQ9AVD6uPwwrIwCD8b40vPMqjkAAKLe0ZQ6iS2yNDCQLneCpG4XXDmItGQd5VzKGovNiWdjO6Vx2fqYxlXWbWitsiPv-9WYx/s1600/Screen+Shot+2018-02-06+at+3.04.05+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8mX0LthE2jyRLJPDjQnHtK4kk_7V_2EnwjmWpoV58y_qoJQ9AVD6uPwwrIwCD8b40vPMqjkAAKLe0ZQ6iS2yNDCQLneCpG4XXDmItGQd5VzKGovNiWdjO6Vx2fqYxlXWbWitsiPv-9WYx/s1600/Screen+Shot+2018-02-06+at+3.04.05+PM.png)  
---  
_"Copy comment to..."_  
So basically if you are currently on an issue **source** you can copy comment number X to issue **destination** clicking the button above. This will generate a link of the form  
  
https://issuetracker.google.com/issues/**destination**?template_issue=**source** &template_comment=**X**  
  
and you will have comment **X** from **source** copied to**destination**. But hold on what does it happen if you do not have access to issue **source**? Well here was a little glitch that made anyone potentially knowing the number of comments existing in an issue without having access to that issue. But how? Here is the self explanatory example:  
  

  * Navigate to https://issuetracker.google.com/issues/**destination**?template_issue=**source** &template_comment=4. Observe a read error message saying: "Issue b/source#comment4 does not exist"
  * Navigate to https://issuetracker.google.com/issues/**destination**?template_issue=**source** &template_comment=1. Observe a read error message saying: "Access denied for: <MAIL_ADDRESS>".
  * Navigate to https://issuetracker.google.com/issues/**destination**?template_issue=**source** &template_comment=2. Observe a read error message saying: "Access denied for: <MAIL_ADDRESS>".
  * Navigate to https://issuetracker.google.com/issues/**destination**?template_issue=**source** &template_comment=3. Observe a read error message saying: "Access denied for: <MAIL_ADDRESS>".

Cool. This just told us that the issue **source** has 3 comments (without us having reading access to the issue). Right?  

##  Disclosure timeline 

**23-11-2017 -** Awarded****[Google Vulnerability Research Grant](https://www.google.com/about/appsecurity/research-grants/)  
**30 -11-2017 - **Started giving a look at **Google Issue Tracker**  
**30 -11-2017 (5 minutes later) - **Reported issue to [VRP](https://www.google.com/about/appsecurity/reward-program/)  
**05-12-2017 -** Google internal issue open****  
**14-12-2017 -** Google awarded a 500$ bounty  
  

#  **Part II - Twitter and rant**

This issue was highly inspired by me reading [this blog post](https://blog.innerht.ml/testing-new-features/) from [filedescriptor](https://twitter.com/filedescriptor). In this post [filedescriptor](https://twitter.com/filedescriptor) found an issue in the new OAuth 2 API in [Periscope](https://blog.twitter.com/developer/en_us/topics/tools/2017/introducing-the-periscope-producer-api.html) (little note, while I am a kind of [OAuth 2 expert](https://www.amazon.com/OAuth-2-Action-Justin-Richer/dp/161729327X) I still am not sure I understood this specific issue). Said that this blog post made me curious about this new OAuth implementation hence I decided to give a look at it. This was indeed a great decision since I eventually found a sever issue in the implementation. I do not need to spend too much time talking about this issue since it is identical than some other one I previously found on [Facebook](http://blog.intothesymmetry.com/2014/04/oauth-2-how-i-have-hacked-facebook.html), and Egor Homakov on [Github](http://homakov.blogspot.ch/2014/02/how-i-hacked-github-again.html). This issue is so "popular" that I dedicated a section on the book I [co-wrote about OAuth 2](https://www.amazon.com/OAuth-2-Action-Justin-Richer/dp/161729327X):  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBHDp3Ze8b7hmuA6QTQ5ME8j0VGR4IJSOKhnj1zY1NeN9v_hjTWidjbxQqRMCPscV2ZbBMDoy0Pj6adAxYmj4ee1Sw3eNocc8UeRiwXTECSoyyKlWAj9z4_FT2Dzl9qMTwRzXN4SRvBDx6/s640/page2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBHDp3Ze8b7hmuA6QTQ5ME8j0VGR4IJSOKhnj1zY1NeN9v_hjTWidjbxQqRMCPscV2ZbBMDoy0Pj6adAxYmj4ee1Sw3eNocc8UeRiwXTECSoyyKlWAj9z4_FT2Dzl9qMTwRzXN4SRvBDx6/s1600/page2.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHgzQr81CZ0SvEQj0S0igjiDlIK2Q_lXnACsiP5BgCxTWnq57EVlT_3ufZY6cHq0fJE6JkhNJdfw2MOkbnIJ_qPx8hXL3D-J7v0shsjEF4o4NVW5dN1IVt9QdsX4HnZxFO3KQUSa-k0IkH/s640/page3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHgzQr81CZ0SvEQj0S0igjiDlIK2Q_lXnACsiP5BgCxTWnq57EVlT_3ufZY6cHq0fJE6JkhNJdfw2MOkbnIJ_qPx8hXL3D-J7v0shsjEF4o4NVW5dN1IVt9QdsX4HnZxFO3KQUSa-k0IkH/s1600/page3.png)

  
Providing all those link and references I thought I'd have an easy time collecting a bounty and I opened an issue on Hackerone  
  

> _As seen in<https://hackerone.com/reports/215381> it looks like Periscope.tv implements the OAuth 2 specification.  
>  The redirect_uri validation seems to be vulnerable.  
>  As per <https://hackerone.com/reports/215381> there is a OAuth call_  
>  _[https://www.periscope.tv/oauth?client_id=catbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy&redirect_uri=https://getmevo.com/oauth/periscope&error=true](https://hackerone.com/redirect?signature=608524e15399c6ba8f347b1a7d96d2582f0cc8c3&url=https%3A%2F%2Fwww.periscope.tv%2Foauth%3Fclient_id%3DcatbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy%26redirect_uri%3Dhttps%3A%2F%2Fgetmevo.com%2Foauth%2Fperiscope%26error%3Dtrue "https://www.periscope.tv/oauth?client_id=catbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy&redirect_uri=https://getmevo.com/oauth/periscope&error=true")_  
>  _The registered redirect_uri from client catbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy seems to be[https://getmevo.com/oauth/periscope](https://hackerone.com/redirect?signature=a1c872a1b467111b55fef12ba703bdc9b7ed72c8&url=https%3A%2F%2Fgetmevo.com%2Foauth%2Fperiscope "https://getmevo.com/oauth/periscope")._  
>  _The Periscope OAuth server seems also to accept[https://www.periscope.tv/oauth?client_id=catbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy&redirect_uri=https://getmevo.com/oauth/periscope/../../asanso&error=true](https://hackerone.com/redirect?signature=050c250675d0c37957b0f02c8be8b36a069984a2&url=https%3A%2F%2Fwww.periscope.tv%2Foauth%3Fclient_id%3DcatbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy%26redirect_uri%3Dhttps%3A%2F%2Fgetmevo.com%2Foauth%2Fperiscope%2F..%2F..%2Fasanso%26error%3Dtrue "https://www.periscope.tv/oauth?client_id=catbzQMNEwPxwfvEMqgMFHbNTcwWevGiDRWUaq3aHERZfgnCuy&redirect_uri=https://getmevo.com/oauth/periscope/../../asanso&error=true"). _  
>  _and is indeed vulnerable to path traversal for the redirect_uri. You can see an example of a vulnerability I reported to Facebook that had the same:[http://blog.intothesymmetry.com/2014/04/oauth-2-how-i-have-hacked-facebook.html](https://hackerone.com/redirect?signature=649645d3e834693ebdc74d4d07940a18f2b32a34&url=http%3A%2F%2Fblog.intothesymmetry.com%2F2014%2F04%2Foauth-2-how-i-have-hacked-facebook.html "http://blog.intothesymmetry.com/2014/04/oauth-2-how-i-have-hacked-facebook.html")._  
>  _The impact is the hijacking an access token that is indeed delivered to an attacker location_

  
But this is was not the case :(  

##  Disclosure timeline 

**28-08-2017 -** Opened Hackerone report (see above)  
**29-08-2017 -** Response from Twitter: "We're having some trouble following your report, can you elaborate on exactly what behavior you are reporting and how it leaks the access token..."  
**29-08-2017 -** Gave more details  
**30-08-2017 -** Response from Twitter: "Can you please provide an explanation and demonstration of the behavior you are reporting in your own words here, without linking to these other reports or copying from them..."  
**30-08-2017 -** More info from me  
**31-08-2017 -** Provide some pages of the book I co-wrote (see above) that talk about this specific issue.  
**31 -08-2017 - **Response from Twitter: "As we stated previously, in order to take action on a report for Periscope, we require that you demonstrate an attack that is directed at Periscope specifically and can be actively reproduced....." **Invalid issue and -5 points**  
**31 -08-2017 - **Response from me: "Periscope is an OAuth server with a broken validation algorithm.  
You do not have control of what is the setup and the domain of your potential OAuth clients...  
And with this broken behavior you are putting your 'customers' at risk ."  
**01-09-2017** \- I opened a new Hackerone issue referencing this issue and asking if someone with OAuth 2 knowledge can be assigned to the case  
**01-09-2017 -** Request from Twitter to have more info  
**01-09-2017 -** More info from me  
**01-09-2017******-**** Response from Twitter: "Please keep in mind that our HackerOne program does not accept theoretical or potential vulnerabilities, and requires that researchers demonstrate that the behavior they have found can be actively used in an attack against Twitter or its other in-scope services. Since you have not identified any specific attack against Twitter, we are unable to take further action on your report...." **Invalid issue and -5 points**  
  
I was a bit frustrated at this point **  
**

> so I guess for this time I need to experiment with the lost art of full disclosure sigh<https://t.co/ZDlUpe8Wok> [pic.twitter.com/nAFBQcA4Go](https://t.co/nAFBQcA4Go)
> 
> — Antonio Sanso (@asanso) [September 7, 2017](https://twitter.com/asanso/status/905679236366774272?ref_src=twsrc%5Etfw)

but I have been "invited" to try to "request mediation" from Hackerone  
  

> For the first time ever I had to use [@Hacker0x01](https://twitter.com/Hacker0x01?ref_src=twsrc%5Etfw)'s "request mediation" :( sad<https://t.co/r6F4O3oeWr>
> 
> — Antonio Sanso (@asanso) [September 6, 2017](https://twitter.com/asanso/status/905314469793943552?ref_src=twsrc%5Etfw)

**I must admit it was a bit convoluted, it took a while but it woooooooorkeeeeeeeeeeeed!!!**  
  
****27-10-2017** \- **[Twitter](https://hackerone.com/twitter) rewarded [asanso](https://hackerone.com/asanso) with a **$5,040** bounty.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAmh6r29pfWZ0GA73ePQFrsmD2TQpJUlcP5R5hSeLOXdDkovE6RwxSKXkcdmPkBTUvb4QDrOc7KLNRhNBqRoM43VsLQzZOCb4i7a3DfyVWT9jXCTIlm6gfp-LvuUaD2TIJB3S_CK4YCBGi/s640/Screen+Shot+2018-02-06+at+4.31.06+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAmh6r29pfWZ0GA73ePQFrsmD2TQpJUlcP5R5hSeLOXdDkovE6RwxSKXkcdmPkBTUvb4QDrOc7KLNRhNBqRoM43VsLQzZOCb4i7a3DfyVWT9jXCTIlm6gfp-LvuUaD2TIJB3S_CK4YCBGi/s1600/Screen+Shot+2018-02-06+at+4.31.06+PM.png)

  
At the end of the day also this was an experience. Hence I would like to thank all the security teams involved: Google/Twitter and a big thank to the Hackerone stuff. Request mediation works!  
  
Well that's all folks. **For more OAuth and Webby trickery[follow me on Twitter](https://twitter.com/asanso).  **  
  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[AS vulnerability](https://blog.intothesymmetry.com/search/label/AS%20vulnerability) [bounty](https://blog.intothesymmetry.com/search/label/bounty) [oauth](https://blog.intothesymmetry.com/search/label/oauth) [vulnerability](https://blog.intothesymmetry.com/search/label/vulnerability)

Labels: [AS vulnerability](https://blog.intothesymmetry.com/search/label/AS%20vulnerability) [bounty](https://blog.intothesymmetry.com/search/label/bounty) [oauth](https://blog.intothesymmetry.com/search/label/oauth) [vulnerability](https://blog.intothesymmetry.com/search/label/vulnerability)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

[ Post a Comment ](https://www.blogger.com/comment/fullpage/post/5832863639484084941/2178490539146435970)

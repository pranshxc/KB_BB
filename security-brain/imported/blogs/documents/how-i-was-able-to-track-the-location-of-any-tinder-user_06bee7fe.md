---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-02-19_how-i-was-able-to-track-the-location-of-any-tinder-user.md
original_filename: 2014-02-19_how-i-was-able-to-track-the-location-of-any-tinder-user.md
title: How I was able to track the location of any Tinder user.
category: documents
detected_topics:
- mobile-security
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- mobile-security
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 06bee7fecc0541a3bb500b85bd917702e97e69d9cd65ab512425a0edfe82b164
text_sha256: b7f278b362c5206f5c30bcee18c60f68c1c59051bebe872aae8ff68c9c2cb949
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to track the location of any Tinder user.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-02-19_how-i-was-able-to-track-the-location-of-any-tinder-user.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `06bee7fecc0541a3bb500b85bd917702e97e69d9cd65ab512425a0edfe82b164`
- Text SHA256: `b7f278b362c5206f5c30bcee18c60f68c1c59051bebe872aae8ff68c9c2cb949`


## Content

---
title: "How I was able to track the location of any Tinder user."
page_title: "How I was able to track the location of any Tinder user. - Include Security Research Blog"
url: "https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-the-location-of-any-tinder-user/"
final_url: "https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-the-location-of-any-tinder-user/"
authors: ["Max Veytsman (@mveytsman)"]
programs: ["Tinder"]
bugs: ["Information disclosure"]
publication_date: "2014-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6379
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/tinder-screen-anonymized.png?fit=320%2C427&ssl=1)

# How I was able to track the location of any Tinder user.

February 18, 2021February 19, 2014 — by Max Veytsman

##### By [Max Veytsman](http://twitter.com/mveytsman)

At IncludeSec we specialize in application security assessment for our clients, that means taking applications apart and finding really crazy vulnerabilities before other hackers do. When we have time off from client work we like to analyze popular apps to see what we find. Towards the end of 2013 we found a vulnerability that lets you get exact latitude and longitude co-ordinates for any Tinder user (**_which has since been fixed_**)

[Tinder](http://gotinder.com/) is an incredibly popular dating app. It presents the user with photographs of strangers and allows them to “like” or “nope” them. When two people “like” each other, a chat box pops up allowing them to talk. What could be simpler?

Being a dating app, it’s important that Tinder shows you attractive singles in _your area_. To that end, Tinder tells you how far away potential matches are:  
[![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/tinder-screen-anonymized.png?w=1200&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/tinder-screen-anonymized.png?ssl=1)

Before we continue, a bit of history: In July 2013, a different Privacy vulnerability was [reported](http://qz.com/106731/tinder-exposed-users-locations/) in Tinder by another security researcher. At the time, Tinder was actually sending latitude and longitude co-ordinates of potential matches to the iOS client. Anyone with rudimentary programming skills could query the Tinder API directly and pull down the co-ordinates of any user.  
I’m going to talk about a different vulnerability that’s related to how the one described above was fixed. In implementing their fix, Tinder introduced a new vulnerability that’s described below.

## The API

By proxying iPhone requests, it’s possible to get a picture of the API the Tinder app uses. Of interest to us today is the `user` endpoint, which returns details about a user by id. This is called by the client for your potential matches as you swipe through pictures in the app.  
Here’s a snippet of the response:
  
  
  {
  "status":200,
  "results":{
  "bio":"",
  "name":"Anthony",
  "birth_date":"1981-03-16T00:00:00.000Z",
  "gender":0,
  "ping_time":"2013-10-18T18:31:05.695Z",
  "photos":[
  //cut to save space
  ],
  "id":"52617e698525596018001418",
  "common_friends":[
  
  ],
  "common_likes":[
  
  ],
  "common_like_count":0,
  "common_friend_count":0,
  "distance_mi":4.760408451724539
  }
  }

Tinder is no longer returning exact GPS co-ordinates for its users, but it is leaking some location information that an attack can exploit. The `distance_mi` field is a 64-bit double. That’s a lot of precision that we’re getting, and it’s enough to do really accurate triangulation!

## Triangulation

As far as high-school subjects go, trigonometry isn’t the most popular, so I won’t go into too many details here. Basically, if you have three (or more) distance measurements to a target from known locations, you can get an absolute location of the target using triangulation[1](https://www.blogger.com/blogger.g?blogID=2562550858613734061#fn1). This is similar in principle to how GPS and cellphone location services work.  
[![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/trilateration.png?resize=300%2C220&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/trilateration.png?ssl=1)  
I can create a profile on Tinder, use the API to tell Tinder that I’m at some arbitrary location, and query the API to find a distance to a user. When I know the city my target lives in, I create 3 fake accounts on Tinder. I then tell the Tinder API that I am at three locations around where I guess my target is. Then I can plug the distances into the formula on [this](https://en.wikipedia.org/wiki/Trilateration#Derivation) Wikipedia page.

To make this a bit clearer, I built a webapp….

## TinderFinder

Before I go on, this app isn’t online and we have no plans on releasing it. This is a **serious** vulnerability, and we in no way want to help people invade the privacy of others. TinderFinder was built to demonstrate a vulnerability and only tested on Tinder accounts that I had control of.  
TinderFinder works by having you input the user id of a target (or use your own by logging into Tinder). The assumption is that an attacker can find user ids fairly easily by sniffing the phone’s traffic to find them.  
First, the user calibrates the search to a city. I’m picking a point in Toronto, because I will be finding myself. [![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/03_choose_city.png?w=1200&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/03_choose_city.png?ssl=1)  
I can locate the [office](http://rhino.projectspac.es/) I sat in while writing the app: [![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/04_found_max.png?w=1200&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/04_found_max.png?ssl=1)  
I can also enter a user-id directly: [![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/05_find_user.png?w=1200&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/05_find_user.png?ssl=1)  
And find a target Tinder user in NYC [![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/07_found_clara.png?w=1200&ssl=1)](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2014/02/07_found_clara.png?ssl=1)  
You can find a video showing how the app works in more detail below:  

## FAQ

**Q:** What does this vulnerability allow one to do?  
**A:** This vulnerability allows any Tinder user to find the exact location of another tinder user with a very high degree of accuracy (within 100ft from our experiments)  
**Q:** Is this type of flaw specific to Tinder?  
**A:** Absolutely not, flaws in location information handling have been common place in the mobile app space and continue to remain common if developers don’t handle location information more sensitively.  
**Q:** Does this give you the location of a user’s last sign-in or when they signed up? or is it real-time location tracking?  
**A:** This vulnerability finds the last location the user reported to Tinder, which usually happens when they last had the app open.  
**Q:** Do you need Facebook for this attack to work?  
**A:** While our Proof of concept attack uses Facebook authentication to find the user’s Tinder id, Facebook is **NOT** needed to exploit this vulnerability, and no action by Facebook could mitigate this vulnerability  
**Q:** Is this related to the vulnerability found in Tinder earlier this year?  
**A:** Yes this is related to the same area that a similar Privacy vulnerability was found in July 2013. At the time the application architecture change Tinder made to correct the privacy vulnerability was not correct, they changed the JSON data from exact lat/long to a highly precise distance. Max and Erik from Include Security were able to extract precise location data from this using triangulation.  
**Q:** How did Include Security notify Tinder and what recommendation was given?  
**A:** We have not done research to find out how long this flaw has existed, we believe it is possible this flaw has existed since the fix was made for the previous privacy flaw in July 2013. The team’s recommendation for remediation is to never deal with high resolution measurements of distance or location in any sense on the client-side. These calculations should be done on the server-side to avoid the possibility of the client applications intercepting the positional information. Alternatively using low-precision position/distance indicators would allow the feature and application architecture to remain intact while removing the ability to narrow down an exact position of another user.  
**Q:** Is anybody exploiting this? How can I know if somebody has tracked me using this privacy vulnerability?  
**A:** The API calls used in this proof of concept demonstration are not special in any way, they do not attack Tinder’s servers and they use data which the Tinder web services exports intentionally. There is no simple way to determine if this attack was used against a specific Tinder user.

## Vulnerability Disclosure Timeline

  * October 23rd 2013 – We notified tinder via email to customer service.
  * October 24th 2013 – We notified tinder via email to CEO.
  * October 24th 2013 – Tinder’s CEO acknowledges and says thanks.
  * November 8th 2013 – We ask for status from the CEO, no response.
  * December 2nd 2013 – We ask for status from the CEO, we’re redirected to a tech team lead.
  * December 2nd 2013 – Tech team lead asks for more time to implement a fix, we acknowledge and agree.
  * January 1st 2014 – We look at the server-side traffic to see if the same issue exists and see that the high precision data is no longer being returned by the server (awesome looks like a fix!)
  * January 2nd 2014 – We ask for fix details/status from the tech team lead, no response.
  * February 4th 2014 – We ask for fix details/status from the tech team lead, no response.
  * February 7th 2014 – We ask for fix details/status from the CEO, get short reply saying they’ll get back to us.
  * February 19th 2014 – As the issue does not seem to be reproducible and we have no updates from the vendor….blog post published.

* * *

  1. Technically we’re doing trilateration. Triangulation involves finding distances when you have angle measurements, but it’s used colloquially to mean trilateration as well. If you’re so inclined, you can find out more about trilateration [here](https://en.wikipedia.org/wiki/Trilateration). [↩](https://www.blogger.com/blogger.g?blogID=2562550858613734061#fnref1)

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-the-location-of-any-tinder-user/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-the-location-of-any-tinder-user/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [Exploit](https://blog.includesecurity.com/category/exploit/), [Privacy](https://blog.includesecurity.com/category/privacy/), [Tinder](https://blog.includesecurity.com/category/tinder/), [TinderFinder](https://blog.includesecurity.com/category/tinderfinder/) Post navigation

[How to exploit the x32 recvmmsg() kernel vulnerability CVE 2014-0038](https://blog.includesecurity.com/2014/03/how-to-exploit-the-x32-recvmmsg-kernel-vulnerability-cve-2014-0038/)

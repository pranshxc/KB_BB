---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-07-23_how-i-found-my-way-into-instagrams-ganglia-and-a-bug-with-facebook-likes.md
original_filename: 2013-07-23_how-i-found-my-way-into-instagrams-ganglia-and-a-bug-with-facebook-likes.md
title: How I found my way into Instagram's Ganglia, and a bug with Facebook likes.
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
language: en
raw_sha256: 7942d30598fe88041ac1ec39b2a1d12952ef643b8eba9ca196a01f2b7dbafb7e
text_sha256: fe1753012cb223e6599ffc72119079bd7dfd49ef504e64209f4d0841726d4502
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I found my way into Instagram's Ganglia, and a bug with Facebook likes.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-07-23_how-i-found-my-way-into-instagrams-ganglia-and-a-bug-with-facebook-likes.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `7942d30598fe88041ac1ec39b2a1d12952ef643b8eba9ca196a01f2b7dbafb7e`
- Text SHA256: `fe1753012cb223e6599ffc72119079bd7dfd49ef504e64209f4d0841726d4502`


## Content

---
title: "How I found my way into Instagram's Ganglia, and a bug with Facebook likes."
page_title: "Josip Franjković - archived security blog: How I found my way into Instagram's Ganglia, and a bug with Facebook likes."
url: "https://josipfranjkovic.blogspot.com/2013/07/how-i-found-my-way-into-instagrams.html"
final_url: "https://josipfranjkovic.blogspot.com/2013/07/how-i-found-my-way-into-instagrams.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["Reflected XSS", "IDOR"]
publication_date: "2013-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6401
---

Hello,  
  
I have recently taken part in Facebook Whitehat reward program, and here are some of my findings:  
  

#  Access to Instagram's Ganglia:

  
The original report of this one is too short, so I will post how I got there.  
I have read this old post from [Facebook Bug Bounty official page](https://www.facebook.com/BugBounty):  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMMPJ5P7xHztJcIuSMgs_S08UNqKUTXw88PIcBzKdpzB7S8wepDGWS0fLYGk4M_1ECaVYm0mAQtdmO9JIg4LGBJGmBwLBBe6_RlWf-am7TvrFCI3UlxBVIQDqrdlkOY_mWblNTb8Qu5Hmv/s320/fb1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMMPJ5P7xHztJcIuSMgs_S08UNqKUTXw88PIcBzKdpzB7S8wepDGWS0fLYGk4M_1ECaVYm0mAQtdmO9JIg4LGBJGmBwLBBe6_RlWf-am7TvrFCI3UlxBVIQDqrdlkOY_mWblNTb8Qu5Hmv/s1600/fb1.png)

Great! I'll just run some nmap scans and find something...

2 hours later....

Nothing.

  

After some sub-domain bruteforcing, I have found there is a Ganglia here: [ganglia.instagram.com](http://ganglia.instagram.com/)

Unfortunately, it is protected by basic HTTP auth.

At this point, I did not know what to do, and then it came to me: let me search the all-mighty [Shodan](http://www.shodanhq.com/) for "Instagram.com".

On the second page:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwXVP-N5tJ1EHWeinCFKk9IO2X45vnOr84rXsdgxsXHq7QUfQatwsN5MWRH0sEGCmQ5xuk1HnNPEn8Nu_dwDxTRykZGpWB5Rn7_xqAQ9kesq73495fUv5twkZTSbILqs_yli1fdJUuYt2-/s640/fb2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwXVP-N5tJ1EHWeinCFKk9IO2X45vnOr84rXsdgxsXHq7QUfQatwsN5MWRH0sEGCmQ5xuk1HnNPEn8Nu_dwDxTRykZGpWB5Rn7_xqAQ9kesq73495fUv5twkZTSbILqs_yli1fdJUuYt2-/s1600/fb2.png)

Visit the IP address, and you get Instagram's Ganglia. 

There was also a reflected XSS on **http://23.21.36.116/autorotation.php?view_name= <script>alert(2)</script>**

  

This was reported on 22.4.2013, fixed "5 minutes later" according to Facebook security team, but I believe it was fixed between 23-28 April (I did not really check it).  
**Please, DO NOT test the IP; it is not Facebook's IP anymore.**

  

  

#  Facebook likes bug:

  

This bug is connected with Facebook likes and how Facebook managed them.  
Visibility of likes is connected to visibility of objects (so, if objects is "Friends Only", likes are "Friends only" et cetera), and I have found a way to bypass that - that is, to get likes of the object.  
  
So, whenever your friends like some object, you can check who liked it on following URL:  
  
https://www.facebook.com/browse/likes?id=[[ID of object]].  
  
Example for my profile picture:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhepJ2AcMpljrhTg70xE0j_b8tCSM5BZEgmQjOYmX94KLj5Hw9DDKIyYBKggO2qVLfnGvgVkw9KWBY90qKcP660PoeRN7N3LVYgpv6HIcr600Lucj49i3UiACU0w7VIR0Fc5zCZVflvSX3/s320/fblikes1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhepJ2AcMpljrhTg70xE0j_b8tCSM5BZEgmQjOYmX94KLj5Hw9DDKIyYBKggO2qVLfnGvgVkw9KWBY90qKcP660PoeRN7N3LVYgpv6HIcr600Lucj49i3UiACU0w7VIR0Fc5zCZVflvSX3/s1600/fblikes1.png)

Facebook did not check who was making this request, so **anyone** could view likes of an object. After my first report, Facebook team replied, saying "this is unexpected case, but they will look into it".

This was somewhere at end of December 2012.

  

Great! I should wait for the fix and payment.  

  
Somewhere in June came the reply saying Facebook's security engineer would dig into this more. 

  

**So I replied with better PoC, maybe they take it.**

  

> Hi,  
> 

>  
> 

> While likes may be public, this is really the easiest way to get list of at  
> 

> least some friends of a certain profile.  
> 

> For example, [[some profile]] has a totally closed profile.  
> 

> [[Some profile]] does not allow public to see list of friends; you can check that here:  
> 

> https://www.facebook.com/[[some profile]]/friends

> Now, I go to [[some profile]]'s profile and get list of people who liked that  
> 

> profile picture:  
> 

> https://www.facebook.com/browse/likes?id=[[hidden]]  
> 

> There is currently xx likes there, and they are friends.  
> 

> Is there any way to get list of at least some friends, despite [[Some profile]]'s profile being pretty locked? I am pretty sure no APIs allow that without authorization.

  
The bug was fixed on 11.7.2013.  
  
Engineers from Facebook told me it took that long to fix it because it was not a trivial change to make. I cannot believe how complicated some parts of Facebook are. 

  

**I included this bug to show how even if bug is an "edge case" or "not an issue" first time, you can always try answering with a better PoC.**  

  

**Also, I wanted to show what Facebook takes for "bugs" under privacy - so if you though some "design flaw" you found some time ago is not worth any reward, try reporting it. You might get surprised :)**

  

Payments for these two bugs were quite much more than I expected. 

  

I have found more bugs, mostly in Facebook acquisitions or other Facebook websites. I will post few more bugs later during summer. 

  

Giant thanks to Facebook Security team for their efforts and generous rewards!  
Also, thanks to Shodan for being a great tool!

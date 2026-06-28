---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-25_business-logic-ratings-bug.md
original_filename: 2021-08-25_business-logic-ratings-bug.md
title: Business Logic Ratings Bug
category: documents
detected_topics:
- business-logic
- xss
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- business-logic
- xss
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 8fa87619d4bcc3262b3b371d1c9b7b8589617003f25402e61309b08e7c86f4bb
text_sha256: 87109619daca7291d19bad7a156009de21595792469890cd9591122d5b507df9
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Ratings Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-25_business-logic-ratings-bug.md
- Source Type: markdown
- Detected Topics: business-logic, xss, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `8fa87619d4bcc3262b3b371d1c9b7b8589617003f25402e61309b08e7c86f4bb`
- Text SHA256: `87109619daca7291d19bad7a156009de21595792469890cd9591122d5b507df9`


## Content

---
title: "Business Logic Ratings Bug"
url: "https://maxwelldulin.com/BlogPost?post=7676291072"
final_url: "https://maxwelldulin.com/BlogPost?post=7676291072"
authors: ["Maxwell Dulin (@Dooflin5)"]
bugs: ["Logic flaw"]
publication_date: "2021-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3388
---

![](/static/StrikeoutLongTransparentWhite.png)

### [About](/) [Project](/Project) [Blog](/Blog) [Resources](/Resources)

# Blog[![](https://cdn3.iconfinder.com/data/icons/cosmo-color-basic-2/40/rss-512.png)](https://maxwelldulin.com/api/rss/blog)

# Business Logic Ratings Bug

August 25, 2021

The web is full of user reviewed rating websites that we trust with our lives every day. Glassdoor allows us to see inside a company; Amazon reviews allow us to see what it is like to own a product; Yelp for restaurants... this is just the world that we live in. 

But, what if you could _sway_ the rating system? On Yelp, you could make a restaurant appear at the top of every search! Like in a dream, everyone would flock to your restaurant. Or, you could kill a competitors business, making yours look more appealing. This would be an amazing weapon to gain a competitive advantage on the rest of the market. In this article, we discuss a business logic vulnerability that was able to skew the ratings systems on a popular location-based ratings site. 

##  Vulnerability - The Case of Bad Input Validation 

###  Juice Shop Version 

The company asked to remain anonymous and to have no screenshots of the bug. So, we will get creative! To demo the bug, we will look at [Juice Shop](https://owasp.org/www-project-juice-shop/); the bug from OWASP Juice Shop is essentially the same as the real site. For those not familiar, OWASP Juice Shop is an intentionally vulnerable site from the Open Web Application Security Project (OWASP). In fact, this was one of my main resources for learning prior to becoming a security engineer at my current company. 

OWASP Juice Shop has a _customer feedback_ functionality, which is normal for many applications. This ratings system is on a scale of 1-5 where a sliding scale can be set to choose the rating. On the backend request, this is simply an _integer_ being sent. What if we changed this to something that is NOT 1,2,3,4 or 5? The request for the _customer feedback_ is shown in _Figure 1_ below within Burp. 

![](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/Business-Logic-Ratings-Bug/51398887771_6a87e4f5b8_z.jpg)Figure 1: -100 Rating 

By changing the _rating_ to a non-expected value, such as -100 shown in Figure 1, we can drastically affect the overall customer ratings! This works in either the positive or negative direction. The challenge for this is titled [give a devastating zero-star feedback to the store](https://github.com/apox64/OWASP-Juice-Shop-Write-Up/blob/master/juice-shop-writeup.md#7-give-a-devastating-zero-star-feedback-to-the-store). On Juice Shop, we can change the _rating_ value to be set to 0 in order to solve this challenge. Now, this website is meant to be vulnerable. Does this bug look the same on a real and in production website? 

###  The Actual Site 

The target website stores information about a location and allows for ratings this specific type of location. When giving a rating on the user interface, the options are given as a collection of 5 stars. The user highlights the amount of stars for the rating (1-5) and this is the value sent to the backend. As a result, it is not possible to enter a value other than 1-5 in the UI. As demonstrated in the example above, this is not enough though! Client-side restrictions are a futile security protection. 

This seemed like fertile testing ground to go through, as I remembered the Juice Shop example from years ago. I used a web app pentesters best friend Burp to proxy the request and altered the rating to be **-5000**. But, this failed with a `500` error, which surprised me, since the application had never thrown me a `500` error like this before. After trying increasingly smaller negative numbers, to my surprise, **-500** worked! I did the same thing in the positive direction with positive **500** and this worked as well. It appears they had some sanity checking on the values but not enough. What does this actually mean though? 

###  Impact of Bug 

Most rating systems are calculated by taking the _average_. This average is then used everywhere on the website for finding locations to visit. In fact, this _overall rating_ is the most important descriptor about a location to decide if people do or do not go somewhere. Being able to inject a rating of -500 or +500 would drastically raise the average rating (even past 5 stars) or drop the rating of the location significantly. Raising it could make the location extremely popular while dropping it would make the location unlikely to be visited. 

In a community that relies upon the reviews of others, being able to have this _large of a stake_ in the voting on each location allows for the rise in popularity or the downfall of a place by a single person. This compromises the people sourced system entirely; eventually, this could break the trust of the users and force them to use other services. Luckily, the fix for the bug is simple: only allow values from 1-5 on the backend. 

##  Disclosure 

From previous experiences, I am nervous when trying to report security vulnerabilities. As a result, I have learned to be very kind and come from the perspective of "_I found this bad bug. Please let me help you fix it._ " If you go in guns blazing and attacking the service team with comments about how crappy the software is and how great of a hacker you are, then you are unlikely to have a good response with the team (we've all made this mistake before). Keep this in mind when reporting to companies or people without a formal bug disclosure program especially. Yes, I know testing on these sites is technically illegal; I hope that people see the good in us though, as the testing is done in good faith. In this particular case, the company had the best response I have ever received! 

My initial communication with the company was to a senior engineer over LinkedIn. The company did not have a security email so this was my best course of action. Eventually, a support ticket from the `support@company.com` got back to me as well but hours after the initial contact with the engineer on LinkedIn. 

Since the initial LinkedIn message only allows for only 300 characters, after the initial connection I sent a longer message explaining the details of the bug with a few screenshots. In particular, I sent a screenshot with the overall rating for the location being **0 stars** and the next one being **9 stars** , even though the limit is 5 stars. At this point, the engineer replied _Oh wow, that's pretty bad. we are on it._ " The engineering team fixed the bug immediately. 

After this, the CTO of the company added me on LinkedIn and thanked me for the finding and responsible disclosure. The CTO let me know that a security engineering position would be opening up soon; they wanted me on the short list for the job once the position opened up. Additionally, they offered me a lifetime membership to the application! Considering I use the application quite a lot, this was very exciting for me :) A huge shoutout to the engineer and CTO for the amazing response to the finding. This makes me happy to find bugs and report them to make the internet a safer place. 

##  Conclusion 

Vulnerabilities are not always complicated injection attacks. Commonly, they are centered around how the logic of the site; these bugs are undetectable by scanners. Although throwing `<script>alert(1)</script> ` may find some XSS, lots of bugs require an understanding of the applications logic and expected functionality. Prior to throwing random inputs everywhere, ensure that you understanding the business-logic of the application in test. 

Feel free to reach out to me (contact information is in the footer) if you have any questions or comments about this article. Cheers from **Maxwell "ꓘ"Dulin**. 

  
  

[Maxwell Dulin](https://www.linkedin.com/in/maxwelldulin/)![](/static/Mail.png)Email me![![](/static/twitter.png)Twitter](https://twitter.com/Dooflin5)[![](/static/g.png)Github](https://github.com/mdulin2)[![](/static/admin.png)Admin](/Login)[![](https://cdn0.iconfinder.com/data/icons/basic-ui-elements-round/700/08_rss-512.png)Blog RSS Feed](https://maxwelldulin.com/api/rss/blog)[![](https://cdn0.iconfinder.com/data/icons/basic-ui-elements-round/700/08_rss-512.png)Resources RSS Feed](https://maxwelldulin.com/api/rss/resources)

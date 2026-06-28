---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-07_taking-over-facebook-accounts-using-free-basics-partner-portal.md
original_filename: 2018-02-07_taking-over-facebook-accounts-using-free-basics-partner-portal.md
title: Taking over Facebook accounts using Free Basics partner portal
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
- race-condition
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
- race-condition
- information-disclosure
- api-security
language: en
raw_sha256: fddaa6fac59a1ba18948aafd33598f227d87fe65c15c53335531aba033e7276d
text_sha256: c5aa7a4fd69aa9e9fa15aaf536f032220840db3c1202af1edfa2133243a95a6c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Taking over Facebook accounts using Free Basics partner portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-07_taking-over-facebook-accounts-using-free-basics-partner-portal.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse, race-condition, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `fddaa6fac59a1ba18948aafd33598f227d87fe65c15c53335531aba033e7276d`
- Text SHA256: `c5aa7a4fd69aa9e9fa15aaf536f032220840db3c1202af1edfa2133243a95a6c`


## Content

---
title: "Taking over Facebook accounts using Free Basics partner portal"
page_title: "Taking over Facebook accounts using Free Basics partner portal -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/facebook-partners-portal-account-takeover"
final_url: "https://www.josipfranjkovic.com/blog/facebook-partners-portal-account-takeover"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2018-02-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5981
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Taking over Facebook accounts using Free Basics partner portal 

written on February 7th, 2018

There are a couple [public](https://josipfranjkovic.blogspot.com/2013/11/facebook-bug-bounty-secondary-damage.html) [examples](https://philippeharewood.com/facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-facebook-too/) of Facebook's bug bounty program increasing rewards based on their internal investigation of the report. This is a story of one such report, where a medium-high impact privacy bug turned out to be an **account takeover with no user interaction needed.**

####  Initial report: leaking email address of any Facebook user 

Sometime late September 2017, one of my websites was approved to participate in the Free Basics project by Facebook and I have gained access to their partners portal. After poking around a bit, I have realised adding a new admin user leaks their address in subsequent notification emails. The bug was quite simple to reproduce (copy-paste from my report): 

  1. Using your admin account, go to https://partners.facebook.com/fbs/settings/

  2. Input anything as the name, and in the email field input an email you control.

  3. Click "Add" and intercept the POST request to /mobile/settings/requirements/save/

  4. Change the values[settings.users.userstablecontainer.user_id] GET parameter to an ID of the victim whose email you want to get and forward the request

  5. An email will arrive to your controlled address, which will contain the victim's primary mail as part of <a href link >

Basically, I have added a new admin, and set its partner notifications email to one I control. The notification email itself would leak the admin's primary Facebook email through a n_m GET parameter in one of the links.  
Screenshot: ![Facebook Partners email leak](/resources/img/partners-email.png)

#### Timeline:

  * 30th of September, 2017: Report sent 

  * 2nd of October, 2017: First reply from Facebook's team - triage 

  * 2nd of October, 2017: Account takeover fixed (**note:** I did not know about the takeover yet - the full timeline was communicated to me at a later time) 

  * 24th of October, 2017: Facebook's team has fixed the issue 

The email leak issue was not fixed, so I reply telling them the original steps still work.

  * 31th of October, 2017: Facebook's team informs me this was actually an account takeover bug, and that the original email leak will be fixed later - it was fixed a couple hours later. 

Turns out it was possible to leak login codes somehow. I am pretty sure I have clicked the link itself, and it did not log me in directly. Facebook's team then explained that another parameter from the email link could potentially be used to login to the user's account (with some restrictions) - my test accounts did not have the feature enabled. ![Facebook bounty explanation](/resources/img/partners-bounty.png)

Both of these bugs are fixed.  
Thank you Facebook's security team for being (more than) fair - they could have awarded only the email leak bug, and I would never know this was an account takeover. 

##### Random blog post

Bug bounties 

####  Race conditions on the web 

written on July 12th, 2016

[ Read more ](/blog/race-conditions-on-web)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#076d68746e7729617566696d6c68716e6447606a666e6b2964686a)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković

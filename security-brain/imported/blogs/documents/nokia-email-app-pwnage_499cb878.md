---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-22_nokia-email-app-pwnage.md
original_filename: 2013-10-22_nokia-email-app-pwnage.md
title: Nokia email app pwnage
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 499cb878e4d69dc6e350b8c442af4471fe08a4f399ee0093c1ca776d63a06ee3
text_sha256: 3143d5071f59b3c6506c18e54d7e78c897621249f773e651aca13ff592bd0ec6
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Nokia email app pwnage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-22_nokia-email-app-pwnage.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `499cb878e4d69dc6e350b8c442af4471fe08a4f399ee0093c1ca776d63a06ee3`
- Text SHA256: `3143d5071f59b3c6506c18e54d7e78c897621249f773e651aca13ff592bd0ec6`


## Content

---
title: "Nokia email app pwnage"
page_title: "Shashank's Security Blog: Nokia email app pwnage"
url: "http://blog.shashank.co/2013/10/nokia-email-app-pwnage.html"
final_url: "https://blog.shashank.co/2013/10/nokia-email-app-pwnage.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Nokia"]
bugs: ["XSS"]
publication_date: "2013-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6391
---

This was an interesting bug which I found in the Nokia email app for Symbian mobiles in MARCH 2013.  
The email app was not filtering the JavaScripts in the body part of the mail and thereby leading to JavaScript execution via mail.  
  
**  
****THE VERSION OF NOKIA MAIL: 10.2.0.29(main)****  
****NOKIA 5233 FIRMWARE COMPLETE DETAILS  
software version: v51.1.002  
software version date: 19-10-2011  
custom version : 51.1.002.C01.01  
custom version date: 19-10-2011  
language set: 21  
Model: 5233  
type: Rm-625**  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzvwDCQ2fooHy8ZDTODkFJoIVgh5neZuP5N__UONx-zD6tsP98Uz2f8dQ7x_s5x1WVkf1TBaikXVRkMjwnn78KTWHvtsSpZMTtJFxJ8nDvKC4yLhcUKemPmutuFcuGOdkEjmFD_PjunLUM/s400/Screen2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzvwDCQ2fooHy8ZDTODkFJoIVgh5neZuP5N__UONx-zD6tsP98Uz2f8dQ7x_s5x1WVkf1TBaikXVRkMjwnn78KTWHvtsSpZMTtJFxJ8nDvKC4yLhcUKemPmutuFcuGOdkEjmFD_PjunLUM/s1600/Screen2.jpg)

  
  
  
  
  
  
  
This bug took a long time in fixing but finally when they did ;-) I got a mail from Nokia  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA1HgxWIq4UOwwWFyV_VRy_n4TYKFuoBugTCzxzeUkb1OoWvtJWv5hdtLAwbvq_wB3zebjRmttCJJrjKc7YQN6GJIalHySSSvZN6X2D92SfdiYPXGaWBWgAvKx4AfDGNNKfIhz5dL67Omy/s320/emal.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA1HgxWIq4UOwwWFyV_VRy_n4TYKFuoBugTCzxzeUkb1OoWvtJWv5hdtLAwbvq_wB3zebjRmttCJJrjKc7YQN6GJIalHySSSvZN6X2D92SfdiYPXGaWBWgAvKx4AfDGNNKfIhz5dL67Omy/s1600/emal.PNG)

  

  

TRIBUTE TO MY OLD PAL "NOKIA 5233" who passed away recently breaking its screen, sound system, and everything after slipping off from my hand.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-02_facebook-bugbounty-intercept-incoming-friend-requests-of-victim-addaccept-to-you.md
original_filename: 2018-04-02_facebook-bugbounty-intercept-incoming-friend-requests-of-victim-addaccept-to-you.md
title: 'Facebook BugBounty: Intercept incoming friend requests of Victim add/accept
  to your facebook account'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 74d0b241243e23ea0c37ca72f568025623529d8f010e59a51dbe10ee48efa009
text_sha256: 7b4f38b614739c1d4b42cb974f0c2e687aeeeb7dd6f45dd2b4cb8972f03a8f35
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook BugBounty: Intercept incoming friend requests of Victim add/accept to your facebook account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-02_facebook-bugbounty-intercept-incoming-friend-requests-of-victim-addaccept-to-you.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `74d0b241243e23ea0c37ca72f568025623529d8f010e59a51dbe10ee48efa009`
- Text SHA256: `7b4f38b614739c1d4b42cb974f0c2e687aeeeb7dd6f45dd2b4cb8972f03a8f35`


## Content

---
title: "Facebook BugBounty: Intercept incoming friend requests of Victim add/accept to your facebook account"
page_title: "Hijacking Friend Requests Facebook: White Hat ./FamilyGuy"
url: "https://whitehatfamilyguy.blogspot.com/2019/04/hijacking-friend-requests-facebook.html"
final_url: "https://whitehatfamilyguy.blogspot.com/2019/04/hijacking-friend-requests-facebook.html"
authors: ["Family guy"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2018-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5934
---

###  Hijacking Friend Requests Facebook: White Hat ./FamilyGuy 

[ April 02, 2015  ](https://whitehatfamilyguy.blogspot.com/2019/04/hijacking-friend-requests-facebook.html "permanent link")

## 

##  Facebook BugBounty: Intercept incoming friend requests of Victim add/accept to your facebook account:

###  _Product/URL:_ Facebook android app on facebook

**_Description and Impact_**

**_The issue:_**  
Missing authorisation check while accessing friend request API on android app, an attacker can add friend requests of any facebook user into his own account.

in simple words Peter says:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcXCSnquSwxtz3Tcsn_oppltrX9BaHoGbfO7ARZ9ynSaxula6ljAlQjpYaYXJRKUqn0kxa16XRy1M_5hFncuV0qhnzG5B6Igx4JGhNbpxILDs0m2J2uYzIyfx7OplLqPsfkbU-226-cjI/s640/giphy.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcXCSnquSwxtz3Tcsn_oppltrX9BaHoGbfO7ARZ9ynSaxula6ljAlQjpYaYXJRKUqn0kxa16XRy1M_5hFncuV0qhnzG5B6Igx4JGhNbpxILDs0m2J2uYzIyfx7OplLqPsfkbU-226-cjI/s1600/giphy.gif)

Wait, what, no, no, Peter is a nice fellow.

**_Peter:_** Ok, but still 

Its like I can intercept and accept friend requests from someone which was send to some other user via Facebook send friend request to contacts option.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjizx96s2pmDdeB8BcjbA8-p30-aIIi_bF4FSqSLe8hgMJSoYLhd-_AKe7MWMvE4RDmJ2L6c-nH5RyVnpVlNauiv-PRcq848kHbhN_XelMgeURq1mPgK55LG5_nmWjJKZ5-Xodq1CDRtD0/s400/Capture.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjizx96s2pmDdeB8BcjbA8-p30-aIIi_bF4FSqSLe8hgMJSoYLhd-_AKe7MWMvE4RDmJ2L6c-nH5RyVnpVlNauiv-PRcq848kHbhN_XelMgeURq1mPgK55LG5_nmWjJKZ5-Xodq1CDRtD0/s1600/Capture.JPG)

Let's report!!

**_Sceanrio:_**

X sends friends request by contacts option to Y.

And I can get the request which was send to Y and become friend with X.

  

**_Reproduction Instructions/Proof of Concept:_**

1\. install latest android app. 

2\. Create new account. 

3\. Enter a random mobile number[victim's].

4\. Enter a good name.

5\. Enter gender.

6\. You can skip uploading photo as well as uploading contacts.

7\. As soon as you land on fb home page you can go the friend tabs and can see the friend request that were send to X from Y.

8\. You can accept the friend request of Y and Y is your friend.

  

_**Impact:**_

This bypasses fb authentication to add friends from contact, the valid check to confirm the contact number should come before landing on the home page. Else one can easily accept friend requests thus getting their personal details that are actually meant to be shared with the friends.  
  

**_Reported to Facebook:_** 25th August 2016  
  
_**First reply:**_  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpD0jCy_OJ86pwctwoPjscSVaF_A2CFSCK7RRAOaZZDTmAkiyjhZpb6p9tT7YVXxfHy4DKzm_GwJzzUwCNLEVBIscWqJMAhrWuitUglFvkOXCVTzRPlUXausmqjK__1ZyGhcKcIP8xluI/s400/CaptureNeal.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpD0jCy_OJ86pwctwoPjscSVaF_A2CFSCK7RRAOaZZDTmAkiyjhZpb6p9tT7YVXxfHy4DKzm_GwJzzUwCNLEVBIscWqJMAhrWuitUglFvkOXCVTzRPlUXausmqjK__1ZyGhcKcIP8xluI/s1600/CaptureNeal.JPG)

_**Second reply:**_  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7rxFmVwSyyEfAAnookvbG2OQqoNTc3W6klI7vS2OtGkgd3-_K5ugBPWX5EcvV0Vyb49PrlLJBvq90OBohMnJP7m-E7sWfvPyN4f05yoHkKMZ1Su35AEGm26x-uRI4yRwzlHCl3AbyrVQ/s400/Capture2.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7rxFmVwSyyEfAAnookvbG2OQqoNTc3W6klI7vS2OtGkgd3-_K5ugBPWX5EcvV0Vyb49PrlLJBvq90OBohMnJP7m-E7sWfvPyN4f05yoHkKMZ1Su35AEGm26x-uRI4yRwzlHCl3AbyrVQ/s1600/Capture2.JPG)

_**Fix Confirmed:**_  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQV4e5UweHVZY50wwI6-TF9t-c2LxDDHaW0GbWM77nTQsJNd1sJBuziSzukNDMq7kw9WzgIqq9qcdLlj5b71N2iX5yegp7IRJrCimclmRq5Xox_NvsDsRJSqqrP7L164RXz_db78OYsN0/s640/56Gv.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQV4e5UweHVZY50wwI6-TF9t-c2LxDDHaW0GbWM77nTQsJNd1sJBuziSzukNDMq7kw9WzgIqq9qcdLlj5b71N2iX5yegp7IRJrCimclmRq5Xox_NvsDsRJSqqrP7L164RXz_db78OYsN0/s1600/56Gv.gif)

_Mitigation:_ user was asked to confirm the mobile number, before the friend requests accessibility was allowed.  
  
_**Bounty Awarded:**_  

_**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeRq_hXhUrU1s5Iy6PwdeB0F-Wst6NlIXt9lAdubKNnp097ZvMFs-urxv37HHL8NbXGIII8aMAY3OIC429cxt6xHnt5M87K5s8PvZkBYJ-fJpOIhauuqlllvIs5T4zD7jB_85KMq0Wv9w/s400/Capture3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeRq_hXhUrU1s5Iy6PwdeB0F-Wst6NlIXt9lAdubKNnp097ZvMFs-urxv37HHL8NbXGIII8aMAY3OIC429cxt6xHnt5M87K5s8PvZkBYJ-fJpOIhauuqlllvIs5T4zD7jB_85KMq0Wv9w/s1600/Capture3.JPG)**_

_Meanwhile Lois:_  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikpZiZ8gW_fWUpRJtn04N-8wXW4BGytfOUEJ84BSxRLrds3laUDyofSpY9EdNVannxbo9A9ov_26OHoShe8-YmWEw87EwxE3zNj-syXy8zY5Ia_ZiwTQQ3ND1LNOR5rVZtOw0HZs34J8E/s400/hqdefault.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikpZiZ8gW_fWUpRJtn04N-8wXW4BGytfOUEJ84BSxRLrds3laUDyofSpY9EdNVannxbo9A9ov_26OHoShe8-YmWEw87EwxE3zNj-syXy8zY5Ia_ZiwTQQ3ND1LNOR5rVZtOw0HZs34J8E/s1600/hqdefault.jpg)

[****](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgszC_24bHXpPuHSaUTQJjhtbBaSYLnhTlMVWs2qKqumHlhMTTi5rr8YiHw0OZgAmXGhwDxUVLmkASD3C6UkRDA6iVEBGIwF2gZwyEbOpNWkSGbvZMgYQgMi4N07vKY4Pde4FXINrxMQhE/s1600/1gKc.gif)

**_and Stewie :D_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQ0tN2n1ksSzzK9KINkqVqBk-kXUoovpdfpd9uEqzT49vsaCnFVmk5fjpOM9UDQAo0dXhOZequIi7RxLHJzIVMM3gTxfcIGKKuyrI8SZqm0KE1f_gHBQuegjVSjHzLncfpUq7Hk6WgwMs/s400/giphy+%25281%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQ0tN2n1ksSzzK9KINkqVqBk-kXUoovpdfpd9uEqzT49vsaCnFVmk5fjpOM9UDQAo0dXhOZequIi7RxLHJzIVMM3gTxfcIGKKuyrI8SZqm0KE1f_gHBQuegjVSjHzLncfpUq7Hk6WgwMs/s1600/giphy+%25281%2529.gif)

**_and me :_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifCBpPE_PF-Xln-HAiEI7khLpXNNpNBEYquM_P2niLdxSemL9u0XhOa6vo3WB_yDzCU-D9dhwuuNt7PD8j0Lv75ZmL7h9RkG-FKDQs-UNYYxCmV3K_PC6rZ7UggD0MzRRostGtqTSyjbI/s640/SentimentalTastyArieltoucan-size_restricted.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifCBpPE_PF-Xln-HAiEI7khLpXNNpNBEYquM_P2niLdxSemL9u0XhOa6vo3WB_yDzCU-D9dhwuuNt7PD8j0Lv75ZmL7h9RkG-FKDQs-UNYYxCmV3K_PC6rZ7UggD0MzRRostGtqTSyjbI/s1600/SentimentalTastyArieltoucan-size_restricted.gif)

  

**Thanks Facebook Security for the quick resolution and an awesome program:**

**_./Family Guy_**

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Alex](https://www.blogger.com/profile/17900894053863169959)[April 25, 2019 at 3:19 AM](https://whitehatfamilyguy.blogspot.com/2019/04/hijacking-friend-requests-facebook.html?showComment=1556187582849#c6836714569143842461)

well, this was scary. You would have known easily who all were stalking girls :D  
and also having access to the friends only content, am still interested how much facebook paid for !  
  
Nice one, Family Guy :)

Reply[Delete](https://www.blogger.com/comment/delete/181979799605168940/6836714569143842461)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/181979799605168940?po=3178973750024100176&hl=en&saa=85391&origin=https://whitehatfamilyguy.blogspot.com&skin=notable)

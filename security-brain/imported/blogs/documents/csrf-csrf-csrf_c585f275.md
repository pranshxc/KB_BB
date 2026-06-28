---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-03_csrf-csrf-csrf.md
original_filename: 2020-02-03_csrf-csrf-csrf.md
title: CSRF CSRF CSRF…
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: c585f275130f38b79fdef51eb73097e4be7c3af0d56ffad6aa31a69527dcae1b
text_sha256: b2bdc7f2259f17f6945aee1fd7a4334d8fbe3acb18b3ab7f937b5ebf0b90549a
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF CSRF CSRF…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-03_csrf-csrf-csrf.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c585f275130f38b79fdef51eb73097e4be7c3af0d56ffad6aa31a69527dcae1b`
- Text SHA256: `b2bdc7f2259f17f6945aee1fd7a4334d8fbe3acb18b3ab7f937b5ebf0b90549a`


## Content

---
title: "CSRF CSRF CSRF…"
url: "https://medium.com/@navne3t/csrf-csrf-csrf-f203e6452a9c"
authors: ["Navneet (@na5n33t)"]
bugs: ["CSRF"]
bounty: "50"
publication_date: "2020-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4797
scraped_via: "browseros"
---

# CSRF CSRF CSRF…

Top highlight

CSRF CSRF CSRF…
Navneet
Follow
3 min read
·
Feb 3, 2020

51

1

This article is about few CSRFs i have found in private programs. Although all these CSRFs are of low impact but enough to get paid/swag.The aim of this article is to let beginners/readers know what functionality or action could be vulnerable to CSRF in a web application. Feed backs and comments are welcomed.

1.) CSRF to spam shopping cart.

The first functionality where i had found CSRF was adding all products of some public wish-list in to your cart.

This website have the functionality which let user to add the wish-list of other user in to his/her cart. So, user A can add products to his/her wish-list and can make his/her wish-list public which let other users to see the wish-list. Now, as user B there is a button of add to cart , when you click on it that public wish-list will be added in to your cart.

The button was making a simple HTTP GET request which looks like this

https://www.SomeWebsite.com/xyz?some_page=wishlist&move_all=true&w_id=1337&public_cid=31337

There were no HTTP headers which contains CSRF Token and none of the parameter was there to protect it from CSRF.

So, attacker can add alot of products in to his/her wishlist and then perform CSRF to spam the cart of victim.

Reward/bounty

This was fixed within a day and $25 was rewarded for this.

2.) Bypass of CSRF protection to delete the bookmark.

The second CSRF was found at the functionality which can let user to delete his/her bookmark jobs.

As i mentioned above this delete button was also making GET HTTP request BUT i was not able to perform CSRF. I looked for the reason why CSRF is not working for this request and then i realise it could be referer header which may be protecting this request from CSRF. So, i thought of trying the bypass where you can create the whole path of website in your website.

e.g.

myCSRFwebsite.com/www.victimWebsite.com/abc/xyz/csrf.html

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The website was checking the value of referer header , whether it contains the path

www.victimWebsite.com/abc/xyz/csrf.html

and thus , attacker’s website contains the folders/path as above string , website allows the CSRF.

Here is the link of write-up of the bypass

https://medium.com/bugbountywriteup/critical-bypass-csrf-protection-on-ibm-313ffb68dd0c

Reward/bounty

I thought I will get good amount because I showed them how CSRF protection can be bypassed but they paid only $25 for this.

3.) CSRF disguised in APIs

I have found this CSRF in a private program of hackerone where the whole website was calling the API to perform the actions. So, i thought there will be no chance of CSRF because all API calls to perform any action contains the Auth-header which protect the request from CSRF. But after looking at every request i found two endpoints , one of which performs deletion of phone number and the other was changing the communication settings and the best part was it was GET request and POST Request respectively with no CSRF token. After this i realise , it is best to look for all the actions , may be there are some actions which is not performed by API and can be vulnerable to CSRF.

Reward/Bounty

I got no bounty for this , but got 14 repo points at hackerone. I added this bug in this article because i learned something new from this finding.

4.) CSRF to delete favourite list [T-Shirt as a swag].

There was a section in the website which let user to favourite the articles. Now there was also a button to delete the favourite list. And that action was done by a POST HTTP request with no CSRF Token in the POST request. So, CSRF can be performed to Delete the article from favourite list.

Reward/bounty

They sent me a T-shirt as a reward/swag.

Thanks! Hope you like this post. Feel free to comment.

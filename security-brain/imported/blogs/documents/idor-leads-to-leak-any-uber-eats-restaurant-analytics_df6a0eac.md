---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-02_idor-leads-to-leak-any-uber-eats-restaurant-analytics.md
original_filename: 2021-05-02_idor-leads-to-leak-any-uber-eats-restaurant-analytics.md
title: IDOR Leads To Leak Any Uber Eats Restaurant Analytics
category: documents
detected_topics:
- idor
- automation-abuse
- jwt
- xss
- command-injection
- otp
tags:
- imported
- documents
- idor
- automation-abuse
- jwt
- xss
- command-injection
- otp
language: en
raw_sha256: df6a0eacafe81a4194e6422b1b2c14beda8315242f96e7cb72cae71cb005e739
text_sha256: f52c37c8c402cfff1816405bd0f6ceced25d7bdc3414ca975ffec78d9dff2186
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR Leads To Leak Any Uber Eats Restaurant Analytics

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-02_idor-leads-to-leak-any-uber-eats-restaurant-analytics.md
- Source Type: markdown
- Detected Topics: idor, automation-abuse, jwt, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `df6a0eacafe81a4194e6422b1b2c14beda8315242f96e7cb72cae71cb005e739`
- Text SHA256: `f52c37c8c402cfff1816405bd0f6ceced25d7bdc3414ca975ffec78d9dff2186`


## Content

---
title: "IDOR Leads To Leak Any Uber Eats Restaurant Analytics"
page_title: "IDOR Leads To Leak Any Uber Eats Restaurant Analytics - 0xPrial"
url: "https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/"
final_url: "https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["Uber"]
bugs: ["IDOR"]
bounty: "2,000"
publication_date: "2021-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3683
---

Skip to content

[ ![](https://0xprial.com/wp-content/uploads/2022/01/prial-islam65.png) ](https://0xprial.com)

  * [Home](https://0xprial.com/)
  * [About Me](https://0xprial.com/#aboutme)
  * [Skills](https://0xprial.com/#skils)
  * [Services](https://0xprial.com/#services)
  * [Acknowledgements](https://0xprial.com/#acknowledgements)
  * [Write-Ups](https://0xprial.com/#writeUps)

__ Menu

  * [Home](https://0xprial.com/)
  * [About Me](https://0xprial.com/#aboutme)
  * [Skills](https://0xprial.com/#skils)
  * [Services](https://0xprial.com/#services)
  * [Acknowledgements](https://0xprial.com/#acknowledgements)
  * [Write-Ups](https://0xprial.com/#writeUps)

[ Contact Me ](https://0xprial.com/contact)

![](https://0xprial.com/wp-content/uploads/2021/05/IDOR-Leads-To-Leak-Any-Uber-Restaurants-Analytics-1-1024x597.png)

# IDOR Leads To Leak Any Uber Eats Restaurant Analytics

**Hi fellow Hackers** ,  
At first **Ramadan Kareem!** Wishing everyone a very happy Ramadan. Today I will write about an Insecure direct object references (**IDOR**) vulnerability that I recently discovered in Uber Eats Restaurant.

The **Uber Eats Restaurant** web application at <https://restaurant.uber.com/> is using GraphQL. Back in March, I was doing a collaboration on a **Uber** report with**[Sifat](https://www.facebook.com/xhatanubis)** Bhai. On that engagement, he discovered an IDOR in GraphQL that leaks data of other Restaurants but that leaked data was not giving any sensitive information to make a report on it. So I decided to take a look at that functionality. 

_**Issue Background**_**:** In the Uber Eats for Restaurant dashboard, there is an **Analytics** option where store owners can see **Restaurant Analytics** of the last 12 months. **Analytics** endpoint looks `https://restaurant.uber.com/v2/home/{locationUUIDs}``/analytics/sales` where multiple GraphQL requests pullup all data and parse it in that webpage to a readable view. Now I noticed all those requests contain **locationUUIDs** parameter like `"locationUUIDs":["0292a209-df33-496b-b65b-192c86603d48"]}` where **0292a209-df33-496b-b65b-192c86603d48** is my own test account **locationUUIDs** value. When I changed the **locationUUIDs** value to another account **locationUUIDs** value it responded the same with some **JSON** data in the body that took my attention. But still response body data is not helpful as it is not properly readable and in order to read the data we need to parse it through the webpage.

_**Automation with Burp**_**:** To do the data parsing job I used Burp Suite Tool’s **Match and Replace** option.

  1. In Burp go to **Proxy = > Options => Match and Replace**

  2. Click on **Add** and set up a rule like the below screenshot where **Match** value is my own restaurant’s **locationUUIDs** and **Replace** value is any other restaurant’s **locationUUIDs**. 

![Match-and-Replace](https://0xprial.com/wp-content/uploads/2021/05/Match-and-Replace-1024x751.png)

  3. I also added a rule like the below screenshot to change the currency from **BDT** to **USD** to get all analytics in USD currency.![Currency Match and Replace](https://0xprial.com/wp-content/uploads/2021/05/Currency-Match-and-Replace-1024x750.png)

### Final Exploit

  1. Visit [https://restaurant.uber.com](https://restaurant.uber.com/) and log in using a valid restaurant account username and password and do proper authentication.
  2. Now setup Burp Suite Tools with that browser and keep **Intercept OFF**
  3. Visit `https://restaurant.uber.com/v2/home/{victims_locationUUIDs}/analytics/sales`
  4. All request of the browser will go through Burp & `Match and Replace` rule will replace all `**locationUUIDs**` parameter value and all data will parse into a readable view on that webpage.![](https://0xprial.com/wp-content/uploads/2021/05/Sales-by-hour.png)![Sales data](https://0xprial.com/wp-content/uploads/2021/05/Sales-data.png)![Sales by Item](https://0xprial.com/wp-content/uploads/2021/05/Sales-by-Item.png)

### Impact

An attacker can access all analytics of a restaurant what includes actions

  * Choose a date range to see that date range analytics.
  * Orders analytics view and Clicking on Download will Download a CSV copy.
  * Track orders placed over time to monitor a restaurant’s popularity.
  * Track ticket size over time to see if a restaurant’s receiving larger orders.
  * Learn when a target store tends to generate most of its sales.
  * Learn when customers tend to place the most orders in a target restaurant.
  * Learn when customers tend to place the largest orders in a target restaurant.
  * See which items are a restaurant’s top sellers.

To exploit a stored attacker just needs the **locationUUIDs** parameter value and I showed the **Uber Security team** a promising way to **fuzz** the value for any restaurant. This vulnerability was reported in report [#1116387](https://hackerone.com/reports/1116387) under [Uber Bug Bounty Program](https://hackerone.com/uber) and **`$2,000`** Bounty was Rewarded. Check out the video POC too.

Hope you guys enjoyed this one. 

#Stay_Home  
#Stay_Safe  
#Wash_Your_Hand_Frequently  
#Hack_The_Planet🔥

Post Views: 22,073

  * [ May 2, 2021  ](https://0xprial.com/2021/05/02/)
  * 5:38 am 
  * [ 20 Comments  ](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comments)

[ Back To Blog ](https://0xprial.com/0xprialw/blog/)

[ Back To Home ](https://0xprial.com)

##  20 Responses 

  1. ![](https://secure.gravatar.com/avatar/d487beef429f9243a1a4e7d0a5e7b183e8d0fa4737272218cbb2857d97a8bb29?s=42&d=mm&r=g) **[0x0Asif](https://0x0asif.com)** says:

[May 22, 2021 at 5:18 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-31)

Nice Boi…

Reply

  1. ![](https://secure.gravatar.com/avatar/360fd8882f120689d37504a3be51e2c7cf67ea8edcb41a7ace6b3ece5b6928b0?s=42&d=mm&r=g) **wannabe hacker** says:

[July 18, 2021 at 6:26 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-36)

nice blog , keep it up

Reply

  2. ![](https://secure.gravatar.com/avatar/2674f7c3e439bb40ac65ecb074522e0e7e47e495b28cff0598eceb381f73715e?s=42&d=mm&r=g) **[youssef samir](http://squnity.com)** says:

[May 22, 2021 at 8:24 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-32)

this blog isn’t useful at all , the only thing that could be useful is if you explain how you were able to guess the uuid of any restaurant and you don’t explain that

Reply

  1. ![](https://secure.gravatar.com/avatar/5e73a9d4ce6ecb6b83346be0c2096bb0ec86b88ceb9e8ad4c812b1e95e16f1b8?s=42&d=mm&r=g) **[0xPrial](https://0xprial.com)** says:

[May 22, 2021 at 8:54 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-33)

I was able to get any store uid too, but can’t disclose that part as in my article review process uber team asked me to remove that part for their internal reasons 😇 and I can’t disclose that part without their permission.

Reply

  1. ![](https://secure.gravatar.com/avatar/d20d9b13bd0a1301d1a55856c42c240e5aade5e078e9e72d0df9b9f0ea3b8bec?s=42&d=mm&r=g) **James** says:

[May 25, 2021 at 5:30 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-34)

I don’t think “fuzz” is the correct word as the space for burteforcing the all possibilities of UUIDv4 is too large to be feasible. I think it was more likely that you found the stores’ UUID through other pages.

Reply

  1. ![](https://secure.gravatar.com/avatar/5e73a9d4ce6ecb6b83346be0c2096bb0ec86b88ceb9e8ad4c812b1e95e16f1b8?s=42&d=mm&r=g) **[0xPrial](https://0xprial.com)** says:

[May 25, 2021 at 6:51 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-35)

You are correct on this. I was able to get any store uid, but can’t disclose that part as in my article review process uber team asked me to remove that part for their internal reasons 😇 and I can’t disclose that part without their permission.

Reply

  3. ![](https://secure.gravatar.com/avatar/3c348763c06ddecb2c3ca19bb3942d880711654d5cbf64a2f2c9e7103ffb435d?s=42&d=mm&r=g) **[zoritoler imol](https://www.zoritolerimol.com)** says:

[April 8, 2022 at 4:09 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-69)

I envy your piece of work, regards for all the interesting posts.

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[May 18, 2022 at 3:47 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-168)

Thanks for your feedback 

Reply

  4. ![](https://secure.gravatar.com/avatar/cdcbaf7a16aa701c75efe3f38213e5e4668016d81198c611e9c82d9d31ef68d9?s=42&d=mm&r=g) **msalihb** says:

[April 22, 2022 at 12:16 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-82)

Thank you for awesome write up. Actually If I found this bug, I think that “I can’t find uuid of anyone” Because this uuid’s are not fuzzable. The complexity becomes too high. 

Are you found a way to find, or really they accepted the vulnerabilty on this status I really wonder.

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[May 18, 2022 at 3:39 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-167)

Can you dm me on facebook or twitter on this matter? or email me a [ad***@*ri.al](/cdn-cgi/l/email-protection#5534317f7f7f157f273c7b3439 "This contact has been encoded by Anti-Spam by CleanTalk. Click to decode. To finish the decoding make sure that JavaScript is enabled in your browser.") ?

Reply

  5. ![](https://secure.gravatar.com/avatar/a0101fedacc376ecdb6507208094c13e228b51d139789809d81f7343a299a9e1?s=42&d=mm&r=g) **[graliontorile](http://www.graliontorile.com/)** says:

[April 29, 2022 at 8:15 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-91)

Hello my friend! I want to say that this article is awesome, nice written and include almost all significant infos. I would like to see more posts like this.

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[May 18, 2022 at 3:37 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-164)

Thanks a lot for your feedback 😀

Reply

  6. ![](https://secure.gravatar.com/avatar/5274b8383d175619fddd8d02dd6f72006137dc70a09ea385c0b51525d7b39940?s=42&d=mm&r=g) **[zoritoler imol](https://www.zoritolerimol.com)** says:

[April 29, 2022 at 4:12 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-92)

Some genuinely marvellous work on behalf of the owner of this web site, perfectly outstanding written content.

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[May 18, 2022 at 3:37 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-163)

Thanks a lot for your feedback 😀

Reply

  7. ![](https://secure.gravatar.com/avatar/f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a?s=42&d=mm&r=g) **Rashedul** says:

[May 7, 2022 at 8:24 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-101)

Find it useful, Prial Vai! ❤

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[May 18, 2022 at 3:34 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-155)

Thanks a lot for your feedback 😀

Reply

  8. ![](https://secure.gravatar.com/avatar/c1becc84ce0a2eef1a287883d9a34bc70ddb7f1e2e384b6af610b9750291f04b?s=42&d=mm&r=g) **khan mmm** says:

[June 1, 2022 at 1:22 AM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-235)

how to attacker know victim uuid..what is that?

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[August 20, 2022 at 9:49 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-267)

I DISCOVERED A WAY TO DIG IT OUT BUT UNFORTUNATELY UBER TEAM DIDN’T ALLOW ME TO DISCLOSE THAT PART 😀

Reply

  9. ![](https://secure.gravatar.com/avatar/8d65ab594c93dd7c6b400c0e3d89bfde7ac5a96d50d65d14d6bc7dbc0733b883?s=42&d=mm&r=g) **[zoritoler imol](https://www.zoritolerimol.com)** says:

[August 20, 2022 at 9:05 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-256)

wonderful post, very informative. I wonder why the other specialists of this sector do not notice this. You should continue your writing. I am confident, you’ve a great readers’ base already!

Reply

  1. ![](https://secure.gravatar.com/avatar/3ce9e7782d1d69903fce7abab4d718a9b7372a0fbecff86aa8d6f6f95efc0d1e?s=42&d=mm&r=g) **[0xPrial](https://0xPrial.com)** says:

[August 20, 2022 at 9:38 PM](https://0xprial.com/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#comment-257)

Thanks for your words 😀

Reply

## Leave a Reply [Cancel reply](/idor-leads-to-leak-any-uber-eats-restaurant-analytics/#respond)

Your email address will not be published. Required fields are marked *

Comment *

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

**Captcha** *

![](data:image/png;base64,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)Type the text displayed above:

## RECENT TWEETS 

[Tweets by 0xPrial](https://twitter.com/0xPrial?ref_src=twsrc%5Etfw)

## RECENT POSTS 

[ ![The Art Of Zendesk Hijacking](https://0xprial.com/wp-content/uploads/2023/11/The-Art-Of-Zendesk-Hijacking-768x448.png) ](https://0xprial.com/the-art-of-zendesk-hijacking/)

Bug Bounty

###  [ The Art Of Zendesk Hijacking ](https://0xprial.com/the-art-of-zendesk-hijacking/)

[ ![](https://0xprial.com/wp-content/uploads/2023/01/Subdomain-Hijacking-OF-Any-Qwilrs-customer-768x448.png) ](https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/)

Bug Bounty

###  [ Subdomain Hijacking Of Any Qwilr’s Customer ](https://0xprial.com/subdomain-hijacking-of-any-qwilrs-customer/)

[ ![](https://0xprial.com/wp-content/uploads/2021/02/HOW-TO-GET-STARTED-IN-BUG-BOUNTY-768x402.png) ](https://0xprial.com/how-to-get-into-bug-bounties-part-01/)

Bug Bounty

###  [ How to Get Into Bug Bounties – Part 01 ](https://0xprial.com/how-to-get-into-bug-bounties-part-01/)

[ ![](https://0xprial.com/wp-content/uploads/2020/03/XSS-WAF-Character-limitation-bypass-like-a-boss-768x448.png) ](https://0xprial.com/xss-waf-character-limitation-bypass-like-a-boss/)

Bug Bounty

###  [ XSS WAF & Character limitation bypass like a boss ](https://0xprial.com/xss-waf-character-limitation-bypass-like-a-boss/)

[ ![](https://0xprial.com/wp-content/uploads/2019/01/Unicode-vs-WAF-—-XSS-WAF-Bypass-768x448.png) ](https://0xprial.com/unicode-vs-waf-xss-waf-bypass/)

Bug Bounty

###  [ Unicode vs WAF — XSS WAF Bypass ](https://0xprial.com/unicode-vs-waf-xss-waf-bypass/)

[ ![](https://0xprial.com/wp-content/uploads/2018/11/XSS-bypass-using-META-tag-in-realestate.postnl.nl_-768x448.png) ](https://0xprial.com/xss-bypass-using-meta-tag-in-realestate-postnl-nl/)

Bug Bounty

###  [ XSS bypass using META tag in realestate.postnl.nl ](https://0xprial.com/xss-bypass-using-meta-tag-in-realestate-postnl-nl/)

[ ![](https://0xprial.com/wp-content/uploads/2022/01/prial-islam65.png) ](https://0xprial.com/home)

Sometimes, Hacking Is Just Someone Spending More Time On Something Than Anyone Else Might Reasonably Expect 

[ Facebook ](https://www.facebook.com/0xPrial/) [ Icon-x-twitter __](https://twitter.com/0xprial) [ Linkedin ](https://www.linkedin.com/in/0xprial/) [ Youtube ](https://www.youtube.com/0xprial) [ Github ](https://github.com/0xPrial/)

# Useful Link 

  * [ Contact ](https://0xprial.com/contact)
  * [ Privacy Policy ](https://0xprial.com/privacy-policy)
  * [ Terms & Condition ](https://0xprial.com/terms-condition)
  * [ Site Map ](https://0xprial.com/site-map)

# Newsletter

Name

Email

SUBSCRIBE

__

© All Rights Reserved By [Prial Islam](https://www.linkedin.com/in/0xprial/)

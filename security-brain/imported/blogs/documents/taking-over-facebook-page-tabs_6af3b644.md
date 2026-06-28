---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-14_taking-over-facebook-page-tabs.md
original_filename: 2019-11-14_taking-over-facebook-page-tabs.md
title: Taking over Facebook Page Tabs
category: documents
detected_topics:
- xss
- command-injection
- otp
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- otp
- api-security
- supply-chain
language: en
raw_sha256: 6af3b644aa6549d2e1a2b245487dfc0b152fd262ccfd01167b6c90fae60d115f
text_sha256: 43c5e909d636692f465231be74e30dd634059e174870d2f5350a09ce1db00ba8
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Taking over Facebook Page Tabs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-14_taking-over-facebook-page-tabs.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6af3b644aa6549d2e1a2b245487dfc0b152fd262ccfd01167b6c90fae60d115f`
- Text SHA256: `43c5e909d636692f465231be74e30dd634059e174870d2f5350a09ce1db00ba8`


## Content

---
title: "Taking over Facebook Page Tabs"
url: "https://blog.sagarvd.me/2019/11/taking-over-facebook-page-tabs.html"
final_url: "https://blog.sagarvd.me/2019/11/taking-over-facebook-page-tabs.html"
authors: ["Taking over Facebook Page Tabs"]
programs: ["Meta / Facebook"]
bugs: ["Broken link hijacking"]
publication_date: "2019-11-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4944
---

###  Taking over Facebook Page Tabs 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ November 14, 2019  ](https://blog.sagarvd.me/2019/11/taking-over-facebook-page-tabs.html "permanent link")

In this post, I'm describing how I was able to take over 4 tabs on Facebook's own Pages.  
  

### 1\. Facebook India Ambassadors

  
I was browsing Facebook as usual and not in a mood to test anything. I then visited Facebook India's page to check is there any update from Facebook India and that's when I noticed a page tab **Facebook India Ambassadors**. I clicked on it to see Facebook India's Brand Ambassadors and the tab showed a heroku error page. I was surprised to see that there.It looked interesting to me so I decided to dig further. I found out that it loads a third party website in an iframe in main section.  
  
The url was  _http://immense-atoll-4159.herokuapp.com/_ and I visited the url directly to verify that the subdomain doesn't exist. Heroku shows a does not exist error page if the subdomain doesn't exist.  

  
  
  
  
  
So I logged into my Heroku account and created a new project and give _immense-atoll-4159_ as project id. Then I created a simple NodeJS Script for PoC and deployed it to the Heroku App.  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuBDxOo7Asg70BTWFSEE8UOTPrdi8ZCnTlx1Sht33zAoMAcnEv2bAoMo-ya6jYCw3JK-pXFQukEx0nyCoj4IIwhNXOSGEaN6ETUgycsHCMK-kQvHaVBFsoSNE09R18H0rKJESQPQbFnzg/s1600/poc.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuBDxOo7Asg70BTWFSEE8UOTPrdi8ZCnTlx1Sht33zAoMAcnEv2bAoMo-ya6jYCw3JK-pXFQukEx0nyCoj4IIwhNXOSGEaN6ETUgycsHCMK-kQvHaVBFsoSNE09R18H0rKJESQPQbFnzg/s1600/poc.png)  
I then visited ambassadors tab in Facebook India's page and checked frame source to confirm my code is loading there.  

  

### 2\. Facebook India Livestream

**Livestream** is another tab in Facebook India page which frames an account from Livestream.com, owned by Vimeo. The framed url is  _livestream.com/facebookindia/index.php_ and I saw a page not found error in the tab.  
I visited livestream.com and created an account there with username _facebookindia_ but because of the _/index.php_ , I was unable to show contents there. But if someone visit livestream.com/facebookindia, they will see videos uploaded by me.  
  

  

### 3\. Facebook Portugal Livestream

  
  
  
  
Facebook Portugal page had a tab **F8 | Live** which frames the url _livestream.com/f82011/index.php_ but the username isn't exist in Livestream. I was able to take over that username in Livestream by Vimeo. Because of the _index.php_ in the url, I was unable to serve contents in Facebook Portugal Page.  
  

  

### 4\. Facebook Brasil Recursos

Facebook Brasil had a tab named **Recursos** which frames the url  _https://www.webuzzapps.com/webuzzapp/137331002992480/tab_ and it shows an error. When I digged it's dns, nothing returned. Then I visited GoDaddy to check whether the domain  _webuzzapps.com_ is available for sale or not and I saw that the domain is for sale. It's a premium domain so it's costly but whomever purchases it can serve contents in a tab on Facebook Brasil's Page.

  
  
  
  

  

### Additional Services

1\. Facebook India had a tab **Stories** which frames the url  _facebook.involver.com_ and the subdomain doesn't exist. Involver is a part of Oracle now. Since I'm not familiar with oracle services, I am not sure whether it is possible to take this over or not.

2\. Facebook India had a tab **State Election Tracker** which frames the url  _d6uon097akywu.cloudfront.net_ which doesn't exist.

3\. Facebook India had a tab **#100 Women** which frames the url  _100womenindia.votenow.tv_ and the dig result is 

  

100womenindia.votenow.tv. 59 IN CNAME wildcard.votenow.tv.edgekey.net.  
wildcard.votenow.tv.edgekey.net. 21599 IN CNAME e5223.g.akamaiedge.net.

e5223.g.akamaiedge.net. 19 IN A 23.32.136.41

  

It points to akamai but didn't claimed there.

  
  
  
  

  

### Response

Facebook triaged these reports, removed those tabs and closed this as informative, saying there's no potential impact.

  

I told them open redirect is possible and also the attacker can serve JavaScript in iFrame's context (CSP isn't applicable in JavaScript code within iFrame) and can create fake phishing pages and other forms to convince visitors to enter data.

  

Facebook responded that "that is an inherent risk of all page tabs: you can redirect people from Facebook to a third-party site."

[Bug Bounty](https://blog.sagarvd.me/search/label/Bug%20Bounty) [Facebook](https://blog.sagarvd.me/search/label/Facebook) [hacking](https://blog.sagarvd.me/search/label/hacking) [property takeover](https://blog.sagarvd.me/search/label/property%20takeover)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8968959338756795373?po=1686188424942811872&hl=en&saa=85391&origin=https://blog.sagarvd.me&skin=contempo)

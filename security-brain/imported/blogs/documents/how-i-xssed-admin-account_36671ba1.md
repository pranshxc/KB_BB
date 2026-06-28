---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-13_how-i-xssed-admin-account.md
original_filename: 2019-08-13_how-i-xssed-admin-account.md
title: How I XSSed Admin Account
category: documents
detected_topics:
- xss
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: 36671ba1f55d784887fcf1ec4bee781540d62df9c387860dcff35a1737dce176
text_sha256: 350ae93fd4947bcb94c89211b7ba20d01fdeeab804851b935bf5adbaf9963172
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I XSSed Admin Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-13_how-i-xssed-admin-account.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `36671ba1f55d784887fcf1ec4bee781540d62df9c387860dcff35a1737dce176`
- Text SHA256: `350ae93fd4947bcb94c89211b7ba20d01fdeeab804851b935bf5adbaf9963172`


## Content

---
title: "How I XSSed Admin Account"
page_title: "How I XSSed Admin Account | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/how-i-xssed-admin-account/"
final_url: "https://gauravnarwani.com/how-i-xssed-admin-account/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["Stored XSS", "Account takeover"]
publication_date: "2019-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5084
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/08/xss_acct_takeover.jpg?fit=800%2C600&ssl=1) ](https://gauravnarwani.com/how-i-xssed-admin-account/)

# How I XSSed Admin Account

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [August 13, 2019](https://gauravnarwani.com/how-i-xssed-admin-account/)

Hello Guys, recently I encountered with some Stored XSS on a web application which helped me takeover any account on the application. A bunch of CVE’s were assigned for the Stored XSS which you can find in my [Publications](https://gauravnarwani.com/publications/) page. Although some of the Stored XSS was easy to find, the impact which it had on the application was near critical and hence I’ll pick one of the cases in this post to explain the Impact. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog. To know about Cross-Site Scripting read my previous blog [here](https://gauravnarwani.com/a-tale-of-3-xss/).

### Case Study: Stored XSS to Account Takeover

The application EspoCRM 5.6.8 under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data-Tier (Databases). The application is a CRM application used for scheduling meetings, phone calls and sending Emails. The application used tokens to authenticate users when the user logged in the application. Using tokens added a layer of protection from CSRF and hence prevented requests to be sent on behalf of the user.

The token was generated as follows:  
The username and some random string were encoded into base64 as-

**admin:d4sb6bdfhfyr7hasdr434df** was encoded as **YWRtaW46ZDRzYjZiZGZoZnlyN2hhc2RyNDM0ZGY=**

This token was added to every request and removing the token would send the request as unauthorized.

On checking the request to the site:

GET /EspoCRM-5.6.8/ HTTP 1.1  
Host: localhost  
Authorization: Basic YWRtaW46ZDRzYjZiZGZoZnlyN2hhc2RyNDM0ZGY=  
Espo-Authorization: YWRtaW46ZDRzYjZiZGZoZnlyN2hhc2RyNDM0ZGY=  
Cookie: auth-username=admin; auth-token= d4sb6bdfhfyr7hasdr434df

We can see that the two major elements to form the Auth token were inside the cookie of the request. The Authorization token was constructed as follows:

**Base64 encoding of (auth-username:authtoken)**

Now, all we needed was to get a Reflected or Stored XSS on the application to take over any user as the cookies which form the token are not set as HttpOnly and can be captured by an attacker if he finds a way to deliver the malicious JavaScript.

The application had a preference tab where the user could set his email signature which is added to every email. The Email signature had various markdown methods. One of the features in the markdown which got my attention was the Code View feature on which you could try inserting HTML code inside the signature for better looks.

**The first attempt:**

<svg/onload=alert(1)> was inserted in the code view field. On clicking the close code view feature, the alert box popped. This worked at that moment but on clicking on save, the event handlers were stripped in the application

**Payload:** <svg/onload=alert(1)>

**Final response:** <svg/[data-handler-stripped]=alert(1)>

**Attempt 2:**

XSS via Html Injection and Iframe. <a> tags and <iframe> tags were accepted by the application. Using the payload <a href=javascript:alert(1)>test</a> or the same with Iframe, the tags were inserted into the application but stripped the href or src values.

**Payload:** <a href=javascript:alert(1)>test</a>

**Response:** <a>test</a>

**Payload:** <iframe src=javscript:alert(1)></iframe>

**Response:** <iframe></iframe>

After this all payloads from [Payloads all the things](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection) were tried, but there was no luck. While scrolling through the section about XSS in the same GitHub page, I stumbled across this polyglot XSS payload from [Somdev Sangwan](https://twitter.com/s0md3v/status/966175714302144514).

**– >'”/></sCript><svG x=”>” onload=(co\u006efirm)“>**

As this payload was inserted, it was seen that the XSS was permanently stored on the Preference page.  
The code was then modified as such to steal cookies of the user.

**– > “/><svg x=”>” onload=”(co\u006efirm)(document.cookie)”></svg>**

The payload was very impactful to generate the stored XSS inside the Email as it would fire when the victim would reply or forward the Email having XSS inside the Email Signature.

Now all the attacker needed to do was send an Email to the admin of the application who when replied to the mail executed the malicious JavaScript. The attacker would now steal the cookies of admin and construct the Authorization token of the admin and hence completely take over his account.

The report was submitted to EspoCRM appropriate measures. The bug has now been fixed and a CVE ID of [CVE-2019-14546](https://gauravnarwani.com/publications/CVE-2019-14546/) is generated for this bug.

That’s all for this Blog. Hope you liked it.

**#BugBountyTip:**

**Xss using css:**

<style>img{background-image:url(‘javascript:alert(1)’)}</style>

**Firewall bypass:**

<style>*{background-image:url(‘\6A\61\76\61\73\63\72\69\70\74\3A\61\6C\65\72\74\28\6C\6F\63\61\74\69\6F\6E\29’)}</style>

That’s all for today. Please subscribe to my [blog](https://gauravnarwani.com/blog/). Connect with me on [LinkedIn](https://linkedin.com/in/gauravnarwani97/).

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/how-i-xssed-admin-account/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/how-i-xssed-admin-account/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/how-i-xssed-admin-account/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/how-i-xssed-admin-account/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/how-i-xssed-admin-account/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/how-i-xssed-admin-account/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

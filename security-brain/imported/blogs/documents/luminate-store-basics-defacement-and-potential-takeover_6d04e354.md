---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-30_luminate-store-basics-defacement-and-potential-takeover.md
original_filename: 2017-08-30_luminate-store-basics-defacement-and-potential-takeover.md
title: Luminate Store Basics defacement and potential takeover
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 6d04e3545b55e3b1cafd799194d3c41bfaa1d40a855463825a529c7f09231dfb
text_sha256: 3240ddfaadf9c7feeb89056197c61dbbd6f27bd37ec1687bf05e2a7f3b4b330c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Luminate Store Basics defacement and potential takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-30_luminate-store-basics-defacement-and-potential-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `6d04e3545b55e3b1cafd799194d3c41bfaa1d40a855463825a529c7f09231dfb`
- Text SHA256: `3240ddfaadf9c7feeb89056197c61dbbd6f27bd37ec1687bf05e2a7f3b4b330c`


## Content

---
title: "Luminate Store Basics defacement and potential takeover"
url: "https://medium.com/@rojanrijal/luminate-store-basics-defacement-and-potential-takeover-3b53d1e45b4f"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["CSRF", "Session management issue"]
publication_date: "2017-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6116
scraped_via: "browseros"
---

# Luminate Store Basics defacement and potential takeover

Luminate Store Basics defacement and potential takeover
Rojan Rijal
Follow
3 min read
·
Aug 31, 2017

4

This vulnerability was found when testing the Stores Basic service of Luminate. In this service, we can create a store from where we can sell our products. Luminate service provides a whole CMS for this activity. Here is the snapshot of the backend of the CMS:

Store Basics’ Dashboard

I first ran some CSRF test in the Settings section of this app. In the settings, user can add business information that will be used by Luminate to contact the admin. Along with that, they can also upload Logo and add title for the website. My initial test gave me a successful CSRF attack. I will explain each step below because the generation of attack was complex at first.

Update: this blog covers two main bugs together: 1) CSRF In Luminate allowing to update business information 2) Session issue in Luminate allowing you to modify another user’s data remotely. One has higher impact than the other.

When a business information is modified, a POST request is made to:

https://www.luminate.com/ordermgr/_module?ysbparams={ysb_param}&modulename=ysb-mui-apps&action=save_site_settings

In the POST request JSON request like this is passed:

{"bizprofile":{"info":{"name":{"titlepage":"sec"},"category":"","tagline":{"text":""},"description":"Stay tuned! We're updating this section to bring you everything you want to know about our business. We can't wait to tell you more!"},"media":{"logo":{"desktop":{"image":"logourl"},"mobile":{"image":""}}},"contact":{"phone":"","email":"adminemail","location":{"street":"","city":"","state":"","country":"United States","zip":""}},"accountcontact":{"firstname":"first_name","lastname":"last_name","phone":"phone_number","email":"email_id","address":{"street":"street_address","city":"admin_city","state":"state","country":"United States","zip":"zip_code"}}},"siteObj":{"favicon":"site_favicon","robots":""}}

ysbparams parameter in the url specifically stood out during the testing because it had ==in the end. We went with the idea that this could be a base64 and it was indeed a base64. Once decoded, we got something like this: (this is edited to hide information)

{"appid":"settings","bizid":"ys-123456789-9","bizurl":"http://storeurl.com","lang":"en-us"}

Once that was decoded, I had to identify ways to get the bizid parameter. I noticed that this could easily be grabbed from the source code of the store url. So I could change that and encode the JSON then edit the url with new ysbparam. Initially, when testing this CSRF it did not work, because the server only accepted Content-Type: application/json. So in the end, I used AJAX to send a request with the type set as application/json.

Get Rojan Rijal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I had the CSRF, I decided to dig deeper and noticed that in the POST request there was a certain cookie called ysbauth. This cookie was also base64 encoded. Following is an example of base64 encoded ysbauth.

eyJiaXppZCI6InlzLTEyMzQ1Njc4OS05IiwieXNicGFyYW1zIjoieXNiX3BhcmFtX2Jhc2U2NCwieWlkIjoiZW1haWwiLCJhcHBpZCI6InNldHRpbmdzIiwiYml6dXJsIjoiaHR0cCUzQSUyRiUyRnN0b3JldXJsLmNvbSIsImxhbmciOiJlbi11cyIsInRpbWVzdGFtcCI6IjE1MDI0ODg0NjcuMTk0Iiwic2lnbmF0dXJlIjoiMTkyOThjMTVhNzg0***REDACTED-SUSPECT-TOKEN***When we deocde the base64, we get the following JSON:

{"bizid":"ys-123456789-9","ysbparams":"ysb_param_base64,"yid":"email","appid":"settings","bizurl":"http%3A%2F%2Fstoreurl.com","lang":"en-us","timestamp":"1502488467.194","signature":"19298c15a7847f6867ce5cea16d2ebdc9fa3739e"}

During testing, I found that if I only change the bizid in the ysbauth to one of our victims, I could successfully modify the file. For this attack, first I change the YSBParam by changing bizid and biz_url (like we did for the CSRF) and change the ysbauth with victim’s bizid. Once that is done you could modify the business information of your victim.

After 1 hr of complete testing, I found that all the modules in Store Basics were vulnerable. We could add our own Google Analytics code to the website which would allow monitoring of the website, we could also view coupons of other sites, add products and conduct many other attacks. This concluded that when ysbauth was manipulated, it basically gave access to another user’s session allowing us to modify their store basics profile.

Special thanks to the Yahoo security team for being extremely responsive and fast in the fix. I recommend all hackers to try Yahoo!’S bug bounty.

Cheers!

uranium238 / Rojan Rijal

Originally published at medium.com on August 30, 2017 from my alternate account.

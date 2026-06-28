---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-06_clickjackings-in-google-worth-126447.md
original_filename: 2018-03-06_clickjackings-in-google-worth-126447.md
title: Clickjackings in Google worth 12644.7$
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- sqli
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- sqli
- otp
- automation-abuse
language: en
raw_sha256: 043d41ffc5bf2579de254d4ddee9b514e0e6253a9191864ee1c22e4af012b568
text_sha256: 1c84557b9f15c0a341e5d9af948d3e1214aeb09d513ffde741361c58e9d656c3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjackings in Google worth 12644.7$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-06_clickjackings-in-google-worth-126447.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, sqli, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `043d41ffc5bf2579de254d4ddee9b514e0e6253a9191864ee1c22e4af012b568`
- Text SHA256: `1c84557b9f15c0a341e5d9af948d3e1214aeb09d513ffde741361c58e9d656c3`


## Content

---
title: "Clickjackings in Google worth 12644.7$"
url: "https://medium.com/@raushanraj_65039/google-clickjacking-6a04132b918a"
authors: ["Raushan Raj (@raushan_rajj)"]
programs: ["Google"]
bugs: ["Clickjacking"]
bounty: "12,644.7"
publication_date: "2018-03-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5955
scraped_via: "browseros"
---

# Clickjackings in Google worth 12644.7$

Top highlight

Raushan Raj
 highlighted

Clickjackings in Google worth 14981.7$
Raushan Raj
Follow
4 min read
·
Mar 6, 2018

960

6

Instead of going for Cross Site Scripting, Remote Code Execution, SQL Injection, etc. I decided to find clickjacking in google and facebook. Clickjacking is one of the lowest paid, mostly out of the scope and underestimated vulnerability by organisations.

What is Clickjacking ?

Unknowingly performing some sensitive actions on a webpage embedded(mostly in iframes) in any webpage with different or same domain/subdomain.

A. Clickjacking in Google’s play store payment page. 5000$

Steps to reproduce:
1. Attack url is is https://play.google.com/store/epurchase?dp=null&hl=en&docId=subs:com.google.android.apps.docs:r1.100gb&usegapi=1&id=I2_1505755312332&parent=https://www.google.com

2. When we add this url to <iframe src >there is an csp error :

“Refused to display ‘https://play.google.com/store/epurchase?dp=null&hl=en&docId=subs:com.google….docs:r1.100gb&usegapi=1&id=I2_1505755312332&parent=https://www.google.com' in a frame because an ancestor violates the following Content Security Policy directive: “frame-ancestors ‘self’ https://*.google.com https://*.googleusercontent.com https://editionsatplay.withgoogle.comhttps://livecase.withgoogle.com"."

3. But “*.google.com” is allowed.

4. Go to play.google.com and add some amount > 200 INR using google play recharge code.

5. Go to sites.google.com and create new site, there is an iframe option to insert. add URL given in step 1 to iframe src.

6. For POC i have included it in (https://sites.google.com/site/conceptofmathematicsnow/). The page get embedded . Just by one click on subscribe ,amount (130 rs ) will get deducted and you will get subscribed to 100gb drive unknowingly.

Attack scenario:
Clickjacking on page lead to deduct amount from google play wallet and subscribe user to google drive upgrade

1.) Attacker will embed

“https://play.google.com/store/epurchase?dp=null&hl=en&docId=subs:com.google.android.apps.docs:r1.100gb&usegapi=1&id=I2_1505755312332&parent=https://www.google.com" in any sites.google.com

site like “https://sites.google.com/site/conceptofmathematicsnow/" (here we can add javascript plugins)

2.) When user visit https://sites.google.com/site/conceptofmathematicsnow/ , and unknowingly click just one button (subscribe).Money will get deducted and he will be subscribed.

Press enter or click to view image in full size
B. Clickjacking in https://payments.google.com/ using google’s open redirection vulnerability. 3133.7 $

Steps to reproduce:
1. <iframe height=”1200px” width=”1200px” src=”https://www.google.com/url?sa=D&q=https://payments.google.com/payments&usg=AFQjCNGnO25JhaC9l_zIK-Is46SusuQRsQ"></iframe>

2. The url in iframe src , will make “https://www.google.com/url" as a referer to payments.google.com page.
3. Once there is valid referer , the X-Frame-Options Header Vanishes

Browser/OS:
Chrome / Firefox

Attack scenario:
It’s making whole payments.google.com pages/tabs clickjackable.
With few user interactions
1.) Attacker can close victim’s payment account
2.) Can add his account to manage victim’s account.
3.) Can Change payment profile details

C. Clickjacking in https://docs.google.com/picker . 1337$

Steps to reproduce:
1. Go to youtube there is upload button and “Import your videos from Google Photos” , On clicking this video picker will open and url for the same is :

https://docs.google.com/picker?protocol=gadgets&origin=https%3A%2F%2Fwww.youtube.com&hostId=yt-upload-importer&hl=en_GB&title&actions=picked%2Ccancel%2Cloaded%2Creceived%2CviewContentRendered&mineOnly=true&multiselectEnabled=true&shadeDialog=true&horizNav=true&maxItems=300&relayUrl=https%3A%2F%2Fwww.youtube.com%2F%2Fs.ytimg.com%2Fyts%2Ffavicon-vflz7uhzw.ico&pp=%5B%5B%22album%22%2C%7B%7D%5D%5D&nav=((%22photos%22%2C%22All%20Videos%22%2C%7B%22type%22%3A%22videos-uploaded%22%2C%22svm%22%3Atrue%2C%22rdv%22%3Atrue%7D)%2C(%22photos%22%2C%22Auto%20Backup%22%2C%7B%22type%22%3A%22videos-camerasync%22%2C%22svm%22%3Atrue%7D)%2C(%22photos%22%2C%22Albums%22%2C%7B%22selectAlbum%22%3Atrue%7D))&rpctoken=tppfn9l0d0ug&rpcService=40cmfpboj50i

2.
A.) There is a request parameter origin=https://www.youtube.com and response header x-frame-options:ALLOW-FROM https://www.youtube.com
B.) When we set origin=https://anything.com , there will be error page and x-frame-options: https://anything.com
C.) When we set origin=https://sites.google.com , there will be error page and x-frame-options: https://sites.google.com
D.)When we set origin=https://beta.sites.google.com , PICKER appears and NO error page and x-frame-options: https://beta.sites.google.com in response header
same is the case for https://googledrive.com

Get Raushan Raj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This means we can embed the video picker on https://beta.sites.google.com.

E.) https://beta.sites.google.com/site/conceptofmathematicsnow/ : here i have uploaded the same in iframe.

https://beta.sites.google.com/site/conceptofmathematicsnow/

Browser/OS: Firefox, Chrome

Attack scenario:
Clickjacking the button can convert user’s private/public videos to public on youtube

Press enter or click to view image in full size
D. Clickjacking in Google Sites(New) Setting Page. 1337$

Clickjacking Lead to deleting the google sites (trashed)
Steps to reproduce:
1. As X-FRAME OPTIONS https://sites.google.com/new?usp=jotspot_si is Same-Origin , So the page can be embedded in my https://sites.google.com/site/conceptofmathematicsnow/

2. Page is embedded to https://sites.google.com/site/conceptofmathematicsnow/

Browser/OS: Firefox/Chrome

Attack scenario:
1.) Page contains some sensitive actions like : DELETING THE PAGE, RENAMING THE PAGE.

E. Clickjacking in Google’ site error page. 1337$

Steps to reproduce:
1. Create a Google site (new).Embed iframe with src=”https://sites.google.com/site/sites/_/.%2F..%2f/..%2F/etc/passwd"

2. Open a new browser, log in to Gmail and sites.google.com.

3. In another tab open the site created in 1.(https://sites.google.com/view/raushannewtest). As the user is login. There is an option to change public profile pic (from albums, private photos inside google drive.Also user can upload from the system and set it as a profile pic)inside the iframe.

Browser/OS: chrome , firefox

Attack scenario:
Attacker can embed payload in google site. Just by few clicks , victim who is logged in to sites.google.com/gmail can unknowingly
1.) make his/her private pics public.
2.) Upload unwanted files in google drive
3.) Unknowingly subscribe to site changes subscription.
Embedding this page is like embedding the google drive picker.

F. Embedding unlisted youtube videos. 500$

Steps to reproduce:
1. Go to your video → advance settings — -> Distribution Options → embedding and uncheck it , so it means we can’t embed the video in any iframe
2. It can be embedded into any webpage <iframe src=”https://www.youtube.com/embed/pbsQVpEROw4"></iframe>

Browser/OS:

Chrome / Linux

Attack scenario:
User instead of disallowing the video , can be embedded.

It was able to embed whole Youtube, Google Books. I have reported but both of them went duplicate. If any one want’s poc for duplicate one please ping me.

Next i started learning about CORS Vulnerability and was able to find cors issue in Google. Will disclose “CORS in google” reports soon.

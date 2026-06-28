---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-08_reflected-xss-in-facebooks-mirror-websites.md
original_filename: 2020-08-08_reflected-xss-in-facebooks-mirror-websites.md
title: Reflected XSS in Facebook’s mirror websites
category: documents
detected_topics:
- xss
- automation-abuse
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- automation-abuse
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 9db7e89a7b0be43b9ae5abf8742e738b66a0d047085e0d5389e2ae361ac3d782
text_sha256: 60864e1ce748298182f81ed05a6735193c0cf036da6e96abb3bf62f75394e8a7
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Facebook’s mirror websites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-08_reflected-xss-in-facebooks-mirror-websites.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9db7e89a7b0be43b9ae5abf8742e738b66a0d047085e0d5389e2ae361ac3d782`
- Text SHA256: `60864e1ce748298182f81ed05a6735193c0cf036da6e96abb3bf62f75394e8a7`


## Content

---
title: "Reflected XSS in Facebook’s mirror websites"
url: "https://medium.com/bugbountywriteup/reflected-xss-in-facebooks-mirror-websites-4384b4eb3e11"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Meta / Facebook"]
bugs: ["Reflected XSS"]
bounty: "500"
publication_date: "2020-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4342
scraped_via: "browseros"
---

# Reflected XSS in Facebook’s mirror websites

Reflected XSS in Facebook’s mirror websites
Sudhanshu Rajbhar
Follow
6 min read
·
Aug 8, 2020

826

5

Heyyy Everyoneee,

I hope everyone is doing good , it’s been a while since I haven’t shared any writeup of my finding’s.

This blog post is going to be about a reflected xss bug affecting Facebook mirror websites. I will be explaining the whole process how I found the vulnerable endpoint.

Well many people ask me how do I look for xss bugs so in this same blog I will also share my method of finding xss.

And here we go…..

I was collecting subdomains of thefacebook.com domain, as I have seen many writeups regarding bugs found in thefacebook.com subdomain only. I wanted to find something there too :)

Started with collecting the subdomains. I basically use tools like Findomain, Subfinder,Assetfinder ,etc to find subdomains of my target. After I collected the subdomains I used another tool called httprobe

After the subdomain enumeration part is completed. I have a habit of doing directory bruteforcing(using ffuf) on all the collected hosts from httprobe, then going through them to see if I can find some easy wins. Look at the below code that’s how I do it

python3 dir.py httprobe.txt

While I was looking at the https://mirror-ext.glbx.thefacebook.com ffuf result:

Press enter or click to view image in full size
Press enter or click to view image in full size

Only one directory was there,I decided to look what might be there. http://mirror-ext.glbx.thefacebook.com/help/

It was normal help page with the support email address, didn’t seem interesting to me at first but looking at the page source I could see something ineteresting.

Press enter or click to view image in full size

Look at the second line, I tried accessing that endpoint http://mirror-ext.glbx.thefacebook.com/.layout/mirror.php and it was just a blank page :(

Press enter or click to view image in full size

This time there was nothing in the page source code too that I can look further into, then I decided to find more php endpoints under the /.layout directory.

Press enter or click to view image in full size

These were the files which I was able to find using different wordlists. They were all same as the earlier one mirror.php blank page, only one was different header.php

Press enter or click to view image in full size
http://mirror-ext.glbx.thefacebook.com/.layout/header.php

Looking at the page source code I found that the endpoint was getting reflected inside anchor tag href value, it might be vulnerable to xss so I started testing for it.

Press enter or click to view image in full size

Adding characters like “>< at the end of the url gave not found page.

Press enter or click to view image in full size

I didn’t wanted to give up so easily as I can smell xss there. I started bruteforcing for parameters but didn’t find any.

Upon adding a slash and then another directory name didn’t gave me the not found error like last time.I tried this because of @brutelogic blog which I read in the past

Looking for XSS in PHP Source Code - Brute XSS
If we have the source code of a server side script, which is the case of open source software, we can find XSS…

brutelogic.com.br

Press enter or click to view image in full size
http://mirror-ext.glbx.thefacebook.com/.layout/header.php/shirley
Press enter or click to view image in full size

Trying again with “>< and I found that they are getting url encoded.

Later I realised that the href value is inside single quotes. So trying with single quote this time.

I tried this at first when I saw that my input was getting reflected inside href, href=’/javascript:alert()’, but this wasn’t working because there is a slash before our input. I started looking on google for a way to include two href in a single anchor tag , found a solution on https://stackoverflow.com/questions/13965753/how-can-i-open-multiple-links-using-a-single-anchor-tag

Based upon the solution , the final payload was:

Press enter or click to view image in full size
Press enter or click to view image in full size

I was like holy sh*t!! I just found a xss on a Facebook domain.

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Well I knew about some more Facebook mirror domains so tried to see if I can replicate the same xss on there also. Result was:

Press enter or click to view image in full size
mirror.facebook.net

One more subdomain was vulnerable http://mirror.t.tfbnw.net/ but I don’t have any screenshot of it.

That’s the end of the story.

Regarding the fix, now the single quote(‘) is converted to &.

Press enter or click to view image in full size

I was rewarded with a $500 bounty for this xss.

Video POC:

Now moving on to the second part,

How do I look for xss bugs?

I am using this awesome burp plugin called reflector

elkokc/reflector
Burp Suite extension is able to find reflected XSS on page in real-time while browsing on web-site and include some…

github.com

It basically checks the parameter whose value is getting reflected in the source page and then tries to see which symbols are also getting reflected in the source page like “,>,<,{,},’,etc

You just need to browse the web application , visit every page there, fill all the input fields. Then look at the burp issue tab to see if it has find anything.

Press enter or click to view image in full size
https://github.com/elkokc/reflector/blob/master/screenshot/symbols_analyse.png
Talking about some automation work:

Use tools like paramspider , gau ,etc to collect endpoints which have parameter in them then you can use kxss, dalfox (choice is yours, use whatever tool which works for you, they both are very good.) on them to see if you can find some xss. Below you can see the dalfox tool in action

Press enter or click to view image in full size

https://twitter.com/0xAsm0d3us

devanshbatham/ParamSpider
Finds parameters from web archives of the entered domain. Finds parameters from subdomains as well. Gives support to…

github.com

https://twitter.com/hacker_

lc/gau
getallurls (gau) fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for…

github.com

https://twitter.com/TomNomNom

tomnomnom/hacks
A collection of hacks and one-off scripts. Contribute to tomnomnom/hacks development by creating an account on GitHub.

github.com

https://twitter.com/hahwul

hahwul/dalfox
Just, XSS Scanning and Parameter Analysis tool. I previously developed XSpear, a ruby-based XSS tool, and this time, a…

github.com

Beginner Guide

If you are a beginner and want to learn about xss, start by reading blogs there are many great people writing blogs about xss like @brutelogic (He is very kind and helpful. If you are having a hard time bypassing a xss waf or something , he is always ready to help you there. )

Brute XSS - Master the art of Cross Site Scripting.
Master the art of Cross Site Scripting.

Master the art of Cross Site Scripting.brutelogic.com.br

https://twitter.com/soaj1664ashar

Respect XSS
ReflectionHere and I found that potentially dangerous characters like ', and / etc were not encoded. In order to keep…

respectxss.blogspot.com

https://twitter.com/s0md3v

s0md3v/AwesomeXSS
This repository is a collection of Awesome XSS resources. Contributions are welcome and should be submitted via an…

github.com

There are many more just search them on google yourself.

Want to practise xss somewhere goto : Portswigger Web Security Academy

What is cross-site scripting (XSS) and how to prevent it? | Web Security Academy
In this section, we'll explain what cross-site scripting is, describe the different varieties of cross-site scripting…

portswigger.net

Do ctf challenges related to xss, watch poc videos/writeups they will give you an idea where you should look for xss, which fields are more prone to be vulnerable to xss eg. search fields, submit forms, etc .

That’s all, thankyou very much for reading it till the last. Hope you would have enjoyed it.

Sya everyonee

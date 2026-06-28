---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-21_reflected-xss-in-zomato.md
original_filename: 2019-01-21_reflected-xss-in-zomato.md
title: Reflected XSS in Zomato
category: documents
detected_topics:
- oauth
- xss
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- oauth
- xss
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: a23e3a08e933671ee52a61c470b9170b7845ae394164dddf18b8814fc6961120
text_sha256: 641e9d77839e6107f3d9334c0a4611250d07bc3a1b514f3f738d8c3396b24d64
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Zomato

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-21_reflected-xss-in-zomato.md
- Source Type: markdown
- Detected Topics: oauth, xss, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `a23e3a08e933671ee52a61c470b9170b7845ae394164dddf18b8814fc6961120`
- Text SHA256: `641e9d77839e6107f3d9334c0a4611250d07bc3a1b514f3f738d8c3396b24d64`


## Content

---
title: "Reflected XSS in Zomato"
url: "https://medium.com/@sudhanshur705/reflected-xss-in-zomato-f892d6887147"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Zomato"]
bugs: ["Reflected XSS"]
bounty: "250"
publication_date: "2019-01-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5468
scraped_via: "browseros"
---

# Reflected XSS in Zomato

Top highlight

Reflected XSS in Zomato
Sudhanshu Rajbhar
Follow
4 min read
·
Jan 21, 2019

676

6

Heyy Everyonee,

In this writeup I am going to tell you how I was able to get xss in Zomato.

I will tell the whole story how I found the vulnerable parameter.

Actually at that time I was reading a book “Mastering Modern Web Penetration Testing” (You can get it on Amazon) and from there I got know about a website named wolframalpha which we can use for subdomain enumeration.

I just thought of giving it a try , so I enetered zomato.com in the search bar and it gave me around 10 subdomains.It also shows “daily visitors” of a particular subdomain, thats a great options if you are looking for a less visited areas.So the last domain from the list caught my attention as the visitors were very less compared to others.

Source:https://www.wolframalpha.com/input/?i=zomato.com

I opened secretx.zomato.com, and all I can see is a button -“sign in with Zomato”.I checked the source code , nothing ineteresting.

I clicked on the button, it redirected me to zomato.com and a box was there saying “SecretX Client wants to access you Zomato Account. Accept or Recject” .

So I again went back to the website.From the source code I took out this url https://auth2.zomato.com/oauth2/auth?response_type=code&client_id=80b39918-90be-49d2-ac52-4a8b1a25bcf1&redirect_uri=https%3A%2F%2Fsecretx.zomato.com%2Fuser%2Foauth2%2Fredirect_uri&state=2BHoBnVFFKP29L6SerHgEb7OCnBDPO which was getting load when the button was clicked.

Here I added some junk values to the parameters to check for any oauth misconfiguration.And it gave me some error.

Press enter or click to view image in full size

The parameter value was getting refleted in the source code, So i checked whether <,> are getting filtered or not.The result was, Naaah.

Press enter or click to view image in full size

I tried for xss but I couldn’t get it ,as there was waf.I spent some time on it but no progress, I started looking for XSS reports,waf bypass blogs then I tried with xss payload list.

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Boom yeah with the help of it I got the xss popup.The payload which worked for me was

<marquee loop=1 width=0 onfinish=alert`1`>XSS</marquee>

But I couldn’t access the DOM because alert(),confirm(),prompt() were getting blocked by the waf. Somehow I wanted to make it work, I tried url encoding the payload and other things but nothing worked.It was aound 3 : 40 am so I needed to go to bed coz don’t want to get late for school.

After coming back I started looking for more articles,blogs.Then I got to remember about the xss cheatsheet which was by Somdev , here is the link https://github.com/s0md3v/AwesomeXSS

co\u006efirm()

By encoding the character in unicode I was able to access the DOM.

Press enter or click to view image in full size

I submitted this report to Zomato,and the report was triaged and after that I went to sleep the next day when I woke up I checked the notification and I saw the mail “Zomato has rewarded you 250$”.

In the report Prateek Tiwari mentioned that the problem was with Hydra which is an OAuth 2.0 and OpenID Connect Provider which Zomato are using for authentication on their services.

For showing their gratitude,Hydra mentioned my name in their newsletter which was really great for me.

Press enter or click to view image in full size

Here is the report : https://hackerone.com/reports/456333

POC Video:

A great thanks for reading the writeup. I hope you have enjoyed it.

📝 Read this story later in Journal.

🗞 Wake up every Sunday morning to the week’s most noteworthy Tech stories, opinions, and news waiting in your inbox: Get the noteworthy newsletter >

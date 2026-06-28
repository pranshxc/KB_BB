---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-31_hacking-makes-me-forget-my-pain.md
original_filename: 2020-03-31_hacking-makes-me-forget-my-pain.md
title: Hacking makes me forget my pain
category: documents
detected_topics:
- sqli
- sso
- xss
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- sqli
- sso
- xss
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 1322f7b2ce41fc2fe2592bf1f2311b83ca3d9c2856ddf9e6c32cc70f0cebe7b0
text_sha256: 28f280606a66cde56a3c8316e33cf1a3e1af908de7d7e08ca636960b6b99f4f8
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking makes me forget my pain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-31_hacking-makes-me-forget-my-pain.md
- Source Type: markdown
- Detected Topics: sqli, sso, xss, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1322f7b2ce41fc2fe2592bf1f2311b83ca3d9c2856ddf9e6c32cc70f0cebe7b0`
- Text SHA256: `28f280606a66cde56a3c8316e33cf1a3e1af908de7d7e08ca636960b6b99f4f8`


## Content

---
title: "Hacking makes me forget my pain"
url: "https://medium.com/@abidafahd/hacking-makes-me-forget-my-pain-b04bf51d0407"
authors: ["Abida Fahd"]
bugs: ["SQL injection"]
publication_date: "2020-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4679
scraped_via: "browseros"
---

# Hacking makes me forget my pain

Hacking makes me forget my pain
Eddie Mora
Follow
7 min read
·
Apr 1, 2020

26

1

Hello guys, this is me again and today I will share with you how I was able to forget my sickness just by doing bug hunting and how I was able to get some sweet bugs in a private target.

Press enter or click to view image in full size
Open your Eyes.

So as everyone knows due to the COVID-19 we are all quarantined, which may look annoying for most peoples, but what about us we Hackers?

Well talking from my own experience, I really enjoy it especially its something I do all the time by passing hours and hours in front of my computers hunting for bugs without moving…

Everything was good during the last days, tel the 31/02/2020, I felt cold and powerless its like there something wrong with my body, I don’t hide you that I was scared of being infected by the coronaVirus but thanks God I'm not infected it's just a psychic situation that can happen to all of us.

So to bypass this period and forget these bad feelings, I decided to do a thing that makes me happy, and I have one big thing that I love more than my cat.
It’s Haaaaacking!

So let's hack!

I have chosen a target that I had already pawned before in 2017, it was about an SQL injection and after my report, it got fixed and I didn’t try to check if I can reproduce it again.

So today after 2 years I decided to check if I can pwn this target again and this is the steps I have done :
1) Checking the old SQLI bug if still exist = “Unfortunately No, all the parameters are secure”.
2) looking for a login panel and check if I can bypass the authentification = “Unfortunately Nothing works”.
3) doing some recon and look for something new something I didn't try in 2017.

So after some researches, I found a place where visitors can sign-up

Press enter or click to view image in full size

I tried to create an account then sign-in with, but unfortunately, this can’t happen in our case cause it requires some kind of validation from the Administrator.

So the action can’t stop here of course, a question cames to my mind :
In case of having the verification, where is the login panel responsible to log me in?
The answer cames so fast just by using this simple dork on google search: “www.target.com login”

The inscription button will send you to the Sign-up form and this is a POC that its the login page I'm looking for.

The first thing to try in this kind of situation is to try random strings “Admin/Admin || Admin/Password || Admin/123456…”
But of course, nothing works XD.

So now its time to try SQLI:

I turned on my Burp and sent the request to the repeater, I tried to insert (‘) in the user input and I got this!

Press enter or click to view image in full size
LAAY LAAY LAAY LAAY LAAY

I was expecting an SQL error or at least something readable but wtf?
I decided to believe that there is a problem here “makayn ma walakin xD”
So at the moment where I have no SQL error that can help me to build a payload that will allow me to bypass this, I decided to use a payload that worked with me in more than 60% of my huntings :
This is the Payload: admin’ OR 1=1- -‘

Get Eddie Mora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And yes it worked again and my Intuition was true!

Press enter or click to view image in full size
We are inside!

Basically we are inside the control panel but we are just a simple user and from the first sigh I can tell that there is nothing exploitable here to get an RCE for example.
But before confirming that let's check all the features available!
The first option I have found is :

Press enter or click to view image in full size
I got this after clicking on “Mes demandes”

It looks like a basket of requests that users demand from the administrator in order to verify or something like that.
The more interesting thing is that we can add a new request and maybe there is an option to upload a PHP file on the server from there.

Press enter or click to view image in full size

I tried to make a new request adding some XSS payload but when I click the add button, I got a problem with the Session input because it's empty and there is no choice in the list to check so I decided to make a simple trick by filling it from the element inspector!

Press enter or click to view image in full size
I gave it the value 15

So now let's try the Add button again:

WTF!

This error appeared, and it says that we cant add more than 1 request during the same year, so we have 1 request per year!
This so disappointing and of course, I will not wait the whole year to pwn this stupid application so let’s bypass this shit.

Press enter or click to view image in full size
Here we goo!

Bypassing this error requires me to understand how this application work, so I gave my self some time to understand all the parameters, at the end I realized that this error is generated because we are trying to add a request with the parameter year == ‘2020’ whish already used by an old request already added before, so what if we add 2016 or 2021 or a date that never used?

And guess whuuut !

Press enter or click to view image in full size
Bypassed successfully

After bypassing these errors we got this a kind of file upload points, but with some restrictions that allow only (WORD, EXEL, PDF, JPG or PNG) format.

I started by uploading a simple JPG file to see if its gonna work and yes it worked, then I tried .PHP and of course I got this.

Not allowed format

So now its time to bypass this, there is a lot of ways to bypass it but it depends on how the application is built, in my case the developer used a white list of strings, that gonna search if exist in the name of our files when trying to upload and it's so easy to bypass, we can just name a file script.php.jpg then upload it and catch the request with a proxy, then rename it to script.php and boom!

Until this point, everything is good so let's open the PHP script we just uploaded.

Unfortunately, after going to www.target/uploads/script.php we got automatically redirected to the home page of the target, I tried many tricks but with no result to bypass this.

This is very sad…

So is this the end of our story?
If you said yes in this kind of moment, there is no way to call you're self a hacker any more.

So after a lot of tries to bypass the redirection, I failed!
I started thinking if there is another way that I can take…
suddenly I noticed that the URL of my current page is like this :
https://www.target/content/recapitulation.php?id=612

Press enter or click to view image in full size
Time to win.

A place to try SQL Injection of course, and after using the famous (‘) I got an SQL Error!

And this is the SQLMAP result after exploiting it!

Press enter or click to view image in full size

BTW, for people who ask about how to use automation tools to exploit SQLI even if our vulnerable target is inside a control panel which require an authentification, my answer is this command :

Sqlmap -u “https://target.com/vulnerable/sqli/?id=1" -- cookie “you're cookie session”--dbs

The lessons to learn from this write up
1) Always try to understand every parameter and every part of your target.
2) Play with the application and trie every kid of values and payloads and check the result.
3) Never lose hope, and do things you love to forget your pain.

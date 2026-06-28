---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-02_xss-will-never-die.md
original_filename: 2019-11-02_xss-will-never-die.md
title: XSS will never die
category: documents
detected_topics:
- xss
- idor
- command-injection
- file-upload
- race-condition
- clickjacking
tags:
- imported
- documents
- xss
- idor
- command-injection
- file-upload
- race-condition
- clickjacking
language: en
raw_sha256: 94063ecad733e4e3299d5c381d709247c441d3da8a54845158693ac281160f83
text_sha256: 515a3aea43dab97a7b40e4fbc540bb2c9f590bcc5ce193b8afb21748571f137b
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# XSS will never die

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-02_xss-will-never-die.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, file-upload, race-condition, clickjacking
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `94063ecad733e4e3299d5c381d709247c441d3da8a54845158693ac281160f83`
- Text SHA256: `515a3aea43dab97a7b40e4fbc540bb2c9f590bcc5ce193b8afb21748571f137b`


## Content

---
title: "XSS will never die"
url: "https://medium.com/@04sabsas/xss-will-never-die-eb3584081a5f"
authors: ["Oleksandr Opanasiuk (@Lekssik2)"]
bugs: ["XSS"]
publication_date: "2019-11-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4960
scraped_via: "browseros"
---

# XSS will never die

Top highlight

XSS will never die
Oleksandr Opanasiuk
Follow
8 min read
·
Nov 3, 2019

213

1

Hello all the Penetration Testing community, hope you are doing well.

Got some unusual XSS vulnerabilities for last months, but today I want to discuss the general idea of explanation, since the writeup for each of these vulnerabilities is small. So let’s go!👨‍💻

Disclaimer: there will not be complicated explanations and code analysis, this is a simple discussion of the strange concepts of protecting 5 applications and breaking it.

Okay, so we have one HUGE shop-company, that has a lot of sub-domains and different applications running on them:

Press enter or click to view image in full size

It will be 5 parts with short story about one XSS, protection and breaking in each one.

Part 1 — Stored XSS for mobile on the forum

Really love forums since there are a lot of potential vulnerabilities due to a huge list of functions. I went to the forum.example.com/post?id=123 and started testing of File Upload via URL functionality — here I noticed that it taking the name of file and inserting it twice on the page — in <img> tag and in the description of the file, it looks like:

Press enter or click to view image in full size

Me: what if insert “ to the name? Ok, lets test http://…/1.webp”

Site:

Press enter or click to view image in full size

Me: Ez, go onerror and report it!

Site: Ahahahahahah 👋

What happens? All the DOM-events are removing (<img/src=x/onerror=a> going to <img/src=x>🤯). But, but it turned out that not all. As the world is always improving, DOM-events appeared for mobile too — so they were not blacklisted and we got Stored-XSS for mobile devices. Finally it was like:

Also do not forget that you can use alert`1` instead of alert(1) (here service blocked all the parameters inside “()”)

Resume: no blacklists will help due to the improving of technology — everything cannot be prevented. But filter quotes — it’s quite possible to try.

Here we saw that a quote was inserted into html-code — and with the idea “I won’t believe that you will block all the possible DOM-events” we found that the mobile events were not blacklisted and got Stored XSS in forum post.

Part 2 — Reflected XSS on email preview

I got an email from our HUGE-shop, and they use the domain email.example.com to view emails, like email.example.com/view?id=123&key=abc&statname=DiscountEmail. The parameter “statname” was <input type=”hidden”> and did nit filter the “, but filtered <>. So, we just looked how to exploit XSS in hidden input and founded “accesskey=’X’ onclick=’alert(1)’”. It worked, and we got Reflected-XSS.

Resume: You will increase your chances of finding vulnerabilities if you subscribe to newsletters from the service that you are testing. Firstly, you will receive news about service updates, and will be able to test it faster than other hackers (I do remember how some guy tested YouTube Beta-studio as soon as it was presented and found great IDOR in 15k$). Secondly — it is quite possible that in the email you will find vulnerable links due to less attention to such minor functionality.

So after finding non-filtered quotes and quick-recon in Google “XSS hidden input”, we have found the way to exploit it with “accesskey”.

Part 3 — Stored XSS in live support chat

They had domain support.example.com, where we can find some information about using the service and chat online with manager in case of needing of the help. And you know what — I started chat with manager, and inserted <img src=”x” onerror=”alert(1)”> — it was injected into html-source! I was very surprised…🙈

Press enter or click to view image in full size

As I later understood, no one could get to test this thing — first you have to go to the site at a time when managers are online, and this time is limited to 6 hours a day. Secondly, you need to start a chat, and for this we need to wait for about half an hour to start a conversation with an online manager. That is, from the 3rd time I decided to test this functional, and from 5th time I got into the chat — I think this explains why no one found this thing before.

Resume: Any company has a lot of functionality, and sometimes some things remain outside the scope of developers. We all know that we need to test all the possible functionality, but, unfortunately, sometimes we miss vulnerabilities due to laziness or fatigue.

Here we found a service that was probably created a very long time ago, but was not updated from a security point of view, since no one checked it.

Part 4 — Reflected XSS in User Dashboard

This is the longest vulnerability, if we count from the time when I found the first clue about the presence of the vulnerability, and until the time when I finally exploited it (Before this it was Race Condition in purchasing functionality with about 1 month. Just so that you understand how this process happens with me — when I find some interesting things, I usually record bugs info, and later, when new ideas appear, I return to them and continue to exploit). Are you become to be interested in? 😊

Get Oleksandr Opanasiuk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So here we have User Dashboard, and functionality of filtering our activities — we can insert value “time_from” to filter it with the dates. It was not filtering quotes, so we quickly inserted quote and got:

Press enter or click to view image in full size

Ok, next step — does it filter “< >”. Yes, so I decided that we would exploit this via an input element with DOM-events. But after ‘time_from=”777" onfocus=”alert(1)”’ I got it:

Press enter or click to view image in full size

What just happened? Like in the Part1, it is filtering DOM-events and removing it. But, everything is much more complicated — they don’t have a blacklist, they just block all the parameters in the tag that starts from “on” 🤷‍♂️🙂️🤷‍♂️ Suddenly I was attracted by another coincidence on the page with the entered data and I saw such a strange field:

Press enter or click to view image in full size

It was something like break-links logger and… here “<>” were not filtered:

Press enter or click to view image in full size

I want to stop at this step so that you understand what is going on: we have a filtering function for our activities (user.example.com/activities?time_from=777&acc=submit, and the “time_from” parameter is vulnerable. But there is protection in the application: it removes events (the WAF finds everything inside the tag that starts on “on”). If this happens, the logger fires, captures the broken link, and inserts it in a strange way to page source without filtering “ and <> 👍

But you remember that all DOM-events are removing — I started looking for tags that you can insert and receive XSS, but it turned out that it cuts them out just like events. Another one “but”: I noticed a strange thing — if I wrote a tag, but didn’t close it — it didn’t delete it, that is, only the closed tag was cut out. So it turned into:

Press enter or click to view image in full size

YES!😱 So now we can insert link to execute script, but how to close script tag? If the src is given in script tag — all the source is ignoring inside the tag, so we just need any </script> later on the page. Finally source looks like:

Press enter or click to view image in full size

Let me please explain again what just happened: so we found the broken value “old_request”, that creating if we add something potential danger to url (DOM-event). And in this value we can insert ‘<>” into source, but still can not insert tags and DOM-events. But since the input tag was closing itself — we insert “<script/src=//url and WAF do not see it as dangerous input, so do not removing. Then we discard all the garbage that is passed later through ? (as parameters for the GET request). Now the JavaScript logic gave us an advantage — since the resource for the script is specified, everything inside the tag will be ignored, and the site will wait for the closing tag — which will meet somewhere further anywhere in the source, for example, calling jQuery. So the source logic:

Press enter or click to view image in full size

Resume: no blacklists will help due to the improving of technology — everything cannot be prevented. But filter quotes — it’s quite possible to try. [PART1]

So here we got unfiltered quot, then strange “logging functionality” with unfiltered <>, and even WAF with his blacklists is a little hard — we finally exploited it with understanding of the logic of HTML and JavaScript.

Part 5— Self XSS + Clickjacking = Nice XSS

The last one XSS — will be easy to understand. You sometimes meet Self-XSS, in the functionality of the editing users data, in the form of feedback, etc. But because of the fact that there is no definite request with the help of which XSS is injected — such vulnerabilities are considered as N/A due to the fact that user actions are required.

But, we do have some great thing as Clickjacking — terror of the past 10 years of the web (previously it was very widespread vulnerabilities, as now IDOR). I think you know what is it, but I hope to be useful and explain this to beginners. This vulnerability arises when the site allows to be inserted to <iframe> and thus we impose it invisibly and make some forms that interfere with the coordinates of how that functionality is located on the attacked site that we want to hack — and when user use attacker’s site and inserting data there — user inserting data to another site due to iframe. Here it is described in more human language: https://www.owasp.org/index.php/Clickjacking.

So on feedback.example.com/feedback we can left feedback, it forwards to another non-scope service, but inserts on the origin page “Thanks [username]”. And this [username] was not filtering any html-source, directly inserting everything to the page. Since we did not have direct request, we started to check the X-FRAME — to my luck, it turned out to be vulnerable to clickjacking, and I just created an html+css form, which showed how it works. Here you can find examples of great reports for Clickjacking: https://www.google.com/?q=site:hackerone.com%20intitle:clickjacking

Resume: Increase your knowledges, because this is what will always be with you, and will help everywhere.

Here, thanks to what we knew about the clickjacking , we exploited Self-XSS without any problems.

Thank you so much for reading this👍

Oleksandr Opanasiuk
The latest Tweets from Oleksandr Opanasiuk (@Lekssik2). Great manager and not bad pentester https://t.co/qJyb7tVAtx…

twitter.com

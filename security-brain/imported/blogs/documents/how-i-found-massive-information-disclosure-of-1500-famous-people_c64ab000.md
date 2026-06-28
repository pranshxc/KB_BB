---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-31_how-i-found-massive-information-disclosure-of-1500-famous-people.md
original_filename: 2017-07-31_how-i-found-massive-information-disclosure-of-1500-famous-people.md
title: How i found massive information disclosure of 1500 famous people
category: documents
detected_topics:
- api-security
- mobile-security
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- api-security
- mobile-security
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: c64ab000405c2e58d1d2f0f4a378dd820fcb318c7bf1600970b788196ab194bd
text_sha256: 20518c95e4fc4aa4668ede336e71bc871934537324b94f15138123b9ec995c37
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How i found massive information disclosure of 1500 famous people

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-31_how-i-found-massive-information-disclosure-of-1500-famous-people.md
- Source Type: markdown
- Detected Topics: api-security, mobile-security, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c64ab000405c2e58d1d2f0f4a378dd820fcb318c7bf1600970b788196ab194bd`
- Text SHA256: `20518c95e4fc4aa4668ede336e71bc871934537324b94f15138123b9ec995c37`


## Content

---
title: "How i found massive information disclosure of 1500 famous people"
url: "https://medium.com/@valeriyshevchenko/massive-information-disclosure-of-1500-famous-people-b1b950fa657"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["Information disclosure"]
publication_date: "2017-07-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6134
scraped_via: "browseros"
---

# How i found massive information disclosure of 1500 famous people

How i found massive information disclosure of 1500 famous people
Valeriy Shevchenko
Follow
7 min read
·
Aug 1, 2017

23

1

Before we jump into the details, Just to clarify a few things:

The reason why I’m writing this article today is to inform more QA Engineers that they should work more carefully and focusing on many things. Don't forget about information security aspects.

2. I Hack Ethically. No personal gains. Although, I believe hackers should be positively awarded for their contributions.

Not so long ago this interesting story happened with me. In spare time I watch english vlogs on youtube. In one of the vlogs I noticed a very interesting application. That was native app for the iOS device. The man quickly showed it. And he told how it makes life easier for him, allowing to order sponsorship items anywhere in the world. Honestly, I am a bit of a fan of this company. And I could not pass by this application.

First of all it is necessary to say that this application placed on a special web-page. In the form of special beta versions. The number of downloads was quite small. For the android devices, the number of downloads was near 1000–5000. But this is enough for the seriousness of the problem. In fact, there were a lot of problems, but first things first.

Press enter or click to view image in full size

First, I looked how the application communicates with the server side. And, most importantly, with which server it works.

Surprisingly, I did not found HTTPS protocol there. This was already strange. Having determined our goal, I got to pick the server for vulnerabilities. But in the end I met a login form that was not protected from brut-force attack. Brut-forcing… of course, I did not become impudent. After all, now I live in a country where even torrents are severely punished. And if I conduct such attacks, this is not the most correct act. Though it is without malice. In short, as we usually remember about 272 Russian law, no matter what country you live in.

When i launched app i found password field. Of course, we did not know the password. So a couple of days passed. I was immersed on the main job from morning to evening. And there was practically no time to do something. And then the application reminded itself. He sent me a push-notification. It was not just a notification. It was an information message about a new published article. With the title of this article itself from the internal system.

It immediately made me look more closely at the app. First, notification can not so easily come to an unauthorized user. After all, I have never logged into app. I just opened it and moved to the background. Secondly, I received the notification text from the internal system. And i don't have access to this system at all.

The first thing which I thought about — maybe I have a “token” to the system, which I can reuse to read the something from internal system.

Everything turned out as I thought. Like that. In fact, much worse than I thought.

When you launch the application, it's sends a request to the internal system to read the data that needs to be displayed. The first request from the application falls with 401 error. That, in principle, is reasonable. After all, we are unauthorized users. But then the app again quickly sends another request, but with a token, which is hardcoded into app. And gets 200 from the server side. What does this mean? This means that without any input of login and password, you can read data from the internal system.

In my first approach to analyzing this application, I simply did not check the value of two requests. And most importantly — did not check the size of the response from the server. On the screenshot it's on the right side of the red arrow. Several megabytes of data in json format.

Press enter or click to view image in full size

What do we have as a result?

A typical application launch displays a splash screen with logo. Loading this screen goes in parallel with obtaining a json response with information from the internal system. Then app asked user some password data. If the user is logged in, then he can work with the received data. But we are not ordinary users, we can open received json and see what we have.

And it was epic. At a cursory examination of the json file, I found a full disclosure of personal data about 170 famous people who interact with this company. Personal phones, e-mail addresses, emergency phone numbers through friends or parents, full names and full personal information about managers of that famous personalities. To say that I was surprised — do not say anything.

Press enter or click to view image in full size

Having played around with the parameters of the request to receive this json file, I managed to get an absolutely complete list of famous people with whom this company interacts. And this, for a minute, already 1454 people.

Press enter or click to view image in full size

Basically, I managed to pull out the full list of ads from the internal system. For example, the emergence of new products from this company. Or as in our case — the presentation of our wonderful app, which safely reveals all data already for 2–3 months.

Press enter or click to view image in full size

What I did when I discovered this? I'v did my best and found a person directly responsible for security in this company. Really helped me on this linkedin only. In all other ways of communication, I either did not receive an answer at all. In the end, after a couple of days, both applications were removed from public access. The tokens, which was hardcoded in the app, still left the possibility of reading data from the internal system. But all sensitive data carried outside from the internal system. In general, in situation with a token, it’s not clear what they thought when hardcoded this token in the ios and android app, encoding token itself over and over again in base64. Coding then why did you need it? S — safety.

Get Valeriy Shevchenko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By the way, I made a claim to the person who is responsible for security , that they do not have a security@domain.com mail box. After all, I tried to write there, but received a mail-daemon. In response, he told that there was a box. And it’s called securitynotification@domain.com.

Let’s return to our push-notification. It was first information disclosure.
The reason of the problem with push-notification is extremely simple — mistake in configuring push notifications service. For these notifications they used third-party service. In order to work with it, you must have: REST API key notification service and your app API key.

It is configured according to the instructions from the official website… But no one has managed.

In the end, what have you done? Correctly! Hardcoded in the application, everything necessary to work.

When you start the application — we take 200-ok from the service that sends these notifications.

Press enter or click to view image in full size

Beauty.

Summarizing, we have:

1) The application was not taught to work on httpS. And, I suspect that they will not fix it.

2) There is no protection against brute-force attacks when trying to guess the password. In fact, the combination of passwords in the application is approximately 10,000. It moves fast enough.

3) The application was given a unique token to read data from the internal system. This is directly win win.

4) The application was registered with notification service, which was configured incorrectly.

5) In the application there is no division of roles. Any user can read anything from the internal system.

In my opinion, all this could be avoided simply by testing. Yes, it was at the level of testing that these development and design mistakes should be found before release.

Chronology:

29 june — First report was send

30 june — All issues was confirmed

7 july — Reward was offered

10 july — All issues Fixed

27 july — I chose a trip to Amsterdam for one interesting event as a reward

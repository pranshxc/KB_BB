---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-16_part-1-dive-into-zoom-applications.md
original_filename: 2021-06-16_part-1-dive-into-zoom-applications.md
title: Part-1 Dive into Zoom Applications
category: documents
detected_topics:
- access-control
- command-injection
- file-upload
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- command-injection
- file-upload
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 0c3e793ab02e6a8fde17c1eb2c885c63d0875c8027d4b8b9c7798c6cd9e6a05c
text_sha256: 3863b1a757cef62fedd13c2396e4667820d3940c7a3208f290889be0d79234d4
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Part-1 Dive into Zoom Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-16_part-1-dive-into-zoom-applications.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `0c3e793ab02e6a8fde17c1eb2c885c63d0875c8027d4b8b9c7798c6cd9e6a05c`
- Text SHA256: `3863b1a757cef62fedd13c2396e4667820d3940c7a3208f290889be0d79234d4`


## Content

---
title: "Part-1 Dive into Zoom Applications"
url: "https://rakesh-thodupunoori.medium.com/part-1-dive-into-zoom-applications-d70f3de53ec5"
authors: ["Rakesh Thodupunoori (@rakesh_3895)"]
programs: ["Zoom"]
bugs: ["CSRF", "Payment bypass", "Logic flaw", "Account takeover", "Privilege escalation"]
bounty: "22,000"
publication_date: "2021-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3569
scraped_via: "browseros"
---

# Part-1 Dive into Zoom Applications

Part-1 Dive into Zoom Applications
Rakesh Thodupunoori
Follow
6 min read
·
Jun 16, 2021

701

1

TL;DR

A quick Introduction about Myself, I am Rakesh Thodupunoori working as a security consultant in a Reputed Company and a part-time bug bounty hunter.

This is my first writeup, I will try to be more clear but not step by step, you may find many mistakes while reading, if possible let me know via a direct message which helps me to fix my mistakes from the next writeup.

This series of writeups are on Zoom Applications, and how I made ~22,000$ from Zoom applications. I am going to explain from where I started and where it all ended.

Back in 2018, I got an invitation from the zoom application. Initially, I have no idea what the zoom application is about so I took some time and understood a bit about the application and its functionalities.

Now its time to find some vulnerabilities,

#1 It all started with bypassing CSRF in fact it's not bypassing CSRF. I found a misconfiguration in CSRF header implementation, Basically, the application has CSRF Header which implemented in the request is not validated on the server-side, I confirmed that by removing the CSRF Header from the request and observed the successful response in the burp suite. Soon I made a POC and submitted it. Later I found the same vulnerability in few other functionalities and got rewarded.

Example Request

Press enter or click to view image in full size

Final CSRF POC

<html>
<body>
<form action=”https://zoom.us/reducted/delete" method=”POST”>
<input type=”hidden” name=”id” value=”reducted" />
<input type=”hidden” name=”user&#95;id” value=”” />
<input type=”hidden” name=”occurrence” value=”” />
<input type=”hidden” name=”sendMail” value=”false” />
<input type=”hidden” name=”subject” value=”” />
<input type=”hidden” name=”mailBody” value=”” />
<input type=”submit” value=”Submit request” />
</form>
</body>
</html>

#2 Later looking for other functionalities I found an endpoint /developers/* which redirects to developers.zoom.us where a user can register/start a trial as a developer and manage their API keys, it has two functionalities users can create an API and later disable it. Again tested for CSRF this time the request doesn't contain CSRF token in headers

Press enter or click to view image in full size

Reported on different functionalities and got rewarded.

After few days they fixed it by adding “wp-nonce” parameter. Later I bypassed the fix but they consider it as out of scope. So no fix is applied.

#3 Let's find more CSRF’s

This time I observed I can add/modify/disable users like admin, member, etc by owner.

Here also all the requests (add/modify/delete/disable) contains a CSRF token in the header but this time there is something in the body that is “user_id=” parameter with a random token. Anyways out of curiosity I removed the CSRF header from request and the got a successful response. However, this cannot be exploitable due to the random “user_id=” value. The disable user request would look like

disable user request

After spending a day I was able to find an endpoint that disclosed “user_id=”. It was identified in the profile upload when a user uploads a profile image and views it the profile URL looks like “https://zoom.us/p/GGyDDIP6Qeef1Ol5u-97-g/<token2>”. Made a POC and reported it, Found it in multiple functionalities, and later got rewarded.

The final CSRF POC would be like

<html>
<body>
<script>history.pushState(‘’, ‘’, ‘/’)</script>
<form action=”https://zoom.us/account/<Reducted>/<Reducted>" method=”POST”>
<input type=”hidden” name=”user&#95;id” value=”GGyDDIP6Qeef1Ol5u-97-g” />
<input type=”hidden” name=”status” value=”0" />
<input type=”submit” value=”Submit request” />
</form>
</body>
</html>

Enough of finding CSRF’s, Lets move to other…

#4 Utilizing Paid features for free

This time I took a basic zoom subscription, and navigate to all the functionalities one by one, then observed many features are not included in the trial account. I tried capturing the request from a paid account and sent the request to the repeater tab, then replaced the trial account cookies which is still working and I was able to use all paid features for free using the same method. Again Created POC and reported. Rewarded!

After getting enough bounty I stopped working on Zoom applications. Later in mid-2019. I got a mail as zoom increased rewards. So I thought of testing again.

Get Rakesh Thodupunoori’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

#5 Compromising Triager Zoom Account With One-Click

This would be fun to exploit. While testing Login functionality I suspected something is not good on “cookies” I found duplicate cookies in response which I felt suspicious

# Login Request

Press enter or click to view image in full size
Login Request

#Login Response

Press enter or click to view image in full size
Login Response

Observe the duplicate Set-Cookie values. Later I understood that one cookie is the older one and one is the newer, which means if a user logins and logs out ideally the cookie should change but when the user logs into his account the server responds with both new cookie and old cookie. This made me think. Why is the server sending old cookies?

I tried refreshing the application and intercepted it then this time from the request the old cookie is disappeared, I am in a confusion now where is the old cookie? After spending some time I logged out and tried login again encountered the same two cookies, I noted both. This time I refreshed the application and intercepted the request then replaced the new cookie with an older one and forwarded the request thinking of signed out of the application but to my surprise, I am still logged in. Reported to zoom thinking of possible of Session Fixation issue. But the response I got is

Press enter or click to view image in full size

After this, I started thinking about how to Craft a URL that replaces user cookies with attacker-controlled cookies.

After some trial and error, I was able to craft a URL that replaces user cookies with attacker-controlled Cookies.

Crafted URL: https://zoom.us/<reducted>?firstName=rakesh&lastName=bugcrowd&<Reducted>&_zm_ssid=gVKn0WuETdSgJTfb6kvqzg

Press enter or click to view image in full size

I asked traiger to click on the link after he logs into his zoom account, when triager clicks on the link the attacker-controlled “_zm_ssid=” cookie will be replaced in _zm_ssid of traiger account which is stored in the browser. However, he did not understand what happened initially because he cannot view any changes in his account. But if I click on the same link which is sent to triager without logging into my zoom account I was able to access triager account.

NOTE: Later I understood that“_zm_ssid=” accepts any string, integer as cookie even if I give 1 or a it accepts.

Press enter or click to view image in full size

I added my email id as admin in triager account.

Press enter or click to view image in full size

Soon after sending the Screenshots, Report got triaged and Rewarded!

#6 It's Time For Privilege Escalations...

After adding my account to triager account, I thought of working on privilege escalations because the zoom owner can add multiple users with different roles. for ex: admin, member and custom roles, etc.,

Initial finding — From the owner account added one admin and one member than from the admin account I tried changing the role of member to admin and captured the request

observed the “roleId=” set to 2 which means admin role, I tried changing it to 1, and guess what? I changed the member role to the owner. But the impact would be less as these are done by a high privileged user (Admin). I want to increase the impact to get more bounty. Let’s try with a low privileged user.

Soon I created two more member accounts from the owner account. Then logged into one member account and used the cookies in the above request with another member id as “user_ids=”, which again gives a successful response from the server. Soon made a POC and reported. Rewarded!

any feedback, comments, and suggestions would be highly appreciated

To be Continued…

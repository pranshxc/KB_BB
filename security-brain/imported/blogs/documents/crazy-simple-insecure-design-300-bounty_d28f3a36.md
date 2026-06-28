---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-15_crazy-simple-insecure-design-300-bounty.md
original_filename: 2022-04-15_crazy-simple-insecure-design-300-bounty.md
title: Crazy Simple Insecure Design & 300$ Bounty!
category: documents
detected_topics:
- command-injection
- file-upload
- cors
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- cors
- information-disclosure
- api-security
language: en
raw_sha256: d28f3a36f74442214b73410c4aae0ad432e91f2d58b201438ca0c9b1961fbac0
text_sha256: 05f229acf68e30cf6bc4ab19181287a8c50e44d42bf795904ad6d8733f4ea29c
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Crazy Simple Insecure Design & 300$ Bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-15_crazy-simple-insecure-design-300-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, cors, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `d28f3a36f74442214b73410c4aae0ad432e91f2d58b201438ca0c9b1961fbac0`
- Text SHA256: `05f229acf68e30cf6bc4ab19181287a8c50e44d42bf795904ad6d8733f4ea29c`


## Content

---
title: "Crazy Simple Insecure Design & 300$ Bounty!"
url: "https://mr23r0.medium.com/crazy-smiple-insecure-design-300-bounty-16a2b8e80522"
authors: ["Saransh Saraf (@mr23r0)"]
bugs: ["IP grabbing"]
bounty: "300"
publication_date: "2022-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2707
scraped_via: "browseros"
---

# Crazy Simple Insecure Design & 300$ Bounty!

Crazy Simple Insecure Design & 300$ Bounty!
Hi guys, I’m Saransh Saraf, An Indian Bug Bounty hunter & Security Researcher (I’ve also done LAMP Stack Development)and this will be a series of Logical Bugs….👾 before we explore this I want little help, If you get rewards or HoF from this give some credit 😼 You’ll get my social links at the end of this article.
Saransh Saraf aka (MR23R0)
Follow
3 min read
·
Apr 15, 2022

392

2

Insecure Design : Asset verification error leads to information disclosure

Few months ago I’ve found an article of IP Grabber Bug which is also known as “pixel that steals data” here you can learn basics about this pixel data stealer bug..

Pixel That Steals Data - I’m Invisible
Summary :

shahjerry33.medium.com

Simple enough right? a month ago I was testing a platform target.com and it was a website builder platform, I didn’t found much bugs there so I was looking for some unique bugs… I was looking at the console tab of a subdomain ex: sub.target.com and I saw a 403 error on 3rd party service the website was using, After investigating it a bit I’ve found that it happening because of Same-Origin & CORS Implementation…hmm Interesting though here you can learn more about Same Origin Policy

Same-origin policy - Web security | MDN
The same-origin policy is a critical security mechanism that restricts how a document or script loaded by one origin…

developer.mozilla.org

“The same-origin policy is a critical security mechanism that restricts how a document or script loaded by one origin can interact with a resource from another origin.” this line gave me a hint for the pixel data stealer, And I began to think “Okay, but how can implement it here”

Well as you know that the website allows us to create other website, for that we have an option to create a team project

Press enter or click to view image in full size
Project Dashboard

After Exploring/Intercepting the Settings/~Requests I found a insecure design issue here is the workflow of the website:

Project Logo → Upload → Back to frontend with URL → Then Save it to User Profile (From the Front end)

Now you’re getting Ideas right..😋

What we’ll do : we’ll upload an Image and when the Application will send the post request we’ll replace it with our IP Logger BIN (URL)

But wait what about the Same Origin ? I totally Ignored it and tested my attack and It turns out that it was Misconfigured and my attack was successful, I got the IP, Location, ISP & User Agent of the Victim, he just have to visit the project dashboard on his/her end.

Wait !! this is not it 🤗

Get Saransh Saraf aka (MR23R0)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I Again Started to explore more, I again got this same issue on the “Site Builder Section”

Press enter or click to view image in full size
Site Builder

It got me 300$ in total till now for 2 Resolved issues, 1 more triaged & 3 Active Submissions.

Summary :

1. Upload an Image to any logo/image upload form →

2. See if the response is coming or not →

3. now hit the save button →

4. See if the application is sending the Image url or not →

5. If yes replace it with the IP logger BIN (URL)

Hope You Enjoyed It, If yes make sure to clap for me :) Don’t worry PoC will be Out soon 🤝😼

Connect with me/ Give a mention & Credit

Saransh Saraf - Security Researcher - Bugcrowd | LinkedIn
I am a student of BSC, but I love computers. That's why I learnt Web Development, Networking and Information…

www.linkedin.com

My Teammate

Harsh Banshpal - G.H. Raisoni College of Engineering(GHRCE), Nagpur - Balaghat, Madhya Pradesh…
View Harsh Banshpal's profile on LinkedIn, the world's largest professional community. Harsh's education is listed on…

www.linkedin.com

Instagram

https://www.instagram.com/sarans0x00h https://www.instagram.com/harsh_ban_

A big Thanks to my seniors, friends and enemies :)

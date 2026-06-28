---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-25_web-cache-deception-attack-leads-to-user-info-disclosure.md
original_filename: 2019-02-25_web-cache-deception-attack-leads-to-user-info-disclosure.md
title: Web Cache Deception Attack leads to user info disclosure
category: documents
detected_topics:
- command-injection
- otp
- graphql
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- graphql
- information-disclosure
- api-security
language: en
raw_sha256: 1ef096d722b208ab7b210163d6a5ae7262cee072a90cb42bd777cad931e5e12e
text_sha256: 35236e1db19c49d3ac902f28d62216b78a774a2fb54cd1a1d2c1ec2cce73c2c8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Web Cache Deception Attack leads to user info disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-25_web-cache-deception-attack-leads-to-user-info-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1ef096d722b208ab7b210163d6a5ae7262cee072a90cb42bd777cad931e5e12e`
- Text SHA256: `35236e1db19c49d3ac902f28d62216b78a774a2fb54cd1a1d2c1ec2cce73c2c8`


## Content

---
title: "Web Cache Deception Attack leads to user info disclosure"
url: "https://medium.com/@kunal94/web-cache-deception-attack-leads-to-user-info-disclosure-805318f7bb29"
authors: ["Kunal pandey (@kunalp94)"]
bugs: ["Web cache deception", "Information disclosure"]
bounty: "300"
publication_date: "2019-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5388
scraped_via: "browseros"
---

# Web Cache Deception Attack leads to user info disclosure

Web Cache Deception Attack leads to user info disclosure
Kunal pandey
Follow
5 min read
·
Feb 25, 2019

801

1

Hello Everyone

Around a few days ago, I got some users information leakage due to web cache Deception Attack.

Before we jump into the POC, I want to explain these kinds of attacks and effects.

Web Cache Deception Attack is a type of attack where web app uses cache but it’s not validating properly which allows an attacker to craft cache leakage attacks.

In this scenario, web apps in the background often tend to use a proxy, CDN and other services to use cache functionality in which it reduces the time from the server or simply to reduce latency but not validating properly.

Suppose if there is a website like www.example.com/home.php and you tried an additional extension at the end of this URL like www.example.com/home.php/a.jpg, and if the website has cache functionality, it basically caches the website internal information and stores it into this above endpoint under their cache Directory, Extension can be anything like .css, .jpg, .js anything.

Once the user will visit and their info will be cached, then an attacker will just visit this same endpoint and Boom! user’s personal info can be leaked by visiting source code.

[Note: visit keypoints at the end of write-up :)]

Let’s jump to the main part

Last weak, while I was invited to a private program, I came across three different targets like (let’s just say)

app.example.com

example.com

manage.example.com

So, you can register in example.com and log-in as well.

app.example.com was the main area to develop app and manage.example.com is another web app which basically uses in authenticating with Slack workspace and other services.

So, example.com was something like this (Sorry for Poor art 😐)

Press enter or click to view image in full size
Example.com

So, it was loading as example.com, but then I saw there was no cache control header or anything. Then I decided to give this a try.

[Note: Not all the time it’s vulnerable even if there is no cache control, see key points at the end of this write-up.]

So, I decided to visit endpoint like https://example.com/welcome.css

Press enter or click to view image in full size
Example.com/welcome.css

Notice in this 404 error page, it was still displaying go to your workspace, that means you can fetch some info.

Alright, After visiting this above URL, just visited the same endpoint in incognito mode.

But here comes the observation part, While I visited this endpoint in incognito mode, then for only 2–3 seconds it displayed me “Go to your Workspace” and then itself changes into login and signup area. It was totally a glimpse moment.

Get Kunal pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And I was like :

Maybe, as the session is not been cached properly and so for a glimpse of a moment, it showed me like “Go to your workspace” and changing itself into signup and login option but it has cached the info. So, let’s just visit the “view-souce:https://example.com/welcome.css” and see if there is any info has been cached and not.

Press enter or click to view image in full size
Info leaked

So, yeah info has been cached and disclosed all the personal details.

1st part done

So example.com was over, So I tried to visit app.example.com, but no luck.

So, let’s go for manage.example.com

manage.example.com was just another web app where it allows the user to connect their slack workspace and also it can be used to retrieve info using API endpoint.

So, while I tried to visit manage.example.com and so, it redirects me to app.example.com, so there are some routing rules placed in the backend. It means manage.example.com can only be used for /api endpoints or /auth endpoints.

So, I just tried to simply inject any path like /a and it was showing me a response like this.

Press enter or click to view image in full size
manage.example.com/a (error endpoint)

So, It means that this site has been depreciated in terms of frontend interaction.

But, then suddenly I saw the response header and there was no cache control header. But I was still confused like whether it’s going to work this time or not.

So, I tried to visit endpoint like manage.example.com/hello.css and response was the same as above.

But when I visited the same endpoint in incognito mode, it cached the info and displayed me the same view with active session mode.

So, I tried to visit the endpoint using view-source://manage.example.com/hello.css and this time, info has been cached in huge amount comparing to 1st part (example.com).

Press enter or click to view image in full size
manage.example.com/hello.css

And I was like

Timeline

9th Feb 2019: Submitted the report.

11th Feb 2019: Team triaged the report.

21st Feb 2019: Resolved and rewarded with $150 + $150 with reports and Got positive feedback as well.

Some Keypoints:

If there is cache header is missing, then that doesn’t mean you’ll get Cache info attack. It also depends on backend how routing actually works.
Second, sometimes you can land up to that page even after adding additional parameters and sometimes, you’ll land up in 404 error page, but if there is no info in the source code of 404 error page, then it’s no use.
Most of the time, companies use API or Graphql endpoints to retrieve data, so if you see a session in incognito mode but you can’t view information in the source code of that page, then no use. Only your account name will be leaked nothing else.
Lastly, check all the aspects and report and analyze over and over again and think if you get token or other things, then you can chain other bugs or not.

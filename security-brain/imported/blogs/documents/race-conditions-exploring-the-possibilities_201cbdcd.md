---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-11_race-conditions-exploring-the-possibilities.md
original_filename: 2020-06-11_race-conditions-exploring-the-possibilities.md
title: Race Conditions - Exploring the Possibilities
category: documents
detected_topics:
- oauth
- race-condition
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- oauth
- race-condition
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 201cbdcd8b59117ed3059a6e550d9dea86e21284b751c65776b8d3cf49f1f2e9
text_sha256: 23ab40baad08c55c279ac063cd9df0232fcdd91aa307c8557a84e8e3b0f07dc3
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Race Conditions - Exploring the Possibilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-11_race-conditions-exploring-the-possibilities.md
- Source Type: markdown
- Detected Topics: oauth, race-condition, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `201cbdcd8b59117ed3059a6e550d9dea86e21284b751c65776b8d3cf49f1f2e9`
- Text SHA256: `23ab40baad08c55c279ac063cd9df0232fcdd91aa307c8557a84e8e3b0f07dc3`


## Content

---
title: "Race Conditions - Exploring the Possibilities"
page_title: "Race Conditions - Exploring the Possibilities - PandaOnAir"
url: "https://pandaonair.com/2020/06/11/race-conditions-exploring-the-possibilities.html"
final_url: "https://pandaonair.com/2020/06/11/race-conditions-exploring-the-possibilities.html"
authors: ["Milind Purswani (@MilindPurswani)"]
programs: ["Reddit"]
bugs: ["Race condition"]
publication_date: "2020-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4507
---

# Race Conditions - Exploring the Possibilities

  * [race-condition](/archive.html?tag=race-condition)
  * [bugbounty](/archive.html?tag=bugbounty)
  * [web](/archive.html?tag=web)

  * __ Jun 11, 2020

## Background TLDR;

![RACE](/assets/images/race-meme2.jpeg)

Race conditions are not that old. They are very widely available much more than you might think they are. While we do see that they have not made it in the OWASP Top 10, if there were an 11th Position, I think that place would be perfect to rate their severity. While most of the frameworks now a days have inbuilt capability to handle them, programmers often neglect some areas where the appropriate locks have to be implemented. Wait! What!?.. What’s a lock? In-order to understand the RC, we first need to understand the working of a large application in a multithreaded environment. Let’s just learn about it in very brief. Let’s understand this with a small example:

Assume that there is a small website that allows signing-up users. At the registration, the users are prompted to enter their `username`, `password` and desired `email` address. Once the user clicks on the sign-up button, they are allowed to sign-up to the website. When the user tries to signup again, s/he can’t use the same email address or the same username again. Why do you think that is the case? That’s probably because `username`/`email_address` is the entity that is used by the web application to uniquely identify it’s users. In a sense, we can probably say that there can be only one user for one username. We can very vaguely link this to the one-to-one cardinality of our Database Management System Concepts. Now the question here is, what if there were to be more than one user somehow in the database with the same identity? If the username, is used as a primary key in one table, we know that there cannot be more than one primary key in a table! So, if somehow we manage to get more than one primary key in a table, what do you think happens then? This is where RC comes. Oh! btw, during the course of writing this, I may casually switch between race condition and RC so don’t get alarmed.

In one of my tweets, I asked people:

> Here is a pole to make things easier
> 
> — Milind (@MilindPurswani) [June 10, 2020](https://twitter.com/MilindPurswani/status/1270751264809390085?ref_src=twsrc%5Etfw)

Ignoring the silly spelling mistake, I was surprised at this ratio. Given the fact that the issue is so widespread and not so many people are testing for it, I decided to write this article about some of my findings in race condition. I am no expert at this, whatever I am sharing comes through learning, and I am still learning.

## The Attacking Methodology

For this, we are going to extensively rely on [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack). Its an amazing tool by James Kettle ([@albinowax](https://twitter.com/albinowax)). If you have not read his research yet, I recommend you check it out as it will probably give you quite a lot of insight to the current issue here. Now turbo-Intruder is a great tool, it implements it’s own network layer TCP stack which allows it to send multiple requests per second. This is much higher than the traditional Intruder that comes with a Pro license of Burp. Although it has a small learning curve to it, it’s worth it. For the past few months I can’t remember a single day, I have not used Turbo Intruder atleast once while hunting for bugs. So, the way it works is, you have to be specific about a request that you think could probably create a race condition. Select that request and send it to turbo intruder.

![RACE](/assets/images/rc.png)

Once the request is in the Turbo Intruder, we will use the following script to create race-condition:
  
  
  def queueRequests(target, wordlists):
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=10,
  requestsPerConnection=1,
  pipeline=False
  )
  
  for i in range(10):
  engine.queue(target.req, gate='race1')
  
  # open TCP connections and send partial requests
  engine.start(timeout=10)
  
  engine.openGate('race1')
  
  engine.complete(timeout=60)
  
  
  def handleResponse(req, interesting):
  table.add(req)
  

Over the course of all the examples, that I’ll demonstrate we make small modifications to this script to achieve our goals.

### Race-Condition leads to non-deletable group member

This is an amazing bug that describes one such place where most of us would have never thought about looking it. In this creative find, my friend Yash Sodha [@yashrs](https://hackerone.com/yashrs) found that if a team member joined a group once on [ctf.hacker101.com](https://ctf.hacker101.com) they could not be removed even by group leaders. For some background, once a group is created on ctf.hacker101.com, the group leaders can onboard other group members by sending them invitation link. The invitation can only be used once. Once the invitation is accepted, it cannot be used again, Yash realised this and tried to create a race on the `/group/post_join ` endpoint that accepted the group invite along with his session tokens and `invite` parameter.

You can read more about it [here](https://hackerone.com/reports/604534).

### Classic-old coupon trick

Now this is perhaps the most common use of race-conditions, While hunting on one of the targets, I noticed that one of the very well known e-commerce website allowed their user’s to apply coupon code to provide discount. Now, it is evident that once coupon can perhaps be used only once, so I decided to test this out. Using the same script mentioned earlier, I sent about 10 requests race-condition requests to this endpoint. But nothing happened. I was kind of expecting this since since the website was heavily tested and was pretty well known.

![RACE](/assets/images/classic-old.png)

After a while, I received an update from the program managers stating that the race condition someone tried, created a deadlock within their customer’s database. This was astonishing. I tried to navigate to their website, and learned that it was now impossible to add a coupon. A database lock essentially prohibited all the customers from purchasing anything from their website.

Here is the response when a customer tried to proceed to checkout:
  
  
  HTTP/1.1 500 Internal Server Error
  Date: Thu, 10 Oct 2019 19:11:37 GMT
  Content-Type: application/json; charset=UTF-8
  Content-Length: 46
  Connection: close
  Set-Cookie: REDACTED expires=Fri, 09-Oct-20 19:11:18 GMT; path=/; domain=.REDACTED; HttpOnly
  Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS, DELETE
  Access-Control-Allow-Origin: REDACTED
  Access-Control-Expose-Headers: 
  Access-Control-Max-Age: 1728000
  Vary: Origin
  X-Runtime: 1.826588
  CF-Cache-Status: DYNAMIC
  Server: cloudflare
  CF-RAY: 523ae63e19585739-IAD
  
  {"status":500,"error":"Internal Server Error"}
  

Since the testing was in production environment, I decided to report it to the program. Upon realizing the fact that I was the one who created this deadlock, they gave me a warning and banned me from their program stating that DOS was explicitly OOS.

Sometimes I don’t get these programs, this was a database level DOS which created a critical impact on availability. I am pretty sure that a blackhat would probably have not stopped to read and adhere by the terms and conditions of testing. Whatever!

### OAuth 2.0 Code -> AT - RT Exploit

The current issue is perhaps one of the issue that is highly under-appreciated. Initially discovered by [@dor3s](https://twitter.com/dor3s) and reported to [the internet](https://hackerone.com/reports/55140), basically breaks the one-to-one correspondence between a single `authorization_code` and an `access_token`. How does it work? Inorder to understand this we need to understand the OAuth 2.0 Authorization Model and specifically the _Authorization Code Grant_. You can read about it [here](https://tools.ietf.org/html/rfc6749#section-4.1). A few conditions that are required here:

  1. Your target needs to be an OAuth 2.0 Service provider; meaning, that you should be able to register your own application on the target. Here is a comprehensive [list](https://en.wikipedia.org/wiki/List_of_OAuth_providers) of some of the OAuth providers.
  2. They should support Authorization code grant. Some of the OAuth providers don’t support authorization code grant. There are a few other grants available in OAuth 2.0, which you can learn about [here](https://tools.ietf.org/html/rfc6749#section-1.3). 
  * Some programs don’t allow you to register an OAuth application without proper authorization, meaning you can either register for sandbox environment such as [Paypal](https://hackerone.com/paypal) or they will require you to validate you identity and then register for the application.
  * In this case, recon is your best friend. Try to look for `client_id`, `client_secret` and `redirect_uri` on Github or using google dorks. This does help and plus you may be awarded a bonus for discovering the leaking credentials.
  * _Keep in mind that leaked credentials aren’t a vulnerability in itself and most of the programs would simply close your report as N/A._

If these conditions are met, you can test for `Oauth 2.0 Code -> AT/RT` exploit.

Let’s understand this with a case study.

#### Case Study: Race condition in Reddit’s OAuth 2.0 Implementation.

When I learned about this attack vector, this was the first application that I tested which turned out to be vulnerable. Reddit allows you to register an OAuth application to authenticate users. I registered an OAuth 2.0 Application on their website at `https://www.reddit.com/prefs/apps` and followed their documentation at `https://github.com/reddit-archive/reddit/wiki/oauth2`. Roughly here are the steps that I followed.

  1. Register an application on your target’s website.

  2. Obtain the `client_id`, `client_secret` and `redirect_uri`. You can optionally also use the `scope` parameter, but that won’t be of any use to us in this case.

  3. Generate an authorization URL - It is roughly of the following format. The URL path could be different but the basic query parameters remain the same.

`https://<target>/api/v1/authorize?client_id=<your-client-id>&redirect_uri=<your-redirect-uri>&response_type=code`

  4. Now send this URL to your victim.

  5. Once the victim authorizes the application you will receive a `code` on your `redirect_uri`.

  6. This code can now be exchanged to obtain `AT`/`RT` pair. In case of reddit, it was as mentioned in the below screenshot.
  
  POST /api/v1/access_token HTTP/1.1
  Host: www.reddit.com
  Authorization: Basic bs64(client_id:client_secret)
  User-Agent: insomnia/2020.2.2
  Content-Type: application/x-www-form-urlencoded
  Accept: */*
  Content-Length: 132
  Connection: close
  
  grant_type=authorization_code&code=<obtained-code>&redirect_uri=<your-redirect-uri>
  

you can learn more about reddit’s AT retrieval [here](https://github.com/reddit-archive/reddit/wiki/oauth2#retrieving-the-access-token).

  7. Send this request to Turbo Intruder and see if you got more than one `AT`/`RT` pairs. In case of reddit, there were quite a lot of different pairs generated.

![RACE](/assets/images/reddit.png)

  8. Now, you can probably understand the severity of this attack-vector.

Using one `authorization_code` a malicious application was able to obtain more than one `AT`. This behavior doesn’t pose any immediate risk since the user himself decided to authorize the application. But consider this. What if the user wanted to revoke the malicious application’s access from his account? Reddit has provisions made for that as well. You can navigate to https://www.reddit.com/prefs/apps and simply de-authorize an application.

However, since we authorized the application using race condition, it was observed that even though the application was deauthorised, only one of it’s `AT`/`RT` pair was revoked. The other’s were still valid. Hence, the malicious application was persistently able to maintain access to reddit’s users inspite of them deauthorizing the application.

I reported this issue responsibly and reddit has currently fixed this issue.

### OAuth 2.0 RT -> AT - RT Exploit

This issue was also highlighted in the [report](https://hackerone.com/reports/55140) submitted by [@dor3s](https://twitter.com/dor3s) to the internet. Basically, unlike the above `code -> AT/RT` race condition, we create a race to obtain multiple `AT/RT` with a single `RT`. The authorized application sends a request something like this:
  
  
  POST /api/v1/access_token HTTP/1.1
  Host: www.reddit.com
  Authorization: Basic bs64(client_id:client_secret)
  User-Agent: insomnia/2020.2.2
  Content-Type: application/x-www-form-urlencoded
  Accept: */*
  Content-Length: 112
  Connection: close
  
  grant_type=refresh_token&refresh_token=<your-previous-refresh-token>
  

According to the finder, a race condition found here is even more serious because once a `code` is obtained, it can perhaps be used only once to obtained multiple `AT`/`RT` pair. However, if the `RT` is able to obtain multiple `AT`/`RT` pairs, then that can be used any number of times to generate new pairs. The situation get’s worsen when the access to the resource server is persistent inspite of de-authorizing the application. [Here](https://blog.avuln.com/article/4) is a blog by [@dor3s](https://twitter.com/dor3s) himself that explains about this issue in a little more depth.

### Racing to create fake followers and fake likes

As the title mentions, this issue was discovered in one of the well-renowned social media platforms. The ability to increase the followers and likes by creating RC. Unfortunately, I cannot disclose this report since the current issue has not been mitigated yet. But trust me, if you look for any place where it is possible to do a `like` or `subscribe` or `upvote` or `follow`. Try RC there. You will be surprised how many of such applications are vulnerable to this. Here I’d like to add one thing. While testing for this bug, make sure you also test on mobile endpoints. In this case, my friend Yash ([@yashrs](https://twitter.com/y_sodha)) had already found most of the endpoints vulnerable to RC however, after a little bit of research, I learned that although all the endpoints of Web-application were reported, the Mobile Application was still vulnerable. So, I went ahead and reported them right-away![:stuck_out_tongue:](https://github.githubassets.com/images/icons/emoji/unicode/1f61b.png).​ Later the program declared RC as OOS (which was sad).

### Race to create Loss

This one is the most interesting bug that I recently found and played a crucial role for me tweeting about RC issue. While assessment on one of my targets, I tried the classic-old coupon trick that I described above, but it didn’t work out well. However, this time I tried one more trick. I modified the above python code to something like this:
  
  
  def queueRequests(target, wordlists):
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=5,
  requestsPerConnection=1,
  pipeline=False
  )
  a = ['Session=<session_id_1>','Session=<session_id_2>','Session=<session_id_3>']
  for i in range(len(a)):
  engine.queue(target.req,a[i], gate='race1')
  
  # open TCP connections and send partial requests
  engine.start(timeout=10)
  
  engine.openGate('race1')
  
  engine.complete(timeout=60)
  
  
  def handleResponse(req, interesting):
  table.add(req)
  

In this case, I created 3 different accounts and used a single coupon (which was only one time use) to these 3 accounts and was successfully able to reach to their payment gateway. At this point it was enough to demonstrate the severity of the report and the report was acknowledged by the program managers.

### Some other articles on RC

<https://portswigger.net/daily-swig/google-recaptcha-outfoxed-by-turbo-intruder>

<https://portswigger.net/research/cracking-recaptcha-turbo-intruder-style>

[Race condition on performing retests](https://hackerone.com/reports/429026)

[Race condition in flag submission](https://hackerone.com/reports/454949)

[Race condition in claiming credentials](https://hackerone.com/reports/488985)

and many more…

## Recommended Fix?

![RACE](/assets/images/race-meme1.jpeg)

There isn’t any specific way of fixing an RC issue. In case of multithreaded applications, it is essential that we rely on locks before we get into critical section. However a lot of things have to be considered even while applying locks. An improper implementation on thread locking can lead a sequence of locks from which the application may not be able to escape. This situation is called Deadlock as explained in the above classic old coupon trick. Moreover, it has to be kept in mind that the locking mechanism should only be implemented on the critical section. So, defining the boundaries of critical section is one of the most important aspect. If the critical section is large, it will significantly impact the performance of the Web Application.

The [C](https://docs.oracle.com/cd/E19683-01/806-6867/sync-12/index.html) and [Go](https://tour.golang.org/concurrency/9) use mutex locks for putting a lock. They are pretty simple and easy to use and can be implemented easily after reading a little bit of documentation.

There is a limit to the content that I can write in a single blog. I hope you guys liked it. Do let me know in the comments how you felt or if you have any doubts, DM me on twitter on [Milind Purswani](https://twitter.com/MilindPurswani) or [@panda0nair](https://twitter.com/panda0nair).

Special thanks to Vishal Panchani [@vis_hacker](https://twitter.com/vis_hacker) and Yash Sodha [@y_sodha](https://twitter.com/y_sodha) for reviewing and proofreading the content.

Thanks,

[Milind Purswani](https://twitter.com/MilindPurswani)

* * *

__[Subscribe](/feed.xml)

PREVIOUS[Absolute Bruteforce with Selenium](/2020/03/14/absolute-bruteforce-with-selenium.html)

NEXT[Takemeon](/2020/06/29/takemeon.html)

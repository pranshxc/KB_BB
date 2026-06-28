---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-21_write-up-google-bug-bounty-lfi-on-production-servers-in-springboardgooglecom-133.md
original_filename: 2019-05-21_write-up-google-bug-bounty-lfi-on-production-servers-in-springboardgooglecom-133.md
title: 'WRITE UP – GOOGLE BUG BOUNTY: LFI ON PRODUCTION SERVERS in “springboard.google.com”
  – $13,337 USD'
category: documents
detected_topics:
- rate-limit
- idor
- access-control
- xss
- command-injection
- path-traversal
tags:
- imported
- documents
- rate-limit
- idor
- access-control
- xss
- command-injection
- path-traversal
language: en
raw_sha256: 960143fb74566600c62d2948c1b7917f230b9e9733fbccd38c04bddab7e3ab72
text_sha256: bbeaf838e24a55897282c1e76db14b520317fc93f9127d3b1e53de08ae9f5bf2
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# WRITE UP – GOOGLE BUG BOUNTY: LFI ON PRODUCTION SERVERS in “springboard.google.com” – $13,337 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-21_write-up-google-bug-bounty-lfi-on-production-servers-in-springboardgooglecom-133.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, access-control, xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `960143fb74566600c62d2948c1b7917f230b9e9733fbccd38c04bddab7e3ab72`
- Text SHA256: `bbeaf838e24a55897282c1e76db14b520317fc93f9127d3b1e53de08ae9f5bf2`


## Content

---
title: "WRITE UP – GOOGLE BUG BOUNTY: LFI ON PRODUCTION SERVERS in “springboard.google.com” – $13,337 USD"
page_title: "GOOGLE BUG BOUNTY – LFI ON PRODUCTION SERVERS IN SPRINGBOARD.GOOGLE.COM – $13,337 USD – @omespino"
url: "https://omespino.com/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/"
final_url: "https://omespino.com/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/"
authors: ["Omar Espino (@omespino)"]
programs: ["Google"]
bugs: ["LFI"]
bounty: "13,337"
publication_date: "2019-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5254
---

WEB$13,337 USD[May 2019](/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/)

# GOOGLE BUG BOUNTY – LFI ON PRODUCTION SERVERS IN SPRINGBOARD.GOOGLE.COM – $13,337 USD

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about my greatest find so far (My first P1)

![](/assets/images/2019/05/Screen-Shot-2019-05-23-at-9.38.57-PM-1024x117.webp)

It was in Google VRP program and why you can always check for dirs in 301 / 302 / 403 / 404 status pages because you will surprise that some times some directories listing will work:

[ U P D A T E ] 19 NOV 2019: I was invited to Google yearly security event called ESCAL8 as a speaker and my talk was about how I found this bug in more detail, here is a tweet extract about and the slides:

> Thank you for having me as speaker on [#ESCAL8](https://twitter.com/hashtag/ESCAL8?src=hash&ref_src=twsrc%5Etfw) [#bugSWAT](https://twitter.com/hashtag/bugSWAT?src=hash&ref_src=twsrc%5Etfw) [#initg](https://twitter.com/hashtag/initg?src=hash&ref_src=twsrc%5Etfw) [@GoogleVRP](https://twitter.com/GoogleVRP?ref_src=twsrc%5Etfw) event, super dope event, super dope people [@sirdarckcat](https://twitter.com/sirdarckcat?ref_src=twsrc%5Etfw) Tomasz [@wtm_offensi](https://twitter.com/wtm_offensi?ref_src=twsrc%5Etfw) [@WHHackersBR](https://twitter.com/WHHackersBR?ref_src=twsrc%5Etfw) [@LiveOverflow](https://twitter.com/LiveOverflow?ref_src=twsrc%5Etfw) & all VRP Hunters, such a nice week Fast Recon GG slides <https://t.co/XCPxtsTOGr> [#BugBounty](https://twitter.com/hashtag/BugBounty?src=hash&ref_src=twsrc%5Etfw) [#infosec](https://twitter.com/hashtag/infosec?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/Da3KWCkPiu](https://t.co/Da3KWCkPiu)
> 
> — Omar Espino (@omespino) [November 4, 2019](https://twitter.com/omespino/status/1191224520646045696?ref_src=twsrc%5Etfw)

**FIRST ROUND**

**Title** Auth bypass in springboard.google.com  
**Product / URL: ​** springboard.google.com/REDACTED_DIR **Report sent via google VRP program<https://goo.gl/vulnz>**

**Summary**

Authorization bypass in https://springboard.google.com/REDACTED_DIR and see “OnContent Debug for” mini dashboard

**POC**

1.- Go tohttps://springboard.google.com/ and got redirected tohttps://cloudsearch.google.com/cloudsearch/error?et=6 and see the message

![](/assets/images/2019/04/works-accounts-only-1-1024x956.webp)

2.- Then navigate to https://springboard.google.com/REDACTED_DIR and see a mini dashboard with the form:

![](/assets/images/2019/04/oncontent-debug-1024x356.webp)

3 days after that I got a message: At first glance, this might not be severe enough to qualify for a reward, though the panel will take a look shortly.

**Spoiler:**

Unfortunately, after a week, I got the reply that from google VRP Panel: “As a part of our Vulnerability Reward Program,we decided that it does not meet the bar for a financial reward“

**SECOND ROUND**

Since the bug probably won’t be elegible to get a financial reward, I started thinking to go deeper on that “Auth bypass”, I mean, for some reason is not suppoused to be open, so I decided to try again, then after some new dir enumeration with [wfuzz](https://github.com/xmendez/wfuzz), I got something really really interesting, I was able to escalate that simple Auth bypass bug to LFI on production servers as admin in google production servers. Note: to any people that wonders how I have found the REDACTED_DIR, I used wfuzz to brute force a dir list in [https://springboard.google.com/ ](https://t.co/LiSw6Vlfsu) and filter the non 302 redirect responses that gave me as result [https://springboard.google.com/REDACTED_DIR ](https://t.co/m3OQEMCChz) , since the 302 redirected me to [http://cloudsearch.google.com ](https://t.co/6IKCO2FqOc) I did that brute force before the redirect

**Title** LFI on production servers in the same subdomain  
**Product / URL: ​** springboard.google.com/REDACTED_DIR/ANOTHER_DIR

**Summary**

I’ve able to escalate this auth bypass to LFI on google production servers as “gxx-xxxx” user (admin privileges)!

**POC**

1.- First see that the dashboard panel of “Redacted status main” (FrameworkInfo) is open in <https://springboard.google.com/REDACTED_DIR/ANOTHER_DIR>

![](/assets/images/2019/04/status-main-framework-1024x805.webp)

2.- Then if you navigate to “Show REDACTED” (The last option) you are going to be redirected to <https://springboard.google.com/REDACTED_DIR/ANOTHER_DIR?file=/proc/self/environ> and the /proc/self/environ will be loaded

![](/assets/images/2019/04/proc-self-environ-1024x540.webp)

3.- Just to be sure that was a full LFI working I tried to load another file and I checked with /proc/version and works just as expected!

![](/assets/images/2019/04/proc-version-1024x201.webp)

Then my heart stopped for a second, I just got a LFI on google production servers as administrator (servers on plural because each time that I refreshed /proc/self/environ file the hostname changed)

To be honest I tried to escalate to RCE but I hadn’t any success, since apparently it was very hardened I wasn’t able to read /proc/*/fd, ssh keys, server keys or any logs.

**Environment**

\- Any browser (I used Google Chrome Lastest version)  
\- No authentication or any Google account was needed

**[Rank 62th in Google HOF (May 2019)](https://bughunter.withgoogle.com/profile/e4840477-ddba-46ea-ba4f-068bbe08098a)**

![](/assets/images/2019/05/google-hof-omespino-62-no-avatar.webp)

**Special Media Mentions:**  
Intigriti (Bugbounty platform) May 28, 2019  
[Intigriti Bug bytes #20 write up of the week (Another Google LFI)](https://blog.intigriti.com/2019/05/28/bug-bytes-20-another-lfi-on-google-turning-your-time-into-bugs-by-zseano-live-hacking-like-a-mvh-by-fransrosen/)

Hackerone (Bugbounty platform) May 29, 2019  
[Hackerone Zero Daily 2019-05-21 (Other articles we’re reading)](https://www.hackerone.com/zerodaily/2019-05-29)

**Report Timeline**  
Mar 22, 2019: Sent the report to Google VRP (Just the bypass auth part)  
Mar 22, 2019: Got a message from google that the bug was triaged  
Mar 25, 2019: Bug Accepted  
Mar 25, 2019: Reply about that the bug was in revision in Googgle VRP panel  
Mar 30, 2019: I found the LFI and sent the new POC in the same report  
Apr 1, 2019: Got a message saying that they going to fill a another bug with this LFI information  
Apr 4, 2019: Got a message saying that the first bug wasn’t elegible for financial reward  
Apr 17 ,2019: Since the everything was happening in the same report and the bugs were fixed, I asked to the team if the 2 bugs wasn’t elegibles or what happened  
Apr 23, 2019: Got a message saying that sorry about the confusion and I just had to wait to a new reward decision for the LFI part.  
May 21 2019: $13,337 bounty and permission to publish this write up received

well that’s it, share your thoughts, what do you think about how they handle that security issue? if you have any doubt, comments or sugestions just drop me a line here or in Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-private-bug-bounty-usd-rce-as-root-on-marathon-instance/)

[](/write-up-1000-usd-in-5-minutes-xss-stored-in-outlook-com-ios-browsers/)

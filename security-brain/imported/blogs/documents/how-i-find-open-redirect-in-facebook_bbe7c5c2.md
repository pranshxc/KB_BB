---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-07_how-i-find-open-redirect-in-facebook.md
original_filename: 2022-07-07_how-i-find-open-redirect-in-facebook.md
title: How I find open redirect in Facebook
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: bbe7c5c2ae194c7c3e5bb86bb4267ed541e5a92c053e8375a1d6b3bc7ab0cab7
text_sha256: 76826e43235925f669eecf76095ab568786ce9636285e9dd28f466bfabcfdb4d
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I find open redirect in Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-07_how-i-find-open-redirect-in-facebook.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `bbe7c5c2ae194c7c3e5bb86bb4267ed541e5a92c053e8375a1d6b3bc7ab0cab7`
- Text SHA256: `76826e43235925f669eecf76095ab568786ce9636285e9dd28f466bfabcfdb4d`


## Content

---
title: "How I find open redirect in Facebook"
url: "https://medium.com/@abhinavsecondary/how-i-find-open-redirect-in-facebook-7e7aeb89535d"
authors: ["Abhinav Kumar (@abhinavsecond)"]
programs: ["Brave Software"]
bugs: ["Open redirect"]
bounty: "500"
publication_date: "2022-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2480
scraped_via: "browseros"
---

# How I find open redirect in Facebook

Top highlight

How I find open redirect in Facebook
Abhinav Kumar
Follow
2 min read
·
Jul 5, 2022

97

Hi Guys

My first valid bug on Hackerone and that too with high severity.

This is my first write up and I am going to share with you how I found an open redirect in l.facebook.com. So without wasting any time let’s get started.

On a fine evening one of my old friends sent me a Facebook link and he told me that don’t open it otherwise you will get hacked. I was like REALLY.

I clicked the link and it redirected me directly to Instagram. I was like ok no big deal Facebook allows redirection to the site that are not in their malicious list (Linkshim). But I thought to test it for open redirection. I replaced Instagram URL with evil.com and it redirected successfully.

I was confused with the behavior so I decided to report it to Facebook. What could go wrong? They will say that the report is invalid.

So I reported it to Facebook. And <1 min the team reviewed it and said invalid and this end point is designed for redirection purposes and is protected with the Linkshim System. And they told me that the report will only be valid if I was able to redirect a website that is blocked by Linkshim System and one of the blocked websites is https://test.facebook-whitehat.com that is designed for the same testing purpose. So I tried https://l.facebook.com/l.php?u=https://test.facebook-whitehat.com and I was successful again. I told them and they said they are not able to reproduce it and asked for a POC video and I provided the same. Then I realized that I am using the Brave browser. And they also replied the same that there is no problem from there side it is a client side issue. I immediately understood that this issue is due to the browser not from Facebook.

Now it’s time to test the browser. So I install proxy on the Brave Browser and launched Burp Suite and again requested https://l.facebook.com/l.php?u=https://test.facebook-whitehat.com and I noticed that the browser is directly requesting https://test.facebook-whitehat.com and not requesting l.facebook.com for validation. I reported this issue to the Brave browser and they accepted it within a day and they told me that this issue is due to a feature in the browser called URL Debouncing.

I have reported this issue on medium category but surprisingly the team updated the issue to high. I was very happy and at the same time curious why the issue was upgraded. I did some research and found out that due to this issue there was an open redirect on major sites like Facebook, Amazon, YouTube, Reddit and many more.

Get Abhinav Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Takeaway — Always be aware and test whatever feels out of order

Any suggestion is highly appreciated.

If you are reading till here please do leave a clap. Thanks

Bounty — $500 and swag

Severity — High

Report — https://hackerone.com/reports/1579374

You can follow me on: —

Twitter- https://twitter.com/abhinavsecond

Instagram- https://www.instagram.com/abhinav06.sh/

LinkedIn- https://www.linkedin.com/in/abhinav-kumar-6946b3221/

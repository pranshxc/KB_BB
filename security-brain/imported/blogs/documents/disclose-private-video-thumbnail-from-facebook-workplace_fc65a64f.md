---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-03_disclose-private-video-thumbnail-from-facebook-workplace.md
original_filename: 2018-05-03_disclose-private-video-thumbnail-from-facebook-workplace.md
title: Disclose Private Video Thumbnail from Facebook WorkPlace
category: documents
detected_topics:
- idor
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: fc65a64fd0361335e11fa0786b880aabe6eb585681104fdb045fb902eb2e7b08
text_sha256: fefa4f6073daa816b30b2b566bdb7cef4d66b474ca00043c6548d731bf26a15b
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose Private Video Thumbnail from Facebook WorkPlace

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-03_disclose-private-video-thumbnail-from-facebook-workplace.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `fc65a64fd0361335e11fa0786b880aabe6eb585681104fdb045fb902eb2e7b08`
- Text SHA256: `fefa4f6073daa816b30b2b566bdb7cef4d66b474ca00043c6548d731bf26a15b`


## Content

---
title: "Disclose Private Video Thumbnail from Facebook WorkPlace"
url: "https://medium.com/bugbountywriteup/disclose-private-video-thumbnail-from-facebook-workplace-52b6ec4d73b7"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "3,000"
publication_date: "2018-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5890
scraped_via: "browseros"
---

# Disclose Private Video Thumbnail from Facebook WorkPlace

Disclose Private Video Thumbnail from Facebook WorkPlace
Sarmad Hassan (Juba Baghdad)
Follow
5 min read
·
May 4, 2018

498

1

Press enter or click to view image in full size

Hello guys, It’s me again Sarmad Hassan (JubaBaghdad), I would like to share with you my second bug that I found in Facebook through their BugBounty Program.

The story began when I decided to test Facebook pages, because I knew through reading a lot of write ups, that Facebook pay good bounty when hunters find valid bugs on Pages.

So as usually, I created a Test Page for me and I checked every option on it to see if I can find something interesting or even a juicy info. that may leads me to valid bug.

After a little while an option called CANVAS brought my attention, Basically Page Admin or even an advertiser can create CANVAS and there is some options like upload photo or video inside of it

Press enter or click to view image in full size

so I uploaded my test video and I save it, then I edited the CANVAS that I created, After that I changed the title of canvas and then Intercept it with Burpsuite to see the mechanism of this canvas and what kind of parameters inside of it, the request was as below:

POST /v2.11/{My_Page_ID}?access_token={My_page _Access _Token} HTTP/1.1
Host: graph.facebook.com
User-Agent:
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.facebook.com/
Content-type: application/x-www-form-urlencoded
Content-Length: 206
Origin: https://www.facebook.com
Connection: close

_reqName=object%3Acanvas_video&_reqSrc=AdsCanvasElementDataLoader&bottom_padding=0&locale=en_US&method=post&name=Video&pretty=0&style=FIT_TO_WIDTH&suppress_http_code=1&top_padding=0&video_id=956034724555363

so as you can see above there is a parameter called video_id={id of video}, which is responsible for the video that I uploaded in my canvas

once I saw that parameter, I directly opened my second Test account in my virtual box, I made a post and uploaded a test video, and I copied the (video_id) number

it was like: video-id=130146294495198 and replace it in the video_id={id of video} mentioned above, and boooooooooooom, video uploaded successfully in my page CANVAS, the response was as below:

Press enter or click to view image in full size

so I was able to upload in my CANVAS through the “video id number” any public video from users that not friend with me and any video from my friends posts, if they set the post privacy as “for friends only”

and because we have an IDOR bug in the (video_id=) parameter, which means both videos, My Canvas’s Video and My second test account’s Video have the same video_id number, so I said if I delete my Canvas video the video in My second Test account post will be deleted too, cause logically both of them have the same video_id number, but unfortunately it didn’t work and I was like:

hmmmm, what should I do now, ok let’s think outside the box, I have to turn this Bug from N/A to a valid Bug.

Next day Facebook workplace sub-domain came into my mind, and because I know that every post in Facebook workplace consider as private, like photos or videos, because only members of a company with the same email domain should have see their posts.

So I made a video post in my Workplace test account to see if I can disclose the video (through the video_id) using the CANVAS IDOR bug, I copied the (video_id) number video_id=168712210608619 from my workplace post and replace it in my request mentioned above, and boooooom, the response was as below:

Press enter or click to view image in full size

after that I refreshed the page and clicked on view option to see if I can view the video (video from my workplace account), but again I couldn’t see the video but I noticed something interesting see the below photo :

Press enter or click to view image in full size

as you can see in the photo above, there is a spinning icon for the video, which means the video is uploaded successfully but there is something blocking it to be previewed, and I said to myself I’m really sooooo close and I have to bypass this shit

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

within minutes and while smoking my cigarette an idea came to my mind and I said what if I send my canvas to my Smart Phone (because there is an option to send a preview of your canvas to your mobile device) see the below photo:

Press enter or click to view image in full size

Once I sent the canvas to my Smart Phone, I received a notification in my phone telling me “ your canvas is ready to preview”, I clicked on it and booooooooom, I saw the video in my device.

Press enter or click to view image in full size
Press enter or click to view image in full size

but I couldn’t play the whole video, I was only able to see Video Thumbnail , I was like:

I reported this bug directly to Facebook Security team, because I knew it is a valid bug, why !! well (from my perspective) Facebook workplace is designed for organization or companies and as I mentioned above every post in workplace consider as private and only members of the company or the organization should see their contents, ability to see the video thumbnail in workplace post consider as a security issue, cause imagine these videos contain private information like meeting places, private emails, private titles for the company like prices, budgets, products sales figures or any private info. that should not be visible to the public not to mention private content of the video itself.

Timeline:
March. 30, 2018 — Initial Report
April. 05, 2018 — Report Triaged
April. 10, 2018 — Fixed By Facebook
April. 10, 2018 — Fixed Confirmed
May. 03, 2018 — Bounty of $3000 awarded

I would like to thanks Facebook Security Team for the Bounty, thank you guys

PoC Video:

Takeways:

1- you have to know your target and to check every option on it.

2- Sometimes you need to think outside the box.

3- Always make sure your bug can effect on the App.’s users or its system

4- Always focus on video and photo ID’s, there is a chance to see a flow out there

5- Most important thing “ JUST HAVE FUN” when you pentest.

Thank you

Sarmad Hassan (JubaBaghdad)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-23_un3xpected-dos-attack-on-profile-pictur3.md
original_filename: 2022-07-23_un3xpected-dos-attack-on-profile-pictur3.md
title: Un3xpected DoS Attack on Profile Pictur3
category: documents
detected_topics:
- command-injection
- file-upload
tags:
- imported
- documents
- command-injection
- file-upload
language: en
raw_sha256: 3fb13ec36728f646541575f08e214b055f208ef46901e5e32a0b63d6bab64487
text_sha256: 131484ae6c8ab1469029064e231b5893fa1b8e92d2a9046d4d1b653821defba4
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Un3xpected DoS Attack on Profile Pictur3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-23_un3xpected-dos-attack-on-profile-pictur3.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `3fb13ec36728f646541575f08e214b055f208ef46901e5e32a0b63d6bab64487`
- Text SHA256: `131484ae6c8ab1469029064e231b5893fa1b8e92d2a9046d4d1b653821defba4`


## Content

---
title: "Un3xpected DoS Attack on Profile Pictur3"
url: "https://infosecwriteups.com/un3xpected-dos-attack-on-profile-pictur3-b957979dcc7"
authors: ["Roxst4r (@mveswar98)"]
bugs: ["DoS"]
bounty: "100"
publication_date: "2022-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2412
scraped_via: "browseros"
---

# Un3xpected DoS Attack on Profile Pictur3

Un3xpected DoS Attack on Profile Pictur3
Roxst4r
Follow
3 min read
·
Jul 23, 2022

71

1

Hey Everyone, Hope y’all doing Great and aw3some!

Press enter or click to view image in full size

Okayyyy - First of all, I wanted to say everyone that I prefer to publish Write-ups that are unique and something strange that may help you along the way of Bug Hunting and not something cliche, so I think that this Write-up may not bore you with regular stuffs instead help you with some insights during your hunting( so keep reading ;] ). I’m not a complete bug hunter with all the knowledge, just a random bug hunter with imperfect ideas on bug hunting so please pardon the technical mistakes if any.

- The Bug -
When I try to upload a Pixel Image in profile picture, just like every secure web application — I got a error pop-up not allowing me to upload the pixel image
Then I tried uploading files with various extensions as well like php, .php.jpeg, .svg and other possible extensions to bypass it — Which failed as well
Tried intercepting with Burp suite and did all the testing by changing the extension and everything — which probably failed as well
Then I almost got fedup by doing all these testing and not getting anything from it. Actually this was the first time I tried to bypass a file upload so I tried pretty much everything on the way with the knowledge that I acquired from various writeups, blogs and videos.

Till this time I was thinking that I need to do something complex to find a bug like this and tried all the above method. Now the solution that I got was as simple it could be..,

The Solution
Just like a normal user would do, I uploaded a valid image as the profile picture but I did not click on “Set New profile Picture”
Instead I tried uploading the lotta pixel image now by clicking “Choose file” and then clicked “Set New profile Picture”
Which caused Application Level DoS and the page became unresponsive when I tried from other browsers as well
To increase the impact, I once again tried with svg, php and other extensions but it was not possible
For the whole time I was thinking to find a bug with complex things and at the end it was as a simple thing that made this happen
Steps to Reproduce
First upload a valid image and don’t click Set New profile picture
Now without closing the window upload this lottapixel.jpg file by clicking choose file
Now when you set this as new profile picture, the page becomes unresponsive.

Since it was only a DoS Attack and it was mentioned “Out of Scope” the program was kind enough to reward me with $100 for this issue.

So that’s all about the bug, glad to share my knowledge and give back to the community — If there is any mistake above, please do correct me and if there is any doubt please do contact me.

Get Roxst4r’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Twitter — https://twitter.com/mveswar98

~Thank you!

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE! https://weekly.infosecwriteups.com/

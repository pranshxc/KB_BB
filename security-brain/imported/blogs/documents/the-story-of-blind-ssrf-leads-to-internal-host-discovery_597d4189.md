---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-01_the-story-of-blind-ssrf-leads-to-internal-host-discovery.md
original_filename: 2020-05-01_the-story-of-blind-ssrf-leads-to-internal-host-discovery.md
title: The Story of Blind SSRF leads to internal Host discovery.
category: documents
detected_topics:
- automation-abuse
- idor
- ssrf
- command-injection
- file-upload
- rate-limit
tags:
- imported
- documents
- automation-abuse
- idor
- ssrf
- command-injection
- file-upload
- rate-limit
language: en
raw_sha256: 597d4189795e5f46d8a4dec67e4765829f47bc4ccccb435b18eef3fd8a28670e
text_sha256: dc3652d71b2c5d7b5a8069d58ae10c14ad6b735f37055f0b22bc8e8e23cf5619
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# The Story of Blind SSRF leads to internal Host discovery.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-01_the-story-of-blind-ssrf-leads-to-internal-host-discovery.md
- Source Type: markdown
- Detected Topics: automation-abuse, idor, ssrf, command-injection, file-upload, rate-limit
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `597d4189795e5f46d8a4dec67e4765829f47bc4ccccb435b18eef3fd8a28670e`
- Text SHA256: `dc3652d71b2c5d7b5a8069d58ae10c14ad6b735f37055f0b22bc8e8e23cf5619`


## Content

---
title: "The Story of Blind SSRF leads to internal Host discovery."
url: "https://medium.com/@rooterkaustubh/the-story-of-blind-ssrf-leads-to-internal-host-discovery-ee65b9b91e23"
authors: ["kaustubh padwad (@s3curityb3ast)"]
bugs: ["SSRF"]
publication_date: "2020-05-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4618
scraped_via: "browseros"
---

# The Story of Blind SSRF leads to internal Host discovery.

The Story of Blind SSRF leads to internal Host discovery.
Kaustubh Padwad
Follow
5 min read
·
May 1, 2020

105

1

Background

After reading a Lots of tweets on SSRF, I have decided to test for only SSRF for bug bounty. Generally I work on Synack platform due to precise scope and response time. I Love Hackerone also but due to limited resource and lack of automation I fails/hate to to do lots of discovery stuff. whether its a content discovery or assets discovery I hate both lol. Because sometimes it take too long on my intel Core i5 with 16 GB and 20MBPS connection just to discover a assest/content, Hence I prefer to have a defined scope for testing so that I can spend more time on or sharpening the my testing skills than Discovery skills.

Approach

Since on this platform also there are many targets and many skilled researcher hence you have to be very specific while selecting targets, its really hard to believe that the bug submitted after 20 Mins of target getting Live can be dup and the bug identifier says your bug id is targetname-13

So that’s different pain altogether. Also when selecting target on Synack you have to keep few things in mind which hurts a lot to bug bounty hunters later you get used to it..

“ PoC || GTFO “ if you use words like potential or which can be used, or attacker can later, this means your bug is rejected.
“Out Of Scope” is much wider than that acceptance criteria.
Low hanging fruits a best describe in one picture..
Don’t get surprise if bugs which pays nice $$$ on other platform gets rejected
Technology stack is extremely out of box… some times it takes too long to understand.
Scope… You have to be in scope. it doesn’t matter whether you get RCE is on other subdomain or OOS endpoint ;)

So keeping all above things in mind I am almost sure every time that either I have to find out of box or something obvious which is missed by the our highly skilled Synack Red Team members.

keeping everything in mind,I always select target which is having Blitz

because as you know you are going on war, where you are not sure that whether you can return or not then choose the toughest target to defeat.

Assessment

So i have selected the target which has blitz and the last vulnerability reported to that was 3 Month ago so I took this as a good luck and started. After application mapping,content discovery, and complete enumeration of target i started fuzzing every parameter for SSRF sounds silly but yes only SSRF.

On this target there was an excel parsing so first thing came in mind is to achieve SSRF via XXE via file upload so created a xls file with basic payload and uploaded to application and waited for few times but no luck, then multiple manipulated payloads was loaded and uploaded but still no luck..

Then gave up on this option.

This also dint works as all the parameter were nicely sanitize.

Wait.. Something is there..

So when I was fuzzing the application with some not obvious values like -10. it was making a call to /api/sentry.

Hmmmm lots and lots of parameters are here.. and smells something good here so request was looking like this.i have changed the parameter filename with my burp colab client id.

Get Kaustubh Padwad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And i was Hopelessly looking at my colab client and what its unbelievable I saw the request from xxx.xxx.xx.xx to my colab clinet

so took the request in repeater and again played it but no luck then took again took many of the recent request to the repeater and tried to play again but no luck

first I though may be a sequence of request might be matter like first it was making OPTION request to /api/sentry and then it was doing post request so tried that but no luck
Then I think, Out of many sentry request only few request might have power to make SSRF, so again started from scratch and again i am able to see one request only after repeater again there is no SSRF.
Then i started comparing bit-by-bit in 2,3 requests

And come to know that all request was being track by “event_id”The moment i changed the character from It again hit my colab client

Setting the attack

I have sent the below request to Intruder.

Getting the Payloads

Now click on burp and burp collaborator client it will open the collaborator window Click on number to generate change it to 50 and click on copy to clip board.

Final Attack setup

Now navigate to our attack and select position window here select the two position one is filename parameter and second is event_id parameter. now it will looks like below

"filename":"https://§x422hnxyxutjb4dsi0yne38b72dt8hx.burpcollaborator.net§" event_id":"§bd60122cedbd41728414a0f6400db3e1§"

And now move to payload window in payload set 1 select payload type simple list and paste the URLS which we got from collaborator client and in payload set 2 select bruteforcer in that Change minimum length from 4 to 32 and max length to 32

And Now start The attack….

As soon as I did started the attack I got many request on my client

Press enter or click to view image in full size

After final analysis i came up with 25 Internal amazon IP address so from where the request was made.

So Looks nice I go ahead and reported this Bug to the platform, And Guess what this is declared as As OOS.

Then we have some small conversation over this is valid bug blah blah provided some references

But Finally Platform wins they categorize this into two part

1. Info disclose which is internal IP that was low-impact

2. if we fires millions of request towards any target then its DDOS which is OOS.

During the same time old report 3 Bugs which is having CVSS 9/10 got dups.. and then decided to stop hunting for a while and do other stuff.

Hope you love reading this….

Originally published at https://www.breakthesec.com.

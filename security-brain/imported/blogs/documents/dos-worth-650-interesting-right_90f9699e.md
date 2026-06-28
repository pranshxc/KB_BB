---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-25_dos-worth-650-interesting-right.md
original_filename: 2022-07-25_dos-worth-650-interesting-right.md
title: DoS worth $650 ? Interesting right!
category: documents
detected_topics:
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 90f9699ede2afebf883ce33c11e095ef3f9c405015b92b115f498a6827dd580c
text_sha256: 8bdebbb501125c44322c46fc28ac25d80e2579b82feee0593e30a5b9aeb9bc09
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# DoS worth $650 ? Interesting right!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-25_dos-worth-650-interesting-right.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `90f9699ede2afebf883ce33c11e095ef3f9c405015b92b115f498a6827dd580c`
- Text SHA256: `8bdebbb501125c44322c46fc28ac25d80e2579b82feee0593e30a5b9aeb9bc09`


## Content

---
title: "DoS worth $650 ? Interesting right!"
url: "https://sagarsajeev.medium.com/dos-worth-650-interesting-right-144ff45ccf3b"
authors: ["Sagar Sajeev (@Sagar__Sajeev)"]
bugs: ["DoS", "Pixel flood attack"]
bounty: "650"
publication_date: "2022-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2403
scraped_via: "browseros"
---

# DoS worth $650 ? Interesting right!

DoS worth $650 ? Interesting right!
Sagar Sajeev
Follow
3 min read
·
Jul 25, 2022

205

3

Hey Guys, my name is Sagar Sajeev. This is my second writeup and I would like to share how I was rewarded with a bounty of $650 for a Pixel flood Attack (which crashed the target server and caused an application level DoS.)

A pixel flood attack is when you upload a very large image (image with huge amount of pixels or very large width and height), it allocates the pixels into huge heap of server memory, flooding it and ultimately crashing the server and causing an application level DoS.

I have been hunting on a private program for a while now and have reported around 6 valid vulnerabilities (More interesting writeups loading⚡). Since I can't reveal the program name ,let’s call it redacted.com.

Lemme put a disclaimer here…

Most of the times, DoS will be out of scope. No one wants their website down. So make sure you go through the Terms of the program carefully and attempt this only if you have got explicit permission. I’m not responsible for your actions in any way.

How to find this specific vulnerability?

Locate the file upload functionality in your target site.

Note — This is only a sample image.

Choose the image which you are about to use as the payload with the dimensions or pixels as 64000*64000 (Height ,Width). Many such preset images are available online or you can manually change the pixel ratio of images using various software and online services. A sample of such an image is shown below.

Note — Image only for reference. Not the actual Payload image.

Upload the image. Notice if the website starts to slow down in any way or acts sluggish. Or Did you get a 503 or any 5XX? You know what it means :-)

Bonus Tip

If the website has got a very good backend support, it may not slow down to such an extend, however to prove the impact in the PoC ,we can take reference of the response time in Burp before uploading the image and after uploading it. For this, Sent req to Repeater tab and click go →Right bottom corner will have something in ms.(Take it this way, High ms → Server is having an hard time).

Timeline

Submitted : 02–07–2022

Get Sagar Sajeev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Accepted : 03–07–2022

Resolved : 07–07–2022

Bounty Rewarded : 08–07–2022

Well, I hope you have learned something new today. This is my 2nd writeup. You can find my first writeup here. I’m working on a few more interesting writeups which will be published soon.

I do occasionally share some tips about Bug Bounties and related stuff over at my Twitter and LinkedIn handle. So do follow me there. If you’ve got any queries, feel free to message me. I will be more than happy to help.

LinkedIn : https://www.linkedin.com/in/sagar-sajeev-663491208/

Twitter : https://twitter.com/Sagar__Sajeev

Happy Hunting!

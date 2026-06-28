---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-07_sending-out-phishing-e-mails-from-microsoftcom.md
original_filename: 2018-08-07_sending-out-phishing-e-mails-from-microsoftcom.md
title: Sending out phishing e-mails from @microsoft.com
category: documents
detected_topics:
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 5dbfb327efeeba3552ebbcf4d1cdb19e69a3ed1926172e6b9cb95f82f08d50a4
text_sha256: e7a89ece576e1be2344d671bcd6166e0c41b716715383e91f1c1cea68807e687
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Sending out phishing e-mails from @microsoft.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-07_sending-out-phishing-e-mails-from-microsoftcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5dbfb327efeeba3552ebbcf4d1cdb19e69a3ed1926172e6b9cb95f82f08d50a4`
- Text SHA256: `e7a89ece576e1be2344d671bcd6166e0c41b716715383e91f1c1cea68807e687`


## Content

---
title: "Sending out phishing e-mails from @microsoft.com"
url: "https://medium.com/bugbountywriteup/sending-out-phishing-e-mails-from-microsoft-com-84c3b918ada2"
authors: ["SI9INT (@si9int)"]
programs: ["Microsoft"]
bugs: ["HTML injection"]
publication_date: "2018-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5768
scraped_via: "browseros"
---

# Sending out phishing e-mails from @microsoft.com

Sending out phishing e-mails from @microsoft.com
SI9INT
Follow
4 min read
·
Aug 7, 2018

235

Einstein was right! (Probably)

This is a short writeup about a vulnerability I reported to microsoft.com two months ago, describing a HTML injection issue affecting one of their services called “Microsoft Stream”. Since the vulnerability won’t be patched, quote:

Gaurav:

“MSRC is no longer tracking this due to its severity and impact. We have closed this case.”

I’m gonna describe the details and the impact on the customer for educational purpose. This issue is still unpatched and could be exploited or further researched.

It was a rainy evening and I though I might give the Microsoft bug-bounty program a try. After preparing my toolset (some custom Python-scripts, Burpsuite and a local webserver used for documentation) I logged myself into an old Microsoft-account and searched for a target.

stream.microsoft.com

Never heard of, never used it, never heard anybody using it, sounds good! And it was indeed good. Good programmed using REST-ful API’s (depending on your location: EU, Asia, US) to communicate via XMLHttp-based requests to a token-secured with different authentication-headers equipped backend architecture which validated every char of my request. “No way this application is insecure” I thought to myself.

My methodology is always the same, on every target I try to follow these global steps to ensure some success:

Reconnaissance (to huge to go into detail here)
Determine the correct application-logic
Try to bypass the application-logic in any way (not only security-related)
Take note about “bugs” aka application-errors
Try to expand this functional errors “bugs” to security related issues
Try to exploit these security issues
Try to prove some impact (low; medium; high)
Try to expand the impact by chaining different issues or bugs (heterogeneous)

In the case of “Microsoft Stream” I was greeted with “thousands” of parameters and different API’s so I focused on the file-upload, the core-function. After understanding the logic behind the different parameters I used my Python-fuzzer (probably will it release soon; github.com/si9int) to fuzz the different parameters displaying correlations or differences between valid and invalid input based on the HTTP response and the request-time.

Get SI9INT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I hammered the backend by using different strings and payloads referring different attack vectors and noticed two (later) important things:

HTML is accepted by the API but rendered back encoded, e.g.: <h1>Hello world!</h1>is a valid string for a video-title
Unicode is being interpreted by the API which allows to inject different spaces and whiteblocks disregarding the char-limit (1 Unicode = 1 Char)

But yeah, no reflection no anomaly or any error disregarding the correct and flawless error-handling pumped up with JavaScript functionality. I lost the game, time-wasted, no motivation and went to bed.

The morning after I sat to to my desk and checked my e-mails (as I do mostly every day). * Sigh* I got a lot of new mails all from no-reply-stream@microsoft.com describing that my uploaded video was rendered successfully “bla bla”. Then I noticed something and my stair began to rotate 360 degrees. The title <h1>Hello world!</h1> was being executed, the HTML being rendered inside the e-mail.

BOO(O)OOM!

Jackpot (kinda…; for me it was after the waste of time). I immediately revisited the edit-video page, re-checked the “Share your video” functionality and crafted a proof of concept and submitted it to the “Microsoft Security Response Center”:

Press enter or click to view image in full size
Well yeah.. It was quick and dirty..

I found a valid bug on a top notch coded Microsoft service! Abusing a @microsoft.com domain for phishing purposes. The feeling was incredible

* Try to feel what I felt, let it take effect *

until Gaurav moved my report to N/A.

Ah yeah.. They argued that the mail was named after the payload and therefore it was easy to spot the phishing attempt. I lost my motivation and kicked the mail to /archive.

The next days I was talking with a fellow student of mine about the incident and remembered the char limit. After I went from university to my home I immediately re-checked the issue and crafted a new PoC:

'''Hi loveley lady, it’s microsoft\u0020\u00a0\u0020\u205f\u0020\u205f\u00a0\u0020\<h1>HACKED AND ABUSED</h1>'''

It worked! The combination of whiteblocks and spaces pushed my payload to the right of the sidebar (I was using an instance of “Microsoft Outlook”) , showing only the “legit” title of the e-mail.

Although the guys on Microsoft doesn’t saw any security impact and notified me again that the vulnerability is classified low and won’t be fixed. I don’t think this is a good idea because there might be more to discover and break the actual HTML context, spoofing the HTML itself. This method could be also used to craft extremely efficient spear-phishing mails, whatever.

You can read the original report here (I’ve added second PoC out of the e-mail conversation): https://si9int.sh/view/9/

I hope you enjoyed this short article, feel free to question me at:

SI9INT (https://twitter.com/si9int)

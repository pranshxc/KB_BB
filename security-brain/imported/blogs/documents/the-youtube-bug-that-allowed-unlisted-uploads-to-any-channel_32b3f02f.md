---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-27_the-youtube-bug-that-allowed-unlisted-uploads-to-any-channel.md
original_filename: 2020-10-27_the-youtube-bug-that-allowed-unlisted-uploads-to-any-channel.md
title: The YouTube bug that allowed unlisted uploads to any channel
category: documents
detected_topics:
- sso
- idor
- command-injection
- file-upload
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sso
- idor
- command-injection
- file-upload
- automation-abuse
- information-disclosure
language: en
raw_sha256: 32b3f02f67065930430ceebaf76c9077011d4b95044fc21070bf2fd404d6709d
text_sha256: f0d7ca5e5537cf68a7c5105cddb3fb944ab730c0a61d3b4af577302bc83fb248
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# The YouTube bug that allowed unlisted uploads to any channel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-27_the-youtube-bug-that-allowed-unlisted-uploads-to-any-channel.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, file-upload, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `32b3f02f67065930430ceebaf76c9077011d4b95044fc21070bf2fd404d6709d`
- Text SHA256: `f0d7ca5e5537cf68a7c5105cddb3fb944ab730c0a61d3b4af577302bc83fb248`


## Content

---
title: "The YouTube bug that allowed unlisted uploads to any channel"
page_title: "$6k bounty: unlisted upload to any YouTube channel | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/the-youtube-bug-that-allowed-uploads-to-any-channel-3b41c7b7902a"
authors: ["Ryan Kovatch"]
programs: ["Google"]
bugs: ["IDOR", "Information disclosure"]
bounty: "6,337"
publication_date: "2020-10-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4177
scraped_via: "browseros"
---

# The YouTube bug that allowed unlisted uploads to any channel

The YouTube bug that allowed unlisted uploads to any channel
Ryan Kovatch
Follow
5 min read
·
Oct 27, 2020

175

It was late June when I received an invitation to test out a new product from YouTube: a video building tool that made it easy to put together advertisements with custom fonts and logos.

Press enter or click to view image in full size
The email I got notifying me of the beta.

I don’t know where they got my information — I must have touched every Trusted Tester form on the web — but it presented an opportunity. New products aren’t usually as hardened against attacks. When I tried logging into the website a day after requesting access, to my surprise, it let me in. (Strange, since I hadn’t gotten any sort of notification like they said I would.)

The tool is pretty basic, and it works like this: you choose a template, customize it with colors, photos, and text, and then the server renders it for you. To see how it works better, I opened my swiss army knife of debugging proxies: Charles. Then I watched the traffic go through as I followed the steps.

Nothing particularly stood out to me at first — the file upload feature was secure, they used long encrypted strings to identify resources, and all the fields were sanitized. Bummer. But then I reached the final step and noticed something.

Press enter or click to view image in full size
The upload screen of the video builder.

There’s a menu that allows you to choose from the channels associated with your Google account, and beneath that, a small disclaimer: your video will be saved to your channel as “Unlisted.” So the server was both rendering and uploading the video, and it was giving me the option to choose a channel to upload to. This set off alarm bells. I had to know how it worked.

Every channel on YouTube has its own ID that usually looks like this: UCxXX0xx_X0XxxXXxxxx00Xx. You can usually find them in a channel URL or the source of any video page. When I went back to see how the site was getting the YouTube channels on my account, I found a response from the server that looked like this:

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
  "1": [{
  "1": "UCBCW8XFPYIENZPC659Pk0kg",
  "2": "Ryan Kovatch",
  "3": "https://yt3.ggpht.com/a/..."
  }]
}

There was my channel ID. Then I hit “Save” to see what would happen.

POST /u/0/videobuilder/_/rpc/Image2VideoUiService/UploadToYouTube HTTP/1.1
Host: director.youtube.com
Content-Length: 483
Content-Type: application/x-www-form-urlencoded
__ar=%7B%221%22%3A%7B%221%22%3A%22AFbu1Vq...%22%7D%2C%222%22%3A%22UCBCW8XFPYIENZPC659Pk0kg%22%2C%223%22%3A%221%22%2C%224%22%3A%22Created+with+YouTube+Video+Builder+using+template+%5C%22Introduce+your+brand+%286s%29.%5C%22%22%2C%225%22%3A%222755bb19-6e4b-4cd4-beca-46cc29f26625%22%7D

A form request. Decoded, the value of __ar was:

{
  "1":{
  "1":"AFbu1Vq..."
  },
  "2":"UCBCW8XFPYIENZPC659Pk0kg",
  "3":"Main message",
  "4":"Created with YouTube Video Builder using template \"Introduce your brand (6s).\"",
  "5":"2755bb19-6e4b-4cd4-beca-46cc29f26625"
}

Yep, there was my channel ID. Alongside it were the title, description, and template ID. When I figured this out, my first move was to swap it with the channel ID of my test account. And then…

HTTP/1.1 200 OK

Boom. The server returned an ID to track the progress of the upload, and then I got a link to it on YouTube. Sure enough, it was uploaded as an Unlisted video to a channel I didn’t own. I reported it right away.

Then I got this email right after, which — okay.

Press enter or click to view image in full size
Oh no way, really?

And then I went to bed.

The next day

Lots of movement happened in the early hours of the morning. My report had seemed to cause quite a stir.

First, at 6 AM.
And then 30 minutes later.

I woke up to a “Nice catch!” in my mailbox. It prompted me to actually think through the implications of an issue like this — on a platform like YouTube, it would catalyze the spread of misinformation. The kind of stuff that sways elections and threatens democracy. I had to dig deeper.

Get Ryan Kovatch’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this point, the limitations were that a.) I could not upload a video publicly and b.) I could only upload videos created by the site, not my own. The root issue was plenty harmful, but if I could figure out how to bypass these, it would be considerably more serious. So I revisited the UploadToYouTube function.

{
  "1":{
  "1":"AFbu1Vq..."
  },
  "2":"UCBCW8XFPYIENZPC659Pk0kg",
  "3":"Main message",
  "4":"Created with YouTube Video Builder using template \"Introduce your brand (6s).\"",
  "5":"2755bb19-6e4b-4cd4-beca-46cc29f26625"
}

That identifier? It’s an encrypted string containing information about the video file. (It’s actually much longer.) I would later learn that this is called a scottyResourceId, and it’s used all over YouTube to identify data that’s uploaded to their servers. An idea popped into my head: What if I could upload a file to another YouTube site, pull the resource ID from there, and use it in this API instead? That would allow me to upload a custom video and point the server to it.

I pulled up YouTube Studio and uploaded a test file. The server responded with this:

HTTP/1.1 200 OK
X-GUploader-UploadID: ...
X-Goog-Upload-Status: final
Content-Length: 405
Server: UploadServer
Connection: keep-alive
{
  "status":"STATUS_SUCCESS",
  "scottyResourceId":"ACKujmz..."
}

Bingo! This ID started with ACK, but was just as long as the other one. I sent a new UploadToYouTube request to the video builder, this time with the ID from YouTube Studio, and… got an error.

com.google.apps.framework.request.CanonicalCodeException:
com.google.security.keymaster.KeyUnavailableException:
No matching decryption key found; ciphertext had key hash XXYYZZ but no key version matched it; existing versions:keyhashes are 1:YYZZXX, 2:ZZXXYY, 3:YYXXZZ, 4:XXZZYY, see go/key_unavailable_exception.
Code: PERMISSION_DENIED

So it didn’t work. But exceptions like this can actually be more severe issues than the functionality they prevent. In this case, the server had tried to decrypt the resource ID, but since it was from another server, it couldn’t find the right decryption key to use. When the exception was raised, it included the hashes of all the keys it had stored. This was a critical data leak.

I reported it and got another “Nice catch!” Further research around changing the video from unlisted to public wasn’t successful, so I stopped there.

Conclusion

Even the biggest players in the game are prone to bugs like this. Sometimes they’re more obvious, and sometimes they’re trickier to find, but they’re there. I hope this first write-up of mine is helpful to anyone trying to find a way to their first bug bounty, or maybe already has a few under their belt. There’s no such thing as an impenetrable application.

Timeline
All times are in PST.
Received invitation June 22 @ 9:53 AM
Reported first bug June 23 @ 10:44 PM
Triaged as P1 June 24 @ 6:10 AM
“Nice catch!” and escalated to S1 June 24 @ 6:40 AM
Reported second bug June 24 @ 6:09 PM
“Nice catch!” and escalated to P2S2 June 25 @ 2:02 AM
Panel awards $6,337 bounty July 2 @ 11:20 AM
Both bugs are confirmed as fixed October 16 @ 3:01 PM

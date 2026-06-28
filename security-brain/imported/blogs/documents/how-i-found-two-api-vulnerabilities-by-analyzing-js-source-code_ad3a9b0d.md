---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-28_how-i-found-two-api-vulnerabilities-by-analyzing-js-source-code.md
original_filename: 2023-07-28_how-i-found-two-api-vulnerabilities-by-analyzing-js-source-code.md
title: How I found two api vulnerabilities by analyzing JS source code
category: documents
detected_topics:
- access-control
- api-security
- sso
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- api-security
- sso
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: ad3a9b0deb8eb6fa7aa26c7a46b0e31fb1110d5d2a08ef53089bda0c2227a412
text_sha256: 34bea820ff60a8c1d94fb9ead88f3b22648fc9a4469e84e098367ac33352faed
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# How I found two api vulnerabilities by analyzing JS source code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-28_how-i-found-two-api-vulnerabilities-by-analyzing-js-source-code.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sso, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `ad3a9b0deb8eb6fa7aa26c7a46b0e31fb1110d5d2a08ef53089bda0c2227a412`
- Text SHA256: `34bea820ff60a8c1d94fb9ead88f3b22648fc9a4469e84e098367ac33352faed`


## Content

---
title: "How I found two api vulnerabilities by analyzing JS source code"
url: "https://medium.com/@mohammed0x04/how-i-found-two-api-vulnerabilities-using-website-source-code-6c4b0dc54d6f"
authors: ["Mohammed Waleed"]
bugs: ["IDOR", "Broken Access Control"]
publication_date: "2023-07-28"
added_date: "2023-07-31"
source: "pentester.land/writeups.json"
original_index: 898
scraped_via: "browseros"
---

# How I found two api vulnerabilities by analyzing JS source code

Top highlight

How I found two api vulnerabilities by analyzing JS source code
Mohammed Waleed
Follow
4 min read
·
Jul 27, 2023

1K

11

Hello everybody, my name is Mohammed Waleed, I’m a beginner bug hunter and web developer and today I will share with you how I found two api bugs on a private bug bounty program by analyzing website source code and how you can also use source code and JS files to find vulnerabilities, let’s get started!

since the target is a private program on hackerone and I can’t disclose any information about it, I will call it target.com.

the scope of the target wasn’t very big and consisted of only one wildcard domain(*.target.com), after doing some recon I decided to start hunting on the main application, I found that the website is using react framework.

I wanted to see if the source code was available so I opened the sources tab in chrome DevTools and I found a folder called web-app that contained the frontend source code of the website!

I immediately downloaded it to start reviewing the code and find some vulnerabilities.

I downloaded the code using a chrome extension called resources saver, you’ll find it here:

Resources Saver Extension

I started to manually review the code and because I love api hacking I started looking for api endpoints inside the JS files and I found a folder called api that contained files with a lot of api endpoints for both their web and mobile application.

as I always do with api’s, I saved all api endpoints I found in an excel sheet and started analyzing/testing them one by one, understanding their purpose and what they do in the application.

after a lot of testing I found two access control vulnerabilities using two endpoints.

1) Adding and deleting buttons on any video on target.com:

there was a feature in target.com to upload a video, and when I was testing the api endpoints from the source code I found this endpoint

/v1/videos/<video_id>/cta

in the source code the function looked like this:

export function updateCTA(videoId: string, ctaURL: string, ctaText: string) {
  return getResults(
  appendQuery(`${TARGET_API_URL}videos/${video_id}/cta`, {
  api_key=***REDACTED***
  link: ctaURL,
  text: ctaText,
  }),
  {
  method: ctaText ? 'put' : 'delete',
  }
  )
}

it was weird to me that it didn’t require any authorization headers/parameters other than the web api key, because the web api key is the same for all users, I knew that after I made multiple accounts and found that the api key is the same in all accounts.

I didn’t know what this endpoint was doing exactly so I crafted a PUT request in burp repeater to test it.

inside ${video_id} I added a video id that belongs to a video I uploaded.

Get Mohammed Waleed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I sent the request and it was accepted!

Press enter or click to view image in full size

I still don’t know what this request is doing so I opened the video and I found a button under it that redirects you to a website if you click it.

I was also able to delete it by making a DELETE request.

this means I can add/delete a link to any video on the website without any user interaction!

and it was accepted and triaged:

Press enter or click to view image in full size

the strange thing is that I didn’t find anything that allows you to add links when uploading a video, so this feautre is probably not available in the application anymore, or maybe available for specific account types or something.

2) view stickers associated with a private video:

there was a feature to upload a special kind of videos that allows you to add stickers to the video

I found this api endpoint:

v1/videos/<id>/associations

I found that it allows you to view stickers associated with a video

I uploaded a private video with stickers, then I tried to view associated stickers using another account.

the request was accepted and I was able to see all stickers associated with the private video!

Press enter or click to view image in full size

unfortunately, the report was closed as informative since the impact is very low.

reviewing source code and finding vulnerabilities in it will give you an advantage because only a few bug hunters do it, and it will get you a lot less duplicates.

here are three writeups that helped me a lot on how to get started in source code review and analyzing JS files:

Javascript for bug bounty hunters — part 1
As of today, I’ll start a series of articles targeting javascript files and it’s importance from a bug hunter…

bitthebyte.medium.com

Javascript for bug bounty hunters — part 2
This is a follow up to https://medium.com/@bitthebyte/javascript-for-bug-bounty-hunters-part-1-dd08ed34b5a8

bitthebyte.medium.com

Javascript for bug bounty hunters — part 3
This is a follow up to https://medium.com/@bitthebyte/javascript-for-bug-bounty-hunters-part-2-f82164917e7

bitthebyte.medium.com

Happy Hunting!

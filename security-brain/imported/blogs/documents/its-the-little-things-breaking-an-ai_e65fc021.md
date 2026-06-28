---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_its-the-little-things-breaking-an-ai.md
original_filename: 2022-10-13_its-the-little-things-breaking-an-ai.md
title: 'It’s the Little Things : Breaking an AI'
category: documents
detected_topics:
- command-injection
- path-traversal
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- information-disclosure
- api-security
language: en
raw_sha256: e65fc021e87eb3cfe5df6ede50e2260cfdfab3079c13609636206140170764c3
text_sha256: 50466414791b3197569ac6e0ad8d972493f18896c9e368c338032dbd9b45b809
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# It’s the Little Things : Breaking an AI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_its-the-little-things-breaking-an-ai.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `e65fc021e87eb3cfe5df6ede50e2260cfdfab3079c13609636206140170764c3`
- Text SHA256: `50466414791b3197569ac6e0ad8d972493f18896c9e368c338032dbd9b45b809`


## Content

---
title: "It’s the Little Things : Breaking an AI"
url: "https://infosecwriteups.com/its-the-little-things-breaking-an-ai-40c30ae85f37"
authors: ["Debangshu Kundu (@debangshu_kundu)", "Rajesh (@_rajesh_ranjan_)"]
bugs: ["Path traversal"]
publication_date: "2022-10-13"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2045
scraped_via: "browseros"
---

# It’s the Little Things : Breaking an AI

It’s the Little Things : Breaking an AI
Debangshu Kundu
Follow
5 min read
·
Oct 14, 2022

167

A tale of tiny observations that led to a critical finding.

tl;dr — Feeding an AI path traversal payloads and getting local files spit out in return.

Introduction

There’s this endless debate of AI taking over the planet and rendering manual labor jobless. Well, not today at-least! Let’s explore how untrusted user input led to the disclosure of local system files in an AI model!

A couple of months ago, I stumbled across CatCorp, a company that builds NLP Models as an API service, which can be seen as the next rising trend in Software as a Service (SaaS) economy.

The application is very simple. Upon logging in, you’re presented with a dashboard to create and train your own AI model. Creating a model involves selecting the Model Type and Size, followed by inputting a data separator and your training data. This can be done either via uploading a .txt file containing the data to be fed to the AI/application or referencing a link to a pre-uploaded .txt file hosted on your desired website.

Once the data is uploaded, the processing begins. It’s a 5 stage process.

Data Processing > Finetuning > Exporting Model > Deploying API > Ready.

Therefore, it takes a while.

They also provide a feature to View the logs that occur through the said process.

Discovery and Exploitation

While tinkering around the application, I took a deeper look at the Model Creation feature and the Link to your .txt component sparked my interest. I started fuzzing around and fed in a basic path traversal payload like /../../../etc/doesnotexist just to check how the server responds.

Before we get to that, let’s take a quick detour to check how the request actually looks like :-

This is a pretty basic request that passes in the name, path (link to .txt) and other related attributes required for the model creation. Now, let’s go back and take a look at the responses that peaked my interest!

Request/ Response A (Valid path)
Request A
Press enter or click to view image in full size
Response A
Request/ Response B (invalid path)
Request B
Press enter or click to view image in full size
Response B

Taking a closer look at the response we find a common linux verbose error, indicating that the application is indeed traversing back the directories and trying to fetch the requested file!

Get Debangshu Kundu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Cool! But, how do we actually disclose the said files?! Supplying any valid file, let’s say /etc/hosts or /etc/passwd throws a requirement error as shown in Response A. I was stuck for hours on this one.

Although I did have a single successful response showing the contents of the local file, I wasn’t able to recall how! Thankfully, I hadn’t closed out my burp session and a simple search revealed the culprit here. It was all about a single data separator i.e.: (/).

Can you believe it? A single character was all that decided whether this was gonna be a critical or not!

So, this was how it worked :-

Press enter or click to view image in full size

As evident in the screenshot, all we had to do was to pass a tiny separator, that set things into place for us to extract a part of the local file via a sweet side-channel leak!

Press enter or click to view image in full size
New response

Here’s the new response. Notice how it’s different from the initial response when supplied with a valid filename. This emphasizes the need to look out for tiny hints like the said issue.

Moving on, once the request is successful, we could simply re-visit the dashboard, tap on the created AI model and View the logs, and that would bring us up partial contents of the requested file (here /etc/passwd) as happens in a side-channel leak, displayed in the screenshot below.

Press enter or click to view image in full size
Contents of /etc/passwd being disclosed

This is a sight of extreme euphoria for any hacker on the planet and was enough for the vuln to be accepted as a critical!

The cause?/ Possible Explanation

My best guess is the supplied separator, somehow breaks up/ interrupts the input flow and as a result partially-renders the file contents, as part of an error/warning message.

That’s it for today, folks! See you in a bit.

This bug was in collaboration w/ https://twitter.com/_rajesh_ranjan_

Timeline :-

Reported : 20 Aug 2022

Rewarded : 16 Sep 2022

Takeaway(s) :-

Take care of your burp logs and keep an eye out for even the tiniest of input fields!

Press enter or click to view image in full size

Any feedback is appreciated in DMs :- https://twitter.com/ThisIsDK999

Peace Out! ✌️

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

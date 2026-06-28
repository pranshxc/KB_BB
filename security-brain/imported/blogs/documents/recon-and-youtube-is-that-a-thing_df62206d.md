---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-17_recon-and-youtube-is-that-a-thing.md
original_filename: 2022-02-17_recon-and-youtube-is-that-a-thing.md
title: Recon and YouTube, is that a thing?
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: df62206d8093d2402b98fb5c20cf1dd711c3e25695107ca12459a0b73f0deffd
text_sha256: fd9d2c2e0791019161355c9279d57674c7e6f4ca4151b4511cecf630764e4da7
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Recon and YouTube, is that a thing?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-17_recon-and-youtube-is-that-a-thing.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `df62206d8093d2402b98fb5c20cf1dd711c3e25695107ca12459a0b73f0deffd`
- Text SHA256: `fd9d2c2e0791019161355c9279d57674c7e6f4ca4151b4511cecf630764e4da7`


## Content

---
title: "Recon and YouTube, is that a thing?"
url: "https://medium.com/@720922/recon-and-youtube-is-that-a-thing-5523b48c32e3"
authors: ["Marcos IAF / Rohit (@marcos_iaf)"]
bugs: ["Subdomain takeover"]
publication_date: "2022-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2894
scraped_via: "browseros"
---

# Recon and YouTube, is that a thing?

Recon and YouTube, is that a thing?
Marcos IAF
Follow
6 min read
·
Feb 19, 2022

223

3

Hey fella hunters, hope you all are doing fine. This is my first ever blog, I will try to keep it as much simple as possible spilling as much secrets as I can ;)

YouTube Recon, is that a thing?, You may ask.

Well, yes it is.

We all have heard of the term Recon when it comes to Bug Bounties but what the hell is this Recon? And why it is so important? Let’s dive deep into this and understand the importance of Recon or in general Information gathering what I call it.

What is Recon?

To be honest, It’s just a fancy term for Information Gathering. Recon is coined from Reconnaissance which can be defined as a preparatory phase of gathering information while performing security assessments.

The recon phase constitutes of various steps but we will be focusing mainly on general overview of target and expanding scope.

Ever wondered, what are the countless possibilities of gathering information about your target while doing Bug bounties or General Pentesting? Google dorking, Github Recon, or maybe YouTube Recon?

We all are well aware with what Google dorking or GitHub Recon is, so we will not discuss those here instead we will focus on YouTube Recon and try to understand how YouTube can be used to gather crucial information regarding your target.

What is YouTube Recon?

We all know what YouTube is and the amount of information it carries. Unlike Google or GitHub recon, YouTube have information in a visual form which is more easy to grasp and understand, so why not we explore this gold mine of information for our bug bounty purpose.

The Target

Few weeks back, I decided to hunt on target where everything was in scope and by everything I mean literally everything owned by the company is in scope.

Note: As the target is a private program, we will use the term redacted in place of actual target.

It’s a huge target with tons of products in scope, so I decided not to target the primary application and instead focus on other secondary applications owned by the Company.

Started researching about the target on Google and was blow away with the information that was spread in bits and pieces. There was hell lot of information to go through but also a lot of mess as things were scattered all over the place, started taking notes and by the end of an hour I was with a good amount of domains owned by the company.

Started hunting on freshly collected domains only to find hell lot of duplicates, reported around 17 reports and 13 were marked duplicate. At that moment I realized this is the same information every second person is using, I need to dig deeper.

Note: I was on a mission to get 20+ bugs ASAP, and that is why I needed to target applications which were easy and loosely secured but as well less touched by other security researchers.

I was very excited about this and was very unsettled with the duplicates so this became kind of obsession to me. I challenged myself to get those 20 bugs within 2 days but had no idea where to start with.

The Actual YouTube Recon

Anyways, then I went to sleep only to get dreams about the target and the findings. On the very next day, 05:30 AM I was on treadmill after a workout session but unsettled by the target in my mind, I grabbed my phone and stopped the music and it was this moment when something clicked in my mind and I thought to search the target in YouTube.

Press enter or click to view image in full size
YouTube search results for the Organization

I was baffled by the results. To be honest I had no expectations of getting anything good but I started watching videos one by one while having a sweet walk over the treadmill. To my surprise this was something I was looking for. Boom !! The information was well curated in a visual form, I started digging deep through the videos and started taking notes.

Get Marcos IAF’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Some keywords you can use for your search

Company secrets

How big is Company

Services owned by Company

Company year wise sales

The Company was way bigger than my expectations and the information gathered from YouTube helped me map the whole Organization very easily.

The YouTube videos helped me find some services and applications owned by the company which were at very early stage and were not in public domain for much time, these were good targets to look for. Not only this from one of the video I was able to map the different sectors operated by the company and this point it was crystal clear to me which applications I need to focus on and target them.

Press enter or click to view image in full size
Snap from a YouTube video about the Company

At this stage, the information obtained was enough to map the different applications owned by the Company but I had a challenged myself of completing the task within 2 days hence I needed some straight forward bugs.

Grinding through the Descriptions and the Channels

After this, I started looking for YouTube channels owned by the Company and started going through their videos. The videos included their launch events to their future developments to abolished services. The description of these videos was a Gold mine, had a lot of Information regarding the services and links to these applications.

Press enter or click to view image in full size
Description of a YouTube video giving access to admin panel

I found multiple channels of the niche(secondary) companies owned by the ████ all those linked to their websites. Out of these there were 7 similar channels for a single company but in different languages like

████ English

████ Hindi

████ Russian

████ Japanese

They all had region specific top level domain like .com .in .ru .jp etc etc, one thing was clear to me if I can find a single bug on any one of these I can replicate that on other 6 as well.

Luckily, while enumerating subdomains for ████.ru, I found a domain comm. ████.ru pointing to 3rd party service which was available for registration. This was a quick Subdomain Takeover, I immediately created an account on the 3rd party service and took over the domain.

Press enter or click to view image in full size

This Subdomain Takeover was fun and exciting. This was a totally new service to me and probably to most of you as there were no information available regarding the takeover of this service not even a single blog nothing.

I will write a detailed post regarding this take over and will be publishing a nuclei template for the same as well.

As expected, the takeover replicated on the other 6 domains as well and I got 7 reports triaged within 20 minutes. I continued hunting on other secondary domains found via the YouTube videos, descriptions and community posts and was able to submit 23 bugs by the end of Day 1 itself.

As of today, 10 reports have been resolved and Swags being rewarded.

Press enter or click to view image in full size
Swags being rewarded daily

A huge pile of Information is lying around you be it in raw data, text or visual form. Information Gathering is a huge part of Recon, you need to gather as much information as possible, it doesn’t matter where and which form it comes in.

~ Rohit

So this was it, I hope you enjoyed reading it and learned something new today. Thanks for holding with me :)

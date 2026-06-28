---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-08_persistent-xss-on-microsoft-bingcom-by-poisoning-bingbot-indexing.md
original_filename: 2024-08-08_persistent-xss-on-microsoft-bingcom-by-poisoning-bingbot-indexing.md
title: Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: d6ab7ab3be8ed254640e0cbed9bcdb7b2072777b0b844a76bdd8354fbc1a2f88
text_sha256: de6a7528cab99eb5d8a46668d05e2f7949ef937ea7c4def6dae313e87940b818
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-08_persistent-xss-on-microsoft-bingcom-by-poisoning-bingbot-indexing.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `d6ab7ab3be8ed254640e0cbed9bcdb7b2072777b0b844a76bdd8354fbc1a2f88`
- Text SHA256: `de6a7528cab99eb5d8a46668d05e2f7949ef937ea7c4def6dae313e87940b818`


## Content

---
title: "Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing"
url: "https://infosecwriteups.com/persistent-xss-vulnerability-on-microsoft-bings-video-indexing-system-a46db992ac7b"
authors: ["Supakiad S. (@Supakiad_Mee)"]
programs: ["Microsoft (Bing)"]
bugs: ["Stored XSS"]
bounty: "3,000"
publication_date: "2024-08-08"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 86
scraped_via: "browseros"
---

# Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing

Persistent XSS on Microsoft Bing.com by poisoning Bingbot indexing
Supakiad S. (m3ez)
Follow
7 min read
·
Aug 8, 2024

280

3

1

Persistent XSS Vulnerability on Microsoft Bing’s Video Indexing System.

Press enter or click to view image in full size
This image was generated using ChatGPT
Table of Contents
Introduction
What is Bing and Bingbot
How Bingbot Works
Vulnerability Details
Vulnerability Discovery and Analysis
Discovery of Persistent XSS on Bing
Proof of Concept (PoC)
Disclosure Timelines
Introduction

In this blog post, I will discuss the details of a Persistent XSS on Bing.com by poisoning Bingbot from external websites.

What is Stored or Persistent XSS?
Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-II XSS.

For more information, please visit: Cross Site Scripting (XSS) | OWASP

What is Bing and Bingbot
Press enter or click to view image in full size
How Bing delivers search results — Microsoft Support

Bing is a search engine developed by Microsoft, offering web, video, image, and map searches. It aims to assist users in making informed decisions by providing organized and relevant search results.

Press enter or click to view image in full size

Bingbot is a web crawler, also known as a spider or search engine bot, developed by Microsoft. Its primary function is to explore and index web pages for Bing, Microsoft’s search engine. Launched in October 2010, Bingbot navigates through external and internal links to discover new web pages and update Bing’s index with changes to existing ones.

This process, known as crawling, helps Bing keep its search results up-to-date and relevant. The data collected by Bingbot is fed into Bing’s search algorithms, which evaluate the content’s context and quality to determine its ranking in search results.

How Bingbot works?

As Bingbot crawls the web, it sends information to Bing about what it finds. These pages are then added to the Bing index and algorithms are used to analyze the pages so we can effectively include them in search results, including determining which sites, news articles, images, or videos will be included in the index and available when users search for specific keywords. Learn more about how Bing finds and indexes pages here.

How to recognize and verify Bingbot — Seobility Wiki
Vulnerability Details

A stored Cross-Site Scripting (XSS) vulnerability was discovered on Bing’s platform. This vulnerability occurs when Bing retrieves and stores video details such as the title, description, and owner name from the internet in an insecure manner. The process involves Bingbot or Bing’s web crawler indexing this metadata without proper sanitization, preserving malicious scripts in Bing’s index.

Impacts
Malicious actors can execute arbitrary JavaScript in the context of Bing’s web application.
This can lead to various attacks, including but not limited to cookie theft, session hijacking, defacement, and phishing.
The vulnerability affects all users who view the infected video details, posing a significant security risk.
Vulnerability Discovering and Analysis

When a user searches for videos on Bing, the search engine processes the query and retrieves relevant content from its index. The search results page displays the video details, including the unsanitized, potentially malicious scripts. The application stores this data in a JSON pattern, but the content type is set as text/html, which can lead to Persistent XSS.

When users view or interact with these infected videos, the malicious scripts execute within the context of Bing’s web application. This occurs because the browser interprets the data as HTML due to the content type, allowing the scripts embedded in the JSON data to run. As a result, this can lead to various security threats, including data theft, session hijacking, phishing, and defacement. These threats affect users who view the infected content, potentially compromising their personal information and the integrity of their accounts.

The improper content type setting exacerbates the risk by making it easier for attackers to inject and execute scripts within Bing’s web application, bypassing typical security measures that rely on correct MIME type handling to prevent such vulnerabilities.

Discovery of Persistent XSS on Bing

During my exploration of Bing, I identified a vulnerability in the Bing video search. When users search for videos, Bing displays video details fetched from external sources without proper sanitization. This allows the injection of malicious scripts, posing significant security risks.

Back to the story

One day, I was using Bing and found that if a user searches for an image on Bing image search, and if the result is a video and the user tries to view it, the Bing URL becomes: https://www.bing.com/videos/vdasync

Press enter or click to view image in full size
After clicking and viewing the details I found that the API returns metadata of the video that Bingbot has collected from other websites and stored in Bing’s search system.
Press enter or click to view image in full size
But I noticed that the content type of this URL returns as Content-type: text/html; charset=utf-8 instead of application/json
Press enter or click to view image in full size

What if we could control the metadata, and Bingbot retrieves our data and stores it into Bing website without sanitization or encoding?

As I mentioned in the previous section on how Bingbot works, Bingbot helps Bing keep its search results up-to-date and relevant. So, I tried to create a video post on a different platform.

Get Supakiad S. (m3ez)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The problem is that I don’t know how long it will take for my new video to appear on Bing search, so I considered making new posts on the following websites:

VK: https://vk.com/video/@club226523289
Tiktok: https://www.tiktok.com/@m3ez_xss
Instagram: (@m3ez.ss) • Instagram photos and videos
and other sites

Why I didn’t post a video on YouTube

Because, as you can see from the screenshot response of https://www.bing.com/videos/vdasync, the data response is in JSON format. To execute JavaScript or HTML injection, I need to ensure that I can use <> (angle brackets). But on the YouTube, this isn't possible. This limitation also applies to other popular platforms like Vimeo and Dailymotion.

Press enter or click to view image in full size
Supakiad S. (m3ez) — YouTube

Luckily, after a few days, I found that my video from vk.com appeared on the Bing video search, allowing me to finalize my report and proof of concept as follows

Proof of Concept (PoC):
Post a video on a website and include a script in the owner's name, video title, or description:
For example, I uploaded a video through vk.com with the following payload:
<script>prompt('Stored XSS by Supakiad S. (m3ez)',document.domain);</script>
Press enter or click to view image in full size
M3ez XSS PoC 2024 — Cross site Scripting TEST.. | <script>prompt(‘M3ez:’,document.domain)</script> (vk.com)
Published the video post so anyone can access it, including allowing Bingbot to crawl my video metadata.
Press enter or click to view image in full size
M3ez XSS PoC 2024 — Cross site Scripting TEST.. | <script>prompt(‘M3ez:’,document.domain)</script> (vk.com)
Wait until Bingbot crawls and retrieves the video from vk.com and saves the details (including the injected XSS script).
Start searching the “Microsoft Bing Video” web application. The keyword I used is "m3ez" site:vk.com.
Press enter or click to view image in full size
“m3ez” site:vk.com — Search Videos (bing.com)
Click on the video, the mid parameter will appear in the URL:
Press enter or click to view image in full size
“m3ez” site:vk.com — Bing Videos
Append the mid parameter from the previous steps into the following URL:
https://www.bing.com/videos/vdasync?mid={mid}

After navigating to the URL, the XSS payload will be triggered as shown below.

https://www.bing.com/videos/vdasync?mid=***REDACTED-SUSPECT-TOKEN***Press enter or click to view image in full size
https://www.bing.com/videos/vdasync?mid=***REDACTED-SUSPECT-TOKEN***Video PoC

3,000$ Persistent XSS Vulnerability on Microsoft Bing’s Video Indexing System (youtube.com)
Disclosure Timelines
Jul 1, 2024: Vulnerability discovered.
Jul 1–7, 2024: Initial report and awaiting PoC evidence.
Jul 8, 2024: Reported through MSRC portal.
Jul 9, 2024: Status moved to Review/Repro.
Jul 15, 2024: Confirmed by MSRC; status moved to Develop. MSFT Bounty team started reviewing for possible bounty.
Jul 17, 2024: Draft blog post sent to MSRC for review.
Aug 5, 2024: MSRC reviewed blog post, confirmed fix, status moved to Pre-Release and Complete.
Aug 6, 2024: MSFT Bounty team awarded $3000 for case 89310 under M365 Bounty | MSRC (microsoft.com).
Aug 8, 2024: Publish this blog post.

I appreciate your feedback and would love to hear your thoughts on my blog. If you have any comments or suggestions, please feel free to reach out to me on LinkedIn or Twitter.

LinkedIn: Supakiad Satuwan | LinkedIn
Twitter: My Space! (@Supakiad_Mee) / X (twitter.com)
YouTube: Supakiad S. (m3ez) — YouTube

Thank you for your support!
Previous Articles
How I found DOM-Based XSS on Microsoft MSRC and How They Fixed it | by Supakiad S. (m3ez)
Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms | by Supakiad S. (m3ez)
Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022) | by Supakiad S. (m3ez)

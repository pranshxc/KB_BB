---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-05_race-conditions-with-pipelining.md
original_filename: 2023-11-05_race-conditions-with-pipelining.md
title: Race Conditions with pipelining
category: documents
detected_topics:
- command-injection
- race-condition
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- race-condition
- api-security
- supply-chain
language: en
raw_sha256: f67f64d12033f179fd95b14b86db1b55222d363eed8be53a411fdaa3c9ceaef1
text_sha256: 0eb44647736b7f5a5cb0db3ed75532e7db9411ba7b7f86c0a4a1f6444d3eba73
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Race Conditions with pipelining

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-05_race-conditions-with-pipelining.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `f67f64d12033f179fd95b14b86db1b55222d363eed8be53a411fdaa3c9ceaef1`
- Text SHA256: `0eb44647736b7f5a5cb0db3ed75532e7db9411ba7b7f86c0a4a1f6444d3eba73`


## Content

---
title: "Race Conditions with pipelining"
url: "https://infosecwriteups.com/race-conditions-with-pipelining-9034358a2781"
authors: ["Abbas Heybati (@abbas_heybati)"]
bugs: ["Race condition"]
publication_date: "2023-11-05"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 685
scraped_via: "browseros"
---

# Race Conditions with pipelining

Race Conditions with pipelining
Abbas.heybati
Follow
3 min read
·
Nov 5, 2023

350

4

Hi guy’s
Approximately a year ago, I identified a race condition using pipelining technique that allowed me to add a significant number of videos to my dashboard on the website. You were restricted to adding only one video to your dashboard. A few weeks ago, I emailed James Kettle and explained the situation to him. I wanted to see if anything could be done about it. He responded to my email, showing great enthusiasm about the issue. His response encouraged me to write this report, and I want to express my gratitude to him for his support.

My goal in writing this write-up is to demonstrate that someone has successfully exploited a race condition using pipelining. I have tried many methods in this scenario, but none worked except for pipelining, which successfully executed the attack.

Get Abbas.heybati’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The situation was that the website’s policy allowed only one video to be prepared for download at a time. I tried various methods, such as using Intruder Burp and other tools available on GitHub, as well as manual techniques, but none of them worked. I should also mention that at that time, James Kettle hadn’t yet presented his new method for race conditions. I only knew that I had to send my requests to their server simultaneously in the shortest possible time. That’s when I started checking the requests.

Check Request

When I checked the requests, I realized that in the section POST /video/generate, the videos are prepared. Therefore, I thought about using pipelining to simultaneously send two different videos to the server in the shortest time possible. Initially, I tried various methods for pipelining, such as option/trace… but in the end, I got better results with GET /images/apple-touch-icon.png. That’s why I tested pipelining once to see if it works correctly or not.

Press enter or click to view image in full size
Test pipelining

When I became confident with this method and endpoint, I started the main testing, meaning I sent the original request I wanted to create videos with pipelining to the added request.

Press enter or click to view image in full size
Final Request pipelining

Note: The second response is not visible in the picture, as I mentioned earlier. I discovered this vulnerability a year ago, just as I explained above.
I was able to prepare two videos for simultaneous download here, but you couldn’t do this in different situations. I found it very interesting that such a capability exists through pipelining. However, these documents are old, and this bug no longer exists in this company. If the quality of the images is bad, I apologize. My intention was to show you what I have done with pipelining, and maybe this write-up will be helpful for friends and colleagues in the future.

Best Regards,
Abbas Heybati.

twitter.com/abbas_heybati
www.linkedin.com/in/abbas-heybati-76432220b

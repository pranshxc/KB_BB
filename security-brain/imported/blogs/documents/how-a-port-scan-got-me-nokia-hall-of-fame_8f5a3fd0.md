---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-22_how-a-port-scan-got-me-nokia-hall-of-fame.md
original_filename: 2022-08-22_how-a-port-scan-got-me-nokia-hall-of-fame.md
title: How a Port scan got me Nokia Hall of Fame
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 8f5a3fd0f68814939ba09fc8f4f6f05afb24a08ca1b752211c1edae86395df54
text_sha256: d7081da7ff049e05fc0e217624da5b96127b3de81038426d1b0596d61178298e
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How a Port scan got me Nokia Hall of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-22_how-a-port-scan-got-me-nokia-hall-of-fame.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `8f5a3fd0f68814939ba09fc8f4f6f05afb24a08ca1b752211c1edae86395df54`
- Text SHA256: `d7081da7ff049e05fc0e217624da5b96127b3de81038426d1b0596d61178298e`


## Content

---
title: "How a Port scan got me Nokia Hall of Fame"
url: "https://medium.com/@mullangisashank/how-a-port-scan-got-me-nokia-hall-of-fame-6f9b65e920e3"
authors: ["Mani Sashank"]
programs: ["Nokia"]
bugs: ["Missing authentication", "Information disclosure"]
publication_date: "2022-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2279
scraped_via: "browseros"
---

# How a Port scan got me Nokia Hall of Fame

Top highlight

How a Port scan got me Nokia Hall of Fame
Mullangisashank
Follow
4 min read
·
Aug 23, 2022

519

5

Hi everyone. This is Mani Sashank, a security analyst who does bug bounty in his free time. 😄

As this is my first article, I would really appreciate if you could provide feedback on this.

Before going into the article I would like to highlight that during my initial days into bug bounties I was asking every bug bounty hunter out there about their methodology and some other stupid questions which can obviously be googled. But fortunately many of them took their precious time and replied to my questions.

So now today I am taking my first step towards giving back to the community.

Enough with the chit-chat. Let’s go straight into the topic.

This is the simple methodology I follow:

Enumerate the sub-domains.
Check for sub-domains with functionalities.
Start assessing those websites manually along with some content discovery and port scanning in the background.

That’s it. A simple 3 step process. (Of course there are sub-steps for each step, which we’ll discuss in later blogs.)

As you can see from the above 3 steps the third step includes port scanning. (Spoiler alert: Later on this got me the Hall of Fame). 😅

While I started hunting manually on some websites of Nokia, I also initiated a port scan and content discovery on all the alive websites which are obtained on step 1.

During this process I got port 9090 as open on one of the websites. So later on when I tried to visit this website whose URL looks like: https://valid-domain.nokia.com:9090 it redirected me to https://valid-domain.nokia.com:9090/graph which included some colorful graphs looked like this.

Press enter or click to view image in full size

After seeing this I had no clue of what this graph belongs to. Then after some googling I read what’s “Prometheus”. Then later read some h1 reports on related findings and found some sensitive endpoints. 😉

So after all this I have sent an well written report and POC included mail to security-alert@nokia.com regarding this issue. Then they validated the same from their end and notified me that it was a valid finding. Later on, they added me to their Hall of Fame page as shown below. 😀

Press enter or click to view image in full size
March 2022

Tools I have used:

Subfinder, assetfinder
httpx to check for alive domains
Rustscan for port scanning.

NOTE: Please note that RustScan takes a lot of time when compared to masscan or any other tool. But I personally feel that RustScan is way more reliable than any other tool. (Please let me know if there are any other tools that are fast and reliable than rustscan. After all nobody knows everything. 😅)

Get Mullangisashank’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You might think this was possible just out of luck. Please hold that thought and take a look at the below screenshots and take decision. 😁

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

There were a lot of duplicates before my first valid submission to Nokia VDP. So don’t give up on your dreams. Consistency is what matters ultimately in bug bounty.

Timeline:

2nd March, 2022: Reported the issue to security-alert@nokia.com.

14th March, 2022: Requested for an update.

21st March, 2022: Notified me saying it’s a valid finding.

Later I got one more Hall of Fame on Nokia following the same methodology.

Press enter or click to view image in full size
April 2022

That’s it for this blog. I would really appreciate if you could take some time and provide feedback on this blog, so that I can improve it further. 😁

Wishing you all the very best and success on your bug bounty journey. 🤞

Social Media Links:

Instagram: https://www.instagram.com/mani.sashank/

Twitter: https://twitter.com/manisashankm

LinkedIn: https://www.linkedin.com/in/manisashank/

Feel free to ping me on anything. My DM will always be open. 😀

In next blog let’s discuss about how I was able to get UN hall of fame. See you in next blog. Till then ✌

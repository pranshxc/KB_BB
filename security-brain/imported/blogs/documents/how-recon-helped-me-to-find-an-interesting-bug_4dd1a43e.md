---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-15_how-recon-helped-me-to-find-an-interesting-bug.md
original_filename: 2020-08-15_how-recon-helped-me-to-find-an-interesting-bug.md
title: How recon helped me to find an interesting bug…
category: documents
detected_topics:
- idor
- ssrf
- xss
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- ssrf
- xss
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 4dd1a43eaf79dc5d4fa14b26092e4c7ace3f293751174b7ad09e63e80aec11c1
text_sha256: 1c17f1013dc21f653431184f7177efa707c737aa8f5c9cd129e34e68c7e92499
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How recon helped me to find an interesting bug…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-15_how-recon-helped-me-to-find-an-interesting-bug.md
- Source Type: markdown
- Detected Topics: idor, ssrf, xss, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `4dd1a43eaf79dc5d4fa14b26092e4c7ace3f293751174b7ad09e63e80aec11c1`
- Text SHA256: `1c17f1013dc21f653431184f7177efa707c737aa8f5c9cd129e34e68c7e92499`


## Content

---
title: "How recon helped me to find an interesting bug…"
url: "https://medium.com/@vedanttekale20/how-recon-helped-me-to-find-an-interesting-bug-17a2d8cf1778"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["Open redirect"]
publication_date: "2020-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4320
scraped_via: "browseros"
---

# How recon helped me to find an interesting bug…

1

·

Vedant Tekale
 highlighted

1

·

Vedant Tekale
 highlighted

How recon helped me to find an interesting bug…
Vedant Tekale
Follow
3 min read
·
Aug 15, 2020

231

4

Hello infosec community! I’m back again to share an interesting finding with you. Little bit about me, my name is Vedant and I’m a bug bounty hunter/ethical hacker for about 4 months now. And I love what I do. So back in July I decided that in August I’ll focus solely on “Recon”. I always wanted to up my recon game. On 1st August I rented a VPS and started to install some Recon tools. I installed all the necessary tools for subdomain enumeration, content discovery, parameter discovery etc.

Enough of the backstory, lets understand the bug.

Read and learn
Recon phase:-

One day I started looking for some responsible disclosure programs and got a program. The program had *.target.com in scope so I decided to do some recon on the target. First I enumerated all the subdomains using subfinder and amass and combined the output of both tools. Then I used another tool called as httpx for probing and saved the output in a txt file. After that I used a tool created by projectdiscovery team called as nuclei and I used the following command,

cat final.txt | nuclei -t path/to/nuclei-templates/vulnerabilities -o results.txt

Discovery phase:-

After some time I got some results and there was a subdomain vulnerable to microstrategy ssrf and the URL was as following,

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://something.target.com/MicroStrategy/servlet/taskProc?taskId=shortURL&taskEnv=xml&taskContentType=xml&srcURL=

At first I tried for an open redirect by changing srcURL parameter to bing.com but it wasn’t redirecting. Then I tried for SSRF and again it wasn’t working. I thought its just a false positive.

Then after some time I just googled for the word Microstrategy and got to know that it is some kind of company which provides cloud based services. So just for curiosity’s sake I searched for “Microstrategy vulnerability” and after some time I got link to a medium blog which was about a SSRF vulnerability and in that blog there was exact same url that I found! So I read the blog and understood that srcURL parameter only takes tiny URLs and that’s why it wasn’t redirecting me. So I made a tiny url for https://bing.com and put it in srcURL parameter and it redirected me to bing.com! I tried for SSRF but there wasn’t a SSRF because site was redirecting me and it wasn’t fetching data from external url. To increase the impact I looked for a XSS hosted page and after some time I got it and made its tiny url and again pasted it into srcURL parameter and the XSS executed successfully! I was very happy.

I quickly wrote a good report and sent it to the company. After 4–5 days I received a response from them saying “Thanks for reporting this issue” and they rewarded by adding me to their security researcher’s “Hall of fame”.

Even though I didn’t get any bounty for reporting this issue, I learned some new things and most importantly I learned the power of “Recon”.

If you have any doubts regarding this write up you can reach me here.

Hope you liked this finding. Stay home, stay safe. Thank you!

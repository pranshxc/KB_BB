---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-07_my-debut-with-a-critical-bug-how-i-found-my-first-bug-api-misconfiguration.md
original_filename: 2023-09-07_my-debut-with-a-critical-bug-how-i-found-my-first-bug-api-misconfiguration.md
title: 'My debut with a Critical Bug: How I found my first bug (API misconfiguration)'
category: documents
detected_topics:
- api-security
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- api-security
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: 654e95275718e1a136f5026346ae25d35339bdb58960b91b8e1a2f92aab3a5d7
text_sha256: 1b64cf39c57dfa0f118400de799513a55aa49333bdcbe150cf9c502445670458
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# My debut with a Critical Bug: How I found my first bug (API misconfiguration)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-07_my-debut-with-a-critical-bug-how-i-found-my-first-bug-api-misconfiguration.md
- Source Type: markdown
- Detected Topics: api-security, xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `654e95275718e1a136f5026346ae25d35339bdb58960b91b8e1a2f92aab3a5d7`
- Text SHA256: `1b64cf39c57dfa0f118400de799513a55aa49333bdcbe150cf9c502445670458`


## Content

---
title: "My debut with a Critical Bug: How I found my first bug (API misconfiguration)"
url: "https://medium.com/@jay_rana/my-debut-with-a-critical-bug-how-i-found-my-first-bug-api-misconfiguration-2f7cadc89669"
authors: ["whit3ros3"]
bugs: ["Hardcoded API keys", "Information disclosure"]
publication_date: "2023-09-07"
added_date: "2023-09-13"
source: "pentester.land/writeups.json"
original_index: 800
scraped_via: "browseros"
---

# My debut with a Critical Bug: How I found my first bug (API misconfiguration)

Top highlight

My debut with a Critical Bug: How I found my first bug (API misconfiguration)
whit3ros3
Follow
4 min read
·
Sep 7, 2023

929

8

Finally, the day arrived when I could share my own findings, rather than just reading other researchers’ findings (which I truly love to do, as they are a significant source of my motivation). Without further ado, let’s dive into the journey of my first bug discovery. In short, it’s an API misconfiguration bug where I found an API key with potentially dangerous permissions in the request.

Allow me to introduce you to our target with a cliché statement: let’s call it “example.com,” an e-commerce website.
For a couple of days, I tried to find various vulnerabilities like login bypass, XSS, subdomain takeover, and more, but my efforts were in vain and no good came out of it. Just as my beginner’s patience was wearing thin, I stumbled upon a Medium blog post of a researcher where he found some sensitive data in JavaScript files. Inspired, I decided to try it on my target and started hunting for JS files.

The command I used was
echo “example.com” | gau | grep .js | httpx -mc 200

This led me to discover a ton of JS files. After spending some time, I came across one suspicious file. I copied the JS file data in my VS Code to make it easily readable. I dug into it and found some intriguing data.

Press enter or click to view image in full size
ALGOLIA and Contentful api-keys
Press enter or click to view image in full size
More sensitive data

It contained many secrets and API keys, but as a beginner, I had no idea how to leverage this information. And then I turned to every bug hunter’s friend: RESEARCH!!. I just sat and started searching on Google, ChatGPT, Github repositories, read some blogs, consulted some mentor-friends, all in an attempt to exploit this sensitive data. Regrettably, my efforts yielded little success as the API keys and secrets I had discovered were either not exploitable, like the ALGOLIA key for the blog site, which had permissions of recommendation and search only,

Press enter or click to view image in full size
ALGOLIA api-key permissions

and others led to publicly accessible data, such as the content of the target’s blog site hosted on “contentful.com.” Another dead end.

Get whit3ros3’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was on the brink of abandoning this target for the second time when I decided to glance through my target list in Burp Suite, searching for something interesting — a tip I’d read about in another blog. And that’s when it happened.

A host caught my eye:
https://(application_id).algolianet.com

As I inspected the requests made to this host, I noticed something intriguing. Some requests used the same API key I had found in the JS file, while others contained a different API key.

This difference caught my attention, and I went back to this blog that I had read earlier:

https://www.secjuice.com/api-misconfiguration-data-breach/

Using this knowledge, I explored the permissions of this new API key.And that’s when I had my Eureka moment.

Press enter or click to view image in full size
new api-key permissions

It had permissions to add and delete objects. I didn’t try to add or delete something, fearing I might break the site. I knew that these were some dangerous permissions. So I prepared a report and submitted it. Within a day, it was triaged as high severity, but after a few days, it was updated to critical.

triaged

My patience had paid off, with a touch of luck, I might add. It is not a technical bug like XSS with some crazy payload or something, but a bug’s a bug, and this one can bring a whole blog site down!!!!

Special thanks to 
Debarghya Sahoo
 and 
Aditya Shende
.

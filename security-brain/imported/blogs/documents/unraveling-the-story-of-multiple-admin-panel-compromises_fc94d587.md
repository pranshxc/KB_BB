---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-08_unraveling-the-story-of-multiple-admin-panel-compromises.md
original_filename: 2023-12-08_unraveling-the-story-of-multiple-admin-panel-compromises.md
title: Unraveling The Story of Multiple Admin Panel Compromises
category: documents
detected_topics:
- access-control
- xss
- idor
- ssrf
- command-injection
- rate-limit
tags:
- imported
- documents
- access-control
- xss
- idor
- ssrf
- command-injection
- rate-limit
language: en
raw_sha256: fc94d5870dd5cd21dfb1a4af5065a8690a287e72668ec075b1c91fca0ee45b74
text_sha256: 394ea3ea440e644a38301bc1314987d08b0b5da636a71780087ef88289784848
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Unraveling The Story of Multiple Admin Panel Compromises

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-08_unraveling-the-story-of-multiple-admin-panel-compromises.md
- Source Type: markdown
- Detected Topics: access-control, xss, idor, ssrf, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `fc94d5870dd5cd21dfb1a4af5065a8690a287e72668ec075b1c91fca0ee45b74`
- Text SHA256: `394ea3ea440e644a38301bc1314987d08b0b5da636a71780087ef88289784848`


## Content

---
title: "Unraveling The Story of Multiple Admin Panel Compromises"
url: "https://vedanttekale20.medium.com/unraveling-the-story-of-multiple-admin-panel-compromises-baac4444285f"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["Weak credentials", "Authentication bypass", "HTTP response manipulation"]
bounty: "500"
publication_date: "2023-12-08"
added_date: "2024-01-05"
source: "pentester.land/writeups.json"
original_index: 644
scraped_via: "browseros"
---

# Unraveling The Story of Multiple Admin Panel Compromises

Unraveling The Story of Multiple Admin Panel Compromises
Vedant Tekale
Follow
5 min read
·
Dec 8, 2023

210

1

Welcome back, fellow hackers and cyber security enthusiasts! I’m Vedant, also known as Vegeta on Twitter 😁. It’s been a while, but I’m excited to share another intriguing story with you. Moving forward, I aim to bring more interesting write-ups like this one regularly. You can explore my previous write-ups and stay tuned for upcoming stories on my new website! Feel free to check it out here. So without further delay, let’s dive right in.

Background:

I was actively hacking on a bug bounty program on HackerOne platform for a long time and decided one day to revisit the program again. Previously I found many bugs there including SSRF, Stored XSS and some broken access controls as well. This time I wanted to try out something else so I decided that I will try to find some admin panels and see if somehow I can bypass them, and to find such admin panels one step is very necessary and that is… you guessed it right, Recon!

The Recon:

As I said before, I was working on that program for a very long time so I have a database where I store all the subdomains of all in-scope TLDs of that program. I continuously perform subdomain enumeration on all the in-scope TLD’s using my custom script which basically runs multiple subdomain enumeration tools, sorts the unique items and combines the result in a single txt file, which then I store in my database. So I collected list of subdomains of that target and the count was almost 10k and then resolved them using PureDNS & probed the live subdomains using httpx.

Press enter or click to view image in full size
Here’s an example of how the script works.
The Discovery:

Now I had almost 5k live subdomains of the target, then to find the login panels and admin portals I decided to run the nuclei using the exposed-panels templates. I used the following nuclei command for this:

nuclei -t /root/nuclei-templates/http/exposed-panels/ -l justynot.com-all-resolved.txt | anew panels.txt

After the command ran successfully I started observing the results one by one carefully, and whenever I saw some panel which was new to me I kept note of that name & copied that subdomain URL in a notepad for further research. Now I had 6 subdomains which were running some third party software and the first login panel was named “Kalcium Web”, then I googled about the default credentials of that panel but I did not find any such credentials. But out of curiosity I tried the most common default credential which is admin:admin and guess what? I found myself logged into the Kalcium Web login panel, equipped with full admin privileges!

Press enter or click to view image in full size
The login panel looked like this one.

After this, my excitement soared to such heights that I couldn’t control my laughter. However, reigning in my emotions, I persisted in the quest for additional admin panel access. Exploring further from the list, I stumbled upon a login panel, a customer portal application. Unlike third-party software, I couldn’t rely on default credentials found through a simple google search. Though I attempted the same credentials, this time around, they predictably failed. No surprises there — I’ve long known I’m not the luckiest person around! 😂

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Persistence pays off! Despite initial setbacks, I continued trying various common username and password combinations but any of them didn’t work. Then, I took a closer look at the application’s technology stack and discovered it was running on AngularJS. Whenever I encounter applications on AngularJS or NodeJS, I instinctively attempt response manipulation, a tactic that has proven successful for me numerous times before. I launched my Burp Suite, inputting “admin” as the username and “password” as the password. I captured that request and also the response of that request, which showed a 401 Unauthorized error. Though the response body contained parameters, I overlooked them and proceeded to change the 401 Unauthorized status to 200 OK. Upon forwarding the request, the outcome was astounding — I gained access to the customer portal as an admin, obtaining unrestricted access to all their users’ personally identifiable information (PII) data!

The thrill escalated to another level similar to Vegeta ascending from Super Saiyan to Super Saiyan God! 😂 Much to my amazement, there were three additional customer portals. Employing the same technique, I attempted access, and once more, it yielded success! I secured entry into three more admin panels, each granting full administrative privileges and unrestricted access to multiple users’ personally identifiable information (PII) data! I was like:

After carefully documenting all the proofs of concept (POCs) in great detail, I created comprehensive reports and promptly submitted them to the program. To my satisfaction, each report received due attention and was triaged accordingly. Interestingly, one particular report, which contained more sensitive data compared to the others, caught the program’s immediate attention. As a result, I was rewarded with a $500 bounty — talk about an exciting turn of events! 😁 Now, I’m eagerly anticipating the bounties for the remaining reports; the excitement is real! 😂

Press enter or click to view image in full size

I hope this write-up provided you with some new insights! If you have any questions or want to discuss further, feel free to reach out to me here. If you found this write-up enjoyable and informative, please do give a clap or share with your friends this would be greatly appreciated. Thank you for your time!

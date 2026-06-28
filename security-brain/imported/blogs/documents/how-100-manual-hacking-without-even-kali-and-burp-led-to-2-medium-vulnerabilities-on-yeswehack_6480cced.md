---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-05_how-100-manual-hacking-without-even-kali-and-burp-led-to-2-medium-vulnerabilitie.md
original_filename: 2024-09-05_how-100-manual-hacking-without-even-kali-and-burp-led-to-2-medium-vulnerabilitie.md
title: How 100% Manual Hacking (Without Even Kali And Burp) Led To 2 Medium Vulnerabilities
  On YesWeHack
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 6480cced1110bed7d3b000e5d769fd517e5efcc729951a1bd93ff8da00cb94a6
text_sha256: 73075557c92c266107af651703e8f309f6e17d79bab6da661382ace2fbce4c33
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# How 100% Manual Hacking (Without Even Kali And Burp) Led To 2 Medium Vulnerabilities On YesWeHack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-05_how-100-manual-hacking-without-even-kali-and-burp-led-to-2-medium-vulnerabilitie.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `6480cced1110bed7d3b000e5d769fd517e5efcc729951a1bd93ff8da00cb94a6`
- Text SHA256: `73075557c92c266107af651703e8f309f6e17d79bab6da661382ace2fbce4c33`


## Content

---
title: "How 100% Manual Hacking (Without Even Kali And Burp) Led To 2 Medium Vulnerabilities On YesWeHack"
url: "https://medium.com/@manan_sanghvi/how-100-manual-hacking-without-even-kali-and-burp-led-to-2-medium-vulnerabilities-on-yeswehack-bbda00fcd84e"
authors: ["Manan Sanghvi (@An____Anonymous)"]
bugs: ["XSS"]
publication_date: "2024-09-05"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 16
scraped_via: "browseros"
---

# How 100% Manual Hacking (Without Even Kali And Burp) Led To 2 Medium Vulnerabilities On YesWeHack

Top highlight

How 100% Manual Hacking (Without Even Kali And Burp) Led To 2 Medium Vulnerabilities On YesWeHack
Manan Sanghvi
Follow
4 min read
·
Sep 5, 2024

549

11

Hello Folks, and welcome back! I’m Manan Sanghvi. I’m excited to share another Write-Up with you today.

Press enter or click to view image in full size

If you’re a beginner, this Write-Up is perfect for you. You’ll learn something new about how to perform good reconnaissance through Google Dorking .

Before that, if you haven’t read my previous write-ups, I highly recommend checking them out. You’ll find valuable insights and experiences that can help you on your journey.

For those who haven’t seen it yet, my first write-up is titled: “In under age (<18), How I Hacked Multi- Billion-Dollar-Corp and got first 4 fig. $2600 Bounty!” Make sure to give it a read — it’s an exciting story that marked the beginning of my journey in hacking.

In under age (<18), How I Hacked Multi- Billion-Dollar-Corp and got first 4 fig. $2600 Bounty!
👋 Hello, I am Manan Sanghvi, and this is my first write up on how, at under age ( <18 ), I got my first 4 figure $$$$…

medium.com

So, back to the topic. I was hacking a very large target with numerous subdomains and services in scope for hacking on YesWeHack. Although this is a public program, I won’t be disclosing the name of the program.

I started by looking for subdomains for *.target.com using Google Dorking. My approach is a bit unique compared to what most people do. Typically, people might search like this: site:*.target.com or site:*.*.*.target.com (especially for larger scopes). These mathods are also good but I combine everything and try a different type of dorks:

site:*<*.target.*

site:*<-*.target.*

site:*>*.target.*

site:*->*.target.*

site:*<->*.target.*

In Normal approach you can see that

Press enter or click to view image in full size

And in my approach:

Press enter or click to view image in full size

You can clearly see some small differences in those dorks. To find juicy subdomains, I used a specific dorks on that target, which looked something like this:

site:*<*.target.com intext:"login" | intitle:"login" | inurl:"login" | intext:"username" | intitle:"username" | inurl:"username" | intext:"password" | intitle:"password" | inurl:"password"

You will able see the some different subdomains which has login panels. Now, In that target I found 2 juicy subdomains which has search bar on home page.

Get Manan Sanghvi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, everyone asks me where and how I start looking for XSS vulnerabilities, so here’s my process: I first combine various tags and special characters (abc ' " } < > ; // # -) into a single search to understand how the web application responds to each one. For example, I might input something like this:

abc’ “ ><>#; — —

This is always my first step when testing for XSS. The goal is to see how the website handles different characters and whether it uses any Web Application Firewall (WAF) or encoding that might interfere with the injection. In this case, I put my payload in search bar on both subdomains and I found that there was nothing in place that could block my attempts. This is output I got In one subdomain:

Press enter or click to view image in full size

And in second subdomain:

Press enter or click to view image in full size

You can see that there is not output encoding. So I think I should spend some more time on this and I created custom payload

abc’”><><img src=1 onerror=alert(document.cookie)>

This is my all-time favorite payload for testing XSS. I’ve found numerous vulnerabilities using just this one line of code.

Here is a Pop Up I Got:

Press enter or click to view image in full size
Press enter or click to view image in full size

Then I reported to YesWeHack and It was Accepted:

Press enter or click to view image in full size
Press enter or click to view image in full size

I hope you enjoyed this write-up! If you found it helpful, feel free to connect with me on LinkedIn or Twitter.

Follow Me On Linked in (Most Active):

https://www.linkedin.com/in/manan-sanghvi-799863176/

Follow Me On Twitter:

https://twitter.com/An____Anonymous

Thank You.

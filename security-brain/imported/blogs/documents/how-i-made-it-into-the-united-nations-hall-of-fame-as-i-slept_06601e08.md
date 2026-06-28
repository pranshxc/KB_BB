---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-25_how-i-made-it-into-the-united-nations-hall-of-fame-as-i-slept.md
original_filename: 2022-05-25_how-i-made-it-into-the-united-nations-hall-of-fame-as-i-slept.md
title: How I made it into the United Nations hall of fame as I slept
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
language: en
raw_sha256: 06601e08272b456a64f3668cbec7049b0ce77e64fdc52f09715f4aed3f75f592
text_sha256: f7ecbd889a4a62d6b175dff52c4e84bff800de1573a081110f43d63a01612860
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How I made it into the United Nations hall of fame as I slept

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-25_how-i-made-it-into-the-united-nations-hall-of-fame-as-i-slept.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `06601e08272b456a64f3668cbec7049b0ce77e64fdc52f09715f4aed3f75f592`
- Text SHA256: `f7ecbd889a4a62d6b175dff52c4e84bff800de1573a081110f43d63a01612860`


## Content

---
title: "How I made it into the United Nations hall of fame as I slept"
url: "https://vikaran101.medium.com/how-i-made-it-into-the-united-nations-hall-of-fame-as-i-slept-f567c90be227"
authors: ["Vikaran (@vikaran101)"]
programs: ["United Nations"]
bugs: ["XSS"]
publication_date: "2022-05-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2610
scraped_via: "browseros"
---

# How I made it into the United Nations hall of fame as I slept

How I made it into the United Nations hall of fame as I slept
Vikaran
Follow
4 min read
·
May 26, 2022

302

4

Press enter or click to view image in full size

This article is going to be about how I got my name in the United Nations hall of fame for finding a reflected XSS bug as I slept.

If you are a beginner in bug hunting you must've read a ton of articles for understanding XSS bugs and finding them. Me too!

The classic methodology to find them is…

collect all the URLs from ‘waybackurls’ or ‘gau’
select all the links that require parameters(have ‘=’ in them)
parse all the links to ‘kxss’ and look for the links that dont unfilter characters like <,>,”,’
target those links and try to inject code on those parameters(for the basic methodology of finding XSS read https://vikaran101.medium.com/reflected-xss-on-byjus-my-first-bug-a5bbab098748)

Using all these points to form a one-liner(‘qsreplace’ here helps in parsing the unique links to kxss and saveing time)…

waybackurls un.org | grep = | qsreplace test | kxss

But the basic methodology is a little longer(collecting all alive domains, taking screenshots etc).

Recon tasks like this are long and boring and I always spent the first half-hour of hunting, where my concentration is at its max to run such boring and repetitive tasks. Also, a lot of long scans would be interrupted due to problems like the network and battery.

Setting up a Virtual Private Server

The solutions to these problems were quite easy. To solve the 2nd problem, I decided to use a VPS from Digital Ocean. I set up a Linux server and installed the necessary tools. Ran the commands inside a ‘tmux’ pane so that my sessions would be saved even if I log out.

Press enter or click to view image in full size
Weaponising Waybackurls

As I ran waybackurls on the target, I noticed something very weird about the tool.

Case 1: If I run waybackurls on un.org for all the subs I get web archive links for that domain from all the subdomain.

>> waybackurls un.org
un.org/eg0
un.org/eg1
un.org/eg2
x.un.org/eg0
x.un.org/eg1
y.un.org/eg0

In the example you see above I get only 2 results from ‘x.un.org’ but in case 2…

Get Vikaran’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Case 2: Running ‘waybackurls’ only on ‘x.un.org’

>> waybackurls x.un.org
x.un.org/eg0
x.un.org/eg1
x.un.org/eg2
x.un.org/eg3
x.un.org/eg4

I realised that I get more results for a given subdomain if I give it separately to the tool. This meant that to increase my attack surface, I must run waybackurls on every subdomain. It is not like I have the patience to do that, so I decided to code a script for it.

Press enter or click to view image in full size
5-minute code to get the links from all domains(try threading to speed up the process)

I added this code along with some other code to collect domains from tools like ‘subfinder’, ‘amass’ and ‘findomain’. Then to extract all the alive domains from ‘http’, then use that list to give to the ‘recursive_wayback()’. Once the list was created I piped it to ‘kxss’. Once I had the list of all the URLs with their list of unfiltered characters, I was free to look for points vulnerable to reflected XSS.

Finding XSS

I started the scan before I went to sleep. When I woke after ̶8̶ 6 hours the report was ready.

Press enter or click to view image in full size
Simple grep to instantly find vulnerable parameters

Once I found that the ‘redirectTo’ parameter doesn't filter <,>,”,’, I knew I could trigger an XSS vulnerability.

Press enter or click to view image in full size
Press enter or click to view image in full size
XSS!

Reported: 16th April 2022

Fixed: 21st April 2022

Acknowledged: 25th April 2022

Press enter or click to view image in full size
Done!

Twitter: https://twitter.com/vikaran101

If you enjoyed the blog, feel free to clap and follow me on Twitter.

Thank you.

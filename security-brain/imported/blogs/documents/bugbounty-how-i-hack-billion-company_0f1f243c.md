---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-15_bugbounty-how-i-hack-billion-company.md
original_filename: 2019-01-15_bugbounty-how-i-hack-billion-company.md
title: '#BugBounty How I Hack Billion $ Company'
category: documents
detected_topics:
- idor
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- idor
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: 0f1f243c8247464a76e0f6be97e44cc29efb781c26c83532e9b9f444cfa76aab
text_sha256: 44b19686accc0ad77c5ba58edb41ec3061ca35d6287ea898b3377817cba9a609
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty How I Hack Billion $ Company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-15_bugbounty-how-i-hack-billion-company.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0f1f243c8247464a76e0f6be97e44cc29efb781c26c83532e9b9f444cfa76aab`
- Text SHA256: `44b19686accc0ad77c5ba58edb41ec3061ca35d6287ea898b3377817cba9a609`


## Content

---
title: "#BugBounty How I Hack Billion $ Company"
url: "https://medium.com/@sadiqwest01/bugbounty-how-i-hack-billion-company-5529a3ebe999"
authors: ["Sadiq West"]
bugs: ["Directory listing"]
bounty: "500"
publication_date: "2019-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5475
scraped_via: "browseros"
---

# #BugBounty How I Hack Billion $ Company

Sadiq West
Follow
5 min read
·
Jan 15, 2019

380

4

#BugBounty How I Hack Billion $ Company

A very simple to any pentester, but most ’em show no care about it and yet critical vulnerability to the company, i know it wasn’t very hard to discover but i am writing this one down just to express my methodology. So as always, I initiated with reconnaissance on this website, I’m not an expert and there will probably be some elements that you would miss while making reconnaissance on your target .

I have been trying to earn a seat in Giant company Hall of Fame by finding at least one valid security vulnerability. I tried whenever I had free time at night,so i don’t ever get enough time for hacking i only do it on my free time.This is not a super hack, merely its just a matter of luckkkkk……

I have been trying to find a valid vulnerability in the giant company i know with the hope of discovering some low hanging fruit. i ended-up getting an Xss,and subdomain takeover because i was born from this family. I came across a Online Investment while surfing google

So this post is for the Noobs like me, I will call [REDACTED.COM] to represent the website as i can not disclose the website’s name. but its one of the giant Saudi Arabian base Investment Company as they claim the name even though the owners of the website hide their identity.

Lets the game start; So I signed up and started testing it. The platform was highly vulnerable, to alot of vulnerability like XSS,IDOR,SQL I was surprised to see that a platform having billion of $ is vulnerable to these type of Vulnerabilities,The bug which helped me to download the whole company source code: [i.e script] which contain the company owners identity,company stripe,paypal,ravepay account

an xss from the redacted
Press enter or click to view image in full size

You know how noobs feel when they found a valid bug it was like

hacking the planet

After searching for so long for over 30 days I had found nothing BUT only an XSS,SQL,IDOR. i keept visiting the platform because i invested my money out there, so I had to stop and start learning a bit more how the platform works because i believe that “the higher the risk the higher the profit”

Press enter or click to view image in full size

After over my 30 days been in the platform, i keep i mind that lets try an ethical way again. this time i use what most security researchers forget to do which is i call it “The power of Dirseacrh”

Target: http://redacted.com
[08:35:15] 200–87MB — /new -> http://redacted.com/new/
[08:35:15] 200–235B — /.git
[08:35:16] 200–235B — /plugins.log

This Directory really suprise me, with a file worth 87Mb which make me think either the Developers are lazy, or just busy i quckly run a dirsearch again and i found the name of the file is web.zip

Press enter or click to view image in full size
source code

i was like

I got the whole company source code which allow me to run a website similar to the platform.

Get Sadiq West’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i quckly write a report to the company Email id: i got no response within 7 days, i then desite to report it to the company telegram channel.

That whas the Bug that change my life completely turn my life from a poor kid to a rich kid, the question is how can a company whom they hide their identity decite to pay me such huge bounty by just finding such issues? are they trying to bribe me to kept hiding their identity hence it was an online investment.

As i know most online investment scheme won’t last for over 1 year, but when i look unto how they trade with billions of $ i show no care.

Press enter or click to view image in full size

What to learn from this write-up ?::

Always dig deeper in web application.There is always something fruitful.
Make a directory search using dirsearch on your target, you might be lucky.
Be patient;;;;

At the End: on the other hand i will give this write-up a tittle “the power of dirsearch”

Bug report:26/04/2018

Patched:1/05/2018

Bounty awarded: $500,000 18/05/2018

Remember: i am writing this down not to convice you to believe either i got it or not: just to let you know about “dirsearch: thats it, you have that right to believe it or not, and i have that right to enjoy my Bounty:::

TRY TO KICK THE ASS OF THOSE HUNGRY ENTREPRENEUR RUNNING SUCH ONLINE INVESTMENT, AN SEE IT FOR YOURSELF

You can find me on twitter Sadiq_West

Hey 👋If you found my post usefull, show some ❤️ . You can now buy me a coffee!

https://www.buymeacoffee.com/sadiq

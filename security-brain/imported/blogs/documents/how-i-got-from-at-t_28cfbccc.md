---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-07_how-i-got-from-att.md
original_filename: 2023-09-07_how-i-got-from-att.md
title: How I got $$$ from AT&T
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 28cfbccc567da826685ac5f48b92f9e9fbb301c707f6f44ed84d4b5eb0cd787f
text_sha256: 1da7203f6a5a1c03102d2833c631e82b9e3d612c3edbf27acf77f0f40beca069
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $$$ from AT&T

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-07_how-i-got-from-att.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `28cfbccc567da826685ac5f48b92f9e9fbb301c707f6f44ed84d4b5eb0cd787f`
- Text SHA256: `1da7203f6a5a1c03102d2833c631e82b9e3d612c3edbf27acf77f0f40beca069`


## Content

---
title: "How I got $$$ from AT&T"
url: "https://medium.com/@nomad8061/how-i-got-from-my-first-valid-bug-17462f94c827"
authors: ["Ahmed Badry"]
programs: ["AT&T"]
bugs: ["Missing authentication"]
publication_date: "2023-09-07"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 799
scraped_via: "browseros"
---

# How I got $$$ from AT&T

Top highlight

Ahmed Badry
Follow
4 min read
·
Sep 7, 2023

316

8

How I got $$$ from AT&T
Press enter or click to view image in full size

Hello Geeks

Today I will tell you about my first valid Bug in my Bugbunty journey how i got $$$ Bounty

First of all when I started Bugbunty I seen all newcamers search for xss vurnlablity and I also I did that and I got dublicat so after that I decide to not search for xss any more.

Then I thought about where I could look in places where not many Hunters search, and then I saw Godfather Orwa videos about Recon so after that
I just focused on Shodan and I picked wild scope target like AT&T .

So our Target is [att.com]

I used 2 Dorks

Ssl.cert.subject.CN:”att.com”

ssl:”AT&T Services Inc.”

here you should put just ssl if you don’t know how to get ssl for any Target its easy i will tell you the way

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

remove comma , Because if you didn’t remove it you will get all shodan search result

Press enter or click to view image in full size

without comma ,

Press enter or click to view image in full size

then i searched with http.title and i opened all pages and ips to see what behind them

Press enter or click to view image in full size

After a lot of searching I found this dashboard open on the IP like that https://50.90.000.67

Press enter or click to view image in full size

The first thing I thought of was trying to find any endpoint

i used dirsearch with this command

python3 dirsearch.py -u https://50.90.000.67 

But I didn’t get anything

Get Ahmed Badry’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

after that i used ffuf with Big Wordlist with this command

ffuf -w /path/to/mywordlist -u https://50.90.000.67/FUZZ

But I didn’t get anything again lol

after that i searched for any CVE but i didn’t find any thing

I asked my friends if anyone had seen this dashboard before

No one has seen it before

I was hesitant because the IP is connected to another domain, but it is not affiliated with an AT&T company see below picture

Press enter or click to view image in full size

it was not *.att.com but was another name like *.NOMAD.com

I asked myself if this IP address was not affiliated with an AT&T company

why i see AT&T ssl certificate on this dashboard

so after 1 week of searshing i decided submit it

Sorry I forgot to clarify something

what i wrote in impact section?

I was able to access open Oracle dashbord without authentication

and i can see information about Weblogic Server like Enterprise manager and Configuration Administration and operation and Web Services just i can read it i can’t take any action you can see red guide line below

Press enter or click to view image in full size

i submitted the report in

the report triaged after 6 days

Press enter or click to view image in full size

i got Bounty on Mar

Press enter or click to view image in full size

I know it’s been seven months since, but I stopped hunting to hone my coding skills, and now I’m going to focus on hunting. I hope my first article is good.

You can follow me on Twitter and Facebook. I will post useful information soon

https://www.linkedin.com/in/ahmed-badryjl/

JavaScript is not available.
Edit description

twitter.com

https://www.facebook.com/profile.php?id=100085210021256

Ahmed Badry
Ahmed Badry is on Facebook. Join Facebook to connect with Ahmed Badry and others you may know. Facebook gives people…

www.facebook.com

CuriousCat
Edit description

curiouscat.live

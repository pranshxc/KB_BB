---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-05-22_hacking-the-nhs-for-fun-and-no-profit.md
original_filename: 2017-05-22_hacking-the-nhs-for-fun-and-no-profit.md
title: Hacking the NHS for Fun and No Profit
category: documents
detected_topics:
- path-traversal
- xss
- sqli
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- path-traversal
- xss
- sqli
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 15edf1511d25b23c5647720596d343e9d558f27ac4b3f5f9fc450eea4f2e8a70
text_sha256: ad1004c52ea7a424a36892a61404f6ce748373cadb76a5021cdedf528f7a7d2e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Hacking the NHS for Fun and No Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-05-22_hacking-the-nhs-for-fun-and-no-profit.md
- Source Type: markdown
- Detected Topics: path-traversal, xss, sqli, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `15edf1511d25b23c5647720596d343e9d558f27ac4b3f5f9fc450eea4f2e8a70`
- Text SHA256: `ad1004c52ea7a424a36892a61404f6ce748373cadb76a5021cdedf528f7a7d2e`


## Content

---
title: "Hacking the NHS for Fun and No Profit"
url: "https://medium.com/@nmalcolm/hacking-the-nhs-for-fun-and-no-profit-90931029dcb4"
authors: ["Nathan (@NathOnSecurity)"]
programs: ["NHS"]
bugs: ["SQL injection", "LFI"]
publication_date: "2017-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6196
scraped_via: "browseros"
---

# Hacking the NHS for Fun and No Profit

Hacking the NHS for Fun and No Profit
Nathan
Follow
6 min read
·
May 22, 2017

14

SMB not required.

Press enter or click to view image in full size
Still not sorry for the shitty stock art.

On the 25th of October, 2016, I woke up and thought to myself “How easy would it be to hack the NHS?”. By lunch time I was writing a report.

I started by looking on Shodan for any Internet-facing machines which might be of interest. It came to my attention that the NHS had its own ASN (AS41373 — NATIONAL HEALTH SERVICE) which made my quest far easier. Shodan has an ASN filter to limit results to a specific ASN. After a few minutes I discovered a webserver (194.176.105.219, also known as monitor.nhs.uk) with a simple login form. From here I could have gone multiple routes, but I decided to test for SQL injection first. My favorite tool for the job is sqlmap, a powerful open source toolkit for detecting and exploiting SQL injection vulnerabilities.

$ python sqlmap.py -u 'https://194.176.105.219/login.php' --random-agent --data='username=test&password=***REDACTED*** --batch --dbs

I wasn’t hopeful, but it was worth a shot, and it certainly paid off.

POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 454 HTTP(s) requests:
---
Parameter: username (POST)
  Type: boolean-based blind
  Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
  Payload: username=test' RLIKE (SELECT (CASE WHEN (3915=3915) THEN 0x74657374 ELSE 0x28 END))-- MgVq&password=***REDACTED***
Type: error-based
  Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
  Payload: username=test' AND (SELECT 5095 FROM(SELECT COUNT(*),CONCAT(0x716b707171,(SELECT (ELT(5095=5095,1))),0x716b7a6a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- ppwP&password=***REDACTED***
Type: AND/OR time-based blind
  Title: MySQL <= 5.0.11 OR time-based blind (heavy query)
  Payload: username=test' OR 4720=BENCHMARK(5000000,MD5(0x6d7a554b))-- GVLM&password=***REDACTED***
---

sqlmap detected the “username” parameter was vulnerable to SQL injection, and proceeded to list the databases with ease. Curious how much damage could be done, I began exploring the primary database and unsurprisingly found a “users” table. It had 73 rows, so clearly access was limited to a select number of people. The first user was the person who originally wrote the application, a consultant from the UK. I could tell straight away the passwords were hashed with MD5, and sqlmap automatically cracked the hash for me. His password was “test”.

It’s pronounced jif.

Using his username and password, I proceeded to login to the application.

The “home” page displayed after logging in.

Let’s backup for a second — What the fuck is N3, anyway? Why is there a BT share price graph?

N3 is the national broadband network for the English National Health Service (NHS), connecting all NHS locations and 1.3 million employees across England. In 2004, BT was awarded the contract to deliver and manage the IT project on behalf of the NHS. N3 was preceded by NHSnet, becoming N3 in 2006. — Wikipedia

Oh.

It’s still pronounced jif.

I had just hacked the monitoring tool of the N3 Internet gateway. Not only was I logged in, but I was logged into the application as a privileged administrator. I had the ability to manage users, edit configurations, execute system commands, and more, all from a leftover developer account with a password weak enough to guess.

Press enter or click to view image in full size

The other users in the database were BT employees, some of who were indeed using weak passwords too.

Get Nathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The application was loaded with many tools. I could view gateway metrics (Broadband, DNS infrastructure, VPN tunnels, Firewalls, etc), visualize traffic (GCSX, datacenters, PoPs, gateways, etc), view logs, HTTP probes, and alerts, look up N3 IP addresses, and much more. Although I’m limited to what I can share, here’s a few things I found.

Local file inclusion in the log viewer

I was able to read arbitrary files from the filesystem, including source code. Having read the system hosts file I saw some other interesting machines on the network, though I didn’t go as far as to probe them.

The log viewer limited how many lines I could view, but fortunately for me I discovered a simple but notable slip up…

Source code disclosure

The server had directory indexes enabled, which allowed me to view the contents of the “includes” directory. Someone had made a backup copy of “common.inc.php” and named it “common.inc.php.old”. The server (rightly) didn’t recognize this extension, and prompted me to download the file instead. It’s quite common (no pun intended) for developers to append “.old” or “.bak” to older file revisions, however these files are easily enumerated and can pose a serious risk. It’s messy and lazy, and they should never make their way into production.

I didn’t bother to look for any more SQL injection or XSS vulnerabilities as I had already come to the conclusion the application should be nuked from orbit. I’d be surprised if the application hadn’t already been hacked in the past.

I first reached out to the consultant, however to this day I still haven’t received a reply. I next contacted a BT employee who was a user of the application, and he passed my message along to BTCERT who contacted me the next day.

I wrote up a report of everything I had found and sent it along, and I received a reply a few hours later stating they had taken the application down.

I’m pleased with BT’s response to the situation, and please to hear they have a incident response plan. There’s lots to take away from this post, but the main points are:

You don’t need NSA exploits to breach sensitive systems. A chain is only as strong as its weakest link.
Know your assets, and know them well. If you’re not in control, who is?
Don’t allow your internal applications to face the Internet, even if they require authentication.

Unlike my previous post, Hacking Imgur for Fun and Profit, my only goal here was to have fun and see where my curiosity took me. The NHS provides myself, my family, and my friends with free healthcare, and it’s vital services such as the NHS are adequately protected.

If you liked this post, give me a follow on Twitter for more security talk and memes.

Thanks for reading.

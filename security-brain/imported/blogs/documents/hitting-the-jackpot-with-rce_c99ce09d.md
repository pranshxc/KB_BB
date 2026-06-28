---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-25_hitting-the-jackpot-with-rce.md
original_filename: 2024-08-25_hitting-the-jackpot-with-rce.md
title: Hitting the jackpot with RCE!
category: documents
detected_topics:
- idor
- command-injection
- file-upload
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- file-upload
- rate-limit
- api-security
language: en
raw_sha256: c99ce09dfdd3ac76590561f34970c1f7b5f085fff0ceadf1ed9a83b523073a1e
text_sha256: bdd0d0e4b9ca379ab7e67b2192f1e363d0e70761bc7004f5db5d2d90c98b16fd
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Hitting the jackpot with RCE!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-25_hitting-the-jackpot-with-rce.md
- Source Type: markdown
- Detected Topics: idor, command-injection, file-upload, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `c99ce09dfdd3ac76590561f34970c1f7b5f085fff0ceadf1ed9a83b523073a1e`
- Text SHA256: `bdd0d0e4b9ca379ab7e67b2192f1e363d0e70761bc7004f5db5d2d90c98b16fd`


## Content

---
title: "Hitting the jackpot with RCE!"
url: "https://medium.com/@gokulsspace/hitting-the-jackpot-with-rce-43755cac1415"
authors: ["Gokulsspace (@GokTest)"]
bugs: ["RCE", "Unrestricted file upload"]
bounty: "1,500"
publication_date: "2024-08-25"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 45
scraped_via: "browseros"
---

# Hitting the jackpot with RCE!

Hitting the jackpot with RCE!
Gokulsspace
Follow
3 min read
·
Aug 26, 2024

731

10

Hey, so everyone was pushing me to write another write-up after the acceptance of my first ever bug bounty write up. So if you haven’t already read it please have a look at it here: https://medium.com/@gokulsspace/the-30000-bounty-affair-3f025ee6b834

I am a very lazy person and writing such reports and write-ups are very hectic to me. So excuse my time gap for writing them.

So here I am with another RCE story, my second RCE in the year 2023. So, as I was digging up some hosts of a company, let’s call it redacted.com as always, I came across few interesting subdomains. Whatever we are doing here, the major part of it is recon and be a legend in finding those hidden assets of a company. I don’t care about what tools you use. Subfinder, Amass, knockpy, securitytrails whatever. But, make sure that you have found that one treasury of bugs. It may be a single subdomain or multiple subdomains or may be an IP which isn’t that interesting for you.

So, when we do the subdomain enumeration we will come across a huge list of them especially when it is giant of a company. The most interesting subdomains or IPs you come across includes default pages of Ngnix, Apache, Redhat whatever. So be on the lookout of such pages especially Ngnix.

When I come across one such page, I decided to FUZZ it with my wordlist to enumerate if there is any hidden paths or files are available. Interestingly, I wasn’t wrong and found a path called test. More like http://redacted.com/test/

It was a messy endpoint and developer did some nasty works inside it for testing purpose. So there was few options to upload files also.

Press enter or click to view image in full size

You may have come across on such instances but uploading a file other than the image or doc file might be hectic and you try to bypass the upload restrictions with various ideas and will end up failing to do so. But here it was simple because it was a developer’s playground. He hangs out there on his free time and no restrictions to upload any kind of files.

Yeah, you guessed it write. PHP files for the rescue!!! I tried uploading a random php file called test.php on this endpoint and succeeded. Later, I checked where this file is gonna stored. So again Fuzzed the endpoint http://redacted.com/test/ and found an index of uploaded files on this path: http://redacted.com/test/plain/uploads . There I saw my boy test.php.

Now, I got excited and wasted no time to finish this dirty job. I created another php file called rce.php with one of the dangerous payload that is available <?php system($_GET[“cmd”]);?>

Get Gokulsspace’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The code snippet <?php system($_GET["cmd"]);?> is a simple PHP script that can be very dangerous if deployed on a live web server. It takes a command from the URL (via the cmd GET parameter) and executes it on the server.

So, I uploaded it and went to http://redacted.com/test/plain/uploads to see the file rce.php. Now, the job is almost done. I Just executed those magical commands to verify the RCE by adding cmd parameter. Like this:

http://redacted.com/test/plain/uploads/rce.php?cmd=whoami

Press enter or click to view image in full size

http://redacted.com/test/plain/uploads/rce.php?cmd=ls%20-la

Press enter or click to view image in full size

So that’s it. The target was not a main scope of the program. So they adjusted the bounty to be a little low.

Press enter or click to view image in full size

Hope you guys learned something from this and if you liked it please share it on your social medias and give me a follow here. Thank you!

My linkedin: https://www.linkedin.com/in/gokul-sudhakar-72a93923a/

X: https://x.com/GokTest

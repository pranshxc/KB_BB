---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-26_from-ctfs-to-bug-bounty-booty.md
original_filename: 2018-11-26_from-ctfs-to-bug-bounty-booty.md
title: From CTFs to Bug Bounty Booty
category: documents
detected_topics:
- information-disclosure
- sso
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- information-disclosure
- sso
- sqli
- command-injection
- api-security
language: en
raw_sha256: 3be2ede462aa647b0f56e183a04e3474e5e3b716e275e3ff0232034aa05559fe
text_sha256: 6c9eb851b531389bee3a6b75137a7348efe11e085dfd956303cbe6a15ce87908
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# From CTFs to Bug Bounty Booty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-26_from-ctfs-to-bug-bounty-booty.md
- Source Type: markdown
- Detected Topics: information-disclosure, sso, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `3be2ede462aa647b0f56e183a04e3474e5e3b716e275e3ff0232034aa05559fe`
- Text SHA256: `6c9eb851b531389bee3a6b75137a7348efe11e085dfd956303cbe6a15ce87908`


## Content

---
title: "From CTFs to Bug Bounty Booty"
url: "https://medium.com/@benjitobias/from-ctfs-to-bug-bounty-booty-81bab999b70d"
authors: ["Benji Tobias"]
programs: ["Tailor Store"]
bugs: ["Information disclosure"]
bounty: "200"
publication_date: "2018-11-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5565
scraped_via: "browseros"
---

# From CTFs to Bug Bounty Booty

From CTFs to Bug Bounty Booty
Benji Tobias
Follow
6 min read
·
Nov 26, 2018

361

2

boo·ty /ˈbo͞odē/

noun

something gained or won

While watching some YouTube videos over the weekend I came across a website for custom designing shirts. Being a sucker for almost anything customised I started to have a look and sent it to a friend. After he noted the high level of design the website had, I jokingly said “Yep, now I just have to find an SQLi”.

While I’ve never attempted bug bounty hunting and I’m not really a web expert, I have participated in a few CTFs and have recently been reading a bit more about web hacking.

I didn’t intend to put that much effort in because I didn’t actually think I’d find anything and I was working on some other project so I decided to start simple; find subdomains.

Sublist3r.py returned 28 subdomains, most of them didn’t seem interesting to me, cdn[1–6].tailorstore.com, dyn[1–4].tailorstore.com bla bla bla. I had a look at some of the others until I browsed to office.tailorstore.com and was hit with an invalid certificate.

Having a misconfigured certificate made me curious as to what else may be badly configured here so I accepted the risk to continue but required basic authentication to continue. I obviously don’t have any credentials and got a 401 page. What do?

That’s, err, not gonna happen

Based on the use of basic authentication and the misconfigured certificate and challenges from CTFs I decided to try my luck and guessed for a .git folder.

Press enter or click to view image in full size

Hold on, that was 401 and now I got a 403. .git exists it seems. Let’s confirm. I browsed to .giss and get a 401 and then to really confirm I browse to .git/HEAD. Chrome downloads a file and I start to grin.

I can now access git internal files and therefore, I can access git objects. I won’t go into too much detail on git internals but I’ll link some sources I used at the end if you want to learn more. Also, this is more about the methodology of how I rebuilt it, not a lesson on git (of which I am no expert) so I may have misexplained the internals, don’t quote me on it.

Anyway, this is actually a very typical CTF challenge; restore the files from a repo. The process is essentially finding the hashes of the objects and then getting the objects.

Quick (probably slightly inaccurate) explanation of git objects names: git stores the objects in a directory of which the directory name is the first 2 bytes of the hash and the file name is the rest of the hash. A quick wget to /.git/refs/heads/master contains the hash of the master commit: 040efb92fc0ec4067013a40597dc963dc0118430. So the file I now want is .git/objects/04/0efb92fc0ec4067013a40597dc963dc0118430.

Originally I wrote (read “copied”) a script that would allow me to read the file but eventually I ended up rebuilding the whole repo in order to make things easier and allow me to use git commands.

So now I have the hash of the directory (“tree” in git terms, “blob” is a file).

Get Benji Tobias’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

wget that (.git/objects/82/71eceeb1ad1ba3709f328b8a7a5c0311f37606), git cat-file and I have a directory listing.

api looks interesting. wget, git cat-file (after all of this, these commands have been seared into my screen).

The first thing I looked at here was Product.class.php. Using my trusty wget and git cat-file I get and read the relevant hash path but this time instead of a directory, I’ve pulled a file.

Press enter or click to view image in full size

I have code!

I thought I’d have a look, see if there’s maybe any SQLi or something interesting but all queries were done using an internal method. Ok, class extends DbRenderMethod. Let’s have a look there (I didn’t notice at first that I already have the hash for that file and spent ages looking for it).

I grab the file, ready to search for an SQLi have a look and…

Press enter or click to view image in full size

Full connection details for the DB!

Does this make me a hacker?

This shouldn’t have surprised me because it makes sense that they would be there, I just didn’t think about it at the time.

I stopped here because they don’t have a bug bounty, I didn’t want to get into too much trouble and felt that this was sufficient enough to file a report.

I emailed Tailor Store on a Sunday and by Monday morning received a response. They didn’t have an active bug bounty program but they did offer compensation providing I report a significant issue. I sent them a report, within an hour they had secured the server, credited my account with $200 and given me their blessing to publish a report. I personally was quite impressed with their response time (although I don’t have anything to base it on since it’s my first time).

Press enter or click to view image in full size
I haven’t seen this meme used in a while

All in all it took me less than 2 hours from when I decided to have a look until I had the credentials. Not too shabby if I may say so myself.

This was my first time finding something that wasn’t supposed to be found and I learnt a few things while doing it.

One thing leads to another. The main reason I decided to keep looking at the subdomain was because of the invalid certificate. Had it had been valid I may have moved on to the next subdomain (probably wouldn’t have but that did give me some confidence that I would find something).

100% understanding isn’t necessary. I had some issues with restoring the files from git and didn’t manage to get all of them. Having a deeper understanding of git internals and applying a bit more guesswork would have probably allowed me to get them all but I didn’t need them in the end.

CTFs can be realistic. I see this question popping up a lot but I can now confirm that there is an overlap.

I heavily relied on these links to help me rebuild the repo.

https://en.internetwache.org/dont-publicly-expose-git-or-how-we-downloaded-your-websites-sourcecode-an-analysis-of-alexas-1m-28-07-2015/

https://github.com/ctfs/write-ups-2014/tree/master/9447-ctf-2014/tumorous

https://matthew-brett.github.io/curious-git/reading_git_objects.html

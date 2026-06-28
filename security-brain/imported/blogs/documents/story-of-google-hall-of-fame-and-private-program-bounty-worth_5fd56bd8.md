---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-16_story-of-google-hall-of-fame-and-private-program-bounty-worth-.md
original_filename: 2021-06-16_story-of-google-hall-of-fame-and-private-program-bounty-worth-.md
title: Story of Google Hall of Fame and Private program bounty worth $$$$
category: documents
detected_topics:
- idor
- sqli
- command-injection
- password-reset
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- sqli
- command-injection
- password-reset
- rate-limit
- automation-abuse
language: en
raw_sha256: 5fd56bd8ea5a8e244c27e98dfb6581ab0a3597101b51457ddabff148db4631f0
text_sha256: 5ec0c2b0636fecbc8d72ffaf4f28eb41b7a8c6f61be69e2e771313f84dc46b8c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Story of Google Hall of Fame and Private program bounty worth $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-16_story-of-google-hall-of-fame-and-private-program-bounty-worth-.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection, password-reset, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `5fd56bd8ea5a8e244c27e98dfb6581ab0a3597101b51457ddabff148db4631f0`
- Text SHA256: `5ec0c2b0636fecbc8d72ffaf4f28eb41b7a8c6f61be69e2e771313f84dc46b8c`


## Content

---
title: "Story of Google Hall of Fame and Private program bounty worth $$$$"
url: "https://infosecwriteups.com/story-of-google-hall-of-fame-and-private-program-bounty-worth-53559a95c468"
authors: ["Basavaraj Banakar (@basu_banakar)"]
programs: ["Google"]
bugs: ["Exposed registration page"]
publication_date: "2021-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3570
scraped_via: "browseros"
---

# Story of Google Hall of Fame and Private program bounty worth $$$$

Story of Google Hall of Fame and Private program bounty worth $$$$
Basavaraj Banakar
Follow
4 min read
·
Jun 16, 2021

639

1

Hello Infosec Community myself Basavaraj, this my 2nd writeup, the first one is about Hacking scammers(click here to read), I seen many people getting hall of fames and bounties from google vrp , I thought why should I give a try and successfully got 4 duplicate(and any beginners reading this don't change change your mind when you got dups because it's common for everyone) and started hunting on an acquisition called owl chemylabs (Note: If you are started take acquisition as target please check whether it is solded by google or not first, because you will get acquired information first, rather than solded ,if it is solded then its not google acquisition).

I will not do any recon automation while hunting, I will check everything manually leaving subdomain enumeration and fuzzing, First enumerated all live subdomains and started looking it one by one and a day wasted successfully without getting anything, Next day in shodan I found a target belong to owlchemylabs example search query ssl:target.com 200

Press enter or click to view image in full size

Got two 2 targets having an Login page with title Plastic SCM, Now Opened one link

Plastic SCM: https://en.wikipedia.org/wiki/Plastic_SCM

Press enter or click to view image in full size

Now I got this login panel , Now i tried what every bug hunter tries(checked for default creds,js files,sqli etc) but Got nothing but noticed one thing i.e when I add any password and click on login the URL Changes to https://35.244.187.233/account/login then i removed login in url and added register i.e https://35.244.187.233/account/register Boooom Got an password reset page (This page is occurs when they successfully configure Plastic SCM server and the last step is setting password)

Press enter or click to view image in full size

And I set password as admin and successfully logged in into server.

Press enter or click to view image in full size

And Got, SSL Pfx password and mysql password and i was able to add users and delete users. And i quickly made an POC and reported to google

I tried to increase impact and got nothing that day, and after 3 days also I didn’t got any reply from google and bug is also not accepted , and I am worried too on this report. Now again I started recon on that target and after researching 3 Hours on the target i came across an endpoint https://35.244.187.233/webui/repos that holds private repository codes, after going to that endpoint i got another login page

Press enter or click to view image in full size

Now i tried to login as administrator because i know administrator password but login failed, tried default credentials and sqli and bruteforced login page and this also failed and then i remembered that i came across some users on the server while i logged in as administrator

Press enter or click to view image in full size

Now guess what now i have taken one user who having admin permission and changed his password because i am an administrator.

Press enter or click to view image in full size

and again gone to https://35.244.187.233/webui/repos this time i used the username and password which i changed recently and tried logging in guess what?

Press enter or click to view image in full size

successfully logged in to private code repository having 145 Repositories ,And now suddenly added this comment and got reply from the google vrp within an hour

Press enter or click to view image in full size

And now i felt so happy, And it was an acquisition i got rewarded $$$

Get Basavaraj Banakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I thinked about how to get targets using the same product now i crafted an shodan search query i.e title:”Plastic SCM” (Don’t search now because no targets are there to report😂)and Got two URLs belongs to the one target and they are vulnerable too, they have bug bounty program too and i reported them and they have given an private invite of their program, and they said to report it but they have limited scope only and these two URLs are out of scope and it was critical vulnerability so they marked it as P1 and and waiting for bounty.

Moral of the story : If you got any low level issues please try to increase impact as much as possible by giving much time to that bug.

Google Reported Timeline

Reported: May 16, 2021

Accepted : May 20, 2021

Rewarded: May 25, 2021

Fixed: Jun 7, 2021

Follow me on.

Twitter : https://twitter.com/basu_banakar

Instagram: https://www.instagram.com/basu_banakar/

Website : https://www.basubanakar.com/

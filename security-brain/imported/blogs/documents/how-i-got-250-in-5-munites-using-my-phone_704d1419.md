---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-26_how-i-got-250-in-5-munites-using-my-phone.md
original_filename: 2020-10-26_how-i-got-250-in-5-munites-using-my-phone.md
title: How i got 250$ in 5 munites using my phone
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
raw_sha256: 704d14191a1631fa15d622b06a30cd6615c47c0130921ef89ff12c0e9b1a7a9d
text_sha256: 95fe3d2ac6bdb906e435b7b81eba82070aad7baf633e639571bf129afc8a07e1
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How i got 250$ in 5 munites using my phone

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-26_how-i-got-250-in-5-munites-using-my-phone.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `704d14191a1631fa15d622b06a30cd6615c47c0130921ef89ff12c0e9b1a7a9d`
- Text SHA256: `95fe3d2ac6bdb906e435b7b81eba82070aad7baf633e639571bf129afc8a07e1`


## Content

---
title: "How i got 250$ in 5 munites using my phone"
url: "https://hamzadzworm.medium.com/how-i-got-250-in-5-munites-using-my-phone-91c9b2258282"
authors: ["Abdelkader Mouaz (@hamzadzworm)"]
programs: ["Basecamp"]
bugs: ["HTML injection"]
bounty: "250"
publication_date: "2020-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4178
scraped_via: "browseros"
---

# How i got 250$ in 5 munites using my phone

How i got 250$ in 5 munites using my phone
Hamzadzworm
Follow
3 min read
·
Oct 26, 2020

173

1

Hi , this is my first write up with you in medium and i hope you will like it.

Like everyday i wake up and there was nothing to do, no one to talk with -.-

so i said, lets go to hackerone and take a look in hacktivity maybe there is some new repports, like you know reading repports are better then talking with people :D

and after i read some repports i go to :
https://hackerone.com/directory/programs

to see if there is any new programmes added and i found that one:

Basecamp - Bug Bounty Program | HackerOne
The Basecamp Bug Bounty Program enlists the help of the hacker community at HackerOne to make Basecamp more secure…

hackerone.com

it was recentely added so i go to take a look into it:

Get Hamzadzworm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i signup like any normal user and first thing i notice in settings that i can invite a member to join me in my account so i invite my self with a seconde email
in the invite i can write a sender name so itry to inject an html code in sender name but that didnt work they have filter :’( , i keep searching and i try to accept invite and also nothing new

Press enter or click to view image in full size

i try to inject title, subject, sender name but nothing
untile i see there Decline this inviation like you see in photo,i directly click on it and what i found is that i can make a note for user who invite me why i dont want to join here account so itry on that note to write an html code and it works

Press enter or click to view image in full size

:D NEXT Step was to proof to the security team what i can do with that so itry to give it maximan impact i can let me tell you the senareo:

User A invite user Be to join Hem
User B recive the invite and click decline invitation
when he click decline he’s redirected to a page ask hem to put a note for user A who is the one who invite you on that note you can put anything and user A will recive that you didnt join hem with the note you put,

ithink senareo is clear now:
so on the note user B make an simple <a href=…> code
with simple button, put any thing on button like :
click here to make user B join you or
click here to know why user B didnt join you

And you can redirect hem to malicious a link ask hem to login again
to takeover her account.

Repport Send 14 Oct
Triaged 14 Oct
250$ Bounty awarded 14 Oct

that’s my H1 Profile:
https://hackerone.com/telaviv_h4x0r

Im New at medium So if You Like that write-up follow me :)

That was the impact i give to them, that’s my first write up with you sorry if there is any mistakes, i hope you will like it :).

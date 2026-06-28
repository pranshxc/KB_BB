---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-18_this-is-how-i-was-able-to-hunt-a-rare-bug-in-a-private-program.md
original_filename: 2019-11-18_this-is-how-i-was-able-to-hunt-a-rare-bug-in-a-private-program.md
title: This is How I was able to hunt a rare bug in a private program
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 7acb53a88c96572871cbfac99bfda7ffd8390bed16371e7cd2cff6bd8d2b1b67
text_sha256: 7e07303d44c065ba12263395586bf25ccd45bf3b0f2e341dac5d1d20609c8490
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# This is How I was able to hunt a rare bug in a private program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-18_this-is-how-i-was-able-to-hunt-a-rare-bug-in-a-private-program.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7acb53a88c96572871cbfac99bfda7ffd8390bed16371e7cd2cff6bd8d2b1b67`
- Text SHA256: `7e07303d44c065ba12263395586bf25ccd45bf3b0f2e341dac5d1d20609c8490`


## Content

---
title: "This is How I was able to hunt a rare bug in a private program"
url: "https://medium.com/@abidafahd/how-i-was-able-to-hunt-a-rare-bug-in-a-private-program-caec0ebaef7f"
authors: ["Abida Fahd"]
bugs: ["Missing authentication", "Privilege escalation"]
publication_date: "2019-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4935
scraped_via: "browseros"
---

# This is How I was able to hunt a rare bug in a private program

This is How I was able to hunt a rare bug in a private program
Eddie Mora
Follow
3 min read
·
Nov 21, 2019

35

Hello, this is Eddie Morra and today I will show you how I was able to find a way to upload TXT, PNG, XML files in a server I had no privileges in!

Press enter or click to view image in full size

The story starts when I get my target from a friend, like always I start from collecting information from the target, and the first thing I did is extracting subdomains…
I used a dnsdumpster tool, you can find it here: https://dnsdumpster.com/
So the result was like this :

Press enter or click to view image in full size

A lot of domains and a lot of information that can make the mission easier, I start checking the links one by one…
suddenly I stopped In a domain called ‘Cloud.xyz.com’ with “index Of “as additional information It looked like a group of directories, so I checked the link and Bingo!

Press enter or click to view image in full size

It was an interesting find, some directories with no authentification required! one of them was interesting for me, its the first one the ‘Bugzilla’ folder, in the first second, I had no idea about what this name means so I decided to dig more, by clicking on the folder I got this!

Press enter or click to view image in full size
Get Eddie Mora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I had nooo idea what’s this about xD, but I was so excited to know, I searched on google about Bugzilla and I understood that Bugzilla is a web-based general-purpose bug tracking system and testing tool originally developed and used by the Mozilla project, and licensed under the Mozilla Public License. you can learn more about it here: https://www.bugzilla.org/
This Bugzilla had an authentification system so I needed to log in or in another way I needed a way to bypass the normal way of login!
I started searching on google till the moment I found the good bug to use!
If you add this “createaccount.cgi “ at the end of ur Bugzilla target, you will find a feature that can allow you to create another Account without the confirmation of the super admin!

Press enter or click to view image in full size

I created a new email by using a Temp Mail service and I got the link of the confirmation, then I logged in.
This is how Bugzilla looks like from the inside, and as you can see now we have the possibility to File a Bug!

Press enter or click to view image in full size

So here we can Upload a file!

Press enter or click to view image in full size

And here I was able to upload JPG file I can also upload other Extensions but unfortunately no Php supported!

Press enter or click to view image in full size

I wish I had the ability to get a reverse-shell to complete this write-up by doing some privilege escalation but you can't own everything quickly maybe after a while I will find a way to do it!

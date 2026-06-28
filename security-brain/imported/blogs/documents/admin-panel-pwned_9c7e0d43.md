---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-02_admin-panel-pwned.md
original_filename: 2021-06-02_admin-panel-pwned.md
title: Admin Panel? Pwned!
category: documents
detected_topics:
- api-security
- idor
- xss
- sqli
- command-injection
- rate-limit
tags:
- imported
- documents
- api-security
- idor
- xss
- sqli
- command-injection
- rate-limit
language: en
raw_sha256: 9c7e0d4311bfa14ad68eba4a6000a2183479d1695ed7dcd2520e5fe24b67c5ae
text_sha256: c53f4a23ed04b00c70941ebe7bb2b27afa3434443c5145571815ea83d42567ff
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Admin Panel? Pwned!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-02_admin-panel-pwned.md
- Source Type: markdown
- Detected Topics: api-security, idor, xss, sqli, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `9c7e0d4311bfa14ad68eba4a6000a2183479d1695ed7dcd2520e5fe24b67c5ae`
- Text SHA256: `c53f4a23ed04b00c70941ebe7bb2b27afa3434443c5145571815ea83d42567ff`


## Content

---
title: "Admin Panel? Pwned!"
url: "https://infosecwriteups.com/admin-panel-pwned-89db333f3836"
authors: ["Splintersec (@splint3rsec)"]
bugs: ["Information disclosure", "Hardcoded credentials"]
publication_date: "2021-06-02"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 3607
scraped_via: "browseros"
---

# Admin Panel? Pwned!

Top highlight

Admin Panel? Pwned!
The unstoppable power of recon
Splintersec
Follow
4 min read
·
Jun 3, 2021

560

6

Hello everyone, welcome to my first writeup about a funny story of how some admins store their passwords nowadays.

Before you start reading, I want to mention that this finding was closed as a duplicate, so kudos to the first researcher who reported it!

Press enter or click to view image in full size
Recon Phase

After picking a target on HackerOne (won’t disclose), I started my subdomain enumeration… For this step I don’t like to complicate things, I just follow what everyone does for gathering subdomains (which I don’t recommend, always try to be different than others to avoid dupes lol). Here’s my workflow:

Assetfinder + subfinder → httpx with title, status code and content length

So I got around 60 alive unique subdomains, great :) ! Let’s start the active enumeration…

Subdomains Analysis

Something that experienced bug hunters thaught me is to check the subdomains without doing screenshots, the title and status code plus the content length are more than enough to do the job, and it’s more efficient since you don’t get blank screenshots or redirects and probably miss something…

Scrolling down through the subdomains list, I saw one of them that got my attention

Press enter or click to view image in full size
interesting subdomain!

Hmm… dashboard.redacted.com and a 301 redirect status triggered my inner voice; “A 1 minute quick check won’t hurt you :)”. My intention was to intercept the redirection and do some magic there, but when I opened the URL, no it was not the case where you can test your magic tricks, I got an admin login page.

login panel
Pwn Phase

At first, I did what everyone of you would do, I started guessing default credentials, looking for hidden unsanitized parameters (XSS), injecting single and double quotes (SQLi)… But nothing worked :/

Get Splintersec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s okay, now the next step is what the majority of you won’t do, read the source code :) I strongly advice you to do that everytime you’re visiting an endpoint, and as my inner voice said earlier “A 1 minute quick check won’t hurt you :)” sometimes you will be surprised.

Okay, let’s check the source code

Press enter or click to view image in full size

Of course I won’t close the window and check for another subdomain before looking what’s inside that javascript file! Plus it’s name should reaaally get your attention. So I went to the file and guess what?

Press enter or click to view image in full size

Storing your credentials inside a javascript comment? Naah I don’t think they’re valid, let’s see…

Pwned :D

We successfully pwned our admin :D

Note that I can’t screenshot the whole dashboard because you may easily guess the company from it’s design…

I tried to dig more in the dashboard to check if they have an upload endpoint or something but there’s nothing, all you can do is view data and download it.

Key Takeaways
Never underestimate the power of recon, just do it properly without wasting time and you will definitely get some results.
Don’t miss reading the source code and especially javascript files, you may get credentials, API keys or even sensitive hidden endpoints… Just keep looking and open your eyes!
Always trust your gut, the subconscious mind is triggered based on previous experience and stages of your workflow as a bug hunter.
Hack properly and never give up, I didn’t after this duplicate and got a very nice bug triaged, which I will share with you once it’s disclosed.

If you enjoyed reading my 1st writeup, share it with your friends and remind them to read JS files :)

Thanks for reaching this part of the writeup ❤ and ’til the next one!

https://twitter.com/splint3rsec

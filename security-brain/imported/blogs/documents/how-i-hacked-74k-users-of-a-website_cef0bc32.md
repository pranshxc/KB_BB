---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-11_how-i-hacked-74k-users-of-a-website.md
original_filename: 2018-03-11_how-i-hacked-74k-users-of-a-website.md
title: How I hacked 74k users of a website.
category: documents
detected_topics:
- access-control
- xss
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- api-security
language: en
raw_sha256: cef0bc32262e35ab782ce1386199418db41682659b25e4654b33cdd3853ab41b
text_sha256: 1d587edbd0f035e5179c8d7cbc1f7c8c85d3077efb4a241b580a50061b7e0469
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked 74k users of a website.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-11_how-i-hacked-74k-users-of-a-website.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `cef0bc32262e35ab782ce1386199418db41682659b25e4654b33cdd3853ab41b`
- Text SHA256: `1d587edbd0f035e5179c8d7cbc1f7c8c85d3077efb4a241b580a50061b7e0469`


## Content

---
title: "How I hacked 74k users of a website."
url: "https://medium.com/@agrawalsmart7/how-i-hacked-74k-users-of-a-website-869e8a0b319"
authors: ["Utkarsh Agrawal (@agrawalsmart7)"]
bugs: ["Broken authorization"]
publication_date: "2018-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5952
scraped_via: "browseros"
---

# How I hacked 74k users of a website.

How I hacked 74k users of a website.
Utkarsh Agrawal
Follow
2 min read
·
Mar 11, 2018

115

2

Hello guys,

I follow this Quote “Sharing is Caring” so I decided to share my vulnerability which I found in a website and the vulnerability I named it is “Admin Panel Pawned”. Now Sounds Interesting. Let’s talk about How I found it?

I am not taking the name of the website but instead I use example.com and also I don’t have screenshots, but I will try my best to explain it clearly. ;)

So while I browsing the website for 1 hour I noticed that a directory is present in the website which is the “admin” directory. Now every researcher will go excited to test that directory as I was.

When I go for that directory it says “No Access” error. As I was 90% sure.

Now we all have a great tool i.e. dirbuster. If newbie are reading this, and don’t know about dirbuster ( it is a tool for bruteforce the directory. Or Directory Bruteforcer.)

So I ran it on that directory like http://example.com/admin/

So I just minimize the dirbuster window and go for check other vulnerabilities ( and yeah I found 2 XSS one is simple and other one is “filtered bypass XSS protection” :P ). So When I Come back and check the dirbuster what I see a Bunch of the directories are available.

So I was like

But When I go for check it, I got “No Access”. But I know that I have some malicious stuff in my hand so I want to dig more.

Get Utkarsh Agrawal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And then I got a file i.e. remove_access.php

So when I go for it, I got a super cool webpage which have a user input field for Username with a delete button.

Now When I type my Username into it. It remove my account successfully from it. I screamed loudly. :p

This is the screenshot after removing the account. This is only the screenshot I have.

Press enter or click to view image in full size

Now I can delete any user (from the list of 74k) in their website, Even the ADMIN itself.

So, I quickly go to report the issue, with the XSS vulnerabilities.

Then I get a quick reward, and also they changed the 50%code of their website. And they invite me for pentest their new site Comprehensively.

Now, guys this is really a amazing experiance. I always want to pwned Admin panel and I did it.

Nothing to say more. But, Thank you very much for reading this blog.

Contact:

https://twitter.com/@agrawalsmart7

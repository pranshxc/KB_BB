---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-01_leaked-git-folder-leads-to-rce.md
original_filename: 2020-11-01_leaked-git-folder-leads-to-rce.md
title: Leaked .git folder leads to RCE
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: 26406a267db5012c2e3257435b8bb4f56c04c9f7323795f3d298e9a69ec54674
text_sha256: 1c6ab62a0bc772e20cfa982ea455be0ed6da92c76c13bb3638e10df3563f14a2
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Leaked .git folder leads to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-01_leaked-git-folder-leads-to-rce.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `26406a267db5012c2e3257435b8bb4f56c04c9f7323795f3d298e9a69ec54674`
- Text SHA256: `1c6ab62a0bc772e20cfa982ea455be0ed6da92c76c13bb3638e10df3563f14a2`


## Content

---
title: "Leaked .git folder leads to RCE"
page_title: "Leaked .git folder leads to RCE – James Clee"
url: "https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/"
final_url: "https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/"
authors: ["James Clee (@jtcsec)"]
bugs: [".git folder disclosure", "RCE"]
publication_date: "2020-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4164
---

Categories 

[Uncategorized](https://james-clee.com/category/uncategorized/)

# Leaked .git folder leads to RCE

  * Post author  By [James Clee](https://james-clee.com/author/jamesclee19gmailcom/)
  * Post date  [November 1, 2020](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/)
  * [1 Comment on Leaked .git folder leads to RCE](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/#comments)

Today I wanted to share my first big success story from my bug bounty attempts. Although the issue has been fixed, the report has not been officially disclosed yet. Therefore, the target today will be everyone’s favorite “redacted.com”.

While my methodology for approaching a new target seemingly evolves every time I go through it, one constant has been a tool called [reNgine](https://github.com/yogeshojha/rengine) for initial recon. I set it up on a VPS so that way I can remotely access it from my home PC while offloading all of the scanning. It gives you a GUI to add domains as a target, run basic scans to detect subdomains, ports, run Aquatone, and (most importantly for todays writeup) run a simple dirsearch.

![](https://james-clee.com/wp-content/uploads/2020/10/rengine-1.png?w=1024)ReNgine GUI – note the accessible git artifacts

As you can see, reNgine is great for doing high level analysis of a domain. All of the results including the technology tags and directory results are searchable to help you narrow down what you’re looking for. In this case, the git folder and artifacts immediately caught my eye.

Based off of the endpoints found, it looks like this is part of a git repo or commits to a repo saved locally. I didn’t really know what I was looking at, so I started googling about reconstructing a git repo using these artifacts. I could see timestamps, hashes, commit messages and other information, but I was struggling to put it all together.

I came across an article called [Learing the internals of git by hacking websites](https://levelup.gitconnected.com/learning-the-internals-of-git-by-hacking-websites-c70c59303b12) which sounded exactly like what I was looking for. It takes you step by step through following the chain of the git structure and recovering files based off of the links and file hashes. I went through one successfully, but it took too long for my liking. So naturally, I found something someone else wrote to do it for me! Enter: [GitHack](https://github.com/lijiejie/GitHack). I cant read the whole description because its in a different language, but I do know that I run it with a URL and the black magic happens to get me source code. This is where I say to the camera “Im in” after 15 seconds of typing.

![](https://james-clee.com/wp-content/uploads/2020/10/githack_contents.png?w=1024)GitHack retrieves what appears to be full contents of WordPress site

The resulting folder that was created gave me what appeared to be the entire WordPress site. It wasn’t an exact one-to-one copy of the live version, but it was definitely close. Included were all the themes, plugins, and most importantly: configuration files. 

![](https://james-clee.com/wp-content/uploads/2020/10/wp-config.png?w=1024)Config file with database name, account, and password

Whoever committed these files was kind enough to include wp-config.php, which includes the credentials to connect to the database. I asked myself “surely, it cant be this easy… right?”. I fully expected them to be old or incorrect, but nevertheless tried to find a way to use them while not getting my hopes up. 

I had another stroke of luck that I found the site had Adminer installed. I have some experience with phpmyadmin, and Adminer functions in a similar way – its a GUI to access and modify databases on the web server. I tried the credentials and to my pleasant surprise they worked!

There seemed to be several generations of WordPress tables on the server for several different versions. I didn’t get an exact count but it was in the magnitude of tens to hundreds. Luckily, I was able to find wp_users which gave me all user accounts, hashed passwords, and emails. More importantly, I could edit all the entries in the table.

![](https://james-clee.com/wp-content/uploads/2020/10/edited_table.png?w=849)Mom get the camera!

At this point, I had a couple different options. For starters, I could mess with the users table to try and give access to myself. This could be either adding a new user to the table manually and then granting the account admin rights, or editing the password hash of the admin user. Once I have admin rights, I could proceed with exploiting one of several vulnerable plugins that required authentication or start uploading arbitrary files, whatever I wanted. Odds are, once you have admin rights there’s a way to escalate it to RCE given the outdated WordPress site. That being said, it requires editing a production database and potentially locking out the administrator account – not something I was looking to screw with.

Fortunately, as I highlighted in the top left of the above screenshot, adminer comes with a GUI to run SQL commands against the database. So boom, arbitrary SQL command execution. There are several ways to use this to access files on the local system and get true command execution. Unfortunately, I did not get a screenshot of the interface and the test commands I ran, mainly because I was frantically writing a report to let the program know the activity was my doing before they started wondering why some idiot was banging away at their system.

In my report, I outlined both paths to achieve RCE from the point I could verify on my own – adminer interface and database access. The program asked me to not make any changes to the data and promptly updated the credentials to kick me out as well. They also verified that both paths could most likely have been successful – good enough for me! 

While not the first report I’ve had triaged, its the first one that I felt like I actually did something for. Instead of just finding an exposed endpoint and reporting I could get there, I was able to take that information and escalate it. My tips for anyone out there would be enumeration and escalation. Find out everything you can about the target, and then take that information and ask yourself over and over “what can I do with this?”. I know I’m not the first person to say either of those, but if I just saw /.git returned 200 with no content and didn’t look any further, I would have missed the whole chain. Persistence is key!

Happy hunting to all you bug hunters out there!

### Share this:

  * [ Share on X (Opens in new window) X ](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/?share=facebook)
  * 

Like Loading...

### _Related_

* * *

[ ← More Information Disclosure in Wavlink Devices: CVE-2020-10973, CVE-2020-10974, and CVE-2020-12266 ](https://james-clee.com/2020/04/23/more-information-disclosure-in-wavlink-devices/)

* * *

##  One reply on “Leaked .git folder leads to RCE” 

[![howisityourlife's avatar](https://0.gravatar.com/avatar/9ae5147e977de027a4711690b9839d7a7f5d253a255d76fa2e74702a521571d7?s=120&d=identicon&r=G)howisityourlifesays:](http://howisityourlife.wordpress.com)

[November 3, 2020 at 8:48 am](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/#comment-16)

Great , Thanks for sharing

[Like](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/?like_comment=16&_wpnonce=a721f57561)Like

[Reply](https://james-clee.com/2020/11/01/leaked-git-folder-leads-to-rce/?replytocom=16#respond)

* * *

## Leave a comment [Cancel reply](/2020/11/01/leaked-git-folder-leads-to-rce/#respond)

Δ

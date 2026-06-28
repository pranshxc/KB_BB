---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-04_auditing-github-repo-wikis-for-fun-and-profit.md
original_filename: 2019-03-04_auditing-github-repo-wikis-for-fun-and-profit.md
title: Auditing GitHub Repo Wikis for Fun and Profit
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: 535a855da0d626b59c30338951742d9fcd9ad813e7b03d5ec1568dcc47d0cd94
text_sha256: c1f1548e1ea8208ddf930cfc5119d073c5ade8638970298a815c7856fe854dbc
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Auditing GitHub Repo Wikis for Fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-04_auditing-github-repo-wikis-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `535a855da0d626b59c30338951742d9fcd9ad813e7b03d5ec1568dcc47d0cd94`
- Text SHA256: `c1f1548e1ea8208ddf930cfc5119d073c5ade8638970298a815c7856fe854dbc`


## Content

---
title: "Auditing GitHub Repo Wikis for Fun and Profit"
page_title: "Auditing GitHub Repo Wikis for Fun and Profit ~ SmeegeSec"
url: "https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html"
final_url: "https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html"
authors: ["Smeege (@SmeegeSec)"]
bugs: ["Misconfigured Github wiki"]
bounty: "500"
publication_date: "2019-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5379
---

##  [Auditing GitHub Repo Wikis for Fun and Profit](https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html)

__[ 3/04/2019](https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html "permanent link") __[ SmeegeSec](https://www.blogger.com/profile/14633686433200305556 "author profile") __[No comments](https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html#comment-form) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=8845853463796109471&postID=9085372415119423028&from=pencil "Edit Post")

[Download github-wiki-auditor.py here](https://github.com/SmeegeSec/GitHub-Wiki-Auditor)

The types of issues you see when managing a bug bounty program vary widely, but every now and then a trend appears where multiple researchers submit the same issue. One day I received several reports regarding "World-editable GitHub Repository Wiki Pages" and it made me scratch my head at first. GitHub repos have wiki pages? Aren't wiki pages supposed to be collaborative and editable by nature? So I decided to look into it.

#### The Problem

All GitHub repositories have the ability to have associated wiki pages, which could potentially be world-editable (anyone with a GitHub account): 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2j3WrnuiGNRzVsYj9dJh7RivmrEZcOPETG3WJ-JxptKEMpAy-3ppwmOnuqLTiiJe-WGAT7eeb-oN9sWIV-CseLh5AgDPZ82RqtTS6RmWU3aED_AlZ5ptp_-mcTwiILj843DHpSboIIijp/s640/WikiPage-w-Border.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2j3WrnuiGNRzVsYj9dJh7RivmrEZcOPETG3WJ-JxptKEMpAy-3ppwmOnuqLTiiJe-WGAT7eeb-oN9sWIV-CseLh5AgDPZ82RqtTS6RmWU3aED_AlZ5ptp_-mcTwiILj843DHpSboIIijp/s1600/WikiPage-w-Border.png)

The issue here is that most developers and engineers at large companies don't know a setting to control this exists. This results in wiki pages which anyone with a GitHub account can modify. So is this really a security issue? Yes...if allowing anyone to edit the wiki pages was **unintentional**. So why does this occur? I've typically found one of the main causes is engineers open sourcing a project, changing the repository from private to public. The enabled wiki setting stays the same, allowing anyone, not just collaborators or internal employees, to edit the wiki page. It's also worth noting it's hard for repo owners to know when changes are made to their wiki pages because they don't get notified when it occurs and notifications can't be inherently configured.

#### The Impact

The impact of this is pretty straightforward. Any GitHub user, even without being a collaborator or having any association with the account, can create or edit wiki pages. On these pages they could include hyperlinks, images, and more using [markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf). It would be fairly easy to create a simple wiki page to social engineer people to install malicious libraries or navigate them to a malicious page owned by the attacker.

Another aspect to the impact of this issue is reputational damage. It's very easy to automate the editing of these wiki pages and would allow a nefarious actor to quickly add text and imagery which does not conform to the companies' principles.

#### The Fix

Unfortunately for large companies with a lot of public repos, there doesn't appear to be an account-level setting which can manage all repository wiki settings. This means they have to control this on a per-repo basis with the "Restrict editing to collaborators only" setting (see, [Changing access permissions for wikis](https://help.github.com/en/articles/changing-access-permissions-for-wikis)). 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMUgX25AxEk5ZfwTlkLdZDShdSnW2B4AQ1eo7hFqPtw9yIQYYMzkyX4cBamywyMQ2ecosMycLelb5cxelmRrTHN8MPp4mdRY8fxnW9FDgXtepBIphUwYNWDWqtJ-uHUZ13zdyw24G6Rot1/s640/WikiSettings-w-border.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMUgX25AxEk5ZfwTlkLdZDShdSnW2B4AQ1eo7hFqPtw9yIQYYMzkyX4cBamywyMQ2ecosMycLelb5cxelmRrTHN8MPp4mdRY8fxnW9FDgXtepBIphUwYNWDWqtJ-uHUZ13zdyw24G6Rot1/s1600/WikiSettings-w-border.png)

Other solutions could include: 

  * [Disable the wiki](https://help.github.com/en/articles/disabling-wikis) altogether, if you don't need it. 
  * Engineer education about this issue and the related wiki settings. 
  * Periodically auditing your account's repositories with my script `github-wiki-auditor.py`. 
  * Create a plugin or service which notifies you have changes to your wiki pages. 

In my opinion GitHub should allow certain plans (e.g. Enterprise customers) to control wiki pages at the account level.

#### The Script

I wrote `github-wiki-auditor.py` which iterates over a list of GitHub accounts, and for each account, iterates through each repository. For each repository it checks if the wiki page is enabled, and if so, will send a request to create a new page. If the request is successful the user is notified and the next repository is checked. This script never actually modifies the wiki pages because the ability to edit can be confirmed without doing so.

Usage: `github-wiki-auditor.py [-h] --accounts_file ACCOUNTS_FILE [--username USERNAME] [--password PASSWORD] [--output_file OUTPUT_FILE]`

Sample output: 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNcA0X6hUpn5dnS2It0twftxdlUOZedkaow1HI63PQkE_ab2t2R3qUm9MByVKgVUh6rl1bMjLdZDKboSR6caql8VXkW37jMDUFzAK_no9Sz5Ps_AKY_R8MShu5YvFwI8Csi-YfmFPCjcTr/s640/auditor-script-output2-w-border.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNcA0X6hUpn5dnS2It0twftxdlUOZedkaow1HI63PQkE_ab2t2R3qUm9MByVKgVUh6rl1bMjLdZDKboSR6caql8VXkW37jMDUFzAK_no9Sz5Ps_AKY_R8MShu5YvFwI8Csi-YfmFPCjcTr/s1600/auditor-script-output2-w-border.png)

#### The Bounty

As this is an issue I thought a lot of companies might have, I created a modified version of my script which creates a bounty report submission based on the found editable wikis. I then collected a list of about 100 unique companies from HackerOne and BugCrowd and found their GitHub accounts. This allowed me to quickly scan multiple accounts and submit bounty reports for each.

I started off by submitting about 10 separate reports. The feedback I received at first wasn't great. Most bug bounty program managers responded with either annoyance, as I wasn't the first person to submit this issue, or they responded by stating it wasn't an actual risk. I did receive a positive response from 2 companies and they had something in common: they ran their own program and weren't on a bounty platform. I believe the companies who run their own programs don't get targeted as much with common or low severity issues. So...Success!? I received my first bounty of $500 and a certificate from the other company. At this point I had proven the capabilities of the script, received my first bounty, and called it a day.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyh1IWo4mM3SzrUwf-8JvZk0N-qdMfW3ERz0FDRWUpR8jf4N5Hb6s-RtZgEgTJrXvAzacBQPxdRwv9YnlqR7wVgh6cGddn68NI9NQ74Cqz9cMy3LoZozMNPWq5OzPGGjJTJfDBAONz-L0g/s640/ACH-w-border.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyh1IWo4mM3SzrUwf-8JvZk0N-qdMfW3ERz0FDRWUpR8jf4N5Hb6s-RtZgEgTJrXvAzacBQPxdRwv9YnlqR7wVgh6cGddn68NI9NQ74Cqz9cMy3LoZozMNPWq5OzPGGjJTJfDBAONz-L0g/s1600/ACH-w-border.png)

Share This: [__Facebook](http://www.facebook.com/share.php?v=4&src=bm&u=https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html&t=Auditing GitHub Repo Wikis for Fun and Profit "Share this on Facebook")[ __Twitter](http://twitter.com/home?status=Auditing GitHub Repo Wikis for Fun and Profit -- https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html "Tweet This!")[ __Google+](https://plus.google.com/share?url=https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html "Share this on Google+")[__Stumble](http://www.stumbleupon.com/submit?url=https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html&title=Auditing GitHub Repo Wikis for Fun and Profit "Stumble upon something good? Share it on StumbleUpon")[ __Digg](http://digg.com/submit?phase=2&url=https://www.smeegesec.com/2019/03/auditing-github-repo-wikis-for-fun-and.html&title=Auditing GitHub Repo Wikis for Fun and Profit "Digg this!")

[Email This](https://www.blogger.com/share-post.g?blogID=8845853463796109471&postID=9085372415119423028&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=8845853463796109471&postID=9085372415119423028&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=8845853463796109471&postID=9085372415119423028&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=8845853463796109471&postID=9085372415119423028&target=facebook "Share to Facebook")

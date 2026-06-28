---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-21_google-books-x-hacking.md
original_filename: 2019-03-21_google-books-x-hacking.md
title: Google Books X-Hacking
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 78087fa989870df7cbe9bcdb3dadbe77ce6bb59eeea476424103e99b45b97cd7
text_sha256: ceaaef9046a1fd79f937e5228931864bc71f66b6be74b95c8765ab3b73b10b48
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Google Books X-Hacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-21_google-books-x-hacking.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `78087fa989870df7cbe9bcdb3dadbe77ce6bb59eeea476424103e99b45b97cd7`
- Text SHA256: `ceaaef9046a1fd79f937e5228931864bc71f66b6be74b95c8765ab3b73b10b48`


## Content

---
title: "Google Books X-Hacking"
url: "https://medium.com/@terjanq/google-books-x-hacking-29c249862f19"
authors: ["Terjanq (@terjanq)"]
programs: ["Google"]
bugs: ["XS-Search"]
bounty: "1,337"
publication_date: "2019-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5346
scraped_via: "browseros"
---

# Google Books X-Hacking

Google Books X-Hacking
terjanq
Follow
4 min read
·
Mar 21, 2019

112

2

Press enter or click to view image in full size

Recently, I have been participating in open Bug Bounties programs, mostly focusing on Cross-Site Search Attacks (XS-Search). This writeup is first of many to come demonstrating a successful cross-site search, here on the books.google.com website. The idea behind the attack comes from the Filemanager task that was presented during 35c3ctf and which is based on abuse of Chromium XSS Auditor. By exploiting that vulnerability the attacker could exfiltrate user’s private book collections along with the reading history.

Proof of Concept in action
Vulnerabilities

When inspecting the source code of the page, I noticed interesting differences between code sources. One of those was a specific JavaScript code added when a search query resulted in at least one book, and which wasn’t otherwise. The inserted code started with:
<script>if (window['_OC_registerHover']){_OC_registerHover({"title":"<title>", where <title> is the book title of the first displayed result.

For a given <title> and user’s <uid>, I was able to create a link https://books.google.com/books?uid=<uid>&num=1&q=<title>&x=<script>if (window['_OC_registerHover']){_OC_registerHover({"title":"<title>" that when visited, the window would be blocked by the XSS Auditor (because of the ‘reflected’ parameter xss detected), if only the first result of the search query had a title <title>, and wouldn’t otherwise.

Another, more or less important, observation is that when the page is being blocked by the XSS Auditor the window.length stays 0 (which means no iframes are embedded). Since Google inserts a lot of frames into their websites, that number usually is higher than 0, and hence, it is trivial to detect the state by reading the mentioned window.length property which is cross-site accessible.
There are other ways allowing detection of an error page which can be found in the GitHub repository that I am a collaborator of.

The main downside of the proposed attack is that the attacker must have known the user’s <uid> making the attack less wide. To make it wider, I looked closer into uid= parameter and here is what I found:

https://books.google.com/books?uid=vulnerability — infinitely redirects to itself.
https://books.google.com/books?uid=%2B — redirects to https://books.google.com/books?uid=<uid>&hl=en.
https://books.google.com/books?uid=%2B1 — throws 404 response.
https://books.google.com/books?uid=1%2B1 — redirects to https://books.google.com/books?uid=<uid>&hl=en
https://books.google.com/books?uid='&q=hack — redirects to https://www.google.com/search?tbo=p&tbm=bks&q=hack
https://books.google.com/books?uid=vulnerability&q=hack — displays results for the logged user without changing the URL (fixed)

So by combining the last vulnerability from the list with the XSS Auditor abuse, the attacker could perform a successful cross-site search on the victim’s account without knowing their <uid>.

Attack scenario

The attack could be carried out following the below scenario:

A regular user of Google Books visits a malicious website. Upon any interaction, a new window is being opened in the background, where the webpage, by manipulating the cross-origin location property, can easily exploit previously mentioned vulnerabilities and hence exfiltrate user’s sensitive data.

The exfiltrated data could consist of information such as Searched Books, Private Book Collections, Purchased Books, Read Books.

Get terjanq’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The attacker could use that information to embarrass, blackmail, threaten or even draw legal consequences from the victim because a specific set of books can be banned in some countries (https://en.wikipedia.org/wiki/List_of_books_banned_by_governments).

Attack implementation and improvements

It is possible to provide multiple ‘reflected’ parameters in one query, and hence, to perform the Binary Search algorithm for efficient information exfiltrate (which you could have noticed in the video that I included). A Proof of Concept and a more detailed description of the attack can be found in the original report that I submitted to Google: https://terjanq.github.io/Bug-Bounty/Google/books-xs-search-enpgws9jw5mb/index.html

Important update from Google

As for mine and other researchers work that intensified the Cross-Site Search attacks, Google decided to improve their services by implementing a chain of defenses against those attacks. Sadly, but a natural, consequence of that action is that they will be no longer rewarding new XS-Search reports but rather treating them as duplicates.

As a result, vulnerability reports in this area are likely to be duplicates unless they significantly change our understanding of our defenses and mitigations. We will be posting in this page the web applications and endpoints that we believe are properly protected against XS-Search, and we will be issuing Vulnerability Research Grants to audit the effectiveness of our defenses, but until then, we don’t recommend bug hunters to spend a lot of time on this (as to avoid duplication of effort). [1]

Timeline
Jan 27, 2019 11:00PM —reported
Jan 28, 2019 10:16AM — triaged
Jan 30, 2019 02:18AM — accepted
Feb 5, 2019 06:20PM — awarded $500
Mar 5, 2019 10:47PM — fixed
Mar 19, 2019 06:20PM — awarded additional $837 totalling in $1337

Thanks Google!

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

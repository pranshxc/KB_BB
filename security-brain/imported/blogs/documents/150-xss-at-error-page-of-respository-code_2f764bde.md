---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-07_150-xss-at-error-page-of-respository-code.md
original_filename: 2019-12-07_150-xss-at-error-page-of-respository-code.md
title: $150 XSS at Error Page of Respository Code
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
raw_sha256: 2f764bde2f1d950ad444d76df720e103adefe22689396d27bf89d99917fa56a5
text_sha256: 3da874a3c55cbcfc1af0a8865db88ee1a60ad9a35e90baf44e8a6dccf16049ea
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# $150 XSS at Error Page of Respository Code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-07_150-xss-at-error-page-of-respository-code.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2f764bde2f1d950ad444d76df720e103adefe22689396d27bf89d99917fa56a5`
- Text SHA256: `3da874a3c55cbcfc1af0a8865db88ee1a60ad9a35e90baf44e8a6dccf16049ea`


## Content

---
title: "$150 XSS at Error Page of Respository Code"
url: "https://medium.com/@navne3t/150-xss-at-error-page-of-respository-code-4fc628892742"
authors: ["Navneet (@na5n33t)"]
bugs: ["Reflected XSS"]
bounty: "150"
publication_date: "2019-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4905
scraped_via: "browseros"
---

# $150 XSS at Error Page of Respository Code

$150 XSS at Error Page of Respository Code
Navneet
Follow
1 min read
·
Dec 7, 2019

90

1

This article is about a security bug/issue i have found at private program on Hackerone(H1).

As the title says the bug was Reflected XSS.

The parameter which was vulnerable to XSS was not at the website of the program but in the code which was at the GitHub respository of the program.

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I searched at GitHub by the name of private program and found they have few codes written in different programming languages. Out of those i look for bug at the PHP code. So ,i look for $_GET[’someParameter’] which should take value of “someParameter” like this

localhost/ThePHPcode/thePage.php? someParameter=XSS_PayLoad

And successfully was able to find one of the parameter in the one of the code file which was a default error page as mentioned above i.e. $_GET[’someParameter’]

Now , i inserted the payload and successfully able to pop up the alert box with document.cookie.

So, i report them by explaining that if some website use their code to integrate the functionality which their code provide then that website becomes vulnerable to XSS because that website have their vulnerable code.

This report was submitted more than a year ago from today’s date. So, i got surprise of $150 after a year.

Feedback and comments are welcomed.

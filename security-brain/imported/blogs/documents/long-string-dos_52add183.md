---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-26_long-string-dos.md
original_filename: 2020-02-26_long-string-dos.md
title: Long String DoS
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 52add183926af808d7436be9af408a438acb06e9ee3696a11411aa5b7e51f49a
text_sha256: 6edeb28d2faca271e59bca430d4ef77adb541d7574cad205a34c2ceb2a563922
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Long String DoS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-26_long-string-dos.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `52add183926af808d7436be9af408a438acb06e9ee3696a11411aa5b7e51f49a`
- Text SHA256: `6edeb28d2faca271e59bca430d4ef77adb541d7574cad205a34c2ceb2a563922`


## Content

---
title: "Long String DoS"
url: "https://medium.com/@shahjerry33/long-string-dos-6ba8ceab3aa0"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["DoS"]
bounty: "100"
publication_date: "2020-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4751
scraped_via: "browseros"
---

# Long String DoS

Top highlight

Long String DoS
Jerry Shah (Jerry)
Follow
3 min read
·
Feb 26, 2020

595

2

Summary : By sending a very long string (100000 characters) it’s possible to cause a denial a service attack on the server. This may lead to the website becoming unavailable or unresponsive. Usually this problem is caused by a vulnerable string hashing implementation. When a long string is sent, the string hashing process will result in CPU and memory exhaustion.

This vulnerability was detected by sending strings with various lengths and comparing the measured response times.

I found this vulnerability on one of the private program on HackerOne. I found it while creating an account, I used the long password string for testing this vulnerability and I got 500 Internal Server Error. So it was confirmed that it is vulnerable.

Now here the minor concern is people always try to find this vulnerability on password function as I did, but you can find this at many places like :

Username
Firstname or Lastname
Email Address (create your own email using temp-mail)
Address
Text-Area
Comment Section

and many more..!!

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I would like to give an example that why username ? Say for example I’m using any social media website and I have created 2 accounts for testing purpose. Now in account A ‘s username I have entered a long string of 1000 characters and I’m searching for account A from account B then 2 things can be happen :

Either it will keeping on searching for long time
Either the application will crash (500 - Error Code)

How I found this vulnerability :

Go to https://privateprogram.com/signup
Fill the form and enter a long string in password
Press enter or click to view image in full size
Long String

3. Click on enter and you’ll get 500 Internal Server error if it is vulnerable

Press enter or click to view image in full size
Server Crash

Now many a times it happens that the signup page is not vulnerable to Long String Dos so you can try it while resetting your password.

Press enter or click to view image in full size
Resetting Password using Long String

I found it on resetting password and got successful, so I reported to the company and the gave me bounty of 100$

Press enter or click to view image in full size

NOTE : This DoS attack falls under the Application Level DoS and not Network Level DoS so you can report it. In some company’s policy of Out-Of-Scope, you’ll find “Denial of Service” which means Network Level DoS and not Application Level DoS. If the company has stated that “Any kind of DoS” is Out-Of-Scope that means you can’t report either of them.

Thank You :)

Instagram : jerry._.3

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_hunting-for-xss-with-codeql.md
original_filename: 2021-08-29_hunting-for-xss-with-codeql.md
title: Hunting for XSS with CodeQL
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6deb41f575d4f7b2a103e78ecc913bb2a35d931f1360f76388c6de6ffd6dbdcc
text_sha256: 9baa910bd27f1febd33bfc4fd29d178d490fdd12dba24f8bdb6265169ace73aa
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting for XSS with CodeQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_hunting-for-xss-with-codeql.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6deb41f575d4f7b2a103e78ecc913bb2a35d931f1360f76388c6de6ffd6dbdcc`
- Text SHA256: `9baa910bd27f1febd33bfc4fd29d178d490fdd12dba24f8bdb6265169ace73aa`


## Content

---
title: "Hunting for XSS with CodeQL"
url: "https://medium.com/codex/hunting-for-xss-with-codeql-57f70763b938"
authors: ["Daniel Santos (@bananabr)"]
programs: ["GitLab"]
bugs: ["XSS"]
bounty: "500"
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3373
scraped_via: "browseros"
---

# Hunting for XSS with CodeQL

Hunting for XSS with CodeQL
Daniel Santos
Follow
4 min read
·
Aug 29, 2021

112

1

What is CodeQL

Some months ago I was introduced to CodeQL by scrolling through my Twitter feed and I fell in love with it ever since. As the name suggests, CodeQL is a query language. However, instead of querying entity records in a database, you query a code repository for interesting patterns. For example, imagine you have the following sample NodeJS application.

Sample JavaScript application

Now, let’s say you want to know in which places of your project, a property with the name foo is read from or written to. The following codeQL query will give you the results you are looking for.

Sample query

The steps for set up your codeQL environment and start to play around are pretty simple and can be found at https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/. Once you have the environment in place, I recommend that you watch the Finding security vulnerabilities in JavaScript with CodeQL workshop. This will give you a basic understanding of the language and its features using a hands-on approach.

Built-in queries

Once you covered the basics, you will learn that CodeQL already has a lot of built-in queries that can be used to hunt for the most common types of coding bugs, XSS included. With that said, one way to start to hunt for bugs using codeQL is to simply run the existing queries against an open-source code repository you cloned.

Get Daniel Santos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For the sake of exemplification, you can take the following steps to find the DOM-based XSS vulnerability I discovered in the Discourse project using CodeQL. To replicate the finding, clone the Discourse repository, checkout commit bb2c48b0657f6182b852ab76fc190825df5d2b7f, and create a codeQL database from it.

Discourse database creation

After the database is created it is possible to use the XssThroughDom.ql query to look for potential DOM-based XSS vulnerabilities. If you set up your Visual Code+CodeQL integration you should get results that look like the following.

Press enter or click to view image in full size
XssThroughDom.ql results

The results will be comprised of paths. Each path connects a source to a sink. In other words, some input to a potentially sensitive function parameter or property assignment value. I won’t get into the details about the vulnerability itself as this is out of the scope of this article. I just used this as an example to prove one can find real-world vulnerabilities in a widely used open-source project by simply using codeQL’s built-in queries.

LGTM

According to GitHub, LGTM is:

A code analysis platform for finding zero-days and preventing critical vulnerabilities

LGTM allows you not only to query a lot of the projects hosted on GitHub, but it also constantly assesses them using CodeQL’s official queries. The results are available to whoever wants to see them. In fact, the vulnerability I found on the Discourse project was available in LGTM as well to whoever had the interest to analyze the alerts.

A good starting point for those interested in the platform and what it has to offer is analyzing the results for the intentionally vulnerable web application Juice-Shop.

Press enter or click to view image in full size
LGTM results
Going further

After finding the Discourse vulnerability I got really excited about CodeQL’s potential and started playing around building my own vulnerable code and testing built-in queries against it. After playing with it for a while I built some DOM-based XSS test cases using the clipboard API as the malicious source. For those who are not familiar with the clipboard API and its security implications, I suggest reading The curious case of copy and paste an article from Mr. Michał Bentkowski (@SecurityMB). To my surprise, none of the built-in queries were able to detect even the most simple clipboard-based XSS. I decided then to build my own query to look for this kind of bug. Finally, after some nights of poor sleep I got my head around CodeQL’s Javascript types and type tracking predicates and voilà, the ClipboardXss.ql query was born.

ClipboardXss.ql

Once it was done, I started querying all of my favorite open-source projects that were available in LGTM with it. I was able to find bugs in GitLab and in one of Github’s dependencies. Both with patches available at this point.
Once I got real results from my query I decided to take a shot at contributing to the CodeQL project itself. At the time of this writing, my query is still under review but I am confident it will be accepted and that eventually the clipboard API source will be merged into the standard XSS queries.

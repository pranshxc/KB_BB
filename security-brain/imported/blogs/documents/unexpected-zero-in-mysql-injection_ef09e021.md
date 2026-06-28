---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-11_unexpected-zero-in-mysql-injection.md
original_filename: 2023-07-11_unexpected-zero-in-mysql-injection.md
title: Unexpected Zero in MySQL Injection
category: documents
detected_topics:
- idor
- sqli
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- sqli
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: ef09e02139d08c6286756aad3aa80a76d2582a462ea4870e5d39e5f961a4b269
text_sha256: d9233e2f30704a1d9aaf64ab4f98637b2aaafc4d15f298ad7ad90ee49fb1dfd5
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Unexpected Zero in MySQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-11_unexpected-zero-in-mysql-injection.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `ef09e02139d08c6286756aad3aa80a76d2582a462ea4870e5d39e5f961a4b269`
- Text SHA256: `d9233e2f30704a1d9aaf64ab4f98637b2aaafc4d15f298ad7ad90ee49fb1dfd5`


## Content

---
title: "Unexpected Zero in MySQL Injection"
url: "https://dimazarno.medium.com/unexpected-zero-in-mysql-injection-511f632714b0"
authors: ["Dimaz Arno (@dimazarno)"]
bugs: ["SQL injection"]
publication_date: "2023-07-11"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 947
scraped_via: "browseros"
---

# Unexpected Zero in MySQL Injection

Unexpected Zero in MySQL Injection
Dimaz Arno
Follow
3 min read
·
Jul 10, 2023

25

1

Press enter or click to view image in full size

When conducting a pentest on a client (sorry, I cannot provide real screenshots here), I discovered a SQL injection vulnerability, but there were some limitations that seemed to be implemented as coding filters.

The discovered form looked like this (I have simplified it for easier reading and understanding):

https://example.com/employee/search/?name={keyword_here}

The SQL injection payloads I could obtain were:

‘+version()+’
‘+database()+’

I concluded that this was a SQL injection vulnerability in MySQL. However, there are a few observations I made:

Boolean-based exploitation cannot be performed because the output always remains the same.
If I provide a function outside of MySQL, such as hello(), it will result in a 500 error.
Attempts to perform enumeration, such as using the substring function, do not provide different output, making enumeration impossible.
The sleep function has been filtered, so I cannot use it.
I am unable to use injection comments either — or #.

Then an idea emerged: What if I input 0 into a certain field? But before that, I tried it out using an online MySQL interface . Please note that the following query returned 91 records.

Press enter or click to view image in full size

Then I tried modifying the query in the CustomerName field as follows:

Press enter or click to view image in full size

And the result still displayed all records!

Get Dimaz Arno’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried confirming this on my local MySQL (with a different database and table):

The result was the same! It returned all the data!

Next, I tried it on PostgreSQL:

Press enter or click to view image in full size

Interestingly, PostgreSQL gave an error. Does this mean that MySQL doesn’t enforce an error when there’s a data type mismatch? Interesting!

Returning to my pentest, if I want to retrieve all the data using SQL injection using this method, it means I need to provide an integer input. However, it’s important to note that the original query expects a string.

Eventually, I came up with an idea like this:

Press enter or click to view image in full size

The injection would be: ‘x’+0+’x’, which would be interpreted as 0 by MySQL, causing a data type difference!

So I can pull all the data without using injection comments, like this:

https://example.com/employee/search/?name=x'+0+'x

Thank you for reading!

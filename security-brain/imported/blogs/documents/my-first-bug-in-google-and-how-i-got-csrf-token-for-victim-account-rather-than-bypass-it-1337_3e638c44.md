---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-07_my-first-bug-in-google-and-how-i-got-csrf-token-for-victim-account-rather-than-b.md
original_filename: 2020-09-07_my-first-bug-in-google-and-how-i-got-csrf-token-for-victim-account-rather-than-b.md
title: My first bug in google and how i got CSRF token for victim account rather than
  bypass it ($1337)!
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: 3e638c44ec657c158b1cd2e343b70bdb9f37ee16b131b82496f9d08cb01870d7
text_sha256: 4180129ced7eb6e45ea239711e361f4e49ab3ca4146ad150473e0340a1836807
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# My first bug in google and how i got CSRF token for victim account rather than bypass it ($1337)!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-07_my-first-bug-in-google-and-how-i-got-csrf-token-for-victim-account-rather-than-b.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `3e638c44ec657c158b1cd2e343b70bdb9f37ee16b131b82496f9d08cb01870d7`
- Text SHA256: `4180129ced7eb6e45ea239711e361f4e49ab3ca4146ad150473e0340a1836807`


## Content

---
title: "My first bug in google and how i got CSRF token for victim account rather than bypass it ($1337)!"
url: "https://medium.com/@odayalhalbe1/my-first-bug-in-google-and-how-i-got-csrf-token-for-victim-account-rather-than-bypass-it-1337-bf01261feb47"
authors: ["Oday Alhalbe"]
programs: ["Google"]
bugs: ["CSRF"]
bounty: "1,337"
publication_date: "2020-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4275
scraped_via: "browseros"
---

# My first bug in google and how i got CSRF token for victim account rather than bypass it ($1337)!

My first bug in google and how i got CSRF token for victim account rather than bypass it ($1337)!
Oday Alhalabi
Follow
2 min read
·
Sep 7, 2020

182

2

Greetings,

Today i will share my first bug in google, Which is in “Books”. I was able to modify/delete bookshelf for victim account by get CSRF token rather than bypass it .

Let’s start ..

When sign in to your account on books.google.com,you will note that there is option to create bookshelf .

Firstly,i created bookshelf and then I captured request when delete it :

Press enter or click to view image in full size

As you can see the sig sent as parameter .I tried different ways to bypass sig ,but unfortunately i couldn’t bypass it :( .

After deep search i found way to get CSRF_TOKEN for victim account rather than bypass :)

Steps :

Get Oday Alhalabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1-Go to victim bookshelf and then you will find as below :

Press enter or click to view image in full size

2-Press on Test :

Press enter or click to view image in full size

3-When modify name or description and press save no thing happen ,because i am not authenticated user .

But let’s start check request :

Press enter or click to view image in full size

The surprise was that there is sig parameter :))))

4- I created PoC with this sig parameter and then i send it to victim.

You need to create a PoC for each targeted victim :D

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-23_new-100-bug-in-my-methodology.md
original_filename: 2024-06-23_new-100-bug-in-my-methodology.md
title: New 100$ Bug in My Methodology!
category: documents
detected_topics:
- xss
- command-injection
- password-reset
tags:
- imported
- documents
- xss
- command-injection
- password-reset
language: en
raw_sha256: 013d85da01fefc55dfb242454ede96b6e8b0da51328333ca4e32efd542bda75c
text_sha256: 3baf3b423830dde938ad8af1a2541090530ff7883cd6ef9f5198b0285539d2e3
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# New 100$ Bug in My Methodology!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-23_new-100-bug-in-my-methodology.md
- Source Type: markdown
- Detected Topics: xss, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `013d85da01fefc55dfb242454ede96b6e8b0da51328333ca4e32efd542bda75c`
- Text SHA256: `3baf3b423830dde938ad8af1a2541090530ff7883cd6ef9f5198b0285539d2e3`


## Content

---
title: "New 100$ Bug in My Methodology!"
url: "https://medium.com/@rewmcode/new-100-bug-in-my-methodology-60d99f0dafe2"
authors: ["Ali Rem (@khodeRewm)"]
bugs: ["Application-level DoS"]
bounty: "100"
publication_date: "2024-06-23"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 231
scraped_via: "browseros"
---

# New 100$ Bug in My Methodology!

New 100$ Bug in My Methodology!
Ali Mojaver
3 min read
·
Jun 23, 2024

--

12

Hello everyone! I’m Rem and I’m 23 years old. I’m here to describe my new bug. This bug is very amazing to me and I think some people might not care about this bug.

New Bug Type for me!

One day, I decided to start hunting on a new program. I’m new in bug hunting (over 1 year), and in the past, I was scared of public programs because I said, ‘Hey Rem, this program is public and many hackers are working on it.’ But this time was different. I believed in myself and said, ‘Just enjoy the program and test it! It isn’t important if you don’t find anything.’

Press enter or click to view image in full size

My friend, please just search for knowledge! One problem with new bug hunters like me is that they just search for money in programs. This mindset can destroy you. You must play with different sections of the application and enjoy it! Think like a real hacker; think about hacking, not just finding and reporting bugs!

What’s a Bug?

I started by playing with the application, testing everything, and trying to find abnormal application behavior. While I was testing different sections of the app, I opened a special section: Invite Member! The invite member system is a normal section in every program, but something was unusual about this invite member system, and it was the first name section!

Hmm, this means I can set the name for other users. At first, I thought this user name was only for the invite section, but after testing, I saw that after inviting the user, this first name and last name were set in site for him/her.

I know it’s incredible, but anyone can set a first name and last name for you if you don’t register in the system, and this happened in a famous public app! It wasn’t a bug, but this behavior was uncommon, and I think to find a bug through this creativity :)

I invited some users via email, but I entered special characters in the first name and last name fields.

Guess what 😂! Because the user’s first name and last name were abnormal, they could no longer register with that email! So, I could effectively disable any email in the system by injecting special characters into their first name.

Imagine you don’t register on this site. In the invite section, I write your email, but in the first name section, I put a special character. After that, an invite email is sent to your email. If you try to register on the site or use the forgot password feature, you can’t! And I blocked you from using this site :)

SO:

1- Every time inject payload into the first name or last name fields (XSS, CSTI, etc.).

2- Finding abnormal application behavior

3- Hacking for the sake of hacking, not for money

My X.com

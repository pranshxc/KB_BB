---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-12_brute-forcing-user-ids-via-csrf-to-delete-all-users-with-csrf-attack.md
original_filename: 2019-03-12_brute-forcing-user-ids-via-csrf-to-delete-all-users-with-csrf-attack.md
title: Brute Forcing User IDS via CSRF To Delete all Users with CSRF attack.
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: 6369cd1d19858f950376a702d290a3db98d062ace59ac1add01698bb53ac4696
text_sha256: a45bee9eef1c86abf4b147d2c84ed4da93662c503f5c78ecbfe220a170a656e9
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Brute Forcing User IDS via CSRF To Delete all Users with CSRF attack.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-12_brute-forcing-user-ids-via-csrf-to-delete-all-users-with-csrf-attack.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6369cd1d19858f950376a702d290a3db98d062ace59ac1add01698bb53ac4696`
- Text SHA256: `a45bee9eef1c86abf4b147d2c84ed4da93662c503f5c78ecbfe220a170a656e9`


## Content

---
title: "Brute Forcing User IDS via CSRF To Delete all Users with CSRF attack."
url: "https://medium.com/@armaanpathan/brute-forcing-user-ids-via-csrf-to-delete-all-users-with-csrf-attack-216ccd4d832c"
authors: ["Armaan Pathan (@armaancrockroax)"]
bugs: ["CSRF", "Bruteforce"]
publication_date: "2019-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5366
scraped_via: "browseros"
---

# Brute Forcing User IDS via CSRF To Delete all Users with CSRF attack.

Brute Forcing User IDS via CSRF To Delete all Users with CSRF attack.
Armaan Pathan
Follow
2 min read
·
Mar 12, 2019

311

1

While testing an application, there was a module “Delete User” in which an admin can delete any user.

Press enter or click to view image in full size

If you notice in the request, there is no CSRF Token/Protection implemented into delete user request.

This was very easy CSRF that an attacker can send the form to admin and can delete the user from an application.

Simple CSRF PoC to Delete User

Press enter or click to view image in full size

But again if you notice that request contains the user id. My challenge was to figure out that if an application user ids at any endpoints but I found that there was no user ID leakage.

As it was 5 digits numeric ID, It was easy to brute force,

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

From the research I got the blog post in which an attacker has brute-forced the IDs with the help of clickjacking.

Client-side CSRF Token Brute Forcing
While playing around with some CSRF examples the idea of client-side CSRF token brute-forcing came into my head. I'd…

pwndizzle.blogspot.in

Now Challenge is that an application was using X-Frame Options Header so I was not able to load an application into the frame to brute force the IDS.
I tried with XMLHttpRequest, But again an application was validating the ORIGIN so, in this case, XHR dint work for me.

Then I tried by throwing requests into iframe target.

In this case, I was not able to view the response as the response had X-Frame-Option Header which application was validating. But I was able to send the request

So I made a CSRF Script which brute forces the USER IDS and deletes all the existing Users with CSRF from an application

Press enter or click to view image in full size

And When I sent this PoC to the victim (admin), I was able to delete all Existing users from an application.

Press enter or click to view image in full size

Thanks, guys for reading.
Have a great day ahead.

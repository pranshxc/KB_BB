---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-02_privilege-escalation-stealing-users-point-bugcrowd.md
original_filename: 2021-08-02_privilege-escalation-stealing-users-point-bugcrowd.md
title: Privilege Escalation | stealing user’s point | Bugcrowd
category: documents
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- otp
- rate-limit
tags:
- imported
- documents
- idor
- access-control
- command-injection
- password-reset
- otp
- rate-limit
language: en
raw_sha256: 96f8c257d59fc9816ec9e68a3a8bcdec6448a8907a9f4963bf48601a9b0e0ac7
text_sha256: 87f96f2f7eea662f5730482c547e2c4ea3fbb645222e0ef5cb48117782931b88
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation | stealing user’s point | Bugcrowd

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-02_privilege-escalation-stealing-users-point-bugcrowd.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, otp, rate-limit
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `96f8c257d59fc9816ec9e68a3a8bcdec6448a8907a9f4963bf48601a9b0e0ac7`
- Text SHA256: `87f96f2f7eea662f5730482c547e2c4ea3fbb645222e0ef5cb48117782931b88`


## Content

---
title: "Privilege Escalation | stealing user’s point | Bugcrowd"
url: "https://medium.com/@abhinda1996/privilege-escalation-private-program-bugcrowd-831a7eb58b6c"
authors: ["Abhind Abhi"]
bugs: ["IDOR", "Privilege escalation"]
publication_date: "2021-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3450
scraped_via: "browseros"
---

# Privilege Escalation | stealing user’s point | Bugcrowd

Abhind
Follow
3 min read
·
Aug 1, 2021

30

3

Privilege Escalation | stealing user’s point | Bugcrowd

Hi guys! This blog is about how I found privilege escalation on a web application.

Application Background

It is an E-commerce website that allows users to buy stuff, earn points and convert them to coupon codes that can be used for future purchases. The scope consists of 2 URLs:

The user management page: where a user can edit details, set preferences and convert points into coupon codes.
Shopping page: Where a user can buy the listed items and use the coupon code generated earlier.
Press enter or click to view image in full size
Photo by Brooke Lark on Unsplash

My Methodology

I start by exploring the application URL that are in-scope and how they are linked to each other in terms of the following:

Sharing data
Functionality
User privileges

Hacking begins!

Get Abhind’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After exploring the application for a while, I found an API endpoint that was implemented differently from all the other APIs in the application. The APIs followed the basic cookie-based authentication for session management but this vulnerable API functioned differently because it did not required any authentication cookies.

Press enter or click to view image in full size

It uses the Email ID and an external reference ID for performing an action, which is used to convert the user’s points to coupon code. The coupon can be used on the shopping page for availing discounts.

Now to create a valid attack scenario, I need an Email ID and the corresponding external reference ID. So I created a different account to check for the external ID’s entropy. It was a random alphanumeric string after the first 6 digits so I had to brute-force the T-6 digits( where T is the total length of the string from the start). The endpoint was missing a rate-limit check so that gave me hope.

Now to perform the attack I brute-forced a list of Email IDs and randomly generated external IDs using intruder and it worked. The other way of getting the external ID is via the forgot password link( if any user has used the forgot password URL for resetting the password, the external ID is appended in the token for that URL and it is saved in the browser history). By this method, I can use the points of any user in the application and buy products.

Press enter or click to view image in full size

This issue was triaged P3.

About me: Abhind

Press enter or click to view image in full size
Photo by Courtney Hedger on Unsplash

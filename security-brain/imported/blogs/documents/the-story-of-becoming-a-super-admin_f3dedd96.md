---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-08_the-story-of-becoming-a-super-admin.md
original_filename: 2023-03-08_the-story-of-becoming-a-super-admin.md
title: The story of becoming a Super Admin
category: documents
detected_topics:
- otp
- api-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- otp
- api-security
- command-injection
- information-disclosure
language: en
raw_sha256: f3dedd969ebfcbf81e567c43efb91b294c925b2293e854c19702984fc3e3f274
text_sha256: 7cc7be8b16dff2b6771f0f114ccfbe7a5e4e4d34de3c93796056d7de2cec7d6d
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# The story of becoming a Super Admin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-08_the-story-of-becoming-a-super-admin.md
- Source Type: markdown
- Detected Topics: otp, api-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `f3dedd969ebfcbf81e567c43efb91b294c925b2293e854c19702984fc3e3f274`
- Text SHA256: `7cc7be8b16dff2b6771f0f114ccfbe7a5e4e4d34de3c93796056d7de2cec7d6d`


## Content

---
title: "The story of becoming a Super Admin"
page_title: "The Story of Becoming a Super Admin | by Ömer Kepenek | Medium"
url: "https://medium.com/@omerkepenek/the-story-of-becoming-a-super-admin-ab32db7dd1b3"
authors: ["Ömer Kepenek (@omer_kepenek)"]
bugs: ["Hardcoded credentials", "Account takeover", "Information disclosure"]
publication_date: "2023-03-08"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1409
scraped_via: "browseros"
---

# The story of becoming a Super Admin

The Story of Becoming a Super Admin
Ömer Kepenek
Follow
5 min read
·
Mar 8, 2023

200

6

Press enter or click to view image in full size

Hey everyone! I hope y’all are doing well.

Before I move on to the P1 vulnerability I found, let me tell you a little about myself. I’m Ömer and I’ve been working as a Penetration Tester at Privia Security for over 3 years. Application security is a field that I am particularly interested in and enjoy working in. Apart from my work, I do bug bounty to spend time in my spare time. In this blog post, I will be sharing with you a critical vulnerability I found while doing bug bounty on Intigriti.

So let’s get right into it, shall we?

I started with the recon phase, which is the most important phase in the process of finding vulnerabilities. I said it’s the most important step because the more attack surfaces you can extract the more likely you are to find vulnerabilities.

I always create target based word lists besides commonly used ones. Also there is a another powerful tool named fuzzuli, it’s a url fuzzing tool that aims to find critical files by creating a dynamic word list based on the domain. It provides a word list by extracting all combinations of the domain name and allows fuzzing with specific matchers. With the wordlists I have created and using fuzzuli, I started to FUZZ all the domains included in the scope of the target program. In one of the domain, I found a “.dll” file which contains all the source code of an application.

The Common Intermediate Language (CIL) code in the .NET framework is the “.dll” and “.exe” files that you get once source code is compiled. That means when the web application is compiled, this “.dll” file contains all the source code.

Press enter or click to view image in full size
Dll File Found

I have hidden the name of the “.dll” file as it is related to the domain.

I immediately downloaded the “.dll” file I found and started to examine it. There are several decompilers you can use to examine “.dll” files, some of them are dotPeek, ILSpy and dnSpy. I personally prefer dnSpy and in this blog I will continue over dnSpy.

I opened the file with dnSpy decompiler and took a look at the namespaces and class names. After doing this, I realized that this web application I encountered is an API service.

Press enter or click to view image in full size
WebApiConfig Class

When I examined the whole code in detail, I came across something that caught my attention. One of them was that there are user account types with different privileges in this service.

Press enter or click to view image in full size
Account Types

As you can see in the screenshot above, there are 3 different types of user accounts. I learned that the most authoritative user account type on the service is Super Admin. Let’s keep this in mind, who knows, maybe it will help us 😉.

Get Ömer Kepenek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I dug deeper into the code, something else caught my attention, which was the hard-coded credentials.

Press enter or click to view image in full size
Super Admin Credentials

As soon as I saw this, I was just hoping those credentials were still valid. Because as you can see in the screenshot above, the credentials I found have Super Admin privileges. Immediately I started looking for places where I could use these credentials and I found an API endpoint where I can get a session using the credentials in the code. I tried to get a session right away from there.

Press enter or click to view image in full size
Got Token
Press enter or click to view image in full size
User Info

Yay! The credentials were still valid and I was able to log in to the Super Admin account. Then I decided to examine what I could do with the privileges of this account. I saw that critical operations can be performed in the application by using the token with “SuperAdmin” privileges. For example, all users can be listed, another user’s password can be changed, any user can be deleted or a new user can be added. Of course I chose to create my own backdoor user for the PoC (Proof of Concept).

Let’s become the top man!!!

Press enter or click to view image in full size
Account Created with Super Admin Privileges
Press enter or click to view image in full size
Got New Token with New User
Press enter or click to view image in full size
All Users Listed

By opening my own user, I have become one of the most authorized users of this service and we have come to the end of our story. After performing the above steps, I wrote a detailed report containing all the steps I took and reported it to the program.

Timeline:

09.02.2023 -> First Reported
13.02.2023 -> Changed the severity from High (7.5) to Critical (9.1)
13.02.2023 -> Triaged by Intigriti
22.02.2023 -> Accepted by the Company
22.02.2023 -> Marked as Resolved and Added to Hall of Fame.

I would like to thank Talha Aydın for his contributions.

Thank you for reading my story. See you on another adventure. 🧙‍♂️

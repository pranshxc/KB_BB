---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-14_pii-data-leakage-and-us1500-bounty.md
original_filename: 2023-06-14_pii-data-leakage-and-us1500-bounty.md
title: PII Data Leakage and US$1500 Bounty
category: documents
detected_topics:
- idor
- sqli
- sso
- access-control
- xss
- command-injection
tags:
- imported
- documents
- idor
- sqli
- sso
- access-control
- xss
- command-injection
language: en
raw_sha256: 1f04b4c867f9fa985703f0debe8f31331005743dcc5a8e1d76d46d89d38434d2
text_sha256: a29642344db92f6dfd9e29eba6a73371c4c00f5e760f54dd39e98fc8353a70ba
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# PII Data Leakage and US$1500 Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-14_pii-data-leakage-and-us1500-bounty.md
- Source Type: markdown
- Detected Topics: idor, sqli, sso, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `1f04b4c867f9fa985703f0debe8f31331005743dcc5a8e1d76d46d89d38434d2`
- Text SHA256: `a29642344db92f6dfd9e29eba6a73371c4c00f5e760f54dd39e98fc8353a70ba`


## Content

---
title: "PII Data Leakage and US$1500 Bounty"
url: "https://medium.com/@ferferof/pii-data-leakage-and-us-1500-bounty-af676350fb76"
authors: ["ferferof (@ferferof_)"]
bugs: ["Information disclosure", "IDOR"]
bounty: "1,500"
publication_date: "2023-06-14"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1045
scraped_via: "browseros"
---

# PII Data Leakage and US$1500 Bounty

Top highlight

PII Data Leakage and US$1500 Bounty
ferferof
Follow
6 min read
·
Jun 15, 2023

206

3

Greetings, ladies, and gentlemen. Today, I would like to present to you an exposition on the vulnerability of information disclosure on a private program.

To begin with, please allow me to introduce myself. I am a recent entrant into the field of security, having previously served as a back-end developer. However, due to the dynamic nature of security and the need for constant updating, I find this field to be particularly alluring.

Without further ado, let us now delve into the crux of the matter and examine the intricacies of this vulnerability in greater detail.

As part of my job, I had the opportunity to work with private programs, which I found to be particularly rewarding. Unlike public programs, private programs often have fewer hackers working on them, which made my job more manageable and gave me the necessary motivation to succeed.

One day, I stumbled upon a Google dork that caught my attention. The dork in question was as follows:

inurl:responsible disclosure

Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Wikipedia

Using this dork, Google provided me with a list of private programs. After carefully reviewing the list, I decided to focus on one program in particular that had a unique and intriguing startup concept.

To begin my security assessment, I started by using Subfinder to identify any subdomains associated with the target domain. From there, I used a variety of other tools, including GitHub Scan and Certificate Scan, to gather as much information as possible about the target’s web environment. Finally, I used my own wordlist to brute force the target, both statically and dynamically, which allowed me to discover a total of 42 subdomains.

Once I had a better understanding of the target’s web environment, I proceeded to explore the main domain of the site. While navigating the site, I discovered a registration button that led to a user panel where users could create an account and enter their personal information, including their name, email, phone number, and profile details.

First Scenario, Let’s hack everything

The first scenario I attempted was to try XSS payloads on fields that didn’t have validation, such as the name field. I tried several attempts, but unfortunately, this scenario failed to yield any results.

Here is my payload which I tried to pop an alert.

Press enter or click to view image in full size
Second Scenario, Annihilation is always the answer

Next, I attempted to upload a shell instead of the profile image. To do this, I created a PHP file and wrote echo 1 inside it. I then attempted to upload the file with content-type: image/png. I noticed an interesting thing — the file was uploaded successfully. I quickly located the path of the photo and used curl in the terminal to check if the code inside my file was executed. Unfortunately, I discovered that the code was not executed, which left me feeling disappointed.

I attempted various tactics to upload my file by changing the content type, but the only content type supported was “image”. I even tried changing the file extension to “phar” or “php5”, but these attempts also failed.

Third Scenario, Control is an illusion

The startup architecture allowed users to define one or more companies for their accounts and enter their information, enabling them to operate them through the startup idea. Each user was assigned an ID, which was denoted as u_wdobhREkbf. Similarly, each company also had an ID, which was c_z8zI6a4unp. The only difference between the IDs was that the user ID started with “u”, while the company ID started with “c”. This distinction made sense in the context of the startup’s architecture.

The third scenario I attempted was IDOR (Insecure Direct Object Reference). During my time working at the company, I had not paid attention to the relationship between objects in the database, and I had forgotten to include validation that checked whether the reference being retrieved from an object was related to the user or not. To test for vulnerabilities, I created another account and filled in company information to obtain the company ID.

Get ferferof’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next, while logged in as my previous user, I edited my profile and replaced the company ID with the ID of the company I had created earlier. To my surprise, I received a response API that contained a SQL query error. I noticed that a similar API was triggered when attempting to create another account with a duplicate email.

Press enter or click to view image in full size

Although the third scenario I attempted ultimately failed, it provided me with a great deal of motivation. I was struck by the fact that the API was returning a SQL query error, which should not be happening under normal circumstances.

I was initially interested in trying a SQL injection method, but I quickly discovered that the startup had implemented prepared statements for all of its fields, making it immune to SQL injection attacks.

Last Scenario, A light in the darkness

With two users on the site, I decided to test the site’s access control by using an endpoint that returns a user’s information to see if one user could access another user’s information. I obtained the ID of the other user and entered it, eager to see what would happen.

What I found was surprising.

Press enter or click to view image in full size
Press enter or click to view image in full size

Upon accessing the user information endpoint /main/api/v1/users/<userId>, I was shocked to discover that sensitive information such as the user’s photo, phone number, signature picture, address, and more, was being disclosed. However, this discovery was overshadowed by an important bug.

Each user ID had a prefix, denoted by the letter “u”, followed by a randomly generated string of 10 characters. I realized that the number of all possible combinations of these characters was staggering — with 26 lowercase letters, 26 uppercase letters, and 10 numbers, each position had 62 possible choices. This meant that the total number of possible states was a staggering 839,299,365,868,340,224 — a number too large even for supercomputers to handle.

Despite the sensitive information that was being disclosed through this endpoint, the sheer scale of possible user IDs made it difficult for anyone to exploit this vulnerability.

So there was no disclosure until I reached this endpoint. /main/companies/search/findByNameIgnoreCaseContaining?q=<searchParam>&limit=20

Press enter or click to view image in full size

One of the site’s features allowed users to search for companies based on their names. Upon searching, a list of up to 20 companies containing the search term would be returned. However, upon closer inspection, I noticed that the user ID of the person who created each company was also included in the search results. This presented a significant security risk that I decided to investigate further.

To exploit this vulnerability, I developed an algorithm that involved creating a list of all possible one-letter, two-letter, and three-letter combinations of English words. I used the API to search for each combination and retrieve the corresponding company names and user IDs. Next, I called the API that provides user data, passing in the user ID obtained in the previous step. I then saved the data in a JSON file.

Press enter or click to view image in full size

Due to the high number of API calls required for this exploit, I implemented the algorithm using Python and utilized multi-threading to speed up the execution time. After just 10 minutes, I exposed over +40k pieces of sensitive data. I immediately reported this issue to the company, who recognized my efforts with a bounty of $1,500.

This experience underscored the importance of thorough testing and the potential risks associated with seemingly innocuous features. By identifying and addressing vulnerabilities like this, we can help to ensure a safer and more secure online experience for everyone.

I hope you found this informative and engaging.

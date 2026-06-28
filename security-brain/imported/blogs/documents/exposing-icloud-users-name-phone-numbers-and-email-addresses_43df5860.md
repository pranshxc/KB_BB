---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-20_exposing-icloud-users-name-phone-numbers-and-email-addresses.md
original_filename: 2023-05-20_exposing-icloud-users-name-phone-numbers-and-email-addresses.md
title: Exposing iCloud user’s Name, phone numbers, and email addresses.
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- information-disclosure
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- information-disclosure
- cloud-security
language: en
raw_sha256: 43df586084de9d62b13fbc64654818d6e806f237a84ba524a1af98ca6d028925
text_sha256: 510cd653536c24e1008b6441e07578f4b39347aa42d0b3d88fa4832b52339734
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Exposing iCloud user’s Name, phone numbers, and email addresses.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-20_exposing-icloud-users-name-phone-numbers-and-email-addresses.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `43df586084de9d62b13fbc64654818d6e806f237a84ba524a1af98ca6d028925`
- Text SHA256: `510cd653536c24e1008b6441e07578f4b39347aa42d0b3d88fa4832b52339734`


## Content

---
title: "Exposing iCloud user’s Name, phone numbers, and email addresses."
url: "https://infosecwriteups.com/exposing-icloud-users-name-phone-numbers-and-email-addresses-d1f4a3786092"
authors: ["Renganathan (@IamRenganathan)"]
programs: ["Apple (iCloud)"]
bugs: ["Information disclosure"]
publication_date: "2023-05-20"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1134
scraped_via: "browseros"
---

# Exposing iCloud user’s Name, phone numbers, and email addresses.

Exposing iCloud user’s Name, phone numbers, and email addresses.
Renganathan
Follow
3 min read
·
May 19, 2023

339

1

Hi There,

Renganathan Here, I’m an Ethical Hacker & a Security researcher.

This writeup is shared publicly with the permission of the Apple Product Security Team.

This write-up is about a misconfiguration that I found on iCloud and how I could have accessed the iCloud user’s name, phone number, and email address.

I’ve submitted only one report to Apple till now but It was not a valid one.

After seeing one of my mentors, 
Hemant Patidar
 was awarded $$$$ for finding a vulnerability on apple id, I thought should give it a try to apple again :)

I started with iCloud this time instead of starting with apple.com and subdomain enumerations and other stuff.

Press enter or click to view image in full size
iCloud dashboard

I’m not an Apple user, I didn’t know the features and functions so was manually exploring them. Then I clicked upon notes and saw something like the one below.

Press enter or click to view image in full size
given attention to the URL

So there’s a link for the iCloud notes which I can share with people.

The link looked something like the one below:

https://www.icloud.com/notes/neVeRgoNNagiVEyouuP

so just like another bug hunter, I was curious to access others’ notes.

I used the below Google Dorks to enumerate all the notes.

site:icloud.com/notes/*

The notes link were crawled only because they were shared publicly, else Google can’t crawl them.

Press enter or click to view image in full size
Links Enumerated

But that doesn’t stop there I need to gain access to others’ notes.

Get Renganathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

but a few of them gave me this 404 error.

Press enter or click to view image in full size
404 error

But they returned with a verification requirement

Press enter or click to view image in full size
verification requirement

I clicked on verify,

BOOM! (The most expected word LOL)

Press enter or click to view image in full size
email id exposed

That just showed me who’s the owner of the notes by exposing the email id.

Again a few of them showed me the owner’s phone number

Press enter or click to view image in full size
phone number exposed

By opening the link in the private window it showed me the name of the owner

Press enter or click to view image in full size
Owner name exposed

I tried to get a copy of the verification link by modifying the API request but it was not vulnerable. So I reported this as the owner’s details were exposed, my bug was accepted, and I was credited to the apple hall of Fame.

TimeLine:

June 2, 2021 - Reported

June 16, 2021 - Accepted & patch was implemented against crawling the links.

- Completely fixed.

February, 2022 - got listed in their hall of fame.

Press enter or click to view image in full size
Patched

Thanks for reading :)
Stay Safe.

https://www.instagram.com/renganathanofficial/

https://twitter.com/IamRenganathan

https://www.linkedin.com/in/renganathanofficial

AI-Powered Cyber Threat Detection and Response: SIEM and Compliance solution powered by AI, real-time correlation, and threat intelligence. Built for simplicity, reduced noise and affordability. Learn More

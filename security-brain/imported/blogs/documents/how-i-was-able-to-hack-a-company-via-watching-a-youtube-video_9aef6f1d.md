---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-02_how-i-was-able-to-hack-a-company-via-watching-a-youtube-video.md
original_filename: 2024-02-02_how-i-was-able-to-hack-a-company-via-watching-a-youtube-video.md
title: How i was able to hack a Company via watching a YouTube video
category: documents
detected_topics:
- mobile-security
- command-injection
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- api-security
language: en
raw_sha256: 9aef6f1dc878d267ffc5b6d777eeaf1aa6dff53cdf7059dc43540b0a63717ecd
text_sha256: 6c8cfc4d94d118d3131b5e32a11acba38d80d4ed72d708fe5a8a4f5341770033
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to hack a Company via watching a YouTube video

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-02_how-i-was-able-to-hack-a-company-via-watching-a-youtube-video.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `9aef6f1dc878d267ffc5b6d777eeaf1aa6dff53cdf7059dc43540b0a63717ecd`
- Text SHA256: `6c8cfc4d94d118d3131b5e32a11acba38d80d4ed72d708fe5a8a4f5341770033`


## Content

---
title: "How i was able to hack a Company via watching a YouTube video"
url: "https://ahmadmansourr.medium.com/how-i-was-able-to-hack-a-company-via-watching-a-youtube-video-without-any-technical-pentesting-4941753a150a"
authors: ["Ahmad Mansour"]
bugs: ["Weak credentials"]
publication_date: "2024-02-02"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 461
scraped_via: "browseros"
---

# How i was able to hack a Company via watching a YouTube video

Ahmad Mansour
 highlighted

How i was able to hack a Company via watching a YouTube video
Ahmad Mansour
Follow
3 min read
·
Feb 1, 2024

104

2

Hello everyone, its Ahmad here, a penetration tester from Lebanon, without wasting time introducing, lets get into details of this bug.

In this article i will be explaining an outside of the box way of thinkin that helped me to access a company data on a recent pentest, with just watching a YouTube video, which actually i rarely see pentesters focusing on such scenarios where they tend to see demo videos of a company dashboard usage ( most of the time they would contain some hidden information, paths, entry points )

Yes as you heard, by just watching a YouTube video i was able to hack into their Dashboard and access all the users data.

The story started on a recent project that i had, lets call the company xyz.ae, its a company that handle Food deliveries for restaurants, upon agreeing with the client about the project, the scope was to test their mobile application and website.

As always, the first approach on a pentest would be to discover the client website and infrastructure more, just to understand what's the company is about and how does it work, which will help me later in finding more bugs and deciding which requires reporting or no

To make the pentest as normal as possible from an attacker perspective, i acted as client and asked them for a dashboard access as a normal Client privilege, and then they sent me.

So they sent me a YouTube tutorial about their dashboard and how it works

Press enter or click to view image in full size

So i was watching the video as a normal user, if you zoom in abit, you can see that the person who is explaining the video, left an email and a passwords ( which is 3 chars/digits only )

And guess what ? ..

Get Ahmad Mansour’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

No i was not able to gain anything with those creds as they were an empty account for explanation purposes :(

After that i thought about something, if the employee itself is using a weak password for a demo account, could not be that a sign that most of them would be using simple passwords ?

So again, i assumed the password would be either 123/abc as it looks from the YouTube ***, and there is no password policy but the problem resides that i do not have any username ( admin, manager, etc. does not work )…

With quick searches, i was able to get a list of employes first name and last name ( LinkedIn, Facebook, just asking the name of the customer support whom you are talking to ), with a simple burp suite intruder i just tried the first names with mix of simple passwords, and …

Press enter or click to view image in full size

And as you can see, i was able to access the main dashboard, and have admin privilege, and access the information of 100 000+ user/order, which is hard to blur as the company name is nearly everywhere on the dashboard

Key takeaways:

As a bug bounty hunter:

Always approach the application as normal user before trying to pentest it, just ask as much as you can for normal purposes actions ( videos/ explanations) most of the time those demos contain some juicy information
Think outside the box and don’t just spam some random payloads and praying that it would work, I've done in a simple way without the need of using any script or technical scripts.

As a company, website owner:

Ensure password policy for clients, and employes because brute forcing a password which has no policy couldn't be an easier attack path for attackers

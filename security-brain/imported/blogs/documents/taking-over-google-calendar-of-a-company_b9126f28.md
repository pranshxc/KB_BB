---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-04_taking-over-google-calendar-of-a-company.md
original_filename: 2018-12-04_taking-over-google-calendar-of-a-company.md
title: Taking over Google calendar of a company
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: b9126f28f1a3eedbeaf3103805ff7911bea6d9edfc51601f6225465817740be5
text_sha256: a07494a76b90ecb1b42095b725b86ca0fa082bea78e9eaf18358557c307c96c9
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Taking over Google calendar of a company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-04_taking-over-google-calendar-of-a-company.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b9126f28f1a3eedbeaf3103805ff7911bea6d9edfc51601f6225465817740be5`
- Text SHA256: `a07494a76b90ecb1b42095b725b86ca0fa082bea78e9eaf18358557c307c96c9`


## Content

---
title: "Taking over Google calendar of a company"
url: "https://medium.com/bugbountywriteup/taking-over-google-calendar-of-a-company-1c49071f6a9"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["Subdomain takeover"]
publication_date: "2018-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5546
scraped_via: "browseros"
---

# Taking over Google calendar of a company

Taking over Google calendar of a company
Daniel "V" Morais
Follow
3 min read
·
Dec 4, 2018

132

1

Hello Guys!

This time i will show an unusual takeover that I found in a company with 30.000 customers.

Summary:

The flaw allows you to take the services of google Gsuite like a common takeover, making it impossible for the company to create a new Gsuite account with the domain itself.

Explaining Takeover vulnerability:

A sub-domain takeover is considered a high severity threat and boils down to the registration of a domain by somebody else (with bad intentions) By doing this, the hacker can take full control of the sub-domains. Sub-domain Takeover can be done by using external services such as Desk, Squarespace, Shopify, Github, Tumblr, and Heroku.

You can read more about it here.

Discovery phase:

Listing all domains is the most time-consuming part of the discovery phase (i’m using my own methodology) so the first tool that i use is ‘Aquatone’ with two functions at the same time, Discovery & Takeover.

aquatone-discover — domain company.com.br && aquatone-takeover — domain company.com.br
Press enter or click to view image in full size

Find more about Aquatone here.

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The results showed me that one of the subdomains ‘calendar.company.com.br’ had a CNAME pointed to ‘ghs.googlehosted.com’ and when i tried to access i get this error:

Press enter or click to view image in full size

To confirm the CNAME association i used mxtoolbox:

Press enter or click to view image in full size

Until then i was discouraged with the false positive alert by the tool, as i already had found the same flaw, i knew that it was not possible to perform a takeover in google services. Anyway, i decided to test:

I created a new Gsuite account and specified my company domain as ‘calendar.company.com.br’

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Next, next, next… and… Done!

I received an email saying that the account was successfully registered:

Press enter or click to view image in full size

I believe that if you followed up until here, you realized the importance of running the tests to the end, even if it was not possible to schedule new events or send emails with company’s gsuite, it was enough to block new registrations on the platform.

Hope you liked it. Happy hacking :)

Find me at Linkedin.

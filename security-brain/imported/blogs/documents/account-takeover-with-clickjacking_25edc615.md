---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-19_account-takeover-with-clickjacking.md
original_filename: 2019-06-19_account-takeover-with-clickjacking.md
title: Account Takeover with Clickjacking
category: documents
detected_topics:
- command-injection
- clickjacking
- mobile-security
tags:
- imported
- documents
- command-injection
- clickjacking
- mobile-security
language: en
raw_sha256: 25edc615d8c4d21fd8e1e53445e4d787675f25cfa87484a6f291945f9496d1ff
text_sha256: a4e45c4f475f933d260db6b3231f3ba1e0d7cd79eea60bbc4c45e681f7e5d703
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover with Clickjacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-19_account-takeover-with-clickjacking.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `25edc615d8c4d21fd8e1e53445e4d787675f25cfa87484a6f291945f9496d1ff`
- Text SHA256: `a4e45c4f475f933d260db6b3231f3ba1e0d7cd79eea60bbc4c45e681f7e5d703`


## Content

---
title: "Account Takeover with Clickjacking"
url: "https://medium.com/@osamaavvan/account-taker-with-clickjacking-ace744842ec3"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["Clickjacking"]
publication_date: "2019-06-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5200
scraped_via: "browseros"
---

# Account Takeover with Clickjacking

Account Takeover with Clickjacking
Osama Avvan
Follow
2 min read
·
Jun 19, 2019

279

1

This writeup is about how I was able to change other users account email with clickjacking. It was a private program on Bugcrowd.

The Profile page of the site allows the user to change their email and there was no X-Frame Header on that page so the profile page can be loaded in an iframe.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The profile page URL was http://example.com/mi-cuenta/mi-perfil/ the page contains a form with an email field which was prefilled with the current email, so out of curiosity I just added an email parameter in the URL to check if the specified email in the parameter is being inputted in the email field and yes it worked. http://example.com/mi-cuenta/mi-perfil?email=hacked@gmail.com

Press enter or click to view image in full size

Now everything was set up, I just needed to load this URL in an iframe and make the user click on the Update button to change their email. So I created an HTML page for that to trick user into clicking that Update button.

Press enter or click to view image in full size

I loaded the URL in an iframe and created a <div> tag with the text Click here and positioned it above the Update button, so now when the User will click on Click here the Update button below it will be clicked. Which will change the User Email.

Press enter or click to view image in full size

This is the final look after setting the iframe opacity to 0, so now after clicking on the Click here text User email will be changed, and I can request a new password for the account with that email.

So that is it, Always try to look for opportunities, even small vulnerabilities can have a larger impact, Thanks for Reading.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-23_xx-to-xxx-in-one-day.md
original_filename: 2019-07-23_xx-to-xxx-in-one-day.md
title: XX to XXX in one day
category: documents
detected_topics:
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- business-logic
language: en
raw_sha256: 70607d933c3931596cae43d081932133102ab881c737b2e570e6309cbdb961cc
text_sha256: d3350164b65609d972bc8f6b5efbf8e9c98a70fd34cadc2c00aad0ca5b6dd6b2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# XX to XXX in one day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-23_xx-to-xxx-in-one-day.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `70607d933c3931596cae43d081932133102ab881c737b2e570e6309cbdb961cc`
- Text SHA256: `d3350164b65609d972bc8f6b5efbf8e9c98a70fd34cadc2c00aad0ca5b6dd6b2`


## Content

---
title: "XX to XXX in one day"
page_title: "How I made $$$$ attending one day bug bounty workshop. | by Baibhav Anand | Medium"
url: "https://medium.com/@baibhavanandjha/xx-to-xxx-in-one-day-9578858b6286"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["WePay"]
bugs: ["Account takeover", "Parameter tampering"]
publication_date: "2019-07-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5126
scraped_via: "browseros"
---

# XX to XXX in one day

Baibhav Anand
Follow
3 min read
·
Jul 23, 2019

260

1

Press enter or click to view image in full size

Hello readers,

I am Baibhav Anand Jha and this is my story about how a web security vulnerability workshop organized by BountyBash helped me multiply my money in one day.

About the workshop

I was in this workshop where Mr. Shashank Kumar was our tutor for the day. He is actually very good at teaching and I enjoyed every single second of the workshop.

So how exactly did this help me multiply money?

While I was in the workshop, Shashank sir gave us many practical advises on bug hunting. One of which was, “Whenever you see a link with two parameters try changing one of the parameters and check if the value gets accepted.”

The workshop ends. It was a wonderful experience. I got to learn so many new things.

Now while I am on my way home my phone beeps but I didn’t check it instantly. I decided to check it upon reaching home.

I was in my home casually sitting in front of TV. I check my phone for the notification and there was this email from HackerOne about a private program. I checked the program like I check every other program. I decided to sign up. As I was signing up I got this confirmation email to verify if the email belonged to me.

The link looked something like : https://www.website.com/register/verify/(my email)/(token)

Looking at this link I was like

“Two parameters” just like what Shashank sir told us to check. “Let me dig in a little more”, I thought to myself. I didn’t open the link and decided to create a new account using a random email. Since, I didn’t have access to the new random email I decided to modify my confirmation link by changing the email parameter to that of the new random email but I didn’t change the token.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And as soon as I opened the modified link, I was like

It got verified!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

I instantly reported it to the program, and they reward me a 3digit bounty.

I then thought to myself, “why not try this in other websites as well.” I looked into some public programs at HackerOne and I came across this website called (Censored until fixed). It is a fairly popular website I am sure most of you would have heard about it before.

Co-incidentally it had the same vulnerability. And I was like

Another $XXX BOUNTY!!!!!!!!!!!!!!!!!!!!

Thank you for making it to the end of the story. Here is a bug bounty tip — Whenever you see a link with two parameters try changing one of them and check if the value gets accepted.

Wanna connect?

Here are some of my social media profiles where you can find me.

Facebook -https://www.facebook.com/ibaibhav

Instagram- https://www.instagram.com/baibhavanand

Twitter- https://www.twitter.com/spongebhav

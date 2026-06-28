---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-26_disabling-new-emails-from-facebook-without-email-owner-interaction.md
original_filename: 2017-07-26_disabling-new-emails-from-facebook-without-email-owner-interaction.md
title: Disabling New Emails From Facebook Without Email Owner Interaction
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 879f6ceff0ff4a98b05993a6b0085c16e2787ac06a492d53b5a47a2c5851eb88
text_sha256: cdae73136f94fb141070e7746638fa46d025a0837201cc5f558e1bf8f761f41d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Disabling New Emails From Facebook Without Email Owner Interaction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-26_disabling-new-emails-from-facebook-without-email-owner-interaction.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `879f6ceff0ff4a98b05993a6b0085c16e2787ac06a492d53b5a47a2c5851eb88`
- Text SHA256: `cdae73136f94fb141070e7746638fa46d025a0837201cc5f558e1bf8f761f41d`


## Content

---
title: "Disabling New Emails From Facebook Without Email Owner Interaction"
url: "https://medium.com/@zahidali_93675/disabling-new-emails-from-facebook-without-email-owner-interaction-11c979778a68"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2017-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6139
scraped_via: "browseros"
---

# Disabling New Emails From Facebook Without Email Owner Interaction

Disabling New Emails From Facebook Without Email Owner Interaction
Zahid Ali
Follow
2 min read
·
Jul 26, 2017

5

I was following lokesh kumar’s bug ‘Confirming new email/mobile-number bug in facebook’ https://www.youtube.com/watch?v=4euBQCMxlE8 …. He found this bug in 2016 and i was following in 2017 as i saw it to late. You can see the video he wrote ‘POC’ inside the video.

So i was following the steps and was like ‘wow’ bug has been fixed. Now what’s next???

I thought what if the whole account is disable. As you people know there are a few ways to disable facebook account for reporting fake account or that specific account violates facebook terms and conditions. So i did something fishy here ;d , i copied celebrities photos in my test account and set as a display and cover photos. After that reported from another account that this guy is violates facebook AUP.

After a few hours my account has been disabled from facebook and due to the disability unconfirmed email was also disabled permanently.

Proof of concept

Create facebook account with the email you want to disable permanently and do not confirm email.
copy the photos of any celebrity ‘‘verified one’’
upload on your display and cover photo
Now change your first name last name and set as it is the one from where you copied the photos. (celebrities first name last name)
report that account from your another fb id.
that’s it. In return facebook disable the unconfirmed email aswel.

WARNING.

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is a working bug so do not harm any user. Try to test it to your own email addresses.

According to Facebook policy only email owner can disable his email id permanently and for that facebook send that instructions in a very first email when we create facebook account.

But here attacker can disable any email id permanently from facebook without email owner interaction.

Got a reply from admin ‘Neal’

After all facebook knows their security best.

Report closed as . N/A

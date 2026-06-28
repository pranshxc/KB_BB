---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-29_story-of-an-idor-via-email.md
original_filename: 2019-07-29_story-of-an-idor-via-email.md
title: Story of an IDOR via Email
category: documents
detected_topics:
- idor
- sso
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- idor
- sso
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: 68bb1e0fb4502d7bbe2b57a61e4eaed5e36d32e61e66f4a0142b3f5cbc2831a8
text_sha256: efcbd0da35f0bd2d1d7615383c26b9579156055fcc4f866f1d66b88e67b2a797
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Story of an IDOR via Email

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-29_story-of-an-idor-via-email.md
- Source Type: markdown
- Detected Topics: idor, sso, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `68bb1e0fb4502d7bbe2b57a61e4eaed5e36d32e61e66f4a0142b3f5cbc2831a8`
- Text SHA256: `efcbd0da35f0bd2d1d7615383c26b9579156055fcc4f866f1d66b88e67b2a797`


## Content

---
title: "Story of an IDOR via Email"
page_title: "cat ~/footstep.ninja/blog.txt"
url: "https://footstep.ninja/posts/idor-via-email/"
final_url: "https://footstep.ninja/posts/idor-via-email/"
authors: ["Shuaib Oladigbolu (@_sawzeeyy)"]
bugs: ["IDOR"]
publication_date: "2019-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5116
---

# Story of an IDOR via Email

  * Jul 29, 2019
  * 2 min read

A year ago, I discovered an Insecure Direct Object Reference (IDOR) vulnerability which allowed anyone to reply to messages on behalf of other users on a website. I have been very much interested in this class vulnerability considering how easy one could find one by paying attention to details.

The target allows project creation where users can send messages to one another and get notified by email. They can also send replies directly from email and it would reflect on the website.

### An Informative Report

Initially, I had discovered a vulnerability which I reported with the subject “Persistent Association of an Email to Projects”. This allowed me to create an activity in a project from an email that has been removed from an account. While it seems like a vulnerability to me, it wasn’t to the target. The team decided the scenario described was unlikely to occur and fixing it would be decremental to user experience.

![This got me thinking](https://media.giphy.com/media/3ohzdQiW3BvzKfwUjm/giphy.gif)

The flow was:

> Create an Account → Create a Project → Send Message → Receive Mail Notification → Change Email Address → Confirm the Change → Respond to the Mail Notification → Activity Created on Project!

PS: Send Message means to send a message in the project and Receive Mail Notification means someone else replied and you got notified in email. Also, confirming the change entailed requesting a password reset with the old email address which returned an error confirming the email was no longer linked to an account.

### Aaand, the IDOR!

I couldn’t get my mind off the other report, so I kept looking. And after a week, I got an IDOR via the same channel.

![Gotcha! Awesome :\)](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)

The reply-to email address caught my attention and on a closer look, it contains my user ID and the project ID. It had the following structure:

###### [Constant Token]+[Project Unique Token]-[User ID]-[Project ID]@inbound.postmarkapp.com

Example:

###### 7458hb73fa4d5hs97wf8fs0bkb4a8392+1bafh7sjh245h525bj6n74knk134134jn563n357-123456-2345678@inbound.postmarkapp.com

PS: The target is NOT PostmarkApp and the tokens and IDs are just an example :D

Since it was quite easy to get other user’s ID by viewing their profile, I just replaced my user ID with the other user’s ID and sent an email to the crafted email address. And the activity got created in the project.

Until next time!

### Timeline

May 22, 2018 - First Report Sent

May 22, 2018 - Marked Informative

May 29, 2018 - Second Report Sent

May 30, 2018 - Report Triaged

June 5, 2018 - Fix Requested and Confirmed

June 6, 2018 - Bounty Awarded

Share on [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)[](https://twitter.com/intent/tweet/?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)[](mailto:?subject=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"&body=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f&title=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"&summary=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"&source=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)[](https://reddit.com/submit/?url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f&resubmit=true&title=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email")[](whatsapp://send?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"%20https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)[](https://news.ycombinator.com/submitlink?u=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f&t=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email")[](https://telegram.me/share/url?text=I%20just%20read%20"Story%20of%20an%20IDOR%20via%20Email"&url=https%3a%2f%2ffootstep.ninja%2fposts%2fidor-via-email%2f)

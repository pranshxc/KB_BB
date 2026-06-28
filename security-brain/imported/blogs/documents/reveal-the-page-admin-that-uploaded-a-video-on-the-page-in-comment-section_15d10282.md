---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-02_reveal-the-page-admin-that-uploaded-a-video-on-the-page-in-comment-section.md
original_filename: 2020-11-02_reveal-the-page-admin-that-uploaded-a-video-on-the-page-in-comment-section.md
title: Reveal the page admin that uploaded a video on the page in comment section
category: documents
detected_topics:
- command-injection
- otp
- csrf
- information-disclosure
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- csrf
- information-disclosure
- business-logic
- mobile-security
language: en
raw_sha256: 15d102825471ac0fef300b332ab4e0c23fc6ff73f5024207325d37b7048ff423
text_sha256: d3f1ef8525807888be4c5819551865921d6dc82add0b55cd8257abc68362a0a6
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Reveal the page admin that uploaded a video on the page in comment section

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-02_reveal-the-page-admin-that-uploaded-a-video-on-the-page-in-comment-section.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf, information-disclosure, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `15d102825471ac0fef300b332ab4e0c23fc6ff73f5024207325d37b7048ff423`
- Text SHA256: `d3f1ef8525807888be4c5819551865921d6dc82add0b55cd8257abc68362a0a6`


## Content

---
title: "Reveal the page admin that uploaded a video on the page in comment section"
url: "https://lokeshdlk77.medium.com/reveal-the-page-admin-that-uploaded-a-video-on-the-page-in-comment-section-9760e4a31453"
authors: ["Lokesh Kumar (@lokeshdlk77)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
bounty: "4,838"
publication_date: "2020-11-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4161
scraped_via: "browseros"
---

# Reveal the page admin that uploaded a video on the page in comment section

Lokesh Kumar
Follow
3 min read
·
Nov 2, 2020

240

Reveal the page admin that uploaded a video on the page in comment section

This post is about an bug that I found on Facebook which used to disclose the page role person’s User ID when posted a video on comment section of the page.

Recently I read a page admin disclosure writeup that was found by Kassem Bazzoun in https://bugreader.com/kbazzoun@221 .That bug Reveal the page admin that uploaded a video on the page feeds and After reading the Write Up then I decided to try if I can bypass the Fix with different scenarios.

The Question Raised in my mind that how Facebook server will validate the Video ID if it is in Different section in pages.

Example:

Video in Page Cover Pic
Video in Page Conversation
Video in Comment Section on page feeds

The 3rd example disclosed the page admins User ID in response. with same reproduction steps in Kassem Bazzoun Write Up .

Reproduction Steps:

Find if any video was uploaded in comments section of page post. that was uploaded as page.
Press enter or click to view image in full size

2. Then the attacker need to get the Video ID of the video in comments by using Facebook Api.

Get Lokesh Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Endpoint: https://graph.facebook.com/v5.0/PAGEID_POSTID?fields=comments{attachment}&access_token=XXXX

Press enter or click to view image in full size

3. After getting the Video ID open the https://messenger.com and click any images that was send between the conversation and then click “Info” button. Before Clicking the info button make sure Burp Suite Intercept is on.

Press enter or click to view image in full size

4. Intercept the request and replace the node(xxxxxxx) Base64 value into the Video ID in the comment section

Press enter or click to view image in full size

5. After forwarding the the request the response disclose the creator User ID of the page role person that who uploaded the video.

Press enter or click to view image in full size

Timeline:

22-Sep-2020: Report Sent

22-Sep-2020 : Further investigation by Facebook

08-Oct-2020: Fixed confirmed by Facebook and me

10-Oct-2020: $4500 bounty + $338 bonus awarded by Facebook

Press enter or click to view image in full size

This bug was reported on BountyCon2020 event submission and Thank you Facebook Team for quickly addressing and fixing this issue.

Apart from this bug also found another 2 bugs during event submission .

Delete any Photos in Facebook.
Stealing CSRF token using Click Jacking Attack.

Will make this remaining writeup soon..

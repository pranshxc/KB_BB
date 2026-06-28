---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-21_what-an-injection-into-jquery-selector-can-lead-to.md
original_filename: 2022-02-21_what-an-injection-into-jquery-selector-can-lead-to.md
title: What an injection into jQuery-selector can lead to
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: f37fa9f9aa8896d10290ee3acf872a6093d1dc2ce5251328b28a2c838ef2082b
text_sha256: 8a675bb187ba41724356a43ae15cf78c4aab5fa047301213733f9016a652caed
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# What an injection into jQuery-selector can lead to

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-21_what-an-injection-into-jquery-selector-can-lead-to.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `f37fa9f9aa8896d10290ee3acf872a6093d1dc2ce5251328b28a2c838ef2082b`
- Text SHA256: `8a675bb187ba41724356a43ae15cf78c4aab5fa047301213733f9016a652caed`


## Content

---
title: "What an injection into jQuery-selector can lead to"
url: "https://systemweakness.com/what-an-injection-into-jquery-selector-can-lead-to-1fcaabfd51e5"
authors: ["Anton Subbotin (@ska_vans)"]
bugs: ["CSRF"]
publication_date: "2022-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2881
scraped_via: "browseros"
---

# What an injection into jQuery-selector can lead to

What an injection into jQuery-selector can lead to
Anton Subbotin (skavans)
Follow
3 min read
·
Feb 21, 2022

112

1

​I somehow came across a page with something like a user survey (the program is private, so I will speak abstractly).

The owner of the survey chooses which questions (from a pre-prepared list) he wants to include in it. When saved, they fly to the server in the form
{“chosen_questions”: [“country”, “gender”, “favorite_movie”]}

It turned out that I can add any strings to this array, even those that do not match any of the provided questions, and they will be saved quite successfully.
When a visitor enters the survey, this JSON with questions is present inside the HTML, and on the client-side the following form is crafted:

<form id=questions>
<input id=country>
<input id=gender>
<input id=favorite_movie>
</form>

And there is also a form submit function that does something like

var results = {};
for (q of chosen_questions) {
  results[q] = $('form#questions > input#' + q).val()
}
send_post('/results', results);

After the user has filled out the form and sent it, the owner of the survey can see the user’s email in his personal account and this very results with answers.

As you can see, the question name is injected into the jQuery selector without any filtering. The jQuery version was the most recent, and so you can forget about XSS. I’ve never really worked with jQuery before. I poked around a little different variants of selectors and found interesting behavior: it turned out that the selector like $(‘#invalid,#valid’)if there is no element with id=invalid on the page, but there is an element with id=valid, it returns the second one.

Get Anton Subbotin (skavans)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In other words, you can separate several selectors with commas, they will be executed one-by-one, and as soon as one of them succeeds, the element will be returned. Since I had an injection inside the selector, I looked for inputs on the survey page that contain sensitive data. And of course I found a CSRF token in some other form. It looked like this:

<input name=csrf value=123123123>

Finally, I crafted the following attack scenario:
1. I created my survey, as a list of questions I saved something like
{“chosen_questions”: [“country”, “gender”, “INVALID,
[name=’csrf’]”]}
2. When the user opens my survey, fills the fields, and clicks the “Submit” button, the form submit function loops through the JSON questions in turn, injects them into the jQuery selector, finds the desired input, and puts its value in results.
3. When it comes to the third question, jQuery looks for input with a selector like this: $(‘form#questions > input#INVALID,[name=”csrf”]’)

The form#questions > input#INVALID element is searched first, but since there is no input with id INVALID, this part of the selector is ignored. Next, the element [name=’csrf’] is searched for, which matches the input with the CSRF token inside. It is found successfully, and its value is included in results.

Accordingly, after submitting the form, I, as an attacker, can see the victim’s CSRF token as an answer to the third question :)

What is especially cool is that the user’s email is also available to me, as it is automatically attached to each answer. Thus, I can send each victim an email with a link to a specially crafted CSRF form, where the CSRF token of this particular user will be included, and forge any request for a service on his behalf.

If you love my posts you can subscribe me on Patreon (from $1 per month): https://www.patreon.com/skavans

All my posts (including this one) are first published in my Telegram channel. Beyond, there is a lot of exclusive content about being a full-time Bug Bounty Hunter. Subscribe:

Bounty PLZ | in English
For three years now, my main job has been Bug Bounty Hunting. It’s like freelancing, but only about infosec (and more…

t.me

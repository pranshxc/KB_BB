---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-02_an-amazing-way-to-turn-a-xss-into-an-ato_2.md
original_filename: 2023-01-02_an-amazing-way-to-turn-a-xss-into-an-ato_2.md
title: An amazing way to turn a xss into an ATO
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 6760f553707299946143d21b6489c7988f9cfb216ab83deee584cd1c55f437e2
text_sha256: 10c9dc69460559b3e571d1100df1465849fbb99bf808c0dcc04573af6c66a97b
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# An amazing way to turn a xss into an ATO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-02_an-amazing-way-to-turn-a-xss-into-an-ato_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `6760f553707299946143d21b6489c7988f9cfb216ab83deee584cd1c55f437e2`
- Text SHA256: `10c9dc69460559b3e571d1100df1465849fbb99bf808c0dcc04573af6c66a97b`


## Content

---
title: "An amazing way to turn a xss into an ATO"
url: "https://medium.com/@nakah_/an-amazing-way-to-turn-a-xss-into-an-ato-40bc92772195"
authors: ["Naka"]
bugs: ["XSS", "Account takeover"]
publication_date: "2023-01-02"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1712
scraped_via: "browseros"
---

# An amazing way to turn a xss into an ATO

An amazing way to turn a xss into an ATO
Naka
Follow
2 min read
·
Jan 2, 2023

21

1

In this write-up, I will discuss a bug that both myself and Flag_c0 discovered in a program. Without further delay, let’s get into the details of the vulnerability.

Press enter or click to view image in full size
Finding the xss

Flag_c0 found an XSS vulnerability while browsing the website. He discovered a hidden parameter that allowed them to bypass a simple filter by changing `<script>` to `<ScRiPt>`, leading to the XSS vulnerability. This vulnerability was easy to find, which is why it was marked as a duplicate.

Account Takeover

To escalate this issue, Flag_c0 found that the CSRF token was being reflected on the source code in the profile settings when visited. This meant that if we were able to obtain the CSRF token, we could use JavaScript to change the email and profile settings.

Get Naka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, we encountered difficulties while attempting to fetch the settings because the filter was blocking certain words , so I had the idea to use an external JavaScript file, <script src=”my_js.file”>, to make it easier to fetch the settings since it would allow me to escape the filters.

Now that the difficult part is completed, we just need to extract the CSRF token and send a POST request to update the email and country in the profile settings.

Press enter or click to view image in full size

This code defines two functions: `changeEmail` and `handleResponse`. `ChangeEmail` sends an HTTP GET request to `/xx/profile/edit`, and when the response is received, it calls the `handleResponse` function.

The `handleResponse` function extracts the CSRF token from the response text and then sends an HTTP POST request to `/xx/profile/update` with the necessary headers and request body to update the email address and country in the profile settings.

I hope that this information was clear and helpful. Thank you for reading.

Feedback, suggestions and your point of view are always appreciated!

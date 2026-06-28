---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-14_from-open-redirect-to-reflected-xss-manually.md
original_filename: 2022-07-14_from-open-redirect-to-reflected-xss-manually.md
title: From Open Redirect to Reflected XSS manually
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 47768954fc909b53840d8245da24368cf6bd2a7c1ffb9f10fef9dc396f83e788
text_sha256: 575880c83344ee2c9e4967e3e6b7d5417bdf89104ec5c64c339822f8950dfb1a
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# From Open Redirect to Reflected XSS manually

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-14_from-open-redirect-to-reflected-xss-manually.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `47768954fc909b53840d8245da24368cf6bd2a7c1ffb9f10fef9dc396f83e788`
- Text SHA256: `575880c83344ee2c9e4967e3e6b7d5417bdf89104ec5c64c339822f8950dfb1a`


## Content

---
title: "From Open Redirect to Reflected XSS manually"
url: "https://medium.com/@rodricbr/from-open-redirect-to-reflected-xss-manually-64e633a3d23f"
authors: ["Rodric"]
bugs: ["Open redirect", "Reflected XSS"]
publication_date: "2022-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2455
scraped_via: "browseros"
---

# From Open Redirect to Reflected XSS manually

From Open Redirect to Reflected XSS manually
Rodric
Follow
3 min read
·
Aug 15, 2022

66

1

# For the purpose of this write-up, and the integrity of the company, we’ll consider that the target we’re testing is:
> https://redacted.com/

# What is an Open Redirect?
- An Open Redirect vulnerability is when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behavior can be leveraged to facilitate phishing attacks against users of the application.

# What is a Cross-Site Scripting (XSS)?
- A Reflected XSS vulnerability occurs when user input is immediately returned by a web application in an error message, search result, or any other response that includes some or all of the input provided by the user as part of the request, without that data being made safe to render in the browser, and without permanently storing the user provided data.

# How I found the vulnerable parameter:
- When analyzing the requests that are made to the site using the “network” tab of “dev tools”, I reloaded the page and noticed strange .js (Javascript) files being called by the application.
I noticed that there were 4 Javascript files being called consecutively (one after the other), so I decided to investigate such files, whose names were: “0.js”, “5.js”, “4.js”, and so on…

- The file “5.js” returned a 404 status code when I tried to access it, and the files “0.js”, “4.js”… were returning status code 200, and so I could read them.

- After analyzing the javascript file manually for a few minutes, I noticed that in the “0.js” file,
there was a parameter that received an href value in the application, similar to this:
> window.location.href(“?url=”);

- When I noticed that there was a parameter called “url”, I knew right away that this parameter could be used to redirect to an external site when the request was sent to the application, and that’s exactly what I tested shortly thereafter.

Get Rodric’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

# Proof of Concept (PoC):
- After the root directory “/”, I added the parameter I had found earlier (url), and I included a url as the value of this parameter, and it looked like this:
> https://redacted.com/?url=https://www.google.com/

And… to my surprise, nothing happened!

- Then I remembered that a few hours earlier, when I was analyzing the same subdomain, I had noticed that certain characters made a difference when they were included within the value of certain parameters I was testing. So I started trying to bypass the character filter manually, and a few minutes later, using the following payload:
> ?url=https://www.google.com/%3C--//#/

I had managed to bypass the character filter! And when I loaded the url, I was redirected to www.google.com, which means the “url” parameter was vulnerable to open redirect!

- Since we could call a url including the http protocol after the url parameter itself, my friend (ferreiraklet), which was hunting along with me in another part of the application, managed to find a way to get an XSS(Cross-
site scripting) by calling the “javascript:” attribute, which executes whatever is
after the colon (:) in Javascript, the Reflected XSS payload looks like this:
> ?url=javascript:confirm(document.domain)%3C — //#/

- And that was how I managed to manually find a vulnerable parameter while analyzing a Javascript file, then finding an Open Redirect vulnerability, and escalating it to a Reflected XSS! Please check out my Github, there you’ll find more information about me and what I do.

This was my first bug hunting write-up ever, and I hope you enjoyed it!

Thank you,
Rodric researcher.

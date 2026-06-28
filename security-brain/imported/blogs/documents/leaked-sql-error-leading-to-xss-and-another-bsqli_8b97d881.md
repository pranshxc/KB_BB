---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-22_leaked-sql-error-leading-to-xss-and-another-bsqli.md
original_filename: 2024-01-22_leaked-sql-error-leading-to-xss-and-another-bsqli.md
title: Leaked SQL Error Leading To XSS And Another BSQLi
category: documents
detected_topics:
- xss
- sqli
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- xss
- sqli
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: 8b97d8819b52cf939c0feed8f666cf354fa803a4d1f6feb05684ab2c577c9515
text_sha256: be89703509477fa5846d30a2dec70ebfed507e852d512bbe4d7ce7f196075e5a
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Leaked SQL Error Leading To XSS And Another BSQLi

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-22_leaked-sql-error-leading-to-xss-and-another-bsqli.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `8b97d8819b52cf939c0feed8f666cf354fa803a4d1f6feb05684ab2c577c9515`
- Text SHA256: `be89703509477fa5846d30a2dec70ebfed507e852d512bbe4d7ce7f196075e5a`


## Content

---
title: "Leaked SQL Error Leading To XSS And Another BSQLi"
page_title: "Leaked SQL error leading to XSS, and another BSQLi... | by Sevada797 | Medium"
url: "https://medium.com/@zatikyan.sevada/leaked-sql-error-leading-to-xss-and-another-bsqli-cdadde032687"
authors: ["Zatikyan Sevada"]
bugs: ["Reflected XSS"]
publication_date: "2024-01-22"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 512
scraped_via: "browseros"
---

# Leaked SQL Error Leading To XSS And Another BSQLi

Sevada797
 highlighted

Sevada797
Follow
3 min read
·
Jan 22, 2024

34

Hello everyone, it would be unpolite of me not returning the favour to medium cyber security community which gives me so much knowledge

I am too polite

so here I am with this writeup of another interesting story of blind SQL injection and another bug in backend, OK, so about website where I found BSQLi-

while testing for some requests that any registered user has access to, I thought ‘let me be a bit more creative’, after, while playing with the password reset functionality, (which was working by sending link to the email) I understood that it’s not a one-time link, and another thing I noticed was the fact that the authentication-code/token was in url, so I imagined that the backend probably gets that token and makes SQL query to check if it’s active token than → proceeds function password reset.

And this time it was an easy win for me, all I needed, was to pass the url to sqlmap, but I don’t remember if I also used `-p` to mention the exact parameter, anyways passing it gave me injection found.

Second story about the problem in backend of some website. While testing, I thought of inserting emoji in the search query,( this technique is known as fuzzing, trying things to make application break or behave strange ) now, if I remember correct at first nothing happened, but after I inserted the emoji in url, like

redacted.com/…/search?filter%5Bkeyword%5D=😎

After this I saw error page¹, than I quickly pressed Ctrl+U to view the source. After scrolling down a bit I saw

General error: … mixed colation error

yes it was leaked SQL error, now of what caused this, was that the collation was set to

utf8_general_ci

and turns out the emojis aren’t included in this encoding range, instead they could’ve used

utf8mb4_general_ci

which wouldn’t have lead to error, but the next thing you question will be but why is the error visible?

Get Sevada797’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Well sadly I am not familiar with yarn, I remember in leaked error there was yarn mentioned, yeah, but I am familiar with PHP and I think that it should also have something like `error_reporting(0);` which will not display errors, and this should always be done in real running applications to prevent information disclosure via errors.

Ok so what can I do with this? Well I couldn’t do pretty much anything 🙂

I saw the whole query being reflected in error message, but after trying several injection techniques to try breaking the quotes, I stopped, and I wasn’t intended to test it longer, for what I regret now.

But one thing only came to my mind was XSS, well nobody would html-escape the SQL select query in their back-end right 😀

And I inserted simple XSS injection after the emoji with script tags, -and also this was leading to ATO via cookies, as they weren’t httpOnly, my JS code could access them, +csrf to every request- to be more demonstraitive here payload.

redacted.com/…/search?filter%5Bkeyword%5D=😎<script>confirm(8)<%2fscript>

There wasn’t even WAF so this payload worked just fine, but in next writeup I will tell how I bypassed the WAF for an XSS.

Happy hacking, I whish luck to everyone in their hacking journey, and I encourage everyone sharing their gained knowledge from hacking in here, so that we can learn from each others findings, ciao guys !

I don’t remember if it was error page tho, or if everything showed up fine, but no I think it displayed error 404 page, maybe there wasn’t other custom error page for 500 internal server error ) so any other type of error was handled by error page 404.

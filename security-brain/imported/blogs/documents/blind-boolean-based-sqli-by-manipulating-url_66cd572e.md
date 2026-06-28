---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-08_blind-boolean-based-sqli-by-manipulating-url.md
original_filename: 2024-01-08_blind-boolean-based-sqli-by-manipulating-url.md
title: Blind Boolean Based SQLi By Manipulating URL
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 66cd572e8b84980e55e3a8e7c1c84b7059112d84a0f0a3ad48517672b5c76097
text_sha256: 698a67a5f36e80bb1e59c8c60f3490adf6ec543c8e91187e089d3bc852a0e093
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Blind Boolean Based SQLi By Manipulating URL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-08_blind-boolean-based-sqli-by-manipulating-url.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `66cd572e8b84980e55e3a8e7c1c84b7059112d84a0f0a3ad48517672b5c76097`
- Text SHA256: `698a67a5f36e80bb1e59c8c60f3490adf6ec543c8e91187e089d3bc852a0e093`


## Content

---
title: "Blind Boolean Based SQLi By Manipulating URL"
page_title: "Blind boolean-based SQLi, by manipulating url | by Sevada797 | Medium"
url: "https://medium.com/@zatikyan.sevada/blind-boolean-based-sqli-by-manipulating-url-96e1e086378c"
authors: ["Zatikyan Sevada"]
bugs: ["SQL injection"]
publication_date: "2024-01-08"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 570
scraped_via: "browseros"
---

# Blind Boolean Based SQLi By Manipulating URL

Sevada797
Follow
3 min read
·
Jan 8, 2024

160

Press enter or click to view image in full size

Hello guys, today I will talk about how I’ve found a blind boolean-based SQL-injection, by manipulating url,

Alright so, it appears that modern web apps can fetch information from link itself, I know most of you would know the GET request with parameters, but this didn’t have parameter instead backend has some regexp that get’s the numbers in the url and makes an sql query, from a link like this

x.com/resume/doesntmatterwhathere-76541

So now as you might guessed anything before the numbers might not matter, and when I tested it — it actually didn’t matter, so now the most simple injections will give us hint if there is possible SQLi(injection)

After testing this url

x.com/resume/-76541'

I got an error 404 as response status code, and there was a redirect written in JS with window.location, which after was causing redirection to the main page which is just

x.com

After this I tried another injection really a simple one

x.com/resume/-76541'%20OR%20'

And it returned actual persons resume, indicating SQL returned true, I was also a bit confused that why a number, is being used in quotes in SQL query but it is what it is, if this was just a number, a payload like this

payload: 76541+1-1
payload url-encoded: 76541%2B1%2D1

Should return the same content that returns this link below

x.com/resume/76541

Because let’s imagine the SQL query and you will get it

SELECT * FROM users where userID=76541

Our payload that does +1–1 basically changes nothing but in our case this was a string like this

SELECT * FROM users where userID='76541'

OK now it was a little bit hard to get sqlmap return some data for us, as it was unusual case, I get always 404 error code and only when sql statement is returning false I get another HTML response, here I quickly asked chatGPT to help me,

Get Sevada797’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And turns out there are several options like

--code, --string, --not-string

I only needed these 2 —code and —not-string, first one is for telling what status code to be expected as normal, second telling what exact response to check for to understand that SQL statement returned false, also we can use —random-agent as we might get blocked, and sometiimes cookies as well, but this time there wasn’t need for that, tho sometimes you should run sqlmap verbosly

sqlmap ... -v 4

Or -v 5, I don’t remember now, to see responses and see if your requests aren’t getting blocked, remember mostly status code 403 is returned whenever WAF blocks but it’s not always like that so checking the response is the best option, and then try —tamper with custom bypass payloads untill you are able to bypass WAF, OK this was it but ah no wait before I tried running sqlmap I actually did manual testing, and

NOTICE: IF I DIDN’T FIND THIS MANUALLY, SQLMAP WOULDN’T FIND IT EVER

Ok so what I did was I tried several payloads, after guessed the column count using ORDER BY, and after prooved rightness of ORDER BY with UNION statement

Here the payloads I used

payload: 76541' ORDER BY 38 #
payload url-encoded: 76541'%20ORDER%20BY%2038%20%23
full payload: x.com/76541'%20ORDER%20BY%2038%20%23

Sure before testing 38 I went like 2, 7, 24 everything was OK SQL was returning true, but than let’s say 41 would return the error response which is redirection in JS as I told you above, like this (look below)

<script>window.location="/";</script>

And sure I used this with —not-string

Now back to proving if the columns are actually 38 and not less or more

We can use UNION for this, and in SQL you can select everything + aditionally select something, just the returned columns with union should be exact same as first columns returned by SQL Select statement writen right before UNION.

So I wrote these payloads

full payload: x.com/76541'%20UNION%20SELECT%201,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1%20%23

Now there are exact 38 1’s here if I wrote one 1 more or less we would get error, by this I finally confirmed the vuln and submited my report additionally giving them their db tables as proof.

Thanks for reading, if you have questions fill free to ask in comments.

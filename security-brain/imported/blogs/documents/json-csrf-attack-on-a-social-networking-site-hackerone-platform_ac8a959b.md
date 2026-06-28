---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-26_json-csrf-attack-on-a-social-networking-sitehackerone-platform.md
original_filename: 2018-01-26_json-csrf-attack-on-a-social-networking-sitehackerone-platform.md
title: JSON CSRF attack on a Social Networking Site[Hackerone Platform]
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: ac8a959b4997996eff7a739b3f3c8e0f7ec500a483ca412ab1c32c2bee641782
text_sha256: 655abaa62268ed0bffbc9fcf39f976a28b8deca680dbb196a847cf62f463750a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# JSON CSRF attack on a Social Networking Site[Hackerone Platform]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-26_json-csrf-attack-on-a-social-networking-sitehackerone-platform.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `ac8a959b4997996eff7a739b3f3c8e0f7ec500a483ca412ab1c32c2bee641782`
- Text SHA256: `655abaa62268ed0bffbc9fcf39f976a28b8deca680dbb196a847cf62f463750a`


## Content

---
title: "JSON CSRF attack on a Social Networking Site[Hackerone Platform]"
url: "https://medium.com/@pig.wig45/json-csrf-attack-on-a-social-networking-site-hackerone-platform-3d7aed3239b0"
authors: ["Sahil Tikoo (@viperbluff)"]
programs: ["Badoo"]
bugs: ["JSON CSRF"]
bounty: "280"
publication_date: "2018-01-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5994
scraped_via: "browseros"
---

# JSON CSRF attack on a Social Networking Site[Hackerone Platform]

Sahil Tikoo
Follow
3 min read
·
Jan 27, 2018

85

JSON CSRF attack on a Social Networking Site[Hackerone Platform]

Press enter or click to view image in full size
Badoo.com on Hackerone Platform

Before describing the actual attack scenario let us first discuss what is CSRF attack ?

Basically lets consider Victim has an active session on a website and lets say victim has some details in his/her settings page on that website , so if no csrf token is implemented for the requests that go out from the settings page when someone tries to update the content in the settings page then an attacker can craft an html file or an image containing the details to be updated in the victim’s settings page using <form>, <input> etc in html , so as soon as the victim opens the image or the html file, the content in his/her settings page will get updated with the attackers’s content.

The two conditions that must be satisfied for this attack to be carried out is that first , there shouldn’t be any token going with the requests from that site , secondly the Victim should have an active session on that site.

Get Sahil Tikoo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, one year back I was searching for bugs in this site m.badoo.com on hackerone platform, where i found this request https://m.badoo.com/api.phtml?SERVER_DELETE_ACCOUNT in burpsuite in which data was going in json format , as you can guess it was a request to delete the account of a registered user and similarly i got another one which was https://m.badoo.com/api.phtml?SERVER_RESET_TRUSTED_NETWORK , it was meant to delete all the contacts of a user on that site , so when i saw these requests i noticed that no csrf token was being sent alongwith these requests but the problem was that the data was sent in Json and i had to find a way to generate an HTML file for the CSRF POC , so I crafted two html files one for erasing imported contacts and another one for deleting account on m.badoo.com . But, as the content-type was json so parser introduced “=” at the end of content in header, so this became a problem for the attack to trigger but you can easily bypass such parameters by adding your own pair of values at the end like I added “ignore_me”:”’ value=’test”. The HTML code[Erasing Contacts] has been shown below :

<html>
<head>
<meta name="DNT" content="1">
<meta name="Connection" content="close">
</head>
<body>
<form action="https://m.badoo.com/api.phtml?SERVER_RESET_TRUSTED_NETWORK" method="POST" enctype="text/plain">
<input name='{"$gpb":"badoo.bma.BadooMessage","version":1,"message_type":327,"body":[],"is_background":false, "ignore_me":"' value='test"}' type="hidden">
<input type="submit">
</body>
</html>

The other thing i would like to mention here is that the entire json payload passed in the name parameter will not be accepted as content-type Json until we mention enctype=”text/plain” in the form action. So it was somehow a little bit different from a basic HTML form we generate for CSRF. The moral of this finding is that if request is going in JSON format just use encoding-type as text/plain and also bypass the “=” that is automatically appended at the end of the content in the request.Below is the Response in the Browser after the victim opened up the html code in his/her browser .

Press enter or click to view image in full size
“Your contacts are being erased, this could take up to 5 minutes.”

Finally i Received 280$ bounty from badoo through hackerone for this bug.

Press enter or click to view image in full size

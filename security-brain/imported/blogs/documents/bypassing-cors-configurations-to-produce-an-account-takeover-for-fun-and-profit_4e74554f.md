---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-13_bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit.md
original_filename: 2023-02-13_bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit.md
title: Bypassing CORS configurations to produce an Account Takeover for Fun and Profit
category: documents
detected_topics:
- cors
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- cors
- command-injection
- otp
- supply-chain
language: en
raw_sha256: 4e74554f394c8d76953bef99298a8bb341f0cba33235e4aa9c2a761da23fe775
text_sha256: 2a1bea8ee70b476882f897c1c1518db301e93234983f36c03f85bbc0191defb4
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-13_bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: cors, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `4e74554f394c8d76953bef99298a8bb341f0cba33235e4aa9c2a761da23fe775`
- Text SHA256: `2a1bea8ee70b476882f897c1c1518db301e93234983f36c03f85bbc0191defb4`


## Content

---
title: "Bypassing CORS configurations to produce an Account Takeover for Fun and Profit"
url: "https://pullerjsecu.medium.com/bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit-3e50c3f2a124"
authors: ["Josh Fam (@Pullerze)"]
bugs: ["CORS misconfiguration", "Account takeover"]
publication_date: "2023-02-13"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1534
scraped_via: "browseros"
---

# Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

Bypassing CORS configurations to produce an Account Takeover for Fun and Profit
Josh Fam
Follow
4 min read
·
Feb 14, 2023

102

1

The bug that is being written about here is from an previous bug bounty engagement for a major telecommunication company. This bug consists of a CORS misconfiguration that isn’t commonly a misconfiguration unless certain conditions are met. First for individuals who aren’t familiar with CORS technology, CORS stands for Cross Origin Resource Sharing and is a common method to bypass SOP for developers in order to retrieve information across multiple domains. CORS works by facilitating certain headers in the initial request and requires certain headers being available in the server response. The request specifies the Origin Header which declares the site that is making the request to the server in question. The relevant headers located on the server are the Access-Control-Allow-Origin headers and the Access-Control-Allow-Credentials header. Access-Control-Allow-Origin specifies the value that is located in the request’s Origin header and is only reflected in the server response if that Origin is allowed to make requests to the server. The Access-Control-Allow-Credentials header is in place in order to specify that the request made includes cookie values for the server in question. An CORS vulnerability occurs when two conditions are present, the first condition is that an attacker can specify the value in the Origin header and that value is accepted by the server and reflected in the Access-Control-Allow-Origin headers. The second condition being that the Access-Control-Allow-Credentials header is set to True, allowing cookies in the request to be utilized by the server. After these conditions are set an attacker can get a user of the server to go to his site and leak sensitive information from the that user’s session from the server in question.

Press enter or click to view image in full size

When looking for this bug I noticed that a server was returning sensitive information in the response of an logged in user. This information included the id token, refresh token and the server authentication token. The server authentication token is the value that was being used in order to authenticate the user to the server. The server’s response also included an Access-Control-Allow-Origin and a Access-Control-Allow-Credentials header set to True. This information was being returned on every response from the server.

Get Josh Fam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In this particular scenario the second condition was met, but the first condition wasn’t present. Instead of the Access-Control-Allow-Origin header being set to the value in the Origin it was permanently set to a wildcard. A wildcard in the header essentially means that any site can request information from the server cross domain, however if the Access-Control-Allow-Origin header is set to a wildcard the Access-Control-Allow-Credentials header will not be included in the server response. This was created as a security boundary to the overly permissive nature of the wildcard value. This is a problem due to the fact that the impact of a CORS vulnerability is usually a disclosure of sensitive information from a session. If the Access-Control-Allow-Credentials header isn’t available its the same as logging into an application without a session.

There is a small caveat to this rule however and it allows for this security boundary to be bypassed. If the HTTP response contains the Access-Control-Allow-Origin header with a wildcard as its value and it also doesn’t contain an Cache Control header with a value of no store, it is possible to send a request to a endpoint in question to retrieve the response from the cache instead of the website directly if a logged in user has already visited that endpoint. In this scenario, every page on this site contained the sensitive data in the HTTP response with the required headers. I selected a page that was apart of the login flow of the site to guarantee that if the user was logged in previously, that page had to be cached in the browser. The way to exploit this client side bug is utilize the fetch javascript library and change the cache option to force-cache and host the script on a malicious server.

Press enter or click to view image in full size
Example POC for this bug

After a logged in user of the vulnerable site visit the site the script will fetch the response of the page from the browser along with sensitive data in the response. In this case it was the server authentication token which allowed for a full account takeover of the logged in user.

Connect with me on Twitter: @Pullerze

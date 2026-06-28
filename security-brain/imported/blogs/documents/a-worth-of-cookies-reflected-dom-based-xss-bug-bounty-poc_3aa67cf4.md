---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-03_a-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc.md
original_filename: 2022-12-03_a-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc.md
title: A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 3aa67cf401be5fb10c2f89f24c0b42fd5513f1d2a0df6417afbde2c16970348d
text_sha256: daca0bd212789dfc7b4dfbc7693ca3d6bd7492f05a9b473754fbf9860845a596
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-03_a-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `3aa67cf401be5fb10c2f89f24c0b42fd5513f1d2a0df6417afbde2c16970348d`
- Text SHA256: `daca0bd212789dfc7b4dfbc7693ca3d6bd7492f05a9b473754fbf9860845a596`


## Content

---
title: "A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC"
url: "https://medium.com/@haroonhameed_76621/a-775-worth-of-cookies-reflected-dom-based-xss-bug-bounty-poc-3e7720c78fbe"
authors: ["Haroon Hameed (@HaroonHameed40)", "Hannan Haseeb (@HannanHaseeb11)"]
bugs: ["DOM XSS"]
publication_date: "2022-12-03"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1821
scraped_via: "browseros"
---

# A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC

A $$$ worth of cookies! | Reflected DOM-Based XSS | Bug Bounty POC
Haroon Hameed
Follow
3 min read
·
Dec 3, 2022

302

1

Hey everyone! This is Haroon Hameed and I’m here to share about my recent finding on Synack Red Team about Reflected DOM-based XSS. In this blog post, I’m going to discuss the Bug Bounty report of this discovery.

It was a QR-based target on Synack Red Team, and whenever there is a QR-based target, my brother Hannan Haseeb and I collaborate!

Vulnerability Analysis:

Lets begin! My main focus was on the main domain, which is https://redacted.com, so I won’t do any subdomain enumeration and starting looking for juicy JavaScript files and luckily I found two interesting JavaScript file, where I found the following JavaScript function:

code: function(e) {
  var a = e.car,
  t = e.articleUuid,
  i = e.returnPath,
  u = e.moreInfoData,
  m = e.currentUser,
  o = m.canPrint,
  d = void 0 === o || o,
  E = m.canBookmark,
  b = void 0 === E || E,
  f = a.uuid,
  h = i ? "Search Results" : "Car";
  return l.createElement("div", null, l.createElement("div", {
  className: "viewer-header"
  }, l.createElement("div", {
  className: "car-form-container"
  }, l.createElement("div", {
  className: "article-toolbar-container"
  }, l.createElement("div", {
  className: "page-width article-toolbar"
  }, l.createElement(l.Suspense, {
  fallback: l.createElement("div", null)
  }, l.createElement(s, a)), l.createElement("ul", {
  className: "back-to-search-ul"
  }, l.createElement("li", {
  className: "back-to-search-results"
  }, l.createElement("a", {
  className: "button",
  href: i || "/car/" + f + "/search"
  },

This code is used for rendering a car viewer component in a React application. The component displays the car details, as well as other information such as a back to search button and a tool bar that allows the user to perform certain actions. DOM based XSS is possible with this code if the href attribute of the “a” tag is not properly sanitized. If user input is not properly sanitized, it is possible for malicious code to be executed, allowing for a DOM based XSS attack.

In 2nd JavaScript file, I found the proper Source and Sink of the Reflected DOM-Based XSS, the following are our Source and Sink:

Source:

document.addEventListener("DOMContentLoaded", (function() {
  var e = document.getElementById("search-application-container")
  , t = JSON.parse(e.getAttribute("state")) || window.initialState;
  a.render(r.createElement(rr, t), e)

This Source is used for rendering a React component in the DOM. It parses the state from the element with the id “search-application-container” and passes it to the React component. The component is then rendered in the element.

Sink:

l.createElement("a", {
  className: "button",
  href: i || "/car/" + f + "/search"
  }

The DOM function l.createElement create a HTML tag a and set it’s attribute value to HTML href attribute which is user controllable returnPath parameter.

Get Haroon Hameed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After understanding the JavaScript code you will clearly see that it will take user-supplied input from returnPath parameter and executing it in DOM aka sink.

So I used the following JavaScript payload:

javascript:alert(document.domain)
Press enter or click to view image in full size

Hence, I had successfully submitted the best quality report to Synack’s Quality Rule program on Synack Red Team and was awarded with 3/3 stars and a bounty of $$$.

Social Links:

Twitter (Haroon Hameed)

LinkedIN (Haroon Hameed)

Partner:

Twitter (Hannan Haseeb)

LinkedIN (Hannan Haseeb)

We are open to work on any private pentesting projects. If you have any such projects, please feel free to DM any of us. Thank you!

If you like this write-up, Share!

Thank you!

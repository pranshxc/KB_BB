---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-05_1000-for-open-redirect-via-unknown-technique-bugbounty-writeup.md
original_filename: 2020-11-05_1000-for-open-redirect-via-unknown-technique-bugbounty-writeup.md
title: 1000$ for Open redirect via unknown technique [BugBounty writeup]
category: blogs
detected_topics:
- ssrf
- xss
- command-injection
- otp
- cors
- api-security
tags:
- imported
- blogs
- ssrf
- xss
- command-injection
- otp
- cors
- api-security
language: en
raw_sha256: 5b81bfbbdc473c3e55348896c012c8e38c15ded741bc3ca0f919bbc789c20317
text_sha256: 275fcb3d972cb1934e3821980b56372e7047cfec4bafb6391768e517efc3c9d6
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 1000$ for Open redirect via unknown technique [BugBounty writeup]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-05_1000-for-open-redirect-via-unknown-technique-bugbounty-writeup.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, otp, cors, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `5b81bfbbdc473c3e55348896c012c8e38c15ded741bc3ca0f919bbc789c20317`
- Text SHA256: `275fcb3d972cb1934e3821980b56372e7047cfec4bafb6391768e517efc3c9d6`


## Content

---
title: "1000$ for Open redirect via unknown technique [BugBounty writeup]"
url: "https://ruvlol.medium.com/1000-for-open-redirect-via-unknown-technique-675f5815e38a"
authors: ["ruvlol"]
programs: ["GitLab"]
bugs: ["Open redirect"]
bounty: "1,000"
publication_date: "2020-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4156
scraped_via: "browseros"
---

# 1000$ for Open redirect via unknown technique [BugBounty writeup]

Top highlight

1000$ for Open redirect via unknown technique [BugBounty writeup]
ruvlol
Follow
3 min read
·
Nov 4, 2020

1.2K

3

Hey, Bug bounty community!

Long time no updates, so here is a little story that you probably will find useful and maybe earn a bit money with this little trick.

A vulnerability I will talk about is not something new, it is a known behaviour for web developers. But not that many people considired it from security perspective and I never seen it being mentioned on any security paper, that’s why I decided to shed light on it.

What Open Redirect is

So, we already should know what Open redirect is. For someone who doesn’t — it is when remote attacker can set arbitrary value as a redirect destination. For example, considered following “legit” redirect chain:

https://example.com/login?redirectUrl=https://app.example.com

Which in the end leads to app.example.com. But what if someone malforms this url into following:

https://example.com/login?redirectUrl=https://evil.com

Notice that we changed end destination from app.example.com to evil.com. If web app is allowing that URL change and in the end we will get redirected to https://evil.com, then it is an open redirect vulnerability. This behaviour may be used to perform phishing attacks, access tokens stealing from authentication flows, or be combined with other vulnerabilities such as SSRF. A lot of things can be potentially done.

2. Open redirect via top-level navigation

The unknown Open redirect trick is based on iframes. If you ever used iframes, you know that same origin policy is applied to them, that means if we load iframe pointing to other origin, we cannot read its value using javascript.

Consider following HTML page on our website:

<iframe src="https://example.com" id="child"></iframe>
<script>
var a = document.getElementById("child").contentWindow.document;
console.log(a.body.innerHTML);
</script>

We get empty string in console instead of iframe content. This is what SOP is about — javascript must be restricted to read/manipulate objects in cross-origin context. Of course, there are plenty of legal SOP bypasses like postMessages, CORS and so on, but it doesn’t really relate to current issue.

So, we already know what open redirect is, we know what iframes are. Where is the bug, you might ask. By default SOP allows top-level navigation which is by design leading to open redirect. Consider following parent window HTML page (hosted on http://avtohanter.ru/poc.html):

<iframe src="http://ruvlolmail.temp.swtest.ru/toplevel.html">

Due to SOP our parent page can’t get access to child page and vice-versa.

Get ruvlol’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But if child page (http://ruvlolmail.temp.swtest.ru/toplevel.html)contains following script:

<html>
<head>
</head>
<body>
<script>
top.window.location = "https://www.google.com"
</script>
</body>
</html>

Child window have access to top.window.location property and can manipulate its value. This leads to a case when we visit avtohanter.ru/poc.html and immideately being redirected to www.google.com.

Adding a sandbox attribute to iframe without “allow-top-navigation” directive will fix that behaviour. For example, we could use

<iframe sandbox="allow-scripts allow-same-origin" src="http://ruvlolmail.temp.swtest.ru/toplevel.html">

And such redirect wouldn’t be the case.

3. 1000$ bug in GitLab.

Now I want to demonstate a real iframe-powered open redirect issue in GitLab that was fixed in 11.8.0. The link to original disclosed report is:

https://hackerone.com/reports/437142

The issue was in WEB IDE where any developer could write Javascript code and preview it into iframe (this is required to prevent XSS attacks). The issue was that preview Iframe didn’t contain sandbox attribute, allowing malicious javascript to perform top-level redirect. Here is how it looked:

Press enter or click to view image in full size

I was pretty surprised that I got awared 1000$ for such issue, big respect to GitLab security team!

4. How to find it yourself

Of course, Gitlab is not the only program I reported this issue to. And I think you can try it to find it yourself. What you should be paying attention is:

If you have a possiblity to run javascript inside iframe (as a sandbox to prevent XSS), check if it allows top-level-navigation
If you can insert iframe with arbitrary URL value (for example, on a forum), check if it has sandbox attribute and allows top-level-navigation
If there is iframe pointing to expired domain, you could try to claim it and place your script.

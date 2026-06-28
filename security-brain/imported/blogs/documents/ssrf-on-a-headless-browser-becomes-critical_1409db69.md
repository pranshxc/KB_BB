---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-03_ssrf-on-a-headless-browser-becomes-critical.md
original_filename: 2024-02-03_ssrf-on-a-headless-browser-becomes-critical.md
title: SSRF on a Headless Browser Becomes Critical!
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 1409db691a6183fd1302c87c8e647b42fccb53f82d3536503270522bed3ee37e
text_sha256: 266a190478c207a1868210d12f508683465ade16a2a5057d2d4a02aefbe5471e
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF on a Headless Browser Becomes Critical!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-03_ssrf-on-a-headless-browser-becomes-critical.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `1409db691a6183fd1302c87c8e647b42fccb53f82d3536503270522bed3ee37e`
- Text SHA256: `266a190478c207a1868210d12f508683465ade16a2a5057d2d4a02aefbe5471e`


## Content

---
title: "SSRF on a Headless Browser Becomes Critical!"
url: "https://medium.com/@Nightbloodz/ssrf-on-a-headless-browser-becomes-critical-c08daaa1017e"
authors: ["Alvaro Balada"]
bugs: ["SSRF"]
bounty: "2,000"
publication_date: "2024-02-03"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 457
scraped_via: "browseros"
---

# SSRF on a Headless Browser Becomes Critical!

SSRF on a Headless Browser Becomes Critical!
Alvaro Balada
Follow
4 min read
·
Feb 5, 2024

443

8

Press enter or click to view image in full size

When I’m frustrated and I haven’t found bugs for a long time, I like to write about my found bugs. This time, I’m going to talk about my first critical vulnerability. I found this bug on a private program on Intigriti, I will call it REDACTED.

Before explaining the bug I’d like to explain the vulnerable part of the application.

This application is used to create dashboards with images, videos and dynamic graphics using external data.

A Dashboard example looked like this:

Press enter or click to view image in full size

The main flow of this application is:

Create a dashboard
Edit it with some images, videos and graphics with data.
Save It
Export It to PDF or PNG

The Dashboard functionality relies on javascript to retrieve the JSON structure of the dashboard.

Press enter or click to view image in full size

Data retrieved from /JSONDATA, used to paint the dashboard

{
  "title":"Hello",
  "items":[
  {
  "type":"imageobject",
  "url":"https://brrrr",
  },
  {
  "type":"graphic-type",
  "data":"",
  "row":""
  },
...
  ]
}

This data can be modified sending a petition to the same API endpoint with the same data format, the dashboard data can contain multiple data types with multiple parameters

This Dashboard can be exported to PDF or PNG.

Detecting and exploiting the Headless browser

A common way to export something to PDF is through a Headless Browser

Headless Browser is a browser without User Interface that loads a webpage, it can be used to automate some web tasks.

I exported the dashboard to PDF and I extracted the metadata of the PDF.

The PDF was created using Chromium.

That means that a browser is running in the backend, if we inject some html, it will be loaded by the internal browser and we can get SSRF.

SSRF allows an attacker to cause the server-side application to make requests to an unintended location

I tried multiple injections and XSS but I didn’t find anything. After some time, I tried to understand all the parts of the Dashboard and data types.

Get Alvaro Balada’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The previous JSON showed multiple data types like “imageobject”, “videoobject”, graphics and other types, all accessible through the UI. I wanted to check all possible data types, so I opened the javascript code of the application.

A good approach to lazy loaded javascript code is search strings or endpoints, I searched for “imageobject” and I found a JSON with all possible object types including “imageobject” with an URL parameter.

Reviewing the code I found “iframeobject” and I tried to edit the dashboard to include “iframeobject” with my attacker URL.

{
  "title":"Hello",
  "items":[
  {
  "type":"iframeobject",
  "url":"https://attacker"
  },
...
  ]
}

It showed my page inside an Iframe!!

Press enter or click to view image in full size

Right after that, I exported the dashboard and I received a callback on my server!!! That was a SSRF!!!

Press enter or click to view image in full size

The SSRF loaded my page inside the PDF.

Press enter or click to view image in full size
SSRF to localhost:9222 leaked user tokens

I tried to change the iframe URL to 127.0.0.1 and localhost but the URL parameter needed HTTPS and doesn’t allow internal ip’s.

I tried redirections, octal bypasses and a lot of techniques to load internal resources, but I realized that the browser was loading my html inside an iframe, why not create another iframe inside the iframe?

My attacker’s HTML:

It worked and loaded the internal view of the application login page.

I scanned the internal network and I found an opened port localhost:9222, that port is where the headless browser API recieves requests!!.

I searched for endpoints and I found that /json lists all the active browser tabs.

I exported a new PDF and booooom:

Press enter or click to view image in full size

The PDF contained all the URL’s of active browser tabs, those URLs contained the user session token to retrieve the dashboard, that means that I could takeover the account of any user that generates a PDF or PNG.

I reported the vulnerability and It took less than 48h to be triaged and awarded.

Critical(9.1) — €2,000

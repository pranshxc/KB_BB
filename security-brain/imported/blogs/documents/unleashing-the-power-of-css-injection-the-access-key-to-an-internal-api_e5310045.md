---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-24_unleashing-the-power-of-css-injection-the-access-key-to-an-internal-api.md
original_filename: 2024-01-24_unleashing-the-power-of-css-injection-the-access-key-to-an-internal-api.md
title: 'Unleashing the power of CSS injection: The access key to an internal API'
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- api-security
language: en
raw_sha256: e531004576347b65c25be80c5d02ddbddcea15d44b62bb00b1b4a753b8259ca1
text_sha256: 62a9b26fb73c60f5af2cc0d5f2513c1c41875d8e45744c5c4a7141bc1e06941b
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Unleashing the power of CSS injection: The access key to an internal API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-24_unleashing-the-power-of-css-injection-the-access-key-to-an-internal-api.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `e531004576347b65c25be80c5d02ddbddcea15d44b62bb00b1b4a753b8259ca1`
- Text SHA256: `62a9b26fb73c60f5af2cc0d5f2513c1c41875d8e45744c5c4a7141bc1e06941b`


## Content

---
title: "Unleashing the power of CSS injection: The access key to an internal API"
url: "https://sanderwind.medium.com/unleashing-the-power-of-css-injection-the-access-key-to-an-internal-api-789b166d0527"
authors: ["Sander Wind (@SanderWind)"]
programs: ["Prince"]
bugs: ["CSS injection", "SSRF"]
publication_date: "2024-01-24"
added_date: "2024-01-03"
source: "pentester.land/writeups.json"
original_index: 501
scraped_via: "browseros"
---

# Unleashing the power of CSS injection: The access key to an internal API

Press enter or click to view image in full size
Photo by FIN on Unsplash
Unleashing the power of CSS injection: The access key to an internal API
Sander Wind
Follow
4 min read
·
Jan 25, 2023

283

2

In this write-up, we will be explaining a vulnerability that was discovered in an online accounting application. The vulnerability was a CSS injection flaw that could be exploited in the application’s PDF generator. We will explain to you how we discovered the vulnerability and how we were able to exploit it to get internal API access.

The first step was to identify entry points where we could inject malicious code. We focused on the application’s invoice generation feature, which allows users to create and download invoices in PDF format. We hoped for finding injection points within the PDF generation feature, allowing us to inject malicious payloads leading to code execution.

Useless CSS injection

We tried injecting our payloads in different user input fields for invoices which got included in the generated PDF. All these input fields did not lead to execution of our payloads. This led us to the global styling configuration for the invoice documents. Most of the configuration options had validation and sanitization in place, except for one configuration option: the color of the text being used in the documents.

<style>
  body {
  color: #7c878e; /* USER-SETTING */
  font-family: Arial, Helvetica, sans-serif; /* USER-SETTING */
  }

  .identity-text {
  color: #f3f3f3;}Hi there! I am some new css but I can not escape the style tag to become xss : (
  ; /* USER-SETTING */
</style>

As the application allowed us to preview the styling options being configured, we quickly found out that the injection point wasn’t as exciting as we hoped for. The characters <>'" were escaped making it impossible to close the <style> tag and inject our own HTML (e.g. <script> or <iframe>). At first we thought this was a dead end, but something interesting caught our attention. The CSS injection got rendered by the PDF generator. Fiddling a bit with the CSS, we found that SSRF was possible by using the url() directive without encapsulating the URL in quotes

[c6029550qf512863dfOgcgynjfayyyyyn] Received DNS interaction (AAAA) from xx.xxx.xx.xx at 2021-11-01 17:32:35
[c6029550qf512863dfOgcgynjfayyyyyn] Received DNS interaction (A) from xx.xxx.xx.xxx at 2021-11-01 17:32:35
[c6029550qf512863dfOgcgynjfayyyyyn] Received HTTP interaction from xx.xxx.xx.xxx at 2021-11-01 17:32:35

But again, excitement was short-lived as we were not able to extract any interesting data. Images did not render as they were not valid images and timing attacks by polling for alive internal IPs and hosts were not possible due the PDF generation time not being consistent enough.

At this point we started looking into the PDF generation software. When viewing the metadata of the generated PDFs, we found that Prince 13.2 was being used.

Documentation boring?

PrinceXML’s documentation is very extensive, so we ran a local copy to start testing the possibilities. The things we looked at were custom HTML-tags and custom CSS directives, which looked promising to abuse. Unfortunately, nothing seemed to work as we were limited by the escaped characters in the CSS injection point.

Get Sander Wind’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When we tested the prince-pdf-script property, we thought it didn’t work at first.

This property can be used to include JavaScript code that will be executed when the PDF file is opened. A common use case is to activate the “Print” dialog automatically. The script can be located in an external JavaScript file, referenced with the url() function.

@prince-pdf {
  prince-pdf-script: "this.print();"
}

Nothing happened. No print box popped up. No custom code got executed during the generation of the PDF. Nothing. But then it hit!

The script can be located in an external JavaScript file, referenced with the url() function.

We tried to include a local file with the url() function.

@prince-pdf { 
  prince-pdf-script: url(/etc/hostname);
}

When looking at the source of the generated PDF, we noticed that the content of the given file was included as JavaScript. The content was encoded in HEX UTF16.

4 0 obj
<</S /JavaScript
/JS <FEFF003000330066003800320037006500610065006100350063000A>>>
endobj

Decoding the UTF16 string, showed us the hostname of the generator service: 03f827eaea5c. Retrieving other files e.g. /etc/passwd, worked perfectly fine. Apparently, PrinceXML does not validate the content type of the included file and includes the content as is.

The final destination

As the generation process of one PDF document took six separate requests, we created a script to automate the process. This made it possible to run wordlists against the PDF generator and extracting the included “JavaScript” in one run.

Unfortunately, a list with common UNIX files did not expose a lot of interesting stuff. We did move on and started looking at requesting internal hosts. Using securitytrails.com we got us an accurate list of subdomains being available to enumerate.

After enumerating a few domains, we found out we had access to:

A NuGet gallery, exposing other applications available to downloading
An Elastic Search instance, which allowed us to query all public and internal network requests
The internal API, making it possible to query all available data of other customers

Being able to access the above listed hosts, the company decided that this was enough to assess the severity as a critical vulnerability.

PrinceXML decided to change the functionality of the prince-pdf-script property in version 15.

We hope you found this write-up entertaining, informative and interesting to read. Thank you for your attention.

Don’t forget to share your thoughts, feedback or even your own endeavours with CSS injections!

— The Vismagicians 🪄 (bandjes, floerer, holme and iQimpz)

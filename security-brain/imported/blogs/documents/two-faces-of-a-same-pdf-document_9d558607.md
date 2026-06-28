---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-01_two-faces-of-a-same-pdf-document.md
original_filename: 2022-07-01_two-faces-of-a-same-pdf-document.md
title: Two faces of a same PDF document
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 9d558607722e51e7818592fd96b2c9763adcd5af1f69a20200da516c70bd5dc2
text_sha256: 254c48c19a9a0614a9e9534e23b07bfcdb7ada0e1835cde0d8188c687a093e6e
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Two faces of a same PDF document

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-01_two-faces-of-a-same-pdf-document.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `9d558607722e51e7818592fd96b2c9763adcd5af1f69a20200da516c70bd5dc2`
- Text SHA256: `254c48c19a9a0614a9e9534e23b07bfcdb7ada0e1835cde0d8188c687a093e6e`


## Content

---
title: "Two faces of a same PDF document"
page_title: "Two Faces of a Same PDF Document. In this article, we introduce a parser… | by Toni Huttunen | Fraktal"
url: "https://blog.fraktal.fi/two-faces-of-the-same-pdf-document-17e7a15522a0"
authors: ["Toni Huttunen"]
programs: ["Mozilla", "Google", "Adobe"]
bugs: ["PDF parser differential attack"]
publication_date: "2022-07-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2494
scraped_via: "browseros"
---

# Two faces of a same PDF document

Two Faces of a Same PDF Document
Toni Huttunen
Follow
6 min read
·
Jul 1, 2022

14

In this article, we introduce a parser differential attack targeting PDF readers. The attack makes it possible to create a malicious PDF document which presents different content based on the reader application used.

Press enter or click to view image in full size
Introduction

In the digital world, we have been taught to stay vigilant. We can spot fishy emails and know not to believe things that seem too good to be true. But there are some digital assets that we have grown to trust. Amongst those is the trusty PDF format. When you receive a PDF file, you tend to think that the content that you see is the same to everyone who opens the file.

Could a PDF file be manipulated in a way that the same file would display different content when using different viewer apps? We found out that it could — by design!

Consider the following exchange:

Press enter or click to view image in full size

In this example, the stakeholders have different understandings about the content of the PDF. Let’s see how that might happen.

Background of PDF format

Portable Document Format (PDF) is a popular file format for presenting legal documents and agreements between parties. The presentation of PDF files is meant to be independent of the used PDF viewer software, web browser, operating system, or existing font-files on the device; they should render identically even through various printer devices. PDF readers attempt to present documents as well as they can and use as many supported and requested sophisticated PDF ISO standards and proprietary features as possible.

The presentation of PDF files is meant to be independent of the used PDF viewer software, web browser, operating system, or existing font-files on the device.

The original PDF file format is dated and limited, and more formats and ISO standards have been made to fill the gaps. Of these, particularly interesting in this case is Adobe’s PDF 1.7 (ISO 32000–1), which introduces Adobe’s Interactive Forms, including JavaScript extensions, AcroForms and Adobe XML Forms Architecture (XFA). Many PDF readers do not render content that is not standardized or contain non-essential sophisticated features.

PDF readers are not identical and do not support the same set of proprietary or other, more sophisticated PDF features. In this write-up, we focus on the Mozilla PDF.js solution, but the overall issue is more general.

Finding a weakness

Mozilla PDF.js is a popular Portable Document Format (PDF) library used in Mozilla Firefox for presenting PDF documents. On 2 October 2021, Mozilla activated PDF XFA form support by default.

The PDF XML Forms Architecture (XFA) specification contains customizable fallback pages for non-XFA readers and the PDF readers can choose which pages they present. PDF readers also do not warn the user that the presented content contains features that might not be rendered identically everywhere.

Press enter or click to view image in full size
https://www.pdfa.org/norm-refs/XFA-3_3.pdf

In practice, PDF.js renders fillable XFA form pages that most other readers do not support — these other readers present a fallback PDF page included as part of the document.

Press enter or click to view image in full size
This fallback page is included into most of the XFA documents.

The fallback page content stored inside the document is fully customizable.

Press enter or click to view image in full size
The fallback page content stored inside the document is fully customizable.

This means that XFA PDF readers and non-XFA-compliant readers can present completely different content out of the same base document file. None of the readers alert that the document contains unsupported features, or that some rare PDF features are being used that most readers won’t be able to render properly.

Contrary to user expectation, XFA PDF readers and non-XFA-compliant readers can by design present completely different content out of the same base document file.

Adobe Acrobat Reader, Mozilla Firefox and products using PDF.js core renders the XFA content. Most other readers are non-XFA-compliant readers, including Safari, Chromium, Edge and iOS Firefox. Situation is more mixed in practice. Acrobat Reader might integrate into browser, or web sites might use own embedded PDF reader (PDF.js) and bypasses the browser’s own reader.

Impact from a security perspective

This design feature could be used by an attacker to conduct fraud against business processes, where integrity of PDF documents are inherently trusted by people involved in review and acceptance roles.

Get Toni Huttunen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As an example, an attacker could try to inject mutually exclusive pages into document, and hope the various openers are using different readers and see the different context. An invoice document could attempt to present a contract which will present different payable amounts and account numbers to an approving supervisor and accounts payable; in this scenario the approval is made by the supervisor for a lower sum, while accounting executes a payment with a larger sum.

Parser differential issues happen when multiple PDF parsers are used for processing a single document. PDF.js enables embedding a PDF viewer in an HTML page making many popular sites affected regardless of the web browser. Websites might present a PDF file through PDF.js preview, but the download and opening the file locally leads to an alternative content.

Content previewed and downloaded using Firefox might be later opened using a local PDF viewer or printed on paper. Corporate printers might accept PDF files directly, via web interfaces or through the USB stick. Also, a system default PDF viewer might change over time, changing the visible content.

On a more general note, this manipulation/attack technique demonstrates that even the digital content which trustworthiness we take for granted, can be manipulated.

Proof of concept

As proof of concept, we crafted a malicious PDF called “Purchase order”.

This PDF file shows a different purchase order depending on the used PDF reader (1337 € for XFA readers, and 1000 € for others). The content manipulation was possible simply by modifying the fallback PDF page text area of “The document you are trying to load…”.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Remediation advice

There is currently no fix available for the issue. In the following, we provide suggestions for the stakeholders to consider.

For companies

Being knowledgeable about that PDFs might not present the same content for all users might provide input for assessing risks related to agreement and purchase payment processes.

For services handling PDFs

Services handling arbitrary PDF files should define a list of supported PDF file format extensions and ensure that the files being accepted are in-line with the requirements. Avoid supporting file formats that cannot guarantee the same content will be visible to all users. Files could also be converted to a simpler format where the same potentially lossy converter handles those special cases and strips them out similarly.

For PDF reader apps

Feature rich PDF readers should provide a compatibility view of the document, rendering the document like a basic PDF reader would do. The fallback page could be presented as a compatibility page of the document. This would be simple, effective and easy to understand for the end users.

Basic PDF readers should alert in a situation where the document contains an unsupported feature, and the potential consequences of the suffered document portability situation causes. If all pages can’t be rendered, the reader should alert about the issue.

Timeline

2022–03–25 Reported issue to Mozilla PDF.js
2022–04–04 Mozilla confirmed the issue
2022–06–16 Mozilla closed the issue and decided not to fix
2022–06–22 Reported the issue to Chromium
2022–06–22 Chromium marked the issue as a duplicate with a previously reported bug without a security concern
2022–06–22 Reported issue to Adobe
2022–06–27 Adobe reported issue to be a product bug instead of a security issue
2022–07–01 This article published.

Links

https://bugzilla.mozilla.org/show_bug.cgi?id=1761472
https://bugs.chromium.org/p/chromium/issues/detail?id=1338561
https://bugs.chromium.org/p/chromium/issues/detail?id=1048930 https://hackerone.com/reports/1609243

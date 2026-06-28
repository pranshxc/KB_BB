---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-19_out-of-band-xxe-in-an-e-commerce-ios-app.md
original_filename: 2020-11-19_out-of-band-xxe-in-an-e-commerce-ios-app.md
title: Out of Band XXE in an E-commerce IOS app
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 0faee60630b82682fc320838c749bcc9dc80debc6fe013da319c88e60c6b7262
text_sha256: f87f8337e3e19d266d9cd055ddd4fdee65970f1bcea9baa449d9b2ddf7cc916f
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Out of Band XXE in an E-commerce IOS app

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-19_out-of-band-xxe-in-an-e-commerce-ios-app.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `0faee60630b82682fc320838c749bcc9dc80debc6fe013da319c88e60c6b7262`
- Text SHA256: `f87f8337e3e19d266d9cd055ddd4fdee65970f1bcea9baa449d9b2ddf7cc916f`


## Content

---
title: "Out of Band XXE in an E-commerce IOS app"
url: "https://0xgaurang.medium.com/out-of-band-xxe-in-an-e-commerce-ios-app-e22981f7b59b"
authors: ["Gaurang Bhatnagar (@0xgaurang)"]
bugs: ["XXE"]
publication_date: "2020-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4119
scraped_via: "browseros"
---

# Out of Band XXE in an E-commerce IOS app

Out of Band XXE in an E-commerce IOS app
Gaurang Bhatnagar
Follow
3 min read
·
Nov 19, 2020

135

Press enter or click to view image in full size

While testing IOS app of the target application, I had found XXE vulnerability for which I’m going to share the writeup. Wanted to publish this since long time, but was only waiting for the disclosure. Anyways, since I did not received permission to reveal the name of the target, I’m going to redact their name in the screenshots.

The target is a big giant in E-commerce industry and their app has more that 50 million downloads as of today.

The vulnerability detection was easy due to the XML parsing error displayed to the end user. The parsing functionality did not had XML External Entity Declaration disabled which allowed an attacker to read files from the server.

About XXE

An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

Vulnerability Identification

The first identification that the host might be processing XML was made when I flipped the content type to XML on a JSON endpoint.

Get Gaurang Bhatnagar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By sending a generic XML payload, the target returned XML parsing error which confirmed the suspicion that the application was processing XML input.

Press enter or click to view image in full size
External Service Interaction

To check whether it was possible to make requests to external sites, I started a listener on the remote server and used XML payload to send a request to that server.

As shown in the following screenshot, the connection was received from the target IP address. Also, the user-agent indicated that the back-end server is processing Java.

Press enter or click to view image in full size
Out-of-Band Data Retrieval

The next thing to do was to exfiltrate data from the remote host.

I used XXEserve in this case which runs a web server, creates a DTD file and prints out the logs. XXEServe is a tiny Sinatra app that runs a server which is useful in collecting data sent out of band.

The following image shows it was possible to retrieve files from the target host (/etc/resolv.conf in the following case) via HTTP using XXEServe.

Press enter or click to view image in full size

To harden a JSON endpoint, XML parsing should be disabled altogether and/or inline DOCTYPE declarations should be disabled to prevent XML external entity injections.

The vulnerability was reported and fixed in few hours by the team.

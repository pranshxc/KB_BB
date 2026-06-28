---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-03_automating-sql-injection-on-encrypted-request.md
original_filename: 2023-05-03_automating-sql-injection-on-encrypted-request.md
title: Automating SQL Injection On Encrypted Request
category: documents
detected_topics:
- sqli
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: ad017d910336b2304e8e0445e3c5920f5d35a385de5ecae063abd0efa9820068
text_sha256: 24a330ff7b132cbb1a05b940a256292165c6919d74f5e0bcaec998f9e39e38ef
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Automating SQL Injection On Encrypted Request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-03_automating-sql-injection-on-encrypted-request.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ad017d910336b2304e8e0445e3c5920f5d35a385de5ecae063abd0efa9820068`
- Text SHA256: `24a330ff7b132cbb1a05b940a256292165c6919d74f5e0bcaec998f9e39e38ef`


## Content

---
title: "Automating SQL Injection On Encrypted Request"
url: "https://medium.com/@janirudransh/automating-sql-injection-on-encrypted-request-21a43aa2e7ef"
authors: ["Janirudransh"]
bugs: ["SQL injection", "Client-side encryption bypass"]
publication_date: "2023-05-03"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1195
scraped_via: "browseros"
---

# Automating SQL Injection On Encrypted Request

Automating SQL Injection On Encrypted Request
Janirudransh
Follow
6 min read
·
May 3, 2023

14

Hi, Guys hope you all are doing well. I’m back with an adventure of exploiting an SQL Injection on an encrypted request and response.

Introduction

SQL injection is a type of cyber attack where malicious code is inserted into a SQL (Structured Query Language) statement through an input field on a website or application.

Target Application

The application was a portal for suppliers and vendors, which had various functionalities related to each role. One of the features was to fetch tickets raised by the users regarding an issue.

Identification

As the tickets were fetched by the feature, there were more than 10,000 tickets. To improve the understanding of the functionality, we narrowed down the results using filters.

During the SQL injection identification process, we attempted to inject a single quote (‘), but we received no response from the application. Then, we tried to balance the query using a comment (‘ — ), and this technique worked, allowing us to proceed with the SQL injection.

Challenge

Upon further inspection of the request, we discovered that the request body is encrypted, as well as the response. This encryption adds an additional layer of complexity to our SQL injection exploit, as we would need to consider the encryption and decryption process in our attack strategy.

Press enter or click to view image in full size
Observe the encrypted request

Note: Ignore itest= as of now

Now as encryption is done on client side, there has to be a key and algorithm for encryption/decryption some where is the website.

Upon analyzing the javascript main.js, I found the key for example

x=atob(“<base64 encoded>”)

Upon further analysis of the JavaScript code, we were able to determine that the application was using AES 128 encryption with ECB (Electronic Codebook) mode. This information provides insight into the encryption algorithm being used, which will be crucial for developing a strategy to work with the encrypted request and response in our SQL injection exploit.

Using this online tool. I was able to encrypt and decrypt request — response.

Decryption of cipher

As the output is base64 encoded, I used burp’s decoder to make it readable.

Press enter or click to view image in full size
Base64 to plain text

Using the above method I was able to exploit the SQL injection manually by repeating the encryption and decryption process. However, the main challenge we encountered was the presence of a boolean-based SQL injection vulnerability, which made manual exploitation nearly impossible.

Automated Exploitation

Initially, one might consider using SQLmap directly to exploit the SQL injection vulnerability. However, in this case, using SQLmap directly wouldn’t be feasible due to the encrypted request. Since the backend would attempt to decrypt the request body, straight forward SQLmap wouldn’t be effective in this scenario.

After an extensive search on the internet, I couldn’t find any existing tools or scripts to exploit SQL injection on encrypted requests. Consequently, I made the decision to develop my own solution from scratch.

I wanted to make mechanism just for encryption and decryption. Supply the plain text to SQLmap. Further SQLmap will do things.

By leveraging the tamper script feature of SQLmap, I developed a Python-based script. My goal was to circumvent the encryption and decryption process altogether. Instead, I used an already decrypted request and utilized SQLmap to dynamically craft the encrypted request with the desired payload. This approach allowed me to interact with the application while bypassing the need for manual encryption and decryption steps.

Press enter or click to view image in full size

You can the find the format of writing of a tamper script from here.

Get Janirudransh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

SQLmap will call tamper function so we need to write the main logic under tamper function. Using already available code for encryption-decryption.

A) Key : Enter the encryption key.

B) payload: The payload is the input provided by SQLmap (e.g. xyz' AND 'a'='a). In our case, the payload will be in the form of the encrypted request appended with the SQL injection payload (e.g., <encrypted-request>' AND 'a'='a). To ensure the modified request appears legitimate, we need to remove the encrypted text, leaving only the payload (e.g. ' AND 'a'='a). To achieve this, we utilized the replace function within our tamper script.

C) retVal: The retVal represents the decrypted request. Since we are going to craft the encrypted request, we need to replace the original value with the malicious payload. After the replace process, the request would appear as follows (e.g.{"roleName":"Editor' AND 'a'='a"}). This modified request includes the injected SQL payload, allowing us to test for vulnerabilities in the application.

D) .encode(“utf8) : To comply with the requirements of the crypto library, it is necessary to convert the string into bytes since the library does not accept strings as input.

E) raw: It is used to add padding to the plaintext.

F) cipher: It creates an object for encryption

G) cipher.encrypt(“plaintext”):It encrypts the plaintext with the defined algorithm.

H) .b64encode: It convert the encrypted text to base64. It is how the algorithm works so need to convert it.

I) .decode(): It converts the byte to string as byte is not accepted by SQLmap.

This how the tamper script works.

Acceptable Format By SQLmap

In order to make SQLmap work effectively, we need to ensure that the request is in a format that it understands, which typically involves key-value pairs (e.g. file=test.txt). In our case, since the request is encrypted, we explicitly added a parameter to the request, specifically itest=<encrypted-request>. This parameter allows SQLmap to recognize and process the encrypted request correctly, enabling us to perform the necessary SQL injection tests.

Press enter or click to view image in full size
Added itest=

After realizing that the format with the added itest=<encrypted-request> parameter was not accepted by the server, I consulted with our colleagues and came up with a solution. We decided to utilize Burp Suite as a middleware to intercept and modify the request. Using Burp Suite's "Match & Replace" feature, we created a rule to remove the itest= parameter from the request before it reaches the server. This rule ensures that the modified request no longer contains the unwanted parameter, allowing it to be processed correctly by the server.

Remove itest= from request

Great! The mechanism is fully operational now. However, it’s important to note that since there is no decryption function included in the script, it can only be used for Boolean-based and Time-based SQL injection scenarios.

Middleware Challenge

Due to the presence of middleware for encryption and decryption, the time-based attack method caused the database to sleep, but SQLmap couldn’t definitively determine if the payload was executed. Boolean-based attacks were not viable either since the response length varied due to our injected payload being included in the response.

Although the exploitation attempt was hindered by the middleware, it was still an enjoyable experience.

Summary

Request Response Encrypted with AES 128 ECB.
Find encryption key from website
Manually exploit it.
Automated script to avoid manual encryption decryption process.
Make SQLmap friendly request.
Using burp as our middle ware, make server friendly request and send it.

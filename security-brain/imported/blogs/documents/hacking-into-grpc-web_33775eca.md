---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_hacking-into-grpc-web_2.md
original_filename: 2023-09-18_hacking-into-grpc-web_2.md
title: Hacking into gRPC-Web
category: documents
detected_topics:
- sqli
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- sqli
- xss
- command-injection
- supply-chain
language: en
raw_sha256: 33775ecaa7c559e7c764f76dec9c4be7e2ad3127acc03ab5b3dc2cbdacc99a18
text_sha256: 1e0b6aa3927d4b48859d303c22f6b3a40f4c0158fb77d1ef8e95f08877244731
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking into gRPC-Web

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_hacking-into-grpc-web_2.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `33775ecaa7c559e7c764f76dec9c4be7e2ad3127acc03ab5b3dc2cbdacc99a18`
- Text SHA256: `1e0b6aa3927d4b48859d303c22f6b3a40f4c0158fb77d1ef8e95f08877244731`


## Content

---
title: "Hacking into gRPC-Web"
url: "https://infosecwriteups.com/hacking-into-grpc-web-a54053757a45"
authors: ["Amin Nasiri (@0xnxenon)"]
bugs: ["gRPC", "SQL injection"]
publication_date: "2023-09-18"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 764
scraped_via: "browseros"
---

# Hacking into gRPC-Web

Hacking into gRPC-Web
Manipulating gRPC Web Payloads and Finding Hidden Services
Amin Nasiri
Follow
7 min read
·
Sep 18, 2023

114

How Did It Start?

It started when I faced a web application using gRPC-Web and I could not manipulate the requests in Burp Suite. I searched a lot and there was no good or complete resource for pentesting gRPC-Web, then the research began and I could make a tool and a Burp Suite Extension for manipulating payloads. I also found a hidden gRPC-Web parameter SQLi vulnerability in a travel agency company and submitted the report to them. The vulnerability that I found was so low-hanging fruit but maybe other hunters would miss it because there was no comprehensive article about how to manipulate gRPC-Web payloads. I will also release a YouTube video for presenting gRPC-Web Pentesting.

If you are new to gRPC-Web read my other article that describes the basics of this design. What are gRPC & gRPC-Web?

What Was The Problem? Manipulating The Payloads!

Here is one example payload after base64 decoding it:

Press enter or click to view image in full size
Hex Output of the Payload

In Burp Suite:

Press enter or click to view image in full size
Base64 Decoded Payload in Burp Suite

It is clear that you cannot easily manipulate binary data in the payload and just encode it to base64 again because it uses Protocol Buffers and it uses kind of serialization and when you want to make changes in the payloads that have multiple parameters, it is kind of impossible to do it manually like editing JSON.

Here is another payload from a real target:

Press enter or click to view image in full size
Payload from a real target

There are some tools to send gRPC or gRPC-Web Requests but there is a problem! You need the .proto file! If you are doing a black-box test, naturally you do not have the .proto file and the only thing you have is the payload and the Webpacked JavaScript files which the browser uses for sending gRPC-Web Requests. In the end, I will show a little about white-box testing with .proto files.

Explain The Base64 Decoded Payload

After decoding the base64 encoding payload, and piping the output to xxd command, we can see hex data. The 5 first bytes of the payload is the entire message length in hex, in this example is (16¹ * 1 + 16⁰ * 6 = 22) which means the entire payload is 22 bytes long.

Press enter or click to view image in full size
Hex Output of the Payload

after removing the length prefix we can pipe the payload to Protoscope tool and it outputs a human-readable version of the payload which is editable and is like JSON format but not exactly JSON. The message fields are separated with field numbers and not field names because protocol buffers work with field numbers and field names are specified in the .proto file and stub files.

Now Let’s Hack The gRPC-Web Easier…
gRPC Pentest Suite

gRPC Pentest Suite has 2 tools + 1 Burp Suite extension for hacking gRPC-Web:

1. gRPC Coder

This tool helps manipulate the payloads, removes the length prefix, and is useful also for examining responses from the server or doing response manipulation. you also need to have the Protoscope tool installed to make the gRPC Pentest Suite Complete and Available.

The gRPC Coder Burp Extension

This extension helps use gRPC Coder tool faster and with just one click for decoding and encoding payloads. The available Content-Type:

application/grpc-web-text
application/grpc-web+proto
2. gRPC Scan

This tool scans JavaScript Webpacked gRPC-Web related files and outputs gRPC endpoints, services, methods, messages, fields, and field types. It helps a lot to find hidden parameters or hidden endpoints and also in some situations you can make .proto file with the output of this tool.

gRPC Coder Usage

First, you have to pass the payload to the standard input of the gRPC Coder with — decode flag. Then pass the output of the tool to Protoscope and save the output to a file for editing.

echo "AAAAABYSC0FtaW4gTmFzaXJpGDY6BVhlbm9u" | python3 grpc-coder.py --decode | protoscope > out.txt
cat out.txt
2: {"Amin Nasiri"}
3: 54
7: {"Xenon"}

Edit the out.txt file:

cat out.txt
2: {"Amin Nasiri Xenon GRPC"}
3: 54
7: {"<script>alert(origin)</script>"}

Then use Protoscope and pass its output to the gRPC Coder tool with — encode flag:

protoscope -s out.txt | python3 grpc-coder.py --encode

After that, we can send the payload with Burp Suite:

AAAAADoSFkFtaW4gTmFzaXJpIFhlbm9uIEdSUEMYNjoePHNjcmlwdD5hbGVydChvcmlnaW4pPC9zY3JpcHQ+

I am sure you found out that this is a time-consuming process and for manipulating every request, you have to spend tons of minutes to do that. That’s why I made the extension.

gRPC Coder Burp Suite Extension Usage:

I have made a video for using this extension, in the video I exploit a lab sample that has client side XSS protection:

gRPC Coder Burp Suite Extension Usage

You can easily encode and decode payloads with the extension. See the gRPC Pentest Suite to install the extension in Burp.

gRPC Scan Usage:

When you are working with a web application that is using gRPC-Web, maybe you see a main.js or somethingRandom.js file that has gRPC-Web related files inside itself.

Note: For finding the correct JS file which has gRPC-Web data, you can search one gRPC-Web route in all Burp Responses for example search this:
hidden.sqli.Searcher like this:

Press enter or click to view image in full size
Logger++ Filter for Finding gRPC-Web JavaScript File

After finding the right JS file, download the file and scan it with gRPC Scan.

Get Amin Nasiri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The example for Hidden-SQLi gRPC lab after web packing client.js file is this:

Press enter or click to view image in full size
gRPC-Web Webpacked JavaScript File

It is a minified JavaScript file that has good information about the gRPC back-end endpoints and services. The gRPC Scan tool makes analyzing this file much easier:

python3 grpc-scan.py --file main.js

The output:

Press enter or click to view image in full size
gRPC Scan Tool Output

In the output, we can see 2 endpoints in which we can send requests to them.

There are also 3 messages, each of them has some fields, and each field has a field number and field type. Pay attention that field names in gRPC Scan output are not important when we are manipulating payloads, because Protobuf works with field numbers. fields names are just small clues that help us know a bit about parameter and their usage.

Pay attention that sometimes the application does not use all endpoints or all message fields and maybe they are optional. You have to fuzz them to find possible vulnerabilities.

At first, I decode the payload:

gRPC Scan Decoding Process

The result is this:

Decoded Payload

Then change the route and put the SQLi payload inside it:

Edit the payload and add SQLi payload inside it

After making all changes to the payload, I encode it and send it to the server:

gRPC Coder Extension Payload Encoding Process
Sending New Encoded Payload

When I decode the response with gRPC Coder Extension, we see that there are no published posts, and /Search2 route was not protected against SQLi vulnerability and we see the flag :)

Press enter or click to view image in full size
Decoding the Response

The complete video of exploiting hidden SQLi and XSS is here:

Hacking into gRPC-Web YouTube video
Test with .proto File

If you have .proto file you can use grpcui tool but you have to make .protoset file and then use it for sending gRPC-Web requests:

protoc --proto_path=. --descriptor_set_out=NAME.protoset --include_imports ./NAME.proto

Then run the grpcui:

grpcui -protoset NAME.protoset -plaintext localhost:8080

Open the grpcui generated URL and send your desired requests:

Press enter or click to view image in full size
grpcui Command
Press enter or click to view image in full size
grpcui
About Me

I’m Mohammad Amin Nasiri (Xenon), a web application penetration tester with 2+ years of hands-on security assessment and auditing experience, trying to expand my hacking skills with my programming knowledge. Find me on Github, LinkedIn, and Twitter.

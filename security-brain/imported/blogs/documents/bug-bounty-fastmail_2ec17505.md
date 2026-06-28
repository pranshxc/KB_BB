---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-08_bug-bounty-fastmail.md
original_filename: 2017-12-08_bug-bounty-fastmail.md
title: 'Bug Bounty: Fastmail'
category: documents
detected_topics:
- command-injection
- ssrf
tags:
- imported
- documents
- command-injection
- ssrf
language: en
raw_sha256: 2ec17505228572a7143da118e4d5c0647f391aef796627490632043f2f5597a3
text_sha256: e842be64a4540885f56bc47e14fb9c89b9a4a23e3cdecb66e0ecee5f80cea3a9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty: Fastmail

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-08_bug-bounty-fastmail.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `2ec17505228572a7143da118e4d5c0647f391aef796627490632043f2f5597a3`
- Text SHA256: `e842be64a4540885f56bc47e14fb9c89b9a4a23e3cdecb66e0ecee5f80cea3a9`


## Content

---
title: "Bug Bounty: Fastmail"
url: "https://medium.com/bugbountywriteup/bug-bounty-fastmail-feeda67905f5"
authors: ["Brian Hyde (@0xHyde)"]
programs: ["Fastmail"]
bugs: ["Blind SSRF", "Blind XXE"]
bounty: "3,000"
publication_date: "2017-12-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6033
scraped_via: "browseros"
---

# Bug Bounty: Fastmail

Bug Bounty: Fastmail
hyde
Follow
3 min read
·
Dec 8, 2017

369

1

I would first like to start off by saying that Fastmail has a great bug bounty program and they really care a lot about the security of their services and customers. I first started looking into their bug bounty program a few months back and not long after browsing through the web application I came across the following feature:

Press enter or click to view image in full size

I discovered that using this feature I could make HTTP requests to any website using any port, including internal IP addresses. If you made a request to a server that did not contain a valid iCal file it would return an error with partial contents of the response body, which easily made it apparent that this was a valid security concern. The second thing I noticed is that if you included \r\n in the URL path you could add custom headers, so in theory this could have been used as a way to protocol smuggle. Unfortunately I was not able to find any internal services that I could use to leverage this to remote code execution. However, while looking through the source of their website I was able to find a reference to an internal IP address which was running a webserver and I was able to pull partial contents of their internal web application.

Press enter or click to view image in full size

I reported this vulnerability to their security team and was rewarded $1,000 for my find.

Get hyde’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The second vulnerability I found was a blind SSRF + blind XXE. I found this vulnerability by including the hostname of my Amazon EC2 instance which was running a webserver in an area of the website that requested an E-Mail address.

Press enter or click to view image in full size

After seeing HTTP requests made to my VPS’s webserver that were coming from Fastmail, I immediately knew I found a blind SSRF vulnerability as the response did not contain any contents of the file being requested. However, I wasn’t able to specify the port number or a custom filepath, but I quickly discovered that this SSRF followed redirects specified in the Location header. I first tried to use gopher:// to craft custom requests in an attempt to craft custom requests to internal services in an attempt to interact with protocols other than HTTP and HTTPS, unfortunately that was unsuccessful as the only requests that were successful were redirects to HTTP or HTTPS. Shortly after I looked back at the access logs on my VPS and I noticed that the initial request was requesting an XML file. I next placed an blind XXE payload at the exact file path being requested by their servers which turned out to be successful.

Press enter or click to view image in full size

The first request is the file the server initially requested. The XXE payload I used then tried to request success.txt, however since that file did not exist my webserver redirected to the root directory. In the root directory was a php file that redirected to /example-test-redirect.txt using the Location header. I then reported this vulnerability to Fastmail and received a $2,000 reward for my find.

In my experience with Fastmail’s bug bounty program, I have found that their security team is always quick to respond and they have always rolled out a patch within 24 hours of my report. I highly suggest this program to any security researchers. In addition to the bounties paid, I was also added to their Hall of Fame.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-01_the-powerful-http-request-smuggling-.md
original_filename: 2020-10-01_the-powerful-http-request-smuggling-.md
title: The Powerful HTTP Request Smuggling 💪
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 153834b55bb63f07cf514fd6fbadc9f77153c3476b41cd94db57db5887e8cb98
text_sha256: dd56f66b624791008d78eeea3e5d5b2c44474b206eaee2542f634c06f6c05cec
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# The Powerful HTTP Request Smuggling 💪

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-01_the-powerful-http-request-smuggling-.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `153834b55bb63f07cf514fd6fbadc9f77153c3476b41cd94db57db5887e8cb98`
- Text SHA256: `dd56f66b624791008d78eeea3e5d5b2c44474b206eaee2542f634c06f6c05cec`


## Content

---
title: "The Powerful HTTP Request Smuggling 💪"
url: "https://medium.com/@ricardoiramar/the-powerful-http-request-smuggling-af208fafa142"
authors: ["Ricardo Iramar dos Santos (@ricardo_iramar)"]
bugs: ["HTTP request smuggling"]
bounty: "17,050"
publication_date: "2020-10-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4225
scraped_via: "browseros"
---

# The Powerful HTTP Request Smuggling 💪

Ricardo Iramar dos Santos
 highlighted

The Powerful HTTP Request Smuggling 💪
Ricardo Iramar dos Santos
Follow
13 min read
·
Oct 2, 2020

893

3

TL;DR: This is how I was able to exploit a HTTP Request Smuggling in some Mobile Device Management (MDM) servers and send any MDM command to any device enrolled on them for a private bug bounty program.

Press enter or click to view image in full size
I am inevitable.
What is HTTP Request Smuggling? 📖

If you already know what is HTTP Request Smuggling you can skip this section but if you want to know the basics I’d recommend read carefully.

In this section I’ll try to put everyone under the same page covering only the basics about HTTP Request Smuggling. If you want to learn in details I recommend you read this documentation https://portswigger.net/web-security/request-smuggling, read all the references and do all the labs.

In August 2019 when James Kettle brought HTTP Request Smuggling back from the ashes I tried to understand this vulnerability and at that time it was difficult to me understand everything.

Now after exploiting a few instances I see the problem to understand at the first glance. Most of the time we are looking for a vulnerability on the application and HTTP Request Smuggling also involves another layer called network.

The images from now one in this section are from this YouTube video “$6,5k + $5k HTTP Request Smuggling mass account takeover — Slack + Zomato”. Thanks Grzegorz Niedziela for allowing me to use the images! I strong recommend you to watch this video after reading this post.

Before talking about HTTP Request Smuggling itself lets recap some features from HTTP protocol version 1.1. A HTTP server can process multiple requests under the same TCP connection as you can see in the example below.

The header Content-Length defines the size of the body which tells to the server where the body finishes. There is another header called Transfer-Encoding which also defines the size of the body.

Press enter or click to view image in full size

The Transfer-Encoding header indicates the body will be sent in chunks and the numbers in the beginning of each chunk indicates the size of it in a hexadecimal format. The last chunk should be indicate with number 0 which determines the end of the body.

The main difference between Content-Length and Transfer-Encoding is in the first case the request send the entire body at once and on Transfer-Encoding the body is sent in pieces.

But what happen when both headers are present?

Press enter or click to view image in full size

The RFC 2616 is clear on section 4.4 Message Length page 34 about it.

If a message is received with both a Transfer-Encoding header field and a Content-Length header field, the latter MUST be ignored.

RFC describes the beauty of the theory but this is not what happen in practice. When an environment do not respect the sentence above the HTTP Request Smuggling is possible.

Nowadays is pretty common to see web applications in the back-end and a reverse proxy in the front-end like the diagram below.

Press enter or click to view image in full size

What happen if Bob sends a request with Content-Length and Transfer-Encoding and front-end and back-end interprets these headers in a different order ignoring RFC 2616? Let’s assume Alice also sends a request right after Bob with only the Content-Length header.

Press enter or click to view image in full size

In the image above we can see Bob and Alice requests one next to another. The Bob’s request comes first and the front-end is using the Content-Length header (ignoring Transfer-Encoding) to defines the body length which means for the front-end Bob’s request ends right after the text key=value and Alice’s request starts at POST / HTTP/1.1.

In the other side back-end is using Transfer-Encoding header (ignoring Content-Length) and defining the end of Bob’s request at the number 0 and assuming the Alice’s requests starts with the text key=value which is an invalid request.

If Bob is a skilled attacker he can craft a malicious request and force Alice to receives a different response from what was supposed to be the original response from Alice’s request.

That’s the most important part of HTTP Request Smuggling. If you didn’t get what is happening here I strong recommend you go back and read everything again.

Reporting HTTP Request Smuggling 📝

I was scanning some subdomains using Smuggler in a private bug bounty program on Hackerone when I initially found 13 subdomains reported as potential vulnerable to HTTP Request Smuggling by Smuggler. I reported all of them in one single report as critical even without a real PoC because I was afraid to get a duplicate and decided to work on the impact later. I got that felling there was something big which would require time to investigate.

If you already ran Smuggler before you probably know most of the time Smuggler reports as potential vulnerable but you cannot really get any real impact directly. For each case a research is required to understand the context and test a malicious scenario to prove the impact.

The most common impact that I’ve seen it is what I called as Universal Redirect. Universal Redirect is when you can force any user to receive a malicious response which actually redirects the user to another domain.

As usual the Hackerone triager asked me for a PoC with a valid impact which is a fair enough request. From those 13 subdomains reported as potential vulnerable I was able to quickly found one vulnerable to Universal Redirect by just sending the request below.

The request above was pointed to one of the 13 subdomains. Since I cannot reveal anything regarding the company let’s say the requests was actually made to https://vulnerable.requestsmuggling.com. As you can see instead of using vulnerable.requestsmuggling.com on the Host headers I’ve changed to www.example.com in order to get a redirect in the response pointed to it.

By playing the attacker with the request above the luckiest next user making any request to https://vulnerable.requestsmuggling.com would receive the response below generated by my malicious request.

Press enter or click to view image in full size

Without knowing what is happening and totally transparent the next user would be magically redirected to https://www.example.com/getfile/. If I keep sending the same request described above I’d be able to redirect almost all the users to a domain that I control.

After been able to demonstrate the Universal Redirect above I also found other 4 subdomains (17 subdomains in total) identified as vulnerable by Smuggler and included them under the same report. At that time I didn’t look closely to these 4 new subdomains. The Hackerone triager accepted my report and downgrade the severity from critical (9.1) to high (7.5) which later on the company changed from high (7.5) to critical. 🤷‍♂️

As soon as my report was validated I asked permission to try other scenarios which could affect real users and got this answer below from the Hackerone triager.

I passed your report to the company team, please don't perform any activity that might affect live users before hearing back from the team.

HTTP Request Smuggling is really powerful and if you don’t what you doing you can impact all the users. I just continued with my investigation to see what else impact I could prove with all those instances.

The First Bounty 💰

After four days from the date that I opened the report someone from company commented in the report asking for more details how to reproduce for a specific subdomain and as much as possible to avoid test on production subdomains. By the subdomain names it was easy to identify which subdomains were production and which were not.

After providing all the details how to reproduce the Universal Redirect for one subdomain I was rewarded with a US$2,000 bounty. In order to elevate the bounty I checked all the subdomains and from those 17 subdomains I was able to demonstrate the Universal Redirect only for 7 subdomains.

I didn’t agree with the bounty because I knew it with those 7 vulnerable subdomains I could cause a big impact in their business by just redirecting all the users to a malicious domain. I complained through the comments and got the comment below from the company.

The bounty payment was based on the number of unique systems affected and the maximum perceived impact of the vulnerability (redirection).

That is fair enough, I decided to take a close look on the others 10 subdomains to see what I could get from them.

Trying Harder ⚔️

I tried for a few days to get some impact on those 10 subdomains but got nothing. I was trying harder because some of them subdomain names had api in the middle. If I could redirect the traffic from those APIs to another domain under my control maybe I could get some sensitive information.

Get Ricardo Iramar dos Santos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After trying everything I decided to go back to the other 7 subdomains to check if I was missing something and the subdomain mdm.qa-vulnerable.requestsmuggling.com took my attention.

A few months back I had some experience working with a Mobile Device Management (MDM) solution and I knew it a little bit about the MDM protocol so I decided to investigate more in details the subdomain mdm.qa-vulnerable.requestsmuggling.com. I was really comfortable to work on this subdomain since the name was clear saying this is a QA environment.

First step was redirect a random request to Burp Collaborator to see if I could get a request from a random user and analyze it. I’ve created my payload, sent the request below and waited.

After a few seconds I was able to see the request below in my Burp Collaborator.

Press enter or click to view image in full size

By the request headers “Content-Type: application/x-apple-aspen-mdm”, “Mdm-Signature: …” and “User-Agent: MDM/1.0” we can assume this request came from a MDM client. A quick google search returned the Mobile Device Management Protocol Reference document as the first hit.

Press enter or click to view image in full size

After the enrollment the devices start to listen for a push notification from the server. To cause the device to poll the MDM server for commands, the MDM server sends a notification through the APNS gateway to the device. The message sent with the push notification is JSON-formatted and must contain the PushMagic string as the value of the mdm key.

Since I didn’t have the mdm key and I’m not sure if we could send a notification through the APNS gateway to the device I’ve checked what happen next. The device responds to this push notification by contacting the MDM server using HTTP PUT over TLS (SSL) which matches with our Burp Collaborator request. This message may contain an Idle status or may contain the result of a previous operation. I though the requests that I was seeing on Burp Collaborator were Idle status since it was Sunday so I didn’t think anyone was sending commands to devices in a QA environment.

From the documentation we can see the MDM clients follow HTTP 3xx redirections without user interaction and in case of mdm.qa-vulnerable.requestsmuggling.com there is no client certificate authentication since we can see the header Mdm-Signature on the request.

If your MDM server is behind an HTTPS proxy that does not convey client certificates, MDM provides a way to tunnel the client identity in an additional HTTP header. If the value of the SignMessage field in the MDM payload is set to true, each message coming from the device carries an additional HTTP header named Mdm-Signature.

Press enter or click to view image in full size

My attack scenario was based in the way the MDM protocol works. From the documentation we can see after execute one command a device will wait for the server finish the process or sending more commands.

Press enter or click to view image in full size

In theory I could inject a redirection and replace the server response that pretends to finish the process and redirect the device to a fake MDM server which would send another command instead. To do that I got the example below from the document which sends a command to install an application on the device.

Press enter or click to view image in full size

As you can see from the documentation the user needs to accept the request in order to install the application. Since the attack is kind of blind I created a test Python server and hosted under https://myattackerdomain.com with the example above and add the parameter ManifestURL pointing to Burp Collaborator to see if I’d receive any feedback which unfortunately it didn’t happen.

After running my fake server for a few minutes and perform the attack pointing the redirection to https://myattackerdomain.com/api I was able to see just a few requests coming to my server. I’m not sure if these requests were coming from real MDM devices and since it was a QA environment I didn’t think there was much traffic from devices to the server.

Press enter or click to view image in full size

I was afraid to violate their policy so I decided to stop and send all the information above to the company and after that I got the answer below.

If you are able to prove that the vulnerability can be used for more than redirection, like gaining access to sensitive information, we can re-evaluate the reward.
No Retreat! No Surrender! 🥋

I decided to give a try on production since I wasn’t seeing much traffic in any other server. I did the same attack as before but now on mdm.prod-vulnerable.requestsmuggling.com and I got the response from the devices for valid server commands.

I also did a little improvement in my server to print the requests and reply with a response for the “ProfileList” command using this documentation as example. The screenshot below is from this python BaseHTTP server.

Press enter or click to view image in full size

In order to prove that I could execute MDM commands I got a valid CommandUUID from one of the outputs and changed one letter to be sure it would be a unique CommandUUID and did the same attack again.

By keep doing the same attack I got another request (which is the command response to the server) with the exactly same CommandUUID from my payload proving that I was able to execute the ProfileList MDM command in any client.

At this point there was nothing else to attack so I included everything in my report and started to press F5 waiting for the response below.

Alright! I think this proves your point much better. Based on the impact even just testing can have on active devices, please stop testing this while we investigate further.

After that the company asked a few questions about the attack and one thing that I highlighted to them was about the clients following the redirects. The RFC 2616 states it should send the data through the redirect URL but the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user.

In the MDM context it would be impracticable for a user accept all possible redirects that’s why in the MDM documentation it’s describing the 301 redirect will be automatically followed but it won’t be remember it. I have no idea why the clients needs to blindly follow the redirects.

RFC 2616
Press enter or click to view image in full size
MDM documentation

After some days when everything was confirmed as fixed I was rewarded with the maximum payout US$15,000 bounty and a US$50 bonus. In total I got US$17,050 for this report. 🤑

The company was really nice and also told me they created a lab to test the same attack but using the EraseDevice command. Below you can check their on comments about the results.

A few seconds later, we hear on the call the iPad had rebooted and was showing a progress bar. About a minute later, the iPad rebooted again and showed the default iOS setup screen. A complete device wipe!
Bonus Track 🏆

After receiving the bounty I asked the company if I could publish this post of course without mention their name or anything related to their company. They replied back saying to wait for a few days because some vendors were involved and they wanted to check if others costumers could have the same problem.

It took more than few days but finally I got the answer below.

Good news! Citrix has released their security bulletin and have credited you in it, as well as in their hall of fame!
Bulletin - https://support.citrix.com/article/CTX281474
Hall of Fame - https://www.citrix.com/about/trust-center/vulnerability-process.html
You should be all set to go ahead and publish your report.
Press enter or click to view image in full size
Press enter or click to view image in full size

Unfortunately Citrix doesn’t have any bug bounty program but at least I was recognized in their portal.

If you have any question or want to share any interesting technique about HTTP Request Smuggling please send email to ricardo.iramar@gmail.com or contact me on twitter @ricardo_iramar.

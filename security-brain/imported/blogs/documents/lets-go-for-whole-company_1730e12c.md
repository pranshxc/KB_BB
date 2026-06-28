---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-13_lets-go-for-whole-company.md
original_filename: 2023-07-13_lets-go-for-whole-company.md
title: Let’s Go For Whole Company
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 1730e12cbf3f6171357e26f264152e2e083fb1a03e5029c039da480f7fe00020
text_sha256: cc324dafb8c73830c4ef7869d9e051b917673906eb158eee1b548ff80899af62
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Let’s Go For Whole Company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-13_lets-go-for-whole-company.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `1730e12cbf3f6171357e26f264152e2e083fb1a03e5029c039da480f7fe00020`
- Text SHA256: `cc324dafb8c73830c4ef7869d9e051b917673906eb158eee1b548ff80899af62`


## Content

---
title: "Let’s Go For Whole Company"
url: "https://infosecwriteups.com/lets-go-for-whole-company-d2e24bcfb5ef"
authors: ["Arman (@M7arm4n)"]
bugs: ["Default credentials"]
publication_date: "2023-07-13"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 928
scraped_via: "browseros"
---

# Let’s Go For Whole Company

Let’s Go For Whole Company
M7arm4n
Follow
3 min read
·
Jul 13, 2023

121

1

Hello amazing hackers, here we are with another amazing post, this time we are not going to talk about the effects of a vulnerability on users or even the database. This time we want to talk about taking over an entire organization. I can say that more than 90% of the process of finding this vulnerability is summed up in the calculation.

Press enter or click to view image in full size

It was a private Pentest project, belonging to a government agency. They gave me two domains along with their subdomains. I started working on the main system to get started and was able to find a few XSS vulnerabilities. I spent some time on the subdomain but found nothing. A few days later I went back to Target again, but this time it wasn’t to find a vulnerability. I just wanted to do a very deep recon on the target.

To start extracting the subdomains of pairs of domains, I reached something close to 10 subdomains. Some of them were available. In the next step, I started phasing the subdomains with all kinds of backup files, but I didn’t achieve anything. Some paths were found, but they didn’t seem to be anything important.

I tried to find subdomains using ready tools such as subfinder and… but I thought to myself that it is possible that I have lost a subdomain. That’s why I started brute force DNS using other tools and then combined them with the DNSgen tool. After reducing the data, this time I reached 15 subdomains.

But again, nothing was found for us in these 5 new subdomains, but an interesting point in these 5 subdomains is that 3 of them refer to an IP, which the other 12 do not refer to. I was able to get 3 IPs from these subdomains using DNSX. I started my work with port scanning. the results of the portscan weren’t so interesting.

When I want to work deeply on a target, I always do virtual hosts discovery on the target using public wordlists and subdomains of the domain.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I did not achieve anything by using subdomains on the IPs, but when I phased the IP of our target, which I found with DNS Brute Force, with a public wordlist, I reached a virtual host named admin, and it was very attractive to me.

You can fuzz virtual hosts with FFUF:

FFUF -w ~/wordlist.txt -u http://127.0.0.1 -H "Host: FUZZ"

After opening the virtual host, I encountered a guacamole login panel, which defaults to the password and username: guacadmin. I entered the username and password and entered the admin account :)

I had remote connection access to the gate and monitoring server and many other things, the level of access was incredibly high and I could control the entire organization.

Press enter or click to view image in full size

Thank you for following me here, Don’t forget to follow me for more write-ups.

Linktree 🌲

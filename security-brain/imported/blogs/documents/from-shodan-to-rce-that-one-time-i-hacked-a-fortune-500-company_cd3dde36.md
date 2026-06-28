---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-08_from-shodan-to-rce-that-one-time-i-hacked-a-fortune-500-company.md
original_filename: 2022-08-08_from-shodan-to-rce-that-one-time-i-hacked-a-fortune-500-company.md
title: 'From Shodan to RCE: That one time I hacked a Fortune 500 company.'
category: documents
detected_topics:
- command-injection
- sso
- mfa
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- mfa
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: cd3dde36fbe53454e008e7b81e7b96a3284b2772e489a1fc794459a823e72854
text_sha256: 581a49d39388806dbfd1380540543c409c396e3510ad5fcbd9c9fada937b50fc
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# From Shodan to RCE: That one time I hacked a Fortune 500 company.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-08_from-shodan-to-rce-that-one-time-i-hacked-a-fortune-500-company.md
- Source Type: markdown
- Detected Topics: command-injection, sso, mfa, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `cd3dde36fbe53454e008e7b81e7b96a3284b2772e489a1fc794459a823e72854`
- Text SHA256: `581a49d39388806dbfd1380540543c409c396e3510ad5fcbd9c9fada937b50fc`


## Content

---
title: "From Shodan to RCE: That one time I hacked a Fortune 500 company."
url: "https://systemweakness.com/rooting-jenkins-remote-code-execution-on-a-live-bug-bounty-target-fc2c12d89a2e"
authors: ["vimanari_ (@vimanari_)"]
bugs: ["Missing authentication", "Arbitrary file read", "RCE", "Exposed Jenkins instance"]
publication_date: "2022-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2354
scraped_via: "browseros"
---

# From Shodan to RCE: That one time I hacked a Fortune 500 company.

From Shodan to RCE: That one time I hacked a Fortune 500 company.
vimanari_
Follow
5 min read
·
Aug 8, 2022

233

5

Press enter or click to view image in full size

tl;dr:

After grinding through Shodan results for like 5 hours I found an unauthenticated Jenkins dashboard that belonged to a Fortune 500 company and managed to:

Read the contents of any file on the server from within the browser; and
Assume complete control of the webserver. Full remote code execution (RCE) was achieved by popping a reverse TCP shell on the server as the root user from my local machine(!).

The target:

Press enter or click to view image in full size
Organisation: redacted.

As per usual, the target itself and any identifying details have been redacted from this write up in line with the program scope.

What I can tell you is the target is a multinational company with tens of thousands of employees and bajillions of endpoints to play with. I’ve been prodding at this beast of a program since early 2020.

The program has a luxurious scope with *.company.* domains along with any Asset owned by the organisation being fair game. This calls for a wide-scope reconnaissance process where you can really go “top down” and find all assets owned by the organisation by searching ASNs, SSL certificates etc.

WTF is a Jenkins, anyway?

Jenkins is an open source continuous integration/continuous delivery and deployment (CI/CD) automation software DevOps tool written in the Java programming language. It is used to implement CI/CD workflows, called pipelines.

Initial recon:

Gently boys, the scope says max 20 requests/sec.

I found this specific subdomain during the recon phase using Shodan. It came up after a particularly protracted exercise of manually browsing Shodan results and opening interesting pages in new tabs. I probably sifted through at least 100 pages of results before landing on this dashboard.

The search term I used was:

ssl: "company"

The result looked something like this:

Press enter or click to view image in full size
Shodan search results for SSL certificates owned by the target organisation

Some initial poking around revealed some interesting items:

Ability to install add-on apps. Specifically the Terminal app. The shell would startup but no command would successfully run. Dead end.
Ability to see all user profiles. This helped confirm that we were in fact looking at a server owned by the organisation. A quick LinkedIn search or the users confirmed that they were all members of the organisation‘s DevOps team, bingo.
Press enter or click to view image in full size
The already-installed Groovy terminal. This was juicy. Using these 2 guides, I was able to find the two following bugs:
Remote Code Execution | A Story of Simple RCE on Jenkins Instance.
Vulnerability Category: A1- Code Injection

medium.com

Abusing Jenkins Groovy Script Console to get Shell
Jenkins is a leading open source automation server for deploying and automating any project.

blog.pentesteracademy.com

Arbitrary file read:

What is an arbitrary file read vulnerability? This vulnerability exists because the web application does not properly validate user-supplied input. An attacker could exploit this vulnerability by sending a crafted HTTP request that displays the contents of any file on the webserver without authentication.

The bug: This little beauty was located at /script and was basically a primitive little webshell.

Get vimanari_’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After looking at previous research and reviewing the Jenkins documentation, I started experimenting with various commands and was able to arbitrarily print the contents of any file on the webserver:

Press enter or click to view image in full size
The successful payload that revealed too much.
Press enter or click to view image in full size
Boom-shakalaka!

Remote code execution:

What is a remote code execution vulnerability? A misconfiguration in the web application whereby an attacker can remotely execute commands on someone else's computing device, in this case as the root user.

The bug: At this point I thought my bloodlust was satiated, but boy was I wrong. Digging further into the depths of the documentation and some previous writeups, I was able to fire a reverse TCP shell from within the webshell! It took a significant number of iterations to finally work, but we got there in the end:

Press enter or click to view image in full size
The syntax used for the reverse shell

One thing that helped was knowing which ports were open on the webserver. An nmap scan of the server showed port 80 (http) and port 443 (https) being open.

I tried all the usual reverse shell ports in my netcat listener (4444, 4445, 9001, 1337) and none worked — so sometimes, it pays to use the ports that are already open on the target!

Voila:

Press enter or click to view image in full size
Final boss: root-user reverse TCP shell.

Impact:

In this case, an attacker can perform any action they want on the target webserver, including accessing, modifying and removing all files.

I did not proceed past the point of confirming my user as root and the networking info under ifconfig as this is evidence enough of compromise.

Lessons:

Persistence is key in large-scope recon. Push further beyond what others are willing to.
Experiment with your payloads — you never know which combination of IP address, port, quotes/no quotes etc will work in the end, keep on trying until it does.
Don’t be satisfied with the first bug you find. If you find one misconfigured element in a web app, chances are there is more to find if you dig a little deeper.

Timeline:

16th of May, 2022: Bugs submitted via bug bounty platform, vendor responded immediately.

17th of May, 2022: Submission resolved by vendor — Jenkins instance taken offline.

CVSSv3 Severity Rating of this bug upgraded to: Exceptional (9.5–10/10)

Outcome: redacted.

How to remediate:

Do not expose your Jenkins Dashboard to the open internet.
If you absolutely must — Enforce login for read access to the dashboard, and/or:
Enforce 2FA

Bonus round - How to automate finding other vulnerable Jenkins instances to test:

Step 1: Register for a Shodan account and configure Shodan CLi

Step 2: Compile a list of all organisation names that have bug bounty programs from here

Step 3: Save the list in a text file and run the following bash one-liner:

while read line; do shodan search ssl:$line x-jenkins 200; done < list.txt

Step 4: Profit????

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-04_responsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce.md
original_filename: 2020-02-04_responsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce.md
title: 'Responsible Disclosure: Breaking out of a Sandboxed Editor to perform RCE'
category: documents
detected_topics:
- command-injection
- cloud-security
- ssrf
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- cloud-security
- ssrf
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 3f78e90f3dc51a498e02cf60bf3cac99f4b1fda96a4616c995268566cb7a4d58
text_sha256: 9e3f989e6c18266a5b0a3cffba01aed7aaa1604eae4b5960722c5f81fa7666b1
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Responsible Disclosure: Breaking out of a Sandboxed Editor to perform RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-04_responsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, ssrf, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `3f78e90f3dc51a498e02cf60bf3cac99f4b1fda96a4616c995268566cb7a4d58`
- Text SHA256: `9e3f989e6c18266a5b0a3cffba01aed7aaa1604eae4b5960722c5f81fa7666b1`


## Content

---
title: "Responsible Disclosure: Breaking out of a Sandboxed Editor to perform RCE"
page_title: "Responsible Disclosure:  Breaking out of a Sandboxed Editor to perform RCE - Weblog of JD"
url: "https://jatindhankhar.in/blog/responsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce/"
final_url: "https://jatindhankhar.in/blog/responsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce/"
authors: ["Jatin Dhankhar (@jatindhankhar_)"]
programs: ["HackerEarth"]
bugs: ["RCE"]
publication_date: "2020-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4794
---

# Responsible Disclosure: Breaking out of a Sandboxed Editor to perform RCE 

__3 minute read

####  __Table

  * tl;dr
  * Story - Finding the issue \- Trying out things \- Reading AWS Credentials
  * Timeline

# tl;dr

Found a way to escape the sandboxed editor to perform Remote Code Execution which leads to the ability to view AWS credentials, SSL certificate and other stuff.

Pretty much owning the entire machine ![:smiling_imp:](https://github.githubassets.com/images/icons/emoji/unicode/1f608.png)

# Story - Finding the issue

If you are still here after reading the tl;dr, I guess you are here for the story?  
So, let me give you one.

While doing recon I found many sub-domains and IP addresses belonging to HackerEarth, one of them was [https://[REDACTED]/#/home/node/he-theia/sandbox](https://%5C%5BREADACTED%5C%5D/#/home/node/he-theia/sandbox) which was running an online ide built on top of vs-code named [Theia IDE](https://theia-ide.org/ "https://theia-ide.org/").

At first glance, it looked pretty boring, after all, it’s an IDE running in a browser (wait, that’s normal since most of them are electron based ![:neutral_face:](https://github.githubassets.com/images/icons/emoji/unicode/1f610.png) )

So, anyway, I played around with it for a while, the ultimate goal was to execute random code on the machine. But, they removed the terminal view command from the IDE shortcuts and menu. So, I tried to “run” the code file but that option was also not available.

Then poking around I tried “Task: Run selected text” by bringing up the global action menu shortcut from vscode (ctrl/cmd + shift + p) and lo, and behold, it opened up a terminal. ![](/images/disclosure-hackerearth/run_selected_text_prompt.png)

One I got the terminal access, it was easy to demonstrate the RCE.

![](/images/disclosure-hackerearth/terminal_prompt.png)

### Trying out things

I tried with the possibility of reading system config files and was able to read HackearEarth’s private SSL `.crt` and `.key` files. Pretty much, most of the system configuration files.

![](/images/disclosure-hackerearth/ssl_certificates.png)

![](/images/disclosure-hackerearth/ssl_private_key.png)

I was even able to read the git log and original `ide_fetcher.py` that powered the ide initial startup commands since the repo cloned still had git metadata.

![](/images/disclosure-hackerearth/git_config.png)

![](/images/disclosure-hackerearth/git_log.png)

Through some command-line fu, I was able to read the original arguments used to invoke the web-ide.

![](/images/disclosure-hackerearth/command_line_arguments.png)

### Reading AWS Credentials

After it was clear that I was able to read system files, write arbitrary files and command, I wanted to see if it was possible to use the terminal to read AWS credentials since the instance was hosted on AWS infrastructure just like the rest of the HackerEarth’s infrastructure.

I first tried the usual metadata URL to access aws details

`curl http://169.254.169.254/latest/api/token` but it didn’t work instead it gave me `curl: failed to connect`.

Lost, I tried to ping the domain that also didn’t work. Then I found a blog by Puma Scan on [Cloud Security - Attacking The Metadata Service](https://pumascan.com/resources/cloud-security-instance-metadata/)

There it was mentioned that attacking ECS metadata was different from attacking EC2 metadata service since it was served from a different domain. Then I checked the environment variable output again which I ignored earlier for some reason ![:sweat_smile:](https://github.githubassets.com/images/icons/emoji/unicode/1f605.png) and it was right there in front of my eyes the whole time.

![](/images/disclosure-hackerearth/env_output.png)

It contained both the `ECS_CONTAINER_METADATA_URI` and `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI`

After that, it was just a `curl` away ![:smile:](https://github.githubassets.com/images/icons/emoji/unicode/1f604.png)

![](/images/disclosure-hackerearth/aws_metadata.png)

![](/images/disclosure-hackerearth/aws_creds.png)

# Timeline

  * Tue, Dec 24 [ 7:35 PM IST] - Reached out to HackerEarth support about the issue
  * Wed, Dec 25 [ 9:50 AM IST] - HackerEarth support team asked to submit the issue to them so that they can forward it to security team (Although I wanted to report it directly to security team)

< Back and forth regarding submission >

  * Wed, Dec 25, 2019 [ 10:25 PM IST ] - Submitted the issue along with detailed POC and evidence
  * Thu, Dec 26, 2019 [ 05:49 PM IST ] - The instance was down. I asked HackerEarth for the confirmation of the fix.
  * Fri, Dec 27, 2019 [ 12:57 PM IST] - HackerEarth confirmed the fix from their end.
  * Mon, Jan 13, 2020 [12:32 PM IST] - Bounty Awarded
  * Thu, Jan 23, 2020 [4:21 PM IST] - Bounty received
  * Thu, Jan 23, 2020 [11:10 PM IST] - Disclosure draft shared
  * Tue, Feb 04, 2020 [06:03 PM IST] - Disclosure draft approved
  * Tue, Feb 04, 2020 [06:25 PM IST] - Blog published

**__Updated:** February 4, 2020

[__Twitter](https://twitter.com/intent/tweet?text=Responsible+Disclosure%3A++Breaking+out+of+a+Sandboxed+Editor+to+perform+RCE%20https%3A%2F%2Fjatindhankhar.in%2Fblog%2Fresponsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce%2F "Share on Twitter") [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fjatindhankhar.in%2Fblog%2Fresponsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce%2F "Share on Facebook") [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fjatindhankhar.in%2Fblog%2Fresponsible-disclosure-breaking-out-of-a-sandboxed-editor-to-perform-rce%2F "Share on LinkedIn") [Previous](/blog/auto-refresh-tokens-in-ruby-using-procs/ "Auto Refresh tokens in Ruby using Procs
") Next

#### Comments

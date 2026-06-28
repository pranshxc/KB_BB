---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-12_zip-bomb-attack.md
original_filename: 2023-02-12_zip-bomb-attack.md
title: Zip bomb attack
category: documents
detected_topics:
- access-control
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- file-upload
- api-security
language: en
raw_sha256: a4f79532c8a64d7807afc5032dabf6adf8be6ab5a90d9d6f4ad0f647274b7c7a
text_sha256: 8694d826376fcebd9d41d5d03857250bc5c3d0e170e77127ed1655df64b8c744
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Zip bomb attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-12_zip-bomb-attack.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `a4f79532c8a64d7807afc5032dabf6adf8be6ab5a90d9d6f4ad0f647274b7c7a`
- Text SHA256: `8694d826376fcebd9d41d5d03857250bc5c3d0e170e77127ed1655df64b8c744`


## Content

---
title: "Zip bomb attack"
url: "https://medium.com/@ramkumarnadar47/zip-bomb-attack-88d84a98be9f"
authors: ["Ramkumar Nadar"]
bugs: ["Zip bomb", "DoS", "Unrestricted file upload"]
publication_date: "2023-02-12"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1540
scraped_via: "browseros"
---

# Zip bomb attack

Zip bomb attack
Ramkumar Nadar
Follow
4 min read
·
Feb 12, 2023

30

A while ago I encountered an application which had file upload functionality exclusive to zip files. One of my witting seniors told me you can perform a zip bomb attack and so I did.

It was simple enough to perform and I’ll explain the process I went through in this article.

After knowing that the application allows only zip files to be uploaded and that too with a certain naming convention I researched on how you go about performing a zip bomb attack and learnt that you need a zip bomb in the first place, that is to say, you need a zip file which unzips to a humongous size. I found the same in the below link (Shout out to David Fifield @bamsoftware.com):

A better zip bomb
David Fifield david@bamsoftware.com updated , , , , , , , , , , , , , , ,, , ,, This article shows how to construct a…

www.bamsoftware.com

The first file ‘zbsm.zip’ sized 42 kb unzips to 5.5 GB and the rest is obvious.

These files are flagged as viruses by most anti-virus programs and rightly so. And all three are flagged as dangerous files by the chrome browser.

Get Ramkumar Nadar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For instance check below the scan report for the ‘zbsm.zip’ in the Virus Total site.

Press enter or click to view image in full size

And the chrome will display the warning:

Having acquired this file, you need two user Ids of the application in question who have access to the same upload functionality;

And with one user you upload the file, in my case, I uploaded the file ‘zblg.zip’ (10 MB → 281 TB) from user Bob and the upload got stuck, I was staring at the screen for a while assuming the application crashed or something which lead me to upload the file with the user Alice and to my amusement I found the error prompt to the effect “Disk space is full”. It was only then I learnt that the upload got stuck because there was no storage space left.

This attack was possible because the application was not verifying the file size before writing it onto the disk which also made me realize that I should have uploaded a 42 kB file in place of the 10 MB one, thereby avoiding the DoS and an earful from my manager. In my feeble defence, the attack was performed in a UAT environment.

The core problem lies in the file size limit and hence the solution depends on a file size check.

A code as such could be implemented on the server side as mitigation (code and explanation by ChatGPT):

Press enter or click to view image in full size

In this code, the prevent_zip_bomb function takes a zip file and a size limit as arguments. The function uses the zipfile module to open the zip file, and then iterates through each file in the archive using the infolist method. The file_size attribute of each ZipInfo object is checked against the size limit, and if any file exceeds the limit, a ValueError is raised to cancel the unzip operation.

So it all boils downs to the file size limit. This is a very simple attack with a severe impact. If you are willing to perform this attack, first take proper authorization from the management or the concerned authority and then begin the pen test and that too mostly with the 42zip, as in you check first, if the application accepts a file with the file size of 5.5 GB and then decide on what is to be done after coordination with all the concerned party.

I am emphasizing this because if you are to upload a file of size 281 TB or more it will most definitely cause a DoS which can lead to the compromise of availability and consequently cause financial loss, so keep everyone in the loop. Period.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-09_file-upload-to-rce.md
original_filename: 2021-12-09_file-upload-to-rce.md
title: File Upload to RCE
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
- supply-chain
language: en
raw_sha256: 8ce507d79923871f9feb891d289aebf43c9cae49a51dbb5f073ca479bbaba0f4
text_sha256: 60d121f37c11812ff2f2f764f35b0597e882c9871cedc50dfd6ddc32aa97bc17
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# File Upload to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-09_file-upload-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `8ce507d79923871f9feb891d289aebf43c9cae49a51dbb5f073ca479bbaba0f4`
- Text SHA256: `60d121f37c11812ff2f2f764f35b0597e882c9871cedc50dfd6ddc32aa97bc17`


## Content

---
title: "File Upload to RCE"
url: "https://ahmed8magdy.medium.com/file-upload-to-rce-538bb4128062"
authors: ["Ahmed Magdy (@8Ahmed88Magdy8)"]
bugs: ["Unrestricted file upload"]
publication_date: "2021-12-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3099
scraped_via: "browseros"
---

# File Upload to RCE

File Upload to RCE
Ahmed Magdy
Follow
3 min read
·
Dec 8, 2021

117

2

Hi , My name is Ahmed Magdy :)

and i will be publishing my first Write-up for bug about a File Upload to RCE

Let’s go……

First of all, This was a private program, so I will refer to it with example.com or subdomain.domain

Here I can upload A Normal photo

Press enter or click to view image in full size
( احمينا ياااا رب )

All file upload Profile updated successfully :)

alt=”photo here”

But not work with all ( alt=”photo here” )

Press enter or click to view image in full size
cannot be displayed because it contains errors.

After bypass the filter upload it is work

Press enter or click to view image in full size
Profile updated successfully

Wait some code in file work and some not work

Press enter or click to view image in full size
Press enter or click to view image in full size
Code HTML and JS and some PHP work but all parameter not work
Press enter or click to view image in full size
Press enter or click to view image in full size
All Commands in parameter not work and blocked

example.com/uploads/ (ids user) /lol.png.php?c=ls;id;whoami;

ِAnd all Commands not work

code HTML and JS and some PHP work but all parameter not work it is rce but all Commands block but is OK…

Get Ahmed Magdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I report this because i can print phpinfo() severity P2

oh nice…

After 2 day and more search i ask some friend as Abdalla Tarek and Flex about is issue

After ( Al habd Al gamed ) with Tarek

كمان واحده و النبى ياريس 😂😂 كفايه بجي😂😂ء

Flex give my the solve this problem

Resource popen (command ,$mode )

Opens a pipe to a process executed by forking the command given by command…. Example: <?php $h = popen("ls","r");?>

Resource fgets (file,length)

Function returns a line from an open file…. Example:

$handle = fopen("inputfile.txt", "r");
if ($handle) {
  while (($line = fgets($handle)) !== false) {
  // process the line read.}
  fclose($handle);
}else {error opening the file.}

The site afraid and work after the two lines Flex,
And I wrote more than 20 lines and the site don’t afraid or work

happy and sad
Press enter or click to view image in full size
Press enter or click to view image in full size
example.com/uploads/96/lol.png.php?c=cat /etc/passwd
All Done
I report that as RCE the severity become P1 …. :)

Think you for your time :)

And finally, Thank you to read this write-up :)

Have a great day :)

I hope you enjoyed reading and I will be very happy if you have any feedback!!

Contact me if you want : Ahmed Magdy

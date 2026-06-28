---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-11_adminer-script-results-to-pwning-server-private-bug-bounty-program.md
original_filename: 2018-08-11_adminer-script-results-to-pwning-server-private-bug-bounty-program.md
title: Adminer Script Results to Pwning Server?, Private Bug Bounty Program
category: documents
detected_topics:
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: c17807076aed585cc2f5ec08a38125eeb09afa0d79cf0517cb7e135df23aca21
text_sha256: 610d78fc86cea3477a102b1451bff26904dd4f8bd69bc0ca025d38cf300c0682
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Adminer Script Results to Pwning Server?, Private Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-11_adminer-script-results-to-pwning-server-private-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c17807076aed585cc2f5ec08a38125eeb09afa0d79cf0517cb7e135df23aca21`
- Text SHA256: `610d78fc86cea3477a102b1451bff26904dd4f8bd69bc0ca025d38cf300c0682`


## Content

---
title: "Adminer Script Results to Pwning Server?, Private Bug Bounty Program"
url: "https://medium.com/bugbountywriteup/adminer-script-results-to-pwning-server-private-bug-bounty-program-fe6d8a43fe6f"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
bugs: ["Authentication bypass"]
publication_date: "2018-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5756
scraped_via: "browseros"
---

# Adminer Script Results to Pwning Server?, Private Bug Bounty Program

Adminer Script Results to Pwning Server?, Private Bug Bounty Program
Yasho
Follow
3 min read
·
Aug 11, 2018

306

3

If an adminer script is left in a server, most likely the server will be pawned soon. In this story, I want to introduce a technique in order to exploit adminer script without valid credentials.

Recon

While ago I participated in a private bug bounty program (let name the domain milk.tld in this story), I did recon with some sorts of scripts, sub-domain finders and etc, revealed several sub-domains, one of them was support redirecting the user to the main domain. I conducted an action brute force by wfuzz by the following syntax:

https://support.milk.tld/FUZZ

Finally found /login endpoint. I tested too many vectors on the page, didn’t find any flaw, though. Afterward, I conducted a file name brute force by wfuzz by using some word-lists, found an interesting file named connect.php, after opening, I saw the adminer.php script.

Common scenario is brute force attack, I did it but nothing gained.

Attack Vector

With inspiration of following articles:

https://w00tsec.blogspot.com/2018/04/abusing-mysql-local-infile-to-read.html

https://phonexicum.github.io/infosec/sql-injection.html

I designed an attack scenario:

Setting up MySQL server within public IP address
Connecting adminer to the MySQL server (now user has logged to adminer)
Reading local files by read data local infile command, inserting the results in a table
Get Yasho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Press enter or click to view image in full size
The Attack

Just filled adminer login form by server address and credentials I’d set up before. Logged-in successfully.

The right MySQL command to read files from the client’s side is

LOAD DATA LOCAL INFILE '/etc/passwd' 
INTO TABLE test.test
FIELDS TERMINATED BY "\n"

The result:

Press enter or click to view image in full size

YES! I’d capability of reading files by the mysql user. I went to read Nginx configuration file. As each site has a configuration in /etc/nginx/sites-enabled/ , However, I didn’t know the filename. I created a list based on the company name and started brute forcing the name. Luckily I found the configuration file (the filename was mil.tld just a letter removed compared with the original domain, and there wasn’t .conf extension):

/etc/nginx/sites-enabled/mil.tld

The result was:

The all I wanted was rootpath. Reading index.php confirmed the portal had written by Laravel. Opening the database.php revealed the connection credentials of the database:

I got all the databases within the credentials revealed. I connected with credentials to adminer, consequently, I had the databases. Unfortunately, the user didn’t have FILE permission so I didn’t accomplish uploading a shell script by into outfile MySQL query. However, the main point is about adminer script which might result in pawning the server in the similar cases. In comparison to phpMyAdmin, admin is less secure since it has host field which makes hackers conduct several scenario attacks pre-authentication. As an instance, revealing the real IP address of servers behind CDNs as Cloud-flare.

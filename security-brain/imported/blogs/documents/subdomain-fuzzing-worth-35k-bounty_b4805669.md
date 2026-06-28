---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-18_subdomain-fuzzing-worth-35k-bounty.md
original_filename: 2024-03-18_subdomain-fuzzing-worth-35k-bounty.md
title: Subdomain Fuzzing worth 35k bounty!
category: documents
detected_topics:
- sqli
- sso
- command-injection
tags:
- imported
- documents
- sqli
- sso
- command-injection
language: en
raw_sha256: b4805669bf758be5f025fa282f5b77eeb278ed4094e4192a1dea3195c7e07e90
text_sha256: 5ab2ccbfcda7d9c6fa8da2f561b25020571346d0c06e9a452f5125c671f30209
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Fuzzing worth 35k bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-18_subdomain-fuzzing-worth-35k-bounty.md
- Source Type: markdown
- Detected Topics: sqli, sso, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `b4805669bf758be5f025fa282f5b77eeb278ed4094e4192a1dea3195c7e07e90`
- Text SHA256: `5ab2ccbfcda7d9c6fa8da2f561b25020571346d0c06e9a452f5125c671f30209`


## Content

---
title: "Subdomain Fuzzing worth 35k bounty!"
url: "https://medium.com/@HX007/subdomain-fuzzing-worth-35k-bounty-daebcb56d9bc"
authors: ["Abdullah Nawaf / HX007", "Orwa Atyat (@GodfatherOrwa)"]
bugs: ["RCE", "Authentication bypass", "SQL injection"]
bounty: "35,000"
publication_date: "2024-03-18"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 377
scraped_via: "browseros"
---

# Subdomain Fuzzing worth 35k bounty!

1

·

Top highlight

1

Subdomain Fuzzing worth 35k bounty!
Introduce Myself:
HX007
Follow
5 min read
·
Mar 18, 2024

3.6K

39

My Name is Abdullah Nawaf, Full Time Bug Bounty Hunter, Working actively in BugCrowd with Top 50 Rank, Rank 11 for P1 Bugs, Hunting For P1, and P2 Bugs

HackerX007 on Bugcrowd
Bugcrowd's bug bounty and vulnerability disclosure platform connects the global security researcher community with your…

bugcrowd.com

In this Writeup I will explain how I and 
Orwa Atyat
 Were able to get 35K Bounty using Subdomain Fuzzing and chaining multiple bugs together to Get Full rce

I’ve been hunting for 4 years and this is my first Writeup, Sorry if there was any mistake in it, I tried my best :)

Description:

The Story being in 2022 when I reported Auth Bypass Leads to SQLI&RCE for a private program in Bugcrowd, the Bug was fixed just one day after the report.

In 2024/3 me and orwa decided to re-testing our old bugs

The target that we were Re-Testing was admin.Target.com

we used Subdomain Fuzzing By Using this command

ffuf -w /subdomain_megalist.txt -u 'https://adminFUZZ.Target.com' -c  -t 350 -mc all  -fs 0

You will find subdomain_megalist.txt in reference part

Using this command we found a subdomain called admintest.Target.com

Press enter or click to view image in full size

You can notice there is a lot of Errors in the PIC, But its ok since u fuzzing subdomain ,errors means the the subs not working

The admintest.Target.com was vulnerable since it has the same Back-end as the origin subdomain admin.Target.com

Let's talk about the bugs we have found one by one

Auth Bypass&BAC :

The https://admintest.Target.com was redirect to https://admintest.Target.com/admin/login.aspx

reading some js files, we found an endpoint called https://admintest.Target.com/admin/main.aspx Opening it directly in the browser will redirect us again to the login page but in Burp we noticed something,

Press enter or click to view image in full size

the Content-Length was so large, so larger for redirect response

you can notice here that even though you redirect to the login page, the end is working, with full access,
by removing these 3 headers I was able to access the panel

Press enter or click to view image in full size

Using Burp Match And Replace or using Burp intercept response by

change 302 Moved Temporarily to 200 OK
remove Location: /admin/Login.aspx?logout=y
remove html redirect code 

we were able to get FULL Auth Bypass, and it was fully functional, not just front-end bypass, after digging deep, we were able to find adduser.aspx this endpoint was redirecting us to the login page as main.aspx using the same trick in adduser.aspx we were able to access the endpoint and add an admin account, also we found another endpoint that shows admins password&username without any Auth

Press enter or click to view image in full size

SQLI:

After adding admin account , we were able to login It would be easier for us than using the above trick

we found an endpoint called `SQLQuery.aspx` And from it name u know what it function :)

The first thing I tried this Query Select * from users

Get HX007’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

we were able to see all user's info including passwords,emails,username

Press enter or click to view image in full size

RCE:

Since the database was `mssql` we tried to escalate it to RCE using xp_cmdshell

you read about xp_cmdshell

Enable xp_cmdshell in SQL Server
Learn how to enable xp_cmdshell for SQL Server and some of the errors you may encounter when using xp_cmdshell as well…

www.mssqltips.com

In a short way xp_cmdshell allow the user to execute commands in the system using mssql

By default it is disabled, but you can enable it so easily, using sqlmap option --os-shell

But in our case, we don't need sqlmap since we execute query directly to the database just like Select * from users also SELECT @@version

so the first thing we should do to make xp_cmdshell working is to enable it by using these queries

SP_CONFIGURE "show advanced options", 1
RECONFIGURE
SP_CONFIGURE "xp_cmdshell", 1
RECONFIGURE

you can see this, it would help

https://medium.com/@s12deff/microsoft-sql-server-to-rce-984016b4aaf8

and then xp_cmdshell ‘whoami’ BOOM RCE!

Press enter or click to view image in full size

we sent all of them in one report + one other SQLI in another endpoint,and we got in total 35k bounty

Lessons learned&Summary:

1_Always check the redirect response in burp

I and Orwa found a lot and a lot of that same auth bypass, my first bounty was in 2020 and it was the same trick, /admin/admin.php Redirect to login.php But when I see the response in burp , the admin.php just working fine and it is just Front-End Redreact !

2_ If u found a bug in a subdomain and it fixed try Subdomain Fuzzing

you can use it this way

admin-FUZZ.target.com E.G: admin-stg.target.com
FUZZ-admin.target.com E.G: cert-admin.target.com
adminFUZZ.target.com  E.G: admintest.target.com
FUZZadmin.target.com  E.G  testadmin.target.com
admin.FUZZ.target.com E.G: admin.dev.target.com

The Command again

ffuf -w /subdomain_megalist.txt -u 'https://adminFUZZ.Target.com' -c  -t 350 -mc all  -fs 0

-t means threads , dont make it so high u could miss alot of working subs , aslo its dpends in your network speed
,sinc im using vps 350 find for me 

-mc all means macth all respone codes like 200,302,403 and this importent 

3_Try to escalate the bug before reporting

4_ Quality over Quantity:

when u find multiple bugs or chaining bugs together try to report them as one report , u will get higher bounty :)

Reference:

subdomain_megalist.txt

https://github.com/netsecurity-as/subfuz/blob/master/subdomain_megalist.txt

thx for Netsecurity for that list :)

you can find a lot of lists here also

https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS

All Of This Findings Was With OrwaGodfather As We Collaborate On All Hunt

I hope you guys have enjoyed the Reading

HX007&OrwaGodfather

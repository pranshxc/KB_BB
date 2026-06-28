---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-14_my-new-discovery-in-oracle-e-business-login-panel-that-allowed-to-access-for-all.md
original_filename: 2022-05-14_my-new-discovery-in-oracle-e-business-login-panel-that-allowed-to-access-for-all.md
title: My New Discovery In Oracle E-Business Login Panel That Allowed To Access For
  All Employees Information's & In Some cases Passwords At More Than 1000 Companies
category: documents
detected_topics:
- sso
- command-injection
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- cloud-security
language: en
raw_sha256: 7d04ffdef6ecd2adc56058856b8b1541f649b08e29d5cdcbdd144af45a0414fa
text_sha256: 0e6e4074b08174b950a8ec09076daecc2dade763943f924149b77d58521f39e3
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# My New Discovery In Oracle E-Business Login Panel That Allowed To Access For All Employees Information's & In Some cases Passwords At More Than 1000 Companies

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-14_my-new-discovery-in-oracle-e-business-login-panel-that-allowed-to-access-for-all.md
- Source Type: markdown
- Detected Topics: sso, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `7d04ffdef6ecd2adc56058856b8b1541f649b08e29d5cdcbdd144af45a0414fa`
- Text SHA256: `0e6e4074b08174b950a8ec09076daecc2dade763943f924149b77d58521f39e3`


## Content

---
title: "My New Discovery In Oracle E-Business Login Panel That Allowed To Access For All Employees Information's & In Some cases Passwords At More Than 1000 Companies"
url: "https://orwaatyat.medium.com/my-new-discovery-in-oracle-e-business-login-panel-that-allowed-to-access-for-all-employees-ed0ec4cad7ac"
authors: ["Orwa Atyat (@GodfatherOrwa)", "Abdullah Nawaf (@XHackerx007)"]
bugs: ["Exposed registration page"]
publication_date: "2022-05-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2641
scraped_via: "browseros"
---

# My New Discovery In Oracle E-Business Login Panel That Allowed To Access For All Employees Information's & In Some cases Passwords At More Than 1000 Companies

Top highlight

My New Discovery In Oracle E-Business Login Panel That Allowed To Access For All Employees Information's & In Some cases Passwords At More Than 1000 Companies
Orwa Atyat
Follow
4 min read
·
May 14, 2022

1.1K

8

Hay Hunters , Hello Infosec Community

To Introduce My Self

My Name Orwa Atyat Iam Full Time Bug Bounty Hunter As You Know Me On Twitter (GodFather Orwa)

https://twitter.com/GodfatherOrwa
And Hunting On BugCrowd For Full Time With A Current Rank 66th And On P1 Bugs Current Rank 8th
https://bugcrowd.com/orwagodfather
https://hackerone.com/mr-hakhak

Our Topic Here Is About New Discovery In Oracle E-Business Login Panel That Allowed To Access For All Employees Information’s [Emails , First & Last Name , User Name] & In Some cases Access To Data Base Passwords At More Than 1000 Companies That Used Oracle E-Business Login Panel Service

The Best Part Here It Is Not Common Vulnerability And Exposure (CVE) It Is New Vulnerability Due To This Security Issue, I Was Looking & Test It On Companies Deal With This Panel And It Work 100%

So You Can Check Your Private Programs , Or If You A Customers For Oracle Check Your Panels

As I Reported This And Fixed On About 15 Bounty Programs Like Uber, Amazon, Mastercard , Etc…..

In The Next Section Description & Steps To Reproduce

Description:

So I Discovery This Bugs On Oracle E-Business Login That When You Visit Its Like This

Target/OA_HTML/AppsLocalLogin.jsp
Press enter or click to view image in full size

The Bug Here That I Can Create And Get Full Login And Access To This Panel

But When You Go To Register here Its Now Working As This Just For Employees

Get Orwa Atyat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But You Can Register A Account On This End

Target/OA_HTML/ibeCAcpSSOReg.jsp
Press enter or click to view image in full size

NOTE: Till Now This A Known Issue My Discovery After Create Account And Login

After I Found This Bug I Made Shodan Dork To Find All Oracle E-Business Login Panels

“X-ORACLE-DMS-ECID” http.title:”Login” 200
Press enter or click to view image in full size
Steps To Reproduce For PII:

Visit The Target And Create Account

Target/OA_HTML/ibeCAcpSSOReg.jsp

And Back And Login With Your Credentials On

Target/OA_HTML/AppsLocalLogin.jsp
Press enter or click to view image in full size
Move To Manage Proxies
Run Proxy Report
Press enter or click to view image in full size
Get Access For All Employees Info
Emails &First name & Last Name & Username
Add For Employees That Start By a For Example In Search And Search
Press enter or click to view image in full size
search for a or b or C Etc..
And You Can Search by Username Or First Or Last Name Or Email 
And Will Got All Employees Result's  
Press enter or click to view image in full size

There Is Definitely More But No Need To Dig Deeper

Steps To Reproduce For Passwords:

Note its not In all Panels Enabled

Back To home Page And Check On
Diagnostic Console If You Can Find It Then Ok With This One

Visit Diagnostic Console

Press enter or click to view image in full size
Visit SQL
===>
In SQL Statements
===>
select * from FND_USER
===>
RUN SQL
Press enter or click to view image in full size

Then You Will Get Access For

USER_IDs,
USER_NAMEs,
LAST_UPDATE_DATE,
LAST_UPDATED_BY
CREATION_DATE,
CREATED_BY,
LAST_UPDATE_LOGIN,
ENCRYPTED_FOUNDATION_PASSWORDs

All Of This Findings Was With Hackerx007 As We Collaborate On All Hunt

I Hope you guys have enjoyed the Reading

and hope you learn and found bugs and tweet by that for me that will make my happy

Stay safe dears

Orwa

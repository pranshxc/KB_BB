---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-20_google-vrp-insecure-direct-object-reference-313370.md
original_filename: 2022-10-20_google-vrp-insecure-direct-object-reference-313370.md
title: Google VRP — [Insecure Direct Object Reference] $3133.70
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 6945164185c28d353892345ab7373644cf6096afcd87e10429dfe019e2b2f3b9
text_sha256: c9f7c634f24183ba651281cfdcf2188d7b4121e93be2fdd58a04d16a66cac3ab
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Google VRP — [Insecure Direct Object Reference] $3133.70

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-20_google-vrp-insecure-direct-object-reference-313370.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `6945164185c28d353892345ab7373644cf6096afcd87e10429dfe019e2b2f3b9`
- Text SHA256: `c9f7c634f24183ba651281cfdcf2188d7b4121e93be2fdd58a04d16a66cac3ab`


## Content

---
title: "Google VRP — [Insecure Direct Object Reference] $3133.70"
url: "https://caesarevan23.medium.com/google-vrp-insecure-direct-object-reference-3133-70-a0e37023a4c7"
authors: ["Caesar Evan Santoso"]
programs: ["Google"]
bugs: ["IDOR"]
bounty: "3,133.70"
publication_date: "2022-10-20"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 2009
scraped_via: "browseros"
---

# Google VRP — [Insecure Direct Object Reference] $3133.70

Google VRP — [Insecure Direct Object Reference] $3133.70
Caesar Evan Santoso
Follow
4 min read
·
Oct 20, 2022

362

5

Press enter or click to view image in full size
Google VRP

Hi All!!!, Yes… it’s me. As usual I want to give a story about how I find IDOR [Insecure Direct Object Reference] vulnerability on one of Google’s subdomains (https://datastudio.google.com/)

Description

Google Data Studio is a tools for displaying data to make it easier to read. So, you can determine a website development plan or other business strategy more quickly and precisely.
By the way, it looks like Data Studio is now a Looker Studio…

Looker Studio Overview
Unlock the power of your data with interactive dashboards and beautiful reports that inspire smarter business…

datastudio.google.com

Proof Of Concept

After I tried several Requests that I got on Request Burpsuite and also so many that it made me dizzy, I finally got one of the Endpoints that had this IDOR vulnerability.
The one with the vulnerability is “/persistTempReport”

Create Template

The first step I did was go to the “Template” page and then select one of the templates available there.

Press enter or click to view image in full size

After you click on one of these templates you will be directed to the Template page that you will create later, and there is an ID but it is not our Template ID (Maybe it’s like a temporary ID from this Data Studio)

Press enter or click to view image in full size

Before I click “Edit & Share” I enable Intercept on my BurpSuite, And then click “Add to Report”

Press enter or click to view image in full size
Get Request {/persistTempReport}

And I got Request from “/persistTempReport”, and this is where I got this IDOR vulnerability.

Press enter or click to view image in full size

As you can see in the picture above that the previous ID has changed, and this is my ID and the one you will use later like (https://datastudio.google.com/u/0/reporting/[XXXXXXX]/page/qlD/edit)

Press enter or click to view image in full size

And in the picture above this belongs to my 2nd account ID

Found IDOR

In the content of Request “/persistTempReport” there is a parameter named “sourceReportId” which contains our Template ID and we can change it

Press enter or click to view image in full size
ID Template Account {A}

And when I changed the contents of the “sourceReportId” parameter with my 2nd account ID, and it worked!

Press enter or click to view image in full size
ID Template Account {B}
{getReport} and {persistentTempReport}

It doesn’t stop there, after several times I’ve been looking for more requests, I found 1 Request “/getReport” which will have the same response as “/persistentTempReport”

Press enter or click to view image in full size
Request and Response from /getReport

And when I change the contents of my Template ID from “/getReport” it will display the response “PERMISSION_DENIED” and on “/persistentTempReport” no error.

Press enter or click to view image in full size
Permission Denied at getReport
Reference IDOR
Insecure direct object references (IDOR) | Web Security Academy
In this section, we will explain what insecure direct object references (IDOR) are and describe some common…

portswigger.net

Timeline

> 16 Sep 2022 (01:04) : Get IDOR and report to Google
> 16 Sep 2022 (01:13) : Additional Information (Added /getReport and /persistTempReport equations)
> 20 Sep 2022 : Nice Catch! from Google
> 27 Sep 2022 : The VRP panel has decided to issue a reward of $3133.70 for my report.
> 19 Okt 2022 : Fixing by Google

Press enter or click to view image in full size
Follow Me

https://www.linkedin.com/in/c3van/

Get Caesar Evan Santoso’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks!

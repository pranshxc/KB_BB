---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-04_unauthorized-access-to-admin-panel-via-swagger.md
original_filename: 2023-03-04_unauthorized-access-to-admin-panel-via-swagger.md
title: Unauthorized Access To Admin Panel via Swagger
category: documents
detected_topics:
- access-control
- rate-limit
- idor
- command-injection
- path-traversal
tags:
- imported
- documents
- access-control
- rate-limit
- idor
- command-injection
- path-traversal
language: en
raw_sha256: 50fd89ea676fe36ab62703c12bdf9de478969a9f8e475a436f03e88af8cc57a0
text_sha256: 86b3086b4dcfa2e1c5d055cf3e191b5c5553b7622b6ae0e3585f25c61cc36bd6
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized Access To Admin Panel via Swagger

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-04_unauthorized-access-to-admin-panel-via-swagger.md
- Source Type: markdown
- Detected Topics: access-control, rate-limit, idor, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `50fd89ea676fe36ab62703c12bdf9de478969a9f8e475a436f03e88af8cc57a0`
- Text SHA256: `86b3086b4dcfa2e1c5d055cf3e191b5c5553b7622b6ae0e3585f25c61cc36bd6`


## Content

---
title: "Unauthorized Access To Admin Panel via Swagger"
url: "https://m7arm4n.medium.com/unauthorized-access-to-admin-panel-via-swagger-c242e8341045"
authors: ["Arman (@M7arm4n)"]
programs: ["Coca-Cola"]
bugs: ["Missing authentication", "Broken Access Control"]
publication_date: "2023-03-04"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1431
scraped_via: "browseros"
---

# Unauthorized Access To Admin Panel via Swagger

Unauthorized Access To Admin Panel via Swagger
M7arm4n
Follow
3 min read
·
Mar 5, 2023

494

Hi guys, My name is Arman and you know me as M7arm4n. Today I want to talk about how I was able to access the admin panel in Coca-Cola for the 2022 World Cup 🏆

https://bugcrowd.com/coca-cola

The essential part of discovering this vulnerability is continuous RECON, about 1 month before Hunting on this program, I decided to test my private recon tool. So I fired my recon tool on Coca-Cola domains, My tools do subdomain enumeration daily and push results into the database.

After around one month continues recon, Now time to check the results. Around 20/30 subdomains were added during the last month. Before starting deep hunting, I decided to try a mass scan on all new results.

Fuzzing directories of subdomains for sensitive information is one of the most popular methods, but the PowerPoint of this method is your wordlist.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I recommend you build your own wordlist from GitHub and write-ups, even CVEs. Onetime for a hack-the-box machine, faced to a WordPress website whiteout any features. I immediately fuzzed the website with a special wordlist for the WordPress website. As soon as possible I found this endpoint that leads to Local File Inclusion :D

wp-admin/admin-ajax.php?action=duplicator_download&file=..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd

So, Back to our story. I usually do my fuzz with FFUF, I recommend you most of the time fuzzing websites one by one, Anyway in this case I did it all in one :) with the following command:

ffuf -w wordlist.txt:FUZZ -w subdomain.txt:URL -u URLFUZZ -ac -of csv -o result.txt

And for check the result:

cat result.txt | awk -F ',' '{print $3}'

Sometimes the rush of programmers in developing websites to present to the employer makes them forget to consider and implement basic security protocols during development. In this scenario, the programmer was developing a website for the 2022 World Cup, which was a blog model website so that normal users did not have the ability to log in or create an account, and there was only one admin role.

The admin directory was available at /admin, after some tests like directory/file brute force, to try to find the registering endpoint, SQL and LDAP bypass, etc method. I didn’t find anything. Actually, I was sad but I don’t know why I had a kind of feeling that said to me you were able to access the admin panel:)

During the testing admin panel, the fuzzing process was finished as well. I back to the results and figure out I have another important endpoint to check for this website and that was an API Swagger. I immediately open the endpoint and checked functions, all the functions and features were available without authentication and all these are for admin 😍

Press enter or click to view image in full size

The main login admin panel was safe but I think the programmer was updating the API admin panel and was using Swagger for his tests, but he forgot to define authentication for Swagger. Now we have bypassed the admin panel :))

Thank you for following me here, Don’t forget to follow for more write-ups.

https://twitter.com/M7arm4n

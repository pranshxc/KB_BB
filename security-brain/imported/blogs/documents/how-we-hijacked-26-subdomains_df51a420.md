---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-07_how-we-hijacked-26-subdomains.md
original_filename: 2020-05-07_how-we-hijacked-26-subdomains.md
title: How we Hijacked 26+ Subdomains
category: documents
detected_topics:
- cloud-security
- sso
- idor
- command-injection
- rate-limit
- race-condition
tags:
- imported
- documents
- cloud-security
- sso
- idor
- command-injection
- rate-limit
- race-condition
language: en
raw_sha256: df51a420b2c16f2cfbfe98c140ba518e3de409e57f46dba969f523f085cb181d
text_sha256: 89d239f3961ffa77b2283236d9021cc51528abd3d3369c008fc499e16880a5f2
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How we Hijacked 26+ Subdomains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-07_how-we-hijacked-26-subdomains.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, idor, command-injection, rate-limit, race-condition
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `df51a420b2c16f2cfbfe98c140ba518e3de409e57f46dba969f523f085cb181d`
- Text SHA256: `89d239f3961ffa77b2283236d9021cc51528abd3d3369c008fc499e16880a5f2`


## Content

---
title: "How we Hijacked 26+ Subdomains"
url: "https://medium.com/@aishwaryakendle/how-we-hijacked-26-subdomains-9c05c94c7049"
authors: ["Aishwarya Kendle (@aish_kendle)"]
bugs: ["Subdomain takeover"]
publication_date: "2020-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4602
scraped_via: "browseros"
---

# How we Hijacked 26+ Subdomains

Aishwarya Kendle
 highlighted

Top highlight

How we Hijacked 26+ Subdomains
Aishwarya Kendle
Follow
4 min read
·
May 7, 2020

1.3K

4

Press enter or click to view image in full size

In
the midst of the lockdown, I and my friend Prateek Thakare decided to improve our bug bounty skills and this time we focused on a particular bug, reading a lot about it, referring POCs and then automating the vulnerability. We decided to start from Subdomain Takeover and 0xpatrick’s blogs is what we started reading. I’ve seen many blogs regarding subdomain takeover but hardly anyone has mentioned how to find them?
I am writing this blog to talk about our methodology and tools that we used to achieve this.

Subdomain Takeover Basics :

Process of registering a non-existing domain name to gain control over another domain.

Press enter or click to view image in full size
A CNAME record
Subdomains map themselves to a specific IP, 3rd party services like Azure, AWS, Heroku, Github, Fastly, Shopify, etc. to serve the contents. These subdomains use a CNAME record to another domain [eg. xyz.company.com CNAME xyz.cloudservice.com]
Now due to whatever reason, the company decides to stop utilizing this service and to save some bucks, the company cancels the subscription of the 3rd party cloud service provider.
But, the company forgets to update or simply remove the CNAME record in the DNS zone file
Since the CNAME record is not deleted from company.com DNS zone, anyone who registers xyz.cloudservice.com has full control over xyz.company.com until the DNS record is present.
How to find subdomain takeover ?

We followed some steps during this process to perform this scan on a large scale.

I. Gathering RDP domains :

We used Google Dorks to search for companies that have a responsible disclosure program or bug bounty program.

inurl:  /bug bounty
inurl: / security
inurl: security.txt
intext: responsible disclosure
inurl:/security ext:txt "contact"

Once the search results are loaded, we referred this blog to extract the URLs from the page. It contains an Extraction Bookmarklet Code which is nothing but a javascript function that scrapes the URLs present in the google search result.

Extracting URLs from Google’s search page

After extracting the URLs, we stored it in a file called urls.txt. To extract the domain, we used tomnomnom’s unfurl tool .

tomnomnom/unfurl
Pull out bits of URLs provided on stdin If you have Go installed and configured: ▶ go get -u…

github.com

cat alive.txt | unfurl domains >> subs.txt

This will extract the domains and store it in a file called subs.txt

II. Enumerating Subdomains:

During the learning period we tried different subdomain enumeration tools and found out that different tools give varied outputs. Some tools might include a subdomain which the other one may not. So to get the best result, gathering the output of different tools is what we decided to do.

Subdomain Enumeration Script
./enumSubdomains.sh subs.txt

We used the above script to enumerate subdomains using Sublist3r and assetfinder. You can add any other subdomain enumerator tool and combine its output.

III. Checking for takeover:

To check for takeover, there are many different tools available and all of them works similarly: The tool checks for a fingerprint i.e. an error message provided by the cloud service for pages that are expired and are vulnerable to takeover. You can add your fingerprint if you have found a new type of subdomain takeover.

haccer/subjack
Subjack is a Subdomain Takeover tool written in Go designed to scan a list of subdomains concurrently and identify ones…

github.com

Ice3man543/SubOver
But something more awesome will come soon! Subover is a Hostile Subdomain Takeover tool originally written in python…

github.com

We used subjack and it gave the result as follows:

It gave us the subdomains which are probably vulnerable and the cloud service that they are using.

Get Aishwarya Kendle’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Combining the above script with subjack we get :

Subdomain Takeover Script
./subdomainTakeover.sh. subs.txt

Once a subdomain has been identified which is vulnerable, the following repository can be used to view the steps for creating a POC.

EdOverflow/can-i-take-over-xyz
The authors of this document take no responsibility for correctness. This project is merely here to help guide security…

github.com

Some tips that will help you when you encounter a vulnerable subdomain:
The subjack tool sometimes gives a false-positive result.
For more information and POC, refer to 0xpatrick and m7mdharoun blogs.
Make sure you record the POC and then submit the report, we encountered a program who fixed the takeover immediately after reporting and marked our report as an internal known issue 😑️.
Heroku and Azure require a Credit Card to be added to add a custom domain name.
Pantheon requires you to buy a 50 $ basic plan to add a domain name.
We’ve encountered many Fastly pages and couldn’t succeed in hijacking it. But as mentioned by d0xing “most are not vulnerable because they’ve claimed their root domain, but if you setup fastly with a subdomain only and release it, it is vulnerable to takeover”
We used a DigitalOcean VPS which gave us good speed and bandwidth. You can sign up using our referral link to get 100 $ credit for 60 days
Connect with us on :

Twitter : @aish_kendle | @thakare_prateek

Linkedin : Aishwarya Kendle | Prateek Thakare

Well if you loved this write up, drop a clap 👏

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-07_how-i-found-moodle-cross-site-scripting.md
original_filename: 2022-09-07_how-i-found-moodle-cross-site-scripting.md
title: How I found Moodle Cross site scripting
category: documents
detected_topics:
- xss
- oauth
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 3eae47366671f9dbf7836d234b6854cda8adfd1ada49afdfdfaa31cac791ff9f
text_sha256: f90dd59dcbfe1629d8fc75e3d2dc9cc1a62063894451b0e0fa80fd8c8f9b6347
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Moodle Cross site scripting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-07_how-i-found-moodle-cross-site-scripting.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `3eae47366671f9dbf7836d234b6854cda8adfd1ada49afdfdfaa31cac791ff9f`
- Text SHA256: `f90dd59dcbfe1629d8fc75e3d2dc9cc1a62063894451b0e0fa80fd8c8f9b6347`


## Content

---
title: "How I found Moodle Cross site scripting"
url: "https://medium.com/@Parag_Bagul/how-i-found-moodle-cross-site-scripting-459a1c9ad4d5"
authors: ["ParagBagul"]
programs: ["Moodle"]
bugs: ["XSS"]
publication_date: "2022-09-07"
added_date: "2022-09-19"
source: "pentester.land/writeups.json"
original_index: 2201
scraped_via: "browseros"
---

# How I found Moodle Cross site scripting

ParagBagul
Follow
4 min read
·
Sep 7, 2022

61

How I found Moodle Cross site scripting

Hello folks , I’m a Parag Bagul security Researcher and bug bounty hunter

I would like to share the recent successful disclosure of the vulnerability.

as mentioned above its cross-site scripting vulnerability is commonly found in web applications mostly security researchers look for it all the time

#So what is cross-site scripting:

cross-site scripting is a website vulnerability that allows attackers to execute any javascript code on the client and server sides.

#The finding:

I started by roaming around gov.lv website and was looking for cross-site scripting firstly I started subdomain recon

for subdomain recon, I used the command

subfinder -d gov.lv -o domain.txt

This command will find the subdomain of gov. lv and save all of those subdomains will be kept in the domain.txt file

Press enter or click to view image in full size

subfinder extracted a total of 1389 subdomains

Press enter or click to view image in full size

After that, I started the httpx tool to find active subdomains

Press enter or click to view image in full size

httpx tool saved all active subdomains in the active.txt file.

I started waybackurls crawler. the waybackurls is a tool that fetches URLs from the Wayback machine

now all active domains are in the active.txt file.

I started the waybackurls tool on active.txt

cat active.txt | waybackurls > all-domain-crawl.txt

Press enter or click to view image in full size

all fetched URLs were stored in the crawl.txt file but I saw that there are some domains whose URLs were not found in the crawl.txt file

I stored all domains those results were not found in waybackurls crawling that time I decided that I will start my testing on those domains first.

there is one domain in my list called skillslatviamoodle.viaa.gov.lv I started crawling with waybackurls and gau but both did not work 😟

Press enter or click to view image in full size

after this, I started crawling into the burp suite

Press enter or click to view image in full size

after this, I started crawling manually and looking for its feature. in my manual crawling phase I found the following URL

Get ParagBagul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://skillslatviamoodle.viaa.gov.lv/mod/lti/auth.php?redirect_uri=https://exampl.com

that time I decided that I will test open redirect and cross-site scripting here. I started burp suit again and intercepted the request.

https://skillslatviamoodle.viaa.gov.lv/mod/lti/auth.php?redirect_uri=HACKER

Press enter or click to view image in full size

After intercepting the request. send that request in the burp suite repeater and I quickly did click on the send button. and Boom my string is Reflected in Response.

Press enter or click to view image in full size

now slowly I started my cross-site scripting test on this parameter. I added <HACKER> in input but in response, my HACKER input string was not reflected.

Press enter or click to view image in full size

our string did not reflect means there is a filter that blocks less than and Greater-than signs after that, I started a google search about this and also I referred to the Hacker One report of XSS. and i found two resources :)

Glovo disclosed on HackerOne: Moodle XSS on evolve.glovoapp.com
Cross Site Scripting (XSS) / Moodle XSS ** **Summary : ** *Cross-site scripting (XSS) is a type of computer security…

hackerone.com

https://twitter.com/secnhack/status/1400698061832155144

after reading those resources I tried to implement it so first i added XSS payload: javascript:alert(1)

Press enter or click to view image in full size

and yes our output was reflected in the response. after that again I crafted my payload below.

javascript:alert(‘hacked_by_hax_wizard’)

Press enter or click to view image in full size

again payload was reflected in the response. after that i changed hacker string in hacked_by_hax_wizard , I opened the same request in the browser.

Press enter or click to view image in full size

both cross-site scripting payloads worked 😎

javascript:alert(1)

javascript:alert(‘hacked_by_hax_wizard’)

tada !! the below picture gives me a sigh of relief and the efforts are truly appreciated moreover it gives me the adrenaline to report more bugs on the website. follow for more bug Reports.

Letter of Appreciation from Latvia cert

Thank you,

Parag Bagul!!

HaxWizard

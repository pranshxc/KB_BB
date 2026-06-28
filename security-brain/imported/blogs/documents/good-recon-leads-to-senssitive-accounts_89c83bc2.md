---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-15_good-recon-leads-to-senssitive-accounts.md
original_filename: 2022-07-15_good-recon-leads-to-senssitive-accounts.md
title: Good Recon Leads To Senssitive Accounts
category: documents
detected_topics:
- idor
- sqli
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- sqli
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: 89c83bc2b575d233501c2b950cbee3e6bd5bb863a3d3ff05b681115f18072442
text_sha256: be212b46fead70a7624c70515012bb5aefba9d0dd4b8d1be8e613985f692d4dd
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Good Recon Leads To Senssitive Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-15_good-recon-leads-to-senssitive-accounts.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `89c83bc2b575d233501c2b950cbee3e6bd5bb863a3d3ff05b681115f18072442`
- Text SHA256: `be212b46fead70a7624c70515012bb5aefba9d0dd4b8d1be8e613985f692d4dd`


## Content

---
title: "Good Recon Leads To Senssitive Accounts"
page_title: "GOOD RECON LEADS TO SENSSITIVE ACCOUNTS | by Milanjain | Medium"
url: "https://medium.com/@milanjain7906/good-recon-leads-to-senssitive-accounts-a8abb6c21333"
authors: ["Milanjain"]
bugs: ["Information disclosure", "Username enumeration"]
publication_date: "2022-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2447
scraped_via: "browseros"
---

# Good Recon Leads To Senssitive Accounts

GOOD RECON LEADS TO SENSSITIVE ACCOUNTS
Milanjain
Follow
3 min read
·
Jul 15, 2022

160

4

Hello people i have back with new hacking story !! . so yesterday i was hunting on one of the vdp program let’s consider it xyz.com . so let’s hack it !!

Let’s hack

so when i go to my target https://xyz.com I started recon first i start finding subdomains of my target by the using subfinder . and save it in file

subfinder -d xyz.com -o xyz_sub.txt

then i run some tools for finding bugs but i don’t find anything .

then i find waybackurls of my target

cat xyz_sub.txt | waybackurls | tee -a xyz_url.txt

then i found 10K+ urls and i was like

It is very hard to check each url then i think to find some login panels for sql injection …..

cat xyz_url.txt | grep “login” | httpx -mc 200

cat for opening urls files

grep to extract urls who contains login parameter inner them

httpx -mc 200 :- only whose urls who are alive / and on working phase

then i found some urls who but i try sql injection but do’nt work then i found two urls which looks same

https//subdomain/:fileter/status%5D=either&filters%5Buser_login%5D=name

https//subdomain/:fileter/status%5D=either&filters%5Buser_login%5D=name2

then i open the url in first my view i do’nt understand what is this…

then i again open this …

Press enter or click to view image in full size

after some time i found that these are the employees account who translate companies documents . in this account i able able to access every detail about translate and also i am able to see employees details who are they and there name and when they join company . then i think lets try to edit these translates then i found a link you have to login to edit this translation . then i click on the link i found wordpress login panel ..

then i go to login panel who contains username and password .

i have username . but i am not sure it will work then i enter username ( name which i found in url) . boom !! it give me error password is incorrect for this username name . that means user is present in the database i can perform burth force attack to got access !! then i reported it ..

Get Milanjain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

THANKS …

Follow for more ..

INSTAGRAM :-

https://www.instagram.com/m_i_lan___jain/

LINKEDLN:-

Milan Jain - Intern - SISTMR | LinkedIn
View Milan Jain's profile on LinkedIn, the world's largest professional community. Milan has 3 jobs listed on their…

www.linkedin.com

TWITTER

JavaScript is not available.
Edit description

twitter.com

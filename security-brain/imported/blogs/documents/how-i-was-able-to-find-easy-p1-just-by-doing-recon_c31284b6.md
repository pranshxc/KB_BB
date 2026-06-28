---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-22_how-i-was-able-to-find-easy-p1-just-by-doing-recon.md
original_filename: 2020-08-22_how-i-was-able-to-find-easy-p1-just-by-doing-recon.md
title: How I was able to find easy P1 just by doing Recon
category: documents
detected_topics:
- idor
- command-injection
- path-traversal
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- path-traversal
- rate-limit
- api-security
language: en
raw_sha256: c31284b6c4e5c072d694138e348154ff7ada688c2860af0205a13d677eab85fa
text_sha256: d1448552a5c9627e75094a6ecd0b88643cf227c26d12ece7eba0d6db21cdb86a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to find easy P1 just by doing Recon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-22_how-i-was-able-to-find-easy-p1-just-by-doing-recon.md
- Source Type: markdown
- Detected Topics: idor, command-injection, path-traversal, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c31284b6c4e5c072d694138e348154ff7ada688c2860af0205a13d677eab85fa`
- Text SHA256: `d1448552a5c9627e75094a6ecd0b88643cf227c26d12ece7eba0d6db21cdb86a`


## Content

---
title: "How I was able to find easy P1 just by doing Recon"
url: "https://medium.com/@kirtanpatel9111998/how-i-was-able-to-find-easy-p1-just-by-doing-recon-fdef0c689362"
authors: ["Kirtan Patel (@kirtanpatel9111)"]
bugs: ["LFI"]
publication_date: "2020-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4299
scraped_via: "browseros"
---

# How I was able to find easy P1 just by doing Recon

Top highlight

How I was able to find easy P1 just by doing Recon
Kirtan Patel
Follow
2 min read
·
Aug 23, 2020

472

6

To all the readers, this blog post is for beginners, there is nothing special trick here and also this is my first write up, so any suggestions or corrections are always welcomed.

Hello you beautiful people, I will be talking about how i was able to find easy p1(critical) bug just by doing Reconnaissance. i was invited to a private program on bugcrowd, let’s call it “target.com”.

The target had a huge scope(*.target.com). Whenever i see something like “.target.com”, I quickly start subdomain enumeration using multiple tools like Assetfinder, Findomain, Amass ( Always try to run more than two tools).

assetfinder -subs-only target.com

findomain -t target.com

amass enum passive -d target.com

Make simple bash script to automate the process.

After subdomain enumeration I was going through each of subdomains manually. But you can try aquatone to get screenshot of all the subdomains or you can also open all the subdomains in firefox for quick view using this simple bash one liner.

cat subdomains.txt | while read subs; do firefox $subs; sleep 8; done

During this process there were many subdomains i was unable to connect or it gives error. so i thought let’s try port scanning if i may found any other ports(like ftp,ssh or any other) are open for these subdomains. i quickly find ip address of all the subdomains and started nmap scan.

nmap -sV -iL ips.txt -oN nmap_scan.txt

or you can also try “naabu” tool by projectdiscovery. it is much faster than nmap.

cat ips.txt | naabu

By going through results of nmap i have found one subdomain(loadturn002.example.com) has port 5080(OnScreen Data Collection Service) is open. i quickly went to browser and type http://loadturn002.example.com:5080 it gives me error “File no Found” with some server information. I thought let’s try directory bruteforcing. then I fired dirsearch.

Get Kirtan Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

python3 dirsearch.py -u http://loadturn002.example.com -e * -w my_wordlist.txt -t 100 -x 403,404,301

And interestingly found a directory named “/etc/passwd” and i was like…

I opened the browser and type http://loadturn002.example.com:5080/etc/passwd and i got

Press enter or click to view image in full size
Easy LFI :)

Few Takeaways:-

always try to find subdomains as much as you can.
shortlist all the subdomains which feels juicy. Try hidden parameter search, Directory bruteforcing, Port scanning, js fils, CVE search.
Strong and proper recon= sometimes easy win :)

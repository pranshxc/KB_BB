---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-03_elasticsearch-a-easy-win-for-bug-bounty-hunters-how-to-find-and-report.md
original_filename: 2022-08-03_elasticsearch-a-easy-win-for-bug-bounty-hunters-how-to-find-and-report.md
title: Elasticsearch A Easy Win For Bug Bounty Hunters || How To Find and Report
category: documents
detected_topics:
- api-security
- command-injection
- otp
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- api-security
- command-injection
- otp
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: 9922f53f788ea0ea98c9b03cf99ed6ed11dcd20c83421b55fd8d90da55294ba5
text_sha256: ea4cc9be091065c31c62d9f58f7cf7577de4e30803afd0d7c32cf53f393e83a4
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Elasticsearch A Easy Win For Bug Bounty Hunters || How To Find and Report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-03_elasticsearch-a-easy-win-for-bug-bounty-hunters-how-to-find-and-report.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `9922f53f788ea0ea98c9b03cf99ed6ed11dcd20c83421b55fd8d90da55294ba5`
- Text SHA256: `ea4cc9be091065c31c62d9f58f7cf7577de4e30803afd0d7c32cf53f393e83a4`


## Content

---
title: "Elasticsearch A Easy Win For Bug Bounty Hunters || How To Find and Report"
url: "https://tamimhasan404.medium.com/elasticsearch-a-easy-win-for-bug-bounty-hunters-how-to-find-and-report-ddd900395bcb"
authors: ["Tamim Hasan (@tamimhasan404)"]
bugs: ["Information disclosure"]
publication_date: "2022-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2368
scraped_via: "browseros"
---

# Elasticsearch A Easy Win For Bug Bounty Hunters || How To Find and Report

Elasticsearch A Easy Win For Bug Bounty Hunters || How To Find and Report
Tamim Hasan
Follow
5 min read
·
Aug 3, 2022

294

4

Press enter or click to view image in full size
Assalamu Alaikum
peace be upon you

Hello hackers. I hope you are well. I am Tamim Hasan a Security Researcher and Bug Bounty hunter From Bangladesh 🇧🇩. Today I am telling you one of my recent finding which is about Elasticsearch. So let's started.

🔴So What Is Elasticsearch?

I am not going to bore you but here is some necessary information about Elasticsearch

// Elastic search like Mysql database used to hold and query information.
// By default Elasticsearch doesn’t have authentication enabled.
// In Mysql we use column names but in Elastic Search, It uses field names. The field names in the above JSON blob would be id, name, and password.
// Elasticsearch is developed in Java
// Elasticsearch allows you to store, search, and analyze huge volumes of data quickly and in near real-time.
// It uses a structure based on documents instead of tables and schemas and comes with extensive REST APIs for storing and searching the data.

🔴 So for security purposes, we call our target as target.com.

While recon one of my methodology is doing port scanning. And for port scanning, I am not doing full port scanning because it creates a huge noise on target like 65535(ports) × all of your target subdomains and it’s time-consuming too. For that, I do some specific common and useful ports for port scanning on targets. This method I learn from GodFather Orwa. He shares much cool stuff on Twitter so you can follow him. And the ports are

81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672

And the command is

naabu -l live-httpx-target.txt -pf common-ports.txt -ep 80,443 -c 200 -timeout 1500

And suddenly I notice this vault.target.com:9200

As we know 9200 is the default port of Elasticsearch. So when I visit this domain it looks like

Press enter or click to view image in full size

Great, It’s means now I can try to find all the indexes(Databases) that are available. For this I do http://vault.target.com:9200/_cat/indices?v and the output is

Press enter or click to view image in full size

But when I do http://vault.target.com:9200/_cat. It shows me lot’s of paths after /_cat/ like this

Press enter or click to view image in full size

Further investigation I know that they are commonly used Elasticsearch API see here. So you can check one by one manually.

But if you can’t see anything after going to this path http://vault.target.com:9200/_cat/ then you can simple bruteforce there like http://vault.target.com:9200/_cat/bruteforec-here

Press enter or click to view image in full size

If you want to perform a full-text search on the database then you can do

http://vault.target.com:9200/_all/_search?q=users

Press enter or click to view image in full size

Or you can also do bruteforce there with a common important wordlist like token
secret
username
uuid
client
admin
password
error
file
data

etc.

👉Tips: It is good if you put some wordlist related to your target.

After manual analysis, I have enough information for making a report but before making a report, I do another brute force with this wordlist command was

Get Tamim Hasan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

dirsearch -u http://vault.target.com:9200 -w elasticsearch.txt -U -L -C -e json,bak -i 200 and the result was

🔥🔥 Now I have more stuff which I include in my report.

🔴 Now It’s time to talk (shortly) about how you found exposed Elasticsearch

⭐ Manual Part:

# Port Scanner Naabu

naabu -l live-urls.txt -p 9200

Remember It’s better when you search for especially Elasticsearch try with only 9200 ports because I saw sometime when you do full port scan you may miss some open ports though they are open because you are doing 65535(ports) × all of your target subdomains. So it may happen. It’s better if we cross-check that part.

> For that you can use httpx tool for that like

httpx -l live-urls.txt -p 9200 -path /_cat/ -mc 200

# Search Engine

## Zoomeye
site:target.com +port:”9200" +”elastic”
port:9200 +elasticsearch

## Shodan
port:9200 all:”indices” all:”production”/

To find Elastic Kibana
## Google dorks
inurl:/app/kibana
inurl::5601/app/kibana

⭐ Automation Part:

Here is a tool which is collect data from thousands of exposed Elasticsearch or Kibana instances and generates a report to be analyzed.

GitHub - 9oelM/elasticpwn: Quickly collect data from thousands of exposed Elasticsearch or Kibana…
Quickly collect data from thousands of exposed Elasticsearch or Kibana instances and generate a report to be analysed…

github.com

👉 Nuclei Elasticsearch Templates

Search · elasticsearch · projectdiscovery/nuclei-templates
GitHub's search supports a variety of different operations. Here's a quick cheat sheet for some of the common searches…

github.com

👉 Other customs Nuclei Templates for Elasticsearch

https://github.com/c-sh0/nuclei_templates/tree/main/elasticsearch

↪ some cool stuff about Elasticsearch

https://github.com/bontchev/elasticpot
https://github.com/jordan-wright/elastichoney

Impact: Without any kind of authentication an attacker can see much information from elastic search. Also, an attacker can run his custom query on your elastic search and if the word exists attacker easily gets internal information from the elasticsearch. And it may also be possible that an attacker can dump the database too.

Fix: Change the elastic search default port 9200 and Implement authentication so that nobody who is not authenticated can’t see any information.

That’s all for today guys. If you find it useful then do clapt and If I made any mistakes please pardon me and if you have any suggestions/questions let me know. Have a nice day :)

You can follow me on Youtube | Github | Twitter | Linkedin | Facebook

🔴I try to explain easily about misconfigured Elasticsearch and how to find and report it in the Bengali language on my youtube channel. You can check this out here.

✨ Infosec add my writeup on their weekly.infosecwriteups.com. Thank You infosecwriteups.

Press enter or click to view image in full size

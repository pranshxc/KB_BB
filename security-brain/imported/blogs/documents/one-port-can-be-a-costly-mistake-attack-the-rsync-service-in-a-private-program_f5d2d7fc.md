---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-15_one-port-can-be-a-costly-mistake-attack-the-rsync-service-in-a-private-program.md
original_filename: 2023-12-15_one-port-can-be-a-costly-mistake-attack-the-rsync-service-in-a-private-program.md
title: One port can be a costly mistake | Attack The Rsync Service in a Private Program
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: f5d2d7fc1627e02226d23f6b46427031f30cfbcf032552c315a815b5d054ef4b
text_sha256: d5a9f32a498fced4efb4b847aada1262fd8fdcb76b01d98de6a3cea6f6dfe0e9
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# One port can be a costly mistake | Attack The Rsync Service in a Private Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-15_one-port-can-be-a-costly-mistake-attack-the-rsync-service-in-a-private-program.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `f5d2d7fc1627e02226d23f6b46427031f30cfbcf032552c315a815b5d054ef4b`
- Text SHA256: `d5a9f32a498fced4efb4b847aada1262fd8fdcb76b01d98de6a3cea6f6dfe0e9`


## Content

---
title: "One port can be a costly mistake | Attack The Rsync Service in a Private Program"
url: "https://medium.com/@sword0x00/one-port-can-be-a-costly-mistake-attack-the-rsync-service-in-a-private-program-cdbf9ecc650d"
authors: ["Mohanad Hesham (@sword0x00)"]
bugs: ["Rsync", "Missing authentication"]
publication_date: "2023-12-15"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 621
scraped_via: "browseros"
---

# One port can be a costly mistake | Attack The Rsync Service in a Private Program

One port can be a costly mistake | Attack The Rsync Service in a Private Program
Mohanad Hesham
6 min read
·
Dec 15, 2023

--

2

Hello friends,

This is my first write-up, and I will talk about how I gained access to the entire file system in a Private Program at HackerOne. So, grab your cup of tea and join me as we delve into this story.

Table of Contents:
WhoAmI
Before the story and CIDRs
Fingerprinting Phase and Port Scan
Enum and Attack Rsync Service
Some Advanced Tips and Conclusion
WhoAmI:

I am Mohanad Hesham, also known as @sword0x00, a Master’s student in Cybersecurity at uOttawa, and a part-time Bug Bounty Hunter.

Before the story:

Our program was private. So, let’s call it ‘Target, Inc.’ It involved about five wild cards. After using the subfinder tool to gather subdomains and conducting deep reconnaissance on each one, I discovered some bugs (one valid, one duplicate, and one info). After taking a break, I decided to resume my work. This time, I noticed there were CIDR ranges. I asked myself, “Why you are not testing them? Not all assets are usually Web Apps, right?” In my case, the CIDRs were prepared by the program. So, I gathered them in a text file called ‘list_OfCIDRs.txt’ There were approximately 25 CIDR ranges. You can check this blog if your CIDRs are not ready… from here[1]

“CIDR[2] Classless Inter-Domain Routing is a notation for describing groups of IP addresses and is used heavily in various networking configurations”.

Fingerprinting Phase and Port Scan

“After you find your targets assets you need to fingerprint them. The purpose of
fingerprinting[3] is to find out what technologies are running on your target’s assets.
You want to know the technology stacks, version numbers, running services, and
anything else that can be used to identify what’s running on an endpoint”

Press enter or click to view image in full size

My workflow for the fingerprinting phase was active. Essentially, I use Naabu and Wappalyzer for the subdomains, and after that, I go deeper by fuzzing and crawling one by one. However, in CIDRs, I typically use the Masscan[4] tool, because it is very fast in the large and wide Scope.

Press enter or click to view image in full size
fingerprinting phase with some tools

let’s build our main line by masscan:

masscan -p <port_numbers> <one_CIDR_range> --exclude <broadcast_IPs> --banners -oL <output.txt>

<port_numbers>: I did not work on all ports because it is time and resource-consuming. So, I focused on:-

Top 1000 port. (0–1024)
Also, sometimes services can be launched on their default ports, such as 8080, 8433, etc. We don’t need to ignore them. So, I add these ports[5].
Finally, when I saw a default port mentioned in published write-ups or tips that did not exist in my list of ports, I added it manually.

<one_CIDR_range>: Do you remember our ‘list_OfCIDRs.txt’ that contains all 25 lines of groups of IPs? You can use ‘-iL’ for ‘list_OfCIDRs.txt,’ but I prefer to work on them one by one. Let’s suppose that we have:

111.222.333.444/24
44.55.66.77/28
88.99.100.111/26
.
.
.
99.99.99.99/24

$<broadcast_IPs>: it was 255.255.255.255

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

And here we go… here is our main line starting from the first CIDR 111.222.333.444/24 and repeating it, one by one. It takes a lot of time, so be patient if you are not working from a VPS:

masscan -p 8080,8001,3389,8009,1311,2480,4444,4445,3333,4567,5000,5001,5104,5800,7000,7001,7002,8008,8042,8088,8222,8243,8280,8281,8333,8530,8531,8887,8888,8443,8834,9080,9443,9981,12043,12046,16080,18091,10443,18092,1010,1311,2082,2087,2095,2096,3000,3128,4243,4711,4712,4993,5108,6543,7396,7474,8000,8001,8008,8014,8069,8080,8081,8090,8091,8118,8088,8123,8172,8500,8880,8800,8983,9000,9043,9060,9090,9091,9200,9800,12443,20720,28017,0-1024 111.222.333.444/24 --exclude 255.255.255.255 --banners -oL outputOf_111_222_333_444_24.txt

I got a normal result of open ports like 22,80,433, etc… from all these assets, until I found a port it was not common for me !!!!!!!!!!

Press enter or click to view image in full size
this is the output of masscan tool but without the timestamp column.

Once I found it, I put it in my browser, but unfortunately, it wasn’t working.

Press enter or click to view image in full size
Browse on “99.99.99.99:873” …. all these IPs from my mind and it aren’t real

So, I ran my Nmap tool to deep Enum for this port .. by this line:

nmap -sV -sC 99.99.99.99
-sV: This flag enables service and version detection.
-sC: This flag enables script scanning. to gather additional information about hosts and services.
Press enter or click to view image in full size
the result of nmap tool

Here we can observe that there is a SERVICE called rsync.

Enum and Attack Rsync Service

“rsync[6] is an open source utility that provides fast incremental file transfer.”

Once I saw this word, I came here to Medium and searched for rsync exploitation until I found this write-up[7] by 

Nairuz Abulhul
. He talked about “insecure Rsync service and obtaining a shell with SSH”. After I read it, the idea of an RCE vulnerability came to my mind immediately.😈

So, I started to enumerate the Rsync service using the Rsync tool and began listing the available shares:

apt install rsync

“If Rsync[7] returns with the available directories and files without asking for authentication, it means that the service allows anonymous unauthenticated access.”

This line to check Is there any directories or files there :

rsync -a "rsyn://99.99.99.99/"
Press enter or click to view image in full size
As seen in the above screenshot, we got a share name (gentoo) with no authentication needed.

Oops… there’s a word called ‘gentoo,’ but I didn’t know what it meant. Is it the name of a directory or a file or what ?? After some research, I discovered it was the name of a Linux distribution[8], and it was a root directory.🤪

Then, I decided to check the upload permissions, as discussed in the above write-up, by creating an empty file and running the command by rsync source path then the destination path:

touch sword0x00
rsync /root/sword0x00 99.99.99.99::gentoo/etc

But unfortunately didn’t work.

Press enter or click to view image in full size
Why things didn’t work from the first time !!!

I decided to stop and go back to the tool again, starting to understand all options/operators by doing some research. While reading, I said to myself, “I just tried uploading, but what about downloading?” 💡

So, let’s reverse our command:

rsync 99.99.99.99::gentoo/etc/passwd .

rsync <destination> <source>
Our source here is the dot “.” which means the current directory path.

Press enter or click to view image in full size
if you can’t write, read it!

And here we go ,,, we could read the /etc/passwd file.

Panjiki

A threat actor can read config, backups, and sensitive data or we can say “He can read the entire file system”.

The severity here was critical, and therefore, the bounty was also maximum.

Some Advanced Tips and Conclusion:

I intended to include some sources while writing this write-up because I want you to understand how things are tied together. You need to make notes for every tip and try to use them together. So, what if you don’t find any open ports?
If you leave the testing area, you might leave some bugs behind. However, if you like the program or find it exclusive, you need to monitor these CIDRs at least once per day[9]. Sometimes, you may discover the insider team has worked on some services, and you might find yourself accessing things that don’t require authentication. You need to be the first in the hunting race. All you need is a VPS (if you haven’t read these posts[10]), understand what monitoring[11] is, and finally, use this script from my repository[12]. That’s it!

Here is the end of our write-up, I welcome your comments if something isn’t clear, and follow me for the next write-ups soon!

Keep in touch:

Twitter/sword0x00
GitHub/sword0x00
Linkedin/sword0x00

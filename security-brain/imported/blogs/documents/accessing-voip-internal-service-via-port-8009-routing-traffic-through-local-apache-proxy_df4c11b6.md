---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-16_accessing-voip-internal-service-via-port-8009-routing-traffic-through-local-apac.md
original_filename: 2018-12-16_accessing-voip-internal-service-via-port-8009-routing-traffic-through-local-apac.md
title: 'Accessing VoIP Internal service via Port 8009: Routing traffic through local
  Apache proxy'
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- supply-chain
language: en
raw_sha256: df4c11b634dc159335a51cf54ec8d530e2df2445c4bfd487265cd68ee2019c75
text_sha256: e8d3f3d6893424b98e3611fddd698c73f6f49dfa51d3d4f0f558acdd9d0b4941
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing VoIP Internal service via Port 8009: Routing traffic through local Apache proxy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-16_accessing-voip-internal-service-via-port-8009-routing-traffic-through-local-apac.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `df4c11b634dc159335a51cf54ec8d530e2df2445c4bfd487265cd68ee2019c75`
- Text SHA256: `e8d3f3d6893424b98e3611fddd698c73f6f49dfa51d3d4f0f558acdd9d0b4941`


## Content

---
title: "Accessing VoIP Internal service via Port 8009: Routing traffic through local Apache proxy"
url: "https://medium.com/@ahmedasherif/accessing-voip-internal-service-via-port-8009-routing-traffic-through-local-apache-proxy-54a4ff539c5f"
authors: ["Ahmed A. Sherif"]
bugs: ["Information disclosure"]
publication_date: "2018-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5519
scraped_via: "browseros"
---

# Accessing VoIP Internal service via Port 8009: Routing traffic through local Apache proxy

Accessing VoIP Internal service via Port 8009: Routing traffic through local Apache proxy
Ahmed A. Sherif (Batee5a)
Follow
3 min read
·
Dec 16, 2018

73

Hello, this is my first bug bounty write-up and I decided to write it to share the importance of reconnaissance whenever you are beginning to test on a new bug bounty program.

The program is private so I am going to use “example.com” as a reference to the website.

They lately added a wildcard in their scope to all their sub-domains, so I started enumerating sub-domains by Sublist3r. A normal step after that is to do an nmap -sVon the list of extracted sub-domains to check which has open ports and to check the services running and one of them caught my attention.

Nmap scan report for preview.example.com
Host is up (0.20s latency).
Not shown: 995 closed ports 
PORT STATE SERVICE VERSION 
25/tcp filtered smtp 
1300/tcp open h323hostcallsc? 
1720/tcp open h323q931? 
3306/tcp open mysql MySQL (unauthorized) 
8009/tcp open ajp13 Apache Jserv (Protocol v1.3)

Okay so far so good, an open 3306 MySQL port but it won’t let me connect (whitelists IPs). What about that 8009 Port? Apache Jserv? YES!

Apache tomcat by default listens on ports 8005,8009,8080. But what Can I do with it? After some digging I stumbled upon this wonderful article by @Michael_Bielenberg https://ionize.com.au/exploiting-apache-tomcat-port-8009-using-apache-jserv-protocol/ and I quote him:

“ 8009 hosts the exact same functionality as port 8080. The only difference being that port 8009 communicates with the Apache JServ Protocol while port 8080 uses HTTP.”

Okay, how do get that traffic in a readable form so I can access whatever is running on that port? Luckily he didn’t leave that one out as well.

Get Ahmed A. Sherif (Batee5a)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The section below is quoted from that previous article, all credit goes to @Michael_Bielenberg

Step 1: Install the Dependencies

The first line installs the mod-jk package which allows Apache to forward requests to Tomcat using the AJP protocol. It can communication to Tomcat on the local machine or to a remote instance. The second line enables the proxy_ajp module and required dependencies automatically.

apt-get install libapache2-mod-jk
a2enmod proxy_ajp

Step 2: Configure Apache

Next create a configuration file in /etc/apache2/sites-enabled/ which will hold our proxy setup, I’ve named mine ajp.conf.

ProxyRequests Off
# Only allow localhost to proxy requests
<Proxy *>
Order deny,allow
Deny from all
Allow from localhost
</Proxy>
# Change the IP address in the below lines to the remote servers IP address hosting the Tomcat instance
ProxyPass / ajp://192.168.109.134:8009/
ProxyPassReverse / ajp://192.168.109.134:8009/

Now start apache.

systemctl start apache2

Visiting 127.0.0.1 should cause Apache to redirect the request to the specified server in the ajp.conf file using the AJP protocol.

And it surely did.
Press enter or click to view image in full size
VOS3000 (VoIP) Instance on Port 8009

Right at this moment I felt the rush of having access to something that I shouldn’t have access to. I didn’t know what VOS3000 at the beginning but after a quick google about it, I understood it was a VoIP service. Okay lets continue by checking out which Apache Tomcat version this was.

Press enter or click to view image in full size
Apache Tomcat/5.5.15

Apache Tomcat 5.5.15. Well, that is outdated and has numerous amount of vulnerabilities. I also started checking the flow of the VOS3000 service system and it turns out their Invalid authentication redirection is done in javascript. The page loads before I get redirected to the login screen so I got to see things that I am not allowed to.

At this point I stopped everything and reported this issue to not forfeit the bounty for breaking their policy.

Lessons learned:

Reconnaissance is always important, not only in port scanning but in every aspect of bug hunting so don’t ignore it.
If something looks suspicious, dig deeper.

Timeline:

11/12/2018 Discovered and reported the bug

11/12/2018 Bug Triaged

13/12/2018 Bug resolved and Bounty rewarded

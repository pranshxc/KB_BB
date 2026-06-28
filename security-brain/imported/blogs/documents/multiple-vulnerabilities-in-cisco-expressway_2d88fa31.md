---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-14_multiple-vulnerabilities-in-cisco-expressway.md
original_filename: 2022-04-14_multiple-vulnerabilities-in-cisco-expressway.md
title: Multiple Vulnerabilities in Cisco Expressway
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 2d88fa3139ecc9cfc9e90991674919fb2a76ae29b19d0a78f7cce462e0fabfae
text_sha256: 5adf6829063c5dfe827872ea45fd3c8367ef8248e6fd9b08ec6803d174dc9d4b
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Vulnerabilities in Cisco Expressway

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-14_multiple-vulnerabilities-in-cisco-expressway.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `2d88fa3139ecc9cfc9e90991674919fb2a76ae29b19d0a78f7cce462e0fabfae`
- Text SHA256: `5adf6829063c5dfe827872ea45fd3c8367ef8248e6fd9b08ec6803d174dc9d4b`


## Content

---
title: "Multiple Vulnerabilities in Cisco Expressway"
page_title: "Multiple Vulnerabilities in Cisco Expressway :: firefart"
url: "https://firefart.at/post/multiple_vulnerabilities_cisco_expressway/"
final_url: "https://firefart.at/post/multiple_vulnerabilities_cisco_expressway/"
authors: ["Christian Mehlmauer (@firefart)"]
programs: ["Cisco"]
bugs: ["Memory leak", "Exposed administrative interface", "STUN", "TURN"]
publication_date: "2022-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2710
---

#  [Multiple Vulnerabilities in Cisco Expressway](https://firefart.at/post/multiple_vulnerabilities_cisco_expressway/)

2022-04-15 ::  Christian Mehlmauer

Some time ago I stumbled across a [HackerOne report](https://hackerone.com/reports/333419) about abusing Slacks TURN server for proxy functionality inside their internal network. I found this interesting and decided to take a look at our videoconferencing software at work, which happened to be Cisco Expressway. Since there are currently no public tools available, I developed a tool to help others in testing.

You can get the tool over here <https://github.com/firefart/stunner/>

During testing of our Cisco Expressway instance I found 3 vulnerabilities which will be covered in this blog post.

To enable others to test other implementations and products for this kind of vulnerabilities I implemented all protocol related vulnerabilities in [stunner](https://github.com/firefart/stunner/).

Cisco first released the main vulnerability as `medium` serverity and later changed the article to a RTFM one (because it’s no vulnerability if you warn on a page on the internet about the implications of the configuration). Another vulnerability which allowed config dumps with a read only user was also not accepted as a valid bug because they documented in the manual that a config dump can contain sensitive information.

## Protocols⌗

So lets begin with a short explanation what STUN and TURN are. Both are protocols mostly used in Audio and Video conferencing solutions. Some services that use TURN are for example MS Teams, Calls via Slack, Calls via Facebook Messenger and basically every other video conferencing software out there.

Both protocols are well documented on Wikipedia and the referenced blog posts, so this will only be a short overview.

The following link to Censys.io shows how many services out there use those protocols. [Search Results](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.port%3A3478)

## STUN⌗

STUN is defined in [RFC 5389 - Session Traversal Utilities for NAT (STUN)](https://tools.ietf.org/html/rfc5389) and is a protocol for devices behind a NAT Gateway to discover if they are using another IP (NAT) when communicating with a target. It’s basically a protocol that tells you your public ip using a STUN server. This result is then used by other protocols to find the best path to communicate with each other which is heavily used in voice and video installations but does not have any other usefull usecases. The STUN protocol itself uses no authentication and uses UDP on port 3478 by default.

For more information on the STUN protocol have a look at [Wikipedia](https://en.wikipedia.org/wiki/STUN) or the [RFC](https://tools.ietf.org/html/rfc5389) itself.

## TURN⌗

TURN is an extension to the above mentioned STUN protocol to support relaying of UDP packets to targets behind the TURN server. It just defines new Attributes and Methods on top of the already established STUN protocol. TURN is used as kind of a proxy server to single peers where one or more endpoint are behind a NAT. The client can contact the TURN server, request that all UDP packets are forwarded to a target, and if the server is configured correctly, it should only allow forwards to known and trusted IP adresses. After this, the peers have a direct data connection to communicate with each other and the TURN server relays the packets thus the NAT is “bypassed”. This feature is also used in almost all video and voice call systems to route the media traffic from a client to a backend server. Using this technique the client and the backend can both be behind different NATs and still exchange packets which each other.

TURN also implements authentication on top of the STUN protocol so you need a valid username and password which are exchanged via other channels like HTTP to use this protocol.

The TURN extensions to the STUN protocol are defined in [RFC 5766 - Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN)](https://tools.ietf.org/html/rfc5766). [Wikipedia](https://en.wikipedia.org/wiki/Traversal_Using_Relays_around_NAT) also has some more information on the protocol and the basic behaviour.

TURN also uses port 3478 UDP or TCP by default. You can also connect to a TURN server via TCP and initiate a UDP connection to the backend system.
  
  
  client --UDP--> TURN Server --UDP--> target
  client --TCP--> TURN Server --UDP--> target
  

## TURN over TCP⌗

This is another extension to TURN which simply enables TCP traffic to peers instead of UDP traffic.

The extension is defined in [RFC 6062 - Traversal Using Relays around NAT (TURN) Extensions for TCP Allocations](https://tools.ietf.org/html/rfc6062).

TURN over TCP uses port 3478 or 443 by default.
  
  
  client --UDP--> TURN Server --TCP--> target
  client --TCP--> TURN Server --TCP--> target
  

## Vulnerabilities⌗

### CVE-2020-3482 - Relaying of traffic to all endpoints (Cisco Bug ID CSCvt83751)⌗

[Cisco Advisory](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-Expressway-8J3yZ7hV.html)

This is the most critical vulnerability. The included TURN server on port 3478 relays all TCP and UDP traffic without further restrictions to internal ip adresses when enabled. By sending a `Connect` request followed by a `ConnectionBind` request we can specify arbitrary IP addresses like 127.0.0.1 or some other internal IPs. Internal IPs can only by restricted by putting the system inside a restricted DMZ but there seems to be no way to restrict 127.0.0.1 and [::1]. The admin interface for example is available on https://127.0.0.1:7443 and accessible with the use of [stunner](https://github.com/firefart/stunner/) even if it’s not exposed to the internet.

**So if you enable this functionality you create an unrestricted socks proxy inside your internal network.**

This bug is not and will not be fixed by cisco. The easiest would be a configurable target whitelist but according to Cisco they can not implement it because of their product architecture. So if you happen to have a Cisco Expressway with open STUN/TURN ports be sure to have strong admin passwords on your admin interfaces and segregate the devices as much as possible from the rest of the network as you are able to access each IP on each port via the Expressway. I would also suggest to take a look into other products that allow a whitelist to be configured.

You can use the `socks` command of [stunner](https://github.com/firefart/stunner/) to exploit this. This command will start a local socks5 server relaying all traffic via the TURN server to the network behind it. This grants you full TCP access to all internal systems reachable by the server itself. How to get the required credentials and servers is described in the [Example Workflow](https://github.com/firefart/stunner#example-workflow).

There are also two nice blogposts which desribe this feature and how to abuse it:

[How we abused Slack’s TURN servers to gain access to internal services](https://www.rtcsec.com/2020/04/01-slack-webrtc-turn-compromise/) and the corresponding [HackerOne report](https://hackerone.com/reports/333419).

[Vulnerability disclosure – Cisco Meeting Server (CMS) arbitrary TCP relaying](https://www.immunit.ch/en/blog/2018/06/12/vulnerability-disclosure-cisco-meeting-server-arbitrary-tcp-relaying-2/)

### Download of confidential information (Cisco Bug ID CSCvt83753)⌗

Using the vulnerability above and a captured user account from another source, I was able to access the Expressway admin interface on port 7443 as a read only user. It looks like everything is read only as it should be, except the system snapshot page: [https://[::1]:7443/snapshot](https://%5B::1%5D:7443/snapshot). This page allows the download of the current running configuration and also includes all user password hashes which can be cracked offline to gain administrative rights on the system. One file containing the hashes is `mnt\harddisk\snapshot\plugins\tshell\xconfiguration_thsell.txt`. The other files might also contain some internal information.

Cisco did not accept this as a valid vulnerability because the docs say that a configuration dump will contain sensitive information but they said to look into removing the functionality for read only users. The fact that a read only user can dump the whole configuration of the device does not seem to be a problem to cisco 🤷🏻‍♂️.

### Memoryleak (Cisco Bug ID CSCvt83761)⌗

I found a memory leak in the application working like OpenSSL Heartbleed. When initiating a connection you open a `channel` to the TURN server and then send data packets with a special header containing the channel number to the TURN server. The server will check for a valid channel in the header and then forwards all data with the header removed to the target.

The packet including the header looks like this:
  
  
  | channelnumber | length_of_data | data
  

So we send a channelnumber, the length and the data that the TURN server should forward to the target.

If we supply a arbitrary length and a very short data which does not match the length, the server returns the length we requested to the relayed server which contains memory information as it does not check for boundaries.

The maximum value for the length I could get to work was 35510.

So the payload is
  
  
  | channelnumber | 35510 | xxxx
  

and the server sends a lot of memory to the external server.

Cisco did not accept this as a valid security vulnerability because the memory of the leaked data is from the buffer of the previous packet. I could not confirm nor deny this but they also said they look into fixing this.

You can use the `memoryleak` command of [stunner](https://github.com/firefart/stunner/) to test for this vulnerability.

## Testing for these vulnerabilities⌗

To test for these vulnerabilties you need to first grab credentials. These can be captured for example by using a webclient for a meeting solution and by using an intercepting proxy like in <https://hackerone.com/reports/333419>. These credentials are most often short lived but on Cisco Expressway it’s a configured never changing password. You can also grab the credentials for Cisco Expressway using the following script <https://github.com/firefart/stunner/blob/main/scripts/expressway_get_creds.py>. You only need a meeting id which normaly is the telephone number / extension which can be found online (if you get a 401 on the websocket call simply execute the script again). You can often find some valid extensions to use on the main site under a contact page.
  
  
  python3 expressway_get_creds.py --domain https://join.xxx.com --telephonenumber 12345  
  {'turnPort': 3478, 'turnTcpPort': 443, 'turnAddress': 'xx.xx.xx.xx', 'turnUsername': 'admin', 'turnPassword': 'passw0rd!$'}
  

In this case you could run [stunner](https://github.com/firefart/stunner/) the following way:
  
  
  ./stunner range-scan -s x.x.x.x:443 -u admin -p 'passw0rd!$' --protocol tcp
  ./stunner range-scan -s x.x.x.x:3478 -u admin -p 'passw0rd!$' --protocol udp
  

if this yields any hits you can execute one of the following two commands to open a socks proxy:
  
  
  ./stunner socks -s x.x.x.x:443 -u admin -p 'passw0rd!$' --protocol tcp -x
  ./stunner socks -s x.x.x.x:3478 -u admin -p 'passw0rd!$' --protocol udp -x
  

I also described a sample workflow on the [stunner](https://github.com/firefart/stunner/) repos readme over here: [Example Workflow](https://github.com/firefart/stunner#example-workflow).

## Shodan and Censys searches⌗

This searches allow you to identify Cisco Expressway setups. The `Cisco Meeting App` is the webapplication that’s using the TURN server so you can use these apps with a valid telephone number (no password needed to grab the credentials) to grab the TURN server informationen needed for the use of [stunner](https://github.com/firefart/stunner/).

[Shodan - Expressway Servers](https://www.shodan.io/search?query=%22Server%3A+CE_E%22)

[Shodan - Expressway Servers](https://www.shodan.io/search?query=%22Server%3A+CE_C%22)

[Shodan - Cisco Meeting App](https://www.shodan.io/search?query=http.title%3A%22Cisco+Meeting+App%22)

[Censys.io - Cisco Meeting App](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.http.response.html_title%3A+%22Cisco+Meeting+App%22)

[Censys.io - STUN/TURN Servers](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.port%3A3478)

## Additional Links⌗

[Cisco Expressway Admin Guide](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/expressway/admin_guide/Cisco-Expressway-Administrator-Guide-X8-11-4.pdf)

[STUN, TURN and ICE Description from AnyConnect](https://anyconnect.com/stun-turn-ice/)

[What are STUN, TURN and ICE from LiveSwitch](https://developer.liveswitch.io/liveswitch-server/guides/what-are-stun-turn-and-ice.html)

[Advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-Expressway-8J3yZ7hV)

Read other posts

* * *

[ How to build your Dockerhub Images with Github Actions → ](https://firefart.at/post/github_actions_dockerhub/)

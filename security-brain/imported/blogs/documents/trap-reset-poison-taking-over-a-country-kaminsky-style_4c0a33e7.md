---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-29_trap-reset-poison-taking-over-a-country-kaminsky-style.md
original_filename: 2023-11-29_trap-reset-poison-taking-over-a-country-kaminsky-style.md
title: TRAP; RESET; POISON; - Taking over a country Kaminsky style
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- graphql
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- graphql
- api-security
language: en
raw_sha256: 4c0a33e791a2c829f08b5912901ae957312566267ae71e0efa3846dbf40fea9d
text_sha256: 0e9d16b1bd168404b53a63107ddd6af57d7f2887b1c9cdc2cf06dc2b17f7e204
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# TRAP; RESET; POISON; - Taking over a country Kaminsky style

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-29_trap-reset-poison-taking-over-a-country-kaminsky-style.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, graphql, api-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `4c0a33e791a2c829f08b5912901ae957312566267ae71e0efa3846dbf40fea9d`
- Text SHA256: `0e9d16b1bd168404b53a63107ddd6af57d7f2887b1c9cdc2cf06dc2b17f7e204`


## Content

---
title: "TRAP; RESET; POISON; - Taking over a country Kaminsky style"
page_title: "TRAP; RESET; POISON; - Taking over a country Kaminsky style - SEC Consult"
url: "https://sec-consult.com/blog/detail/taking-over-a-country-kaminsky-style/"
final_url: "https://sec-consult.com/blog/detail/taking-over-a-country-kaminsky-style/"
authors: ["Timo Longin (@timolongin)"]
bugs: ["DNS cache poisoning", "Kaminsky attack", "DoS", "Email spoofing"]
publication_date: "2023-11-29"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 661
---

1. [ Home ](/)
  2. [ Blog ](/blog/)
  3. TRAP; RESET; POISON; - Taking over a country Kaminsky style

# TRAP; RESET; POISON; - Taking over a country Kaminsky style

29.11.2023 

A technical deep dive on how to poison the DNS name resolution of an entire country!

![](/fileadmin/_processed_/2/e/csm_sec-consult-h-kaminsky-poison_c3cc60f8fb.png)

_In the course of a research project in collaboration with the SEC Consult Vulnerability Lab, Timo Longin (_[_@timolongin_](https://twitter.com/timolongin) _) discovered an exotic DNS Cache Poisoning vulnerability that could have manipulated the DNS name resolution of an entire country. The exploitation of this issue would have allowed threat actors to cause serious harm, transcending the world of bits and bytes. This blog post gives an in-depth look on all the technical intricacies of the attack and how to TRAP, RESET and POISON a DNS resolver._

In **2021** , Timo's research ["Forgot password? Taking over user accounts Kaminsky style"](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/) showed us how to take over user accounts of web applications via DNS Cache Poisoning attacks.

Then, in **2022** , we looked beneath the DNS iceberg in ["Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style"](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/) and learned how to attack even internal DNS resolvers of hosting providers.

Now, in **2023** , we up the game and compromise the DNS name resolution of an **entire country!**

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-01-DNS.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-01-DNS.png) Figure 1: Simple example of a DNS name resolution of "google.com" 

## **Kaminsky Recap**

Before we dive into the specifics of this attack, let's lay the groundwork by understanding the basics of DNS name resolutions and DNS Cache Poisoning.

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-02-dns-poison.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-02-dns-poison.png) Figure 2: DNS Cache Poisoning theory 

A client (PC, phone, server, etc.) is asking a DNS resolver for the IP address of "google.com" in this example DNS resolution. Since the DNS resolver hasn't cached this record yet, the DNS resolver asks the root authoritative domain nameserver (ADNS), the "com." ADNS, and eventually the "google.com." ADNS for this DNS record. After receiving the record, the DNS resolver caches it for a specific time (time-to-live, TTL), and forwards it to the client. The client now knows that the IP address of google.com is 142.251.39.5.

_But what happens, if an attacker sends a manipulated DNS response to the DNS resolver, before the legitimate response arrives? Shouldn't this work, since we can use IP spoofing on UDP-based protocols like DNS? Also, wouldn't this allow us to poison the cache of the DNS resolver with a manipulated DNS record?_

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-03-spoofed-dns.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-03-spoofed-dns.png) Figure 3: Sending spoofed DNS responses in pre-Kaminsky times 

In theory, yes, this should work and is the basis of **off-path** DNS Cache Poisoning! However, in practice, it's not that simple! To get a better understanding of why an attacker can't just simply poison DNS resolvers, let's take a look at the following diagram:

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-04-spoofed-dns2.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-04-spoofed-dns2.png) Figure 4: Sending spoofed DNS responses in pre-Kaminsky times 

Nowadays, most DNS resolvers use two components to increase the entropy of their queries, a **16-bit random DNS ID** and a **16-bit random UDP source port** , totaling to **32 bits of randomness**. If there is no match of these two values in the query and the response, the response gets discarded. Therefore, an attacker must guess a correct pair of DNS ID and source port for a manipulated DNS record to be accepted by the resolver. This might take a very long time, since 32 bits equal to roughly 4.294 billion possibilities. In the above example the attacker cannot poison the DNS resolver, since the guessed UDP port is incorrect.

However, these 32 bits of randomness weren't always being used for the DNS protocol. Before Dan Kaminsky discovered the [Kaminsky attack](https://www.blackhat.com/presentations/bh-jp-08/bh-jp-08-Kaminsky/BlackHat-Japan-08-Kaminsky-DNS08-BlackOps.pdf) in summer 2008, lots of DNS resolvers were only relying on the 16-bit DNS ID for randomness, which totals to roughly 65000 possible values, making guessing 65000 times easier! 

Like in figure 4, this allowed DNS Cache Poisoning en masse.

Since it's not 2008 and we are living in post-Kaminsky times, simple Kaminsky attacks won't work. Therefore, some very smart researchers developed so-called post-Kaminsky attacks. These attacks leverage ways to decrease the entropy of DNS responses, making them exploitable like in pre-Kaminsky times! 

  * IP fragmentation attacks: In 2012, Amir Herzberg and Haya Shulman discovered a way to split DNS responses in two parts (["Fragmentation Considered Poisonous"](https://doi.org/10.1109/CNS.2013.6682711)) via manipulation of the path MTU between resolver and the ADNS. This allowed an attacker to completely bypass UDP source port and DNS ID randomness, and only requires guessing a 16-bit IP ID.
  * Side-channel attacks: In 2020, Keyu Man et al. discovered a side-channel attack ([SAD DNS](https://www.saddns.net/) attack) on ICMP rate-limits that allowed to infer the used UDP source port of a DNS query. A year later, they found another attack which exploits Forwarding Information Base (FIB) Next Hop Exception (FNHE) cache as a side channel. After they have leaked the source port, a simple Kaminsky attack can be used to poison the DNS resolver.

So, now that we have a good understanding of DNS Cache Poisoning attacks, how come we can poison an entire country?

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-05-target.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-05-target.png) Figure 5: Source port distribution of a yet unknown DNS resolver (created via DNS Analysis Server) 

## **The Target**

After reviewing some of the research results of ["Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style"](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/), a peculiar distribution of UDP source ports stuck out like a sore thumb.

![](/fileadmin/_processed_/7/3/csm_sec-consult-c-poison-kamisky-06-07-request_eb5469af5f.png) Two source port distributions (figure 6, left and figure 7, right) for two different destinations/IPs 

Why is this bad? Well, if the used source ports of a DNS resolver are guessable, as it seems here, the randomness of DNS queries is at about 16 bits. Like described in the previous section, this can be exploited via a Kaminsky attack! This initial excitement was sparked even more, after understanding the purpose of this DNS resolver. **It's serving as a resolver for****millions of people!**

However, the excitement was short-lived, since ,"unfortunately", exploiting this issue is not that simple. In this case, the sequential distribution of source ports is on a per-destination basis, which means that every IP has its own offset. For example, for an ADNS with IP 1.2.3.4 the currently used source port may be 2484, but for an ADNS with IP 5.6.7.8, it is 32201.

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-08dns-cgnapt.png) Figure 8: DNS resolution with intermediate CGNAPT device 

A successful attack would therefore require us to know the current offset for the IP address of the target ADNS (e.g., ADNS of "google.com"). Consequently, **we must find a way to leak the used source port for an arbitrary destination/IP!**

To accomplish such a feat, a good understanding of what we are dealing with is necessary. Analysis of the used source ports revealed that there is a static pool of roughly 3000 ports that are being used in a sequential order.
  
  
  2482, 2483, 2484, 2485, 2486, 2487, 2488, [~3000 other ports], 64536, 64537, 64538, 64539, 64540, 64541, 64542, 64543, 64544

Furthermore, the unnatural distribution of source ports indicates that there is most likely a system between the DNS resolver and the ADNS, which manipulates the source port distribution.

Some research revealed that the steps in the source port distribution (as seen in the above distributions) can be caused by so-called "**port block allocation** ". In this case, it can be attributed to a **carrier-grade network address and port translation (CGNAPT)** device. The scenario that we're dealing with looks somewhat like this:

So, leaking a single source port with these prerequisites is a piece of cake, right? RIGHT?!

Well, easier said than done... Let's take a look at some failed attempts:

**SAD side channels:** As mentioned in the previous chapter, recent papers used side channels in operating systems and network protocols to leak source ports. Even though lots of different methods were tried, the CGNAPT device did not react to any of them.

**IP fragmentation:** The same goes for IP fragmentation based attacks. Lots of different methods were attempted, but as with the SAD methods, the CGNAPT device did not bulge.

**Time-based side channels:** The idea behind time-based side channels is to cause a measurable time delay on the currently used sequential source port. For example, we can send loads of UDP packets on the assumed open port, which would pass the CGNAPT device and hit the DNS resolver. This could lead to a tiny overload and may be noticeable in the response time when querying the DNS resolver. However, even a big number of UDP packets (including fake DNS responses) did not create a delay.

Even though a lot of the approaches seemed promising at first, none of them reaped the desired results. Just before all hope was lost, a crucial piece of information was uncovered.

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-09-simplified-attack.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-09-simplified-attack.png) Figure 9: Simplified attack scenario in "Security of Patched DNS" 

## **TRAP;**

In 2012, Amir Herzberg and Haya Schulman published a paper called ["Security of Patched DNS"](https://doi.org/10.1007/978-3-642-33167-1_16), which includes a number of post-Kaminsky attacks that achieve source port de-randomization. One of them is called "**Trap-then-Poison for Random Ports Allocation** ". In this attack we assume the following scenario (figure 9).

  1. The zombie client sends UDP packets to the ADNS (i.e., google.com with IP address 1.2.3.4) on port 53, until every port mapping in the CGNAPT device is used.
  2. Then, the attacker sends a UDP packet on port 666 to the CGNAPT with the source IP address of the ADNS (1.2.3.4). This packet reaches the zombie client, which allows it to deduct the used port mapping in the CGNAPT device.
  3. Now, the zombie client again sends UDP packets to the ADNS on port 53 but skips over port mapping 666. After some time, the mapping for port 666 times out, while every other port mapping constantly gets refreshed by the zombie.
  4. The zombie client now sends a DNS query to the DNS resolver for "www.google.com". Since source port 666 is the only available port for IP 1.2.3.4 on UDP port 53, the source port of the DNS query is translated to 666.
  5. By using a source port known to the attacker, the entropy of the request decreases to 16 bits, which can now be exploited with a Kaminsky attack!

[![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-10-procedure.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-10-procedure.png) Figure 10: Port blocking via spoofed UDP responses 

However, all of this cannot be directly applied to our situation, since we are not in the same local network as the DNS resolver. Still, we can use the general idea of source port exhaustion to our advantage!

In the paper, the zombie client is blocking port mappings and leaving a specific one open/trapped, which can then be used for a Kaminsky attack. We don't have that luxury, but we can use a little trick. Instead of a client blocking UDP ports by repeatedly sending UDP packets, we can do it with a server.

Therefore, whenever the DNS resolver sends a query, we can hold the used UDP port mapping in the CGNAPT device open, by repeatedly sending UDP packets to the port.

Now, to better understand how the CGNAPT device's port allocation works, we use this method to block all 3000 static ports for the IP address of our test ADNS (demo-admin.ga). As described above, we do this by continuously sending UDP packets (about every 10 seconds for each port) with a spoofed source IP address to all of the static ports used by the CGNAPT. By querying the DNS resolver 3000 times for names that get resolved at the test ADNS (wfo1dl.demo-admin.ga, k3aup.demo-admin.ga, etc.), all available ports should have been used at least once for the test IP address. If this is the case, some CGNAPT devices stop working entirely, and no more connections to the specific IP are possible. Therefore, a DNS resolver could be blocked from resolving a specific domain! However, in this case, the CGNAPT device starts to assign source ports at random and doesn't seem to be bothered by blocking all of the ports. 30 seconds after we stop sending UDP packets, UDP port mappings get removed in the CGNAPT device.

So, how can we exploit this?

## **RESET;**

The simplest solution would be trapping a specific set of ports by leaving them unblocked. This would significantly decrease the source port randomness (e.g., only 10 possible ports) and allow Kaminsky attacks. However, since a port mapping persists for 30 seconds, ports cannot be reused for this time. Therefore, a pool of ports large enough to bypass this timeout must be used, which in this case would be too large to gain an actual Kaminsky advantage (e.g., a pool of 2000 ports). Furthermore, the order of the port assignment became unstable as more ports were left unblocked. This brings us to the RESET part of this blog post!

After tinkering around with CGNAPT devices, the solution hid behind the following questions.

_What happens with the sequential port block allocation, after blocking and then unblocking all the ports? Where does the port sequence start off?_

With these questions in mind, we should be able to manipulate the CGNAPT device's port block allocation to use source ports of our liking!

  1. At first, we trap 10 ports, leaving around 2990 ports blocked.
  2. Then, we use the DNS resolver to query a name of the test ADNS. This forces the CGNAPT device to use one of the trapped ports, RESETTING the port block allocation.
  3. Furthermore, we stop blocking ports.

What do we end up with? A sequential port block allocation that starts at one of the 10 ports that we know!

To get a better understanding of how this works, we trap the ports 2483 to 2493 in the following demo. The first 3000 requests show how sequential port blocks are used as source ports. After all the ports are blocked, random ports are used. When we stop sending queries to the DNS resolver, we can observe how the port block allocation is reset.

###  Trapping and resetting ports from the perspective of a test ADNS 

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_11/sec-consult-c-poison-kamisky-10-procedure.png) Figure 11: Kaminsky attack procedure 

## **POISON;**

Since we've achieved our goal of "leaking" the currently used sequential source port, we can start with the Kaminsky attack.

The procedure to poison the A record of "test1234.demo-admin.ga" via the "**w11 method** ", as described in the paper ["Internet-wide study of DNS cache injections"](https://doi.org/10.1109/INFOCOM.2017.8057202), works as follows (figure 11).

  1. The attacker sends a DNS request for an A record of a random subdomain of “test1234.demo-admin.ga” (e.g., “sf5ldi.test1234.demo-admin.ga”) to the DNS resolver.
  2. Since the random subdomain “sf5ldi.test1234.demo-admin.ga” is not yet cached in the resolver, it sends a DNS request to the ADNS of “demo-admin.ga”.
  3. The CGNAPT device receives the DNS request and overwrites the UDP source port with one of the first 10 possible incremental source ports.
  4. The “demo-admin.ga” ADNS receives the request and returns a DNS response. While this is happening, the attacker continuously sends a barrage of malicious DNS responses with varying DNS IDs on the 10 possible ports with the source IP address of the “demo-admin.ga” ADNS. The DNS response contains the following entry in the NS section: 
  
  test1234.demo-admin.ga IN NS ns1.demo-attacker.ga

  5. The DNS resolver receives a malicious DNS response of the attacker with the correct port and DNS ID, before it receives the legitimate response. The DNS resolver caches the malicious entry returned by the attacker.
  6. The DNS resolver returns the manipulated response.

If this procedure fails to poison the “test1234.demo-admin.ga” subdomain in the first run, we can repeat it indefinitely by incrementing the source-port guess by 1.  
After we manage to point “test1234.demo-admin.ga” to the attacker ADNS “ns1.demo-attacker.ga”, every DNS request for “test1234.demo-admin.ga” or a subdomain of it gets delegated to the attacker nameserver. The “dig” command can be used to confirm that the cache poisoning worked.
  
  
  $ dig @RESOLVER_IP test1234.demo-admin.ga
  ; <<>> DiG 9.16.15-Debian <<>> @RESOLVER_IP test1234.demo-admin.ga
  ; (1 server found)
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43612
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 1232
  ;; QUESTION SECTION:
  ;test1234.demo-admin.ga. IN A
  ;; ANSWER SECTION:
  test1234.demo-admin.ga. 86400 IN A 1.2.3.4
  ;; Query time: 320 msec
  ;; SERVER: RESOLVER_IP#53(RESOLVER_IP)
  ;; WHEN: Tue Jan 17 12:58:34 EST 2023
  ;; MSG SIZE rcvd: 67
  

## **The Impact**

After all that, what can we actually do?

**Denial of Service (DoS):** At the very least, we can bend DNS resolutions to invalid targets. Want to access www.google.com? Too bad, it's now pointing to 127.0.0.1.

**Traffic redirection:** Redirecting traffic to an attacker server can be more or less effective depending on the context. Nowadays, with lots of services using and enforcing TLS, Man-in-the-Middle (MitM) attacks may not allow a lot of room to play with. This is especially the case for web applications. However, other fields like e-mailing are not as advanced in terms of TLS and certificate verification. As shown in our previous blog post ["Forgot password? Taking over user accounts Kaminsky style"](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/), this allows us to redirect e-mails to our attacker server.

**E-mail spoofing:** SPF, DKIM and DMARC are mechanisms for e-mail authenticity that are all based on DNS. Therefore, manipulating the DNS resolution of a receiving e-mail server allows us to spoof arbitrary sender domains.

**Bypassing domain verification:** Certificate authorities (CAs) sometimes fully rely on DNS to verify the ownership of a domain. Manipulating the DNS resolution of a CA potentially allows us to issue certificates for arbitrary domains. This was also shown in ["Domain Validation++ For MitM-Resilient PKI"](https://doi.org/10.1145/3243734.3243790) by Markus Brandt et al. in 2018.

However, this only scratches the surfaces. More DNS-based attacks might be possible depending on the context.

Bottom line: **You don't want a country-wide DNS fallout!**

## **Conclusion**

Even 15 years after Dan Kaminsky revealed the Kaminsky attack, DNS is still a critical and sometimes vulnerable part of Internet infrastructure. From time to time security researchers demonstrate the inherent issues carried by this ancient protocol. With our "**TRAP; RESET; POISON** " attack, we again shed light on one of the many aspects that must be considered when securing the DNS protocol. Even though attacks on (CG)NAPT devices in combination with DNS are known since 2012, we assume that many more DNS setups are affected. The challenge of identifying (CG)NAPT devices suggests that what we've seen might only scratch the surface. But this is research for another day!

This concludes the third installment of the "Kaminsky style" series. In the next part, we may even poison the entire planet!

 _This research was done by Timo Longin and published on behalf of the[SEC Consult Vulnerability Lab](https://sec-consult.com/vulnerability-lab/)._

##  FAQ 

What's the name of the affected country? 

We are not allowed to disclose the affected country. However, the used infrastructure was generally very advanced, which made the vulnerability even more unexpected. The vulnerability got patched promptly!

That was an interesting blog post, where can I read more about DNS attacks? 

You can find more interesting DNS attacks in ["Forgot password? Taking over user accounts Kaminsky style"](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/) and ["Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style"](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/). Also, we've published [a ](https://sec-consult.com/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/)[DNS Analyzer extension for Burp Suite](https://sec-consult.com/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/)!

How can I get started with DNS vulnerability research? 

If you want to go hunting for DNS vulnerabilities as well, you can use the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server) for some in-depth analysis, or the [DNS Analyzer](https://sec-consult.com/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/) for some light-weight analysis of web applications directly in Burp Suite!

What about DNSSEC and other security features? 

Even though security features like DNSSEC and DNS cookies would have prevented this attack, they are often not used/enforced on resolvers as well as on authoritative nameservers.

So, I'm running a DNS resolver. What can I do to stay secure? 

Well, one good starting point involves configuring DNS resolvers according to established best practices, as shown by [Google](https://developers.google.com/speed/public-dns/docs/security) and [DNS flag day](https://dnsflagday.net/2020/#action-dns-resolver-operators). Furthermore, when operating huge DNS resolvers, pentesting might not hurt.

How long did this research take? 

After roughly 100 hours a stable exploit for DNS Cache Poisoning was developed.

Can similar attacks be launched against victims behind a consumer NAT device? 

We haven't tried yet, but most likely yes!

###  Are you interested in working at SEC Consult? 

SEC Consult is always searching for talented security professionals to work in our team.  

[ More Information ](/career/)

##  More On The Topic 

### [DNS Analyzer - Finding DNS vulnerabilities with Burp Suite](/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/ "DNS Analyzer - Finding DNS vulnerabilities with Burp Suite")

[![Analyzing web applications via Burp Collaborator & DNS Analyzer](/fileadmin/_processed_/4/0/csm_sec-consult-h-Burp_Collaborater_fe23fcf919.png)](/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/ "DNS Analyzer - Finding DNS vulnerabilities with Burp Suite")

26.06.2023 research

A brand-new Burp Suite extension for discovering DNS vulnerabilities in web applications.

[ Read more ](/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/ "DNS Analyzer - Finding DNS vulnerabilities with Burp Suite")

### [Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

[![](/fileadmin/_processed_/0/8/csm_sec-consult-h-iceberg_c4d1557faf.jpg)](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

06.10.2022 vulnerability

Hidden DNS resolvers and how to compromise your infrastructure 

[ Read more ](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

### [Forgot password? Taking over user accounts Kaminsky style](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

[![](/fileadmin/_processed_/5/0/csm_sec-consult-h_pwd_dns_image_1_en_675bb23e07.png)](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

21.07.2021 

The "Forgot password?" feature and how DNS vulnerabilities may allow the takeover of user accounts. 

[ Read more ](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

####  About the author 

![Portrait of Timo Longin SEC Consult](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/Authors/a-TLO.png)

Timo Longin  
SEC Consult  
Senior Security Consultant  

Timo Longin (also known as Login) is a senior security consultant at SEC Consult at day and a security researcher at night. Aside from everyday security assessments, he publishes blog posts and security tools, holds talks at conferences and universities, and has a passion for CTFs. As a well-rounded offensive security researcher, he tries to find forgotten and new exploitation techniques that make the unthinkable possible!

[ Back ](/blog/)

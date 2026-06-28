---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_zimbra-email-stealing-clear-text-credentials-via-memcache-injection.md
original_filename: 2022-06-14_zimbra-email-stealing-clear-text-credentials-via-memcache-injection.md
title: Zimbra Email - Stealing Clear-Text Credentials via Memcache injection
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
- sqli
- password-reset
- mfa
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
- sqli
- password-reset
- mfa
language: en
raw_sha256: 2591e461abda9d1aee5347c04565e08bb6609ded89376c92117546079764f0ce
text_sha256: 2cdf4f8c7af7424f1c5744025d0fbafeb48da57689b4492c1a3190a9c450e8bf
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Zimbra Email - Stealing Clear-Text Credentials via Memcache injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_zimbra-email-stealing-clear-text-credentials-via-memcache-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain, sqli, password-reset, mfa
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `2591e461abda9d1aee5347c04565e08bb6609ded89376c92117546079764f0ce`
- Text SHA256: `2cdf4f8c7af7424f1c5744025d0fbafeb48da57689b4492c1a3190a9c450e8bf`


## Content

---
title: "Zimbra Email - Stealing Clear-Text Credentials via Memcache injection"
page_title: "Zimbra Email - Stealing Clear-Text Credentials via Memcache injection | Sonar"
url: "https://www.sonarsource.com/blog/zimbra-mail-stealing-clear-text-credentials-via-memcache-injection/"
final_url: "https://www.sonarsource.com/blog/zimbra-mail-stealing-clear-text-credentials-via-memcache-injection/"
authors: ["Sonar (@SonarSource)"]
programs: ["Zimbra"]
bugs: ["Memcache injection", "CRLF injection"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2554
---

## TL;DR overview

  * Sonar researchers discovered a Zimbra vulnerability where memcache injection allows attackers to steal clear-text credentials by poisoning the cached authentication data.
  * The attack exploits insufficient input sanitization in Zimbra's memcache protocol handling, enabling an attacker to inject commands that redirect credential storage to an attacker-controlled key.
  * Clear-text credential theft gives attackers direct access to email accounts without triggering password reset alerts or multi-factor authentication challenges.
  * Zimbra administrators should patch immediately; the finding highlights the security risks of using memcache without proper input validation in authentication-critical code paths.

Zimbra is an enterprise-level email solution, similar to Microsoft Exchange. It comes with mail servers, load balancing features, a powerful web interface, and more. According to the vendor's website, it is used around the globe by over 200,000 businesses, universities, and financial & government institutions where users log in to their Zimbra mail account to read and send private emails. 

We discovered a vulnerability in Zimbra that allows an attacker to steal the login credentials from users of a targeted Zimbra deployment. With the consequent access to the victims’ mailboxes, attackers can potentially escalate their access to targeted organizations and gain access to various internal services and steal highly sensitive information. With mail access, attackers can reset passwords, impersonate their victims, and silently read all private conversations within the targeted company. Just a few months ago, Volexity published [research](https://www.volexity.com/blog/2022/02/03/operation-emailthief-active-exploitation-of-zero-day-xss-vulnerability-in-zimbra/) on a 0day vulnerability being used to target Zimbra instances, in particular those deployed by government institutions. In their blog post, they mention that it is likely that a state actor was behind the attacks. 

This blog post describes a new vulnerability that allows an unauthenticated attacker to steal cleartext credentials from a Zimbra instance without any user interaction. We will learn how Memcache Injection vulnerabilities work and how attackers can exploit them. Due to the severity of this issue and previous exploitation of Zimbra instances, we urge Zimbra users to upgrade their installations immediately.

## Impact

The following video demonstrates how an unauthenticated attacker can steal the password of a known user of a targeted instance. The vulnerability triggers the next time the victim uses a mail client to connect to their organization’s Zimbra server.

Zimbra - Stealing a victim's password

We verified that the code flaws (CVE-2022-27924) are present in both the 8.8.x and 9.x branches of Zimbra, affecting both the open-source and commercial versions. The code flaws affect Zimbra’s Reverse Proxy and can be exploited with default configurations by an unauthenticated attacker. The fixed versions are respectively 8.8.15 with Patch level [31.1](https://wiki.zimbra.com/wiki/Zimbra_Releases/8.8.15/P31.1) and 9.0.0 with Patch level [24.1](https://wiki.zimbra.com/wiki/Zimbra_Releases/9.0.0/P24.1)..

As detailed later in this blog post, there are two strategies that attackers could use to exploit this vulnerability: The first strategy requires the attacker to know the email address of victims to be able to steal their login credentials. Typically, an organization uses a pattern for email addresses for their members, such as `{firstname}.{lastname}@example.com`. A list of email addresses could be obtained from OSINT sources such as LinkedIn.

The second exploitation technique exploits “Response Smuggling” to bypass the restrictions imposed by the first strategy and allows an attacker to steal cleartext credentials from any vulnerable Zimbra instance without requiring any knowledge about the instance. Both strategies require no user interaction.

## Technical Details

In the following sections, we provide a high-level overview of Zimbra's architecture. Although the root cause of the security issue lies in the source code, an understanding of the setup is necessary to understand the vulnerability and how an attacker might exploit it.

### Background - Zimbra Proxy

By default, the Zimbra installation script installs all necessary services on a single server. Additional backend servers can be easily added to distribute the workload of heavy email exchange.

In order to manage this load balancing feature, Zimbra uses Nginx as a Reverse Proxy to receive all incoming HTTP and Email (IMAP & POP3) traffic and forward it to one of the registered backend servers. Due to Zimbra's architecture, Nginx's default behavior of forwarding requests to backend servers in a round-robin fashion is not sufficient. The reason for this is that the data stored on different backend servers might not be mirrored on all servers and different backend servers are responsible for different users.

To tackle this problem, Zimbra's developers maintain a [modified version of Nginx](https://github.com/Zimbra/nginx/tree/zimbra/develop), as well as [custom Nginx modules](https://github.com/Zimbra/packages/tree/develop/thirdparty/nginx/zmmodules). These customizations ensure that Nginx forwards traffic sent by a specific user to the correct backend server. 

The correct routing is achieved via the  _Zimbra Lookup Service_. When Zimbra's Reverse Proxy receives a connection (1), it attempts to identify the user making the request through various methods. One example of this is extracting the user from certain URLs. When an incoming HTTP request is made to the example URL `https://example.com/service/home/`**exampleUser**`/file`, the user `exampleUser` is identified. 

Zimbra's Nginx then (2) makes an HTTP request to the internal Zimbra Lookup Service and asks it for the correct backend server for this user. This service then replies with an IP and Port, to which the incoming traffic is then forwarded (3).

The following graphic illustrates this process:

![Zimbra Route determination flow](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5d7f0e9e-3c91-45ae-a73d-4802fd779e6e/body-709c1b93-06fc-43d5-b2e9-07077eded221_Fig1%2BnoPad%2BZimbra%2BFull%2BChain%2B%25402x.png)

It is important to note that this process takes place even if there is only one backend server registered and the result will always be the same. Hence, the vulnerabilities can be exploited even when no additional servers were added.

### Background - Route Caching with Memcached

In the previous section, we described how Zimbra's Reverse Proxy makes an HTTP request to the Zimbra Lookup Service for every connection it receives, before forwarding the traffic to the correct backend service. 

As this extra HTTP request is expensive on performance, the result is cached per user by a Memcached instance. Before making the HTTP request to the Lookup Service, the cache is checked for an existing route. If a cache entry exists, the Lookup request is skipped.

Memcached is a server that stores key/value pairs that can be set and retrieved with a simple text-based protocol.

Let's continue the previous example of `exampleUser `making an HTTP request. Once the right backend server has been fetched from the Zimbra Lookup Service, the backend server's address is added to the cache by sending the responsible Memcached service the following message:

![The add command for Memcache](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4d16ffd1-bf44-45b6-8061-aa1fdcd0934a/body-970fed86-a79c-48d1-b004-185239416e07_1.png)

The snippet above shows that the `add `command was used to set the key `route:proto=httpssl;user=exampleUser@example.com`. The following graphic explains different message parts of the Memcached message that was sent:

![Memcache message breakdown](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f3a08c9b-edda-40fa-8942-222245e18a7c/body-c8571688-fb71-4462-b26e-609d381e7a65_Fig2%2BnoPad%2BZimbra%2BFull%2BChain%25402x.png)

Please note that we explicitly use `(\r\n)` to indicate new lines in Memcache example messages, as they are important to understand the following vulnerability.

The server then responds with a simple message to signal the Memcached client, in this case, Zimbra's reverse proxy, that the store was successful:

![Stored reply](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/36453799-356f-4c5b-8f6e-3ed4814da244/body-3c1bea06-66a1-4954-a7e2-5d130f1872c7_2.png)

After this data was added to the cache, Zimbra's Reverse Proxy attempts to fetch it every time the `exampleUser `makes an HTTP request. To do so, it would send the Memcached server the following message:

![fetching a route](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/dadb3e29-ba05-4f97-ae5b-9eb078f32e13/body-a07e96c3-d48e-49d1-be23-9059477dfc3c_3.png)

The Memcached server would then send the following reply:

![A route value reply](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0ca22209-9a8c-4532-9716-63d561c37770/body-14f7a859-6efe-4cf2-be9d-cb6cc935be0b_4.png)

We can see how the key of the cache entry is predictable. It follows the format `route:proto=`**PROTOCOL**`;user=`**EMAIL**. The protocol could be `httpssl`, `imap `or `pop3`. We will discuss the two latter options later.

### Vulnerability (CVE-2022-27924) - CRLF injection in Memcached lookups

Memcached uses a text-based protocol that interprets incoming data line by line. This means that if an attacker would be able to inject newline characters into the username of Memcached lookups, they could execute malicious Memcached commands.

In the previous sections, we described how an HTTP request to the URL `https://example.com/service/home/`**exampleUser**`/file` leads to the following Memcached lookup:

![a route lookup](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/9a81dbae-6728-42d0-8116-11a6267600de/body-8221b971-09d6-427b-a554-e53d6371b417_5.png)

What happens if the URL contains newlines, followed by an injected command? Let's assume an attacker were to craft the following URL (not encoded for clarity):

![A stats injection](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4a52dc48-2ce5-4f4d-9b93-a9b064630230/body-b9e967ed-23f9-471d-b5c3-659d1bb7e564_6.png)

As newlines were in fact not escaped prior to constructing Memcached lookups, the following data would be sent to the Memcached server by Zimbra's Reverse Proxy:

![stats injection request](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c5cb4ee2-5649-40e2-b729-597bf073da53/body-3d671d32-3157-4d0e-b711-55417ea6f5b7_7.png)

The server then processes the input line by line and would respond with the following data:

![stats injetion reply](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/106d7570-5c88-4d4d-adda-4613c4fd6d4c/body-1d8c21e7-c2e8-4c39-b6ac-d302afb2d663_8.png)

The first line of the response contains `END(\r\n)` to indicate that the `get `command failed as the `route:proto=httpssl;user=example` key was not present. On the next line, Memcached responded with various runtime statistics as a response to the injected `stats `command. The last line indicates an error to the `User@example.com` string, which was on its own line but does not represent a valid command.

The example above demonstrates how attackers can execute arbitrary Memcached commands, of which a [documented list](https://lzone.de/cheat-sheet/memcached) exists. Most importantly, an attacker can create and overwrite arbitrary cache entries, given they know the key they want to overwrite. This is achieved by injecting an `add `or `set `command.

#### Stealing cleartext credentials of known users

In the previous sections, we have seen how attackers can overwrite cache entries in the Memcached instance of a targeted Zimbra installation. In order to understand how an attacker would exploit this vulnerability, we needed to find out which cache entries could be overwritten and what security impact this might have on a targeted Zimbra instance.

Route cache entries turned out to be interesting targets to be overwritten as the route keys are predictable. We have previously seen how the `exampleUser`'s route is cached with the key `route:proto=httpssl;user=exampleUser@example.com`. Here, the protocol is `httpssl`, as the user was identified through the request URL of an HTTP(s) request. Then, the `exampleUser@example.com` string follows. The username is predictable as we control it. `example.com` is derived from the Host header that was part of the same HTTP request.

We mentioned earlier that Zimbra uses Nginx to proxy IMAP and POP3 traffic as well. With all of this in mind, we realized an attacker could overwrite the IMAP route cache entries for any known user of a targeted installation, for example by making the following HTTP request:

![malicious URL](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/51cf848c-9026-4114-995b-dc15d843165f/body-4be3670d-70cc-41e0-81e1-cc435b254918_9.png)

As a result, the following message would have been sent to the server:

![route injection](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ba72cd16-2ca0-447b-aa70-5cde302a0b88/body-578d9f9f-1977-4e34-841c-ad870492328f_10.png)

As a result of this cache poisoning, the next time the `victim@example.com` user would connect to their Zimbra instance via IMAP, the Nginx Proxy would use the poisoned value and forward all IMAP traffic to an attacker-controlled server. Consequently, clear-text credentials are forwarded to the attacker's server.

All of this happens in the background without the victim user knowing. Usually, Mail clients such as Thunderbird, Microsoft Outlook, the macOS Mail app, and Smartphone mail apps store the credentials that the user used to connect to their IMAP server on disk. When the Mail client restarts or needs to re-connect, which can happen periodically, it will re-authenticate itself to the targeted Zimbra instance.

Organizations usually have a naming convention for email addresses for their members, for example, `{firstname}.{lastname}@company.tld`. If an attacker conducting targeted attacks can get a list of members of an organization, for example by using a source such as LinkedIn, they could poison the caches for all known users and wait until the next time their email clients reconnect to the targeted company's Zimbra instance. They would then be given a list of cleartext credentials.

#### Memcache response injection to steal arbitrary credentials

In the previous section, we demonstrated how an attacker can steal the username and password of users of a targeted Zimbra instance by poisoning their IMAP route cache entry. 

However, for this attack to succeed, the following requirements must be met: (1) An attacker has to know the email addresses of one or multiple victims to be able to poison their cache entries and 2) the victims have to actually use an IMAP client. Zimbra ships with a web client that bypasses the Proxy route lookup and directly talks to the backend server, thus no credentials could be stolen. Although we think that it is very reasonable to assume that in an organization with hundreds of members at least a subset of users uses a mail client (including those installed on phones), the users the attacker knows about might not use them.

An attacker can exploit Zimbra's Memcached client in an interesting way to bypass these restrictions and steal credentials from any user utilizing an email client.

By default, Zimbra uses 4 worker processes to handle incoming connections. In a default configuration, each worker process can handle 10240 connections. A connection slot might be filled with an HTTP request or an IMAP or POP3 session. 

What caught our attention was the fact that Zimbra's Nginx established one connection to the Memcached server per process and not per user connection. 

In the underlying code, whenever a worker thread handling a user connection needs to fetch a cache entry from Memcached, the thread sends the message to the Memcached server via the shared socket and then enqueues a work item in a queue that is shared across all threads of a worker process. 

Let's assume that there are concurrently 3 users (`A`, `B`, and `C`) whose route lookup is in the work queue. Once the Memcached server processed all 3 lookups it sends the results for the three lookups back to the client. We can illustrate this state with the following image:

![valid workqueue](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/e4952040-fdb2-4952-84c1-45d382c2e9c5/body-968257e9-d2a5-4ed0-8cf1-a700f0dec69c_Fig3%2BnoPad%2BZimbra%2BFull%2BChain%2B%25402x.png)

As a reminder, if the users `A`, `B` and `C` had made a HTTP request, the following Memcached commands would have been sent to the server:

![Shared traffic](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/39c95650-4cb3-4d63-8885-dfd49162c134/body-83175e67-2703-400f-9830-35284f578402_11.png)

Memcached would have then responded with the following data:

![Shared Memcache traffic](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/823aa972-537f-4bb3-9fef-57c0ae386164/body-b7520723-5806-4a1e-9a62-82574d7b0f1b_12.png)

User `A`'s lookup response is first in the shared work queue. When processed, only the bytes in the response stream that are relevant to this work item are processed. In this case, it is the first value. After having processed `A`'s work item, `B`'s work item is processed with the remaining bytes, and so on.

This behavior can be exploited by injecting more responses to get requests than there are work items in the queue. Let's assume again that cache lookups of users `A`, `B`, and `C` are in the shared work queue. However, user `A` is malicious and abuses the previously discussed CLRF to force Zimbra to send the following traffic to the Memcached server:

![Injected request](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3e8aabde-68ab-404e-85aa-1ab4b6350cc9/body-593998c0-6642-40e5-b048-0af294517260_13.png)

If the attacker had previously set the `route:proto=httpssl;user=` and `A@example.com` cache entries to a value of an attacker-controlled server, the response stream could look like the following:

![Injected response](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c6c1f3c4-d244-4bd9-93f7-2c88f139acfa/body-3f9ceeb9-3d6b-4867-a23f-e0e50a46a2e9_14.png)

We can also illustrate this state with the following image:

![corrupt workqueue](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0298e277-1983-41c2-b3bd-dda079c91cde/body-5e072a12-4930-4f9e-8537-992431a2cb16_Fig4%2BnoPad%2BZimbra%2BFull%2BChain%2B%25402x.png)

The image above demonstrates how there are more items in the response stream than there are items in the work queue. If this state was forced, `A`'s cache lookup request would process only the first result, `result A1`. When `B`'s cache lookup request is then processed, it would use the value of `result A2`, which is attacker-controlled.

The idea is that by continuously injecting more responses than there are work items into the shared response streams of Memcached, we can force random Memcached lookups to use injected responses instead of the correct response. This works because Zimbra did not validate the key of the Memcached response when consuming it. 

By exploiting this behavior, we can hijack the proxy connection of random users connecting to our IMAP server without having to know their email addresses. This exploitation strategy also does not break anything, as HTTP lookup requests that would use a poisoned value would fall back to a Round Robin approach.

## Patch

Zimbra patched the vulnerability by creating a SHA-256 hash of all Memcache keys before sending them to the Memcache server. As the hex-string representation of a SHA-256 can’t contain whitespaces, no new-lines can be injected anymore.

The fixed versions are respectively 8.8.15 with Patch level [31.1](https://wiki.zimbra.com/wiki/Zimbra_Releases/8.8.15/P31.1) and 9.0.0 with Patch level [24.1](https://wiki.zimbra.com/wiki/Zimbra_Releases/9.0.0/P24.1).

## Timeline

**Date**| **Action**  
---|---  
2022-03-11| We report the issue to Zimbra  
2022-03-11| Zimbra acknowledges the report  
2022-03-16| Zimbra confirms that they were able to reproduce the vulnerability  
2022-03-31| Zimbra releases a patch for the 8.8.15 and 9.0.0 branches  
2022-04-01| We inform Zimbra that the patches are insufficient  
2022-04-05| We discuss the insufficient patch and patch strategies with Zimbra developers on a Webex call  
2022-05-01| We ask Zimbra for an update on the patches  
2022-05-02| Zimbra tells us that they are testing a patch  
2022-05-06| Zimbra sends us patch to test  
2022-05-06| We verify the patch works  
2022-05-10| Zimbra informs us about the upcoming release of the patch  
2022-05-22| We inform Zimbra about the release date of this advisory  
  
## Summary

In this blog post, we presented a Memcache Injection vulnerability in Zimbra that exists because newline characters `(\r\n)` are not escaped in untrusted user input. This code flaw ultimately allows attackers to steal cleartext credentials from users of targeted Zimbra instances.

Although vulnerabilities such as Cross-Site Scripting and SQL Injections still exist and occur due to a lack of input escaping, they have been well known and documented for decades. The majority of developers understand these vulnerabilities and that certain, context-specific characters should be escaped before passing them to a potentially dangerous function. However, as we have seen, other injection vulnerabilities can occur that are less known and can have a critical impact. 

We recommend developers to always be aware of special characters that should be escaped when dealing with technology where less documentation and research about potential vulnerabilities exists.

## Related Blog Posts

  * [Zimbra 8.8.15 - Webmail compromise via Email](https://blog.sonarsource.com/zimbra-webmail-compromise-via-email)
  * [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer)
  * [NodeBB 1.18.4 - Remote Code Execution With One Shot](https://blog.sonarsource.com/nodebb-remote-code-execution-with-one-shot)

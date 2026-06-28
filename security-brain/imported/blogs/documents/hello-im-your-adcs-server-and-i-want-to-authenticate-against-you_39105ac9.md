---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-25_hello-im-your-adcs-server-and-i-want-to-authenticate-against-you.md
original_filename: 2024-02-25_hello-im-your-adcs-server-and-i-want-to-authenticate-against-you.md
title: 'Hello: I’m your ADCS server and I want to authenticate against you'
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- path-traversal
- graphql
- api-security
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- path-traversal
- graphql
- api-security
language: en
raw_sha256: 39105ac9e2c8b3ac7618d92c12e774a0adc42635bb80956d7400f22707b8f4fd
text_sha256: 95802067f83ee457b6d16b5ea29f8f96e9754c8fd2aea359bc653b35a264b260
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Hello: I’m your ADCS server and I want to authenticate against you

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-25_hello-im-your-adcs-server-and-i-want-to-authenticate-against-you.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, path-traversal, graphql, api-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `39105ac9e2c8b3ac7618d92c12e774a0adc42635bb80956d7400f22707b8f4fd`
- Text SHA256: `95802067f83ee457b6d16b5ea29f8f96e9754c8fd2aea359bc653b35a264b260`


## Content

---
title: "Hello: I’m your ADCS server and I want to authenticate against you"
page_title: "Hello: I’m your ADCS server and I want to  authenticate against you – Decoder's Blog"
url: "https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/"
final_url: "https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/"
authors: ["ap (@decoder_it)"]
bugs: ["ADCS", "Authentication coercion", "Active Directory Privilege Escalation", "Internal pentest"]
publication_date: "2024-02-25"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 407
---

In my exploration of all the components and configurations related to the Windows Active Directory Certification Services (ADCS), after the “deep dive” in [Cert Publishers ](https://decoder.cloud/2023/11/20/a-deep-dive-in-cert-publishers-group/)group, I decided to take a look at the “**Certificate Service DCOM Access** ” group.

This group is a built-in local security group and is populated by the special **NT AUTHORITY\Authenticaterd Users** identity group, which represents every Domain user account that can successfully log on to the domain, whenever the server assumes the role of a Certification Authority (CA) server by installing the Active Directory Certification Services (ADCS) role.

The “DCOM Access” is somewhat intriguing; it evokes potential vulnerabilities and exploitation 😉

But let’s start from the beginning. What’s the purpose of this group? MS says: “ _Members of this group are allowed to connect to Certification Authorities in the enterprise_ “.

In simpler terms, this group can enroll certificates via DCOM. Thus, it’s logical that all authenticated users and computers have access to the specific application.

Each time a user or computer enrolls or auto enrolls a certificate, it contacts the DCOM interfaces of the **CertSrv Request** application which are exposed through the[ MS-WCCE](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/446a0fca-7f27-4436-965d-191635518466) protocol, the Windows Client Certificate Enrollment Protocol.

There is also a specific set of interfaces for Certificate Services Remote Administration Protocol described in [MS-CSRA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-csra/40e74714-14bf-4f97-a264-35efbd63a813).

![](https://decoder.cloud/wp-content/uploads/2024/02/image.png?w=1024)

I won’t delve into the specifics of these interfaces. Maybe there are interesting interfaces to explore and abuse, but for now, my focus was drawn to the activation permissions of this DCOM server.

The **DCOMCNFG** tool provides us a lot of useful info.

At the computer level, the Certificate Service DCOM Access group is “limited” to Local and Remote Launch permissions:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-2.png?w=932) ![](https://decoder.cloud/wp-content/uploads/2024/02/image-1.png?w=1024)

This does not mean that this group can activate all the DCOM objects, we have to look at the specific application, CertSrv Request in our case:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-3.png?w=1024)

Everyone can activate from remote this DCOM server. To be honest, I would have expected to find the Certificate Service DCOM Access group here instead of Everyone, given that this group is limited to Local Launch and Local Activation permissions:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-8.png?w=732)

Maybe some kind of combined permissions and nested memberships are also evaluated.

There’s another interesting aspect as well: from what I observed, the **Certificate Service DCOM Access** group is one of the few groups, along with **Distributed COM Users** and **Performance Log Users** , that are granted **Remote Activation** permissions.

Let’s take a look at identity too:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-6.png?w=1024)

This DCOM application impersonates the SYSTEM account, which is what we need because it represents the highest local privileged identity.

So, we have a privileged DCOM server running that can be activated remotely by any authenticated domain user. This seems prone to our loved ***potato** exploits, don’t you think?

In summary, most of these exploits rely on abusing a DCOM activation service, running under a highly privileged context, by unmarshalling an IStorage object and reflecting the NTLM authentication back to a local RPC TCP endpoint to achieve local privilege escalation.

There are also variants of this attack that involve relaying the NTLM (and Kerberos) authentication of a user or computer to a remote endpoint using protocols such as LDAP, HTTP, or SMB, ultimately enabling privilege escalation up to Domain Admin. And this is what @splinter_code and I did in our [RemotePotato0](https://labs.sentinelone.com/relaying-potatoes-dce-rpc-ntlm-relay-eop/).

But this scenario is different, as a low-privileged domain user, we want to activate a remote DCOM application running under a high-privileged context and force it to authenticate against a remote listener running on our machine so that we can capture and relay this authentication to another service.

We will (hopefully) get the authentication of the remote computer itself when the DCOM application is running under the SYSTEM or Network Service context.

Sounds great! l Now, what specific steps should we take to implement this? 

Well, it is much simpler than I initially thought 🙂

Starting from the original [JuicyPotato](https://decoder.cloud/2018/08/10/juicy-potato/) I made some minor changes:

  * Set up a redirector (socat) on a Linux machine on port 135 to redirect all traffic on our attacker machine on a dedicated port (ex: 9999). _You certainly know that we can no longer specify a custom port for Oxid Resolution_ 😉 .
  * In JuicyPotato code: 
  * Initialize a [COSERVERINFO](https://learn.microsoft.com/en-us/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure and specify the IP address of the remote server where we want to activate the DCOM object (the ADCS server)
  * Initialize a [COAUTHIDENTITY](https://learn.microsoft.com/en-us/windows/win32/api/wtypesbase/ns-wtypesbase-coauthidentity) and populate the username, password, and domain attributes.
  * Assign the COAUTHIDENTITY to the COSERVERINFO structure
  * In IStorageTrigger::Marshallfinterface specify the redirector IP address
  * In CoGetInstanceFromIStorage() pass the the COSERVERINFO structure:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-9.png?w=1024)

And yes it worked 🙂 Dumping the NTLM messages received on our socket server we can see that we get an authentication type 3 message from the remote CA server (SRV1-MYLAB):

![](https://decoder.cloud/wp-content/uploads/2024/02/image-7.png?w=827)

The network capture highlights that the Remote Activation requested by our low-privileged user was successful:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-10.png?w=1024)

The final step is to forward the NTLM authentication to an external relay, such as [ntlmrelayx](https://github.com/fortra/impacket), enabling authentication to another service as the CA computer itself.

Last but not least, since we have an RPC Client authenticating, we must encapsulate and forward the authentication messages using a protocol already implemented and supported in ntlmrelayx, such as HTTP.

I bet that now the fateful question arises:

_Ok, regular domain users can coerce the authentication of an ADCS server from remote, intercept the authentication messages, and relay it, but is this really useful?_

Well, considering the existence of other unpatched methods to coerce authentication of a Domain Controller, such as [DFSCoerce](https://github.com/Wh04m1001/DFSCoerce), I would argue its utility may be limited.

To complicate matters further, the only protocols that can be relayed, due the the [hardening](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/dcom-authentication-hardening-what-you-need-to-know/ba-p/3657154) MS recently made in DCOM, at the moment are HTTP and SMB (if signing is not required).

In my lab, I tested the relay against the HTTP **/CertSrv** endpoint of a CA web enrollment server running on a different machine (guess why?… you cannot relay back to the same machine over the network). With no NTLM mitigations in place, I requested a Machine certificate for the CA server. 

![](https://decoder.cloud/wp-content/uploads/2024/02/image-11.png?w=1024)

The attack flow is shown below:

![](https://decoder.cloud/wp-content/uploads/2024/02/image-16.png?w=1024)

With this certificate, I could then log onto the ADCS server in a highly privileged context. For example, I could back up the private key of the CA, ultimately enabling the forging of certificates on behalf of any user.

## The POC

I rewrote some parts of our old JuicyPotato to adapt it to this new scenario. It’s a quick & dirty fix and somehow limited, but it was more than enough to achieve my goal 🙂

Source Code: <https://github.com/decoder-it/ADCSCoercePotato/>

_Side Note:_ You can get rid of the socat redirector by using our [JuicyPotatoNG ](https://github.com/antonioCoco/JuicyPotatoNG)code and implement a fake Oxid Resolver like we did in [RemotePotato0](https://github.com/antonioCoco/RemotePotato0), with the extra bonus that you can also control the SPN and [perform a Kerberos relay](https://github.com/cube0x0/KrbRelay) too… and yes, you can **relay back** in this case!

![](https://decoder.cloud/wp-content/uploads/2024/02/image-21.png?w=1024)

## Conclusions

While the method I described for coercing authentication may not be groundbreaking, it offers interesting alternative ways to force the authentication of a remote server by abusing the Remote Activation permission granted to regular domain users. 

This capability is only limited to the **Certificate Service DCOM Access** group, which is populated only when the ADCS service is running. However, there could be legacy DCOM applications that grant Remote Activation to everyone.

Imagine DCOM Applications running under the context of the “Interactive User” with Remote Activation available to regular users. With cross-session implementation, you could also retrieve the authentication of a logged-in user 😉

![](https://decoder.cloud/wp-content/uploads/2024/02/image-19.png?w=1024)

Another valid reason to avoid installing unnecessary services on a Domain Controller, including the ADCS service!

That’s all 🙂

### Share this:

  * [ Share on X (Opens in new window) X ](https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/?share=facebook)
  * 

Like Loading...

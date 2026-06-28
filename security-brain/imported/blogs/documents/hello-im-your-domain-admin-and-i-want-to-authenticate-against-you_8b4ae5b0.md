---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-24_hello-im-your-domain-admin-and-i-want-to-authenticate-against-you.md
original_filename: 2024-04-24_hello-im-your-domain-admin-and-i-want-to-authenticate-against-you.md
title: 'Hello: I’m your Domain Admin and I want to authenticate against you'
category: documents
detected_topics:
- command-injection
- sso
- access-control
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- sso
- access-control
- api-security
- mobile-security
language: en
raw_sha256: 8b4ae5b00d283658ae8c01f81493f7b5693c5ba02d8d6f97cba81024a6e203ee
text_sha256: f5f3b540c9e6dcf202f7df0c161a2c228f6c588f16fd13efca21d43db6445105
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Hello: I’m your Domain Admin and I want to authenticate against you

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-24_hello-im-your-domain-admin-and-i-want-to-authenticate-against-you.md
- Source Type: markdown
- Detected Topics: command-injection, sso, access-control, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `8b4ae5b00d283658ae8c01f81493f7b5693c5ba02d8d6f97cba81024a6e203ee`
- Text SHA256: `f5f3b540c9e6dcf202f7df0c161a2c228f6c588f16fd13efca21d43db6445105`


## Content

---
title: "Hello: I’m your Domain Admin and I want to authenticate against you"
page_title: "Hello: I’m your Domain Admin and I want to authenticate against you – Decoder's Blog"
url: "https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/"
final_url: "https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/"
authors: ["ap (@decoder_it)"]
programs: ["Microsoft"]
bugs: ["RCE", "Privilege escalation", "Authentication coercion", "Active Directory", "NTLM", "Internal pentest"]
publication_date: "2024-04-24"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 322
---

_TL;DR (really?): Members of Distributed COM Users or Performance Log Users Groups can trigger from remote and relay the authentication of users connected on the target server, including Domain Controllers._ _**#SilverPotato**_

Remember my previous [article](https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/)? My insatiable curiosity led me to explore the default DCOM permissions on Domain Controllers during a quiet evening…

Using some custom Powershell scripts, I produced an Excel sheet with all the information I needed.

You can’t imagine the shock I felt when I discovered these two Application Id’s

![](https://decoder.cloud/wp-content/uploads/2024/04/image-4.png?w=1024)

The first one, **sppui** with ID: {0868DC9B-D9A2-4f64-9362-133CEA201299}, seemed very interesting because it was impersonating the **Interactive** user. Combined with the permissions granted to Everyone for activating this application from remote, this could potentially lead to some unexpected privilege escalation, don’t you think?

The output of the DCOMCNFG tool confirmed my analysis:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-1.png?w=598) ![](https://decoder.cloud/wp-content/uploads/2024/04/image-2.png?w=586) ![](https://decoder.cloud/wp-content/uploads/2024/04/image-5.png?w=755)

But wait, this does not mean Everyone can activate this DCOM Application remotely. We have to look also at the default limits for Everyone:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-6.png?w=791)

Everyone can only activate and launch locally… but… there are these two interesting groups, **Distributed COM Users** and**Performance Log Users** who can launch and activate the application remotely:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-7.png?w=816)

Combined with Everyone’s permission this sounds really interesting! But before going further, what is this application **sspui?**

With the magic [Oleview](https://github.com/tyranid/oleviewdotnet) tool, we can get much more information:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-8.png?w=1024)

This app has the following CLSID **F87B28F1-DA9A-4F35-8EC0-800EFCF26B83 – SPPUIObjectInteractive** **Class** , and runs as a Local Server :

![](https://decoder.cloud/wp-content/uploads/2024/04/image-9.png?w=1024)

**slui.exe** is related to the License Activation Service and exposes some interfaces:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-11.png?w=1024)

At first glance, the methods implemented seem not very interesting from an Attacker perspective.

However, we have this DCOM object running in the context of the interactive user, accessible remotely by members of these two groups. So, why not attempt coercing authentication using our *potato exploit? If successful, we could intercept the authentication of the user connected to the Domain Controller, who should theoretically be a Domain Admin, correct 😉 ?

This is very similar to what I did in [ADCCoercePotato](https://github.com/decoder-it/ADCSCoercePotato), except for the fact that we may need to implement also the cross-session activation if we want to specify a specific session ID where the user is logged in.

![](https://decoder.cloud/wp-content/uploads/2024/04/image-12.png?w=1024)

I won’t go too much into the details; @splinter_code and I have discussed this argument so many times 🙂

The key point is that there are two authentication processes: the first occurs during the oxid resolve call, while the second takes place when the victim attempts to contact the malicious endpoint.

## First AUTH

I obviously tried the first one, and without too much effort, was able to trigger and intercept the NTLM authentication of a Domain Admin connected to the target Domain Controller.

For testing purposes, I impersonated my user “simple”, a regular domain user and member of the “Performance Log Users” domain group:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-13.png?w=610)

I used my new “SilverPotato” tool, a modified version of ADCSCoercePotato:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-15.png?w=1024)

In this case, with **-m** ,**** I specified the IP address of the target domain controller, and with **-k** , the IP of the Linux box where the**socat** redirector and **ntlmrelayx** were running:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-16.png?w=908)

And yes, it worked! I got the authentication of Administrator connected on the first session (I did not specify the session ID).

I decided to relay the authentication to the SMB service of the ADCS server (_but it’s just an example…_), which by default has no signing enabled, and dumped the local SAM database:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-18.png?w=1024)

With the NT hash of the local Administrator, I could access the ADCS Server via Pass The Hash, backup the Private/Public key of the CA, and the get CRL configuration.

![](https://decoder.cloud/wp-content/uploads/2024/04/image-24.png?w=1024)

_Side note:_ _Of course, there are other methods to achieve remote code execution on the target server. For instance, I utilized ntlmrelay to copy my malicious wbemcomn.dll file with a reverse shell into the c:\windows\system32\wbem directory. This file was subsequently loaded under different conditions, granting me a shell with SYSTEM, Network Service, or logged-in User privileges_

After this, with [ForgeCert](https://github.com/GhostPack/ForgeCert) tool, I was able to request a certificate on behalf Domain Administrator with the backup file of the CA.

![](https://decoder.cloud/wp-content/uploads/2024/04/image-20.png?w=1024)

Finally, request a TGT with [Rubeus](https://github.com/GhostPack/Rubeus) and logon to the Domain Controller as Administrator

![](https://decoder.cloud/wp-content/uploads/2024/04/image-22.png?w=1024)

## second auth

Afterward, I attempted to exploit the second authentication, which is more or less what we implemented in our [RemotePotato0](https://github.com/antonioCoco/RemotePotato0).

However, to my surprise, the resulting impersonation level in this case was limited to **Identify** , which is useless against SMB or HTTP, and unusable against LDAP/LDAPS because of the sign flag… 😦

Otherwise, it could have presented a great opportunity to use Kerberos relay instead of NTLM, given that the Service Principal Name (SPN) was within the attacker’s control.

## kerberos relay in first auth?

In theory, you could specify the Service Principal Name (SPN) in the first call in the security bindings strings of the “dualstring” array of the Marshalled Interface Pointer:
  
  
  typedef struct tagSECURITYBINDING 
  {
      unsigned short    wAuthnSvc;     // Must not be 0
      unsigned short    wAuthzSvc;     // Must not be 0
      unsigned short    aPrincName;    // NULL terminated
  } SECURITYBINDING

I specified the SPN with the **-y** switch:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-25.png?w=1024)

But my tests were unsuccessful, I always got back the SPN: **RPCSS/IP** in the NTLM3 message:

![](https://decoder.cloud/wp-content/uploads/2024/04/image-26.png?w=870)

A few days ago, James Forshaw pointed out to me the potential for Kerberos relay via OXID resolving, by exploiting the marshaled target info trick detailed in his [post](https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html) under the “Marshaled Target Information SPN” section.

I attempted some tests ~~but quickly gave up, using the excuse that I’m just too lazy 😉 .. so I’ll leave it up to you!~~ and it worked! Starting from [@cube0x0](https://twitter.com/cube0x0) great[ KrbRelay](https://github.com/cube0x0/KrbRelay) tool, I added an extra layer of complexity to get the SilverPotato beast working.

![](https://decoder.cloud/wp-content/uploads/2024/05/image.png?w=1024)

## conclusion

At this point, I know I have to answer the fateful question: _Did you report this to MSRC_?

Obviously, yes! I’ll spare you the disclosure timeline. In short, MSRC confirmed the vulnerability and initially marked it as a critical fix. However, about a month later, they downgraded it to moderate severity. Their final verdict was: _After careful investigation, this case has been assessed as moderate severity and does not meet MSRC’s bar for immediate servicing._

So, I feel free to publish this finding 😉

I’m not going to release the source code for now, but crafting your own should be a breeze, wouldn’t you agree?

This “vulnerability” has been probably around for years, and it’s surprising that nobody has made it public.

So how dangerous is it?

Hard to say, especially since membership in groups like “Distributed COM Users” and “Performance Log Users” isn’t exactly commonplace, especially domain-wide. Also, the “Distributed COM Users” group is sometimes considered a [tier 0 asset ](https://specterops.github.io/TierZeroTable/)

But think about it: the ability to coerce and relay the (NTLM, Kerberos) authentication of highly privileged accounts from remote, is incredibly risky. It’s another valid reason to include privileged accounts in the Protected Users group!

Another point to consider is that this method applies to the local “Distributed COM Users” and “Performance Log Users” groups too. So, it really depends on who is logged into the server at the time…

I would recommend carefully reviewing the memberships of these and until MS won’t fix this vulnerability, definitely consider these groups tier 0!

What’s next after SilverPotato? Well, there’s another interesting one, but this was classified as an Important Privilege Escalation so I have to wait for the fix…

Last but not least, as usual, thanks to James Forshaw @tiraniddo and Antonio Cocomazzi @splinter_code for their precious help.

That’s all 🙂

## UPDATE:

Microsoft fixed this “DCOM permissions bug” in July 2024 Patch Tuesday with[ CVE-2024-38061.](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38061) Interestingly, the same vulnerability was discovered by another researcher after my initial report, and Microsoft Security Response Center (MSRC) deemed it to be of IMPORTANT severity. When I requested MSRC to update my case, they refused without providing a valid reason, which was incredibly frustrating. I believe MSRC should be ashamed of this behavior. As a result, I asked for my acknowledgment in the CVE to be removed. Therefore, you won’t find my name any more, even though I was the first to discover this vulnerability. I refused to have my name associated with such a ridiculous behavior.

### Share this:

  * [ Share on X (Opens in new window) X ](https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/?share=facebook)
  * 

Like Loading...

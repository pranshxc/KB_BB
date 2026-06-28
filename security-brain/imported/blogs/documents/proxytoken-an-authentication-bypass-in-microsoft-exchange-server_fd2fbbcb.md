---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-30_proxytoken-an-authentication-bypass-in-microsoft-exchange-server.md
original_filename: 2021-08-30_proxytoken-an-authentication-bypass-in-microsoft-exchange-server.md
title: 'Proxytoken: An Authentication Bypass In Microsoft Exchange Server'
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: fd2fbbcbf845f51df5deefba944fd313f434b399e4f3a2b4fbe5e0b4ff68bcf1
text_sha256: 77dcc0711096c4cb6431a6573bb7fe5456b7eef4598d9d10f444da60f762b5b9
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Proxytoken: An Authentication Bypass In Microsoft Exchange Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-30_proxytoken-an-authentication-bypass-in-microsoft-exchange-server.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `fd2fbbcbf845f51df5deefba944fd313f434b399e4f3a2b4fbe5e0b4ff68bcf1`
- Text SHA256: `77dcc0711096c4cb6431a6573bb7fe5456b7eef4598d9d10f444da60f762b5b9`


## Content

---
title: "Proxytoken: An Authentication Bypass In Microsoft Exchange Server"
page_title: "Zero Day Initiative — ProxyToken: An Authentication Bypass in Microsoft Exchange Server"
url: "https://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server"
final_url: "https://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server"
authors: ["Xuan Tuyen"]
programs: ["Microsoft"]
bugs: ["Authentication bypass"]
publication_date: "2021-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3369
---

# Blog

#  ProxyToken: An Authentication Bypass in Microsoft Exchange Server 

__ August 30, 2021

__ Simon Zuckerbraun

Continuing with the theme of serious vulnerabilities that have recently come to light in Microsoft Exchange Server, in this article we present a new vulnerability we call ProxyToken. It was reported to the Zero Day Initiative in March 2021 by researcher Le Xuan Tuyen of VNPT ISC, and it was patched by Microsoft in the July 2021 Exchange cumulative updates. Identifiers for this vulnerability are [CVE-2021-33766](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33766) and [ZDI-CAN-13477](https://www.zerodayinitiative.com/advisories/ZDI-21-798/).

With this vulnerability, an unauthenticated attacker can perform configuration actions on mailboxes belonging to arbitrary users. As an illustration of the impact, this can be used to copy all emails addressed to a target and account and forward them to an account controlled by the attacker.

**The Trigger**

The essential HTTP traffic needed to trigger the vulnerability is as follows:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1629917172715-K3VVV119DI5SFPDEQM2G/Picture1.png)

“SecurityToken=x”? What might this be, some secret backdoor access code?

**Understanding the Root Cause**

To understand what has happened here, it is necessary to discuss a bit about the architecture of Exchange Server. Recently, security researcher [Orange Tsai](https://www.twitter.com/orange_8361) has done excellent work in this area, and readers are encouraged to read his full findings [here](https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/) as well as the recent [guest blog](https://www.zerodayinitiative.com/blog/2021/8/17/from-pwn2own-2021-a-new-attack-surface-on-microsoft-exchange-proxyshell) he wrote on this site. However, for the purposes of this particular vulnerability, the salient points will be summarized below.

Microsoft Exchange creates two sites in IIS. One is the default website, listening on ports 80 for HTTP and 443 for HTTPS. This is the site that all clients connect to for web access (OWA, ECP) and for externally facing web services. It is known as the “front end”. The other site is named “Exchange Back End” and listens on ports 81 for HTTP and 444 for HTTPS.

The front-end website is mostly just a proxy to the back end. To allow access that requires forms authentication, the front end serves pages such as `/owa/auth/logon.aspx`. For all post-authentication requests, the front end’s main role is to repackage the requests and proxy them to corresponding endpoints on the Exchange Back End site. It then collects the responses from the back end and forwards them to the client.

Exchange is a highly complex product, though, and this can lead to some wrinkles in the usual flow. In particular, Exchange supports a feature called “Delegated Authentication” supporting cross-forest topologies. In such deployments, the front end is not able to perform authentication decisions on its own. Instead, the front end passes requests directly to the back end, relying on the back end to determine whether the request is properly authenticated. These requests that are to be authenticated using back-end logic are identified by the presence of a `SecurityToken` cookie:

In `Microsoft.Exchange.HttpProxy.ProxyModule.SelectHandlerForUnauthenticatedRequest`:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1629917271871-VNLS3PTRWXWB6X2DZ1GH/Picture2.png)

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1629917306935-E19576QKU0EY1N7T2KCA/Picture3.png)

Thus, for requests within `/ecp`, if the front end finds a non-empty cookie named `SecurityToken`, it delegates authentication to the back end.

Code on the back end that examines and validates the `SecurityToken` cookie is found in the class `Microsoft.Exchange.Configuration.DelegatedAuthentication.DelegatedAuthenticationModule`. What goes wrong on the validation side? To see the answer, have a look at `/ecp/web.config` on the back end:

As you can see, in a default configuration of the product, a `<remove>` element appears, so that the module `DelegatedAuthModule` will not be loaded at all for the back-end ECP site.

In summary, when the front end sees the `SecurityToken` cookie, it knows that the back end alone is responsible for authenticating this request. Meanwhile, the back end is completely unaware that it needs to authenticate some incoming requests based upon the `SecurityToken` cookie, since the `DelegatedAuthModule` is not loaded in installations that have not been configured to use the special delegated authentication feature. The net result is that requests can sail through, without being subjected to authentication on either the front or back end.

**Bagging a Canary**

There is one additional hurdle to clear before we can successfully issue an unauthenticated request, but it turns out to be a minor one. Each request to an `/ecp` page is required to have a ticket known as the “ECP canary”. Without a canary, the request will come back with an HTTP 500. However, the attacker is still in luck, because the 500 error response is accompanied by a valid canary:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1629917386888-TIIWTNJAJSFUTB9UE42P/Picture4.png)

An example of the final request would then be as follows:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1629917418341-D2S571HAY9VJORJ9KPL4/Picture5.png)

This particular exploit assumes that the attacker has an account on the same Exchange server as the victim. It installs a forwarding rule that allows the attacker to read all the victim’s incoming mail. On some Exchange installations, an administrator may have set a global configuration value that permits forwarding rules having arbitrary Internet destinations, and in that case, the attacker does not need any Exchange credentials at all. Furthermore, since the entire `/ecp` site is potentially affected, various other means of exploitation may be available as well.

**Conclusion**

Exchange Server continues to be an amazingly fertile area for vulnerability research. This can be attributed to the product’s enormous complexity, both in terms of feature set and architecture. We look forward to receiving additional vulnerability reports in the future from our talented researchers who are working in this space. Until then, follow the [team](https://twitter.com/thezdi) for the latest in exploit techniques and security patches.

  * [Microsoft](/blog/tag/Microsoft)
  * [Exchange](/blog/tag/Exchange)
  * [Exploit](/blog/tag/Exploit)

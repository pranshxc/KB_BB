---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-01_abusing-microsoft-teams-direct-routing.md
original_filename: 2022-09-01_abusing-microsoft-teams-direct-routing.md
title: Abusing Microsoft Teams Direct Routing
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: cc44f4f048aba735cc2041c32fd62cde3cdb04812b49b23251838effddf617bb
text_sha256: e3b97488a8bd30e8db4a64812effa1ccfdcd3cd2d337b0acffbe3676cd2ad18f
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Microsoft Teams Direct Routing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-01_abusing-microsoft-teams-direct-routing.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `cc44f4f048aba735cc2041c32fd62cde3cdb04812b49b23251838effddf617bb`
- Text SHA256: `e3b97488a8bd30e8db4a64812effa1ccfdcd3cd2d337b0acffbe3676cd2ad18f`


## Content

---
title: "Abusing Microsoft Teams Direct Routing"
page_title: "Abusing Microsoft Teams Direct Routing | SySS Tech Blog"
url: "https://blog.syss.com/posts/abusing-ms-teams-direct-routing/"
final_url: "https://blog.syss.com/posts/abusing-ms-teams-direct-routing/"
authors: ["Moritz Abrell (@moritz_abrell)"]
programs: ["AudioCodes Ltd."]
bugs: ["Spoofing", "Fraud attack"]
publication_date: "2022-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2233
---

In this blog post, a practical problem and security issue when it comes to phone integration with Microsoft Teams Direct Routing is described.  Due to a lack of authentication methods provided by Microsoft, current Microsoft Teams Direct Routing installations may be vulnerable to toll fraud attacks.

# TL;DR

An external, unauthenticated attacker is able to send specially crafted SIP messages, that pretend to originate from Microsoft and are therefore correctly classified by the victim’s Session Border Controller.

As a result, unauthorized external calls are made through the victim’s phone line (toll fraud).

![tl;dr proof-of-concept](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

The research was also presented at this year’s DEF CON Hacking Conference in Las Vegas. The [slides](https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Moritz%20Abrell%20-%20Phreaking%202.0%20-%20Abusing%20Microsoft%20Teams%20Direct%20Routing.pdf) are available on the DEF CON media server.

# Microsoft PSTN connectivity options

Microsoft Teams can be extended for making and receiving external phone calls e.g. using the Microsoft Teams client like a softphone. For enabling this, Microsoft Teams needs to be connected with a Public Switched Telephone Network (PSTN) by one of the following options:

  * **Calling Plan** : Full cloud solution where Microsoft is used as PSTN carrier.

  * **Operator Connect** : Usage of a Operator Connect supported PSTN carrier, where the hosting and connectivity is managed by a third-party operator or the PSTN carrier itself.

  * **Direct Routing** : Enables the integration of your existing VoIP Infrastructure e.g. your own PSTN carrier.

More information about Microsoft Teams PSTN connectivity can be found in the [Microsoft Documentation](https://docs.microsoft.com/en-us/microsoftteams/pstn-connectivity).

Since this blog post focuses on the Direct Routing option, we will go into more detail about it.

## Direct Routing and Session Border Controller

As already mentioned, Microsoft Teams Direct Routing allows you integrating your existing communication infrastructure e.g. PBX, contact center, legacy devices, or your telephone carrier. A common application scenario is connecting Microsoft Teams with a SIP account from a PSTN carrier.

For enabling this, the operation of a dedicated Session Border Controller (SBC) is needed. The following figure shows a basic sample architecture for this scenario:

![Basic sample architecture of Microsoft Teams Direct Routing](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Basic sample architecture of Microsoft Teams Direct Routing_

To ensure full functionality and interoperability Microsoft has a certification program for SBCs. More details about this certification program and the list of tested and certified devices can be found in the [Microsoft documentation](https://docs.microsoft.com/en-us/microsoftteams/direct-routing-border-controllers).

In the author’s experience, one of the common SBCs are devices from AudioCodes. Therefore, we chose an AudioCodes SBC as an example to analyze Microsoft Teams Direct Routing PSTN connectivity.

# Analysis of a recommended configuration

AudioCodes published configuration guidelines for the integration with Microsoft Teams, which are results from the certification process and interoperability tests by Microsoft. These guidelines include some [carrier specific guides](https://www.audiocodes.com/partners/sbc-interoperability-list?server=microsoft%20teams) as well as a [gerneral configuration note](https://www.audiocodes.com/media/13253/connecting-audiocodes-sbc-to-microsoft-teams-direct-routing-enterprise-model-configuration-note.pdf).

In addition, AudioCodes provides a [configuration wizard](http://redirect.audiocodes.com/install/index.html), where all requirements can be clicked together resulting in a final configuration, as the following figure illustrates:

![AudioCodes configuration wizard](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _AudioCodes configuration wizard_

Therefore, a configuration recommended and certified by the manufacturer is used as the basis for the security analysis.

## Call handling

The communication between the Microsoft SIP proxies and the SBC is done with the Session Initiation Protocol. When a call is initiated from the Microsoft Teams client, the configured SBC receives the SIP messages of the call.

After receiving a SIP message, the SBC handles this by configured actions and call routing rules e.g. establish a connection through the configured PSTN carrier. In this case, the SBC acts as a so-called _back-to-back user agent_ (B2BUA) between the Microsoft SIP proxies and the PSTN carrier.

## Conditions and classification

Before a SIP message is handled by the routing policies, it must be first classified by the SBC.

In the configuration recommended by the manufacturer, this classification includes the following conditions:

  * The SBC’s Fully-Qualified Domain Name (FQDN) must be set as destination host (host part of the SIP Request-URI) inside the SIP message

  * The static string `pstnhub.microsoft.com` must be included in the host part of the “Contact” header of the SIP message

After reviewing the rest of the configuration, no further conditions or authentications are required for correct classification of SIP messages received from Microsoft.

# Exploitation

Due to the lack of authentication, the attack idea is to send specially crafted SIP messages pretending to be from Microsoft, get correctly classified by the SBC, and finally establish a connection through the victim’s PSTN carrier.

For a successful attack, however, the FQDN of the SBC must be known. This can be obtained e.g. from the common name or subject alternative name value of the X.509 certificate of the exposed SIP-TLS service:

`
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  #> openssl s_client -connect XXX.XXX.XXX.XXX:5061 | openssl x509 -noout -text"
  
  [...]
  Subject: CN = sbc.example.com
  [...]
  
  
---|---  
`

## Proof of concept

As a proof of concept, the following SIP call flow was defined in an XML template, which can be used by the open source tool [SIPp](http://sipp.sourceforge.net/):

![Proof of concept SIP call flow](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Proof of concept SIP call flow_

When connecting to a SIP-TLS service, [SIPp](http://sipp.sourceforge.net/) requires an X.509 certificate. In fact, this is not required for the actual TLS handshake, and therefore a self-signed certificate can be used. The [proof of concept XML template](https://github.com/MoritzAbrell/MSTDR-PoC) can then be executed as follows:

`
  
  
  1
  2
  3
  

| 
  
  
  #> sipp <victim-sbc-ip>:5061 -sf poc.xml -s <dest-phone-number> \
  -m 1 -t l1 -tls_cert selfsign.crt -tls_key selfsign.key \
  -key hostname <sbc-fqdn> -key caller <victim-phone-number>
  
  
---|---  
`

As already seen in the tl;dr section, the SIP messages were correctly classified and an external phone call was initiated.

The call flow of the attack from the SBC’s point of view is shown in the following figure:

![SIP call flow from the perspective of the SBC](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _SIP call flow from the perspective of the SBC_

## Impact

This is a good time to consider the implications of such an attack.

First of all, the obvious impact with this issue is that an attacker is able to impersonate the victim and make calls on their behalf, e.g. CEO fraud or other social engineering attacks.

Second, the worse and common attack is toll fraud. In this case, an attacker initiates an external phone call through the victim’s PSTN carrier with the destination of a premium phone number. This premium phone number is under the attacker’s control, and therefore he receives the incurred charges, as illustrated in the following figure:

![Toll fraud](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Toll fraud_

# Responsible disclosure

In order for the security issues to be addressed, we have reported the vulnerabilities to AudioCodes Ltd. according to our [Responsible Disclosure Program](https://www.syss.de/en/responsible-disclosure-policy/). AudioCodes Ltd. responded after our vulnerability report and provided several workarounds during the disclosure process, which are described below.

## Insufficient IP filter

The manufacturer added the following additional IP filter:

![Insufficient IP filter](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Insufficient IP filter_

This IP filter means that classification is only successful if the incoming SIP messages have a source IP from the network `52.0.0.0/8`.

However, the addresses on this network are not exclusively assigned to Microsoft.

For example, the addresses from `52.0.0.0` to `52.79.255.255` are assigned to Amazon Technologies Inc.:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  

| 
  
  
  #> whois 52.0.0.0
  
  [...]
  NetRange:  52.0.0.0 - 52.79.255.255
  CIDR:  52.0.0.0/10, 52.64.0.0/12
  NetName:  AT-88-Z
  NetHandle:  NET-52-0-0-0-1
  Parent:  NET52 (NET-52-0-0-0-0)
  NetType:  Direct Allocation
  Organization:  Amazon Technologies Inc. (AT-88-Z)
  RegDate:  1991-12-19
  Updated:  2021-02-10
  Ref:  https://rdap.arin.net/registry/ip/52.0.0.0
  OrgName:  Amazon Technologies Inc.
  [...]
  
  
---|---  
`

The IP address assignments in AWS are documented and can be queried from <https://ip-ranges.amazonaws.com/ip-ranges.json>:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  

| 
  
  
  $ curl https://ip-ranges.amazonaws.com/ip-ranges.json \
  | jq '.prefixes[] | select (.ip_prefix|test("^52"))'
  
  [...]
  {
  "ip_prefix": "52.4.0.0/14",
  "region": "us-east-1",
  "service": "EC2",
  "network_border_group": "us-east-1"
  },
  {
  "ip_prefix": "52.95.224.0/24",
  "region": "eu-south-1",
  "service": "EC2",
  "network_border_group": "eu-south-1"
  },
  [...]
  
  
---|---  
`

So for an attacker, it is possible to allocate an IP address of the allowlisted IP range `52.0.0.0/8` in some AWS locations:

![Allocated IP address within the allowlisted IP range](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Allocated IP address within the allowlisted IP range_

This IP address can then be assigned to an EC2 instance in AWS and finally the attack is still possible.

## Insufficient mutual TLS authentication

Microsoft Teams Direct Routing supports mutual TLS authentication, which was also recommended as mitigation to the described attack by AudioCodes Ltd. This means, that the SBC is able to request and then validate the X.509 certificate of the Microsoft Teams SIP proxy for incoming SIP connections.

### Mutual TLS in a nutshell

One important check at certificate validation is the comparison of the requested hostname to the Common Name (CN) or Subject Alternative Name (SAN) of the X.509 server certificate.

When it comes to mutual TLS authentication, the server requests the client certificate and the client then responds with its X.509 client certificate. Due to this, the server does not validate the CN or SAN values of the client certificate. Therefore, it is even more important that the server does only trust the needed Certificate Authorities (CA) and that an attacker is not able to obtain a signed certificate form a trusted CA.

### Mutual TLS in Microsoft Teams Direct Routing

For enabling mutual TLS for Microsoft Teams Direct Routing, the SBC has to trust the following two certificates:

  * `DigiCert Global Root G2` (SHA1 fingerprint: `DF3C24F9BFD666761B268073FE06D1CC8D4F82A4`)

  * `Baltimore CyberTrust Root` (SHA1 fingerprint: `D4DE20D05E66FC53FE1A50882C78DB2852CAE474`)

However, both certificates are widely used. For example, the following image is showing the signing tree of the `Baltimore CyberTrust Root` certificate:

![Baltimore CyberTrust Root signing tree](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Baltimore CyberTrust Root signing tree_

Thus, an attacker is able to request a signed certificate for an arbitrary FQDN from a CA which ultimately signs the certificates by `DigiCert Global Root G2` or `Baltimore CyberTrust Root`. Finally, the attack is still possible, even if mutual TLS is enforced on the SBC.

More information about mutual TLS can be found in the [Microsoft documentation](https://docs.microsoft.com/en-us/microsoftteams/direct-routing-plan#public-trusted-certificate-for-the-sbc).

## Further measures

After we reported that the attack is still possible, AudioCodes Ltd. responded with the following statement:

> The AudioCodes Configuration Guides are focused on interworking and only describe the basic security rules.

Furthermore, the manufacturer recommended filtering the incoming party number and follow the SBC security and hardening guideline.

However, filtering the incoming party number is just a minimal security improvement, since the phone number can often be easily obtained by simple web search. Next, the SBC security and hardening guideline would also not prevent this attack without keeping Microsoft Teams Direct Routing working.

In addition to these recommendations, we noticed that AudioCodes added the additional section **_Configure Firewall Rules (Optional)_** in its guideline:

![Optional firewall rules](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Optional firewall rules_

If configured correctly, these firewall settings would only allow incoming TCP traffic from the documented Microsoft Teams SIP proxies, which indeed will effectively prevent exploiting the demonstrated attack.

However, it should be noted that this section is marked as optional by the manufacturer, and that the firewall settings are also not applied, if the configuration wizard is used.

## Microsoft

In general, the described issues are affecting all Microsoft Teams Direct Routing installations and SBCs. Please be aware that the AudioCodes SBC is just an example in this case.

Therefore, we also submitted a report to Microsoft about the security vulnerability and requested the implementation of proper authentication. For example, application-specific SIP digest authentication, which would allow a long password to be defined for SIP session authentication. Also, signing the Microsoft Teams SIP proxies with an exclusively used and dedicated CA would secure mutual TLS authentication.

But until now, this case is still open.

# Recommendation and mitigation

Currently, the only effective way to secure the SBC in combination with Microsoft Teams Direct Routing is defining an IP filter, only allowing incoming TCP traffic to the corresponding SIP service from the [documented Microsoft SIP proxies](https://docs.microsoft.com/en-us/microsoftteams/direct-routing-plan#microsoft-365-office-365-and-office-365-gcc-environments):

  * `52.112.0.0/14`

  * `52.120.0.0/14`

In addition, some SBCs support static SAN filtering and verification. Since all Microsoft Teams SIP proxies use an X.509 certificate including the SAN `sip.pstnhub.microsoft.com`, this value can be configured for static SAN verification.

Moreover, limiting the maximum call duration, sufficient logging and monitoring, and denying calls to premium phone numbers are generally recommended measures.

## Update (Oct-17-2022)

After this blog post had been published, AudioCodes Ltd. updated the Microsoft Teams Direct Routing configuration guideline and the configuration wizard template. Now, the updated [guideline](https://www.audiocodes.com/media/13253/connecting-audiocodes-sbc-to-microsoft-teams-direct-routing-enterprise-model-configuration-note.pdf) and the wizard template are including more detailed classification rules. These rules limit incomming SIP Messages, received at the configured Microsoft Teams SIP interface, to the documented Microsoft Teams SIP proxy IP address ranges only:

![Updated Classification Rules](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Updated Classification Rules_

In addition, the section `Configure Firewall Settings` is no longer marked as `Optional`:

![Updated Firewall Settings Section](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Updated Firewall Settings Section_

We welcome these updates provided by AudioCodes Ltd. and recommend implementing them in addition to the already referred firewall settings.

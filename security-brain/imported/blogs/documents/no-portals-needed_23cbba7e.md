---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-24_no-portals-needed.md
original_filename: 2023-04-24_no-portals-needed.md
title: No Portals Needed
category: documents
detected_topics:
- mfa
- sso
- saml
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- mfa
- sso
- saml
- ssrf
- command-injection
- otp
language: en
raw_sha256: 23cbba7e6b49ddd45c2fee3ff16a3e0205c01291afa0ba25e62c61fe5341c1dc
text_sha256: 2f34bdb6b61ce22439c1d6f53822e3028c3d7769fcd6fb4fd8123f3c1f60409e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# No Portals Needed

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-24_no-portals-needed.md
- Source Type: markdown
- Detected Topics: mfa, sso, saml, ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `23cbba7e6b49ddd45c2fee3ff16a3e0205c01291afa0ba25e62c61fe5341c1dc`
- Text SHA256: `2f34bdb6b61ce22439c1d6f53822e3028c3d7769fcd6fb4fd8123f3c1f60409e`


## Content

---
title: "No Portals Needed"
page_title: "Bypassing GlobalProtect VPN MFA | Chen Levy | CYE | CYESEC"
url: "https://medium.com/cyesec/no-portals-needed-79995d8f7e62"
authors: ["Chen Levy Ben Aroy"]
bugs: ["2FA / MFA bypass", "Security misconfiguration"]
publication_date: "2023-04-24"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1228
scraped_via: "browseros"
---

# No Portals Needed

Press enter or click to view image in full size
No Portals Needed
Abusing a misconfiguration to bypass Palo Alto GlobalProtect VPN multi-factor-authentication.
Chen Levy Ben Aroy
Follow
8 min read
·
Apr 24, 2023

82

3

Introduction

The adversary mindset is a must-have quality for offensive operators in a Red Team. Every assessment brings its own limitations and “trophies.” The operators have to align with the environment’s limitations such as: secure tiering models, cutting-edge endpoint detection and response solutions, etc. Having the ability to adapt and embrace these so-called “obstacles” let the team members operate in the best and most creative ways possible to achieve control over critical assets and environments.

In a recent assessment, as in any other Red Team engagement, it started with the reconnaissance phase. During this phase, we gather internet-facing assets that are associated with the customers’ organization. After collecting and analyzing the recon data, we realized that the attack surface was pretty narrow, with no exploitable versions of internet facing software, and social engineering was reserved as the last resort. Some assets we found were determined as GlobalProtect VPN portals. After multiple tries of connection and authentication, it was determined that the authentication to the GlobalProtect portal was enforced with multi-factor authentication. As this was our only way to gain a foothold in the organization’s internal environment, we decided to further investigate the GlobalProtect interfaces.

GlobalProtect VPN Basics

Palo Alto’s GlobalProtect VPN is based on HTTPS requests and responses and XML data sets of configurations. The VPN has two main components that are engaged by an end user: the portal and the gateway. The portal’s job is: first, to act as a web-server that hosts the GlobalProtect’s client for Windows and MacOS. Second, it provides the official Palo Alto’s client configurations and the list of available gateways. The gateway’s purpose is to provide the raw SSLVPN tunnel we know and love, to secure the end user session to the enterprise.

The official Palo Alto’s client’s flow is:

Login to the portal
Get a configuration and a list of gateways
The gateway is selected automatically or by the user’s manual selection
Login to the gateway
Provide Host Information Profile (HIP) report
If all goes right, connect to VPN and secure session
Press enter or click to view image in full size
GlobalProtect connection flow (Source: docs.paloaltonetworks.com)

When trying to connect to the customer’s environment with the official client, we were prompted for an MFA token. But what if we tried to connect to the gateway, while bypassing the portal?

TL;DR It seems that enforcing MFA is crucial in both the portal and gateway as these are independent components.

Diving In to the Authentication Flow

When first connecting with the official GlobalProtect’s client, we see the first POST request being sent to the portal by its URL which points to /global-protect/prelogin.esp

The requests will be appended with the client’s environment variables such as: ”kerberos-support”, ”client-os”,“os-version”, “ipv6-support”, etc.

The server will then respond with a “PHPSESSID” cookie and an XML data-set with the status of the request, and if successful, it will also attach the login labels for the client, such as: “Enter MFA token” or “Enter Password.”

Press enter or click to view image in full size
First request made by the official GlobalProtect client

After the user enters credentials, the client will send the next request to /global-protect/getconfig.esp, sending the same information as the previous request with the credentials attached to it.

If authentication is successful, the server will send an XML data-set that includes: the server configuration, version, the client’s host information to collect, and if it exists - custom checks to perform. Custom checks are special compliance checks created by the VPN administrators, such as special registry keys the machine has to set to be compliant. Also included in the response is the list of gateways and their configurations.

Press enter or click to view image in full size
The server’s response to the second request results in a list of gateways and other configuration variables

The next request aims for the gateway, and the same authentication sequence as when the portal begins, but this time to the gateway’s endpoint: /ssl-vpn/prelogin.esp.

The pre-login phase is the same as with the portal, sending the client’s environment variables to the server. The server responds with a status, the authentication form’s labels and sets a “PHPSESSID” cookie.

Press enter or click to view image in full size
A successful request to the gateway yields a Success status and login labels

After receiving a session ID and authenticating, the next request is what differentiates between the portal and gateway authentication. The request is sent to /ssl-vpn/login.esp, with the user’s credentials appended, and in response the server sends multiple untitled arguments that look like: MTU, DNS domain, the “authcookie” that will be used in the next request, and more configuration variables.

Press enter or click to view image in full size
The login request to the gateway results in the server responding in multiple unknown arguments

The client then parses the XML data set correctly and append these variables, including the “authcookie”, to its next request to /ssl-vpn/getconfig.esp. The server responds with a response status and more configuration variables, but this time these are all titled and more variables are sent, such as ciphers to use, protocols of the gateway, preferred tunnel IP to use, etc.

Press enter or click to view image in full size
The request contains the “authcookie” received in the last server response (in red) and results in multiple configuration arguments

The final phase is a GET request to /ssl-tunnel-connect.sslvpn, with the user name and “authcookie” appended. This initiates the VPN session with a server response of “START_TUNNEL”.

Press enter or click to view image in full size
A successful connection was made and a tunnel interface was set up
One Misconfiguration Away from Bypassing MFA

As we saw in the previous chapter, the VPN sequence relies on two independent components that require two separate authentication flows.
Because these are independent, each of the authentication sequences could be engaged manually. This means that if we already know the gateway’s information, there is no need to pass-through the portal to get a list of gateways, we could only authenticate once, with valid credentials, and still be able to get a VPN connection.

Get Chen Levy Ben Aroy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In this recent assessment, we found that an MFA token is requested by the portal only, while the gateway asks for domain credentials. The IT department and Palo Alto GlobalProtect developers, counted on their in-house client use only, with no external adaptation in mind. While not enforcing MFA at the gateway is safe when using the official client, it is not safe when using other open-source or self-built clients. This is the part where it is also important to mention that this is caused by a misconfiguration only, rather than a vulnerability in Palo Alto’s VPN solution.

Luckily, the guys from InfraDead already did their research on GlobalProtect while they developed the open-source VPN client OpenConnect which supports multiple VPN vendors and technologies, which among them is Palo Alto GlobalProtect. In their documentation they elaborate:

“GlobalProtect VPNs actually contain two different server interfaces: portals and gateways. Most VPNs have one portal server and one or more gateway servers; the server hosting the portal interface often hosts a gateway interface as well, but not always. The portal interface mostly sends centrally-imposed security/lockdown settings for the official client software to follow. The only information sent by the portal that’s clearly useful to a VPN client like OpenConnect (which tries to give full control to the end user) is the list of gateways.

Some GlobalProtect VPNs are configured in such a way that the client must authenticate to the portal before it can access the gateway, while with other VPNs no interaction with the portal is necessary. In order to replicate the behavior of the official clients, OpenConnect first attempts to connect to the portal interface of the specified server.

If--usergroup=gateway is specified (or, equivalently, /gateway is appended to the server URL, e.g. https://vpn.company.com/gateway), then OpenConnect will attempt to skip the portal interface and connect immediately to the gateway interface. This is useful if the GlobalProtect VPN portal is misconfigured, such as by not offering the desired gateway server in the list it provides.”

This OpenConnect feature was magical to find as it saved us expensive research and coding time.

No Need for Portals Here…

Because the portal and the gateway were running on the same interface, there was no need to find other gateways (such as other ports on the same server or other external assets).

We used the OpenConnect client to bypass the portal and connect to the gateway first:
openconnect --protocol=gp --user=user_name https://vpn.company.com/gateway

The /gateway endpoint probably does not exist on the server, though it is discarded while the client runs and only serves as a flag so it will start communicating the /ssl-vpn/ endpoint rather than the /global-protect/ ones.

The VPN client prompts us for domain credentials:

Press enter or click to view image in full size
Connecting to the GlobalProtect gateway, prompts us with domain credentials only

Success! We are successfully connected to the internal network!

Press enter or click to view image in full size
Connection to the VPN is successful, though there is no connection to some internal machines

In this assessment, although it was possible to connect and communicate with the organization’s domain controllers, we couldn’t communicate with many services and domain machines as we could from the official client. After researching the different behaviors between different operating systems and clients, we realized that a valid HIP report should be submitted. The OpenConnect developers, here too, were genius enough to automate a shell script that creates a fake HIP report. We copied the one from our Windows machine (By entering to the settings pane of the official client, in the Troubleshooting tab, click the “Collect Logs” button. It will create a GlobalProtectLogs.zip file in the User directory. Inside the compressed folder the HIP report could be found as pan_gp_hrpt.xml”)
to our ../openconnect/trojans/hipreport.sh.

Press enter or click to view image in full size
Copied a benign HIP report from a Windows machine

Trying to submit our fake report:
openconnect --protocol=gp --user=username --csd-wrapper=trojans/hipreport.sh https://vpn.company.com/gateway and trying to reach the segmented service:

Press enter or click to view image in full size
HIP report was submitted successfully and connection to segmented resources is now available

We successfully bypassed both MFA and machine segregation!

From here, connecting to Active Directory, and further exploitation of the organization’s internal environment was possible.

Quick Fix

Mitigation of this misconfiguration is quite easy:

MFA should be enforced on both the portal AND gateway(s)
Monitor direct SSLVPN connections to the gateway
Separate the portal and gateway(s) to different interfaces and ports
If possible, allow SAML authentication only
Summary

As Red Team operators, we always aim to give our customers an added value. Every assessment has its own obstacles, but being extra vigilant when everything seems secure goes a long way. At first, it seemed like there was no external asset to attack and MFA was enforced on every interface exposed to the internet, including the GlobalProtect VPN. However, diving deeper into the interface revealed that relying on a “peace-time” user-interaction is dangerous.

Although GlobalProtect’s client is safe and could not be altered to be used differently, other VPN programs can be. The portal and gateways are independent components, which means we can authenticate each component individually, while not enforcing MFA on the gateway could lead an attacker to a foothold in the internal enterprise environment.

Written as part of the CYE “CyberTalks” series, to share personal knowledge gained from our real-world experience.

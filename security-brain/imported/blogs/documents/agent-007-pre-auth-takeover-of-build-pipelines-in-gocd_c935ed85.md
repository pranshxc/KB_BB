---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-27_agent-007-pre-auth-takeover-of-build-pipelines-in-gocd.md
original_filename: 2021-10-27_agent-007-pre-auth-takeover-of-build-pipelines-in-gocd.md
title: 'Agent 007: Pre-Auth Takeover of Build Pipelines in GoCD'
category: documents
detected_topics:
- api-security
- command-injection
- sso
- ssrf
- xss
- path-traversal
tags:
- imported
- documents
- api-security
- command-injection
- sso
- ssrf
- xss
- path-traversal
language: en
raw_sha256: c935ed85ceee0a3fa29caefc3fe4f77001d8c2fedb63e4077f664bd44485f707
text_sha256: 1fd0a168b632431214cf6cf10ffd65345b8dd380c475f42dc341a1db2da4695f
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Agent 007: Pre-Auth Takeover of Build Pipelines in GoCD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-27_agent-007-pre-auth-takeover-of-build-pipelines-in-gocd.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, sso, ssrf, xss, path-traversal
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c935ed85ceee0a3fa29caefc3fe4f77001d8c2fedb63e4077f664bd44485f707`
- Text SHA256: `1fd0a168b632431214cf6cf10ffd65345b8dd380c475f42dc341a1db2da4695f`


## Content

---
title: "Agent 007: Pre-Auth Takeover of Build Pipelines in GoCD"
page_title: "Agent 007: Pre-Auth Takeover of Build Pipelines in GoCD | Sonar"
url: "https://blog.sonarsource.com/gocd-pre-auth-pipeline-takeover"
final_url: "https://www.sonarsource.com/blog/gocd-pre-auth-pipeline-takeover/"
authors: ["Sonar (@SonarSource)"]
programs: ["GoCD"]
bugs: ["Broken authentication", "Broken authentication"]
publication_date: "2021-10-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3211
---

## TL;DR overview

  * GoCD contains a pre-authentication remote code execution vulnerability that allows unauthenticated attackers to take over CI/CD pipelines by exploiting a flaw in the agent registration or API endpoint.
  * Because GoCD agents execute pipeline jobs with the permissions of the CI service account, a successful attack can result in full control over build processes, secrets, and deployment targets.
  * The flaw does not require any valid credentials, making it a high-severity risk for organizations exposing GoCD to untrusted networks or the internet.
  * Organizations using GoCD should apply the patch immediately, restrict network access to the GoCD server, and audit recent pipeline executions for signs of unauthorized activity.

GoCD, written in Java, is a popular CI/CD solution with a large range of users from NGOs to Fortune 500 companies with billions of dollars in revenue. Naturally, this makes it a critical piece of infrastructure and an extremely attractive target for attackers. In order to automate build and release processes, a centralized CI/CD solution has access to various production environments and private source code repositories. 

With so much trust and responsibility placed in CI/CD solutions, a compromise of any part of the software delivery pipeline would be detrimental to a company running GoCD. An attacker in control of any component within a release pipeline could leak intellectual property or include backdoors in software that the company distributes to the public or uses internally. As an example, think about the [SolarWinds hack](https://blog.qualys.com/vulnerabilities-threat-research/2021/01/04/technical-deep-dive-into-solarwinds-breach), where attackers gained access to the software delivery pipeline and added a backdoor to critical software, leading to one of the most impactful supply-chain attacks thus far.

In this blog post, we detail a vulnerability that lets unauthenticated attackers leak highly sensitive information from a vulnerable GoCD Server instance, including all encrypted secrets stored on the server (CVE-2021-43287). Furthermore, the vulnerability can be used to impersonate a GoCD Agent, i.e. GoCD worker, and take over software delivery pipelines. We will also discuss how this vulnerability could be used to take over a GoCD server and execute arbitrary code on it. The vulnerability has been detected in GoCD’s Java code with SonarSource’s taint analysis.

[**Open vulnerability on SonarQube Cloud**](https://sonarcloud.io/project/issues?branch=release-vulnerable2&id=SonarSourceResearch_gocd&open=AXydEiM_1tRJe0-g5GyX&resolved=false&sonarsourceSecurity=path-traversal-injection&types=VULNERABILITY)

## Impact

We discovered and disclosed multiple vulnerabilities to the GoCD Security Team. The vulnerability discussed in this blog post is related to broken authentication and allows an unauthenticated attacker to view highly sensitive information and read arbitrary files on a GoCD server instance. We will discuss how attackers might abuse this vulnerability to gain access to authenticated attack surface. In a follow-up blog post, we are going to detail how attackers can abuse authenticated attack surfaces to gain RCE impact on a GoCD Server instance by exploiting other vulnerabilities we discovered.

We rate the vulnerability presented in this blog post as **highly critical** , since an unauthenticated attacker can extract all tokens and secrets used in all build pipelines. For instance, attackers could leak API keys to external services such as Docker Hub and GitHub, steal private source code, get access to production environments, and overwrite files that are being produced as part of the build processes, leading to supply-chain attacks.

All GoCD instances within the version range [v20.6.0](https://www.gocd.org/releases/#20-6-0) \- [v21.2.0](https://www.gocd.org/releases/#21-2-0) are affected, i.e. all GoCD instances that include commits [291d3d3485da818cd9067e487850c8153c6ba1e7](https://github.com/gocd/gocd/commit/291d3d3485da818cd9067e487850c8153c6ba1e7) and [dd13d401f4b8cad1e7ef3846a86f11f6d2a2f9f2](https://github.com/gocd/gocd/commit/dd13d401f4b8cad1e7ef3846a86f11f6d2a2f9f2). The vulnerability was fixed in version [v21.3.0](https://www.gocd.org/releases/#21-3-0).

The vulnerabilities require no prior knowledge of a targeted GoCD server instance. They work on default configurations and can be triggered even if authentication mechanisms are deployed for a GoCD server instance. For this reason, we highly recommend applying the available patches as quickly as possible. Although it is best practice to host CI/CD instances on an internal network, we observed hundreds of instances exposed to the internet.

Our exploit video demonstrates how a GoCD instance can be easily breached remotely:

## Technical Details

In the following sections, we go into the technical details of the vulnerability. We first provide a bit of background information on how GoCD works on a high level and then break down the root cause of the vulnerability. We then examine strategies that could be used by attackers for compromising the GoCD Server with the acquired information in the first step.  

### Background - GoCD Server and Agent Architecture

Typically, a company would manage its source code in a version control system, such as git. Whenever code changes or a release is being made, the GoCD server is aware of it and automatically runs one or more build and release pipelines associated with the source repository. A pipeline in GoCD is simply a collection of tasks that need to be run in a certain order. A high-level example of a pipeline could be:

  1. Compile the source code
  2. Run unit and integration tests
  3. Build a Docker image and push it to the company’s registry

In order to delegate these workloads, the GoCD Server assigns the pipeline run to one or more GoCD Agents. An Agent in the GoCD ecosystem is simply a worker that pings the server regularly and checks if any work is assigned to it. If there is, the GoCD Server replies with the information the Agent requires: commands to run and environment variables to apply. Typically those environment variables are going to include secrets and access tokens for services the pipeline needs to access.

The GoCD Agents are authenticated to the GoCD server via an access token that the server assigns to them. By default, when a new agent is launched, it contacts the GoCD Server and registers to it. It is then up to an administrator to enable the Agent so that it becomes active and is part of the workload rotation.  

### Broken Authentication in Business Continuity Add-On

GoCD utilizes the popular Spring framework and relies on the FilterChainProxy to ensure correct authentication for various endpoints. The following code snippet shows how different filters are added to the filter chain, along with the URLs that they are registered for:

Copy to clipboard
  
  
  25  @Component("authenticationFilterChain")
  26  public class AuthenticationFilterChain extends FilterChainProxy {
  27 
  28  @Autowired
  29  public AuthenticationFilterChain(
  30  @Qualifier("agentAuthenticationFilter") Filter x509AuthenticationFilter,
  31  // ...
  32  @Qualifier("accessTokenAuthenticationFilter") Filter accessTokenAuthenticationFilter,
  33  @Qualifier("assumeAnonymousUserFilter") Filter assumeAnonymousUserFilter) {
  34  super(FilterChainBuilder.newInstance()
  35  // X509 for agent remoting
  36  .addFilterChain("/remoting/**", x509AuthenticationFilter)
  37 
  38  // For addons
  39  .addFilterChain("/add-on/**", assumeAnonymousUserFilter)
  40 
  41  // ... more filters omitted

When an HTTP request is made to a GoCD server, the Spring framework maps the request URL to a list of filters responsible for this request before passing execution to a controller. The code snippet above shows how all request paths that begin with `/add-on/` are filtered with the `assumeAnonymousFilter` in line 39. As the name suggests, this filter does not actually perform authentication and lets any request through. This means endpoints exposed by addons are responsible for ensuring correct authentication and permissions themselves, as any unauthenticated attacker could access them.

A quick investigation showed that this behavior had not always been the case; commit [291d3d3485da818cd9067e487850c8153c6ba1e7](https://github.com/gocd/gocd/commit/291d3d3485da818cd9067e487850c8153c6ba1e7) changed it. Prior to this commit, these endpoints were accessible to authenticated users only. We realized that this breaking change could lead to add-ons being vulnerable to unauthenticated attacks, as the developers of add-ons might not be aware of this transfer of responsibility.

We decided to scan some of the most popular add-ons with SonarQube Cloud and discovered an arbitrary File Read vulnerability in the [Business Continuity](https://extensions-docs.gocd.org/business-continuity/current/) add-on for GoCD. This add-on is installed and enabled by default since version [v20.6.0](https://www.gocd.org/releases/#20-6-0). The vulnerable code is shown in the next code snippet:

Copy to clipboard
  
  
  119  @RequestMapping(value = "/plugin", method = RequestMethod.GET)
  120  public void getPluginFile(
  121  @RequestParam("folderName") String folderName,
  122  @RequestParam("pluginName") String pluginName,
  123  HttpServletResponse response) {
  124  String pluginFolderPath = isBlank(folderName) || folderName.equalsIgnoreCase("bundled") ? systemEnvironment.getBundledPluginAbsolutePath() : systemEnvironment.get
  ExternalPluginAbsolutePath();
  125  File pluginFile = new File(pluginFolderPath, pluginName);
  126  serveFile(pluginFile, response, "application/octet-stream");
  127  }

The pluginName parameter, which can be controlled by an attacker, is passed into the constructor of a new File object. This file is then read and served to the user making the request. By setting the `pluginName` parameter to, for example, `/../../../../../../../../etc/passwd,` it is possible to read the contents of the `/etc/passwd` file of a GoCD server. The injection of unsanitized user input into a sensitive API, such as a file opener, can be automatically detected with our taint analysis technology in SonarQube Cloud.

[**Open vulnerability on SonarQube Cloud**](https://sonarcloud.io/project/issues?branch=release-vulnerable2&id=SonarSourceResearch_gocd&open=AXydEiM_1tRJe0-g5GyX&resolved=false&sonarsourceSecurity=path-traversal-injection&types=VULNERABILITY)

There were two more endpoints exposed that leak extremely sensitive information. They are shown below:

Copy to clipboard
  
  
  92  @RequestMapping(value = "/cruise_config", method = RequestMethod.GET)
  93  public void getLatestCruiseConfigXML(HttpServletResponse response) {
  94  serveFile(ConfigFileType.CRUISE_CONFIG_XML.load(systemEnvironment), respon
  se, "text/xml");
  95  }
  ...
  102  @RequestMapping(value = "/cipher.aes", method = RequestMethod.GET)
  103  public void getLatestAESCipher(HttpServletResponse response) {
  104  serveFile(ConfigFileType.AES_CIPHER.load(systemEnvironment), response, "te
  xt/plain");
  105  }

The first, `/cipher.aes`, leaks an encryption key that is used to encrypt sensitive secrets, such as access tokens. The second, `/cruise_config`, leaks the main configuration file of a GoCD server. This XML config file contains all environment variables for all pipelines. Some of the environment variables are encrypted and contain secrets, but can be decrypted with the leaked AES cipher. This config also contains other sensitive data which we will discuss in the next section.

To summarize this vulnerability, an attacker can extract all secrets that are available to a GoCD server with two requests: one for stealing the encryption key and one for obtaining all the encrypted secrets. The attacker can also read arbitrary files on the GoCD server and can thus read git credentials, the main database file (Hibernate is used by default,) and other sensitive files.

### The GoCD Secrets

In the previous section, we discussed how attackers can abuse the missing authentication on endpoints belonging to the Business Continuity Add-On to leak highly sensitive information. This section discusses the secrets that could be leaked and how attackers might abuse them to attack the GoCD server. This is done by obtaining a valid session, either as an administrator or as an Agent. In a follow-up blog post, we will detail how we found vulnerabilities in the authenticated attack surface and how we managed to get an RCE chain working.

Let’s first look at some configuration options in the main configuration file of a GoCD server. The following snippets show examples of configurations that are included by default:

Copy to clipboard
  
  
  <server 
  agentAutoRegisterKey="xxx-xxx-xxx-xxx-xxx-xxx" 
  webhookSecret="xxx-xxx-xxx-xxx-xxx-xxx" 
  tokenGenerationKey="xxx-xxx-xxx-xxx-xxx-xxx">

**agentAutoRegisterKey**

This secret can be used to register new GoCD workers, or GoCD Agents as they are called in the GoCD ecosystem, without requiring the approval of an administrator. This means an attacker can register multiple malicious Agents into the worker rotation and hijack build pipelines. It also means that they gain access to an authenticated attack surface reachable from a GoCD Agent.  

**tokenGenerationKey**

[Previous work by Pulse Security](https://pulsesecurity.co.nz/advisories/GOCD-Multiple-Vulnerabilities) has shown how this token could be used to impersonate GoCD Agents that are already in the worker rotation and approved by administrators.  

**webhookSecret**

The webhook secret is used to authenticate webhook requests coming from GitHub, GitLab, or BitBucket. Knowledge of this secret could be abused to trigger pipeline runs. It also opens up more, previously unreachable attack surfaces.  

**Authentication configuration**

By default, GoCD is shipped with two authentication plugins: Password and LDAP-based authentication. The following sections demonstrate how a password file-based authentication might be configured:

Copy to clipboard
  
  
  <authConfig id="file" pluginId="cd.go.authentication.passwordfile">
  <property>
  <key>PasswordFilePath</key>
  <value>/opt/godata/password.txt</value>
  </property>
  </authConfig>

The snippet above shows how the GoCD server is configured to read passwords from the `/opt/godata/password.txt` file. This file follows the  _htpasswd_ file format of having a username and hashed password. According to the [plugin’s documentation](https://github.com/gocd/gocd-filebased-authentication-plugin#generating-passwords-using-htpasswd), the password hashes are either stored in SHA1, Bcrypt, or PBKFD2 format.

Alternatively, GoCD also supports LDAP authentication by default. In a worst-case scenario, an attacker could get access to the company’s LDAP by leaking the LDAP password from the server.  

## Patch

The GoCD Security Team responded very quickly. Patches for both vulnerabilities were released only two days after reporting them and are included in version [v21.3.0](https://www.gocd.org/releases/#21-3-0). The vulnerability was addressed by removing the Business Continuity add-on from the core altogether.

Due to the severity of this issue, we recommend patching these vulnerabilities as soon as possible. If no update can be run immediately, we recommend setting up firewall rules to prevent any HTTP requests to the `/add-on/**` and/or `/add-on/business-continuity/**` endpoints.

## Timeline

**Date**| **Action**  
---|---  
2021-10-16| We report the exposed add-on endpoints to GoCD on HackerOne  
2021-10-18| We report other findings to GoCD on HackerOne  
2021-10-18| GoCD confirms all issues  
2021-10-18| GoCD pushes patches for the exposed add-on endpoints and for other issues to GoCD’s GitHub repository  
2021-10-22| GoCD gives a heads-up about an important Security Fix coming up on their public Google Forum  
2021-10-24| GoCD sends us the experimental installer for release v21.3.0  
2021-10-25| We verify the new version is secured against these vulnerabilities  
2021-10-25| According to GoCD, a warning is sent out to the GoCD mailing list  
2021-10-26| GoCD releases version v21.3.0  
  
## Summary

In this blog post, we broke down a vulnerability that enables attackers to view highly sensitive information from a GoCD server, without any authentication. This vulnerability occurs due to a breaking change related to authentication in add-ons that was introduced one year ago. We highly recommend all users running GoCD to upgrade to the latest version immediately!

We would like to thank the GoCD Security Team who have been exceptionally responsive in the disclosure process. They reacted very quickly and worked with us on patching the vulnerability efficiently.

We will follow up with a second blog post in which we will describe a Cross-Site Scripting vulnerability on the agent attack surface and two additional findings leading to remote code execution. Stay tuned!

## Related Blog Posts

  * [Zimbra 8.8.15 - Webmail Compromise via Email](https://blog.sonarsource.com/zimbra-webmail-compromise-via-email)
  * [Bitbucket 6.1.1 Path Traversal to RCE](https://blog.sonarsource.com/bitbucket-path-traversal-to-rce)
  * [MyBB Remote Code Execution Chain](https://blog.sonarsource.com/mybb-remote-code-execution-chain)
  * [WordPress 5.1 CSRF to Remote Code Execution](https://blog.sonarsource.com/wordpress-csrf-to-rce)

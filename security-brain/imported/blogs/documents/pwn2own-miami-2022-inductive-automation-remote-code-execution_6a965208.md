---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-22_pwn2own-miami-2022-inductive-automation-remote-code-execution.md
original_filename: 2022-07-22_pwn2own-miami-2022-inductive-automation-remote-code-execution.md
title: 'Pwn2Own Miami 2022: Inductive Automation Remote Code Execution'
category: documents
detected_topics:
- sso
- command-injection
- oauth
- access-control
- ssrf
- otp
tags:
- imported
- documents
- sso
- command-injection
- oauth
- access-control
- ssrf
- otp
language: en
raw_sha256: 6a965208bec5d4eae7dc4dc759d7836cadb1a8ee3774deebab2e4461860aded0
text_sha256: f0629632368f4a0ec6f5b5183d03936b88ff5cdfe852d95bc842b5cb739d8d44
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Own Miami 2022: Inductive Automation Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-22_pwn2own-miami-2022-inductive-automation-remote-code-execution.md
- Source Type: markdown
- Detected Topics: sso, command-injection, oauth, access-control, ssrf, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `6a965208bec5d4eae7dc4dc759d7836cadb1a8ee3774deebab2e4461860aded0`
- Text SHA256: `f0629632368f4a0ec6f5b5183d03936b88ff5cdfe852d95bc842b5cb739d8d44`


## Content

---
title: "Pwn2Own Miami 2022: Inductive Automation Remote Code Execution"
page_title: "Pwn2Own Miami 2022: Inductive Automation Ignition Remote Code Execution | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2022-07-inductive-automation-ignition-rce/"
final_url: "https://defion.security/en/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["Inductive Automation Ignition"]
bugs: ["RCE", "Authentication bypass"]
publication_date: "2022-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2417
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Pwn2Own Miami 2022: Inductive Automation Ignition Remote Code Execution

Pwn2Own 22 July 2022 · 7 min read

# Pwn2Own Miami 2022: Inductive Automation Ignition Remote Code Execution

This write-up is part 2 of a series of write-ups about the 5 vulnerabilities we demonstrated last April at Pwn2Own Miami. This is the write-up for a Remote Code Execution vulnerability in Inductive Automation Ignition, by using an authentication bypass (CVE-2022-35871).

> [](https://twitter.com/thezdi/status/1516479026248003594)

The cause of this vulnerability was a weak authentication implementation when using Active Directory single sign-on. We combined this with intended(?) functionality that allowed us to execute Python code on the server (as `SYSTEM`).

## Background

Inductive Automation Ignition is an application that was part of in the "Control Server" category. Control servers are used to supervise and communicate with lower-level devices, such as PLCs. This makes them a critical element in any ICS network.

Ignition is organized in different projects, which are managed using a web interface. Each project needs a user source which determines the authentication and authorization for that project. Authentication can be internal, using a database, or based on Active Directory (which has some sub-options that determine how authorization is handled). The projects can then be used from Ignition Perspective, a desktop application which communicates with the Ignition server through the gateway API.

![](/images/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/usersources.png)

When one of the AD based user sources is configured, it offers an option named "SSO Enabled".

![](/images/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/ssoenabled.png)

To configure an AD based user source, the server needs to be configured with an AD account, the IP address of a domain controller and the Active Directory domain name. The AD account is used to set up an LDAP connection to the AD server for the application itself.

## Vulnerability

### Auth bypass

While, looking at the decompiled Java code (`Ignition/lib/core/gateway/gateway-api-8.1.16.jar`) for how the SSO authentication is handled in the gateway API, we noticed that the function implementing SSO is a lot simpler than we expected.

`com.inductiveautomation.ignition.gateway.authentication.impl.ActiveDirectoryUserSource.class`:
  
  
  protected AuthenticatedUser authenticateAdSso(AuthChallenge challenge) throws Exception {
  String ssoUname = (String)challenge.get(User.Username);
  String ssoDomain = (String)challenge.get(ADSSOAuthChallenge.ADDomain);
  if (StringUtils.isBlank(ssoUname)) {
  this.log.debug("SSO username is blank.");
  return null;
  } 
  if (StringUtils.isBlank(ssoDomain)) {
  this.log.debugf("SSO domain is blank for user '%s'", new Object[] { ssoUname });
  return null;
  } 
  if (ssoDomain.equalsIgnoreCase(this.domain)) {
  User existingUser = this.userSource.findSSOUser(ssoUname);
  if (existingUser != null)
  return (AuthenticatedUser)new BasicAuthenticatedUser(existingUser, new Date()); 
  this.log.debug(String.format("Existing user was not found for username '%s'", new Object[] { ssoUname }));
  } else {
  this.log.debug(String.format("SSO domains did not match! Compared '%s' and '%s'", new Object[] { this.domain, ssoDomain }));
  } 
  return null;
  }

This function receives an `AuthChallenge` object (essentially a JSON dictionary). It checks that it contains a key for the username and a key for the SSO domain. Then it compares the value for the SSO domain to the configured Active Directory domain name. If it matches, it looks up the username using LDAP and, if found, returns it as an `AuthenticatedUser` object.

There's no check here for a password, token, signature, or anything like that. The only data that needs to be submitted to the server is the **username** and the **Active Directory domain name**. In other words, the vulnerability here is that there is no SSO implementation at all! It's not even clear to us what type of SSO was intended to be used here, probably Kerberos?

### RCE

To go from an authenticated user to code execution, we used what we assume is intended functionality that allows us to evaluate Python on the server. There is a `ScriptInvoke` gateway API endpoint with an `execute` function. Authenticated users can submit Python code to this endpoint, which is executed on the server with the same privileges as the server (on Windows, this is `SYSTEM`). Ignition Designer offers the ability to execute scripts on the server in response to specific events or regular intervals. This does not appear to require any special role or permissions, so this design looks risky to us, but it does seem to function as designed.

## Exploit

To exploit the auth bypass, the server needs to be configured using AD authentication with SSO enabled. To perform the attack, we need the following information:

  1. The name of a project using this authentication method.
  2. The name of an existing AD user.
  3. The name of the AD domain.

It turns out that the first two were easy to do. There is an unauthenticated API endpoint on the admin interface returning the list of all projects:
  
  
  http://<server IP>/data/perspective/projects

For the username, this simply had to be any existing AD user, regardless of permissions in AD or Ignition. So, we could just use "Administrator", as that user will always exist in AD.

This only leaves the AD domain name, which we didn't find a way to obtain automatically from Ignition. In practice, that value should be easy to obtain when attacking a company, especially if the attacker is already on the company's internal network. In most cases this would just be the company's primary domain name, or the value might leak in email headers, file metadata, etc.

Finally, we used a reverse shell implemented in Python to setup a connection back to our attacker machine.

## Impact

Exploiting these vulnerabilities would grant us code execution on the machine hosting Ignition. This means that we could immediately manipulate or disrupt any process handled by or via this server. For example, we might be able to take over the communication with PLCs. In addition, the `SYSTEM` privileges would make it a fantastic starting point for further attacks other parts of the ICS or IT network.

In most cases, the Ignition server will not be exposed publicly to the internet, but only available on the internal ICS network. Therefore, this vulnerability would need to be combined with different vulnerabilities or attacks that grant us access to that network.

Your browser does not support the video tag. 

## The fix

This vulnerability was addressed by Inductive Automation in [versions 8.1.17 and 7.9.20](https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities) and assigned CVE-2022-35871. AD User Sources now disable the "SSO Enabled" setting automatically, unless a specific flag is set on the server (`-Dignition.enableInsecureAdSso=true`). In other words, Inductive Automation has chosen to deprecate this feature and [documented that it is dangerous to use](https://support.inductiveautomation.com/hc/en-us/articles/5979279808397-Active-Directory-SSO-Disabled-for-8-1-17-7-9-20-). This may seem like a disappointing fix, but implementing a secure SSO protocol would likely have taken a lot more time. This way the vulnerability can be avoided and, if desired, Inductive Automation could implement a secure SSO protocol without time pressure.

## Thoughts

When implementing security critical features (such as authentication), it is important to make a good design first. When authentication is combined with single sign-on and native applications this is even more important, as it can become very complex. With such a design, it becomes possible to catch mistakes before the features are implemented and to test each part separately.

While we of course don't know how this feature was built, we suspect no such design was created. Having a cryptographic protocol like Kerberos completely missing from the implementation should be quite obvious if the feature had been fully designed first.

Features allowing users to execute their own code on a server can be required in certain use-cases. However, the fact that this was available for a user who did not have any permissions or roles explicitly assigned to them is worrisome. This means that any authentication bypass immediately becomes an RCE vulnerability.

## Conclusion

We've demonstrated a remote code execution vulnerability against Inductive Automation Ignition. We found that authentication can be bypassed on a server with AD single sign-on enabled. The (cryptographic) protocol for handling single sign-on appears to not be implemented at all.

After bypassing the authentication, we used functionality of the server to execute arbitrary Python code with `SYSTEM` privileges to set up a reverse shell.

Big shout-out to Inductive Automation on handling this years edition of Pwn2Own! They published all details of all findings on their website, including a extensive write-up of their thoughts and fixes. Well done!

We thank Zero Day Initiative for organizing this years edition of Pwn2Own Miami, we hope to return to a later edition!

You can find the other four write-ups here:

  * [OPC UA .NET Standard Trusted Application Check Bypass](/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/)
  * [AVEVA Edge Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/)
  * [Unified Automation C++ Demo Server DoS](/en/research-labs/pwn2own-miami-2022-unified-automation-c-demo-server-dos/)
  * [ICONICS GENESIS64 Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution/)

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Red Teaming →](/en/pentesting-services/red-teaming-service/)

[← Back to Research Labs](/en/research-labs/)

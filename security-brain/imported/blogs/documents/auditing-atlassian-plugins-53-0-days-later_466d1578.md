---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-02_auditing-atlassian-plugins-53-0-days-later.md
original_filename: 2024-08-02_auditing-atlassian-plugins-53-0-days-later.md
title: Auditing Atlassian Plugins, 53 0-Days Later
category: documents
detected_topics:
- api-security
- xss
- supply-chain
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- api-security
- xss
- supply-chain
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 466d1578162f08c995aded8a9402f868c10d8702b299aebe2568fa23887903ea
text_sha256: 73ae3b9b867c2603a071cd155c4d4b3aaa8b4eabb3da6d18a794af684d7984d0
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Auditing Atlassian Plugins, 53 0-Days Later

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-02_auditing-atlassian-plugins-53-0-days-later.md
- Source Type: markdown
- Detected Topics: api-security, xss, supply-chain, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `466d1578162f08c995aded8a9402f868c10d8702b299aebe2568fa23887903ea`
- Text SHA256: `73ae3b9b867c2603a071cd155c4d4b3aaa8b4eabb3da6d18a794af684d7984d0`


## Content

---
title: "Auditing Atlassian Plugins, 53 0-Days Later"
page_title: "Auditing Atlassian Plugins, 53 0-Days Later | cyllective's blog"
url: "https://cyllective.com/blog/posts/atlassian-audit-plugins"
final_url: "https://cyllective.com/blog/posts/atlassian-audit-plugins"
authors: ["cyllective (@cyllective)"]
programs: ["Atlassian"]
bugs: ["XSS"]
publication_date: "2024-08-02"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 110
---

# Auditing Atlassian Plugins, 53 0-Days Later

02\. Aug 2024, [#web](https://cyllective.com/blog/tags/web) [#cve](https://cyllective.com/blog/tags/cve) [#plugins](https://cyllective.com/blog/tags/plugins) [#atlassian](https://cyllective.com/blog/tags/atlassian)

**Table of Contents**

  * Enter The Marketplace
  * What’s inside a Plugin?
  * Macros
  * Hello World
  * Hello ~~World~~ XSS
  * XSS vs. Atlassian
  * Hunting for vulnerabilities
  * Atlpie - Our Audit Assistant
  * Ongoing Research
  * Conclusions

This post is the first part of our Atlassian plugin series. In this one, we focus on the general plugin ecosystem, specifically on the data center and server flavors for Atlassian products, and how we found multiple 0-day vulnerabilities. In the [second part](https://cyllective.com/blog/posts/atlassian-malicious-plugin/), we investigate the capabilities of a malicious plugin.

## Enter The Marketplace #

![Atlassian Marketplace](/blog/posts/atlassian-audit-plugins/marketplace.png)Atlassian Marketplace

If you start installing plugins, you’ll land on the [Atlassian marketplace ↗](https://marketplace.atlassian.com/) sooner or later. Let’s dive deeper into what the Atlassian marketplace has to offer and find out how well their security checks hold up, and how well our night’s sleep should be depending on how many plugins we have installed.

Atlassian has [requirements ↗](https://developer.atlassian.com/platform/marketplace/security-requirements/) to list a plugin inside its Marketplace. Those requirements are verified when an app is reviewed. According to Atlassian’s documentation of [How we review app listings ↗](https://developer.atlassian.com/platform/marketplace/creating-a-marketplace-listing/#how-we-review-app-listings):

> Security: Security checks and vulnerabilities scans completed to reduce risk and critical issues for customers.

The security review process itself is not publicly documented, meaning that it is unclear whether or not humans are involved in this process or how often these checks are performed. And, it is unclear if this process happens only on the initial submission or with every update of the plugin.

## What’s inside a Plugin? #

If you’ve ever downloaded a plugin from the Atlassian marketplace directly, you end up with either a `.jar` or `.obr` file. Contained in these archives lives the `atlassian-plugin.xml`, also known as the **plugin descriptor**.

Quoting from the [Atlassian’s Developer resource ↗](https://developer.atlassian.com/server/confluence/creating-your-plugin-descriptor/):

> Every plugin requires an atlassian-plugin.xml file. This is a single file also known as the plugin descriptor. The plugin descriptor is an XML file that describes a plugin and the modules contained within it for the host application.

The plugin descriptor contains one or many **plugin module** definitions. These are different types of functionality or logic the developer registers and implements to achieve the desired functionality.

Peeking at Atlassian’s Developer documentation about [Plugin modules ↗](https://developer.atlassian.com/server/framework/atlassian-sdk/plugin-modules/), one can get an overview of available **plugin module types**.

Some examples of Plugin module types include:

  * [REST Plugin Module ↗](https://developer.atlassian.com/server/framework/atlassian-sdk/rest-plugin-module): Expose RESTful API endpoints
  * [Servlet Plugin Module ↗](https://developer.atlassian.com/server/framework/atlassian-sdk/servlet-plugin-module/): Deploy Java servlets as part of a plugin
  * [Macro Plugin Module ↗](https://developer.atlassian.com/server/confluence/macro-module/): Implement Confluence Macros, i.e. parameterised HTML templates

The remainder of the archive (`.jar` or `.obr`) consists of the source code, implementing the main functionality, and the required first and third-party dependencies.

Let’s take a look at the macro module type as a concrete example.

## Macros #

In it’s simplest form, a macro generates HTML output which is then rendered at the location it was placed in the page editor. Optionally, it accepts user controlled parameters which the macro can use to perform conditional rendering or perform other kinds of logic.

### Hello World #

To better grasp how a macro is structured from a developer’s perspective, we are using the [Hello World Macro ↗](https://developer.atlassian.com/server/framework/atlassian-sdk/create-a-confluence-hello-world-macro/) from Atlassian’s Developer resources.
  
  
  package com.atlassian.tutorial.macro;
  
  import com.atlassian.confluence.content.render.xhtml.ConversionContext;
  import com.atlassian.confluence.macro.Macro;
  import com.atlassian.confluence.macro.MacroExecutionException;
  
  import java.util.Map;
  
  public class helloworld implements Macro {
  
  public String execute(Map<String, String> map, String body, ConversionContext conversionContext) throws MacroExecutionException {
  if (map.get("Name") != null) {
  return ("<h1>Hello " + map.get("Name") + "!</h1>");
  } else {
  return "<h1>Hello World!<h1>";
  }
  }
  
  public BodyType getBodyType() { return BodyType.NONE; }
  
  public OutputType getOutputType() { return OutputType.BLOCK; }
  }
  

As depicted in the code snippet above, the macro greets the world when the `Name` parameter is missing. Otherwise, the `Name` is used to greet that particular individual.

But where do the parameters come from?

The `Map<String, String> map` argument of the `execute()` method is used for passing user controlled parameters to the macro. This is done by registering a `<parameters>` element with `<parameter>` children inside the plugin descriptor:
  
  
  ...
  <xhtml-macro name="helloworld" class="com.atlassian.tutorial.macro.helloworld" key='helloworld-macro'>
  <description key="helloworld.macro.desc"/>
  <category name="formatting"/>
  <parameters>
  <parameter name="Name" type="string" />
  </parameters>
  </xhtml-macro>
  ...
  

After packaging the plugin and installing it on our Confluence test instance, we can add the macro to a page. As expected, the `Name` text field is present and allows the user to pass an arbitrary string:

![Hello world macro](/blog/posts/atlassian-audit-plugins/helloworld_macro.png)Hello world macro

### Hello ~~World~~ XSS #

User controlled input is passed into the macro via it’s parameters, which is then transformed or otherwise used to construct final HTML markup.

_At this point, your web security senses should start tingling…_

In our hello world macro example, there are no input validation or output sanitization mechanisms in place. Thus, by populating the `Name` parameter with an XSS payload, we can achieve stored XSS:

![XSS payload executed](/blog/posts/atlassian-audit-plugins/hello_xss.png)XSS payload executed

Due to potential lack of input validation in user controlled parameters or output sanitization, macros may quickly become a breeding ground for XSS vulnerabilities.

With a concrete example of an XSS vulnerability out of the way, let’s consider the impact of XSS vulnerabilities within an Atlassian plugin for a moment.

### XSS vs. Atlassian #

Looking at the headers that are set after authenticating against a standard Confluence installation, we are met with the session cookie marked as “httpOnly”. Cookies marked as “httpOnly” can not be accessed via JavaScript, which prevents an attacker from stealing the sessions of their victims through XSS attacks.

Despite the “httpOnly” session cookie, an attacker can still ride the victim’s session and perform actions on their behalf. This opens up some interesting attack venues the attacker can pursue to cause havoc.

Some of our favorites we have tinkered with thus far were:

  * Generating a personal access token in the name of the victim, granting temporary API access
  * Installing a [malicious plugin](https://cyllective.com/blog/posts/atlassian-malicious-plugin/), providing the attacker with backdoor access
  * Upgrading the attacker’s own account to that of an admin by calling backend APIs

Check out the video below for a quick demo on the account upgrade attack via XSS:

Your browser does not support the video tag.

_Psst…, interested in more XSS payloads for toying around with Atlassian?  
Check out our [XSS repository ↗](https://github.com/cyllective/XSS-Payloads/tree/main/Confluence)._

With our appetite whetted, we started out with a plan of attack for hunting down plugin vulnerabilities.

## Hunting for vulnerabilities #

Before we got started with hunting for plugin vulnerabilities, we quickly came up with a rough plan of attack. In essence, our plan consisted of the following high level steps that we repeated for each plugin:

  1. Download an Atlassian plugin from the marketplace
  2. Decompile the `.jar` or `.obr` file via [jadx ↗](https://github.com/skylot/jadx) to recover the plugin’s source code and assets
  3. Look at the plugin descriptor to determine available module types and get an initial overview
  4. Run static analysis ([semgrep ↗](https://github.com/semgrep/semgrep) and custom regex patterns via [ripgrep ↗](https://github.com/BurntSushi/ripgrep)) to find potential vulnerabilities
  5. Manually inspect the source code and review the static analysis output
  6. Once a vulnerability is suspected, install the plugin on a confluence test instance
  7. Perform dynamic testing against the plugin to confirm suspected vulnerabilities

  

After manually repeating the same steps over and over again, especially the initial part of downloading and decompiling plugins, we looked for ways to improve our process. We don’t want to spend our time with tedious tasks - we want automation to do that for us.

Having identified the steps that we can automate, we began tinkering on a tool for automating some of the more tedious tasks. Especially things like downloading and decompiling plugins and getting an overview of what a plugin contains were our pain points that we wanted to address.

### Atlpie - Our Audit Assistant #

While tinkering with some ideas, we came up with `atlpie`. This little guy aids us in our hunt for plugin vulnerabilities by automating the boring stuff.

`atlpie` provides us with an easy way to scrape plugins from the Atlassian marketplace and is capable of decompiling them via `jadx`. It also contains logic to extract helpful information, such as different module types contained within a plugin. Additionally, it parses servlet and REST API endpoints, giving us a decent initial overview.

![atlpie parser](/blog/posts/atlassian-audit-plugins/atlpie_preview.png)atlpie parser

 _`atlpie` is still under active development, but we we plan on releasing it to the general public under a permissive open source license in the foreseeable future, so stay tuned for that._

## Ongoing Research #

With the help of `atlpie`, static analysis tools, manual code review and dynamic tests, we are still in an ongoing process of auditing all kinds of Atlassian plugins.

Thus far, we’ve identified a total of 53 vulnerable plugins and are working on responsibly disclosing them. The disclosure process, to our disappointment, is rather convoluted and takes more time than expected, so we are juggling with a growing list of vulnerabilities that will eventually be handled by Atlassian’s security team.

## Conclusions #

Based on the definition of Atlassian’s processes pertaining to marketplace plugin security controls and the results of our research thus far, we can reasonably conclude, that plugins should be used as sparingly as possible.

Don’t exclusively rely on the assuring words of a vendor telling you that plugins are checked for security holes, nor developers participating in bug bounty programs or flashing fancy badges.

Keep in mind that you are introducing additional attack surface to your infrastructure by installing plugins. Audit your plugins for security holes and stay up to date.

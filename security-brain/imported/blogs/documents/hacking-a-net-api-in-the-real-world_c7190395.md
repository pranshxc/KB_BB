---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-27_hacking-a-net-api-in-the-real-world.md
original_filename: 2022-12-27_hacking-a-net-api-in-the-real-world.md
title: Hacking a .NET API in the real world
category: documents
detected_topics:
- path-traversal
- sqli
- command-injection
- automation-abuse
- sso
- access-control
tags:
- imported
- documents
- path-traversal
- sqli
- command-injection
- automation-abuse
- sso
- access-control
language: en
raw_sha256: c719039591fac0a9ea1fdb00629c74638f3bf4fc96c8183f3ba2e7db7a1a5bd7
text_sha256: 4944602544b67892b864d9841ab9e5b3b88987d0073676446d78425c821b77ec
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a .NET API in the real world

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-27_hacking-a-net-api-in-the-real-world.md
- Source Type: markdown
- Detected Topics: path-traversal, sqli, command-injection, automation-abuse, sso, access-control
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `c719039591fac0a9ea1fdb00629c74638f3bf4fc96c8183f3ba2e7db7a1a5bd7`
- Text SHA256: `4944602544b67892b864d9841ab9e5b3b88987d0073676446d78425c821b77ec`


## Content

---
title: "Hacking a .NET API in the real world"
page_title: "Hacking a .NET API in the real world - Dana Epp's Blog"
url: "https://danaepp.com/hacking-a-net-api-in-the-real-world"
final_url: "https://danaepp.com/hacking-a-net-api-in-the-real-world"
authors: ["Dana Epp (@DanaEpp)"]
bugs: ["LFI"]
publication_date: "2022-12-27"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1727
---

December 27, 2022

[API Hacking Techniques](https://danaepp.com/category/api-hacking-techniques)

# Hacking a .NET API in the real world

![Hacking a .NET API in the real world](https://danaepp.com/wp-content/uploads/2022/12/hacking-dotnet-api.png)

I have an interesting story I want to share with you about the fragility of modern web applications. I’ve been struggling with how to share this in a way to protect the innocent while still telling the tale that can educate and enlighten you about red teaming in the real world.

So I’m going to be generalizing a bit. Please bear with me, but stick with it. By the end of this article, you will learn the value of understanding how .NET applications and APIs are built and how the basics in reverse engineering can open you to a world of exploitable vulnerabilities you may never have thought about before.

## The backstory

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-1.png?resize=976%2C734&ssl=1)

One of the more interesting engagements I worked on this year included infiltrating a complex SaaS application written in .NET that ultimately got pwned due to a non-linear kill chain that jumped across a whole bunch of different microservices.

There is no way that traditional vulnerability scanning tools would have been able to find this. In fact, it was a combination of pure damn luck and ingenious reverse engineering that gave me the foothold I needed to exploit the target.

So let’s go back to the beginning of how I found the initial foothold that led me to a cornucopia of interesting code to exploit.

## The foothold

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-2.png?resize=978%2C628&ssl=1)

It all seemed innocuous at first. A report generation endpoint in an API allowed the user to request a report based on a date range. Its response was a unique GUID that could be passed to another endpoint to later fetch and download the report in a PDF format when it was ready.

Whenever I see an endpoint that accepts user input, I try to taint the data by injecting malicious payloads that could trip up the API. Usually, when I see a GUID, I check to see if it may be predictable and something I could ultimately guess. [I’ve talked about attacking predictable GUIDs before](https://danaepp.com/attacking-predictable-guids-when-hacking-apis). However, in this case, I could immediately see this was a v4 UUID, which meant I couldn’t exploit that weakness.

So I turned to a custom polyglot wordlist of “interesting” inputs I typically use on .NET applications to see if I could fuzz the endpoint to see how it would react to weird inputs.

**Side note:** If you are wondering how I knew it was a .NET endpoint, you should check out my article on [detecting an API’s programming language](https://danaepp.com/how-to-detect-the-programming-language-of-an-api). During initial recon, I determined the target was running a modern .NET stack.

So with my polyglot wordlist in hand, I loaded up Burp Repeater with a successful request for the report and fired it off. Sure enough, I could see the endpoint return a 200 HTTP status code along with a PDF file stream body. I replaced the valid GUID input in the URL path with an invalid one and fired it off again. It returned a 404 HTTP response code. Makes sense. Seems like normal behavior.

So I sent the request over to Burp Intruder. I loaded up my wordlist and set an injection point to replace the GUID with the potentially malicious payloads and let Intruder do its thing.

And wow… did it do its thing.

Within minutes I was downloading PDFs left and right.

WTF was going on? Where were all these PDFs coming from?

I looked closer at the successful responses. These weren’t valid PDFs at all. In actuality, they were just file streams. And one of these files was the contents of **/etc/passwd**.

I had tripped over a local file inclusion (LFI) vulnerability in the reports endpoint. As I investigated closer, I realized that the developers had written basic code to prevent directory traversal for normal paths but didn’t account for encoded/escaped UNIX pathing.

So I had a couple of new findings I didn’t have from the initial recon. The first was the LFI vulnerability, and the second was that the target was not running .NET on Windows as I had initially assumed.

Together, these findings gave me the critical links in my kill chain to hack into this .NET web application.

## Exploiting LFI to get API artifacts

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-3.png?resize=972%2C726&ssl=1)

Having the ability to download files directly from the target API is extremely useful. While typical network pentesters love to leverage LFI to find privilege escalation points at this stage, as an appsec pentester, my goal is to gain access to the API artifacts.

And that’s precisely what I did.

At this point, I already knew that we had some sort of Unix environment. Being that the tech stack is .NET based, I pretty much could count on the target running some form of Linux. And there is a good chance this is running in some sort of constrained container since most .NET apps that run on Unix are running dotnet core within a containerized environment.

To confirm the operating system, I grabbed the **/etc/os-release** file. Sure enough. It was a Debian-based operating system.

I then tried to get the **.dockerenv** file at the root of the system. It returned an empty file. But not a 404 status code. That was useful. Just the existence of the file is a leading indicator that we are in a docker container.

Knowing it’s a .NET app running in docker, I wanted to start probing the file system for the .NET assemblies of the API. But how could I find them when I don’t know their name?

### Finding an API’s .NET assembly name

It ends up .NET developers are an interesting clan. They follow a lot of samples directly online without understanding the impact on their applications. There are far too many “experts” who share how to containerize dotnet apps in a way that makes them predictable and in no way hardened for the real world.

Don’t believe me? Start by [reading the guidance directly from Microsoft](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/docker/building-net-docker-images?view=aspnetcore-7.0) to get an idea.

Following the Microsoft Learn guidance, you can learn a lot about how .NET apps usually get containerized. You really should give it a try and see for yourself.

Anyways, in my case, I knew that you could typically find artifacts like `/app/appsettings.json`**** and `/app/appsettings.Development.json`. Sure enough. Both were there.

This already gave me a positive signal that this API wasn’t appropriately hardened. Developers should NEVER leave development artifacts in a production release build.

The files had some interesting findings too, like a connection string to a backend messaging bus that would come into play later in the engagement when I wanted to pivot deeper into the infrastructure. But that’s a story for another day.

Anyways, I wasn’t lucky enough to get any information that would lead to the assembly name of the API. But I did have an idea of where the assemblies were stored within the containerized microservice.

So I had to get a bit creative.

This is where a bit of luck came in. Sometimes, finding failure code paths can lead to more intel on an API. In my case, while interrogating the API, I was able to break it in a way that caused an exception that led to a rare edge case that leaked the assembly name in a stack trace.

You’ve probably seen this before. The developer catches an exception and dumps too much information in the output. In this case, I got the name of the failing function, the class it was in, and the company name. And that aligns with [Microsoft’s guidance](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-assemblies-and-dlls) for how to name managed code DLLs.

It’s usually in the format of `<Company>.<Component>.dll`

And sure enough, as luck would have it, that naming convention ended up matching on the target, and I was able to use the LFI vulnerability to download the main API assembly artifact from inside the `/app` folder.

## Reverse engineering the .NET API assembly

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-5.png?resize=976%2C732&ssl=1)

Once I had the DLL locally, I was well-positioned to decompile the assembly back to human-readable source code. There are lots of ways this can be accomplished. GUI tools like RedGate’s [Reflector](https://www.red-gate.com/products/dotnet-development/reflector/) or JetBrains [dotPeek](https://www.jetbrains.com/decompiler/) can do this quite well.

I prefer to use tools I can leverage at the command line and script as part of automation. I also like to use tools that work across platforms since I hack from systems running Windows, Linux, and even macOS.

My decompiler of choice is [ILSpyCmd](https://github.com/icsharpcode/ILSpy/tree/master/ICSharpCode.ILSpyCmd).

### Decompiling the target API

For obvious reasons, I can’t show you the actual commands and output from my appsec pentest engagement. So instead, for the rest of this article as I explain what I did, I will demonstrate the methodology against the [Damn Vulnerable C# Application (API Only)](https://github.com/appsecco/dvcsharp-api). This vulnerable .NET API written in C# mimics some of the same behaviors I found in this real-world engagement.

The DVCSA assembly is named **dvcsharp-core-api.dll**. To decompile it similarly to the way I did in the actual engagement, I used the following command:
  
  
  
  
  ilspycmd --nested-directories -p -o src dvcsharp-core-api.dll

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/ilspycmd.png?resize=1024%2C638&ssl=1)

Here is a bit of an explanation of the parameters used:

  * **–nested-directory** : Use nested directories for the namespace
  * **-p** : Decompiles the assembly into a compilable project and generates an appropriate .csproj file.
  * **-o src** : Sets the output directory to src

This basically decompiles the target assembly to the destination directory called src, creates a project file, and creates one source file (.cs) per type found, all into nicely nested directories based on the namespace detected.

And with that… we now have the source code for the .NET API.

### Audit the .NET code for vulnerabilities

Now that we have the API in a source code format, we can do a quick rough audit for any suspicious and/or dangerous functions that could be exploited that might exist in the codebase. I use [graudit](https://github.com/wireghoul/graudit) for this purpose and cover it in far more detail in my article on [tracing API exploitability using code review and taint analysis](https://danaepp.com/tracing-api-exploitability-through-code-review-and-taint-analysis).

To use graudit with .NET code, this command worked well:
  
  
  
  
  graudit -d dotnet -L .

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/graudit.png?resize=1024%2C638&ssl=1)

During my engagement, I found a vulnerability that led to a command injection vulnerability on the API microservice that allowed me to manipulate the communications between the API microservice and the backend event processor. In the case of DVCSA here, we can quickly see a potential SQL injection (SQLi) vulnerability.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/graudit-output.png?resize=1024%2C638&ssl=1)

If we open up the offending line in a text editor like vi (thanks to graudit’s `-L` param) we can quickly see that the API route **`/search`** is vulnerable to SQLi in the **keyword** parameter.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/taint-analysis.png?resize=1024%2C638&ssl=1)

## Conclusion

Whew. What a whirlwind tour of hacking a vulnerable .NET API!

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-6.png?resize=978%2C650&ssl=1)

In this article, we walked through how I was able to use a local file inclusion vulnerability in a target .NET API to download the main API assembly artifacts. We then decompiled the assembly back to human-readable source code and did a quick audit for suspicious and dangerous functions that could be exploited. Finally, we found and demonstrated an example of a vulnerable function in the codebase that led to an injection vulnerability on the API microservice that could easily be exploited.

Knowing how .NET works was a big help. Understanding how to reverse engineer the API assembly allows us to weaponize the artifacts to go deeper and find more interesting vulnerabilities. **It’s these skills that continue to prove to me that people-powered pentesting will almost always trump any vulnerability scanner that is being sold on the market.**

What do you think? Does this story resonate with what you are currently seeing in the field? Let me know.

### Share this:

  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://danaepp.com/hacking-a-net-api-in-the-real-world?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://danaepp.com/hacking-a-net-api-in-the-real-world?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://danaepp.com/hacking-a-net-api-in-the-real-world?share=facebook)
  * [ Print (Opens in new window) Print ](https://danaepp.com/hacking-a-net-api-in-the-real-world#print?share=print)
  * 

![Dana Epp](https://danaepp.com/wp-content/uploads/2022/08/danaepp-headshot-1-300x300.jpg)

Dana Epp

Hey, I’m Dana, aka SilverStr. I build and break software for a living, and am a Microsoft Regional Director and Developer Security MVP. I’ve spent decades as a security architect that focuses on helping secure software, data, and infrastructure on both blue and red teams. As of late, I have been focusing more on my offensive tradecraft to help developers and IT administrators see the impact of exploitation on vulnerabilities in their work. This blog is my chance to give back to the community by sharing my experiences and war wounds from the trenches.

← [How to use OAST to detect vulnerabilities in an API](https://danaepp.com/how-to-use-oast-to-detect-vulnerabilities-in-an-api)

→ [3 training resources to improve your API hacking tradecraft](https://danaepp.com/3-training-resources-to-improve-your-api-hacking-tradecraft)

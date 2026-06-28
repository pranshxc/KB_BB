---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_attacking-net-web-services.md
original_filename: 2023-03-06_attacking-net-web-services.md
title: Attacking .NET Web Services
category: documents
detected_topics:
- ssrf
- command-injection
- mfa
- otp
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- mfa
- otp
- api-security
language: en
raw_sha256: 78fb295f3db7be9b89c52862266937b316d23462a8172d1a6526dc102804721f
text_sha256: 70ddbd7a01c2ef90861938ceb0462ba3d5d94fca8b73da25c68aebcd22b053d8
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking .NET Web Services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_attacking-net-web-services.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, mfa, otp, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `78fb295f3db7be9b89c52862266937b316d23462a8172d1a6526dc102804721f`
- Text SHA256: `70ddbd7a01c2ef90861938ceb0462ba3d5d94fca8b73da25c68aebcd22b053d8`


## Content

---
title: "Attacking .NET Web Services"
page_title: "Attacking .NET Web Services – Securifera"
url: "https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/"
final_url: "https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/"
authors: ["b0yd (@rwincey)"]
programs: ["Siemens"]
bugs: ["Security code review", "Arbitrary file read", "Arbitrary file write", "SSRF"]
publication_date: "2023-03-06"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1415
---

Attacking .NET Web Services

![](https://www.securifera.com/wp-content/uploads/2023/02/title.jpg)

### **This article is in no way affiliated, sponsored, or endorsed with/by Siemens Healthineers or Microsoft Corporation. All graphics are being displayed under fair use for the purposes of this article.**

### Last year I spent some time looking for vulnerabilities in a commercial cardiovascular imaging web application called Syngo Dynamics. This product is developed by [Siemens Healthineers](https://www.siemens-healthineers.com/). Syngo Dynamics is a rather complex application that consists of a web application, .NET web services, native binaries, and a database.

![](https://www.securifera.com/wp-content/uploads/2023/02/syngo.jpg)

### For the purposes of this blog post, I’m going to focus on the web services portion of the application. I gave a [BSIDES talk](https://www.youtube.com/watch?v=RNFLk56M4r4) on this topic for those that may prefer that format. The remainder of this post will detail my approach when performing white-box vulnerability research on a .NET web application. The first thing I like to do is open up the IIS config and any “web.config” files for the application. The IIS config can be found at “** _C:\Windows\System32\inetsrv\config_** ” and the “web.config” files are typically in the app pool directories with a format similar to “ _**< Drive Letter>\inetpub\temp\appPools\<App Name>\web.config**_“.

![](https://www.securifera.com/wp-content/uploads/2023/02/inetsrv_config3.jpg)

![](https://www.securifera.com/wp-content/uploads/2023/02/web_config2.jpg)

### When performing white-box vulnerability research, my primary goal is to locate the code so I can look for bugs. There’s two important things we can take away from these config files to further this effort. The “application” node defines the mapping of the application endpoint to the physical path on disk where code exists. The “endpoint” node inside the “service” node specifies the class contract that defines the endpoint behavior. If we navigate to the “physicalPath” for the “DataTransferServices” we find “svc” files that describe each service.

![](https://www.securifera.com/wp-content/uploads/2023/02/svc_file.jpg)

### If we look at the contents of the “CommonService.svc” file, we can see that the assembly that implements this service is called _**DataTransferServices** _and the service name is _**DataTransferServices.CommonService**_. At this point we need to locate the assembly to begin the reverse engineering process. But what is an assembly?

![](https://www.securifera.com/wp-content/uploads/2023/02/assembly.jpg)

### So we’re looking for an assembly named “ _**DataTransferServices.exe.” or “**_ _**DataTransferServices.dll”**_ likely in the same directory tree. If we do a quick search in explorer we find what we are looking for.

![](https://www.securifera.com/wp-content/uploads/2023/02/search.jpg)

### Now that the assembly has been located, it’s time to open up the binary in a decompiler. Since the binary is a managed C# assembly, we can decompile it back into readable C# code. There are two tools I like to use for this, [dotPeek](https://www.jetbrains.com/decompiler) & [dnSpy](https://github.com/dnSpyEx/dnSpy). They are mostly feature equivalent with the exception of dotPeek also providing debugging capabilities.

![](https://www.securifera.com/wp-content/uploads/2023/02/dotpeek.jpg)

### Opening up the “DataTransferServices.dll” binary we find the contract interface that defines the functions that are exposed through the service. From dnSpy we select “Go to Implementation” to view the code for one of the functions.

![](https://www.securifera.com/wp-content/uploads/2023/02/path_combine.jpg)

### One of the first things that jumped out to me is the concatenation of user controlled parameters for the file path that is then read and returned in the response. [Praetorian wrote up an interesting article about abusing the Path.Combine function in C#](https://www.praetorian.com/blog/pathcombine-security-issues-in-aspnet-applications/) . Basically, if an absolute path is given as one of the parameters to concatenate, the others are ignored. To confirm this suspicion, I needed to craft a web request to hit this code. The first thing I did was navigate to the service endpoint in a browser to see what it displayed.

![](https://www.securifera.com/wp-content/uploads/2023/02/svc_disabled.jpg)

### It looks like the metadata output is disabled. Unfortunately without metadata output enabled we won’t be able to easily generate sample web requests for the web service endpoints. Luckily the webpage tells us how to enable it inside the “web.config” file for the web service. After making the modification we are greeted with a slightly different landing page.

![](https://www.securifera.com/wp-content/uploads/2023/02/svc_enabled.jpg)

### The service endpoint shows a link to a new “wsdl” endpoint that describes the functions published by the service. Unfortunately without something to ingest, the “wsdl” XML file it isn’t very useful. Fortunately, Burp has an extension called [Wsdler](https://portswigger.net/bappstore/594a49bb233748f2bc80a9eb18a2e08f) that was made for this very purpose. If we navigate to the “wsdl” endpoint we can then right click on the request in the Burp Proxy -> HTTP history tab and send it to the _**Wsdler** _extension.

![](https://www.securifera.com/wp-content/uploads/2023/02/wsdler.jpg)

### Using Wsdler you can select the operation in the list and it will generate a sample HTTP SOAP request. The request can then be sent to the Repeater tab to test out. I enter the full path in the “ _**fileName**_ ” field to confirm the ability to read arbitrary files using the _**Path.Combine**_ function.

![](https://www.securifera.com/wp-content/uploads/2023/03/dl_req.jpg)

### Our suspicious was correct. We successfully read an arbitrary file rather than files in the intended directory. Often times it isn’t this simple and having the ability to debug the code is pivotal. In the next section, I’ll walk through how to do that using dnSpy.

## **Debugging .NET web services using dnSpy and dotPeek**

### To begin debugging a .NET web service, we need to locate the IIS w3wp.exe process. Click the _**Debug- > Attach to Process**_ menu in dnSpy to bring up the process selection dialog. If no w3wp.exe process exists, send a web request to the web service to ensure a work process is created.

![](https://www.securifera.com/wp-content/uploads/2023/03/debug.jpg)

### If the w3wp.exe process still isn’t listed, there could be an architecture mismatch either between the dnSpy application or the IIS server process. It is important to ensure the architecture of dnSpy, the .NET assembly, and the IIS server process are all the same. The architecture of the IIS process can be modified in the _**Advanced Settings**_ of the IIS Application Pool.

![](https://www.securifera.com/wp-content/uploads/2023/03/iis_settings.jpg)

### Once you attach to the w3wp.exe process you should be able to drop breakpoints in the decompiled source that will get hit when the code executes. If you drop a breakpoint and the circle is an outline rather than filled-in, you have one more step to complete. This means that the debugger could not find symbols for the application you are debugging.

![](https://www.securifera.com/wp-content/uploads/2023/03/no_symbols.jpg)

### In this case we can use dotPeek to generate the symbols for the assembly. Simply open the assembly in dotPeek, right click on the assembly in the “Assembly Explorer” and click _**Generate Pdb.**_

![](https://www.securifera.com/wp-content/uploads/2023/03/generate_pdb.jpg)

### After the PDB has been generated, copy the file into the same directory as the assembly that is being debugged and it should be automatically loaded. Restart the debugger and begin stepping through the code.

![](https://www.securifera.com/wp-content/uploads/2023/03/debugging.jpg)

### As shown in the screenshot above, I can confirm at the code level using the debugger that _**Path.Combine**_ does indeed allow for the opening of arbitrary file paths if one of the arguments is absolute.

## **Finding Variants**

### With the discovery of one misuse of the _**Path.Combine**_ function resulting in an arbitrary file read, it makes sense to search the rest of the code base for additional instances that may have more impact. Since this vulnerability isn’t particularly complex, I chose to use grepWin to search for other uses of _**Path.Combine**_ who’s arguments may be controllable.

![](https://www.securifera.com/wp-content/uploads/2023/03/grepwin.jpg)

### Reviewing the results led to the discovery of a similar usage of  _**Path.Combine**_ but this time as a file write. The impact of an arbitrary file write is often more critical as it typically allows for code execution.

![](https://www.securifera.com/wp-content/uploads/2023/03/file_write.jpg)

### Ultimately an additional 7 instances of exploitable insecure _**Path.Combine**_ usage were identified. These findings fell into three vulnerability categories, arbitrary file read, arbitrary file write, & server side request forgery (SSRF). I will leave exploitation of these vulnerability types as an exercise for the reader as this is a pretty well documented topic. For some examples feel free to watch my [BSIDES Charleston 2022 talk](https://www.youtube.com/watch?v=RNFLk56M4r4).

## **Vendor Disclosure & Patch**

### I reported these issues through the [Siemens Healthineers vulnerability disclosure process](https://www.siemens-healthineers.com/en-us/support-documentation/cybersecurity) and can say everything went smoothly and they worked with me to get the issues fixed and patched in a reasonable time frame. Given the severity of these findings, we strongly encourage anyone that has Syngo Dynamics deployed to update to the latest version immediately. More details about the vulnerabilities can be found on the Siemens Healthineers [security advisory page](https://www.siemens-healthineers.com/en-us/support-documentation/cybersecurity/shsa-741697).

By [b0yd](https://www.securifera.com/blog/author/b0yd/)|2024-04-15T14:25:45+00:00March 6th, 2023|[BUG BOUNTY](https://www.securifera.com/blog/category/bug-bounty/), [EXPLOITS](https://www.securifera.com/blog/category/exploits/), [PENTESTING](https://www.securifera.com/blog/category/pentesting/)|[0 Comments](https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/#respond)

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&t=Attacking%20.NET%20Web%20Services "Facebook")[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&text=Attacking%20.NET%20Web%20Services "X")[Reddit](https://reddit.com/submit?url=https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/&title=Attacking%20.NET%20Web%20Services "Reddit")[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&title=Attacking%20.NET%20Web%20Services&summary=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Siemens%20Healthineers%20or%20Microsoft%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0ALast%20year%20I%20spent%20some%20time%20looking%20for%20vulnerabilities "LinkedIn")[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&name=Attacking%20.NET%20Web%20Services&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Siemens%20Healthineers%20or%20Microsoft%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0ALast%20year%20I%20spent%20some%20time%20looking%20for%20vulnerabilities%20in%20a%20commercial%20cardiovascular%20imaging%20web%20application%20called%C2%A0%20Syngo "Tumblr")[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Siemens%20Healthineers%20or%20Microsoft%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0ALast%20year%20I%20spent%20some%20time%20looking%20for%20vulnerabilities%20in%20a%20commercial%20cardiovascular%20imaging%20web%20application%20called%C2%A0%20Syngo&media=https%3A%2F%2Fwww.securifera.com%2Fwp-content%2Fuploads%2F2023%2F03%2Ftitle.jpg "Pinterest")[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F03%2F06%2Fattacking-net-web-services%2F&title=Attacking%20.NET%20Web%20Services&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Siemens%20Healthineers%20or%20Microsoft%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0ALast%20year%20I%20spent%20some%20time%20looking%20for%20vulnerabilities%20in%20a%20commercial%20cardiovascular%20imaging%20web%20application%20called%C2%A0%20Syngo "Vk")[Email](mailto:?body=https://www.securifera.com/blog/2023/03/06/attacking-net-web-services/&subject=Attacking%20.NET%20Web%20Services "Email")

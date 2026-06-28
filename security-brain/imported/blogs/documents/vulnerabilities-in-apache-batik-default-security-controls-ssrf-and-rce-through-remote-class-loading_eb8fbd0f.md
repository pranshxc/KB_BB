---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-31_vulnerabilities-in-apache-batik-default-security-controls-ssrf-and-rce-through-r.md
original_filename: 2022-10-31_vulnerabilities-in-apache-batik-default-security-controls-ssrf-and-rce-through-r.md
title: Vulnerabilities In Apache Batik Default Security Controls – SSRF And RCE Through
  Remote Class Loading
category: documents
detected_topics:
- ssrf
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: eb8fbd0f062396df590451fce80a054fa02e6d691829145e2b9b6b28bbed28c6
text_sha256: 1c0964528504928f4749422e61d51b0bd13af9e2c6a2f5b3130e3b8303a7c729
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities In Apache Batik Default Security Controls – SSRF And RCE Through Remote Class Loading

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-31_vulnerabilities-in-apache-batik-default-security-controls-ssrf-and-rce-through-r.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `eb8fbd0f062396df590451fce80a054fa02e6d691829145e2b9b6b28bbed28c6`
- Text SHA256: `1c0964528504928f4749422e61d51b0bd13af9e2c6a2f5b3130e3b8303a7c729`


## Content

---
title: "Vulnerabilities In Apache Batik Default Security Controls – SSRF And RCE Through Remote Class Loading"
page_title: "Zero Day Initiative — Vulnerabilities in Apache Batik Default Security Controls – SSRF and RCE Through Remote Class Loading"
url: "https://www.zerodayinitiative.com/blog/2022/10/28/vulnerabilities-in-apache-batik-default-security-controls-ssrf-and-rce-through-remote-class-loading"
final_url: "https://www.zerodayinitiative.com/blog/2022/10/28/vulnerabilities-in-apache-batik-default-security-controls-ssrf-and-rce-through-remote-class-loading"
authors: ["Piotr Bazydło (@chudypb)"]
programs: ["Apache Batik"]
bugs: ["SSRF", "RCE"]
publication_date: "2022-10-31"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 1968
---

# Blog

#  Vulnerabilities in Apache Batik Default Security Controls – SSRF and RCE Through Remote Class Loading 

__ October 31, 2022

__ Piotr Bazydło

**Introduction**

I stumbled upon the Apache Batik library while researching other Java-based products. It immediately caught my attention, as this library parses Scalable Vector Graphics (SVG) files and transforms them into different raster graphics formats (i.e., PNG, PDF, or JPEG). I was even more encouraged when I looked at the [Batik documentation](https://xmlgraphics.apache.org/batik/using/). It was obvious that such a library could be prone to Server-Side Request Forgery (SSRF) issues (e.g., loading of images from remote resources). However, the documentation shows that Batik can also:

· Execute JavaScript through the Rhino interpreter.  
· Load and execute remote Java classes.

Those are some neat features! On the other hand, Apache Batik protects its users from both SSRF and remote code execution (RCE) vulnerabilities through the various security modes it offers. In this blog post, I am going to show you:

· How I bypassed the default security modes: _DefaultScriptSecurity_ ([CVE-2022-40146](https://www.zerodayinitiative.com/advisories/ZDI-22-1327/)) and _DefaultExternalResourceSecurity_([CVE-2022-38398](https://www.zerodayinitiative.com/advisories/ZDI-22-1328/)).  
· How to abuse the SSRF in the default Batik Transcoder to make arbitrary HTTP GET requests or to trigger an NTLM challenge.  
· What configurations are vulnerable to the RCE through remote class loading.  
· What configurations are vulnerable to the RCE through the Rhino interpreter and JavaScript execution.

Before we get into the details, here’s a quick video demonstrating a remote code execution vulnerability exploited through remote JAR loading.

**Sample Web Application Endpoint**

Apache Batik can be used in different ways. There is a pretty good chance that you have already seen it in web applications during the conversion of SVG to PDF/PNG/JPEG. Let’s define a sample endpoint that performs such a conversion:

''' 

This endpoint performs the following actions:

· Retrieves and decodes the base64-encoded SVG file.  
· Creates the Apache Batik JPEG Transcoder.  
· Converts the SVG to JPEG.

This is a common usage of Apache Batik. Note that there is a risk of an easy SSRF if the SVG loads an image from an external resource. Batik tries to protect against such a scenario with its external resource controls, although some of these have existing bypasses with their own CVEs assigned. Let’s quickly review those resource controls. 

**Apache Batik External Resource Controls**

Apache Batik resource controls can be divided into two main categories:

· Script execution  
· External resources controls (like images). 

Let’s take a brief look at the scripting controls. They control whether script provided within an SVG will be executed. The external resource controls are similar to the scripting controls but apply to the fetching of resources such as images. For a full description of security controls, you can access the documentation [here](https://xmlgraphics.apache.org/batik/using/scripting/security.html). Here’s a quick overview of the available _ScriptSecurity_ implementations:

· _NoLoadScriptSecurity_ – scripts are completely blocked.  
· _EmbededScriptSecurity_[sic] **_–_** scripts embedded in the document can be executed when properly referenced.  
· _DefaultScriptSecurity_**–** Embedded external scripts (as above) plus scripts coming from the same origin as the document referencing them are allowed.  
· _RelaxedScriptSecurity_**–** scripts from any location can be loaded.

In my research so far, I have focused only on the default security controls.

Note that the default security control has a concept of “origin”, but what exactly does this mean? It means that the resource or script will be loaded only if it originates from the same “host” as the SVG file. For example:

· If we load a local SVG file, we can also load local scripts or resources.  
· If we load a local SVG file, we cannot load scripts or resources from remote origins (e.g., through HTTP or SMB).  
· If we load an SVG file through the HTTP protocol, we can load remote scripts from the same host through either HTTP or any other supported protocol, such as SMB.

In order to avoid any confusion, let’s quickly describe what “loading an SVG through the HTTP protocol” means in Batik. It specifically means that the HTTP URL is directly provided to the Batik `TranscoderInput`.

This does not look like a particularly common scenario, because the attacker would need to control the URL from which the SVG file is (directly) loaded into Batik.

Accordingly, the default security controls seem to be appropriate. When a local SVG file is loaded, or an SVG is provided as an InputStream, the default controls should block the loading of any remote resources. 

Now let’s see how we can bypass those security checks.

**DefaultScriptSecurity and DefaultExternalResourceSecurity vs URL.getHost**

To start, let’s dig into the _DefaultScriptSecurity_ constructor, which is responsible for our security check. Please note that the code of _DefaultExternalResourceSecurity_ is almost identical, thus it will not be presented.

At [1], the _scriptURL_ and _docURL_ of _ParsedURL_ type are provided. For the sake of simplicity, let’s say that _ParsedURL_ wraps the Java _URL_ class.

At [2] and [3], the respective host strings are retrieved with the _getHost_ method. Under the hood, it retrieves the output of the Java _URL.getHost_.

At [4], hosts obtained in points [2] and [3] are compared. If they are the same, the code flow continues, and the exception will not be thrown.

At [5], a _SecurityException_ is thrown if the security check is not successful. 

If the document host and the script host are the same, the exception will not be thrown, and the script or resource will be loaded. Next, let’s look at how the Java _URL.getHost_ behaves for different protocols:

It’s pretty simple. The host for a local file will be equal to _null_ , whereas for the remote files shown here (referenced by either UNC path or HTTP) it will be equal to _evil.com_. If the Apache Batik _TranscoderInput_ is created with the _InputStream_ , the _getHost_ method will also return _null_.

It seems that the default security routines work properly, and we will not be able to load remote resources during processing of SVGs coming from local files or input streams.

Unfortunately, a trivial bypass exists, and honestly, Java itself is the likely culprit. Let’s see the output of the _getHost_ getter for the JAR protocol:

What? It seems that the host for the JAR protocol is also _null_. In order to properly retrieve the host from the JAR URL, the following cumbersome code can be used. We retrieve the _file_ member from the _URL_ and then use it to create a new _URL_ , from which we can get the host.

In this way, the security check can be easily bypassed with the JAR protocol. Let’s have a look at a sample SVG that leads to SSRF through the _image_ tag.

This SVG will bypass the _DefaultExternalResourceSecurity_ control and will make an HTTP GET request to the attacker’s server. Please note that we can also use the syntax _“jar:file://…”_ , in order to get an NTLMv2 challenge-response in a Windows environment and potentially perform an NTLM relaying attack.

Now that we have shown how to bypass the default external resources controls to get an easy SSRF through the _image_ tag, let’s see how to get remote code execution. This has been fixed in Batik 1.15.

**Apache Batik Remote Class Loading Feature**

While digging through the Apache Batik documentation, I found an [intriguing feature](https://xmlgraphics.apache.org/batik/using/scripting/java.html): “Referencing Java Code From a Document”. 

_Batik implements the Java bindings for SVG, and thus allows Java code to be referenced from script elements…  
In order to use this extension, the type attribute of a script element must be set to application/java-archive. In addition, the xlink:href attribute must be the URI of a jar file that contains the code to run._

It seems that we can provide a script of type _application/java-archive_ referencing a properly structured JAR file. We already know that we can bypass the _DefaultScriptSecurity_ check and load files from remote locations, thus it looks like a win!

Luckily, the script execution is not enabled by default in the Apache Batik transcoder and some configuration modifications must be applied:

1) Enable script execution 

Script execution can be enabled in the transcoder with the following line of code:

Please note that the Apache Batik is a “do it yourself” library and often requires a lot of customization. There is a chance that you will see such a configuration in the wild. Also, Batik defines some methods that allow dynamic verification of whether the SVG file contains scripts or not. This method can be used to automatically enable script execution if needed. 

2) Fix the logical flaw to allow execution of scripts of type “application/java-archive”.

It seems that Apache Batik’s definition of default-allowed script types contains an unintended error. Let’s have a quick look:

You can clearly see that the script types are separated with a comma followed by a space. Now, let’s look at the method that retrieves the list of allowed types:

The list is created with _StringTokenizer_ , where the delimiter is set to a comma without a space! According to that, all the allowed types other than the first one (ECMASCRIPT) will contain a leading space. For example, the allowed type will be _“ application/java-archive”_ instead of _“application/java-archive”_. 

The code will compare the script type declared in the SVG against the type specified in the list. You may think that this is not a problem, since we can declare a script type in the SVG that also includes a space:

`<script type=” application/java-archive”>`

This will not work, though. The type check for remote JAR loading is performed twice. The second check verifies if the script type is equal to _“application/java-archive”,_ without a leading space. As a result, we will not be able to pass both checks. To enable remote class loading, we must manually modify the list of allowed script types by making an API call as follows:

Now, let’s look at how to perform remote JAR loading in Batik. To begin, we must create a class that implements the _EventListenerInitializer_ interface. Then, we must define the _initializeEventListeners_ method. This method will be executed after the JAR is loaded. Here’s an example of a malicious class:

The MANIFEST.MF file included in the JAR needs to specify _SVG-Handler-Class_. The following snippet presents an exemplary manifest:

Finally, we specify a malicious SVG that loads such a JAR and bypasses the security policies:

The following screenshot presents a proof of concept where the JAR was loaded through the HTTP protocol and the code was executed, spawning a curl process and making a request to our HTTP server.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/aa62a43a-a03f-461b-8b38-251aa6a3940a/pocJar.png)

_Figure 1 - Code Execution through remote JAR loading_

Success! We were able to bypass the restrictions defined in _DefaultScriptSecurity_ , load the JAR file from the remote location, and achieve remote code execution.

**Scripts Enabled with Remote JAR Loading Disallowed**

Due to the logical flaw described in the previous section, it’s likely that you will encounter the following configuration:

· Scripts enabled.  
· The setting for allowed script types is untouched, so that, in practice, only ECMAScript is enabled.

Luckily, you can still get an easy RCE. ECMAScript is interpreted with [Mozilla Rhino](https://github.com/mozilla/rhino), an open-source implementation of JavaScript written in Java. This code execution vector has been already [presented](https://twitter.com/pyn3rd/status/1579718705763987456?s=20&t=Q5gThl0rHZR4lKjKToQbIg) by the researcher known as pyn3rd.

The following snippet presents an SVG file with an ugly looking script that will execute the attacker’s command.

The following screenshot demonstrates the achieved code execution:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/97e58c9a-fc54-4527-adb2-8b69076df930/pocEcma.png)

_Figure 2 - Code Execution through ECMAScript_

Execution of ECMAScript is a [well-documented feature](https://xmlgraphics.apache.org/batik/using/scripting/ecmascript.html) of Apache Batik and this behavior will not be fixed. [The official security guide](https://xmlgraphics.apache.org/batik/using/scripting/security.html) recommends securing your application with the Java _SecurityManager_ when scripting is enabled. I’m taking a guess, but I think that we will never see a completely secure implementation of _SecurityManager_ within Batik. It would likely break too much functionality and make the application unusable. This is still merely speculation on my part. It should also be noted that running scripts is disabled by  
default and must be explicitly enabled.

UPDATE: Apache Batik 1.16 has been recently released. It introduces a hardening to Rhino script execution mechanisms. However, it’s hard to call this hardening a strong one. You are still able to call almost any class whose full name starts with “org.”. Saying that, you can still easily abuse many methods included in Apache libraries. This security check can be found [here](https://github.com/apache/xmlgraphics-batik/commit/401aa8595f52d085d40ff5b6b4ac0dd372423082).

**Summary**

To wrap things up, the security checks implemented in the default external resource controllers of Apache Batik could be bypassed prior to Batik 1.15, in order to:

· Perform SSRF through the JAR protocol, producing either an HTTP GET request or NTLM relaying via an UNC path.  
· Potentially achieve RCE through remote JAR loading, provided that a non-default configuration was applied.

The bugs discussed here in _DefaultScriptSecurity_ and _DefaultExternalResourceSecurity_ were fixed in version 1.15. Still, Apache Batik may allow the execution of arbitrary Java code when script execution is enabled, even in the latest version 1.16.

If you are using Batik or are interested in finding additional bugs, here are some things to consider:

· Developers – do not allow scripts to execute through Batik. Apply the strictest controls possible.  
· Pentesters/Bug Hunters – when you test functionality that accepts SVG, try to use the SVG files presented in this blog post.  
· Vulnerability researchers – when your target uses Apache Batik for SVG parsing or conversions, analyze its configuration carefully. You might have an easy win over there.

Thanks for reading, and I hope you’ve enjoyed this post. You can follow me [@chudypb](https://www.twitter.com/chudypb) and follow the team on [Twitter](https://www.twitter.com/thezdi) or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Apache](/blog/tag/Apache)
  * [Batik](/blog/tag/Batik)
  * [Research](/blog/tag/Research)

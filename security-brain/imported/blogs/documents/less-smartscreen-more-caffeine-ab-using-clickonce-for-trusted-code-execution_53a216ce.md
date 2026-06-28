---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-08_less-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution.md
original_filename: 2023-06-08_less-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution.md
title: 'Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution'
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- otp
- cloud-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- otp
- cloud-security
- mobile-security
language: en
raw_sha256: 53a216ce2dad982d6e3e3972dfc800872e9a0b267ce8675f1259777b9a037fe3
text_sha256: c581342456883da77250c0c52eedb00704688d8b3ddfcb99f9b520dfdb5dd5cc
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-08_less-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, otp, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `53a216ce2dad982d6e3e3972dfc800872e9a0b267ce8675f1259777b9a037fe3`
- Text SHA256: `c581342456883da77250c0c52eedb00704688d8b3ddfcb99f9b520dfdb5dd5cc`


## Content

---
title: "Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution"
page_title: "Less SmartScreen More Caffeine | SpecterOps Blog"
url: "https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5"
final_url: "https://specterops.io/blog/2023/06/07/less-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution/"
authors: ["Nick Powers (@zyn3rgy)", "Steven Flores (@0xthirteen)"]
bugs: ["Phishing"]
publication_date: "2023-06-08"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1068
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution

Author

[Nick Powers](https://specterops.io/blog/author/nick-powers/)

Read Time

19 mins

Published

Jun 7, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F06%2F07%2Fless-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution%2F&title=Less+SmartScreen+More+Caffeine%3A+%28Ab%29Using+ClickOnce+for+Trusted+Code+Execution&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F06%2F07%2Fless-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution%2F&text=Less+SmartScreen+More+Caffeine%3A+%28Ab%29Using+ClickOnce+for+Trusted+Code+Execution) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Less SmartScreen More Caffeine: \(Ab\)Using ClickOnce for Trusted Code Execution&Body=https://specterops.io/blog/2023/06/07/less-smartscreen-more-caffeine-abusing-clickonce-for-trusted-code-execution/) [ ](https://specterops.io/blog/category/research/feed/)

The contents of this blogpost was written by Nick Powers ([@zyn3rgy](https://twitter.com/zyn3rgy)) and Steven Flores ([@0xthirteen](https://twitter.com/0xthirteen)), and is a written version of the content [presented at Defcon30](https://www.youtube.com/watch?v=cyHxoKvD8Ck).

With the barrier to entry for initial access ever increasing, we spent some time digging into potentially lesser-known weaponization options for ClickOnce deployments. A few of the hurdles we’d like to overcome by implementing these weaponization options include:

  * Install / execute application without administrative privileges
  * Reputable, known-good file(s) used during execution
  * Streamlined, minimal user interaction required
  * Ease of rerolling execution implementations

Ultimately, we want to take a relatively common initial access technique known as ClickOnce and extend its value for the offensive use case by abusing the trust of third-party applications.

### **ClickOnce Overview and Current Weaponizations**

> “ClickOnce is a deployment technology that enables you to create self-updating Windows-based applications that can be installed and run with minimal user interaction” –[MSDN](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-security-and-deployment?view=vs-2022)

ClickOnce is a vehicle for installing and updating .NET applications. Deployments can be published through a variety of options (e.g. network file shares, legacy media [CD-ROM], and web pages). We will be focusing on the web page method of publishing deployments. Legitimate applications exist and make use of ClickOnce deployments for installation or updating software such as Chrome (previously), Fidelity, and others.

ClickOnce deployments rely on manifests which are formatted in a very specific way. Just like .NET applications, there will be different types of manifests that need to be accounted for. There are three types of manifest to become familiar with when discussing ClickOnce deployments:

> ClickOnce deployment manifests

  * *.application is the file extension for these
  * References the ClickOnce application manifest to deploy
  * APPREF-MS file will point to this (if used)

> ClickOnce application manifests

  * *.exe.manifest is the file extension for these
  * Specifies dependencies for the deployment (states version of .NET that will be utilized)
  * Conducts integrity check of deployment manifest
  * References to dependencies and other files for delivery

> Embedded application and assembly manifests

  * Application manifest can also be called unmanaged or fusion manifest
  * Assembly manifest can also be called managed manifest
  * At runtime, ClickOnce makes comparisons against these

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1lm1YgIibJbPnLTiVV8_t9w.png)Embedded Assembly Manifest ![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1i1E1Ch3nS_lrpQ_VtrpMnw.png)Embedded Application Manifest ![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1LUHv7A76XqKkr6iwCGRdPg.png)ClickOnce Deployment Manifest, Executable, and Application Manifest

ClickOnce applications can be deployed to a client by visiting the _*.application_ deployment manifest using a browser. The download and execution process of a standard ClickOnce deployment requires the end user to be using a Microsoft Edge or Internet Explorer browser. An alternative to requiring the target user to access your deployment manifest from either Edge or Internet Explorer would be to [leverage APPREF-MS](https://i.blackhat.com/USA-19/Wednesday/us-19-Burke-ClickOnce-And-Youre-In-When-Appref-Ms-Abuse-Is-Operating-As-Intended.pdf). When creating an _*.appref-ms_ file, UTF-16 LE encoding is required. An _appref-ms_ file would be used if the end user is using something like Chrome or Firefox to access the application.

> **NOTE:** A simple user-agent check can be done prior to reaching the landing page to determine whether the incoming request should be pointed towards the standard deployment manifest or an appref-ms file.

The host assembly, specified in the manifest, will spawn as a child process of ‘ _dfsvc.exe_ ’, which handles the ClickOnce deployment functionality that is imported from ‘ _System.Deployment.dll_ ’. The contents of the ClickOnce application manifest will specify what dependencies and other resources will be delivered during the deployment process. The contents of the deployment will ultimately be saved to:

_C:Users%USERNAME%AppDataLocalApps2.0 <randomstring>_

Once a user has accepted to run the application, the deployment manifest will look to the ClickOnce application manifest for all the files that need to be downloaded.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1Nwk_ecNbRPDZ7ydd_1Bkuw.png)ClickOnce Deployment Manifest Example

There will be different pieces of information located throughout the manifest that look very similar to .NET application manifests. This will contain all of the files and dependencies the deployment will need to execute properly.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1vXum75dbNZoNDrt5pU_s7w.png)ClickOnce Application Manifest Example

The _dfsvc_ process will make a series of HTTP requests for the downloads and save in the _%LocalAppData%_ location mentioned above.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1pfN16WppCXbZzGgd9IKTUQ.png)HTTP Requests While Downloading a ClickOnce Application

In some scenarios users may want to interact with ClickOnce applications but are not using Microsoft Edge or Internet Explorer. An appref-ms file can be created that will act similar to an LNK or shortcut file that will contain the URL of the deployment manifest and some other pieces of information.

![](https://cdn-images-1.medium.com/max/821/1*eFF9v_vDY8txYOMMteqkrA.png)APPREF-MS Example

During the process before all the downloading happens, the System.Deployment DLL will be utilized to run through various checks and ensure the ClickOnce application can properly execute. One important check to note is the .NET application and ClickOnce deployment identities that are configured in the assembly and the deployment manifests.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1g600iwZzDS8kN0eqgKySqQ.png)System.Deployment.dll Logic to Parse Manifests

Commonly, when crafting an initial access payload and using ClickOnce, you’d go through the process of writing it up in an IDE like Visual Studio and building the ClickOnce application. So what does standard ClickOnce deployment execution look like, using a newly created .NET application?

<https://medium.com/media/89e79bb1f51bfbfbf9b2401ae678f980/href>

### **Current ClickOnce Weaponization Pressure Points**

As seen in the first demo, we experience a few issues. For instance, Microsoft SmartScreen was triggered. This is because the assembly that ultimately executed with our arbitrary code was compiled recently and had never been seen by SmartScreen before. The reputation for Microsoft SmartScreen can be based on a number of factors such as the hash of the host assembly or the certificate used to sign the assembly.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/14X8ZbLQf-Yf59nlU6La9CQ.jpeg)BloodHound Slack Discussion on ClickOnce

Achieving arbitrary code execution within the context of an application seen and otherwise trusted by Microsoft SmartScreen or EDR products can decrease likelihood of prevention. Solutions such as application control or whitelisting prevention can be noteworthy when considering how we want to conduct our code execution, especially during initial access attempts. An Extended Validation (EV) code signing certificate can be used to obtain immediate SmartScreen reputation, but the vetting process and price point increase the barrier to entry. When code-signing certificates are used, there are also additional attribution concerns.

Generally, a ClickOnce deployment can be tedious to make sure “all the stars align” for a successful deployment. Oftentimes people view ClickOnce as tedious to deploy successfully and having many configuration requirements. We hope the next couple sections outline the important fields within ClickOnce manifests to focus on, to assist in reproducing these techniques.

### **Alleviation of ClickOnce Weaponization Pressure Points**

If legitimate .NET applications make use of ClickOnce, and we can reliably sideload or hijack those .NET applications, why not just backdoor an existing deployment? An existing deployment that already has, lets say, a valid EV code signature and SmartScreen reputation?

> **NOTE:** We will backdoor a dependency of a ClickOnce deployment, not the host assembly itself. We _maintain the valid signature_ associated with that host assembly.

Identifying existing ClickOnce deployments can be as easy as leveraging a couple search engine dorking techniques (or using the ClickonceHunter tool which will be covered later). Several tools can be used throughout this process (e.g. dnSpy, reshacker, mage, sigcheck, etc).

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1YsMHwBwOEgyRg4QPHsoTww.png)Download of ClickOnce Application Discovered from Google

We will want to identify sideloading opportunities for dependencies of the target .NET assembly that the ClickOnce deployment will execute. Any way for us to hijack the flow of execution shortly after the application entry point is what we are looking for. Oftentimes this process consists of using dnSpy to decompile the target .NET assembly to understand the execution flow enough to identify a sideload opportunity.

Once an ideal DLL to backdoor has been identified, use dnSpy to add your code to the target DLL. At this point, the ClickOnce manifests of the deployment you’ve chosen will need to be tweaked to pass their integrity checks. If you cannot identify an ideal sideload opportunity in the existing codepath(s), techniques such as AppDomainManager injection or .NET deserialization abuse can be helpful here.

The image below is a quick example of what sideloading an existing, signed ClickOnce deployment would look like. First, we find a ClickOnce deployment published online, download it, and verify the assembly that the deployment executes meets our needs (valid code signature, SmartScreen reputation, etc):

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1gh6RhbJlbcJhnBSF47P3CA.png)Example of Signed ClickOnce Application

Next we take a look at the references within the signed .NET assembly we want to sideload. A few of the DLLs the assembly uses are not strongly named, which can be helpful in certain situations:

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1BLfd__iJPtUlIx_rEm1ZSg.png)Dependencies of Target Assembly

Using DnSpy to begin at the target .NET assembly’s entry point, we follow the code to the first method call of “SetDpiAwareness()”. This function exists within on the the Dlls previously identified:

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1WIUlVr_fMHzOxYKPeJDezQ.png)Following the Code Path

We observe the code within this method and verify it exists within a DLL dependency (not the host .NET assembly):

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1AtLh0G3cBjLjZz2nKBO7Nw.png)Identified Location to Place Additional Code

The additional code we’d like to sideload the ClickOnce deployment with can be added here. For proof-of-concept sake, we will just spawn notepad and prompt with a MessageBox:

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1qKmTqsGW7IAl-JknhKqZ_A.png)Adding Code to Target Dependency

At this point, dnSpy can add your changes to intermediary language (IL) and you will have your backdoored dependency of the target ClickOnce application. Now is a good time to test and make sure the additional code you’ve added properly executes when running the host .NET assembly.

> **NOTE:** We previously thought a prerequisite was targeting only non-strongly named DLLs. We discovered this is not a requirement because modifying a DLL does not modify the PublickeyToken value of the DLL. The PublickeyToken value is in reference to the hash of the assembly’s embedded manifest rather than the code itself. If the manifest is not modified, the PublickeyToken value remains the same and will still be loaded successfully.

Now that we have our sideload of a signed .NET application that is part of an existing ClickOnce deployment, our last step to have a functioning deployment is to tweak the two ClickOnce manifests such that the integrity checks that occur during deployment do not fail. Here’s a few tips that will hopefully speed the process up:

  * **publicKeyToken** — this value is required, but can be nulled out by replacing the value with 16 zeros
  * **< hash> — **this block is optional and can be removed or recalculated (EX: _openssl -dgst -binary -sha1 Program.exe.manifest |openssl enc -base64)_
  * **< publisherIdentity> — **included if the manifests have been signed, but is optional and can be removed

A noteworthy mention regarding modification of an existing ClickOnce manifest is that if the manifest was signed with a valid certificate, then making these modifications will break that integrity. The difference to the end user is minimal and many legitimate ClickOnce deployments do not sign their manifests at all. We still have control of the prompt observed by the target user, such as “Name” and “From”. A signed vs unsigned look similar to the image below:

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1FKW3YLIWRUB3veYKZuRQ8g.png)Difference Between Signed and Unsigned Deployment Manifest

So the question posed is this: _Do we really need a code signing certificate to effectively weaponize ClickOnce deployments?_

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1ZWnH2gC3f7R201RGe-wpWg.png)

<https://medium.com/media/26e9d9500edcdde52bfda392ef95832a/href>

### **Extending Past Existing ClickOnce Deployments**

The number of published ClickOnce deployments easily identifiable through dorking is finite. It’s not a new technology, nor is it the most popular to deploy and update .NET applications. We foresaw this as a potential issue and sought to find a way to take _any_ ideal .NET assembly, identify a sideload opportunity, and wrap it up as a new ClickOnce deployment. As it turns out, this was possible, with a few prerequisites.

  1. The <assemblyIdentity> field within the embedded application manifest must _not_ exist, or the entire embedded application manifest must not exist (more on this in a bit)
  2. The UAC settings cannot be set to ‘requireAdministrator’ or ‘highestAvailable’

.NET assemblies that meet these prerequisites can be weaponized as backdoored ClickOnce deployments relatively easily. The _System.Deployment_ DLL has code that checks the assembly identity which is found in the embedded application manifest. This check cross-references the application manifest’s identity to ensure the identity values are the same. The image below shows what the embedded assembly manifest default identity will be if it is present.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1o_TQIKH4WCSQxOZhGNaJxQ.png)Example of Default “assemblyIdentity” Field

As you can see the identity contains two pieces of information, the version and the name. The figure below shows what is in the deployment manifest for the identity value. If you look at the difference there is a value of processorArchitecture.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1wogHpFRRRdTgVUYVik-MHw.png)ClickOnce Deployment “assemblyIdentity”

The ‘ _processorArchitecture’_ value is a required value to be present for the assembly identity in the deployment manifest.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1J8sJrXGwzPG7Xlf7yP6-fw.png)MSDN Documentation Showing Required Values

These two values are checked against each other to validate assembly identities are the same. If the default identity value is present in the assembly’s embedded manifest it will fail because there is no ‘ _processorArchitecture’_ value present. Therefore, this type of assembly is not possible to use as a ClickOnce application for our purposes. Modifying this value would require modifying the host assembly of our code execution, losing any benefit of a valid code-signature or reputations with Microsoft SmartScreen.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/12DVMN62FzGZ41tCPYF-9Ew.png)System.Deployment dll Checking Identities

Fortunately there are a lot of assemblies that exist which do not have an identity in the application’s manifest. In the next section we will show how to identify these assemblies, but in the meantime, the figure below shows what an embedded manifest looks like when the default identity is not set, and a non-default manifest was used during the build process instead.
  
  
  <?xml version="1.0" encoding="utf-8"?>
  <asmv1:assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv1="urn:schemas-microsoft-com:asm.v1" xmlns:asmv2="urn:schemas-microsoft-com:asm.v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
  <security>
  <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
  <!-- UAC Manifest Options
  If you want to change the Windows User Account Control level replace the 
  requestedExecutionLevel node with one of the following.
  
  <requestedExecutionLevel  level="asInvoker" uiAccess="false" />
  <requestedExecutionLevel  level="requireAdministrator" uiAccess="false" />
  <requestedExecutionLevel  level="highestAvailable" uiAccess="false" />
  
  Specifying requestedExecutionLevel node will disable file and registry virtualization.
  If you want to utilize File and Registry Virtualization for backward 
  compatibility then delete the requestedExecutionLevel node.
  -->
  <requestedExecutionLevel level="asInvoker" uiAccess="false" />
  </requestedPrivileges>
  </security>
  </trustInfo>
  
  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
  <application>
  <!-- A list of all Windows versions that this application is designed to work with. 
  Windows will automatically select the most compatible environment.-->
  
  <!-- If your application is designed to work with Windows 7, uncomment the following supportedOS node-->
  <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
  
  <!-- If your application is designed to work with Windows 8, uncomment the following supportedOS node-->
  <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
  
  <!-- If your application is designed to work with Windows 8.1, uncomment the following supportedOS node-->
  <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
  
  <!-- This Id value indicates the application supports Windows Threshold functionality-->
  <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
  </application>
  </compatibility>
  </asmv1:assembly>

The second condition that is required is for the UAC settings to not be requiredAdministrator or highestAvailable. Another check by the System.Deployment DLL is it will look for the UAC settings and return errors if the disallowed values are set.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1cpNnYFL1SPIbK1bUgJqJJg.png)UAC Check in System.Deployment DLL

If UAC information exists, or it is set to ‘asInvoker’ the assembly will work as a ClickOnce deployment.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/14riL-1p_n9FMm0wJap21Yg.png)Assembly with No UAC Information

Since we are creating ClickOnce applications from scratch, we will have to create new manifests as opposed to our previous weaponization of modifying existing ClickOnce manifests. Microsoft has a utility that is used for this specific task which is called the Manifest Generation and Editing Tool (Mage). Microsoft makes two different tools that can be used, MageUI and Mage. Mage is a command line tool that comes part of the Windows SDK and for the purpose of this blog will be the one we cover.

Once you have gone through the process of identifying a .NET assembly that can be wrapped up as a ClickOnce deployment, you will want to create the directory structure of the assembly, dependencies, and extra files. As previously mentioned, there are two manifests that will need to be created with Mage — the deployment manifest and the application manifest. The application manifest can be created with the following command:
  
  
  "C:Program Files (x86)Microsoft SDKsWindowsv10.0AbinNETFX 4.8 Toolsmage.exe" -New Application -Processor amd64 -ToFile AppVStreamingUX.exe.manifest -name "TargetApp" -Version 1.0.0.0 -FromDirectory .

Next you will need to create the deployment manifest. This can be done with the following command:
  
  
  "C:Program Files (x86)Microsoft SDKsWindowsv10.0AbinNETFX 4.8 Toolsmage.exe" -New Deployment -Processor amd64 -Install false -ProviderUrl "http://localhost/dist/TargetApp.application" -AppManifest TargetApp.exe.manifest -ToFile TargetApp.application

The _ProviderUrl_ argument is the location where the deployment manifest will be hosted since the primary method we’re covering is web-based applications. Once the manifests are created, you will see there are some signature values that are created with _Mage_. Just like what was covered when editing existing manifests, these values are not always required and can be removed. If any changes are made to the overall deployment, the signatures will be invalidated and will have to be regenerated which can lead to unnecessary troubleshooting. As mentioned previously, these values are:

  * **< publicKeyToken>**, required but can be nulled with 16 zeros
  * **< hash>** block can be removed altogether and not required
  * **Publisher identity** block can be removed altogether

Now that we have identified an existing signed .NET assembly that can be deployed as a ClickOnce application, we can go through the same backdoor steps as the other technique. We will follow the code paths, identify called DLLs, and place our code inside of those DLLs. Finally, we can create the manifests with Mage and are ready for deployment.

<https://medium.com/media/69c4555ae96ea40ccee7e867e36c16e9/href>

**Identification of .NET Assemblies and ClickOnce Applications**

So far, we’ve covered the types of applications that can be weaponized, and now we want to discover potential targets. We have released two tools that will aid in the discovery of existing ClickOnce applications and .NET assemblies that can be weaponized for ClickOnce.

> [ClickonceHunter](https://github.com/zyn3rgy/ClickonceHunter)

  * searches online for existing ClickOnce published code
  * Google dorks, Github and others

> [AssemblyHunter](https://github.com/0xthirteen/AssemblyHunter)

  * Searches file paths or files and looks for given criteria (signed, identity info, arch, UAC, etc.)
  * Helps identify target applications to weaponize

ClickonceHunter will automate what can be done manually with Google or other related searches.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1EVQ6ywi-HbyrzPmGZJDPow.png)Dorking to Discover Third-Party ClickOnce Deployments ![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1TM8IzuskE7OYqqNR9uZu-g.png)Github Searches for ClickOnce Projects (maybe with signed releases?)

While ClickonceHunter will go look through the internet for existing applications, AssemblyHunter will recursively search local file systems for assemblies that meet the criteria for a regular .NET assembly to be deployed as a ClickOnce application.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1m1CBFIpwHUECuknPYDUUeA.png)Usage for AssemblyHunter ![](https://specterops.io/wp-content/uploads/sites/3/2023/06/10EOR0MICEx2r3Vy6yuyn5g.png)AssemblyHunter Discovering .NET Assembly

Using AssemblyHunter, we can quickly identify assemblies across a host’s filesystem and look for values that will be useful to us.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/18oYTvyI_mKMsrTY0Chnk5g.png)AssemblyHunter Showing Assemblies that can be Weaponized

AssemblyHunter will also show us assemblies that are not useful to us if we would like to see them.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1oEJGl4hNFfsZAmEE9SYLSA.png)Example of anAssembly that Cannot be Weaponized

### **Detection and Prevention Opportunities**

A major benefit to defenders who want to identify malicious ClickOnce deployments is that ClickOnce is not commonly used in many corporate environments. Defenders can baseline their environments to look for how prevalent they are and make detection or prevention decisions. Things we would consider looking for when identifying or preventing malicious ClickOnce use is:

**> **Monitoring _dfsvc.exe_ process activity

  * Monitoring child process activity (e.g. child processes with unsigned module loads)
  * Baseline required ClickOnce activity to whitelist applications with valid business use-cases
  * Monitoring activity associated with _dfshim.dll_(can also be used for launching ClickOnce deployments)

> Evaluate ETW telemetry associated with ClickOnce deployment execution

  * Keep in mind ETW bypasses or _< etwEnable>_ .NET config value

> Baseline the default ClickOnce installation directories

  * _%LOCALAPPDATA%Apps2.0 <string>_

> Baseline of application that have never been seen making connections to the internet

> [Disable all ClickOnce installations from the internet, while still allowing from other trust zones](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)

  * Options include: Enabled, AuthenticodeRequired, and Disabled
  * Zones include: MyComputer, LocalIntranet, TrustedSites, Internet, UntrustedSites
  * To disable installation from internet: _HKEY_LOCAL_MACHINESOFTWAREMicrosoft.NETFrameworkSecurityTrustManagerPromptingLevel — Internet:Disabled_

> If an Application Control solution is deployed

  * Prevent unreputable DLLs from being loaded

If ClickOnce application execution from the internet is disabled using the registry key(s) mentioned above, a user will recieve a prompt that does not give them the option to run the application.

![](https://specterops.io/wp-content/uploads/sites/3/2023/06/1dgkrmVkIsrJCCvZz35WRQQ.png)Prevention of ClickOnce Installation from Internet Trust Zone

### **Closing**

Based on all that was covered, we see ClickOnce as one of the best opportunities for initial access. There are still plenty of areas to dig into and additional potential for offensive use-cases. A few people we want to give thanks to and who paved the way for the work done are Lee Christensen ([@tifkin_](https://twitter.com/tifkin_)), whose exploration of this technique wouldn’t have been possible without him, Casey Smith ([@subTee](https://twitter.com/subtee)) for previous .NET research, and William Burke ([@0xF4B0](https://twitter.com/0xF4B0)) for [previous ClickOnce research](https://www.youtube.com/watch?v=4FtVwiuBtx4).

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=1446ea8051c5)

* * *

[Less SmartScreen More Caffeine: (Ab)Using ClickOnce for Trusted Code Execution](https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 4,547

[ Nick Powers ](https://specterops.io/blog/author/nick-powers/)

Senior Offensive Security Engineer 

Nick Powers is an Senior Offensive Security Engineer, augmenting capabilities for the SpecterOps [Adversary Simulation](https://specterops.io/services/#red-team-engagements) services. His published research focuses on Windows internals, initial access, and post-exploitation techniques.

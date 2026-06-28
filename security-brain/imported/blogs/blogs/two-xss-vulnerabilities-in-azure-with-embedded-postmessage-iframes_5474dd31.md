---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-14_two-xss-vulnerabilities-in-azure-with-embedded-postmessage-iframes.md
original_filename: 2023-06-14_two-xss-vulnerabilities-in-azure-with-embedded-postmessage-iframes.md
title: Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames
category: blogs
detected_topics:
- xss
- cloud-security
- idor
- sso
- command-injection
- rate-limit
tags:
- imported
- blogs
- xss
- cloud-security
- idor
- sso
- command-injection
- rate-limit
language: en
raw_sha256: 5474dd312d041809e5034cc421fe8a2d03efb43bb3b15caa97f5794400df1357
text_sha256: 4e1f71abe7af9407788c1819b21401176b48d71183d13cdc9d8b552a88d892bc
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-14_two-xss-vulnerabilities-in-azure-with-embedded-postmessage-iframes.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, idor, sso, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `5474dd312d041809e5034cc421fe8a2d03efb43bb3b15caa97f5794400df1357`
- Text SHA256: `4e1f71abe7af9407788c1819b21401176b48d71183d13cdc9d8b552a88d892bc`


## Content

---
title: "Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames"
page_title: "Examining Two XSS Vulnerabilities in Azure Services"
url: "https://orca.security/resources/blog/examining-two-xss-vulnerabilities-in-azure-services/"
final_url: "https://orca.security/resources/blog/examining-two-xss-vulnerabilities-in-azure-services/"
authors: ["Lidor Ben Shitrit"]
programs: ["Microsoft (Azure)"]
bugs: ["XSS", "postMessage"]
publication_date: "2023-06-14"
added_date: "2023-06-21"
source: "pentester.land/writeups.json"
original_index: 1048
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames](https://orca.security/wp-content/uploads/2023/06/blog-graphic_research-pod-xss-azure_Cover.jpg?w=1044)

# Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Jun 14, 2023 

  * [ __](https://twitter.com/share?text=Two%20XSS%20Vulnerabilities%20in%20Azure%20with%20Embedded%20postMessage%20IFrames&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](mailto:?Subject=Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)

Microsoft Azure offers a diverse range of services that empower organizations with convenient and scalable cloud infrastructure solutions. However, even robust systems can fall victim to security vulnerabilities that require prompt identification and mitigation. In this blog post, we will describe two dangerous vulnerabilities that we found in Azure services—Azure Bastion and Azure Container Registry—that allow Cross-Site Scripting (XSS) by exploiting a weakness in the postMessage iframe.

Upon discovery of these vulnerabilities, we immediately informed the Microsoft Security Response Center (MSRC), who were able to reproduce the issues. Both vulnerabilities have now been fixed and verified – with no further action required by Azure users. We are grateful to Microsoft for their cooperation and fast action to secure these vulnerabilities.

In addition to describing the technical intricacies of these vulnerabilities and their impact on Azure services, we also provide further details on how to prevent XSS vulnerabilities via postMessage by implementing robust security practices.

## Executive Summary

  * We found two dangerous vulnerabilities in Azure Bastion and Azure Container Registry, that allowed an attacker to achieve Cross-Site Scripting (XSS) by using iframe-postMessages.
  * The vulnerabilities allowed unauthorized access to the victim’s session within the compromised Azure service iframe, which can lead to severe consequences, including unauthorized data access, unauthorized modifications, and disruption of the Azure services iframes.
  * Despite several [Azure security](https://orca.security/partners/technology/microsoft-azure/) enhancements to mitigate the postMessage iframe XSS vulnerability, we still managed to uncover two Azure services – Azure Bastion and Azure Container Registry— that were exploitable via this vulnerability. 
  * We immediately notified Microsoft Security Response Center (MSRC) when we discovered the vulnerabilities. We notified Microsoft about the postMessage XSS in Azure Bastion on April 13th, and the postMessage XSS in the Azure Container Registry on May 3rd.
  * Microsoft was able to reproduce the issues and has since fixed both vulnerabilities in the Azure infrastructure.

## What is Cross-Site Scripting (XSS)?

XSS occurs when an attacker injects malicious scripts into a trusted website, which are then executed by unsuspecting users’ browsers. This can lead to unauthorized access, data theft, and even complete compromise of the affected system. In the case of the vulnerabilities we discuss in this blog, the postMessage iframe vulnerability acted as the entry point for attackers to exploit XSS flaws.

## postMessage and Azure

So before we discuss the postMessage vulnerability, let’s briefly explain what postMessages are: postMessages are used by applications to send messages from one window to another. However, there have been many security implications in postMessages and they can pose a serious security risk if they’re not implemented correctly. 

The postMessage iframe vulnerability that we discovered in Azure Bastion and the Azure Container Registry allowed attackers to embed endpoints within remote servers using the iframe tag. Exploiting this weakness, combined with a lack of proper validation of postMessage origin, adversaries would have been able to execute malicious javascript code and potentially compromise sensitive data.

Azure offers various services and features that leverage iframes for embedding third-party content or enabling cross-domain communication. Unfortunately, if these iframes are susceptible to XSS attacks via the postMessage mechanism, it opens the door for attackers to manipulate the content displayed within the iframe, potentially compromising sensitive data or executing malicious actions within the Azure environment.

Fully aware of the risks associated with the postMessage iframe XSS vulnerability, in recent years, Microsoft has implemented several related security enhancements in Azure. These include stricter content security policies (CSPs) to prevent the execution of untrusted scripts, robust input validation mechanisms, and enhanced monitoring and logging capabilities to detect and respond to potential XSS attacks in real-time. Microsoft also emphasizes the importance of secure coding practices, encouraging developers to sanitize and validate user input effectively, something that we also explain in our best practices recommendations below.

However, despite these security enhancements, we still managed to uncover two Azure services – Azure Bastion and Azure Container Registry— that were exploitable via the Iframe-postMessage vulnerability.

## Attack Flow Using Iframe postMessages

![](https://orca.security/wp-content/uploads/2024/01/image-339.png)

Below we describe the steps an attacker would take to exploit these vulnerabilities in Azure Bastion and Azure Container Registry (prior to the Microsoft fixes):

  1. **Reconnaissance** : The attacker begins by conducting reconnaissance on various Azure services, seeking potential targets, specifically looking for unique endpoints embedded within the Azure portal.
  2. **Endpoint Misconfiguration** : Upon identifying a potential endpoint to target, the attacker searches for a misconfiguration that allows the embedding of the iframe in any remote server. This typically involves a missing X-Frame-Options header or weak Content Security Policies (CSP).
  3. **Exploiting the Misconfigured Endpoint** : Once the attacker successfully embeds the iframe in a remote server, they proceed to exploit the misconfigured endpoint. They focus on the postMessage handler, which handles remote events such as postMessages.
  4. **Analyzing Legitimate postMessages** : The attacker examines the legitimate postMessages sent to the iframe from[ portal.azure.com](http://portal.azure.com/). This analysis helps the attacker understand the structure and purpose of the postMessages, aiding in the construction of malicious payloads.
  5. **Debugging and Identifying Vulnerable Code** : By capturing and analyzing the legitimate postMessages, the attacker identifies potential weak points in the code. They set breakpoints and meticulously debug the code to find vulnerable sections that can be manipulated.
  6. **Crafting the Exploitative Payload** : Once a vulnerable section is identified, the attacker constructs the payload. This involves embedding the vulnerable iframe in a remote server under the attacker’s control and creating a postMessage handler that delivers the malicious payload.
  7. **Delivery and Execution** : The attacker entices a victim to navigate to the compromised endpoint. As the victim accesses the page, the malicious postMessage payload is delivered to the embedded iframe, triggering the XSS vulnerability and executing the attacker’s code within the victim’s context.
  8. **Exploitation Consequences** : The successful exploitation of the XSS vulnerability grants the attacker unauthorized access to the victim’s session within the compromised Azure service. This can have severe consequences, including unauthorized data access, administrative privileges, data theft, unauthorized modifications, or disruption of Azure services.

By understanding these steps, organizations can strengthen their security measures and protect against other postMessage iframe vulnerabilities in Azure services.

## How to Prevent XSS Vulnerabilities via postMessage

To mitigate misconfigured postMessage handlers and prevent XSS vulnerabilities, we recommend following these best practices:

  1. **Validate and sanitize input data** : Ensure that all user-generated or untrusted data is properly validated and sanitized on the server side. Use input validation techniques to reject any input that does not conform to expected patterns. Also, encode user-generated data properly when displaying it.
  2. **Whitelist trusted domains and origins for postMessage communication** : The idea behind whitelisting is to explicitly specify a list of domains that are considered safe and trusted for communication via postMessage. Only messages originating from these whitelisted domains will be accepted and processed, while messages from any other domains will be ignored or blocked.
  3. **Limit accepted message types and formats** : Determine the specific types of messages that are allowed to be processed by your application. This can include restricting messages to specific data structures or predefined formats.
  4. **Implement Content Security Policy (CSP) to restrict script execution** : CSP allows you to define and enforce a set of policies for your web application, including restrictions on which external scripts can be executed. By setting a strict CSP, you can prevent the execution of malicious scripts injected through XSS attacks.

![](https://orca.security/wp-content/uploads/2024/01/image-340.png?w=1200)The Orca Platform alerts if the X-Frame-Options header is not set, which is an important security mechanism to allow a website to specify whether it can be embedded within an iframe

## Two XSS vulnerabilities discovered on Azure

Below we describe in detail the XSS vulnerabilities we discovered in two Azure services:

Vulnerability #1: Azure Bastion SVG Exporter XSS

Vulnerability #2: Azure Container Registry Quick Start XSS

### Vulnerability #1: Azure Bastion SVG Exporter XSS

Below we will demonstrate how a crafted postMessage was able to manipulate the Azure Bastion Topology View SVG exporter to execute an XSS.

#### What is Azure Bastion?

Azure Bastion is a service provided by Microsoft Azure that offers a secure and seamless way to access virtual machines (VMs) within the Azure cloud environment. It acts as a jump server, providing a dedicated and hardened gateway to connect to VMs securely without exposing them to the public internet.

Azure Bastion works by creating a private Remote Desktop Protocol (RDP) or Secure Shell (SSH) session between the user’s local machine and the Azure VM. This eliminates the need for a public IP address on the VM or a virtual private network (VPN) connection. Instead, users can directly access their VMs through the Azure portal, Azure PowerShell, or Azure CLI, using the secure connection provided by Azure Bastion.

When we first started reviewing the Azure Bastion service, we decided to focus on the following possible attack vectors:

  1. How the Bastion Host Capability can be abused
  2. Manipulating the iframe embedding option
  3. The “Connection Troubleshoot” option

In the next paragraph we’ll demonstrate how we used a crafted postMessage to manipulate the Topology View SVG exporter to execute an XSS.

We started by setting up a new Azure Bastion Service using the Azure Portal –

![](https://orca.security/wp-content/uploads/2024/01/image-341.png?w=1021)

After setting up the service, we’ll select the Connect option on the left in order to initiate a connection to the newly created Bastion Host –

![](https://orca.security/wp-content/uploads/2024/01/image-342.png?w=1200)

Here we are presenting the ability to connect to a remote IP Address, using two main Protocols – RDP and SSH, and in order for that to take place we will need to provide credentials. In this case the credentials are not really important so we’ll set the connection with random ones.

Note: By default, the connection will open in a new tab. This is important since we will abuse this functionality later.

![](https://orca.security/wp-content/uploads/2024/01/image-343.png?w=1083)

After clicking on Connect, a new tab will be opened –

![](https://orca.security/wp-content/uploads/2024/01/image-344.png?w=1200)

As we can see a new tab was open, with our Bastion Host address, and a client Host (which in this case is base64 encoded and obfuscated). We are getting a connection error but that’s ok.

### Iframes Architecture

Next, we decided to check the same workflow again, this time with the option ‘Open in new browser tab’ unchecked.

![](https://orca.security/wp-content/uploads/2024/01/image-345.png)

Next, we hit Connect –

![](https://orca.security/wp-content/uploads/2024/01/image-346.png?w=1161)

Ok, so this is a bit messy but it’s very straightforward – Once we decide to connect to the Host without opening new Tab, we’re presented with the template that works as follows:

The <https://portal.azure.com> endpoint will be hosting two main iframes:  
A. BastionHostIFrame.html  
B. Our Bastion Host endpoint, just like when opening the Connection in a New Tab Option.  
---  
  
We can see from the above screenshot, that both endpoints (`BastionHostIFrame.html` and our Bastion endpoint) were set with different sandbox attributes.

`BastionHostIFrame.html` iframe:

<iframe class=”fxs-part-frame” sandbox=”allow-same-origin allow-scripts allow-popups allow-modals  
allow-forms allow-downloads” allow=”microphone *; encrypted-media *;clipboard-read;”  
role=”presentation” src=”<https://hybridnetworking.hosting.portal.azure.net/hybridnetworking  
/>Content/23.4.0.11-230406-2239/BastionHost/BastionHostIFrame.html?clientOptimizations  
=undefined&amp;l=en.en-us&amp;trustedAuthority=https%3A%2F%2Fportal.azure.com&amp;shellVersion=  
undefined#fb4af48503d940fcb1766b787b06ac42″ allowfullscreen=”true”></iframe>  
---  
  
Our endpoint:

<iframe class=”bastion-host-iframe” id=”bastion-host” role=”document” sandbox=”allow-scripts allow-same-origin allow-popups” frameborder=”0″ src=”https://[BASTION_HOST]?trustedAuthority=https%3A%2F%2Fhybridnetworking.hosting.portal.azure.net” aria-label=”Console”></iframe>  
---  
  
We noticed that using sandboxed iframes with the attributes `allow-scripts` and `allow-same-origin` can potentially introduce security risks. These attributes essentially enable any script to be executed within the iframe, and in some cases, the script may have the ability to modify the sandbox attribute itself, which can lead to a vulnerability known as DOM Clobbering vector.

This means that the entire sandbox environment can be compromised, undermining its intended security measures. It’s important to be aware of these risks and take appropriate precautions when working with sandboxed iframes to ensure the overall security of your web applications.

We thought about trying to escape the sandbox with DOM Clobbering but didn’t manage. In addition our sandbox wasn’t set with allow-modals attributes which would not allow us to execute any prompt or alert (For now (: ).

Moving on, we decided to review the connection string –

https://portal.azure.com/#view/Microsoft_Azure_HybridNetworking/BastionHostFrame/resourceId/ %2Fsubscriptions%2F12345678-1234-1234-1234-123456789012%2FresourceGroups%2FOrca-Research%2Fproviders%2FMicrosoft.Network%2Fbh-hostConnect%2F127.0.0.1/dnsName/[CUSTOM_ENDPOINT_HERE]/ newTab~/false/username/test/hostname/127.0.0.1/password/1/privateKey~/null/passphrase~ /null/protocol/rdp/port/3389/vnetId//bastionId/%2Fsubscriptions%2F12345678-1234-1234-1234-123456789012%2FresourceGroups%2FOrca-Research%2Fproviders%2FMicrosoft.Network%2FbastionHosts%2Forca-bastion-poc/keyboardLanguage/en-us-qwerty

Red – Our custom endpoint, could be any endpoint (Burp Collaborator, ngrok etc, IP etc.)  
Green – Could be removed completely, and connection will still go through.  
Blue – New Tab Option (false/true)

So eventually we were left with:

<https://portal.azure.com/#view/Microsoft_Azure_HybridNetworking/BastionHostFrame/resourceId//dnsName/[CUSTOM_ENDPOINT_HERE]/newTab~/false>

We decided to test it with Burp Collaborator:

![](https://orca.security/wp-content/uploads/2024/01/image-347.png?w=1200)

It loaded Burp Collaborator with no issues, and as expected – created a designated iframe for it, and set it under the BastionHostIFrame.html iframe.

This is what it looked like –

![](https://orca.security/wp-content/uploads/2024/01/image-348.png?w=1200)

Next, we tried executing a XSS so it could be leveraged into a one-click action and execute an XSS on the victim’s behalf.

We set an ngrok server, hosted a simple XSS html file and fired –

![](https://orca.security/wp-content/uploads/2024/01/image-349.png?w=1200)

But as expected – no alert was executed due to a missing allow-modals attribute.

### postMessage Vector

Before jumping in and explaining our specific case, we’ll first explain more in-depth what postMessage is as well as its purpose:

postMessage is a web API that allows communication between different origins (i.e., different domains, protocols, or ports) in a web page. It allows scripts on one page to send messages to another page, even if they are served from different origins. This is important because the Same-Origin Policy (SOP) restricts communication between web pages that originate from different domains.

postMessage works by sending a message to a target window or iframe, identified by its origin (i.e., protocol, hostname, and port), using the postMessage method. The target window or iframe must register an event listener using the addEventListener method, which listens for the message event. When a message is received, the event listener can access the message through the event.data property.

In our scenario, when embedding custom endpoints or the Bastion Host endpoint within the BastionHostIFrame.html file, it is crucial to validate and approve the origin of the endpoint before setting it as an iframe. The screenshot below highlights two important aspects:

  1. global.addEventListener: This represents the postMessage Listener/handler that receives incoming messages and processes them using different functions.
  2. isTrustedOrigin: This function plays a critical role in verifying the postMessage origin. It checks the origin against a predefined list of accepted origins, ensuring that only trusted sources are allowed.

By implementing the isTrustedOrigin function, we can effectively control and validate the origins of the postMessage requests, reducing the risk of unauthorized access or malicious activities within the iframe.

![](https://orca.security/wp-content/uploads/2024/01/image-350.png)

In the above screenshot we can see a very typical common in practice in Azure postMessages Handlers –

const isValidOrigin = isTrustedOrigin(evt.origin)  
---  
  
usually, the evt contains the full postMessage i.e

{ “signature”: “FxFrameBlade”, “kind”: “ChangeContrast”, “data”: { “high”: “flow”, “rotate”: true }}  
---  
  
When using the Connection action in the portal, the following postMessage is sent –

![](https://orca.security/wp-content/uploads/2024/01/image-351.png?w=1200)

As seen above, on the **Left** side of the screenshot there are 3 main endpoints (in this specific case) that are handling the postMessage Communication:

  1. The **Azure Portal** ([https://portal.azure.com](https://portal.azure.com/))
  2. The BastionHostIFrame.html endpoint that is hosting the new iframe (<https://hybridnetworking.hosting.portal.azure.net/hybridnetworking/Content/23.4.0.11-230406-2239/BastionHost/BastionHostIFrame.html>)
  3. The new endpoint Iframe (in this specific case, our **ngrok** Server).

In the **middle** of the screenshot we can see the different messages that are being sent between the different endpoints. On the right we can see an example of a postMessage that was sent from the https://portal.azure.com to the BastionHostIFrame.hml –

![](https://orca.security/wp-content/uploads/2024/01/image-352.png?w=1200)

Each message has its own Kind so it will match with the different handlers for each type of message. In the case above, this was the Initialize telling the BastionHostIFrame.html it wanted to host my _ngrok_ server (uri variable).As previously stated, the above-mentioned postMessage was successfully accepted, and our _ngrok_ endpoint was embedded. HOWEVER, note that we embedded an endpoint that contains an HTML file (iframe.html) that contains the following content:

![](https://orca.security/wp-content/uploads/2024/01/image-353.png?w=1200)

The above file is the one that was set in my failed attempt to execute an alert box, and due to allow-modals failed.

Here is a summary of what we have discovered up to this point:

  1. We have successfully embedded various types of endpoints by manipulating the lengthy Connection URL, resulting in a significantly shorter URL.
  2. However, we cannot execute any cross-site scripting (XSS) attacks on the newly embedded iframe because the sandbox attribute is missing.
  3. While DOM Clobbering might be a potential avenue to explore, we have chosen not to prioritize it at this time.
  4. We can manipulate a user into clicking on a legitimate URL, which can then execute malicious JavaScript code.

### Connection Troubleshoot

After a few good hours of working and trying to manipulate the BastionHostIFrame.html endpoint using a custom endpoint embedded, I’ve came up with the **Connection Troubleshoot** Function in Azure Bastion –

![](https://orca.security/wp-content/uploads/2024/01/image-354.png?w=1193)

The Connection Troubleshoot allows us to check for a connection between the Bastion Host and a desired endpoint. I’ll set a new connection test –

![](https://orca.security/wp-content/uploads/2024/01/image-355.png?w=1200)

As seen above i’ve set the 127.0.0.1 as desired testing endpoint, and a random port of 123.

After clicking Check, the test started, and after a few good seconds it end with the following results –

![](https://orca.security/wp-content/uploads/2024/01/image-356.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-357.png?w=1006)

In the above screenshot we are given with two types of results –

  1. Grid View
  2. Topology View

Each of the following views sending different type of postMessages:

The first message that is being sent is the **Ready** message that is being sent once the Grid View is ready (see the Grid View table above).

Once we switch to the Topology View, something interesting takes place, and this is where our vulnerability resides.

In the below screenshot you can see the two different postMessages that are being sent.

![](https://orca.security/wp-content/uploads/2024/01/image-358.png?w=1184)

Before jumping and review the 2nd postMessage of the Topology View I would like to briefly review the postMessage Listener that handles this message –

![](https://orca.security/wp-content/uploads/2024/01/image-405.png?w=1200)

As explained previously, the postMessage is checking various type of data types, such as the Origin, the Signature, Kind and Type.

These are the Trusted Origins:

![](https://orca.security/wp-content/uploads/2024/01/image-359.png)

When reviewing the Topology View after the Connection Test, I’ve noticed that the following endpoint was embedded in the [https://portal.azure.com](https://portal.azure.com/) page:**https://network.hosting.portal.azure.net/network/Content/4.30.1.216/Topology/connectivity.html**

![](https://orca.security/wp-content/uploads/2024/01/image-360.png?w=1200)

Let’s review the connectivity.html:

![](https://orca.security/wp-content/uploads/2024/01/image-361.png?w=1200)

In the above screenshot we can see how the postMessage is being handled, similarly to other postMessage Handlers, it also checks for valid Origin, Type and Method.

Let’s focus on the postMessage that is being sent in order to show the Topology Graph:

![](https://orca.security/wp-content/uploads/2024/01/image-362.png?w=911)

First, we can immediately notice the render method for this message, and if we look in the previous screenshot above, we can see that the handler checks whether the message itself contains the render method (line 57). If it does, it goes through various checks and conditions, until the Graph is created (connectivityGraph.run function) and as I will demonstrate shortly, the same Topology Graph that was created will pass through the exportSVG() function.

When reviewing the postMessage content, I almost immediately noticed right away that the two Nodes from my Topology View were actually SVG images that can be observed for example in the screenshot above (line 11 and line 26). Now from what I know, SVG is also capable of executing malicious Javascript code if not being handled correctly.

I’ve modified the postMessage so it will contains a malicious script and send the postMessage again –

![](https://orca.security/wp-content/uploads/2024/01/image-363.png?w=631)

and the result –

![](https://orca.security/wp-content/uploads/2024/01/image-364.png?w=1168)

Okay, that’s interesting. It appears that the SVG content is not being properly sanitized, which leaves room for manipulation and potential XSS attacks. However, there is a limitation in that we cannot control the main endpoint, which in this case is “[https://portal.azure.com](https://portal.azure.com/),” for obvious reasons. Consequently, we cannot manipulate it to send a postMessage, unless we reproduce the scenario using an External Extension for postMessages. One example of such an extension is the Posta Extension developed by enso security, which does an excellent job by providing a user-friendly interface for reviewing and sending postMessages.

### Endpoint Enumeration FTW

At this stage, I had a solid vector to try and exploit, but could not find the way to control the endpoint of sending the postMessage, not to mentioned I had to pass a **Origin Policy** , so sending a Malicious postMessage from any remote server (such as ngrok) will no work.

I’ve decided to try and look for another endpoint and came across – index.html which at that point I was still not sure what its purpose was since it doesn’t hold any role in the process of generating the Topology View etc.

![](https://orca.security/wp-content/uploads/2024/01/image-365.png?w=1200)

Reviewing the endpoint itself was a lot similar to reviewing the connectivity.html although it has slight differences that will come handy shortly.

We can see that the index.html is also validating its **trustedAuthority** query string

(?trustedAuthority=https://portal.azure.com for example) –

![](https://orca.security/wp-content/uploads/2024/01/image-366.png?w=1016)

Following along the code, we are now presented with the following –

![](https://orca.security/wp-content/uploads/2024/01/image-367.png?w=1146)

We can see that the postMessage Handler is checking for 3 different cases/kind of postMessage –

  1. NetworkWatcherTopology_showTopology
  2. NetworkWatcherTopology_clearGraph
  3. NetworkWatcherTopology_showLoading

**In comparison to the connectivity.html where it only checks for the render kind**

I’ve decided to create the following scenario:

  1. I will use **ngrok** , and host a **index2.html** file on it with the following content –

![](https://orca.security/wp-content/uploads/2024/01/image-368.png?w=1200)

  2. We can see that I’ve created a sendMessageToIframe() function, that will first grab the bastion-host element from the BastionHostIFrame.html iframe and set it in the iframeElement variable.
  3. I’ll create a new variable called **message** that will hold a proper postMessage json that is corresponded with a valid postMessage that will be received by the postMessage Handler in index.html.
  4. The kind of the postMessage will be NetworkWatcherTopology_showTopology.

![](https://orca.security/wp-content/uploads/2024/01/image-369.png?w=1200)

  1. I’ll use the iframeElement from before, and will send a postMessage to it (notice the “*” which stands for any Origin).
  2. In the second red rectangle above I’ve created a simple “send-button” so it will be much easier to send the postMessage once clicked.
  3. Last but not least I will recreate the same iframe for index.html with all relevant attributes (including **allow-modals**)

The final embedded **ngrok** +index.html will look like the following –

![](https://orca.security/wp-content/uploads/2024/01/image-370.png?w=1200)

From the above we can see the “Send” button which is aimed to send the postMessage. The red arrow indicates the first function that my postMessage will get to (receiveMessage). I’ll set up a Breakpoint to debug it and see it step by step.

![](https://orca.security/wp-content/uploads/2024/01/image-371.png?w=1200)

Once clicked, the postMessage is sent and stopped at the function.

event – This is the complete postMessage content. event.data – Only represent the data itself (the postMessage Kind etc.)

We can see both values in the bottom part of the screenshot (dev console).

Next, the message will go through checking for **valid** Origin. in our case it was valid since it was send as follows:

https://network.hosting.portal.azure.net/network/Content/4.30.1.216/Topology/index.html?trustedAuthority=https://network.hosting.portal.azure.net

meaning that https://network.hosting.portal.azure.net is a subdomain for [portal.azure.net](<https://network.hosting.portal.azure.net>) which is on the list.

![](https://orca.security/wp-content/uploads/2024/01/image-372.png?w=1200)

moving on, we can see the kind check as well –

![](https://orca.security/wp-content/uploads/2024/01/image-373.png?w=1200)

After checking the data, and data.kind our postMessage enter the switch sets –

![](https://orca.security/wp-content/uploads/2024/01/image-374.png?w=1146)

The code starts going through the NetworkWatcherTopology_showTopology, after checking for the different files dependencies, it being “sent” to the topology.run method which takes all variables and arguments from the postMessage and prepare an empty structure to be populate by the SVG – in our case the svgurl which holds the empty structure is now being sent to the exportSVG().

![](https://orca.security/wp-content/uploads/2024/01/image-13.png?w=1200)

The exportSVG() function uses different built-it components from external modules (**yfiles**) and starts building the SVG image for each Node (Node=host/endpoint).

Each node is being set to the createNodes function which is the key module to take the SVG and present it.

![](https://orca.security/wp-content/uploads/2024/01/image-375.png?w=1200)

From there, it goes to the next step of Styling the node itself, i.e populate each image with the SVG –

![](https://orca.security/wp-content/uploads/2024/01/image-376.png?w=1200)

Using a Breakpoint, we can see that my malicious SVG (containing the onmouseover=alert(document.domain)) was received and getting to the createHTMLDocument sink. Finally our SVG is presented on the malicious iframe once clicked.

![](https://orca.security/wp-content/uploads/2024/01/image-377.png?w=1200)

Once hovering the image we can see alert() being executed but the expected sandbox!

Finally all we have to do is build the full scenario:

  1. A remote attacker will create a legitimate but malicious endpoint by abusing the Bastion Host Connection but this time it will open automatically since the newTab sets to **true.**

<https://portal.azure.com/#view/Microsoft_Azure_HybridNetworking/BastionHostFrame/resourceId//dnsName/d52d-XX-XX-XX-XX.ngrok-free.app%2Findex.html/newTab~/true>

  2. A new tab will be opened containing the vulnerable endpoint (index.html) embedded as iframe –

![](https://orca.security/wp-content/uploads/2024/01/image-378.png?w=1200)

  3. **For demonstrating purposes I created a Send button that will send a malicious postMessage to the vulnerable endpoint since this could also be performed automatically without any user interaction.**
  4. Once clicking on Send, I’ve created two new iframes to demonstrate what is the website that is hosting the iframe, and the vulnerable iframe itself. 
  5. We can see that I’ve created a demo SVG with a nice Orca Security whale with on onmouseover event embedded within. plus two new iframes (the blank index.html and the **ngrok** itself).

![](https://orca.security/wp-content/uploads/2024/01/image-379.png?w=825)

Once hovering, the alert(document.domain) pops up!

![](https://orca.security/wp-content/uploads/2024/01/image-404.png)

I’m also attaching the full POC without user interaction (without the Send button):

<https://www.dropbox.com/s/ehinlsdg48a6q69/azure_bastion_xss.mov?dl=0>

## Vulnerability #2: Azure Container Registry Quick Start XSS

Below we will demonstrate how a crafted postMessage was able to manipulate the Azure Container Registry Quick Start to execute an XSS.

### What is Azure Container Registry?

Azure Container Registry is a managed cloud service provided by Microsoft Azure that allows users to store, manage, and deploy container images. It provides a centralized location for hosting your container images, allowing you to efficiently manage and version them.

When first starting to review the Container Registry Service, we really didn’t know where this possibly went wrong. The ACR Service is very straightforward and provides a very user-friendly way of setting up a new Registry endpoint that can be used for various Container Services that Azure provides.

This is the default page of the Container Registry when creating a new service –

![](https://orca.security/wp-content/uploads/2024/01/image-380.png?w=1200)

After briefly reviewing the various options and pages for the Container Registry, we noticed the **Quick Start** tab –

![](https://orca.security/wp-content/uploads/2024/01/image-381.png?w=1111)

The above page is shown. This is in fact an iframe that is embedded within the Portal Page that communicates with the page using postMessages as we can see from the screen below –

![](https://orca.security/wp-content/uploads/2024/01/image-382.png?w=985)

This is the html file that is being embedded and communicated with –

<https://containerregistry.hosting.portal.azure.net/containerregistry/Content/1.0.20230403.6/QuickStart/index.html>

For example, let’s review the following message –

![](https://orca.security/wp-content/uploads/2024/01/image-383.png?w=833)

In the above screenshot we can see how the different text that is being sent in the postMessage is reflected in the portal itself.

We modified the text a little as you can see on the right side of the screen below. Once sent, the content is immediately presented in the UI –

![](https://orca.security/wp-content/uploads/2024/01/image-384.png?w=1200)

What about XSS? We tried sending a modified payload –

![](https://orca.security/wp-content/uploads/2024/01/image-385.png)

Rendered in the UI – an alert box popped up.

![](https://orca.security/wp-content/uploads/2024/01/image-386.png?w=892)index.html postMessage Logic

So now that we have something primitive, let’s try to fully exploit it. When reviewing the iframe itself, it seems that the allow-modals attribute is set, which could indicate a possible JS code execution such as alert, prompt, print etc.

![](https://orca.security/wp-content/uploads/2024/01/image-387.png)

We started by embedding the index.html file via an iframe tag using my remote ngrok server –

![](https://orca.security/wp-content/uploads/2024/01/image-388.png?w=1200)

Note that since we embedded the following link with its original query strings (https://containerregistry.hosting.portal.azure.net/containerregistry/Content/1.0.20230403.6/QuickStart/empty.html?clientOptimizations=undefined&l=en.en-us&trustedAuthority=https%3A%2F%2F&shellVersion=undefined#6c0a497347cc45f8a5b6f684d1e7cdfb), we can see that an empty **trustedAuthority (”https://”)** is set. Therefore, the page managed to load properly but with an important constraint that will be discussed later on.

![](https://orca.security/wp-content/uploads/2024/01/image-389.png?w=800)

When reviewing the iframe itself, we can see the following functions and handlers. Among them is a very common way of checking the Parent Origin in an Azure service – allowedParentFrameAuthorities ****with various domains that allow for communicating with the endpoint.

![](https://orca.security/wp-content/uploads/2024/01/image-390.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-391.png)

When trying to manipulate the page to allow us to send a postMessage, we tried to modify the allowedParentFrameAuthorities ****to one of the allowed domains ****([https://portal.azure.com](https://portal.azure.com/)).

![](https://orca.security/wp-content/uploads/2024/01/image-392.png?w=1200)

When trying to embed the page again using the same technique (Query String) –

![](https://orca.security/wp-content/uploads/2024/01/image-393.png?w=627)

It seems that it is being blocked by the Content Security Policy (frame-ancestors) of the vulnerable html endpoint.

**What Now?**

So we now know that the page is vulnerable via postMessage but we can’t control any allowed domain in order to send a payload.

We continued to search for additional endpoints –

![](https://orca.security/wp-content/uploads/2024/01/image-394.png?w=1200)

When enumerating the main endpoint we discovered a new endpoint empty.html

Reviewing the new endpoint –

![](https://orca.security/wp-content/uploads/2024/01/image-395.png?w=1019)

It seems very similar to the main index.html file but without text.

**Let that sink in..**

Let’s review the code itself –

![](https://orca.security/wp-content/uploads/2024/01/image-396.png)

It seems that the specific file is missing a crucial Origin check, hence any postMessage will be received. In addition, the vulnerability resides in the innerHTML sink as can be seen above.

![](https://orca.security/wp-content/uploads/2024/01/image-397.png?w=883)

As can be seen from the screens above, the endpoint is originally replacing the registry link with a custom one that it receives from the postMessage.

We try to send the following –

![](https://orca.security/wp-content/uploads/2024/01/image-398.png)

Using a Breakpoint we can see the various checks that our message will pass –

![](https://orca.security/wp-content/uploads/2024/01/image-399.png)

Later on it checks for the message **kind (”loginServer”) –**

![](https://orca.security/wp-content/uploads/2024/01/image-400.png)

Finally, it reaches the innerHTML sink, where our payload will be replaced with the registry url.

![](https://orca.security/wp-content/uploads/2024/01/image-401.png)

Final result –

![](https://orca.security/wp-content/uploads/2024/01/image-402.png)

**Exploit Workflow**

  1. First step is to create a ngrok server that will host the **empty.html** vulnerable page as iframe.
  2. After loading the iframe, we send a crafted payload postMessage that will be received by the vulnerable page.
  3. We use the following payload –

![](https://orca.security/wp-content/uploads/2024/01/image-403.png)

![](https://fast.wistia.com/embed/medias/bju1nqnibq/swatch)

## The Orca Cloud Security Platform

Orca’s agentless [cloud security platform](https://orca.security/platform/) connects to your environment in minutes and provides 100% visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, sensitive data at risk, weak and leaked passwords, and overly permissive identities.

  * [ __](https://twitter.com/share?text=Two%20XSS%20Vulnerabilities%20in%20Azure%20with%20Embedded%20postMessage%20IFrames&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)
  * [ __](mailto:?Subject=Two XSS Vulnerabilities in Azure with Embedded postMessage IFrames&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fexamining-two-xss-vulnerabilities-in-azure-services%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).

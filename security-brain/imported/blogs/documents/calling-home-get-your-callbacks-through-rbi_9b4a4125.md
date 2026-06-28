---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-17_calling-home-get-your-callbacks-through-rbi.md
original_filename: 2024-01-17_calling-home-get-your-callbacks-through-rbi.md
title: Calling Home, Get Your Callbacks Through RBI
category: documents
detected_topics:
- xss
- sso
- saml
- access-control
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- sso
- saml
- access-control
- command-injection
- file-upload
language: en
raw_sha256: 9b4a4125b052bb156b48e6010e16c62d747291dd18a83b33f2fd33da2ac056ff
text_sha256: ae9833087a5d60c4ab61fa36129f8fee64c459cc4dd2e1cb29c55ef190c89241
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Calling Home, Get Your Callbacks Through RBI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-17_calling-home-get-your-callbacks-through-rbi.md
- Source Type: markdown
- Detected Topics: xss, sso, saml, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `9b4a4125b052bb156b48e6010e16c62d747291dd18a83b33f2fd33da2ac056ff`
- Text SHA256: `ae9833087a5d60c4ab61fa36129f8fee64c459cc4dd2e1cb29c55ef190c89241`


## Content

---
title: "Calling Home, Get Your Callbacks Through RBI"
page_title: "Calling Home, Get Your Callbacks Through RBI - SpecterOps"
url: "https://posts.specterops.io/calling-home-get-your-callbacks-through-rbi-50633a233999"
final_url: "https://specterops.io/blog/2024/01/17/calling-home-get-your-callbacks-through-rbi/"
authors: ["Lance B. Cain", "Alexander DeMine"]
bugs: ["Red team", "Phishing", "Remote Browser Isolation (RBI)", "Command and Control (C2)"]
publication_date: "2024-01-17"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 527
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Calling Home, Get Your Callbacks Through RBI

Author

[Lance B. Cain](https://specterops.io/blog/author/lance-b-cain/)

Read Time

22 mins

Published

Jan 17, 2024

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F01%2F17%2Fcalling-home-get-your-callbacks-through-rbi%2F&title=Calling+Home%2C+Get+Your+Callbacks+Through+RBI&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F01%2F17%2Fcalling-home-get-your-callbacks-through-rbi%2F&text=Calling+Home%2C+Get+Your+Callbacks+Through+RBI) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Calling Home, Get Your Callbacks Through RBI&Body=https://specterops.io/blog/2024/01/17/calling-home-get-your-callbacks-through-rbi/) [ ](https://specterops.io/blog/category/research/feed/)

_Authored By:_[Lance B. Cain](https://medium.com/u/040c3e09d079) _and_[ _Alexander DeMine_](https://medium.com/u/de29a5193240)

### Overview

Remote Browser Isolation (RBI) is a security technology which has been gaining popularity for large businesses securing their enterprise networks in recent years. This blog post describes methods that SpecterOps consultants have researched to successfully circumvent this technology during offensive assessments. Following a brief introduction to the technology, we share our firsthand experiences when encountering RBI solutions and techniques the SpecterOps team have employed for establishing command and control (C2) to systems that proxy traffic through RBI products broken down into three segments: **Payload Ingress**, **C2 Egress**, and **RBI Bypass**. This post then concludes with us sharing our perspective regarding the recommendation of RBIs as a defensive product for the modern enterprise.

### What is RBI and Why Use It?

Browser isolation is a security concept in which a user’s web traffic is isolated in a virtual machine, hosted web browser, or some other manner to prevent malicious activities from reaching the end user; thereby lowering the general risk of web browsing. There are three types of browser isolation in use today: client-side browser isolation, on-premises browser isolation, and RBI. As these names imply, client-side virtualizes the browsing on the local host, on-premises runs within the organization, and RBI virtualizes the web sessions in the cloud. Each type of browser isolation has different pros and cons, but we will focus on RBI today.

The general concept of RBI is relatively simple. When users open their web browser to surf the web, they are not merely doing so from their local machine; rather, they are connecting to a cloud-hosted virtualized browser in which all web content is rendered and executed and then sent back to the end-user in a sanitized manner (Figure 1). Different vendors stream the content to the user differently, but it is sufficient to say they all do the same thing: sanitize and render client web traffic.

![](https://specterops.io/wp-content/uploads/sites/3/2024/01/1EJZIdvkDgdThnyDr0mV5MA.png)_Figure 1 — Cloudflare RBI Diagram_

The primary focus of RBI is to prevent user interactions with web-based malware such as cross-site scripting (XSS), drive-by downloads, and various forms of malicious JavaScript. In this function, it does an excellent job. It is tough to get a user to fall for your finely crafted HTML smuggling attack when the webpage never actually makes it to the end user; their browser just shows a stream of pixels while the content renders on a separate system.

### Why Do We Care?

At this point, you may ask yourself, “I don’t really do web-based attacks. Why should I care?” Well, my friend, RBI has many more implications than what the vendors provide at face value. Most RBI security vendors supplement their solution with extra email protections to block the delivery of malware via user inboxes along with scanning, sanitizing, and blocking malicious downloads from any site. Additionally, one of the primary concerns you should have as an offensive professional is the profound impact RBI will likely have on your C2 traffic.

It is not generally advertised on the product pages that RBI affects C2 traffic, but we promise you it does. Most RBI solutions we have dealt with are not set up to send individual browser sessions to a cloud-virtualized host. They may offer a link where a user can do that, but an organization usually has a proxy setup that sends **ALL** web traffic through RBI. This means your stealthy HTTPS C2 traffic gets sent through the same virtualized host process the same as everything else and results in the server responses to your agents being rendered as an inert stream. As you can probably imagine, trying to figure out why your C2 traffic is not returning when an organization uses RBI can be very frustrating.

If your next engagement has RBI in place to protect their web traffic; what do you do? Fear not, dear reader; we have asked the same question and are here to help you work through it. We categorize our suggested techniques into three categories:**** ingress, egress, and bypass. Ingress is pretty self-explanatory, but you may wonder why egress and bypass are separated. In our opinion, they are similar but distinctly different techniques concerning RBI. Egress can be summarized as getting your C2 traffic to call back using traffic that communicates “through” the RBI solution, while bypass (as the name implies) means we are taking a different route entirely by avoiding RBI solutions.

### Payload Ingress

When delivering payloads to clients through RBI solutions, these solutions’ sandboxing and scanning capabilities present significant hurdles that must be overcome to achieve code execution in your target environment. RBI solutions typically allow the configuration of file upload and download profiles, restricting the types of files that can be submitted or retrieved from websites based on multiple factors such as file extension, size, entropy/encryption of data, signatures, site reputation, and more. As is tradition, different vendors implement these checks in diverse ways, so you will want to brush up on what the target organization is using to give your payloads the best chance of making it through these defensive solutions, but we have some generalized recommendations to help with that.

#### Sandbox Evasion and System Checks

These two considerations should hopefully be standard in most of your payloads, but you will want to implement them if you haven’t already. Utilizing standard techniques such as prime factorization, thread sleep checks, executing environment checks/guardrails like enumerating processors in a system, string obfuscation, string building, non-terminating conditional-based loops, and logic structures relying on user input will help you get through the RBI scanning process. Why? Well, the RBI solutions need to attempt to scan, sandbox, and evaluate the files they are proxying to users without causing too much of a burden on the user’s browsing experience. Slow browsing leads to unhappy users and unhappy users lead to security products being removed. By increasing the time it takes to evaluate a file, we can bypass some RBI products that, by default, are set to a fail-open state (i.e., if they cannot scan a file in a sufficient amount of time nor detect malicious logic while executing it in a sandbox, then it will just let the file through).

#### Antivirus Inspection

Not all RBI products will prioritize this time factor. Some may only allow a user to view the file contents in the browser or allow the user to download a sanitized version of the file in which the product removes macros, JavaScript, or any other content the vendor deems may be suspicious; leaving the user with an inert download. Other RBI solutions are set to a fail-closed state that blocks the download of a file if it cannot scan it. This can be due to encryption or even size. For example, Cloudflare Zero Trust blocks uploads and downloads of encrypted, password-protected files or files larger than 15MB by default because it cannot scan those files.

If we cannot send an encrypted payload because AV will block it since it cannot scan it, but we also cannot send an unencrypted payload because it will fail an AV check and get blocked, then what do we do? In our experience, obfuscation techniques like encoding data with Caesar ciphers and sandbox evasion checks have proven successful when delivering payloads through RBI solutions. Encoding using a technique with low entropy often has the products scan the delivered files since they are not fully encrypted. However, environment checks, large prime factorization calculations, and non-terminating loops relying on user input prevent the sandbox analysis from observing malicious logic execution since these cannot supply additional input or meet the environment requirements.

#### Users Are Still a Weak Point

The additional challenges RBI solutions present mean we likely need to leverage the human factor to deliver payloads successfully. Although not impossible, the likelihood of bypassing the RBI in a technical manner is low. However, people are naturally curious, and like any good campaign, enticing the user to pull the payload to their system is often the preferred way to go.

When creating payloads such as Office documents,  _.pdf_ files, etc., that serve as an initial dropper capability, it is imperative to design them with hidden content or obfuscation that forces user interaction. Requiring user-supplied values such as passwords to access content increases the likelihood of successful payload detonation and delivery. With user input required, it is unlikely that an RBI solution will be capable of supplying a password or clicking a user engagement button/checkbox when sandboxing a payload and, therefore, cannot detonate any malicious logic during analysis. Be mindful of how you implement the password, though, as fully encrypting a document with a password may get the file blocked since it cannot be scanned. If a user is presented with a rendered document that is obfuscated/unreadable in the RBI browser rendering or sanitized version, they will be enticed to download the document locally and execute the included payload.

Let us move into some demonstrations on payload ingress. We will use Cloudflare’s Zero Trust RBI solution for the demonstrations in this post. This is by no means any slight against Cloudflare’s product; it does its job well and we are fans of it. It just happened to be the solution we were actually able to get our hands on at a reasonable price, which we also see as a good thing as they make RBI reasonably available for most people. We will not be covering any phishing portions of the task, instead leaving that to the reader and presuming the user has reached the point of downloading and executing our payload. During these demonstrations, we are using the Mythic framework with the Apollo agent.

First, we will use a straightforward HTTP C2 profile configuration going to our testing C2 domain (i.e., _HTTPS://WWW.HALFLINGHIDEOUT.COM_) with a standard accept header and user agent (Figure 2).

![](https://cdn-images-1.medium.com/max/979/1*CcxaxlT11fiUgHTjbMc4jg.png)_Figure 2 — HTTP C2 Profile Configuration_

In testing the payload, we can see that in Burp Suite it is successfully reaching back to Mythic through our redirectors (Figure 3).

![](https://cdn-images-1.medium.com/max/979/1*frzXhsZfrBzbliXfMRstGw.png)Figure 3 — Tested C2 Callback Successful

For our initial payload delivery, we are using a ClickOnce application. If you want to know more about abusing ClickOnce applications, we highly recommend you check out the blog post Nick Powers ([@zyn3rgy](https://twitter.com/zyn3rgy)) and Steven Flores ([@0xthirteen](https://twitter.com/0xthirteen)) posted on the subject: [Less Smartscreen More Caffeine: (Ab)using ClickOnce for Trusted Code Execution](https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5). In standard ClickOnce fashion, we click the application file and are prompted with the application run prompt security warning; clicking “Run” starts the installation (Figure 4).

![](https://cdn-images-1.medium.com/max/979/1*Wzujuz2FHrpJEBE5q_WpsA.png)_Figure 4 — ClickOnce Application Security Warning_

However, halfway through the installation, we encounter an error message. The application cannot retrieve all the files, corrupting the installation (Figure 5).

![](https://cdn-images-1.medium.com/max/979/1*ybbxNSN079RcTvSbPCg4pQ.png)_Figure 5 — ClickOnce Application Installation Error_

By digging into the details, we can see that the issue lies in the _Syncfusion.Tools.Window_ s _.dll_ file (Figure 6). Furthermore, we can see in the Cloudflare gateway logs that the file was blocked for failing the AV scan (Figure 7 and Figure 8).

![](https://cdn-images-1.medium.com/max/979/1*WcMo6WuCEH7rWhiK2H3zDg.png)_Figure 6 — ClickOnce Application Error Details_ ![](https://cdn-images-1.medium.com/max/979/1*MJErTHKLR-P3wA0tRENvJQ.png)_Figure 7 — Cloudflare Block Log_ ![](https://cdn-images-1.medium.com/max/383/1*41EJEEiOm9xaHtCMA5d_Bw.png)_Figure 8 — Cloudflare Block Log Details_

We know this file does not contain malicious content, but if we check the setting on our Cloudflare setup, we can confirm that the default setting that blocks all requests that cannot be scanned is the issue because the file is too large (Figure 9). We will not be able to get our payload in this way if we cannot get all of our application files in. If we dig into the documentation, we can get the complete set of information on the non-scannable files (Figure 10). The default setting for Cloudflare is to fail-closed.

![](https://cdn-images-1.medium.com/max/979/1*4_NyZxJi5a6jyQr_Smp6mw.png)_Figure 9 — Cloudflare Network Settings_ ![](https://cdn-images-1.medium.com/max/979/1*tzFhDQBZgrjCY3vGktko3g.png)_Figure 10 — Cloudflare Documentation_

Since our initial ClickOnce route did not work, let’s change tactics. We can swap our delivery vector to a ISO image file (_.iso_) with a macro-embedded Excel file (_.xlsm_). The Excel file is obfuscated and uses a password to protect the content; however, we are protecting it via the macro instead of Excel’s standard password protection encryption. We do this so Cloudflare can still scan the file, but the scanner will not make it past the password prompt when running sandboxed analysis. With everything loaded up and sent, we can see that we can download the  _.iso_ file instead of getting blocked like our previous ClickOnce attempt (Figure 11).

![](https://cdn-images-1.medium.com/max/979/1*lb74KTDIkvBZAdAqNjQfrg.png)_Figure 11 — Successful ISO Download_

Next, we double-click the ISO file and select “Open” to mount it (Figure 12). Then, we drag the Excel file to our desktop, so we do not have the Windows [Mark-of-the-Web](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked#mark-of-the-web-and-trusted-documents) on it (Figure 13).

![](https://cdn-images-1.medium.com/max/428/1*Vlr0CqyLdhqDzgK4v7DuAQ.png)_Figure 12 — ISO Mounting Security Warning_ ![](https://cdn-images-1.medium.com/max/600/0*QAGoKprnja9TTQ6F)_Figure 13 — Excel Export_

When we open the Excel file, we see what appears to be encrypted contents, and the warning asks us if we want to enable the macro. The content is hidden to entice the user to enable the macros. Once we enable the macros, we are prompted to input a decryption password (Figure 14). When the password is entered, Excel tells us we have started decrypting (Figure 15), and finally, we switch out the shown sheets, and the content is shown to the user (Figure 16). On the backend of this process, the macro is writing our payload to disk and executing it.

![](https://cdn-images-1.medium.com/max/979/1*d_PI6LypODmtpJhNzruEbg.png)_Figure 14 — Macro Password Protected Excel_ ![](https://cdn-images-1.medium.com/max/470/1*fvUmDFzRRTUJN-Fy9pK1Zg.png)_Figure 15 — Macro Decryption_ ![](https://cdn-images-1.medium.com/max/402/1*Fc9kECaxbZpPkGish9bgTA.png)_Figure 16 — Excel Content Shown_

However, we still have not received our callback. When we check out Burp Suite logs, we see that the C2 traffic is not getting the 200 response we hoped for (Figure 17). We then check out Cloudflare logs and confirm that the RBI is isolating our C2 traffic (Figure 18).

![](https://cdn-images-1.medium.com/max/979/1*o42tqKniPDZJKw5Ds6Sd8w.png)_Figure 17 — Unsuccessful C2 Callback_ ![](https://cdn-images-1.medium.com/max/979/1*zBrl1uSf-JgfFRSgXrqgbg.png)_Figure 18 — Cloudflare Isolation Log_

### C2 Egress

The first hurdle is over; we got our payload into the target environment. Now, we need to get the C2 session back out. Like the ingress section, while some talking points may not be new, we will cover them to better explain how RBI products affect C2 traffic when deployed in a target environment.

#### HTTP

We will start with general HTTP(S) communication methods. Based on our experience with RBI, our first recommendation when crafting C2 traffic intended to egress an RBI solution with HTTP traffic is to omit any _POST_ requests. Most RBI solutions implement features for Data Loss Prevention (DLP) that limit data that can be submitted or posted to different websites. Some vendors require explicit whitelisting of websites where data can be submitted using _PUT_ or _POST_ HTTP requests. A _GET_ -only C2 profile will help save some heartache in the initial stages of getting an initial foothold; however, you can always expand into _POST_ requests once you have the foothold to try and get the better C2 flow since _GET_ -only profiles tend to be slower overall and produce significantly more transactions to exchange data with C2 servers.

If your C2 supports it, you can also try using web socket profiles like those available for many payloads in the Mythic framework. Since web sockets can currently only function without isolation, some RBI solutions may allow them by default. However, vendors differ and some may require whitelisting of approved sites where web sockets can be utilized. As with much of this post, your best bet is to study which vendor your target is using so you know how to use this information to fine-tune your traffic.

#### Headers

Like many web proxies and traffic-based security solutions, the headers in your C2 profile will matter in terms of blending in and getting through. However, the type of header you use can change how the RBI solution responds to your C2 traffic and may allow you to get out without much trouble. One initial significant header to include is a user agent. Be sure to explicitly set a modern browser-based user agent that is expected to exist in your target environment. Not all RBI solutions will block this, but many will block web traffic with user agents that do not match approved web browsers or do not meet a minimum sufficient version of a browser.

Next, we have the Content-Type. While setting Content-Type to try to match vanilla web traffic to blend in is common, this can be a significant hindrance (and easy fix) when dealing with RBI products. Many RBI solutions will look for a Content-Type of “text/html” and send that traffic through isolation to ensure safe browsing for the user, which will result in breaking our C2 traffic. We recommend changing the Content-Type away from “text/html” if possible. Below is an example of two web requests from PowerShell, one isolated and the other inspected but not isolated (Figure 19 and Figure 20). The only difference between the requests was that the request on the left had a Content-Type of “application/json” and the right had “text/html”. We have even succeeded by removing the Content-Type header entirely, though we do not regularly recommend doing this as it will make your traffic look very suspicious.

![](https://cdn-images-1.medium.com/max/979/1*RtdBnnYKcOXeO8lMw98QWQ.png)_Figure 19 — Accept Header Comparison “application/json”_ ![](https://cdn-images-1.medium.com/max/979/1*0W8CzZ0z2k8kAEnIj7wfJA.png)_Figure 20— Accept Header Comparison “text/html”_

#### Cookies

Our final header worth mentioning is cookies. Passing the C2 traffic in a cookie is not a new way of doing business, but it can be a great technique to get through RBI. Some RBI solutions virtualize and stream the web page content but transparently pass the cookie header to the other end of the channel for usability since many sites require cookie functionality. As with many solutions, usability equals abusability. We recommend modifying your C2 profile to send the traffic in the cookie and get your sessions out of the target environment as another potential option.

#### HTTP Authentication

When attempting to have HTTP traffic egress an RBI security product, you must be prepared to authenticate to get out. Many RBI solutions implement SAML/NTLM/Basic authentication for outbound traffic that requires payloads to be able to authenticate to the web proxy when a HTTP 407 “Proxy Authentication Required” authorization message is returned.

Some tools do not need to worry about this as much as others. PowerShell can natively use stored Kerberos tickets when creating web requests and can be a fundamental capability for web traffic to egress an authenticated proxy using Invoke-WebRequest for droppers. Cobalt Strike has a native capability to specify a proxy and credentials if known. It can automatically utilize stored NTLM credentials if available on a local system using the WinInet API if the proxy accepts it for basic or NTLM authentication. If you use payloads that are not proxy-aware or do not support providing credentials to egress, you will likely need to modify them or pick a new C2 framework for your RBI engagement.

#### Redirectors

As with any C2 channel, your redirector setup will significantly impact how RBI solutions react to your traffic. If you use a strict set of rewriting rules to filter traffic to your redirectors, you may need to open the rules up if the customer uses RBI since the traffic frequently traverses cloud-virtualized infrastructure instead of directly egressing from an organization’s assets; this is to avoid inadvertently blocking new payloads checking in from client environments because they originate from unknown addresses/spaces. Once you know where the traffic is coming from, you should trim down the rules to only what you need to allow and redirect everything else to somewhere else (like the ubiquitous _HTTPS://WWW.GOOGLE.COM_).

Another critical factor is the need to use reputable domains for your redirectors. We do not mean just using domains not classified as malicious; you need actual classifications. Many RBI solutions will block uncategorized sites or sites classified as grayware. More than one RBI security vendor has begun internally tracking site categorizations and can even develop profiles per domain when users access new sites. This makes it more imperative that C2 domains are well established with positive reputations and a good history of being categorized as trustworthy in reputable categories such as news, finance, or healthcare sites.

Lastly, you can likely kiss any unencrypted HTTP traffic goodbye. Ensure you have valid TLS certificates, as RBI products often block unencrypted HTTP traffic. Again, there is nothing necessarily new here, but it is something you want to get set up correctly to help you get a C2 session back to your infrastructure.

So why was our traffic not getting through before? If we look into the product documentation, we can find the answer we need for now. We can see in the isolation documentation that the isolation policies will apply to requests that include the “text/html” accept header (Figure 21). In this case, ensuring our C2 traffic included that to blend in with most web traffic was our downfall.

![](https://cdn-images-1.medium.com/max/979/1*y6x3MmDCcPK5fvKNjAqiMg.png)_Figure 21 — Cloudflare Isolation Documentation_

Let us change our headers and try again. We modify our accept headers on our C2 profile in Mythic and build a new payload (Figure 22).

![](https://cdn-images-1.medium.com/max/979/1*HOUbulEvm2cyS9fiBHwPpA.png)_Figure 22 — Updated HTTP C2 Profile_

Once we get the new payload on the host and execute it, we can see the difference in the traffic. Our Burp Suite shows our desired 200 response code (Figure 23), and Cloudflare shows that our traffic was allowed through to the redirector (Figure 24). Finally, we have our callback to Mythic (Figure 25).

![](https://cdn-images-1.medium.com/max/979/1*zvsTVQ920QJrWMUKHBCMxg.png)_Figure 23 — Successful Callback in Burp_ ![](https://cdn-images-1.medium.com/max/979/1*QNdjrHuuH-JoCbX3hHEOxA.png)_Figure 24 — Cloudflare Allowed Log_ ![](https://cdn-images-1.medium.com/max/414/1*Lg5v4rHlkT-6EDAstcVrFg.png)_Figure 25 — New Callback in Mythic_

### RBI Bypass

Though we are covering it last, the most accessible methods of establishing C2 communications in customer environments that have deployed RBI solutions are to bypass these protections altogether when possible. This can be accomplished in a couple of different ways depending on the capabilities and configuration of the RBI implementation using either **DNS C2** or **Third-Party C2****.**

#### DNS C2

Many RBI solutions only monitor HTTP/HTTPS traffic by default and either require explicitly configuring DNS monitoring or lack that capability altogether. A DNS C2 channel will commonly establish successful callbacks using UDP traffic that will be under less scrutiny rather than egressing a proxy. This comes with the OPSEC consideration that an increase in the volume of DNS requests, especially without any additional web requests resulting from the DNS resolution, can indicate compromise.

Some RBI solutions purport to perform DNS monitoring and inspection, but the effectiveness of these measures will vary by vendor; ultimately, this will rely upon the defensive maturity of your client environments. In our experience, DNS traffic is typically either being monitored and C2 communications will be quickly identified, or it is not monitored at all in many environments.

#### Third-Party C2

When establishing new HTTP/S communication channels through RBI solutions, new domains and IP connections will be subject to inspection for any new traffic. However, it is common for popular applications to either be implicitly or explicitly excluded from inspection for RBI solutions, allowing their traffic to essentially bypass isolation when communicating with their servers. This can be leveraged to establish C2 communication through trusted applications using projects such as [C3](https://github.com/WithSecureLabs/C3) on GitHub, which uses third-party applications like Dropbox, Google Drive, Discord, and Slack to communicate with a team server over the web application channels.

### Our Recommended Methodology

If you are dealing with an RBI solution on your next engagement and cannot test your C2 channels beforehand, you are likely better off trying to go around first. Although DNS C2 callbacks are not the best for constant interaction, they can provide a great initial foothold that you can use to expand into an HTTP C2 channel slowly. Once you establish a DNS C2 foothold, work into a GET-only HTTP C2 channel. It will be your second-best chance of getting out and with the DNS backup, you will be able to troubleshoot what is going wrong. Lastly, you should try to move to a _GET-POST_ HTTP C2 channel if the RBI will let them through.

### Why Do We Still Recommend RBI?

Like every other security product vendor today, RBI vendors will pitch their products as a solution that will cure all your security woes and their product is infallible. We, like many of you, make our living proving that every product is fallible in some way. This does not mean we do not support companies developing RBI solutions. These products were a significant thorn in our side whenever we first encountered them during red team engagements. They do an excellent job allowing enterprises to fine-tune the sites, resources, and applications their users engage with on the web. We are actually quite big fans of RBI and hope that by releasing works like this focusing on the technology more entities will adopt it as they become aware of the benefits and the producers of these proxies can further refine their products. While they are not a one-stop solution for protecting your network, they are a significant advancement in preventative and detective tooling, and we highly recommend adding them to defense-in-depth solutions and testing recommendations.

#### About Us

Lance Cain is an Adversary Simulation Senior Consultant with SpecterOps. Lance has over seven years of experience in information technology with five of those specializing in Red Teaming and Penetration Testing. Lance formerly served as the Engineering Cell Lead of the Marine Corps’ Red Team specializing in payload and C2 channel development.

Alexander DeMine is an Adversary Simulation Consultant at SpecterOps with over 10 years of experience in the field of information technology. Formerly, Alex was the Chief of the Marine Corps’ Red Team, where he supervised and provided full-scope operational assessments of Marine Corps and DoD networks.

We began our journey into RBI while serving on the Marine Corps’ Red Team and have continued this research while working in a variety of different client environments during consultation work with SpecterOps. RBI has been a unique hurdle to overcome each time we have encountered it when working to establish C2 channels on offensive engagements. We hope that by sharing our tradecraft we are able to help shed some light for other teams out there that may be encountering the same challenges.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=50633a233999)

* * *

[Calling Home, Get Your Callbacks Through RBI](https://posts.specterops.io/calling-home-get-your-callbacks-through-rbi-50633a233999) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 7,035

[ Lance B. Cain ](https://specterops.io/blog/author/lance-b-cain/)

Security Engineer 

Lance Cain is an offensive security engineer at SpecterOps responsible for researching and integrating adversary tradecraft and techniques to SpecterOps services. He specializes in macOS threat research and is the creator of both JamfHound and Eve.

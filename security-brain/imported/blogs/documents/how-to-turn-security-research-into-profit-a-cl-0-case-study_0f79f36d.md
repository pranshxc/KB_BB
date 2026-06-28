---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-08_how-to-turn-security-research-into-profit-a-cl0-case-study.md
original_filename: 2022-09-08_how-to-turn-security-research-into-profit-a-cl0-case-study.md
title: 'How to turn security research into profit: a CL.0 case study'
category: documents
detected_topics:
- ssrf
- xss
- csrf
- sso
- sqli
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- csrf
- sso
- sqli
- command-injection
language: en
raw_sha256: 0f79f36de93ecbeebf8c600f7da97deff7d69d4babaf806dfac7926325627422
text_sha256: bcadeb5a63919c82974897b46a2a7130605112fd0ad9ef85be8cb84a5b694512
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How to turn security research into profit: a CL.0 case study

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-08_how-to-turn-security-research-into-profit-a-cl0-case-study.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sso, sqli, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `0f79f36de93ecbeebf8c600f7da97deff7d69d4babaf806dfac7926325627422`
- Text SHA256: `bcadeb5a63919c82974897b46a2a7130605112fd0ad9ef85be8cb84a5b694512`


## Content

---
title: "How to turn security research into profit: a CL.0 case study"
page_title: "How to turn security research into profit: a CL.0 case study | PortSwigger Research"
url: "https://portswigger.net/research/how-to-turn-security-research-into-profit"
final_url: "https://portswigger.net/research/how-to-turn-security-research-into-profit"
authors: ["James Kettle (@albinowax)"]
bugs: ["HTTP request smuggling", "Desync attack"]
publication_date: "2022-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2207
---

[](/)

[Login](/users)

Products Solutions [Research](/research) [Academy](/web-security) Support Company

[Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[My account](/users/youraccount) [Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[ ![Burp Suite DAST](/content/images/svg/icons/enterprise.svg) **Burp Suite DAST** The enterprise-enabled dynamic web vulnerability scanner. ](/burp/enterprise) [ ![Burp Suite Professional](/content/images/svg/icons/professional.svg) **Burp Suite Professional** The world's #1 web penetration testing toolkit. ](/burp/pro) [ ![Burp Suite Community Edition](/content/images/svg/icons/community.svg) **Burp Suite Community Edition** The best manual tools to start web security testing. ](/burp/communitydownload) [View all product editions](/burp)

[ **Burp Scanner** Burp Suite's web vulnerability scanner ![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg) ](/burp/vulnerability-scanner)

[ **Attack surface visibility** Improve security posture, prioritize manual testing, free up time. ](/solutions/attack-surface-visibility) [ **CI-driven scanning** More proactive security - find and fix vulnerabilities earlier. ](/solutions/ci-driven-scanning) [ **Application security testing** See how our software enables the world to secure the web. ](/solutions) [ **DevSecOps** Catch critical bugs; ship more secure software, more quickly. ](/solutions/devsecops) [ **Penetration testing** Accelerate penetration testing - find more bugs, more quickly. ](/solutions/penetration-testing) [ **Automated scanning** Scale dynamic scanning. Reduce risk. Save time/money. ](/solutions/automated-security-testing) [ **Bug bounty hunting** Level up your hacking and earn more bug bounties. ](/solutions/bug-bounty-hunting) [ **Compliance** Enhance security monitoring to comply with confidence. ](/solutions/compliance)

[View all solutions](/solutions)

[ **Product comparison** What's the difference between Pro and DAST? ![Burp Suite Professional vs Burp Suite DAST](/mega-nav/images/burp-suite.jpg) ](/burp/dast/resources/dast-vs-professional)

[ **Support Center** Get help and advice from our experts on all things Burp. ](/support) [ **Documentation** Tutorials and guides for Burp Suite. ](/burp/documentation) [ **Get Started - Professional** Get started with Burp Suite Professional. ](/burp/documentation/desktop/getting-started) [ **Get Started - DAST** Get started with Burp Suite DAST. ](/burp/documentation/dast/getting-started) [ **Downloads** Download the latest version of Burp Suite. ](/burp/releases)

[Visit the Support Center](/support)

[ **Downloads** Download the latest version of Burp Suite. ![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg) ](/burp/releases)

Articles

  * [Overview](/research)
  * Core Topics

[Black Hat](/research/black-hat) [XSS](/research/cross-site-scripting-research) [Request Smuggling](/research/request-smuggling) [Template Injection](/research/template-injection) [Top 10 Hacking Techniques](/research/top-10-web-hacking-techniques)

  * [Articles](/research/articles)
  * Meet the Researchers

[James Kettle](/research/james-kettle) [Gareth Heyes](/research/gareth-heyes) [Zakhar Fedotkin](/research/zakhar-fedotkin)

  * [Talks](/research/talks)
  * [ RSS  ](/research/rss)

# How to turn security research into profit: a CL.0 case study

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-turn-security-research-into-profit&text=How+to+turn+security+research+into+profit%3A+a+CL.0+case+study%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-turn-security-research-into-profit)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-turn-security-research-into-profit)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-turn-security-research-into-profit)
  * [ ](mailto:?subject=How+to+turn+security+research+into+profit%3A+a+CL.0+case+study&body=How+to+turn+security+research+into+profit%3A+a+CL.0+case+study%0A%0AHave+you+ever+seen+a+promising+hacking+technique%2C+only+to+try+it+out+and+struggle+to+find+any+vulnerable+systems+or+non-duplicate+findings%3F+In+this+post%2C+I%27ll+take+a+concise+look+at+the+most+effective%0A%0Ahttps://portswigger.net/research/how-to-turn-security-research-into-profit)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Tuesday, 6 September 2022 at 12:55 UTC

  * **Updated:** Tuesday, 6 September 2022 at 12:55 UTC

  * 

![](/cms/images/3e/b5/e23b-article-research.png)

Have you ever seen a promising hacking technique, only to try it out and struggle to find any vulnerable systems or non-duplicate findings? In this post, I'll take a concise look at the most effective strategies for avoiding this problem. As a case study, I'll use the [CL.0 desync](https://portswigger.net/web-security/request-smuggling/browser/cl-0) attack class recently explored in [Browser-Powered Desync Attacks](https://portswigger.net/research/browser-powered-desync-attacks).

### Analysing the technique

If you're looking for bounty success, it's important to understand the competition. Who else is looking for this bug class, and with what tools and techniques? Good research gets a wildly varying amount of attention from the security community, largely based on how valuable it appears at first glance. This creates an interesting tension - the less valuable research appears, the less competition you'll have turning it into bounties. In effect, there's a scale:

![](/cms/images/c6/27/d475-article-scales2.png)

If research is poorly explained or under-hyped, you can sometimes have major success simply by applying it. For example, [CORS Misconfigurations](https://ejj.io/misconfigured-cors/) missed the infosec hype train, so upon reading it I tried the technique as-is and immediately found a bunch of vulnerabilities with very little effort, leading to deeper research and ultimately [Exploiting CORS Misconfigurations for Bitcoins and Bounties](https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties).  

Conversely, if research is presented at a major conference and looks exciting, chances are you'll be competing against other bug bounty hunters using the same technique and tools. For example, people are [already](https://twitter.com/roughwire/status/1558509016288231424) sharing [successful](https://twitter.com/c3l3si4n/status/1558284246749519872) findings based on the techniques from Browser-Powered Desync Attacks.

Immediately after a presentation is published there's likely to be many vulnerable systems, and you can beat other hackers to reporting them simply by being faster, understanding the technique better, doing more recon, or being more persistent. Over a few weeks and months, this will become tougher and less effective. At this point, you'll need to innovate.

### Identifying the opportunity

Identifying opportunities to build on someone else's research is a bit of an art form. Start by getting really familiar with the research, and then ask yourself some questions:

  * Did the researcher miss anything?
  * Did they release a scanning tool? If not, can I make one?
  * If they did release a scanner, does it detect every vulnerability mentioned in the paper?
  * Can I see any blind spots in their scanner's design or code?

Try taking a look through [Browser-Powered Desync Attacks](https://portswigger.net/research/browser-powered-desync-attacks) and asking these questions.

One of the techniques I shared is [server-side CL.0 desync attacks](https://portswigger.net/web-security/request-smuggling/browser/cl-0). It's only touched on briefly, and the corresponding scan check in HTTP Request Smuggler is quite simple. Notably, it [references a presentation](https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf) which mentions CL.0 style vulnerabilities two years prior! It seems like because no tool was released to test for these, it was overlooked by the community. I under-estimated this desync class myself until I stumbled on one in the wild a year ago. Note that the older publication mentions several obfuscation techniques to make a CL.0 desync happen, but these aren't implemented in [HTTP Request Smuggler](https://github.com/PortSwigger/http-request-smuggler). This looks like an opportunity.

### Going hunting

A few hours of coding later, I'd added most of the obfuscation techniques from this paper, plus some more I made up and all the classic ones usually used to hide the Transfer-Encoding header. I set this running on my 20gb Burp Suite project file of bug bounty sites, and checked back in a few hours later to find around a hundred vulnerable websites, covering roughly 15 different bug bounty programs.

So, which permutations performed the best? The following reliable old-school techniques worked:

`Content-Length x: 7  
Content-Length : 7  
Foo: bar  
Content-Length: 48  
`

Plus these new content-length specific techniques:

`Content-Length: +7  
Content-Length: 0, 7  
Content-Length: 7.0`

And the following techniques flopped:

`Content-Length: -7  
Content-Length: 007  
Content-Length: 7e0`

I've just pushed this update out so everyone can make use of it. Also, now I've got the obfuscation system hooked into the CL.0 scancheck, adding most new techniques is trivial. Just [add the permutation code](https://github.com/PortSwigger/http-request-smuggler/blob/a05163d42989c07ff24bcd9e81e6e2d3c70ec966/src/burp/DesyncBox.java#L388-L390):

`case "CL-commaprefix":  
transformed = Utilities.replace(req, "Content-Length: ", "Content-Length: 0, ");  
break;`

and [register it](https://github.com/PortSwigger/http-request-smuggler/blob/a05163d42989c07ff24bcd9e81e6e2d3c70ec966/src/burp/DesyncBox.java#L106):

`clPermutations.register("CL-commaprefix", true);`

I regard adding new permutations as the easiest way to find fresh desync vulnerabilities that everyone else is missing, and ultimately earn bounties. Even if you struggle to invent your own novel permutation techniques, you can find quite a few documented but unimplemented in assorted academic papers on the topic.

### Summary

If you've found an overlooked piece of research, you might be able to turn it into profit simply by applying it. For mass success with more popular techniques, you'll probably need to bring something new to the table, but this can be as easy as a good idea and a few lines of code. 

If you're interested in a broader look into the art of finding vulnerabilities others miss, you might enjoy watching [Hunting Evasive Vulnerabilities](https://portswigger.net/research/hunting-evasive-vulnerabilities), and reading [So you want to be a web security researcher?](https://portswigger.net/research/so-you-want-to-be-a-web-security-researcher)

Good luck, and have fun!

[ Request Smuggling ](/research/request-smuggling)

[Back to all articles](/research/articles)

## Related Research

### [ How to distinguish HTTP pipelining from request smuggling 19 August 2025 How to distinguish HTTP pipelining from request smuggling ](/research/how-to-distinguish-http-pipelining-from-request-smuggling) ### [ 06 August 2025 ](/research/http1-must-die) ### [ Making desync attacks easy with TRACE 19 March 2024 Making desync attacks easy with TRACE ](/research/trace-desync-attack) ### [ Making HTTP header injection critical via response queue poisoning 22 September 2022 Making HTTP header injection critical via response queue poisoning ](/research/making-http-header-injection-critical-via-response-queue-poisoning)

Burp Suite

[Web vulnerability scanner](/burp/vulnerability-scanner) [Burp Suite Editions](/burp) [Release Notes](/burp/releases)

Vulnerabilities

[Cross-site scripting (XSS)](/web-security/cross-site-scripting) [SQL injection](/web-security/sql-injection) [Cross-site request forgery](/web-security/csrf) [XML external entity injection](/web-security/xxe) [Directory traversal](/web-security/file-path-traversal) [Server-side request forgery](/web-security/ssrf)

Customers

[Organizations](/organizations) [Testers](/testers) [Developers](/developers)

Company

[About](/about) [Careers](/careers) [Contact](/about/contact) [Legal](/legal) [Privacy Notice](/privacy) [Modern Slavery Statement](/modern-slavery-statement)

Insights

[Web Security Academy](/web-security) [Blog](/blog) [Research](/research) [Engineering](/engineering)

[![PortSwigger Logo](/content/images/logos/portswigger-logo.svg)](/) [ Follow us](https://twitter.com/Burp_Suite)

© 2026 PortSwigger Ltd.

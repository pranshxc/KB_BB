---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-07_how-i-was-able-to-list-some-internal-information-from-paypal-bugbounty.md
original_filename: 2018-06-07_how-i-was-able-to-list-some-internal-information-from-paypal-bugbounty.md
title: 'How I was able to list some internal information from PayPal #BugBounty'
category: documents
detected_topics:
- command-injection
- sso
- ssrf
- xss
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- sso
- ssrf
- xss
- information-disclosure
- api-security
language: en
raw_sha256: a6052065bb857a901c1e42126b26610c38437dd54607a453b67f3e2b0a8a2252
text_sha256: 13ee68bbc12d36b521590810b76ea5a5f7af5e29814cdf8ab5ac9bcd3001007e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to list some internal information from PayPal #BugBounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-07_how-i-was-able-to-list-some-internal-information-from-paypal-bugbounty.md
- Source Type: markdown
- Detected Topics: command-injection, sso, ssrf, xss, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `a6052065bb857a901c1e42126b26610c38437dd54607a453b67f3e2b0a8a2252`
- Text SHA256: `13ee68bbc12d36b521590810b76ea5a5f7af5e29814cdf8ab5ac9bcd3001007e`


## Content

---
title: "How I was able to list some internal information from PayPal #BugBounty"
url: "https://medium.com/@adrien_jeanneau/how-i-was-able-to-list-some-internal-information-from-paypal-bugbounty-ca8d217a397c"
authors: ["Adrien Jeanneau (@adrien_jeanneau)"]
programs: ["Paypal"]
bugs: ["Expression Language Injection (JSTL)", "Information disclosure"]
publication_date: "2018-06-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5849
scraped_via: "browseros"
---

# How I was able to list some internal information from PayPal #BugBounty

How I was able to list some internal information from PayPal #BugBounty
Adrien
Follow
5 min read
·
Jun 7, 2018

670

8

TL;DR : A page on domain manager.paypal.com was vulnerable to “Expression Language Injection” (JSTL) and I was able to extract some internal information like internal IP, internal port, internal class and more.

Before continuing, I would say that it’s a fair article to share my discovery and my way of proceeding… I’m not an expert and there will probably be some elements that you would miss.

S
ince september 2017, I started doing Bug Bounty on a regular basis (every night). Until now (and still today) I use the bountyfactory.io platform for hunter.

And then, in February, I set myself a challenge: Find a vulnerability on PayPal.

The scope of PayPal Bug Bounty is quite wide (*.paypal.com), so I started to do the usual recognition: List subdomains, list files, directories... (don’t forget to check my other article about recon)

Security Researchers for PayPal's Bug Bounty Program - PayPal
Use the information on this page to review the Terms and Conditions for PayPal's Bug Bounty Program

www.paypal.com

Then, after some days, I finally discovered an interesting page

Press enter or click to view image in full size

My reaction :

Ok, we have several fields, no button to submit, the page seems “old” (compared to the design) so we will try to do something with all that!

My WappAlyzer plugin (which I recommend for hunting) was clearly not talkative … No version, no info… except “Apache”

Press enter or click to view image in full size
Wappalyzer result

Well, I started to study the source code to see if certain elements could be interesting. I noted the names of the fields I put all the parameters GET and I sent the query :

Press enter or click to view image in full size
My first idea: Try a relfected XSS:

SPOILER: I ended up dropping the idea.

And yes… PayPal has a relatively efficient WAF, and I have not managed to find a bypass. It was certainly possible… but I lack skills!

Second idea: Try to inject data

Because relfected XSS was unsuccessfull, I decided to try inject differents PayLoad that I have already seen on other Bug Bounty.

{7*7}
{{7*7}}
${7*7}

And this last PayLoad was a success and worked.

Press enter or click to view image in full size
Injection payloads

Ok, I can do some mathemathique operation on a server. It’s fun but it’s not a vulnerability.

I decided to find information about Java and how work “${param}”.

“JSTL, JSTL everywhere”

After some research and a good help from Nico (kudos to you for your help !) I discovered that it was a JSTL and with some interesting syntax like:

Implicit Objects | The JSTL Expression Language | InformIT
Examine the JSTL expression language in detail, starting with expressions and identifiers, and ending with sections on…

www.informit.com

The interesting part in this article is about JSP Page and Servlet Properties:

Now that we’ve seen how to access request parameters and headers, initialization parameters, cookies, and scoped variables, the JSTL implicit objects have one more feature to explore: accessing servlet and JSP properties, such as a request’s protocol or server port, or the major and minor versions of the servlet API your container supports. You can find out that information and much more with the pageContext implicit object, which gives you access to the request, response, session, and application (also known as the servlet context).

We have many useful properties for the pageContext implicit object which are listed:

pageContext.request
pageContext.response
pageContext.properties
pageContext.page
pageContext.servletConfig
pageContext.servletContext

I will not detail all existing Implicit Object, but they are used when developper want to interact with the page, servlet and server.

Get Adrien’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, I started to find all param which it could be useful. Documentation + fuzzing. And I injected them into the Intruder functionnality on our favorite tool…. Burp Suite.

Press enter or click to view image in full size
Payloads for JSTL injection on Burp Suite

Nice ! It was possible to extract internal information from PayPal like a SSRF (with some limited possibility).

I’m sorry for this useless screenshot … It’s just to show that I had results, but I’m not allowed to post them)

Press enter or click to view image in full size
Results in Burp Suite Intruder tool

With fuzzing I found a parameter which I don’t find in documentation :

${pageContext.servletContext.docRoot}

This Implict Object display the relative path where the compiled WAR file is hosted on server.

Remote Code Execution ?

After this discovery I tried to use this Expression Language Injection for a Remote Code Execution vulnerability.

Spoiler: It was not successfull

I’ve read many and many writeups and PoC about JSTL injection and RCE, but I never succeeded.

I suppose it was because PayPal use a WAF, and during my attempts, the WAF seems to block injection and I had 301 redirect

I tried some basic payload to test:

${T(java.lang.System).getenv()}

No one worked for me. The response returned from the server was always stopped where I inject my payload.

Second possibility: I don’t have the skills and RCE was possible but I just don’t find how to doing that.

So, I finally submited the vulnerability to PayPal and crossed my fingers!

Thank for reading this article, and thanks to all hunters who share always their writeup and tips about Bug Bounty and don’t forget to follow me on Twitter.

And a special thank to Nico ❤

Timeline :

[06-03-2018] Find the vulnerability
[07–03-2018] Report sended to PayPal
[08–03-2018] First response from PayPal : No security risk, not eligible for reward (WTF ?)
[29–03-2018] Second response from PayPal : Report is valid
[03-04-2018] Vulnerability fixed
[11–04-2018] Nice reward (+ Hall of Fame in June 2018)

Ressources that helped me:

https://portswigger.net/kb/issues/00100f20_expression-language-injection
https://magicbluech.github.io/2017/12/02/VelocityServlet-Expression-language-Injection
http://blog.mindedsecurity.com/2015/11/reliable-os-shell-with-el-expression.html

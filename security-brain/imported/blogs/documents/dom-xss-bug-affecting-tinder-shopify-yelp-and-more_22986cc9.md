---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-09_dom-xss-bug-affecting-tinder-shopify-yelp-and-more.md
original_filename: 2018-10-09_dom-xss-bug-affecting-tinder-shopify-yelp-and-more.md
title: DOM-XSS Bug Affecting Tinder, Shopify, Yelp, and More
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 22986cc9008cfa15d93ba3e5edd53d7eac4c3632d97e3a02fe087a9fefb50eb0
text_sha256: e81b786366aa3506ed05e5535b19be3df5057dec5fce701cb0a73dfce0a3af57
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# DOM-XSS Bug Affecting Tinder, Shopify, Yelp, and More

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-09_dom-xss-bug-affecting-tinder-shopify-yelp-and-more.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `22986cc9008cfa15d93ba3e5edd53d7eac4c3632d97e3a02fe087a9fefb50eb0`
- Text SHA256: `e81b786366aa3506ed05e5535b19be3df5057dec5fce701cb0a73dfce0a3af57`


## Content

---
title: "DOM-XSS Bug Affecting Tinder, Shopify, Yelp, and More"
url: "https://www.vpnmentor.com/blog/dom-xss-bug-affecting-tinder-shopify-yelp/"
final_url: "https://www.vpnmentor.com/blog/research/dom-xss-bug-affecting-tinder-shopify-yelp/"
authors: ["VPN Mentor (@vpnmentor)"]
programs: ["Tinder"]
bugs: ["DOM XSS"]
publication_date: "2018-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5654
---

![DOM-XSS Bug Affecting Tinder, Shopify, Yelp, and More](https://www.vpnmentor.com/wp-content/uploads/2018/10/tinderbug-1-768x403.jpg)

# DOM-XSS Bug Affecting Tinder, Shopify, Yelp, and More

[ ![Author Image Kristina Perunicic](https://www.vpnmentor.com/wp-content/uploads/2020/08/Kristina-Perunicic-1-50x50.png) ](https://www.vpnmentor.com/author/kristina-perunicic/)

[ Kristina Perunicic ](https://www.vpnmentor.com/author/kristina-perunicic/) Updated on July 18, 2023 Cybersecurity Specialist

Table of Contents 

  * Details: 
  * So, how did this bug affect more than Tinder? 

Our team of security researchers was researching dating apps client-side security, and one of the main focus targets was Tinder.

After initial reconnaissance steps were done, a Tinder domain with multiple client-side security issues was found - meaning **hackers could have access to users' profiles and details.**

Immediately after finding these vulnerabilities, we contacted Tinder via their responsible disclosure program and started working with them.

We learned that the vulnerable endpoint isn’t owned by Tinder, but by branch.io, an attribution platform used by many big corporations around the globe. The Tinder security team helped us get in touch with them, and accordingly, they’ve put out a timely patch.

Upon further investigation, it was discovered that numerous prominent websites, such as **Shopify, Yelp, Western Union, and Imgur, were inadvertently exposing the vulnerable endpoint in their code and domains. Consequently, there is a potential risk for up to 685 million users.**

**While the flaw has already been fixed, if you have recently used Tinder or any of the other affected sites, we recommend checking to make sure your account hasn't been compromised. It's a good idea to change your password ASAP.**

## Details:

DOM-based XSS vulnerability, also known as “type-0 XSS” is a class of cross-site scripting vulnerability that appears within the DOM. It is a type of attack wherein the attack payload is executed as a result of modifying the DOM environment in the victim’s browser, more so in a dynamic environment. In DOM-based XSS, the HTML source code and response of the attack will be exactly the same. This means the malicious payload cannot be found in the response, making it extremely difficult for browser-built in XSS mitigation features like Chrome’s XSS Auditor to perform.

Can you spot the vulnerabilities?

![HTML code](/wp-content/uploads/2018/10/code.png)

The fact that the vulnerability is DPM based and branch.io still isn't using CSP made these vulnerabilities easy to exploit in any browser we like.

This meant that by modifying redirect strategy to a specially crafted payload to manipulate the DOM.

### **1\. DOM XSS**

For example, our initial finding was the endpoint https://go.tinder.com/amp-iframe-redirect was prone to multiple vulnerabilities (scheme_redirect & redirect_strategy GET parameters control the div content).

redirect_strategy is “INJECTIONA” and scheme_redirect is “INJECTIONB” from the code above.

This meant that by modifying redirect_strategy to a dom-xss payload, it was possible to execute client-side code in the context of a Tinder domain in any browser:  
https://go.tinder.com/amp-iframe-redirect?scheme_redirect=http://google.com&redirect_strategy=1)%7B%0Aalert(1)%3B//  
will render in the DOM as:

**if** (1){ alert(1);_// && "INJECTIONA") {_

**var** parser **=** document.createElement('a');

parser.href **=** "INJECTIONA";

**var** protocol **=** parser.protocol.toLowerCase();

![Bug screenshot](/wp-content/uploads/2018/10/screenshot.png)

### **2\. validateProtocol() and validate() Bypass**

Also notice how validateProtocol() uses indexOf to check the schemes - the indexOf() method returns the position of the first occurrence of a specified value in a string. This method returns -1 if the value to search for never occurs. However, it can be tricked by using javascript://%0aalert(0)//good.com/https:// -- both the validate functions can be bypassed because indexOf will find “https://“

**var** parser **=** document.createElement('a');

parser.href **=** url;

**var** protocol **=** parser.protocol.toLowerCase();

if ((‘javascript:', 'vbscript:', ‘data:').indexOf(protocol) **<** 0) {**return** url;

}

....

**return null;**

**if** (['http:', 'https:'].indexOf(protocol) < 0) {

window.top.location = validate("http://google.com");

}

## So, how did this bug affect more than Tinder?

go.tinder.com is an alias for custom.bnc.lt, a Branch.io resource. And many other companies have their alias pointing to it.

To name a few websites affected by this vulnerability: RobinHood, Shopify, Canva, Yelp, Western Union, Letgo, Cuvva, imgur, Lookout, fair.com and more.

Thanks to the fast response we got from Branch’s security team, this vulnerability has now been fixed for everyone’s domains.

**Other recent studies of ours:**

[Critical RCE Vulnerability Found in Over a Million GPON Home Routers](https://www.vpnmentor.com/blog/cybersecurity/critical-vulnerability-gpon-router/)

We review vendors based on rigorous testing and research but also take into account your feedback and our affiliate commission with providers. Some providers are owned by our parent company. 

Learn more

vpnMentor was established in 2014 to review VPN services and cover privacy-related stories. Today, our team of cybersecurity researchers, writers, and editors continues to help readers maintain their online freedom in partnership with Kape Technologies PLC, which also owns the following products: Holiday.com, ExpressVPN, CyberGhost, and Private Internet Access which may be ranked and reviewed on this website. The reviews published on vpnMentor are believed to be accurate as of the date of each article, and written according to our strict reviewing standards that prioritize professional and detailed examination by the reviewer, taking into account the technical capabilities and qualities of the product together with its commercial value for users. The rankings and reviews we publish may also take into consideration the common ownership mentioned above, and affiliate commissions we earn for purchases through links on our website. We do not review all VPN providers and information is believed to be accurate as of the date of each article.

Was this helpful? Share it!

  * Share on Facebook __ 4
  * Tweet this __ 6

#### About the Author

  * ![Author Image Kristina Perunicic](https://www.vpnmentor.com/wp-content/uploads/2020/08/Kristina-Perunicic-1-50x50.png)
  * [Kristina Perunicic](https://www.vpnmentor.com/author/kristina-perunicic/) Cybersecurity Specialist

Kristina Perunicic is the chief editor at vpnMentor and a cybersecurity expert specializing in VPNs and digital privacy, with a focus on making complex security topics clear and accessible for everyday users.

Follow our experts:

  * [ __](https://www.linkedin.com/company/vpnmentor/)
  * [ __](https://twitter.com/vpnmentor)
  * [ __](https://www.facebook.com/vpnmentor/)

Did you like this article? Rate it! 

  * ____
  * ____
  * ____
  * ____
  * ____

I hated it! I don't really like it It was ok Pretty good! Loved it! 

out of 10 - Voted by  users 

__Thank you for your feedback

__

Please, comment on how to improve this article. Your feedback matters!

__

![](/wp-content/themes/assets/img/post-popup/post-popup.svg)

####  Thanks for submitting a comment, %%name%%! 

We check all comments within 48 hours to ensure they're real and not offensive. Feel free to share this article in the meantime.

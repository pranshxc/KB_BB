---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-07_bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript.md
original_filename: 2018-09-07_bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript.md
title: Bypassing Hotstar Premium with DOM manipulation and some JavaScript
category: documents
detected_topics:
- otp
- access-control
- xss
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- otp
- access-control
- xss
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 01465d2ae6c6de4e0a7d3f8b747a382bc65c069d0927b9ae7220476a145dda5a
text_sha256: 69c2844d4e6760e40c915d3c2f4ee25192d3e572058a004e7842721059e1d830
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Hotstar Premium with DOM manipulation and some JavaScript

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-07_bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript.md
- Source Type: markdown
- Detected Topics: otp, access-control, xss, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `01465d2ae6c6de4e0a7d3f8b747a382bc65c069d0927b9ae7220476a145dda5a`
- Text SHA256: `69c2844d4e6760e40c915d3c2f4ee25192d3e572058a004e7842721059e1d830`


## Content

---
title: "Bypassing Hotstar Premium with DOM manipulation and some JavaScript"
page_title: "Bypassing Hotstar Premium with DOM manipulation and some JavaScript | OpSecX"
url: "https://opsecx.com/index.php/2018/09/07/bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript/"
final_url: "https://opsecx.com/index.php/2018/09/07/bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript/"
authors: ["OpSecX (@OpSecX)"]
programs: ["Hotstar"]
bugs: ["Logic flaw", "Payment bypass"]
publication_date: "2018-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5717
---

# Bypassing Hotstar Premium with DOM manipulation and some JavaScript

  * [September 7, 2018](https://opsecx.com/index.php/2018/09/07/bypassing-hotstar-premium-with-dom-manipulation-and-some-javascript/ "Bypassing Hotstar Premium with DOM manipulation and some JavaScript")
  * [Blog](https://opsecx.com/index.php/category/blog/)

### **tl;dr**

Hotstar is a premium streaming platform like Netflix and Amazon Prime Videos. The security controls for restricting premium content were implemented at client side as frontend React JS logic. We were able to bypass these access controls and view paid premium content by manipulating the dynamic HTML DOM.

### **Busting Security logic at Frontend**

The past experience in AppSec has taught us not to put security controls only at frontend or client side. The legacy examples are input validation only at client side, client side only captcha validation, hidden fields with sensitive tokens, OTP token exposed to client side etc. The main purpose of frontend is for presentation, but with the advent of JS Frameworks and MVC terminology at frontend, some developers tend to do a lot more things at client side controllers than they should actually do.

Hotstar heavily uses ReactJS at frontend and they had controls on accessing premium content only at client side. From an application security perspective, it’s a nightmare to find such issues by inspecting and debugging JavaScript code. We initially hooked various JavaScript function calls to trace the execution flows and later discovered this issue by fiddling with the HTML DOM.

### **Understanding the Issue**

When you try to access a premium content in Hotstar as an anonymous user, you will be greeted with the following overlay on top of the video player.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202554%201340'%3E%3C/svg%3E)](https://opsecx.com/wp-content/uploads/2018/09/1.png)By looking at the JavaScript execution flow during the page load, we found that the overlay was added by JavaScript. We were curious to know, what happens if we delete the overlay.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202554%201340'%3E%3C/svg%3E)](https://opsecx.com/wp-content/uploads/2018/09/2.png)We deleted the element `slate-wrapper blackBg` in DOM corresponding to the overlay. Now that the black overlay is removed, we were expecting a video player in the background, but this gave us a grey screen as shown below.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202558%201344'%3E%3C/svg%3E)](https://opsecx.com/wp-content/uploads/2018/09/3.png)  
After going through the HTML DOM, we found out an interesting div class named `player-base hide`. With our previous experience in pentesting ReactJS web apps, we quickly edited the HTML to modify the class from `hide` to `show`

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201600'%3E%3C/svg%3E)](https://opsecx.com/wp-content/uploads/2018/09/5.png)  
and voila, we have the player controls visible now. From this point we were sure that they have the video player loaded for every premium content and it’s just covered up by some ReactJS element hide logic. But soon we found another problem. When you click the play button, it plays for a second and then pause the video. We assumed that this might be another ReactJS logic to prevent the content from streaming. Without debugging much, we did a quick JavaScript hack to fix this.

We found out the class corresponding to play button in DOM and wrote some JavaScript code to click the div and put that inside an infinite loop.
  
  
  while(1){
  document.querySelector('.vjs-play-control-play').click();
  }
  

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202548%201348'%3E%3C/svg%3E)](https://opsecx.com/wp-content/uploads/2018/09/6.png)  
And that was it!

### **Video: Bypassing Hotstar Premium**

### **Learn how to pentest JavaScript MVC Frameworks**

We have a dedicated courseware at OpSecX, [**XSSing JavaScript-MVC Applications -XJA**](https://opsecx.com/index.php/product/xssing-javascript-mvc-applications-xja/)that covers some of the modern JavaScript MVC frameworks. This course teaches you to find vulnerabilities in applications developed by improper usage of these otherwise perfect frameworks. This is a deep dive course where students will be walked through the basic architecture of these frameworks and their inbuilt protection mechanisms. Knowledge of building userscripts for dynamic hooking of different templating engines to fuzz for XSS vulnerabilities is practiced over real world applications.

### **Disclosure Timeline**

Hotstar didn’t had a dedicated security team or contact. After much trying, we had to contact them through their regular customer support.  
06-07-2018 – Reported to Hotstar  
06-07-2018 – Acknowledged by customer support  
31-08-2018 – Issue was fixed, no response from Hotstar  
07-09-2018 – Published the findings

[hotstar premium bypass](https://opsecx.com/index.php/tag/hotstar-premium-bypass/)[pentesting js mvc](https://opsecx.com/index.php/tag/pentesting-js-mvc/)[reactjs security](https://opsecx.com/index.php/tag/reactjs-security/)

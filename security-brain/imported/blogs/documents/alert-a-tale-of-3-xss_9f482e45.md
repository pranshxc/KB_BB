---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-29_alerta-tale-of-3-xss.md
original_filename: 2019-03-29_alerta-tale-of-3-xss.md
title: alert(“A tale of 3 XSS!”)
category: documents
detected_topics:
- xss
- command-injection
- password-reset
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- command-injection
- password-reset
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 9f482e45687db076a6a6dc743dbfe49d029dda668710a4ecc399eb396e97dd7c
text_sha256: 70abaf9c0d69720b1b75840ad1403b149bb3b6fe54dab6ddeacd03c53c00899c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# alert(“A tale of 3 XSS!”)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-29_alerta-tale-of-3-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, password-reset, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9f482e45687db076a6a6dc743dbfe49d029dda668710a4ecc399eb396e97dd7c`
- Text SHA256: `70abaf9c0d69720b1b75840ad1403b149bb3b6fe54dab6ddeacd03c53c00899c`


## Content

---
title: "alert(“A tale of 3 XSS!”)"
page_title: "alert(“A tale of 3 XSS!”) | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/a-tale-of-3-xss/"
final_url: "https://gauravnarwani.com/a-tale-of-3-xss/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["XSS"]
publication_date: "2019-03-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5340
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss.png?fit=313%2C161&ssl=1) ](https://gauravnarwani.com/a-tale-of-3-xss/)

# alert(“A tale of 3 XSS!”)

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [March 29, 2019](https://gauravnarwani.com/a-tale-of-3-xss/)

Hello Guys, I recently encountered with 3 Interesting Reflective Cross Site Scripting in a program on Synack. Although these bugs weren’t difficult to find, each of these had a different approach and ways to find and exploit these issues. The case studies are discussed later after a short introduction about XSS and how to find it. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

### Cross-Site Scripting

Cross-Site Scripting (**XSS**) is the name of the most common vulnerability in Web Applications. The abuse of XSS not limits to hooking the victim’s browser but can go deep inside the server to execute commands remotely. To display back content provided or controlled by a user, like an URL parameter or an input field, a flawed application opens the door to manipulation of this content. This manipulation, generically called injection, is the XSS attack.

#### Types of XSS

Focusing on the application, XSS can be caused by server-side code or client-side code.  
Code sent by the web server is the **source code**. It is processed by the browser, with the help of the JavaScript engine, to create the elements of the document in a programmatic manner. This is called **DOM** and it’s generated as soon as the source code arrives.  
So, we have source-based and DOM-based types of XSS in the context of an application. Both have the following execution types.  
Source-based:

  1. Reflected
  2. Stored

DOM-based:

  1. Reflected
  2. Stored

#### Reflected XSS

When the website or application just reflects back content maliciously manipulated by the user (usually in the URL), we have a **reflected XSS** attack. This reflection, as we saw, affects the way browsers display the page and how they process things and behave. Take the following PHP code:

$username = $_GET[‘user’];  
echo “  
<h1>Hello,”. $username. “!</h1>  
”;

What if someone inserts a script tag in the input field, for ex: http://mydomain.com/hello.php?user=**< script>alert(1)</script>**

Would execute a JavaScript on the browser, hence an alert box like this:

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

### Case Study 1: Reflected XSS via the referrer header

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data Tier (Databases). As this was a private program all illustrations of vulnerabilities will be represented with the host as example.com.

The application has a login page where users can use the credentials provided to sign-in the application using provided credentials.

After visiting a few pages, there was a section which had to be tested with another user and thus the logout button was clicked to redirect to the login page. The URL after logout had an interesting parameter referrer with the value of the URL of the page from where logout was initiated. The URL looked like this:

https://www.example.com/SignUp?referrer=https://www.example.com/myAccount

The link provided in the referrer was the new link the application would redirect after the user would sign in to the application. This URL was vulnerable to URL redirection as any domain inserted in the referrer parameter was whitelisted but, Synack considers URL redirection as a Low Impact Vulnerability and these issues are generally Out of Scope.

A good way to convert URL redirection to XSS is to use a JavaScript resource such as javascript:alert(1);

This payload was passed in the referrer parameter in URL. After the user would sign in to the application, an alert box popped up with value 1. A final POC was sent to the program with the URL as:

https://www.example.com/SignUp?referrer= javascript:alert(document.domain);

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

Note that it is a good practice to use document.domain as this increases the value of the report since it shows access to the DOM.

### Case Study 2: Reflected XSS via changing account details.

The application had a ‘My details’ page where a user could change is Name, Address, Phone Number and various other things. There was a password protection on this page when a user wished to save a new value in these parameters. When a new value was entered while editing the Account Details, a prompt pops up where when the user enters the correct password, a POST request is sent to example.com/accDetails with the new values and an extra parameter named as passCheck. This parameter was a random hash value of the correct password entered in the prompt and on a valid check, it would redirect to the same page before.

A test had been made for XSS by entering values such as test”> on every parameter in the request. Every parameter had proper input validations as well as there were space constraints on each of them.

The first instance now was to check for CSRF without the passCheck parameter to modify details of the User. When the request was submitted without the parameter, the application threw an error stating ‘Password was missing, please re-submit’.

The thing which caught attention was that the values provided in the parameters (test”>) would now escape the text box and showed some extra part of code outside it. The page looked something like:

Name: |test | “size=”30”maxlength=”30”

A payload test”><script>alert(document.domain)</script> was passed to the name parameter and the request was submitted again and an alert box popped up. A CSRF POC was made for the request removing the passCheck parameter and after adding the payload to the name parameter the report was submitted to the program.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

### Case Study 3: Reflected XSS via the email parameter in URL

The application had an option to recover the account password in case any user would forget it. The application had a page called forgotPassword where the user would type his email and a password reset link would be sent to the user.

Whenever the email was entered in the application, the application sent a GET request to the server with the email in the URL in the parameter email.

The thing which turned this into a reflected XSS was that whenever a user enters an email in the text box and submitted, the application would give back a message saying ‘a mail has been sent to  xy*@xy*.com ’

The request of the URL was intercepted in burp:

/forgotPassword?email= xy*@xy*.com HTTP/1.1  
Host: example.com  
…  
…  
…

The value of email entered as  xy*@xy*.com ”>hello was submitted in the request. On checking the response, there was no filter on the value and the input tag which took the email id as input had now been closed.

A value  xy*@xy*.com ”><script>alert(document.domain)</script> was submitted in the parameter email and the XSS fired in browser.

The final URL submitted as a POC to the program was:

https://www.example.com/forgotPassword?email= xy*@xy*.com ”><script>alert(document.domain)</script>

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

That’s all for this Blog. Hope you liked it.

**#BugBountyTip:** Google the Copyright footer to get more company domains and discover more assets.

Credits to @_zulln for this tip and @brutelogic for an amazing write-up on XSS101. You can find the write-up [here](https://brutelogic.com.br/blog/xss101/).

That’s all for today. Please subscribe to my **[blog](https://gauravnarwani.com/blog/)**. Connect with me on [**LinkedIn**](https://linkedin.com/in/gauravnarwani97/).

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/a-tale-of-3-xss/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/a-tale-of-3-xss/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/a-tale-of-3-xss/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/a-tale-of-3-xss/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/a-tale-of-3-xss/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/a-tale-of-3-xss/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

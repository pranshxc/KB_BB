---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-17_stored-xss-leads-to-plaintext-password-disclosure.md
original_filename: 2020-05-17_stored-xss-leads-to-plaintext-password-disclosure.md
title: Stored XSS Leads to Plaintext Password Disclosure
category: documents
detected_topics:
- xss
- file-upload
- access-control
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- xss
- file-upload
- access-control
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: a1bc9af866677d69ddae6017543379d66b1ac9e70ae1b3261479722ec4276992
text_sha256: fc4ef430d6b720d8791317001df2610e7ce9a2383e0073f55e367d5d0b862c3d
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS Leads to Plaintext Password Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-17_stored-xss-leads-to-plaintext-password-disclosure.md
- Source Type: markdown
- Detected Topics: xss, file-upload, access-control, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a1bc9af866677d69ddae6017543379d66b1ac9e70ae1b3261479722ec4276992`
- Text SHA256: `fc4ef430d6b720d8791317001df2610e7ce9a2383e0073f55e367d5d0b862c3d`


## Content

---
title: "Stored XSS Leads to Plaintext Password Disclosure"
page_title: "Stored XSS Leads to Plaintext Password Disclosure :: bad5ect0r | Security Researcher"
url: "https://www.bad5ect0r.sh/posts/stored-xss-leads-to-plaintext-password-disclosure/"
final_url: "https://www.bad5ect0r.sh/posts/stored-xss-leads-to-plaintext-password-disclosure/"
authors: ["bad5ect0r (@bad5ect0r)"]
bugs: ["Stored XSS", "Information disclosure", "Unrestricted file upload"]
publication_date: "2020-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4582
---

# Introduction⌗

This post documents another vulnerability I found in the same company as the last post. I disclosed both vulnerabilities on the same day and was told that both vulnerabilities have been resolved. I was authorized to provide a partial disclosure, hence why I’m writing this post now.

# The Story⌗

So once I had logged into the mobile app, I had a look around and noticed a profile image upload feature:

![Can upload a profile picture. Please ignore the missing image icon.](/stored-xss-leads-to-plaintext-password-disclosure/image-upload-on-app.png)

I used Burp to intercept the request sent when uploading a profile image and saw something like this:

![PATCH request used to upload profile image. This was taken after exploiting the issue. Originally the ProfilePicture parameter contained base64 encoded image data and the ProfilePictureMIME parameter contained image/png.](/stored-xss-leads-to-plaintext-password-disclosure/patch-request-example.png)

Basically they are taking the image data, converting it to Base64 and then sending it via a standard JSON OData API request.

The most important thing you should notice is that there is a `ProfilePictureMIME` parameter. This essentially dictates the file type that is being uploaded.

I tried changing that to `text/x-php` and `application/php` but they were not allowed. Surprisingly, `text/html` was allowed. I then created a basic HTML file that pops an alert:
  
  
  <!DOCTYPE html>
  <html>
  <body>
  <h1>Test</h1>
  </body>
  <script>
  alert(1);
  </script>
  </html>
  

I converted this to Base64 and replaced the value of the `ProfilePicture` parameter in the request with my base64 encoded HTML file. I set the `ProfilePictureMIME` to `text/html` and sent the request. When I used my browser to check the raw file to my image, it actually rendered the HTML! Unfortunately I do not have screenshot of this.

So then I thought of a practical attack scenario. I realized that there was no authentication required to access the raw profile image files from their server. I then realized that the domain hosting these profile images was also the same domain as the one hosting their web application:

Link to image file: <https://something.redacted.com/res/img/usermeta//551/USER_7025dffcf32e4097bebe7b530f9f1a5d.png?ts=1584857339> Link to web application: <https://something.redacted.com/login/>

Using the credentials I found before, I logged into the web application and tried visiting the link to the HTML profile image I uploaded. I could access it.

So then I examined any cookies I could access using JavaScript. One of these was called `AUTHH`. It was base64 encoded, so i decoded it using CyberChef and realized that it was the same value as the Authorization header! Since they use HTTP Basic Authentication, the credentials are in plaintext!
  
  
  Cookie: AUTHH=QmFzaWMgWm1GclpUcG1ZV3RsY0dGemN3PT0=
  

I immediately uploaded the following HTML file:
  
  
  <html>
  <head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/js-cookie@rc/dist/js.cookie.min.js"></script>
  </head>
  <body>
  <h1>Password Display by bad5ect0r</h1>
  <p>Your username is: <span id="uname"></span></p>
  <p>Your password is: <span id="pass"></span></p>
  </body>
  <script>
  $(document).ready(function () {
  const AUTHH = Cookies.get('AUTHH');
  const unb64 = atob(AUTHH);
  const basic = unb64.split(' ');
  const uname_pass = atob(basic[1]).split(':');
  const user = uname_pass[0];
  const pass = uname_pass[1];
  $('#uname').html(user);
  $('#pass').html(pass);
  });
  </script>
  </html>
  

This basically displays the user’s username and password by decoding their AUTHH cookie. A real attacker would just forward this information to their server after getting a user to click on the link to their malicious profile image.

I reloaded the link while still authenticated to the web application, and it worked like a charm!

![Viewing that link would disclose your username and password.](/stored-xss-leads-to-plaintext-password-disclosure/password-display.png)

I immediately sent out another email to the company alerting them of this new vulnerability and while there was some initial confusion on the severity of this bug, they were able to prioritize getting it fixed.

I look forward to finding more bugs on this company’s platform and hope that one day they move to a rewards based system to encourage repeat hackers.

# Takeaway⌗

If you can’t upload a web shell, try the next best thing, an HTML file to get stored XSS.

# Disclosure Timeline⌗

Date | Details  
---|---  
21/03/2020 | Issue was reported to the company.  
25/03/2020 | Follow up.  
27/03/2020 | Acknowledged by the company.  
03/04/2020 | Issues were fixed.  
15/05/2020 | Partial disclosure was authorized.

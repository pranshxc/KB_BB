---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-11_otp-bypass-developers-check.md
original_filename: 2020-03-11_otp-bypass-developers-check.md
title: OTP Bypass - Developer’s Check
category: documents
detected_topics:
- command-injection
- mfa
- otp
tags:
- imported
- documents
- command-injection
- mfa
- otp
language: en
raw_sha256: 414253f5d6382624559ea3c82d0fe8b16b1ebe56c9457e4982758fb43426b990
text_sha256: 850670cffa0ec78a49574f91bb5a16eb0eba12e3cafa70e9c997748ad2cce0a7
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# OTP Bypass - Developer’s Check

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-11_otp-bypass-developers-check.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `414253f5d6382624559ea3c82d0fe8b16b1ebe56c9457e4982758fb43426b990`
- Text SHA256: `850670cffa0ec78a49574f91bb5a16eb0eba12e3cafa70e9c997748ad2cce0a7`


## Content

---
title: "OTP Bypass - Developer’s Check"
url: "https://medium.com/@shahjerry33/otp-bypass-developers-check-5786885d55c6"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["OTP bypass"]
publication_date: "2020-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4722
scraped_via: "browseros"
---

# OTP Bypass - Developer’s Check

Top highlight

OTP Bypass - Developer’s Check
Jerry Shah (Jerry)
Follow
3 min read
·
Mar 11, 2020

641

39

Summary :

OTP​ is a string of characters or numbers automatically generated to be used for one single login attempt. OTP, One Time Passwords in full, can be sent to the user’s phone via SMS or Push messaging and is used to protect web-based services, private credentials and data.

I was checking for some bypasses of an OTP and I tried this thing to bypass the OTP and was successful. I call it Developer’s Check because I found it when I was reviewing the code of the application and some of the buttons. The mistake here was that the application was having the OTP check on the client side and was easily identifiable. Due to this mistake anyone can bypass the OTP very easily.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How to find this vulnerability ?

Go to your target website
Press enter or click to view image in full size
Registration

2. Here I had an option to register and they will send me an OTP for login

Press enter or click to view image in full size
OTP received

3. Right-click on the “Continue” button and click on inspect element to check for some functions that validates the OTP check

Press enter or click to view image in full size
Inspect Element

4. Here you can see in the below screenshot that their is an event called “checkOTP(event)”

Press enter or click to view image in full size
checkOTP(event) function

5. Simply type the event in the console of the browser

Press enter or click to view image in full size
Click on the arrow

6. After clicking on the arrow it will open a file in the debugger where you will an OTP that was send to the mobile

Press enter or click to view image in full size
OTP

Logic Code :

<script type=’text/javascript’>
function checkOTP(e)
{
if (document.getElementById(“txtOtp”).value == 8951)
{
var formSignUp = document.getElementById(“formSignUp”);
formSignUp.submit();
}
else
{
var divWrongOTP = document.getElementById(‘divWrongOTP’);
divWrongOTP.style.display = ‘inline’;
e.preventDefault();
return;
}
}
function resubmitOtp()
{
location.reload();
}
</script>

As here you can see if “(document.getElementById(“txtOtp”).value == 8951)” which means if the OTP that you entered matches “8951” then only you will get a successful login which also means that “8951” is your OTP.

Thank You :)

Instagram : jerry._.3

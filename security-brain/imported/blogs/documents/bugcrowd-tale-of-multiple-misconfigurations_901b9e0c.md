---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-04_bugcrowd-tale-of-multiple-misconfigurations-.md
original_filename: 2022-10-04_bugcrowd-tale-of-multiple-misconfigurations-.md
title: Bugcrowd — Tale of multiple misconfigurations!! ❌
category: documents
detected_topics:
- password-reset
- oauth
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- password-reset
- oauth
- command-injection
- otp
- business-logic
language: en
raw_sha256: 901b9e0ca6d23c75b8ef864d4343509ca26d043e6f1d7b98a6def4b87a44a67b
text_sha256: f41c2327e071a8764117b5539d0dddc8e78df0e8a7b28933dc59459925e62b24
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Bugcrowd — Tale of multiple misconfigurations!! ❌

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-04_bugcrowd-tale-of-multiple-misconfigurations-.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `901b9e0ca6d23c75b8ef864d4343509ca26d043e6f1d7b98a6def4b87a44a67b`
- Text SHA256: `f41c2327e071a8764117b5539d0dddc8e78df0e8a7b28933dc59459925e62b24`


## Content

---
title: "Bugcrowd — Tale of multiple misconfigurations!! ❌"
url: "https://medium.com/@302Found/bugcrowd-tale-of-multiple-misconfigurations-cb5b98f09302"
authors: ["Vaibhav Lakhani", "Dhir Parmar"]
bugs: ["Account takeover", "OAuth", "OTP bypass", "Password reset"]
publication_date: "2022-10-04"
added_date: "2022-10-04"
source: "pentester.land/writeups.json"
original_index: 2088
scraped_via: "browseros"
---

# Bugcrowd — Tale of multiple misconfigurations!! ❌

Bugcrowd — Tale of multiple misconfigurations!! ❌
TheBountyBox
Follow
4 min read
·
Oct 4, 2022

218

2

W
elcome to this new article. This article is a story about misconfigurations found on a domain. Since it is a private program let’s call it redacted.com So do you wanna know how??

The scope of the application was huge, but starting off with the normal subdomain scan and all of those fancy recon I decided to start testing the main application. The web application was a simple E-commerce website with a lot of deals to grab on! ;)

I usually try to check all sorts of business logic vulnerabilities on such websites, but this time my eyes captured the authentication mechanism.

So the first thing was to create an account! But what came to my notice was the OAuth mechanism. Perfect it was time to check for various OAuth vulnerabilities!!

Email SignUp

So I used the beautiful methodology from Pentest Book and my 2nd dummy account and started checking for OAuth vulnerabilities, but was not able to find any!

But Hey!! The basic vulnerability check was forgotten. I instantly tried to create an OAuth account using my 1st dummy account and Boom, I was able to create 2 accounts using the same email ID.

Account Created using Email Signup
OAUTH login using same email
Misconfigured Oauth to Pre Account Takeover

To summarize the entire procedure the following steps were performed:

Visit the website and click on Sign Up.
Create an account using an unregistered victim email (say test@gmail.com)
Create another account using the OAuth mechanism and using the same OAuth account.

Impact:
The account created using email and password should get invalidated but it does not which means the attacker can still log in using the credentials he used while creating the account using email leading to pre-account takeover.

Perfect! I got one, let's hunt for more! This time my eyes caught the forget password functionality.

The password reset mechanism was as follows:

The user enters his email.
A 6-digit OTP is generated and sent to the email of the user
The user sets a new password.

Great, let's try for Authentication Bypass and check if we are able to change the victim’s password. So I entered my email and requested an OTP, entered the wrong OTP, and captured the response and tried for response manipulation but no luck.

Get TheBountyBox’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But my eye caught that the application was using ajax to perform password reset .

AJAX allows web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes.

So here’s what I did :

Go to Sign in page and click on forgot password
Enter attackers email (i.e my email say attacker@gmail.com )
Now enter the correct OTP received on attacker@gmail.com and Capture the Response and save it .
You will be redirected to set new password page but DONT SET THE PASSWORD instead Again go to Sign in page and click on forgot password
Enter victims email i.e. victim@gmail.com ( in our case it was aadesh004@protonmail.com )
Press enter or click to view image in full size
Enter Victim Email

6. Enter random OTP i.e. 000000 and Intercept the request using burp and Do intercept > Response to this request

Enter Random OTP

7. IN THE RESPONSE MANIPULATE THE RESPONSE TO :{“successTextKey”:”success”,”errors”:null}

Press enter or click to view image in full size
Generated Response
Press enter or click to view image in full size
Response Manipulation

8. Forward the request and You will be redirected to Set new password . This time Set the password and boom ACCOUNT TAKEOVER .

Set New Password
Press enter or click to view image in full size
Account Takeover

We hope that you enjoyed this article! Do let us know your stories about misconfigurations!

Happy Hunting!

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

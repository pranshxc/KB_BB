---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-15_how-i-bypassed-2-factor-authentication.md
original_filename: 2019-10-15_how-i-bypassed-2-factor-authentication.md
title: How I bypassed 2 Factor Authentication
category: documents
detected_topics:
- mfa
- rate-limit
- command-injection
- otp
- api-security
tags:
- imported
- documents
- mfa
- rate-limit
- command-injection
- otp
- api-security
language: en
raw_sha256: 6b311dc00b735b273d28da94869dfd21f44da250a19aa92c52f8672dba76464e
text_sha256: 03e7a010914cedc30c633e67bd463afcaa7e818e3b2f3bef79c55354e25f22c3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed 2 Factor Authentication

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-15_how-i-bypassed-2-factor-authentication.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6b311dc00b735b273d28da94869dfd21f44da250a19aa92c52f8672dba76464e`
- Text SHA256: `03e7a010914cedc30c633e67bd463afcaa7e818e3b2f3bef79c55354e25f22c3`


## Content

---
title: "How I bypassed 2 Factor Authentication"
page_title: "HOW I BYPASSED 2 FACTOR AUTHENTICATION | by HEMANT SINGH MANRAL | Medium"
url: "https://medium.com/@manralhemant10/how-i-bypassed-2-factor-authentication-899750421331"
authors: ["Hemant Singh Manral"]
bugs: ["2FA / MFA bypass"]
bounty: "250"
publication_date: "2019-10-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4987
scraped_via: "browseros"
---

# How I bypassed 2 Factor Authentication

HOW I BYPASSED 2 FACTOR AUTHENTICATION
HEMANT SINGH MANRAL
Follow
3 min read
·
Oct 15, 2019

171

INTRODUCTION:

Hi readers, I am HEMANT SINGH MANRAL a bug hunter from India.

This is my first write up so forgive my mistakes.

I am not revealing the name of the website, we will be assuming it as example.com

Method used by example.com for 2fa:

->There were two option two implement 2fa:-

1) Authenticator App

2) YubiKey OTP

Background:

Nothing interesting yet, at least for me, but then i saw an option to add recovery method either by mail or phone number this thing was provided so that in case we are not able to use Authentication app code for 2fa than we can have an alternative.

so when we use this alternative option it sends a 6 digit string to our phone number, first thing which comes to mind is brute forcing, a 6 digit code, which was valid for long time, no rate limiting everything set what else we want but the problem was this 6 digit code was a STRING i.e. a combination of alphabets and number, brute forcing this would take too much time and would have been rejected.

So i decided to go for some other way,

it’s time for burpsuite to get into this…:)

The way i approached:

1) I intercepted the recovery code post request into burp suite, which was like

{“loginID”:”1fb4c5f5dcac4cb4faa22409f043effa”,”sendCodeTo”:6547296}

a interesting request , if you look at parameter “sendCodeTo” which by name tells for what purpose its being used, so i decided to test on this parameter

1st try:

By using same phone number I checked whether this parameter value is changing for every new request or not, it was remaining constant…hmmm that was interesting.

2nd try:

I changed my recovery phone number, captured the request for getting 2fa code to my device, again the same request with different value of parameter “sendCodeTo”

so above two try concluded that each phone number is being assigned a particular 7 digit value which is used to identify the phone number.

Assume following:

-> ‘A’ as one account having recovery phone number as ‘a’ and ‘B’ as another account having recovery phone number as ‘b’.

-> Which means that ‘a’ is being assigned a unique id let it be 1234567

-> And ‘b’ is also being assigned a unique id let it be 8901234

Get HEMANT SINGH MANRAL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2) I logged in with ‘A’ it asked for 2fa code i switched to alternative i.e. using phone number to get code

->captured the post request which was like

{“loginID”:”1fb4c5f5dcac4cb4faa22409f043effa”,”sendCodeTo”:1234567}

I changed the value of parameter “sendCodeTo” with the unique code assigned to ‘b’

so now the post request was like

{“loginID”:”1fb4c5f5dcac4cb4faa22409f043effa”,”sendCodeTo”:8901234}

Forwarded this, waited for a while but i didn’t get any code on ‘b’.

3) Now i changed phone number for account ‘A’ i.e. ‘a’ to some another phone number assume it to be ‘c’ and let unique id assigned to it be 5423147

So now scenario is like:

Account ‘A’ with phone number ‘c’(i.e. 5423147)

Account ‘B’ with phone number ‘b’(i.e. 8901234)

And.. ‘a’ is still having unique id 1234567

Now assume ‘B’ to be victims account and ‘A’ as attackers account

4) i logged in with account ‘B’ ->for 2fa used phone number->captured the request which was like:

{“loginID”:”1lc4d5e5dcbc4ce4ava12509f042ghfa”,”sendCodeTo”:8901234}

5) I Changed the value of parameter “sendCodeTo” 1234567, now the request was like

{“loginID”:”1lc4d5e5dcbc4ce4ava12509f042ghfa”,”sendCodeTo”:1234567}

6) forwarded this request and yes i got 2fa code on ‘a’ which was previously used by ‘A’ i.e. on attackers old number.

Disclosure:

1. I reported this bug on 15th September.

2. I got their reply that they have successfully reproduced the issue on 17th September

3. Company rewarded me with 250$ on 12th October

Thanks

Looking forward to share more blogs

Best Regards

Hemant Singh Manral

You can reach out me at : www.linkedin.com/in/hemant-singh-manral-7a33a6174
